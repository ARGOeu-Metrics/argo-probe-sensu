import math
import time

import requests


def unix_now():
    return math.floor(time.time())


class SensuException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Sensu:
    def __init__(self, url, token, namespace):
        self.url = url
        self.token = token
        self.namespace = namespace

    def _get_events(self):
        response = requests.get(
            f"{self.url}/api/core/v2/namespaces/{self.namespace}/events",
            headers={
                "Authorization": f"Key {self.token}",
                "Content-Type": "application/json"
            }
        )

        if response.ok:
            return response.json()

        else:
            message = (f"Error fetching events from Sensu API: "
                       f"{response.status_code} {response.reason}")

            try:
                message = f"{message}: {response.json()['message']}"

            except (ValueError, KeyError, TypeError):
                pass

            raise SensuException(message)

    def get_hostnames(self, metric):
        events = [
            item for item in self._get_events() if
            item["check"]["metadata"]["name"] == metric and
            item["entity"]["entity_class"] == "proxy" and
            int(item["check"]["status"]) == 0
        ]

        return sorted([
            item["entity"]["metadata"]["labels"]["hostname"] for item in events
        ])

    def get_last_ok(self, hostname, metric):
        try:
            event = [
                item for item in self._get_events() if
                item["check"]["metadata"]["name"] == metric and
                item["entity"]["metadata"]["labels"]["hostname"] == hostname
            ][0]

            last_ok = int(event["check"]["last_ok"])

            if last_ok == 0:
                return None

            else:
                return unix_now() - int(event["check"]["last_ok"])

        except IndexError:
            raise SensuException(f"Event {hostname}/{metric} does not exist")

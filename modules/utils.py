import signal


class timeout:
    def __init__(self, seconds=1, error_message="Timeout"):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)


class ServiceStatus:
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3

    def __init__(self):
        self._code = self.OK
        self._msg = ""

    def _set_status(self, status, msg):
        self._code = status
        self._msg = msg

    def set_ok(self, msg):
        self._set_status(status=self.OK, msg=f"OK - {msg}")

    def set_warning(self, msg):
        self._set_status(status=self.WARNING, msg=f"WARNING - {msg}")

    def set_critical(self, msg):
        self._set_status(status=self.CRITICAL, msg=f"CRITICAL - {msg}")

    def set_unknown(self, msg):
        self._set_status(status=self.UNKNOWN, msg=f"UNKNOWN - {msg}")

    def get_message(self):
        return self._msg

    def get_code(self):
        return self._code

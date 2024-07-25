# argo-probe-sensu

The package contains two internal probes used on Sensu. `gather_healthy_nodes` probe generates a file with hostnames that have OK status code for given metric check. The other probe, `check_sensu`, is used to check if certain checks have been run successfully given number of seconds in the past.

## Synopsis

### `gather_healthy_nodes` probe

The probe has five mandatory arguments and two optional arguments. Though optional ones are also mandatory, but have the default values set. The arguments are self-explanatory, and visible through probe's help:

```
# /usr/libexec/argo/probes/sensu/gather_healthy_nodes -h
usage: gather_healthy_nodes -u URL -k TOKEN -n NAMESPACE -m METRIC -f FILE
                            [-t TIMEOUT] [-U USER] [-h]

Probe that generates list of hostnames with a given service in status OK

  required arguments:

  -u URL, --url URL     Sensu API URL
  -k TOKEN, --token TOKEN
                        Sensu API token
  -n NAMESPACE, --namespace NAMESPACE
                        tenant's namespace
  -m METRIC, --metric METRIC
                        metric name for which hostnames are being generated
  -f FILE, --file FILE  full path to file into which the list of hostnames is
                        going to be stored

  optional arguments:

  -t TIMEOUT, --timeout TIMEOUT
                        time in seconds after which the probe will stop
                        execution and return CRITICAL (default: 30)
  -U USER, --user USER  owner of the file (default: sensu)
  -h, --help            show this help message and exit
```

Example execution of probe:

```
/usr/libexec/argo/probes/sensu/gather_healthy_nodes -t 120 -u https://sensu.argo.eu:8080 -n EGI -m eu.egi.SRM-All -f /var/lib/gridprobes/GoodSEs --token <SENSU_API_TOKEN>
OK - Successfully generated file with 79 hosts
```

### `check_sensu` probe

The probe has six mandatory arguments and `timeout` as technically optional argument, since it has a default value defined.  Probe that checks if the probe has been executed successfully in the given time interval (checking the service 'freshness')

```
# /usr/libexec/argo/probes/sensu/check_sensu -h
usage: Probe that checks if the probe has been executed successfully in the given time interval (checking the service 'freshness') -H HOSTNAME -u URL -k TOKEN -n NAMESPACE -m METRIC --interval INTERVAL
                                                                                                                                   [-t TIMEOUT] [-h]

  required arguments:

  -H HOSTNAME, --hostname HOSTNAME
                        hostname
  -u URL, --url URL     Sensu API URL
  -k TOKEN, --token TOKEN
                        Sensu API token
  -n NAMESPACE, --namespace NAMESPACE
                        tenant's namespace
  -m METRIC, --metric METRIC
                        name of the metric to check
  --interval INTERVAL   interval in seconds for which the metric status is checked

  optional arguments:

  -t TIMEOUT, --timeout TIMEOUT
                        time in seconds after which the probe will stop execution and return CRITICAL (default: 30)
  -h, --help            show this help message and exit
```

Example execution of probe:

```
# /usr/libexec/argo/probes/sensu/check_sensu -H sensu-agent-devel.cro-ngi.hr -t 30 -u https://sensu-devel.cro-ngi.hr:8080 -n tenant -m org.nordugrid.ARC-CE-monitor --interval 3600 --token <SENSU_API_TOKEN>
OK - Service sensu-agent-devel.cro-ngi.hr/org.nordugrid.ARC-CE-monitor is OK
```

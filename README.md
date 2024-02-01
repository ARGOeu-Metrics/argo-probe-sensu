# argo-probe-sensu

The package contains internal probe that generates a file with hostnames that have OK status code for given metric check.

## Synopsis

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

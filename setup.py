from distutils.core import setup

NAME = "argo-probe-sensu"


def get_ver():
    try:
        for line in open(f"{NAME}.spec"):
            if "Version:" in line:
                return line.split()[1]

    except IOError:
        raise SystemExit(1)


setup(
    name=NAME,
    version=get_ver(),
    author="SRCE",
    author_email="kzailac@srce.hr",
    description="ARGO probe that generates list of hostnames with a given "
                "service in status OK",
    url="https://github.com/ARGOeu-Metrics/argo-probe-sensu",
    package_dir={'argo_probe_sensu': 'modules'},
    packages=['argo_probe_sensu'],
    data_files=[
        ('/usr/libexec/argo/probes/sensu', ['src/gather_healthy_nodes'])
    ]
)

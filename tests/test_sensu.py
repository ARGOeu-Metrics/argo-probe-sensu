import unittest
from unittest import mock

from argo_probe_sensu.sensu import Sensu

mock_events = [
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/srm/srm_probe.py -H '
                       'atlandse.fis.puc.cl -t 400 -d -p eu.egi.SRM -s ops '
                       '--se-timeout 360 --voname ops -X /etc/sensu/certs/'
                       'userproxy.pem --ldap-url atlandsitebdii.fis.puc.cl ',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 3600,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'SRM__atlandse.fis.puc.cl',
                'SRM__atlasse.lnf.infn.it',
                'SRM__atlassrm-kit.gridka.de',
                'SRM__b2se.mel.coepp.org.au'
            ],
            'proxy_entity_name': 'SRM__atlandse.fis.puc.cl',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.eu_egi_srm_all == 'eu.egi.SRM-All'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 38.972341469,
            'executed': 1705412204,
            'history': [
                {'status': 0, 'executed': 1705369003},
                {'status': 0, 'executed': 1705369003},
                {'status': 0, 'executed': 1705369003}
            ],
            'issued': 1705412204,
            'output': "Jan 16 14:36:44 DEBUG core[19775]: Call sequence: "
                      "[(<function getSURLs at 0x7f4412b14230>, 'GetSURLs', "
                      "True), (<function metricVOLsDir at 0x7f4412b142a8>, "
                      "'VOLsDir', True), (<function metricVOPut at "
                      "0x7f4412b14320>, 'VOPut', True), (<function "
                      "metricVOLs at 0x7f4412b14398>, 'VOLs', True), "
                      "(<function metricVOGetTURLs at 0x7f4412b14410>, "
                      "'VOGetTurl', True), (<function metricVOGet at "
                      "0x7f4412b14488>, 'VOGet', True), (<function "
                      "metricVODel at 0x7f4412b14500>, 'VODel', True), "
                      "(<function metricVOAlll at 0x7f4412b14578>, 'VOAll', "
                      "False)]",
            'state': 'passing',
            'status': 0,
            'total_state_change': 0,
            'last_ok': 1705412204,
            'occurrences': 31,
            'occurrences_watermark': 31,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'eu.egi.SRM-All',
                'namespace': 'EGI',
                'annotations': {'attempts': '4'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'}]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['SRM__atlandse.fis.puc.cl'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'SRM__atlandse.fis.puc.cl',
                'namespace': 'EGI',
                'labels': {
                    'egi_storage_space_mon': 'egi.storage.space-mon',
                    'eu_egi_srm_all': 'eu.egi.SRM-All',
                    'hostname': 'atlandse.fis.puc.cl',
                    'service': 'SRM',
                    'site': 'ATLAND',
                    'site_bdii': 'atlandsitebdii.fis.puc.cl',
                    'srm2_port': '8446'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 55446,
        'timestamp': 1705412243
    },
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/srm/srm_probe.py -H '
                       'atlassrm-kit.gridka.de -t 400 -d -p eu.egi.SRM -s ops '
                       '--se-timeout 360 --voname ops -X /etc/sensu/certs/'
                       'userproxy.pem --ldap-url bdii-site-kit.gridka.de ',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 3600,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'SRM__atlandse.fis.puc.cl',
                'SRM__atlasse.lnf.infn.it',
                'SRM__atlassrm-kit.gridka.de',
                'SRM__b2se.mel.coepp.org.au'
            ],
            'proxy_entity_name': 'SRM__atlassrm-kit.gridka.de',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.eu_egi_srm_all == 'eu.egi.SRM-All'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 5.7436331880000004,
            'executed': 1705412204,
            'history': [
                {'status': 0, 'executed': 1705376203},
                {'status': 0, 'executed': 1705376203},
                {'status': 0, 'executed': 1705379804}
            ],
            'issued': 1705412204,
            'output': "Jan 16 14:36:44 DEBUG core[19784]: Call sequence: "
                      "[(<function getSURLs at 0x7fa896232230>, 'GetSURLs', "
                      "True), (<function metricVOLsDir at 0x7fa8962322a8>, "
                      "'VOLsDir', True), (<function metricVOPut at "
                      "0x7fa896232320>, 'VOPut', True), (<function metricVOLs "
                      "at 0x7fa896232398>, 'VOLs', True), (<function "
                      "metricVOGetTURLs at 0x7fa896232410>, 'VOGetTurl', True),"
                      " (<function metricVOGet at 0x7fa896232488>, 'VOGet', "
                      "True), (<function metricVODel at 0x7fa896232500>, "
                      "'VODel', True), (<function metricVOAlll at "
                      "0x7fa896232578>, 'VOAll', False)]",
            'state': 'passing',
            'status': 0,
            'total_state_change': 0,
            'last_ok': 1705412204,
            'occurrences': 424,
            'occurrences_watermark': 424,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'eu.egi.SRM-All',
                'namespace': 'EGI',
                'annotations': {'attempts': '4'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'
            }]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['SRM__atlassrm-kit.gridka.de'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'SRM__atlassrm-kit.gridka.de',
                'namespace': 'EGI',
                'labels': {
                    'egi_storage_space_mon': 'egi.storage.space-mon',
                    'eu_egi_srm_all': 'eu.egi.SRM-All',
                    'hostname': 'atlassrm-kit.gridka.de',
                    'info_url': 'atlassrm-kit.gridka.de',
                    'service': 'SRM',
                    'site': 'FZK-LCG2',
                    'site_bdii': 'bdii-site-kit.gridka.de',
                    'srm2_port': '8443'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 55454,
        'timestamp': 1705412210
    },
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/srm/srm_probe.py -H '
                       'atlasse.lnf.infn.it -t 400 -d -p eu.egi.SRM -s ops '
                       '--se-timeout 360 --voname ops -X /etc/sensu/certs/'
                       'userproxy.pem --ldap-url atlasbdii.lnf.infn.it ',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 3600,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'SRM__atlandse.fis.puc.cl',
                'SRM__atlasse.lnf.infn.it',
                'SRM__atlassrm-kit.gridka.de',
                'SRM__b2se.mel.coepp.org.au'
            ],
            'proxy_entity_name': 'SRM__atlasse.lnf.infn.it',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.eu_egi_srm_all == 'eu.egi.SRM-All'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 0.442126829,
            'executed': 1705412204,
            'history': [
                {'status': 2, 'executed': 1705397804},
                {'status': 2, 'executed': 1705397804},
                {'status': 2, 'executed': 1705397804},
                {'status': 2, 'executed': 1705397804}
            ],
            'issued': 1705412204,
            'output': "Jan 16 14:36:44 DEBUG core[19777]: Call sequence: "
                      "[(<function getSURLs at 0x7ff7f11f5230>, 'GetSURLs', "
                      "True), (<function metricVOLsDir at 0x7ff7f11f52a8>, "
                      "'VOLsDir', True), (<function metricVOPut at "
                      "0x7ff7f11f5320>, 'VOPut', True), (<function "
                      "metricVOLs at 0x7ff7f11f5398>, 'VOLs', True), "
                      "(<function metricVOGetTURLs at 0x7ff7f11f5410>, "
                      "'VOGetTurl', True), (<function metricVOGet at "
                      "0x7ff7f11f5488>, 'VOGet', True), (<function "
                      "metricVODel at 0x7ff7f11f5500>, 'VODel', True), "
                      "(<function metricVOAlll at 0x7ff7f11f5578>, 'VOAll', "
                      "False)]",
            'state': 'failing',
            'status': 2,
            'total_state_change': 0,
            'last_ok': 1705311404,
            'occurrences': 97,
            'occurrences_watermark': 97,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'eu.egi.SRM-All',
                'namespace': 'EGI',
                'annotations': {'attempts': '4'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'
            }]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['SRM__atlasse.lnf.infn.it'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'SRM__atlasse.lnf.infn.it',
                'namespace': 'EGI',
                'labels': {
                    'egi_storage_space_mon': 'egi.storage.space-mon',
                    'eu_egi_srm_all': 'eu.egi.SRM-All',
                    'hostname': 'atlasse.lnf.infn.it',
                    'service': 'SRM',
                    'site': 'INFN-FRASCATI',
                    'site_bdii': 'atlasbdii.lnf.infn.it',
                    'srm2_port': '8446'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 55447,
        'timestamp': 1705412205
    },
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/srm/srm_probe.py -H '
                       'b2se.mel.coepp.org.au -t 400 -d -p eu.egi.SRM -s ops '
                       '--se-timeout 360 --voname ops -X /etc/sensu/certs/'
                       'userproxy.pem --ldap-url t2site.mel.coepp.org.au ',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 3600,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'SRM__atlandse.fis.puc.cl',
                'SRM__atlasse.lnf.infn.it',
                'SRM__atlassrm-kit.gridka.de',
                'SRM__b2se.mel.coepp.org.au'
            ],
            'proxy_entity_name': 'SRM__b2se.mel.coepp.org.au',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.eu_egi_srm_all == 'eu.egi.SRM-All'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 2.030782328,
            'executed': 1705412204,
            'history': [
                {'status': 2, 'executed': 1705383404},
                {'status': 2, 'executed': 1705387004},
                {'status': 2, 'executed': 1705390604},
                {'status': 2, 'executed': 1705394204}
            ],
            'issued': 1705412204,
            'output': "Jan 16 14:36:45 DEBUG core[19785]: Call sequence: "
                      "[(<function getSURLs at 0x7fcfedb73230>, 'GetSURLs', "
                      "True), (<function metricVOLsDir at 0x7fcfedb732a8>, "
                      "'VOLsDir', True), (<function metricVOPut at "
                      "0x7fcfedb73320>, 'VOPut', True), (<function "
                      "metricVOLs at 0x7fcfedb73398>, 'VOLs', True), "
                      "(<function metricVOGetTURLs at 0x7fcfedb73410>, "
                      "'VOGetTurl', True), (<function metricVOGet at "
                      "0x7fcfedb73488>, 'VOGet', True), (<function "
                      "metricVODel at 0x7fcfedb73500>, 'VODel', True), "
                      "(<function metricVOAlll at 0x7fcfedb73578>, 'VOAll', "
                      "False)]",
            'state': 'failing',
            'status': 2,
            'total_state_change': 0,
            'last_ok': 0,
            'occurrences': 498,
            'occurrences_watermark': 590,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'eu.egi.SRM-All',
                'namespace': 'EGI',
                'annotations': {'attempts': '4'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'
            }]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['SRM__b2se.mel.coepp.org.au'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'SRM__b2se.mel.coepp.org.au',
                'namespace': 'EGI',
                'labels': {
                    'egi_storage_space_mon': 'egi.storage.space-mon',
                    'eu_egi_srm_all': 'eu.egi.SRM-All',
                    'hostname': 'b2se.mel.coepp.org.au',
                    'service': 'SRM',
                    'site': 'Australia-T2',
                    'site_bdii': 't2site.mel.coepp.org.au'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 55455,
        'timestamp': 1705412206
    },
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/check_ssl_cert -H '
                       'argo-mon-biomed.cro-ngi.hr -t 60 -w 30 -c 0 -N '
                       '--altnames --rootcert-dir /etc/grid-security/'
                       'certificates --rootcert-file /etc/pki/tls/certs/'
                       'ca-bundle.crt -C /etc/sensu/certs/robotcert.pem '
                       '-K /etc/sensu/certs/robotkey.pem',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 14400,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'argo.mon__argo-mon-biomed.cro-ngi.hr',
                'argo.mon__argo-mon-devel.egi.eu'
            ],
            'proxy_entity_name': 'argo.mon__argo-mon-biomed.cro-ngi.hr',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.generic_certificate_validity == "
                    "'generic.certificate.validity'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 2.9318630839999997,
            'executed': 1705400600,
            'history': [
                {'status': 0, 'executed': 1705299799},
                {'status': 0, 'executed': 1705299799},
                {'status': 0, 'executed': 1705314199},
                {'status': 0, 'executed': 1705314199}
            ],
            'issued': 1705400600,
            'output': "SSL_CERT OK - x509 certificate "
                      "'argo-mon-biomed.cro-ngi.hr' from 'SRCE CA' valid "
                      "until Oct 24 08:59:30 2024 GMT (expires in 281 days)"
                      "|days=281;30;0;;\n",
            'state': 'passing',
            'status': 0,
            'total_state_change': 0,
            'last_ok': 1705400600,
            'occurrences': 1488,
            'occurrences_watermark': 1488,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'generic.certificate.validity',
                'namespace': 'EGI',
                'annotations': {'attempts': '2'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'
            }]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['argo.mon__argo-mon-biomed.cro-ngi.hr'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'argo.mon__argo-mon-biomed.cro-ngi.hr',
                'namespace': 'EGI',
                'labels': {
                    'generic_certificate_validity':
                        'generic.certificate.validity',
                    'hostname': 'argo-mon-biomed.cro-ngi.hr',
                    'info_url': 'https://argo-mon-biomed.cro-ngi.hr',
                    'service': 'argo.mon',
                    'site': 'GRIDOPS-SAM'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 5651,
        'timestamp': 1705400603
    },
    {
        'check': {
            'command': '/usr/lib64/nagios/plugins/check_ssl_cert -H '
                       'argo-mon-devel.egi.eu -t 60 -w 30 -c 0 -N --altnames '
                       '--rootcert-dir /etc/grid-security/certificates '
                       '--rootcert-file /etc/pki/tls/certs/ca-bundle.crt '
                       '-C /etc/sensu/certs/robotcert.pem -K /etc/sensu/certs/'
                       'robotkey.pem',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 14400,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': [
                'argo.mon__argo-mon-biomed.cro-ngi.hr',
                'argo.mon__argo-mon-devel.egi.eu'
            ],
            'proxy_entity_name': 'argo.mon__argo-mon-devel.egi.eu',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'proxy_requests': {
                'entity_attributes': [
                    "entity.entity_class == 'proxy'",
                    "entity.labels.generic_certificate_validity == "
                    "'generic.certificate.validity'"
                ],
                'splay': False,
                'splay_coverage': 0
            },
            'round_robin': False,
            'duration': 3.802225814,
            'executed': 1705400600,
            'history': [
                {'status': 0, 'executed': 1705299799},
                {'status': 0, 'executed': 1705299799},
                {'status': 0, 'executed': 1705314199},
                {'status': 0, 'executed': 1705328599}
            ],
            'issued': 1705400600,
            'output': "SSL_CERT OK - x509 certificate 'argo-mon-devel.egi.eu' "
                      "from 'GEANT eScience SSL CA 4' valid until Jul  2 "
                      "23:59:59 2024 GMT (expires in 168 days)"
                      "|days=168;30;0;;\n",
            'state': 'passing',
            'status': 0,
            'total_state_change': 0,
            'last_ok': 1705400600,
            'occurrences': 149,
            'occurrences_watermark': 149,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'generic.certificate.validity',
                'namespace': 'EGI',
                'annotations': {'attempts': '2'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': '',
            'processed_by': 'sensu-agent-egi-devel.cro-ngi',
            'pipelines': [{
                'name': 'hard_state',
                'type': 'Pipeline',
                'api_version': 'core/v2'}]
        },
        'entity': {
            'entity_class': 'proxy',
            'subscriptions': ['argo.mon__argo-mon-devel.egi.eu'],
            'last_seen': 0,
            'deregister': False,
            'deregistration': {},
            'metadata': {
                'name': 'argo.mon__argo-mon-devel.egi.eu',
                'namespace': 'EGI',
                'labels': {
                    'generic_certificate_validity':
                        'generic.certificate.validity',
                    'hostname': 'argo-mon-devel.egi.eu',
                    'info_url': 'https://argo-mon-devel.egi.eu',
                    'service': 'argo.mon',
                    'site': 'GRIDOPS-SAM'
                }
            },
            'sensu_agent_version': ''
        },
        'id': 'xxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'hard_state',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 5654,
        'timestamp': 1705400604
    }
]


class MockResponse:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code
        self.reason = "BAD REQUEST"
        self.ok = False
        if str(status_code).startswith("2"):
            self.ok = True
            self.reason = "OK"

    def json(self):
        return self.data


class SensuTests(unittest.TestCase):
    def setUp(self):
        self.sensu = Sensu(
            url="https://sensu.example.com:8080",
            token="53n5u_t0k3n",
            namespace="TENANT"
        )

    @mock.patch("argo_probe_sensu.sensu.requests.get")
    def test_get_hostnames(self, mock_get):
        mock_get.return_value = MockResponse(mock_events, status_code=200)
        hostnames = self.sensu.get_hostnames(metric="eu.egi.SRM-All")
        mock_get.assert_called_once_with(
            "https://sensu.example.com:8080/api/core/v2/namespaces/TENANT/"
            "events",
            headers={
                "Authorization": "Key 53n5u_t0k3n",
                "Content-Type": "application/json"
            }
        )
        self.assertEqual(
            hostnames, ["atlandse.fis.puc.cl", "atlassrm-kit.gridka.de"]
        )

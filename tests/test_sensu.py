import unittest
from unittest import mock

from argo_probe_sensu.sensu import Sensu, SensuException

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
    },
    {
        'check': {
            'command': 'source /etc/sensu/secret_envs ; export $(cut -d= -f1 '
                       '/etc/sensu/secret_envs) ; /usr/libexec/argo/probes/'
                       'oidc/check-refresh-token-expiration -t 5 --token '
                       '$OIDC_REFRESH_TOKEN',
            'handlers': [],
            'high_flap_threshold': 0,
            'interval': 86400,
            'low_flap_threshold': 0,
            'publish': True,
            'runtime_assets': None,
            'subscriptions': ['internals'],
            'proxy_entity_name': '',
            'check_hooks': None,
            'stdin': False,
            'subdue': None,
            'ttl': 0,
            'timeout': 900,
            'round_robin': False,
            'duration': 0.147931253,
            'executed': 1705395865,
            'history': [
                {'status': 0, 'executed': 1705395865}
            ],
            'issued': 1705395865,
            'output': 'OK - Refresh token valid until Aug 01 2024 14:51:07\n',
            'state': 'passing',
            'status': 0,
            'total_state_change': 0,
            'last_ok': 1705395865,
            'occurrences': 1,
            'occurrences_watermark': 1,
            'output_metric_format': '',
            'output_metric_handlers': None,
            'env_vars': None,
            'metadata': {
                'name': 'argo.oidc.refresh-token-validity',
                'namespace': 'EGI',
                'annotations': {'attempts': '1'}
            },
            'secrets': None,
            'is_silenced': False,
            'scheduler': 'memory',
            'processed_by': 'sensu-agent-egi-arc-devel.cro-ngi',
            'pipelines': [{
                'name': 'reduce_alerts',
                'type': 'Pipeline',
                'api_version': 'core/v2'
            }]
        },
        'entity': {
            'entity_class': 'agent',
            'subscriptions': [
                'argo.mon__argo-mon-biomed.cro-ngi.hr',
                'argo.mon__argo-mon-devel.egi.eu',
                'SRM__atlandse.fis.puc.cl',
                'SRM__atlasse.lnf.infn.it',
                'SRM__atlassrm-kit.gridka.de',
                'SRM__b2se.mel.coepp.org.au',
                'internals'
            ],
            'last_seen': 1705395865,
            'deregister': False,
            'deregistration': {},
            'user': 'agent',
            'metadata': {
                'name': 'sensu-agent-egi-arc-devel.cro-ngi',
                'namespace': 'EGI',
                'labels': {
                    'hostname': 'sensu-agent-egi-arc-devel.cro-ngi',
                    'services': 'argo.sensu.internal'
                }
            },
            'sensu_agent_version': '6.7.1+oss_el7'
        },
        'id': 'xxxxx',
        'metadata': {'namespace': 'EGI'},
        'pipelines': [{
            'name': 'reduce_alerts',
            'type': 'Pipeline',
            'api_version': 'core/v2'
        }],
        'sequence': 1,
        'timestamp': 1705395865
    }
]


mock_events_freshness = [
    {
        "check": {
            "command": "/usr/lib64/nagios/plugins/check_arcce_monitor -O "
                       "service_suffix=-ops -O lfc_host=dummy -O se_host=dummy "
                       "--timeout 900 --command-file /var/nagios/rw/nagios.cmd "
                       "--how-invoked nagios --voms ops --user-proxy /etc/"
                       "sensu/certs/userproxy.pem",
            "handlers": [],
            "high_flap_threshold": 0,
            "interval": 1200,
            "low_flap_threshold": 0,
            "publish": True,
            "runtime_assets": None,
            "subscriptions": [
                "internals"
            ],
            "proxy_entity_name": "",
            "check_hooks": None,
            "stdin": False,
            "subdue": None,
            "ttl": 0,
            "timeout": 900,
            "round_robin": False,
            "duration": 0.146744673,
            "executed": 1720600488,
            "history": [
                {
                    "status": 0,
                    "executed": 1720587288
                },
                {
                    "status": 0,
                    "executed": 1720588488
                },
                {
                    "status": 0,
                    "executed": 1720589688
                },
                {
                    "status": 0,
                    "executed": 1720590888
                },
                {
                    "status": 0,
                    "executed": 1720592088
                },
                {
                    "status": 0,
                    "executed": 1720593288
                },
                {
                    "status": 0,
                    "executed": 1720594488
                },
                {
                    "status": 0,
                    "executed": 1720595688
                },
                {
                    "status": 0,
                    "executed": 1720596888
                },
                {
                    "status": 0,
                    "executed": 1720598088
                },
                {
                    "status": 0,
                    "executed": 1720599288
                },
                {
                    "status": 0,
                    "executed": 1720600488
                }
            ],
            "issued": 1720600488,
            "output": "No jobs to monitor since the working directory has not "
                      "yet been created.\n",
            "state": "passing",
            "status": 0,
            "total_state_change": 0,
            "last_ok": 1720600488,
            "occurrences": 1147,
            "occurrences_watermark": 1147,
            "output_metric_format": "",
            "output_metric_handlers": None,
            "env_vars": None,
            "metadata": {
                "name": "org.nordugrid.ARC-CE-monitor",
                "namespace": "egi",
                "labels": {
                    "tenants": "egi"
                },
                "annotations": {
                    "attempts": "8"
                }
            },
            "secrets": None,
            "is_silenced": False,
            "scheduler": "memory",
            "processed_by": "sensu-agent-egi-devel-el9.cro-ngi.hr",
            "pipelines": []
        },
        "entity": {
            "entity_class": "agent",
            "system": {
                "hostname": "sensu-agent-egi-devel-el9.cro-ngi.hr",
                "os": "linux",
                "platform": "rocky",
                "platform_family": "rhel",
                "platform_version": "9.4",
                "arch": "amd64",
                "libc_type": "glibc",
                "vm_system": "",
                "vm_role": "",
                "cloud_provider": "",
                "processes": None
            },
            "subscriptions": [
                "sub1",
                "sub2",
                "sub3",
                "sub4",
                "sub5",
                "sub6",
                "sub7",
                "sub8",
            ],
            "last_seen": 1720600488,
            "deregister": False,
            "deregistration": {},
            "user": "agent",
            "metadata": {
                "name": "sensu-agent-egi-devel-el9.cro-ngi.hr",
                "namespace": "egi",
                "labels": {
                    "hostname": "sensu-agent-egi-devel-el9.cro-ngi.hr",
                    "services": "argo.sensu.internal"
                }
            },
            "sensu_agent_version": "6.11.0+oss_"
        },
        "id": "787c3495-296e-4328-8850-2333293cccd0",
        "metadata": {
            "namespace": "egi"
        },
        "pipelines": None,
        "sequence": 435,
        "timestamp": 1720600489
    },
    {
        "check": {
            "command": "/usr/lib64/nagios/plugins/check_arcce_clean --timeout "
                       "600 --command-file /var/nagios/rw/nagios.cmd "
                       "--how-invoked nagios --voms ops --user-proxy /etc/"
                       "sensu/certs/userproxy.pem",
            "handlers": [],
            "high_flap_threshold": 0,
            "interval": 1200,
            "low_flap_threshold": 0,
            "publish": True,
            "runtime_assets": None,
            "subscriptions": [
                "internals"
            ],
            "proxy_entity_name": "",
            "check_hooks": None,
            "stdin": False,
            "subdue": None,
            "ttl": 0,
            "timeout": 900,
            "round_robin": False,
            "duration": 0.14313019,
            "executed": 1720600384,
            "history": [
                {
                    "status": 0,
                    "executed": 1720590784
                },
                {
                    "status": 0,
                    "executed": 1720591984
                },
                {
                    "status": 0,
                    "executed": 1720593184
                },
                {
                    "status": 0,
                    "executed": 1720594384
                },
                {
                    "status": 0,
                    "executed": 1720595584
                },
                {
                    "status": 0,
                    "executed": 1720596784
                },
                {
                    "status": 0,
                    "executed": 1720597984
                },
                {
                    "status": 0,
                    "executed": 1720599184
                },
                {
                    "status": 0,
                    "executed": 1720600384
                }
            ],
            "issued": 1720600384,
            "output": "No jobs to clean since the working directory has not "
                      "yet been created.\n",
            "state": "passing",
            "status": 0,
            "total_state_change": 0,
            "last_ok": 1720600384,
            "occurrences": 1144,
            "occurrences_watermark": 1144,
            "output_metric_format": "",
            "output_metric_handlers": None,
            "env_vars": None,
            "metadata": {
                "name": "org.nordugrid.ARC-CE-clean",
                "namespace": "egi",
                "labels": {
                    "tenants": "egi"
                },
                "annotations": {
                    "attempts": "4"
                }
            },
            "secrets": None,
            "is_silenced": False,
            "scheduler": "memory",
            "processed_by": "sensu-agent-egi2-devel-el9.cro-ngi.hr",
            "pipelines": []
        },
        "entity": {
            "entity_class": "agent",
            "system": {
                "hostname": "sensu-agent-egi2-devel-el9.cro-ngi.hr",
                "os": "linux",
                "platform": "rocky",
                "platform_family": "rhel",
                "platform_version": "9.4",
                "arch": "amd64",
                "libc_type": "glibc",
                "vm_system": "",
                "vm_role": "",
                "cloud_provider": "",
                "processes": None
            },
            "subscriptions": [
                "sub1",
                "sub2",
                "sub3"
            ],
            "last_seen": 1720600384,
            "deregister": False,
            "deregistration": {},
            "user": "agent",
            "metadata": {
                "name": "sensu-agent-egi2-devel-el9.cro-ngi.hr",
                "namespace": "egi",
                "labels": {
                    "hostname": "sensu-agent-egi2-devel-el9.cro-ngi.hr",
                    "services": "argo.sensu.internal"
                }
            },
            "sensu_agent_version": "6.11.0+oss_"
        },
        "id": "5bbc7474-fec9-43e4-908e-50576cdd97c9",
        "metadata": {
          "namespace": "egi"
        },
        "pipelines": None,
        "sequence": 434,
        "timestamp": 1720600385
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

        elif str(status_code).startswith("4"):
            self.reason = "BAD REQUEST"

        else:
            self.reason = "SERVER ERROR"

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

    @mock.patch("argo_probe_sensu.sensu.requests.get")
    def test_get_hostnames_with_exception_without_message(self, mock_get):
        mock_get.return_value = MockResponse(None, status_code=500)
        with self.assertRaises(SensuException) as context:
            self.sensu.get_hostnames(metric="eu.egi.SRM-All")

        self.assertEqual(
            context.exception.__str__(),
            "Error fetching events from Sensu API: 500 SERVER ERROR"
        )

    @mock.patch("argo_probe_sensu.sensu.requests.get")
    def test_get_hostnames_with_exception_with_message(self, mock_get):
        mock_get.return_value = MockResponse(
            {"message": "Something went wrong"}, status_code=400
        )
        with self.assertRaises(SensuException) as context:
            self.sensu.get_hostnames(metric="eu.egi.SRM-All")

        self.assertEqual(
            context.exception.__str__(),
            "Error fetching events from Sensu API: 400 BAD REQUEST: "
            "Something went wrong"
        )

    @mock.patch("argo_probe_sensu.sensu.unix_now")
    @mock.patch("argo_probe_sensu.sensu.requests.get")
    def test_get_last_ok(self, mock_get, mock_now):
        mock_get.return_value = MockResponse(
            mock_events_freshness, status_code=200
        )
        mock_now.return_value = 1720603196
        freshness = self.sensu.get_last_ok(
            hostname="sensu-agent-egi2-devel-el9.cro-ngi.hr",
            metric="org.nordugrid.ARC-CE-clean"
        )
        self.assertEqual(freshness, 2812)

    @mock.patch("argo_probe_sensu.sensu.unix_now")
    @mock.patch("argo_probe_sensu.sensu.requests.get")
    def test_get_last_ok_if_no_event(self, mock_get, mock_now):
        mock_get.return_value = MockResponse(
            mock_events_freshness, status_code=200
        )
        mock_now.return_value = 1720603196
        with self.assertRaises(SensuException) as context:
            self.sensu.get_last_ok(
                hostname="hostname.example.com",
                metric="org.nordugrid.ARC-CE-clean"
            )
        self.assertEqual(
            context.exception.__str__(),
            "Event hostname.example.com/org.nordugrid.ARC-CE-clean does not "
            "exist"
        )


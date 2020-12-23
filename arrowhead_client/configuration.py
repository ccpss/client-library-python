from arrowhead_client.system import ArrowheadSystem
_default_address = '127.0.0.1'

default_config = {
    'core_service': {
        'service_registry':
            ArrowheadSystem(
                    'service_registry',
                    _default_address,
                    8443, ),
        'orchestrator':
            ArrowheadSystem(
                    'orchestrator',
                    _default_address,
                    8441, ),
        'authorization':
            ArrowheadSystem(
                    'authorization',
                    _default_address,
                    8445, ),
        'eventhandler':
            ArrowheadSystem(
                    'eventhandler',
                    _default_address,
                    8455, ),
        'gatekeeper':
            ArrowheadSystem(
                    'gatekeeper',
                    _default_address,
                    8449, ),
        'gateway':
            ArrowheadSystem(
                    'gatekeeper',
                    _default_address,
                    8453, )
    },
    'certificate authority': '',
}

config = default_config

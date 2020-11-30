from typing import Dict
from arrowhead_client.service import Service

_http_core_services: Dict[str, Service] = {
    'register': Service(
            service_definition='register',
            service_uri='serviceregistry/register',
            interface='HTTP-SECURE-JSON', ),
    'query': Service(
            service_definition='query',
            service_uri='serviceregistry/query',
            interface='HTTP-SECURE-JSON', ),
    'unregister': Service(
            service_definition='unregister',
            service_uri='serviceregistry/unregister',
            interface='HTTP-SECURE-TEXT', ),
    'orchestration-provided_service': Service(
            service_definition='orchestration-provided_service',
            service_uri='orchestrator/orchestration',
            interface='HTTP-SECURE-JSON', ),
    'publickey': Service(
            service_definition='publickey',
            service_uri='authorization/publickey',
            interface='HTTP-SECURE-TEXT', ),
}


def core_service(service_defintion: str) -> Service:
    # TODO: Why are the services being copied?
    core_service_instance = _http_core_services.get(service_defintion, None)

    if not core_service_instance:
        raise ValueError(f'Core provided_service \'{service_defintion}\' not found, '
                         f'available core services are {list(_http_core_services.keys())}')

    return core_service_instance
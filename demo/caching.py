import os

def caching_config():
    service_name = os.getenv('CACHING_SERVICE_NAME', '').upper().replace('-', '_')
    if not service_name:
        return None

    host = os.getenv('{}_SERVICE_HOST'.format(service_name))
    port = os.getenv('{}_SERVICE_PORT'.format(service_name))
    
    return {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '{}:{}'.format(host, port),
    }

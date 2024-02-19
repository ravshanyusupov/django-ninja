from heplers.import_folder import import_from_folder

API_DIRECTORY = 'api/v1/'


def generate_api(api):
    modules = import_from_folder(API_DIRECTORY)
    for module in modules:
        endpoint_instance = module['path_name']
        handler_instance = module['handler']

        if endpoint_instance.split('/')[-1] == 'create':
            api.post(endpoint_instance, tags='user')(handler_instance.handler)
        elif endpoint_instance.split('/')[-1] == 'get' or endpoint_instance.split('/')[-1] == 'list':
            api.get(endpoint_instance)(handler_instance.handler)
        elif endpoint_instance.split('/')[-1] == 'put' or endpoint_instance.split('/')[-1] == 'update':
            api.put(endpoint_instance)(handler_instance.handler)
        elif endpoint_instance.split('/')[-1] == 'patch':
            api.patch(endpoint_instance)(handler_instance.handler)
        elif endpoint_instance.split('/')[-1] == 'delete':
            api.delete(endpoint_instance)(handler_instance.handler)

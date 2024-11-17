import sys


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    dict_int = {'type': type_obj,
                'attributes': attributes,
                'methods': methods,
                'module': module}

    return dict_int


number_info = introspection_info(42)
print(number_info)

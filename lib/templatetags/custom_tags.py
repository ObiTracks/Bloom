import json
from django import template
from django.forms.models import model_to_dict

register = template.Library()

@register.filter
def get_model_name(obj):
# def get_model_name(obj, arg):
    model_name = type(obj).__name__
    return model_name

@register.filter
def serialize_model_to_dict(obj):
# def get_model_name(obj, arg):
    print(obj)
    dict_obj = model_to_dict(obj)
    data = json.dumps(str(dict_obj))
    # data = dict_obj
    print(data)
    return data



from django import template
register = template.Library()

@register.simple_tag
def dict_get(the_dict, key):
  return the_dict.get(key, '')

@register.filter
def get(mapping, key):
  return mapping.get(key, '')
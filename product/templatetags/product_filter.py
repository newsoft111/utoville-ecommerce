from django import template

register = template.Library()


@register.filter
def options_create(data):
    final_data = ''
    count = 1
    for key, value in data.items():
        if count == len(data):
            final_data += '{}(+{}) '.format(key, value)
        else:
            final_data += '{}(+{}), '.format(key, value)
        count = count+1
    return final_data

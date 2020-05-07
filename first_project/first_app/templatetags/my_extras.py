from django import template

register = template.Library()

#a Decorator replaces the need for a register.filter(value, arg) function
#AND IT LOOKS NEATER

@register.filter(name="cut")
def cut(value, arg):
    """
    This cuts out all values of arg from the string!
    :param value: self
    :param arg: to_be_removed
    :return: new_string
    """

    return value.replace(arg, "")

# register.filter('cut', cut)
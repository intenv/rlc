from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from jinja2 import Environment, FileSystemLoader
from ansible import errors


def extend_join(value, d=u'', p=u'', s=u''):
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()


    """Return a string which is the concatenation of the strings in the
    sequence. The separator between elements is an empty string per
    default, and concatenate prefix an suffix for each item:

    .. sourcecode:: jinja

        {{ ['host1', 'host2', 'host3']|join(';', 'http://', ':800') }}
            -> http://host1:800;http://host1:800;http://host1:800

    """
    value = list(value)
    display.vvvv(str(value))
    for idx, item in enumerate(value):
        display.vvvv(str(item))
        value[idx] = str(p + item + s)
    display.vvvv(str(value))
    return d.join(value)


class FilterModule(object):
    ''' adds extend_join filter '''
    def filters(self):
        return {

        # filter map
        'extend_join': extend_join

        }

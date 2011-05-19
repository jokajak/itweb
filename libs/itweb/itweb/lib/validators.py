# turbogears imports

# third party imports
from formencode import *
import formencode
from pylons.i18n import ugettext as _

# project specific imports
import itweb.lib.ipaddr as ipaddr

class IPAddress(FancyValidator):
    messages = {
            'bad ip': '%s does not appear to be an IPv4 or IPv6'
            ' address',
        }
    def _to_python(self, value, state):
        val = None
        # remove spaces from the string
        try:
            val = value.strip()
        except AttributeError:
            pass
        # try converting it to a number first
        try:
            if val:
                val = long(val)
            else:
                val = long(value)
        except ValueError:
            pass
        # see if val is defined and try to convert it
        if not val:
            val = value
        try:
            ip = ipaddr.IPAddress(val)
        except ValueError:
            raise Invalid(self.message('bad ip', state, address=value), value, state)
        return ip

def validate_network(form_values, state, validator):
    netaddr = form_values.get('netaddr')
    prefix = form_values.get('prefix')
    net_value = "%s/%s" % (netaddr, prefix)
    try:
        network = ipaddr.IPNetwork(net_value)
    except ValueError:
        return {'netaddr': "%s does not appear to be an IPv4 or IPv6 network" % net_value}

class Network(formencode.Schema):
    allow_extra_fields = True
    netaddr = ipaddr.IPAddress
    prefix = validators.Regex(r'^[.0-9:]+$')
    notes = validators.MaxLength(255)
    chained_validators = [ schema.SimpleFormValidator(validate_network) ]

# originally from formencode.validators
# modified to support dashes as separators
class MACAddress(FancyValidator):
    """
    Formencode validator to check whether a string is a correct hardware
    (MAC) address.

    Examples::

        >>> mac = MACAddress()
        >>> mac.to_python('aa:bb:cc:dd:ee:ff')
        'aabbccddeeff'
        >>> mac.to_python('aa:bb:cc:dd:ee:ff:e')
        Traceback (most recent call last):
            ...
        Invalid: A MAC address must contain 12 digits and A-F; the value you gave has 13 characters
        >>> mac.to_python('aa:bb:cc:dd:ee:fx')
        Traceback (most recent call last):
            ...
        Invalid: MAC addresses may only contain 0-9 and A-F (and optionally :), not 'x'
        >>> MACAddress(add_colons=True).to_python('aabbccddeeff')
        'aa:bb:cc:dd:ee:ff'
    """

    strip=True
    valid_characters = '0123456789abcdefABCDEF'
    add_colons = False

    messages = {
        'bad_length': _(u'A MAC address must contain 12 digits and A-F; the value you gave has %(length)s characters'),
        'bad_character': _(u'MAC addresses may only contain 0-9 and A-F (and optionally :), not %(char)r'),
        }

    def _to_python(self, value, state):
        address = value.replace(':','') # remove colons
        address = value.replace('-','') # remove dashes
        address = address.lower()
        if len(address)!=12:
            raise Invalid(self.message("bad_length", state, length=len(address)), address, state)
        for char in address:
            if char not in self.valid_characters:
                raise Invalid(self.message("bad_character", state, char=char), address, state)
        if self.add_colons:
            address = '%s:%s:%s:%s:%s:%s' % (
                address[0:2], address[2:4], address[4:6],
                address[6:8], address[8:10], address[10:12])
        return address

    _from_python = _to_python

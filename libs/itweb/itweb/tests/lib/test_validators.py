from formencode.validators import Invalid
from itweb.lib.validators import IPAddress
import itweb.lib.ipaddr as ipaddr

def validate(validator, value):
    try:
        return validator.to_python(value)
        return None
    except Invalid, e:
        return e.unpack_errors()

def test_ipaddress():
    ip_validator = IPAddress()
    messages = ip_validator.message
    assert ip_validator.to_python("10.1.1.1") == ipaddr.IPAddress("10.1.1.1")
    assert ip_validator.to_python(3232235777) == ipaddr.IPAddress("192.168.1.1")
    assert validate(ip_validator, "x") == messages('bad ip', None, address='x')
    assert validate(ip_validator, "300.1.1.1") == messages('bad ip', None, address='300.1.1.1')
    assert validate(ip_validator, "300.1.1.1") == messages('bad ip', None, address='300.1.1.1')

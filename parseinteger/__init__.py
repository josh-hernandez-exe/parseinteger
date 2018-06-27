import sys
import string

import six

_BASE_CLASS = int
if sys.version_info < (3,0,0):
    _BASE_CLASS = long

class BaseBigIntegerException(Exception):
    pass

class NegativeRadixException(BaseBigIntegerException):
    pass

class RadixToLargeException(BaseBigIntegerException):
    pass

class StringNotMappedException(BaseBigIntegerException):
    pass

def _call_initialize(klass):
    """Call `_initialize` when the class is created"""
    klass._initialize()
    return klass

@_call_initialize
class Integer(_BASE_CLASS):
    _alphabet = list("".join([
        string.digits,
        string.ascii_lowercase,
        string.ascii_uppercase,
    ]))
    _new_digit_format="<{}>"
    _mapping = None

    @classmethod
    def _initialize(klass):
        klass._mapping = {v:k for k,v in enumerate(klass._alphabet)}

    @classmethod
    def _create_alphabet(klass, radix=10):
        if not isinstance(radix, six.integer_types):
            raise TypeError("Expected type 'int' for parameter 'radix', got '{}' instead.".format(radix))
        if radix < 0: raise NegativeRadixException()
        if radix <= len(klass._alphabet): return klass._alphabet

        for ii in range(len(klass._alphabet), radix):
            klass._alphabet.append(klass._new_digit_format.format(ii))

        return klass._alphabet

    @classmethod
    def _create_mapping(klass, radix=10):
        if not isinstance(radix, six.integer_types):
            raise TypeError("Expected type 'int' for parameter 'radix', got '{}' instead.".format(radix))
        if radix < 0: raise NegativeRadixException()
        if radix <= len(klass._mapping): return klass._mapping

        for ii in range(len(klass._mapping), radix):
            kk = klass._new_digit_format.format(ii)
            klass._mapping[kk] = ii

        return klass._mapping

    def to_string(self,radix=10,alphabet=None):
        alphabet = alphabet or self._create_alphabet(radix)

        if not isinstance(radix, six.integer_types):
            raise TypeError("Expected type 'int' for parameter 'radix', got '{}' instead.".format(radix))
        if radix < 0: raise NegativeRadixException()
        if radix > len(alphabet): raise RadixToLargeException()

        rep = []
        cur_integer = self
        while cur_integer > 0:
            digit = cur_integer % radix
            rep.append(alphabet[digit])
            cur_integer//=radix

        return "".join(reversed(rep))

    @classmethod
    def from_string(klass,string,radix=10,mapping=None):
        mapping = mapping or klass._create_mapping(radix)

        if not isinstance(string, six.string_types):
            raise TypeError("Expected type 'str' for parameter 'string', got '{}' instead.".format(string))
        if not isinstance(radix, six.integer_types):
            raise TypeError("Expected type 'int' for parameter 'radix', got '{}' instead.".format(radix))
        if radix < 0: raise NegativeRadixException()

        if not isinstance(mapping,(list,tuple,dict)):
            raise TypeError()

        if isinstance(mapping,(list,tuple)) and not all(isinstance(v,six.integer_types) for v in mapping):
            raise TypeError()
        elif isinstance(mapping,dict) and not all(isinstance(v,six.integer_types) for v in mapping.values()):
            raise TypeError()

        cur_integer = 0
        base_pow = 1
        for char in reversed(string):
            if char not in mapping: raise StringNotMappedException()
            cur_integer += base_pow * mapping[char]
            base_pow *= radix

        return klass(cur_integer)

__all__ = [
    "Integer",
]

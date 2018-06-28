# parseinteger
Parse Integer in any base and convert them into any other base.

# Example

```python
from parseinteger import Integer

# subclasses long
Integer(256).to_string(16)# '100'

# or from a string
Integer.from_string('akdshfk8t3984q8734yx68743y5n3879xqnyxfhuinh389n187x3y5n', 62).to_string(16)
# '1dc00552daa21cfd42411af7c1be830d89ff4249ff249aca962efa46ec4b867000ba948009560cdc6d'

# Can do bases beyound the alphanumeric charater per digit
xx = Integer(1234567890).to_string(128) # '4<76><88>5<82>'
Integer.from_string(xx,128) # 1234567890 (base 10)
```

You can also change the alphabet if you wanted

```python
from parseinteger import Integer

Integer("FFFF", 16).to_string(10) # 65535

Integer._alphabet = list(reversed(Integer._alphabet))
Integer._initialize() # re-initalize internal mapping, for converting strings to integers
Integer(65535).to_string(10) # 'TUUWU'

Integer.from_string("TUUWU", 10) # 65535
```

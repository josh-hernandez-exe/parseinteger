# parseinteger
Parse Integer in any base and convert them into any other base.

# Example

```python
from parseinteger import Integer

# subclasses long
Integer(256).to_string(16)

# or from a string
Integer.from_string('akdshfk8t3984q8734yx68743y5n3879xqnyxfhuinh389n187x3y5n', 62).to_string(16)
```

You can also change the alphabet if you wanted

```python
from parseinteger import Integer

Integer("FFFF", 16).to_string(10) # displays 65535

Integer._alphabet = list(reversed(Integer._alphabet))
Integer._initialize() # re-initalize internal mapping, for converting strings to integers
Integer(65535).to_string(10) # displays TUUWU

Integer.from_string("TUUWU", 10) # displays 65535
```

# Memory

Key notes:

- Memory: Is a big array of bytes
- Variable: A human readable name for the index in memory bytes array. We can also call it "address"

Getting real address value: In C, we can use operator `&`

Assignment: The size_of_addr function accepts a long long (a potentially very large integer) as input and returns the size of its address.

There's a bug! Memory addresses in Sneklang should always be 4 bytes long...

Fix the function so that it returns the size of i's address, not value.

```c
#include "snek.h"

unsigned long size_of_addr(long long i){
  unsigned long sizeof_snek_version = sizeof(i);
  return sizeof_snek_version;
}
```

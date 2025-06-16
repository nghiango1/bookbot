# C strings

C string is any number of characters that is terminated by a null character.

- Which lead to `printf("%s", pointer)` can lead to a lot of garbage data being print (which also leak memory and lead to data lost/stolen bug)
- A lot of builtin function using this `\0` terminate instead of a real string length property, which lead to a lot of security issue

Assignment: Complete `concat_strings` function. It should append str2 to the end of str1 in place

Answer:
```c
#include "exercise.h"

void concat_strings(char *str1, const char *str2) {
  int i = 0;
  for (; str1[i] != 0; i ++);
  for (int j = 0; str2[j] != 0; j ++) {
    str1[i+j] = str2[j];
    str1[i+j+1] = 0;
  }
}
```

# C String Library

The C standard library provides a comprehensive set of functions to manipulate strings in the `<string.h>` header file. Two interesting function here are:

- `strstr`: Finds the first occurrence of a substring in a string.

    ```c
    char str[] = "Hello World";
    char *pos = strstr(str, "World");
    // pos points to "World" in "Hello World"
    ```

- `strchr`: Finds the first occurrence of a character in a string.

    ```c
    char str[] = "Hello";
    char *pos = strchr(str, 'l');
    // pos points to the first 'l' in "Hello"
    ```

Assignment: Complete the smart_append function. It appends a src string to a dest TextBuffer struct.

It's called a "smart" append because the destination buffer is a fixed 64 bytes, and it:

- Checks for available space before appending.
- Appends as much as possible if there's not enough space.
- Always ensures the buffer remains null-terminated.
- Returns a status indicating whether the full append was possible.

My answer:
```c
#include <string.h>
#include "exercise.h"

#define MAX_SIZE 64

int smart_append(TextBuffer* dest, const char* src) {
  if (dest == 0 || src == 0) {
    return 1;
  }

  size_t src_length = strlen(src);

  size_t remain_dest_length = MAX_SIZE - (dest->length + 1);

  if (src_length > remain_dest_length) {
    strncat(dest->buffer, src, remain_dest_length);
    dest->length = MAX_SIZE - 1;
    return 1;
  }
  else {
    strcat(dest->buffer, src);
    dest->length += src_length;
    return 0;
  }
  
  return 0;
}
```

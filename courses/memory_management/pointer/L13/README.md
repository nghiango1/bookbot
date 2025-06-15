# Arrays Decay to Pointers

It mean array name become a pointer to the first element of the array. It happend in specific senario:

- When array used in expressions containing pointer
- And when they are passed to function

When they don't:

- `sizeof` Operator: Returns the size of the entire array (e.g., `sizeof(arr)`), not just the size of a pointer.
- `&` Operator Taking the address of an array with &arr gives you a pointer to the whole array, not just the first element. The type of `&arr` is a pointer to the array type, e.g., `int (*)[5]` for an int array with 5 elements.
- Initialization: When an array is declared and initialized, it is fully allocated in memory and does not decay to a pointer.

> The `&` thing is quite interesting

## Assignment

On lines 12 and 13 it prints the size of the array and the length of the array.
Complete the `core_utils_func` function to print

```
sizeof core_utilization in core_utils_func: X
```

```c
#include <stdio.h>

void core_utils_func(int core_utilization[]) {
  // ?
}

// don't touch below this line

int main() {
  int core_utilization[] = {43, 67, 89, 92, 71, 43, 56, 12};
  int len = sizeof(core_utilization) / sizeof(core_utilization[0]);
  printf("sizeof core_utilization in main: %zu\n", sizeof(core_utilization));
  printf("len of core_utilization: %d\n", len);
  core_utils_func(core_utilization);
  return 0;
}
```

## Expected output

We can't implement the function to show the correct size of array, as

> ... due to the array decaying to a pointer, the reported size is the size of a pointer, not the size of the actual array.

```
sizeof core_utilization in main: 32
len of core_utilization: 8
sizeof core_utilization in core_utils_func: 4
```

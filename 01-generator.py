from typing import Iterator

# Generators are a type of coroutines. They are functions that has a state and can yield to return to the caller.
# They can resume operation afterward.
# Generators are also Iterators hence it's valid to define it's return type as Iterator
def even_numbers(n: int) -> Iterator[int]:
    for i in range(0, n, 2):
        yield i

# even_numbers_up_to_ten is a generator instance
even_numbers_up_to_ten = even_numbers(10)
print(even_numbers_up_to_ten)
# Run until yield is encountered
print(next(even_numbers_up_to_ten))
# Continue from the state the coroutine has been suspended
print(next(even_numbers_up_to_ten))

# This will print the remaining yielded elements
for i in even_numbers_up_to_ten:
    print(i)

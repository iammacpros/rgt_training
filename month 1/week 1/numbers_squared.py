def fibonacci_sequence(integer: int) -> list[int]:

    fib = [0, 1]

    for i in range(integer-2):

        new_num = fib[-1] + fib[-2]
        fib.append(new_num)


    return fib


list_of_numbers = fibonacci_sequence(20)
print(list_of_numbers)

def squared(numbers: list[int]) -> list[int]:
    return [number**2 for number in numbers]


print(squared(list_of_numbers))
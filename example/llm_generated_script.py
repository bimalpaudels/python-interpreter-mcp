# Script location .my_tool_sandbox/script.py

def fibonacci(n):
    """
    Generate a list of the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq


# Example usage
print(fibonacci(10))
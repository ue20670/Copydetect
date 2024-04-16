# ========================性能问题检测代码==================================
def fibonacci(n):
    """Recursive function to calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def main(times):
    # This loop causes a performance issue because the fibonacci function is
    # called repeatedly for the same values, leading to redundant calculations.
    for i in range(times):  # Increase this value to make the problem more pronounced
        print(f"Fibonacci of {i} is {fibonacci(i)}")

if __name__ == "__main__":
    main(100)
def perform_calculations(numbers):
    """
    This function performs numerical operations on a list of numbers.
    """

    # Option 1: Calculate the sum of squares of the numbers
    result = sum([num ** 2 for num in numbers])
    print("Sum of squares:", result)

    # Option 2: Calculate the factorial of each number
    # import math
    # result = [math.factorial(num) for num in numbers]
    # print("Factorials:", result)


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    perform_calculations(numbers)
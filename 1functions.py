
def adder(a, b):
    """Returns the sum of a and b."""
    return a + b

def multiplier(a, b):
    
    """Returns the product of a and b."""
    return a * b

def subtractor(a, b):
    """Returns the difference of a and b."""
    return a - b

if __name__ == "__main__":
    num1 = 10
    num2 = 5

    print("\nAddition:", adder(num1, num2))
    print("\nMultiplication:", multiplier(num1, num2))
    print("\nSubtraction:", subtractor(num1, num2))
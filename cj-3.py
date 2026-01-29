def f(x):
    """Returns the result of x^3 + 8."""
    return x**3 + 8

def main():
    # Call the function with x = 9
    val = 9
    result = f(val)
    
    # Print the result
    print(f"The result of f({val}) is: {result}")
    
    # Check if the result is larger than 27
    if result > 27:
        print("YAY!")

# Standard boilerplate to run the main function
if __name__ == "__main__":
    main()
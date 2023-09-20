# Decorators in Python

# A decorator is a design pattern in Python that allows a function to be extended or modified by wrapping it with additional code.

# Example 1: Creating a Function-Based Decorator

def my_decorator(func):
    def wrapper():
        """
        Wrapper function that adds behavior before and after function execution.
        """
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator  # Applying the decorator to the function
def my_function():
    """
    Function to be decorated.
    """
    print("Inside the function")


# Using the decorated function
my_function()

# Example 2: Function-Based Decorator with Arguments


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Wrapper function that repeats the decorated function execution.
            """
            print(f"Repeating {n} times:")
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)  # Applying the decorator with an argument
def greet(name):
    """
    Function to be decorated.
    """
    print(f"Hello, {name}!")


# Using the decorated function
greet("Alice")

# Example 3: Creating a Class-Based Decorator


class Logger:
    def __init__(self, func):
        """
        Initialize the decorator with the function to be decorated.
        """
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        Define the behavior to be added before and after function execution.
        """
        print("Before function execution")
        result = self.func(*args, **kwargs)
        print("After function execution")
        return result


@Logger  # Applying the class-based decorator to the function
def my_function_2():
    """
    Function to be decorated.
    """
    print("Inside the function")


# Using the decorated function
my_function_2()

# Explanation:

# Decorators in Python allow us to extend or modify the behavior of functions or methods without directly modifying their code.
# They provide a way to wrap additional functionality around the original function.

# Example 1 demonstrates creating a function-based decorator 'my_decorator' and applying it to 'my_function'.

# Example 2 shows a function-based decorator 'repeat' that takes an argument and can be applied to a function.

# Example 3 introduces a class-based decorator 'Logger' that achieves the same behavior as the function-based decorator.

# Class-based decorators achieve the same result by implementing the __init__ and __call__ methods.
# __init__ initializes the decorator with the function to be decorated, and __call__ defines the behavior before and after function execution.

# Decorators with classes provide more flexibility for managing state or additional functionality compared to function-based decorators.

# Related Functions:

# functools.wraps: A decorator for updating the attributes of the wrapper function to match the original function.
# This is important for preserving metadata and docstrings.

# functools.lru_cache: A decorator that caches the results of a function, improving performance for repeated calls with the same arguments.

# functools.singledispatch: A decorator that allows a function to have different implementations based on the type of the first argument.

# Decorators are a powerful tool in Python for extending or modifying the behavior of functions, making them more flexible and reusable.

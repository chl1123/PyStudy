# import functools
# import inspect
#
#
# def log_class_methods(cls):
#     """
#     This decorator will add logging to all non-abstract methods of a class except the __init__ method.
#     """
#     for attr_name, attr_value in cls.__dict__.items():
#         if callable(attr_value) and not (inspect.isabstract(attr_value) or isinstance(attr_value, (
#         staticmethod, classmethod)) or attr_name == '__init__'):
#             setattr(cls, attr_name, log_method_calls(attr_value))
#     return cls
#
#
# def log_method_calls(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         class_name = args[0].__class__.__name__ if args else ''
#         method_name = func.__name__
#
#         print(f"\n[Begin]|{class_name}.{method_name}")
#         result = func(*args, **kwargs)
#         print(f"[ End ]|{class_name}.{method_name}\n")
#         return result
#
#     return wrapper


# import functools
# import inspect
#
# def log_class_methods(cls):
#     """
#     This decorator will add logging to all non-abstract methods of a class except the __init__ method.
#     """
#     global indentation_level
#     indentation_level = 0
#
#     def log_method_calls(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             global indentation_level
#             class_name = args[0].__class__.__name__ if args else ''
#             method_name = func.__name__
#
#             indentation = '    ' * indentation_level
#             print(f"\n{indentation}[Begin]|{class_name}.{method_name}")
#             indentation_level += 1
#
#             result = func(*args, **kwargs)
#
#             indentation_level -= 1
#             print(f"{indentation}[ End ]|{class_name}.{method_name}\n")
#             return result
#
#         return wrapper
#
#     for attr_name, attr_value in cls.__dict__.items():
#         if callable(attr_value) and not (inspect.isabstract(attr_value) or isinstance(attr_value, (
#                 staticmethod, classmethod)) or attr_name == '__init__'):
#             setattr(cls, attr_name, log_method_calls(attr_value))
#     return cls

import functools
import inspect


def log_class_methods(cls):
    """
    This decorator will add logging to all non-abstract methods of a class except the __init__ method.
    """

    def log_method_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global level
            class_name = args[0].__class__.__name__ if args else ''
            method_name = func.__name__

            # Increment the level by 1 for each method call
            level += 1

            # Print the beginning of the method call with level number
            print("\033[31m", end="")
            print(f"\n{'    ' * (level - 1)}[{level}][Begin]|{class_name}.{method_name}", end="")
            print("\033[m")

            # Call the original method
            result = func(*args, **kwargs)

            print("\033[31m", end="")
            # Print the end of the method call with level number
            print(f"{'    ' * (level - 1)}[{level}][ End ]|{class_name}.{method_name}\033[m", end="")
            print("\033[m")

            # Decrement the level after the method call completes
            level -= 1

            return result

        return wrapper

    global level
    # Initialize the level counter
    level = 0

    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not (inspect.isabstract(attr_value) or isinstance(attr_value, (
                staticmethod, classmethod)) or attr_name == '__init__'):
            setattr(cls, attr_name, log_method_calls(attr_value))
    return cls

import functools


def my_decorator(func):
    functools.wraps(func)

    def run_func(*args, **kwargs):
        print("Doing something before running the function")

        func(*args, **kwargs)

        print("Doing something after running the function")

    return run_func


def decorator_with_params(*args_d, **kwargs_d):
    def another_decorator(func):
        functools.wraps(func)

        def run_func(*args, **kwargs):
            print("Doing something before running the function")
            print(args_d)

            func(*args, **kwargs)

            print(kwargs_d)
            print("Doing something after running the function")

        return run_func
    return another_decorator


@my_decorator
def one():
    print("First decorator")


@decorator_with_params()
def two():
    print("Another decorator")

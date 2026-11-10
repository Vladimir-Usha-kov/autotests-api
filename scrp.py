import time
from curses.ascii import isdigit
from functools import wraps
from ipaddress import summarize_address_range
from typing import Any, Type, Callable

from fixtures.courses import function_course


#
# # TASK 7
# def deprecated(warning):
#     def decor(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(warning)
#             return func(*args, **kwargs)
#         return wrapper
#     return decor
#
# @deprecated("use new_func instead")
# def old_func():
#     print("old")
# old_func()


# TASK 6
# def retry(times: int, exceptions: tuple = (Exception,), delay: float = 0.0):
#     def decor(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             last_exe = None
#             for attempt in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as exe:
#                     last_exe = exe
#                     if attempt < times - 1:
#                         time.sleep(delay)
#             raise last_exe
#         return wrapper
#     return decor
#
# @retry(times=3, exceptions=(ValueError,), delay=3)
# def unstable():
#     print("trying...")
#     raise ValueError("nope")
#
# try:
#     unstable()
# except ValueError as e:
#     print("failed:", e)


# def limit_calls(max_calls):
#     def decor(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             wrapper.count += 1
#             if wrapper.count > max_calls:
#                 raise RuntimeError
#             return func(*args, **kwargs)
#         wrapper.count = 0
#         return wrapper
#     return decor
#
# @limit_calls(2)
# def f():
#     print("ok")
#
# f()
# f()
# f()
#
# def log_method(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'[log] {func.__name__}, args={args}, kwargs={kwargs}')
#         return func(*args, **kwargs)
#     return wrapper
#
# class Calc:
#     @log_method
#     def add(self, a, b):
#         return a + b
#
#
# a = Calc()
# a.add(3, 1)

#
# def tag(arg=None):
#     def make_wrapper(func, level):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f'[{level}]')
#             return func(*args, **kwargs)
#         return wrapper
#
#     if callable(arg):
#         return make_wrapper(arg, 'INFO')
#       level = arg if arg is not None else 'INFO'
#     `def decor(func):
#         return make_wrapper(func, level)
#     return decor
#
#
# @tag
# def f1():
#     ...
#
# @tag("DEBUG")
# def g():
#     ...
#
# f1()
# g()

# def memoize(func):
#     cash = {}
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = (args, tuple(sorted(kwargs.items())))
#         if key in cash:
#             return cash[key]
#         result = func(*args, **kwargs)
#         cash[key] = result
#         return result
#     return wrapper
#
# @memoize
# def f(a, b):
#     print('Calculate')
#     return a + b
#
# print(f(a=1, b=2))
# print(f(a=1, b=2))
# print(f(a=1, b=2))
# print(f(5, 5))
# print(f(5, 5))
# print(f(5, 5))
# print(f(5, 5))
# print(f(5, 5))
# print(f(5, 5))
#
#
# s = {"a": 1, "b":2}
# print(tuple(sorted(s.items())))


# property
from string import digits, ascii_uppercase
#


# def limit_count(limit: int):
#     def wrapper(func: Callable):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             inner.count += 1
#             if inner.count > limit:
#                 raise RuntimeError(f'Функция {func.__name__} не может быть вызвана больше {limit} раз')
#             return func(*args, **kwargs)
#         inner.count = 0
#         return inner
#     return wrapper
#
# @limit_count(2)
# def f():
#     return 1
#
#
# f()
# f()

# from time import perf_counter
# from typing import Callable
# class Timer:
#     def __init__(self, func: Callable):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         res = self.func(*args, **kwargs)
#         end = perf_counter()
#         print(f'func {self.func.__name__} time called {end - start}')
#         return res
#
#     def calc(self, *args, **kwargs):
#         ...
#
# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# @Timer
# def fac(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr *= i
#     return pr


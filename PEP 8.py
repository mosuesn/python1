"""PEP 8 is the official style guide for Python code.

It recommends consistent, readable formatting so code is easier to scan and
maintain. Common conventions include:

- Use four spaces for each indentation level; do not mix tabs and spaces.
- Keep lines to about 79 characters (72 for comments and docstrings).
- Use ``snake_case`` for functions and variables, ``PascalCase`` for classes,
	and ``UPPER_CASE`` for constants.
- Put spaces around operators and after commas, but avoid extra spaces inside
	parentheses, brackets, or braces.
- Separate top-level functions and classes with two blank lines; use one blank
	line to separate methods inside a class.
- Write imports at the top of the file, usually grouping standard-library,
	third-party, and local imports separately.
- Add comments and docstrings when they clarify intent, and keep them accurate.

PEP 8 is a set of conventions rather than a requirement for program behavior.
Following it consistently improves readability; tools such as ``pycodestyle``
and formatters such as ``Black`` can help check or apply many of its rules.
"""

""" use four spaces for indentation"""
for i in range(5):
    print(i)  # four spaces

""" keep lines under 79 characters"""
product_price = 19.99
quantity = 3
shipping = 4.99
tax = 1.50
discount = 5.00
total_price = (
    product_price * 
    quantity + shipping + 
    tax - discount
    ) # use parentheses to break long lines

"""Use ``snake_case`` for functions and variables, ``PascalCase`` for classes,
	and ``UPPER_CASE`` for constants."""
apples = 5 # 
class Fruit:
    pass
PI = 3.14159
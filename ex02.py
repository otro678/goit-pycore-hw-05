from typing import Callable
import re

def generator_numbers(text: str):
    pattern = r'\d+\.\d+'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1020.12 як основний дохід, доповнений додатковими надходженнями 212.32 і 2.12 доларів."
print(f"Загальний дохід: {sum_profit(text, generator_numbers)}")
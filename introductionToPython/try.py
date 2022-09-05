from __future__ import annotations


def add(a: float, b: float) -> float | None:
    try:
        return a/ b
    except ZeroDivisionError:
        print("can't divide with zero")
        return None
    except (TypeError, NameError):
        print("Type error")


print(add(1, 0))
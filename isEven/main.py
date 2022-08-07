def isEven(value: int) -> bool:
    return int(bin(value)[-1]) == 0

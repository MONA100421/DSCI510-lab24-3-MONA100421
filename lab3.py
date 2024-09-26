import string

def compute_persistence(num: int) -> int:
    if not isinstance(num, int) or num < 0:
        raise Exception("Invalid input")

    if num < 10:
        return 0

    count = 0
    while num >= 10:
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        num = product
        count += 1

    return count

def is_digit_power_sum(num: int, power: int) -> bool:
    if not isinstance(num, int) or not isinstance(power, int) or num < 0 or power < 0:
        raise Exception("Invalid input")

    total = sum(int(digit) ** power for digit in str(num))
    return total == num

def is_valid_product_code(code: str) -> bool:
    if not isinstance(code, str):
        raise Exception("Invalid input")
    
    if len(code) != 12:
        return False

    if code.count('-') != 1 or code.startswith('-') or code.endswith('-'):
        return False

    upper_count = sum(1 for char in code if char.isupper())
    digit_count = sum(1 for char in code if char.isdigit())

    if upper_count < 2 or digit_count < 3:
        return False

    allowed_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-")
    if any(char not in allowed_chars for char in code):
        return False

    return True
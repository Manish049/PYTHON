# Test script to demonstrate math_utils, string_utils, and shop_package modules

from Math_utils import addo, subtract, square_root
from string_utils import capitalize_words, reverse_string, word_count
from shop_package import apply_discount, flat_discount, calculate_total, apply_tax

print("=== Testing math_utils Module ===\n")

# Test addo
print("addo(5, 3) =", addo(5, 3))
print("addo(10, 20) =", addo(10, 20))

# Test subtract
print("\nsubtract(10, 3) =", subtract(10, 3))
print("subtract(5, 8) =", subtract(5, 8))

# Test square_root
print("\nsquare_root(16) =", square_root(16))
print("square_root(25) =", square_root(25))
print("square_root(2) =", square_root(2))

# Test error handling
try:
    print("square_root(-4) =", square_root(-4))
except ValueError as e:
    print(f"square_root(-4) -> Error: {e}")

print("\n=== Testing string_utils Module ===\n")

# Test capitalize_words
test_str = "hello world python"
print(f"capitalize_words('{test_str}') =", capitalize_words(test_str))
print(f"capitalize_words('the quick brown fox') =", capitalize_words("the quick brown fox"))

# Test reverse_string
print(f"\nreverse_string('hello') =", reverse_string("hello"))
print(f"reverse_string('python') =", reverse_string("python"))

# Test word_count
print(f"\nword_count('hello world') =", word_count("hello world"))
print(f"word_count('the quick brown fox jumps') =", word_count("the quick brown fox jumps"))

print("\n=== Testing shop_package Module ===\n")

# Test apply_discount
print("apply_discount(100, 20) =", apply_discount(100, 20))
print("apply_discount(500, 10) =", apply_discount(500, 10))

# Test flat_discount
print("\nflat_discount(100) =", flat_discount(100))
print("flat_discount(200) =", flat_discount(200))

# Test calculate_total
prices = [50, 75, 100, 25]
print(f"\ncalculate_total({prices}) =", calculate_total(prices))

# Test apply_tax
amount = 1000
print(f"\napply_tax({amount}) =", apply_tax(amount))
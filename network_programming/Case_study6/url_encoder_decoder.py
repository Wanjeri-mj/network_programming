# File: url_encoder_decoder.py
from urllib.parse import quote_plus, unquote_plus

print("=" * 55)
print("     URL PERCENT-ENCODING & CODEC UTILITY")
print("=" * 55)

# Prompt for a string containing whitespace and web-breaking control symbols
text_input = input("Enter raw text/query parameter: ").strip()

# 1. Encoding Step: Convert symbols into browser-safe percent strings
# spaces become '+' and non-alphanumeric symbols become '%XX'
encoded_text = quote_plus(text_input)

# 2. Decoding Step: Reverse the transformation back to human-readable form
decoded_text = unquote_plus(encoded_text)

print("-" * 55)
print(f"Encoded String: {encoded_text}")
print(f"Decoded String: {decoded_text}")
print("=" * 55)
class Solution:
    def toHex(self, num: int) -> str:
        # Handle zero explicitly
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"
        result = []

        # For negative numbers use two's complement for 32 bits
        if num < 0:
            num += (1 << 32)

        while num > 0:
            result.append(hex_digits[num & 15])
            num >>= 4

        return ''.join(reversed(result))


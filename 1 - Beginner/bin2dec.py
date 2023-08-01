# Bin2Dec
# Tier: 1-Beginner

# Binary is the number system all digital computers are based on. Therefore it's important for developers to understand binary, or base 2, mathematics. 
#The purpose of Bin2Dec is to provide practice and understanding of how binary calculations.

# Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

# This challenge requires that the developer implementing it follow these constraints:

# Arrays may not be used to contain the binary digits entered by the user

bin = '10101011'

def bin2dec(bin):
    dec = 0

    if not all(i in '01' for i in bin) or len(bin) > 8:
            raise ValueError("Invalid binary input. Only 0s and 1s allowed, up to 8 characters.")

    for i, bit in enumerate(reversed(bin)):
            dec += int(bit) * (2 ** i)
    return int(dec)

print("Decimal equivalent of", bin, "is:", bin2dec(bin))
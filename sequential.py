import random
import string
import time

randomHash = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]).lower();

CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"

lastDigit = randomHash[len(randomHash) - 1]
print(randomHash)
print(lastDigit)

numWhereLastDigitOfCHARS= CHARS.index(lastDigit)
if(numWhereLastDigitOfCHARS == 35):
    numWhereLastDigitOfCHARS = 0
print(numWhereLastDigitOfCHARS)
print(CHARS[numWhereLastDigitOfCHARS + 1])

# Get index of string randomhash.length in CHARS then increment CHARS[i]
import random
import string
import time
from threading import Thread




class BITCoin():
    CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
    COIN_LEN = 6
    def __init__(self):
        tokens = []
        for _ in range(0, 100000):
            token = ""
            for _ in range(0, self.COIN_LEN):
                token += random.choice(self.CHARS)
            tokens.append(token)
        self._tokens = set(tokens)

    _instance = None
    @staticmethod
    def getInstance():
        if not BITCoin._instance:
            BITCoin._instance = BITCoin()
        return BITCoin._instance

    def isCoin(self, token):
        return token in self._tokens


class BITCoinMiner():

    def __init__(self):
        pass

    def hashGenerator(self):

        global randomHashGeneratorCount
        randomHashCount = 0
        timeout = time.time() + 30                      # 30 seconds from now

        while(True):

            #Generate a random hash
            randomHash = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]).lower()

            # Check if random hash matches a coin in the currency pool
            if (BITCoin.getInstance().isCoin(randomHash)):
                randomHashCount += 1
                print("Coins mined from random hash generator: " + randomHash);

            if time.time() > timeout:
                randomHashGeneratorCount += randomHashCount
                break



    def sequentialScan(self):

        global sequentialScanGeneratorCount
        timeout = time.time() + 30
        counter = 2
        randomHash = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]).lower();
        CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"
        tempList = list(randomHash)
        randomHashCount = 0

        while(True):

            randomHashLastValue = randomHash[len(randomHash) - 1]   # Last value in randomHash string
            charIndex = CHARS.index(randomHashLastValue)            # Index of the lastRandomHashValue in CHARS

            CharsLength = len(CHARS)                                # length of CHARS string
            charIndex += 1                                          # Corresponding character after the lastRandomHashValue

            if (charIndex == CharsLength):                          # Check whether the lastValue of randomHash is 'Z'
                charIndex = 0
                thisDigit = tempList[len(tempList) - counter]       # Get second last value of randomHash string

                secondLastChar = CHARS.index(thisDigit)             # Get the index of the second last value of randomHash

                if(secondLastChar == 35):                  # Check if second last value of randomHash is 'Z'
                    secondLastChar = 0
                    counter += 1
                    if(counter == 5 or counter == 6):
                        secondLastChar = CHARS.index(tempList[len(tempList) - counter])
                else:
                    secondLastChar += 1                                 # Corresponding character after the second last value of randomHash

                if(counter == 7):
                    randomHash = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)]).lower();
                    tempList = list(randomHash)
                    counter = 2
                secondLastChar = CHARS[secondLastChar]
                tempList[len(randomHash) - counter] = secondLastChar

            nextChar = CHARS[charIndex]
            tempList[len(tempList) - 1] = nextChar
            tempHash = ''.join(str(e) for e in tempList)
            randomHash = tempHash

            # Check if current hash matches a coin in the currency pool
            if (BITCoin.getInstance().isCoin(randomHash)):
                print("Coins mined from sequential scan: " + randomHash)
                randomHashCount += 1

            if time.time() > timeout:
                sequentialScanGeneratorCount += randomHashCount
                break



randomHashGeneratorCount = 0
sequentialScanGeneratorCount = 0
bitCoinMiner = BITCoinMiner();

# Run 4 threads for 30 seconds

# start the threads for the random hash generator
for i in range(2):
    t1 = Thread(target=bitCoinMiner.hashGenerator(), args=(i,))
    t1.start()


# start the threads for the sequential scan
for i in range(2):
    t2 = Thread(target=bitCoinMiner.sequentialScan(), args=(i,))
    t2.start()

print("Total coins mined using random hash generator: " + str(randomHashGeneratorCount))
print("Total coins mined using sequential scan: " + str(sequentialScanGeneratorCount))






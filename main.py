#just importing some necessary functions ...
import numpy as np
from functools import reduce
import operator as op


bits = np.random.randint(0, 2, 16) #makes a series of 16 1s and 0s
enumerate(bits) #makes that series an array
print(bits) #prints the series
print(list(enumerate(bits))) #assigns positions in an array to the series

#only prints positions that have a 1
print([i for i, bit in enumerate(bits) if bit]) 

#idk how, but it makes the positions with a 1 into a number, idk what for
print(reduce(op.xor, ([i for i, bit in enumerate(bits) if bit])))

#prints that new number as binary
print(bin(reduce(op.xor, ([i for i, bit in enumerate(bits) if bit]))))

#this was hard to do, I reworked it from a 3blue1brown video about Hamming Codes... for Repl... maybe I will do something like this again, but hopefully not soon, I hope...  ANYWAY buh-bye!
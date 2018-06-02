from collections import deque
import math
from Module1Created import *
listNums = randomListOfInts(start=0, finish=10, length=8)
listStrings = ["first", "second", "third","fourth"]
stack = [True, None, False, not False, not True]
queue = deque(listStrings)
dictionary1 = {"first":"first" }

print(listNums)
print(stack)
print(queue)
print(set(listStrings))

listStrings[0] = "e"
print(listStrings)
print(queue.popleft())

addressOf(listNums)
addressOf(listNums[:]) # copy of listNums
#del listNums # and del listNums[:] do the same thing
#addressOf(listNums)

odds = oddSet = {(lambda x: 2*x+1)(i) for i in range(100)}
evens = evenSet = {(lambda x: 2*x)(i) for i in range(100)}

print("".join(evens & odds))
print(evens | odds)






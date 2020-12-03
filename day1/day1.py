import numpy

inputList = []
with open ('./day1input.txt') as f:
    for line in f:
        inputList.append(int(line.strip('\n')))
# print inputList

def twoSum(inputList, sumTo):
    foundNumbers = []
    for entry in inputList:
        pair = sumTo - entry
        if pair in foundNumbers:
            return entry, pair
        else:
            foundNumbers.append(entry)
    return 0,0

# key, value = twoSum(inputList, 2020)
# print key
# print value
# answer = key*value
# print answer

def threeSum(inputList, sumTo):
    inputList.sort()
    n = len(inputList)
    answer = []

    for i in range(n):
        target = sumTo - inputList[i]
        print "target: {}".format(target)
        ans1, ans2 = twoSum(inputList, target)
        print("two sum ans: {}, {}".format(ans1, ans2))
        if ans1 != 0 and ans2 != 0:
            answer.append(inputList[i])
            answer.append(ans1)
            answer.append(ans2)
            return answer
    return None
        
ans = threeSum(inputList, 2020)
print ans
answer = numpy.prod(ans)
print(answer)


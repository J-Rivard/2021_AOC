class PartOne:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.input.append(line.replace("\n", ""))
    
    def solve(self):
        mapCount = {}

        for i in range(len(self.input[0])):
            mapCount[i] = {0: 0, 1: 0}

        for i in self.input:
            for idx, c in enumerate(i):
                mapCount[idx][int(c)] += 1

        gamma = ""
        epsilon = ""
        for k,v in mapCount.items():
            if v[0] > v[1]:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"

        return int(gamma, 2) * int(epsilon, 2)


class PartTwo:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.input.append(line.replace("\n", ""))

    def mostCommonBit(self, arr, index):
        mapCount = {0: 0, 1: 0}

        for i in arr:
            if i[index] == "1":
                mapCount[1] += 1
            else:
                mapCount[0] += 1

        mostCommon = 1
        # If there are more 0s than 1s, most common is 0
        # if there are equal, most common is 1
        if mapCount[0] > mapCount[1]:
            mostCommon = 0
        return mostCommon

    def leastCommonBit(self, arr, index):
        mapCount = {0: 0, 1: 0}

        for i in arr:
            if i[index] == "1":
                mapCount[1] += 1
            else:
                mapCount[0] += 1

        leastCommon = 0
        # if there are more 0's than 1's, least common is 1
        # if there is an equal amount, least common is 0
        if mapCount[0] > mapCount[1]:
            leastCommon = 1
        return leastCommon

    
    def solve(self):
        mostCommonInput = self.input.copy()
        i = 0
        while len(mostCommonInput) != 1:
            charIndex = i % len(mostCommonInput[0])
            mostCommonBit = self.mostCommonBit(mostCommonInput, charIndex)
            mostCommonInput = [x for x in mostCommonInput if x[charIndex] == str(mostCommonBit)]
            i += 1

        leastCommonInput = self.input.copy()
        print(leastCommonInput, "\n")
        i = 0
        while len(leastCommonInput) != 1:
            charIndex = i % len(leastCommonInput[0])
            leastCommonBit = self.leastCommonBit(leastCommonInput, charIndex)
            leastCommonInput = [x for x in leastCommonInput if x[charIndex] == str(leastCommonBit)]
            i += 1


        print(mostCommonInput, int(mostCommonInput[0], 2))
        print(leastCommonInput, int(leastCommonInput[0], 2))
        return int(mostCommonInput[0], 2) * int(leastCommonInput[0], 2)

        
            


# p = PartOne()
# ans = p.solve()
# print(ans)

p = PartTwo()
ans = p.solve()
print(ans)
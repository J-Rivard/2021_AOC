class PartOne:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                cleanLine = int(line.replace("\n", ""))
                self.input.append(cleanLine)
    
    def solve(self):
        count = 0
        
        left = 0
        right = 1
        while right < len(self.input):
            if self.input[left] < self.input[right]:
                count += 1
            
            left += 1
            right += 1
            
        return count

class PartTwo:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                cleanLine = int(line.replace("\n", ""))
                self.input.append(cleanLine)
    
    def solve(self):
        count = 0
        left = 0
        right = 1
        
        previousRunningTotal = 0
        runningTotal = self.input[left]
        
        while right < len(self.input):
            runningTotal += self.input[right]
            
            if right - left == 2:
                if previousRunningTotal < runningTotal:
                    count += 1
                
                previousRunningTotal = runningTotal
                runningTotal -= self.input[left]
                
                left += 1
                right += 1
            else:
                right += 1
        # count - 1 to account for first increase from 0 doesnt count
        return count - 1

p = PartOne()
ans = p.solve()
print(ans)

p = PartTwo()
ans = p.solve()
print(ans)
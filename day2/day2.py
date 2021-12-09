class PartOne:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.input.append(line)
    
    def solve(self):
        h = 0
        v = 0

        for i in self.input:
            command = i.split(' ')
            dir = command[0]
            amt = int(command[1])
            
            if dir == 'forward':
                h += amt
            elif dir == 'up':
                v -= amt
            elif dir == 'down':
                v += amt
            
        return h * v

class PartTwo:
    def __init__(self) -> None:
        self.input = []
        with open('p1_input.txt') as f:
            lines = f.readlines()
            for line in lines:
                self.input.append(line)
    
    def solve(self):
        h = 0
        v = 0
        
        aim = 0

        for i in self.input:
            command = i.split(' ')
            dir = command[0]
            amt = int(command[1])
            
            if dir == 'forward':
                h += amt
                v += amt * aim
            elif dir == 'up':
                aim -= amt
            elif dir == 'down':
                aim += amt
            
        return h * v

p = PartOne()
ans = p.solve()
print(ans)

p = PartTwo()
ans = p.solve()
print(ans)
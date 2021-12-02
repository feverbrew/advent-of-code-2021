

def horizontal_x_depth():
    with open('input.txt') as input:
        instructions = [line.split(' ') for line in input]
        horizontal = 0
        depth = 0
        for instruction in instructions:
            if instruction[0] == 'forward':
                horizontal += int(instruction[1])
            elif instruction[0] == 'up':
                depth -= int(instruction[1])
            elif instruction[0] == 'down':
                depth += int(instruction[1])
            else:
                print('Bad instruction!')
        return horizontal * depth

def aim_horizontal_x_depth(input_file='input.txt'):
    with open(input_file) as input:
        instructions = [line.split(' ') for line in input]
        horizontal = aim = depth = 0
        for instruction in instructions:
            if instruction[0] == 'forward':
                horizontal += int(instruction[1])
                depth += int(instruction[1]) * aim
            elif instruction[0] == 'up':
                aim -= int(instruction[1])
            elif instruction[0] == 'down':
                aim += int(instruction[1])
            else:
                print('Bad instruction!')
        return horizontal * depth

if __name__ == '__main__':
    print('Part 1: ' + str(horizontal_x_depth()))
    print('Part 1: ' + str(aim_horizontal_x_depth()))
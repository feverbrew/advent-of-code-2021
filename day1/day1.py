
def depth_increases() -> int:
    with open('input.txt') as input:
        increased = 0
        depths = [int(line.strip()) for line in input]
        i = 0
        while i < len(depths) - 1:
            if depths[i+1] > depths[i]:
                increased += 1
            i += 1
        return increased

def window_depth_increases() -> int:
    with open('input.txt') as input:
        increased = 0
        depths = [int(line.strip()) for line in input]
        i = 0
        while i < len(depths) - 3:
            window_one = depths[i] + depths[i+1] + depths[i+2]
            window_two = depths[i+1] + depths[i+2] + depths[i+3]
            if window_two > window_one:
                increased += 1
            i += 1
        return increased

if __name__ == '__main__':
    print('Part 1: ' + str(depth_increases()))
    print('Part 2: ' + str(window_depth_increases()))
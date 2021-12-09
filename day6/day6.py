import sys

def laternfish_spawning(input_file: str, days: int) -> int:
    with open(input_file) as input:
        strlanternfish = next(input).split(',')
        lanternfish = [int(alanternfish) for alanternfish in strlanternfish]
        fishdict = {i:0 for i in range(9)}
        for alanternfish in lanternfish:
            try:
                fishdict[alanternfish] += 1
            except:
                fishdict[alanternfish] = 1
    
    for day in range(days):
        fish_after_day = {}
        for i in range(len(fishdict)):
            if i == 6:
                fish_after_day[i] = fishdict[7] + fishdict[0]
            elif i == 8:
                fish_after_day[i] = fishdict[0]
            else:
                fish_after_day[i] = fishdict[i+1]
        fishdict = fish_after_day
    return sum(fishdict.values())

def recursive_laternfish_spawning(input_file: str, days: int) -> int:
    with open(input_file) as input:
        strlanternfish = next(input).split(',')
        lanternfish = [int(alanternfish) for alanternfish in strlanternfish]
    total = 0
    for fish in lanternfish:
        total += recurse_fish(fish, days)
    return total

def recurse_fish(lanternfish, days):
    if days == 0:
        return 1
    elif lanternfish == 0:
        return recurse_fish(6, days-1) + recurse_fish(8, days-1)
    else:
        return recurse_fish(lanternfish-1, days-1)


if __name__ == '__main__':
    print(laternfish_spawning('input.txt', int(sys.argv[1])))
    print(recursive_laternfish_spawning('input.txt', int(sys.argv[1])))
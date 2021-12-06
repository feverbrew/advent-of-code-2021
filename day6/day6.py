

def laternfish_spawning(input_file: str, days: int) -> int:
    with open(input_file) as input:
        strlanternfish = next(input).split(',')
        lanternfish = [int(alanternfish) for alanternfish in strlanternfish]
    
    for day in range(days):
        baby_lanternfish = 0
        for i in range(len(lanternfish)):
            if lanternfish[i] == 0:
                baby_lanternfish += 1
                lanternfish[i] = 6
            else:
                lanternfish[i] -= 1
        print(f'{baby_lanternfish} baby laternfish were born on day {day}!')
        lanternfish.extend([8]*baby_lanternfish)
        # print(lanternfish)
    return len(lanternfish)

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

def formula(input_file, days) -> int:
    # given an input of fish and days, can calculate the fish population using a math formula
    # Maybe the best way of doing this is just figure out how many fish spawn from a certain number after 80 days. If we can do that and just skip 80 days at a time, it gets faster (note that actual number must be a factor of 256)
    with open(input_file) as input:
        strlanternfish = next(input).split(',')
        lanternfish = [int(alanternfish) for alanternfish in strlanternfish]
    total_fish = len(lanternfish) * (1.09289252) ** days
    return total_fish

if __name__ == '__main__':
    print(laternfish_spawning('input.txt', 40))
    print(recursive_laternfish_spawning('input.txt', 40))
    print(formula('input.txt', 40))
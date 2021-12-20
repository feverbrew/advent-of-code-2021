from os import sep
import time
from typing import List
import random

def binary_to_decimal(binary: str) -> int:
    decimal = 0
    for i in range(len(binary)):
        position_value = 2**(len(binary) - 1 - i)
        decimal += int(binary[i]) * position_value
    return decimal

def run_diagnostics(input_file: str) -> int:
    print(f'\033[38;2;20;20;200m\033[48;2;255;255;255mNow running system diagnostics...\033[0m', flush=True)
    time.sleep(.5)
    with open(input_file) as input:
        diagnostic_feed = [line.strip() for line in input]
        line_length = len(diagnostic_feed[0])
        gamma_counts = [0] * line_length
        # Figure out how common things are
        index = 0
        width = 20
        for row in diagnostic_feed:
            list(row)
            for i in range(line_length):
                if row[i] == '1':
                    # print('|*|',end='', flush=True)
                    gamma_counts[i] += 1
                # else:
                #     print('| |',end='', flush=True)
            index += 1
            percent = 100 * float(index) / float(len(diagnostic_feed))
            left = width * index // len(diagnostic_feed)
            right = width - left
            print('\r[', '#'*left, ' '*right, ']', f' {percent:.0f}%', flush=True, end='', sep='')
            percent += 1
            time.sleep(.01)

    # Construct the resulting binaries
    gamma_binary = ''
    epsilon_binary = ''
    for col in gamma_counts:
        if len(diagnostic_feed) - col >= col:
            gamma_binary += '1'
        else:
            gamma_binary += '0'
    for x in list(gamma_binary):
        if x == '1':
            epsilon_binary += '0'
        else:
            epsilon_binary += '1'

    print(f'\nSystem analyzed, calculating status code... \n\033[31;5mWarning:\033[0m errors \033[38;2;200;20;20m{epsilon_binary}\033[0m and \033[38;2;200;20;20m{gamma_binary}\033[0m have been detected!', flush=True)

    # Turn the binaries into decimal
    gamma_decimal = binary_to_decimal(gamma_binary)
    epsilon_decimal = binary_to_decimal(epsilon_binary)

    diagnostic_product = gamma_decimal * epsilon_decimal

    print(f'Status code {diagnostic_product}.\nPlease check the \033[38;2;20;230;20mowner\'s manual\033[0m for more details.')

    return diagnostic_product

def run_life_support_diagnostics(input_file: str) -> int:
    print('\nNow running life support diagnostics...', flush=True)
    time.sleep(.5)
    with open(input_file) as input:
        diagnostic_feed = [line.strip() for line in input]

    print(f'\nOxygen generator rating:', flush=True)
    oxygen_gen_rating = life_support_system_rating(diagnostic_feed, True)
    print(' \033[92mok\033[0m')
    print(f'\nCO2 scrubber rating:', flush=True)
    CO2_scrubber_rating = life_support_system_rating(diagnostic_feed, False)
    print(' \033[31mcheck system\033[0m')

    # Turn the binaries into decimal
    oxygen_decimal = binary_to_decimal(oxygen_gen_rating)
    CO2_decimal = binary_to_decimal(CO2_scrubber_rating)

    life_support_rating = oxygen_decimal * CO2_decimal

    print('\n\nLife support rating:')

    for digit in str(life_support_rating):
        for i in [random.randint(0,9) for j in range(10)]:
            print(f'\b{i}', end='', flush=True)
            time.sleep(.1)
        print(f'\b{digit} ', end='', flush=True)
        time.sleep(.1)
    print(' Normal')

def life_support_system_rating(diagnostic_feed: List, most: bool):
    # Get the system rating
    rating = -1
    rating_candidates = diagnostic_feed.copy()
    for i in range(len(diagnostic_feed)):
        updated_candidates = []
        if len(rating_candidates) == 1:
            rating = rating_candidates[0]
            print(rating[i:], end='', flush=True)
            break
        counts = 0
        for diagnostic_line in rating_candidates:
            list(diagnostic_line)
            if diagnostic_line[i] == '1':
                counts += 1
        if len(rating_candidates) - counts <= counts:
            if most:
                common = '1'
            else:
                common = '0'
        else:
            if most:
                common = '0'
            else:
                common = '1'
            

        print(common, end='', flush=True)
        time.sleep(.1)
        for diagnostic_line in rating_candidates:
            list(diagnostic_line)
            if diagnostic_line[i] == common:
                updated_candidates.append(diagnostic_line)
        rating_candidates = updated_candidates.copy()
    return rating
    

            

if __name__ == '__main__':
    run_diagnostics('input.txt')
    time.sleep(1)
    run_life_support_diagnostics('input.txt')
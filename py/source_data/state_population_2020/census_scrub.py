from pathlib import Path
import os

with open('source_data/2020_state_population/DECENNIALCD1182020.P1-2024-08-29T005844.csv','r') as file:
    k = 0
    dict = {}
    for line in file:
        k = k + 1
        if k != 1:
            my_list = line.split(',')
            i = 0
            pop = ''
            for item in my_list:
                item = item.replace('\n','')
                i = i + 1
                if i == 1 and item != '':
                    state = item
                elif i != 1 and item != '':
                    pop = pop + item
            dict[state] = int(pop)

dir = Path.cwd()
file = Path.joinpath(dir,'source_data','2020_state_population','scrubbed_census.csv')
with open(file,'w+') as scrubbed:
    scrubbed.write(f'State,Population\n')
    for key in dict:
        scrubbed.write(f'{key},{dict[key]}\n')

# TESTING

pass
def states_abbrev():
    
    from pathlib import Path
    
    with open('py/source_data/state_population_2020/State_Abbreviations.txt','r') as file:
        dict = {}
        for line in file:
            if line != '':
                splt0 = line.split('\t')
                splt = []
                for i in splt0:  
                    if i != '':
                        splt.append(i)     
                state = splt[0]
                state = state[:-1]
                abbr = splt[1]
                if '\n' in abbr:
                    st = ''
                    for i in abbr:
                        if i != '\n':
                            st = st + (i)
                        else:
                            pass
                else:
                    st = abbr
                # print(f'{state}, {st}')
                dict[state] = st
        # print(dict)
    return dict

def main():
    states_abbrev()

if __name__ == '__main__':
    main()
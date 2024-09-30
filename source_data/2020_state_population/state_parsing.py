def States():
    
    from pathlib import Path
    
    with open('source_data/2020_state_population/State_Abbreviations.txt','r') as file:
        dict = {}
        for line in file:
            if line != '':
                splt0 = line.split('\t')
                splt = []
                for i in splt0:  
                    if i != '':
                        splt.append(i)     
                state = splt[0]
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
                print(state, st)

def main():
    States()

if __name__ == '__main__':
    main()
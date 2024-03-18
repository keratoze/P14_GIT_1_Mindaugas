#suformuosime nedideli pasirinkimu meniu vartotojui
while True:
    print('\n1. Atspauzdinti ivesti atbulai'
          '\n2. Atspauzdinti ivesti ir simboliu ivestije kieki'
          '\nq - iseiti ')
    pasirinkimas = input('>>>>')
#####################
 #pasirinkimo patikrinimas
    if pasirinkimas not in ('1','2','q'):
        print('Tokio pasirinkimo nera')
        continue

#suformuosime nedideli pasirinkimu meniu vartotojui
while True:
    print('\n1. Atspauzdinti ivesti atbulai'
          '\nq - iseiti ')
    pasirinkimas = input('>>>>')
#####################
 #pasirinkimo patikrinimas
    if pasirinkimas not in ('1','q'):
        print('===========')
        print('Tokio pasirinkimo nera')
        continue

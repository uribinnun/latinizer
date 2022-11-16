def first_declention(noun, case, number):
    nouns_sn = dict(nom=noun, dat=f"{noun[:-1]}ae", acc=f"{noun[:-1]}am")
    if (case == '1' or case == '5' or case == '6') and number == '1':
        return nouns_sn['nom']
    if (case == '2' or case == '3') and number == '1':
        return nouns_sn['dat']
    if case == '4' and number == '1':
        return nouns_sn['acc']

    nouns_pl = dict(nom=f"{noun[:-1]}ae", gen=f"{noun[:-1]}arum", dat=f"{noun[:-1]}is", acc=f"{noun[:-1]}as")
    if (case == '1' or case == '6') and number == '2':
        return nouns_pl['nom']
    if case == '2' and number == '2':
        return nouns_pl['gen']
    if (case == '3' or case == '5') and number == '2':
        return nouns_pl['dat']
    if case == '4' and number == '2':
        return nouns_pl['acc']




print(first_declention(noun=input("choose a noun from the first declention: "),
                       case=input("choose a case: 1-nom, 2-gen, 3-dat, 4-acc, 5-abl, 6-voc: "),
                       number=input('1-singular 2-plural: ')))

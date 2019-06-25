def zatvaraj_vrata(broj):

    vrata = []
    # True - Otvorena
    # False - Zatvorena
    for i in range(0, broj):
        vrata.append(False)

    # Prelazi ucenika po ucenika
    for i in range(1, broj + 1):
        # Prelazi vrata po vrata
        for x in range(1, broj + 1):
            if not(x % i):
                if vrata[x - 1] == False:
                    vrata[x - 1 ] = True
                else:
                    vrata[x - 1] = False

    print(vrata)

zatvaraj_vrata(5)


while True:
    mdp = input("Mot de passe : ")
    if len(mdp) < 6: print("Trop court")
    else:
        lettres = chiffres = 0
        for c in mdp:
            if c.isalpha(): lettres += 1
            elif c.isdigit(): chiffres += 1
            else:print("Caractère invalide") ; break
    if lettres < 2: print("Au moins 2 lettres")
    elif chiffres < 2: print("Au moins 2 chiffres")
    else: print("Mot de passe valide")
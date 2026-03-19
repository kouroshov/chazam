import re

def addition(match):
    a = int(match.group(1))
    b = int(match.group(2))
    somme = a + b
    return [f"le resultat est {somme}", somme]

def info_date(match):
    jour, mois, annee = match.group(1), match.group(2), match.group(3)
    return [f"Le {jour}/{mois}/{annee} a été enregistré", f"{jour}/{mois}/{annee}"]

def calcul_age(match):
    age = match.group(1)
    return [f"Cool, t'as {age} ans!", age]


regle_v2 = [
    ["date", r"(\d{2})/(\d{2})/(\d{4})", None, info_date, 8, True],
    ["age_reg", r"(\d+)\s*ans?", None, calcul_age, 7, True],
    ["calcule", r"(\d+)\s*\+\s*(\d+)", None, addition, 5, False],
    ["JO", r"\bJO\b", "Le prochain JO sera en 2028.", None, 3, False],
    ["BJ", r"\bBonjour\b", "Bonjour mon ami!", None, 2, False],
    ["au_revoir", r"\bAu revoir\b", "Au revoir ca m'a fait plaisir de parler avec toi", None, 1, False]
]



enregistrement = {}
the_name = ""
fois = 0
x = ""

while x.lower() != "stop":
    if fois < 1:
        print("Parle avec ZAGROS...")
        the_name = input("Mais d'abord donne ton nom >>> ")
        fois += 1
    
    x = input(f"{the_name} >>> ")
    if x.lower() == "stop":
        print(f"ZAGROS >>> Au revoir {the_name}")
        break

    trouve = False
    regle_v2.sort(key=lambda x: x[4], reverse=True)

    for i in range(len(regle_v2)):
        match = re.search(regle_v2[i][1], x, re.IGNORECASE)
        if match:
            if regle_v2[i][3] is not None:
                resultat = regle_v2[i][3](match)
                print("ZAGROS >>>", resultat[0])
                
                if regle_v2[i][5]:
                    enregistrement[regle_v2[i][0]] = resultat[1]
            
            elif regle_v2[i][2] is not None:
                print("ZAGROS >>>", regle_v2[i][2])
            
            trouve = True
            break
            
    if not trouve:
        print("ZAGROS >>> Je ne vous ai pas compris.")

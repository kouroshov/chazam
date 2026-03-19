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
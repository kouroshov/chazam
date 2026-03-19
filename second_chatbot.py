regle_v2 = [
    ["date", r"(\d{2})/(\d{2})/(\d{4})", None, info_date, 8, True],
    ["age_reg", r"(\d+)\s*ans?", None, calcul_age, 7, True],
    ["calcule", r"(\d+)\s*\+\s*(\d+)", None, addition, 5, False],
    ["JO", r"\bJO\b", "Le prochain JO sera en 2028.", None, 3, False],
    ["BJ", r"\bBonjour\b", "Bonjour mon ami!", None, 2, False],
    ["au_revoir", r"\bAu revoir\b", "Au revoir ca m'a fait plaisir de parler avec toi", None, 1, False]
]
from evaluate import *
from wallet import *

def debut():
    choix_debut = int(input("Bonjour et bienvenue sur le programme de finance assisté !\n\nComment puis-je vous aider ?\n\n1) Accéder à l'évaluateur d'action\n2) Accéder à la gestion de wallet fictif ?\n\nChoix : "))

    return choix_debut

def redirection(choix_debut):
    while choix_debut not in [1, 2]:
        choix_debut = int(input("\n##################\nERREUR DE SAISIE, veuillez réessayer\n\nComment puis-je vous aider ?\n\n1) Accéder à l'évaluateur d'action\n2) Accéder à la gestion de wallet fictif ?\n\nChoix : "))

    if choix_debut == 1:
        module_evaluate()

    elif choix_debut == 2:
        module_wallet()

def module_evaluate():
    code_isin = isin()
    lien_donnee = url(code_isin, 1)
    lien_indic = url(code_isin, 2)
    liste_donnees = scrapping_bilan_compte_resultat(lien_donnee)
    liste_ratio = scrapping_ratio(lien_indic)
    ca(liste_donnees)
    resultat_net(liste_donnees)
    bpa(liste_ratio)
    per(liste_ratio)
    ##fdr
    ##bfr(liste_donnees)
    ##treso_net = fdr - bfr
    roe(liste_donnees)
    roce(liste_ratio)
    gearing(liste_ratio)
    # div_par_action
    # div_payout_ratio
    # capitalisation/fonds propres

def module_wallet():
    choix_wallet = start()

    if choix_wallet == 1:
        code_isin = isin(choix_wallet)
        url_recup = url(code_isin)
        scrapping(url_recup)

    elif choix_wallet == 2:
        transactions = read()
        calcul_gain(transactions)

    elif choix_wallet == 3:
        code_isin = isin(choix_wallet)
        url_recup = url(code_isin)
        nom_action, price = scrapping(url_recup)
        write(nom_action, price, code_isin, url_recup)

"""
PARTIE PROCESSUS
"""
if __name__ == '__main__':
    choix_debut = debut()
    redirection(choix_debut)

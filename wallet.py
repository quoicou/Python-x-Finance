import requests
import datetime
from bs4 import BeautifulSoup
import re
import os

def start():
    choix = int(input("\n##################\nQue souhaitez-vous ?\n\n1) Consulter action (Prix + Variation)\n2) Consulter les wallets\n3) Créer wallet\n\nChoix : "))

    while choix not in [1, 2, 3]:

        choix = int(input("\n##################\nERREUR DE SAISIE\n\nQue souhaitez-vous ?\n\n1) Consulter action(Prix + Variation)\n2) Consulter les wallets\n3) Céer wallet\n\nChoix : "))

    if choix in [1, 2, 3]:
        return choix

def start_2():
    choix_2 = int(input("\n##################\nQue souhaitez-vous ?\n\n1) Comparer wallet\n2) Ajouter une action au wallet\n\nChoix : "))

    return choix_2

def isin_wallet(choix):
    code_isin = ""

    if choix == 1:
        code_isin = input("\n##################\nRentrez le code ISIN de l'action que vous souhaitez consulter\n\nChoix : ")

    if choix in [2, 3]:
        code_isin = input("\n##################\nRentrez le code ISIN de l'action que vous souhaitez ajouter\n\nChoix : ")

    return code_isin

def url_wallet(code_isin):
    query = f"site:tradingsat.com {code_isin} inurl:societe.html"
    url = f"https://www.google.com/search?q={query}"
    url_recup = ""

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all('a')

    for result in results:
        try:
            lien = result.get("href")
            if f"{code_isin}/societe.html" in lien:
                url_recup = lien
        except:
            pass

    return url_recup

def scrapping(url_recup):
    response = requests.get(url_recup)

    soup = BeautifulSoup(response.text, 'html.parser')

    infos_action = soup.find('div', class_='quote-header-id')
    nom_action = infos_action.find('h1').text
    price = soup.find('span', class_='price').text
    price = float(price.replace('€', '').replace(',', '.').strip())
    variation = soup.find('span', class_='variation').text

    print(f"\n##################\nAnalyse de l'action\n\nNom de l'action : {nom_action}")
    print(f'Prix actuel : {price}')
    print(f'Variation de prix : {variation}')

    return nom_action, price

def write(nom_action, price, code_isin, url_recup, nom_wallet):
    nb_action = int(input("\n##################\nCombien d'action souhaitez-vous acheter ?\n\nChoix : "))

    prix_total = round(price * nb_action, 4)

    print(f"\nVous venez d'acheter {prix_total} € d'action {nom_action}")

    filename = "C://Users//fabi1//Documents//PYTHONxFinance//" + nom_wallet
    with open(filename, "a") as f:
        f.write(f"\n[[{code_isin}][{nom_action}][{price}][{nb_action}][{datetime.datetime.now()}][{url_recup}]]")

def read():
    chemin, liste_wallet = affichage_liste_wallet()

    nom_wallet = input("\nQuel est le nom du wallet que vous souhaitez évaluer ?\n\nChoix : ")

    nom_wallet = nom_wallet + "txt"

    while nom_wallet not in liste_wallet:
        print("\n##################\nERREUR DE SAISIE")

        affichage_liste_wallet()

        nom_wallet = input("\nQuel est le nom du wallet que vous souhaitez évaluer ?\n\nChoix : ")

    filename = chemin + nom_wallet

    with open(filename, "r") as f:
        transactions = f.readlines()
    return transactions

def affichage_liste_wallet():
    chemin = "C://Users//fabi1//Documents//PYTHONxFinance//"

    liste_wallet = os.listdir(chemin)

    print("\nVoici la liste des wallets disponibles : ")

    for nom_wallet in liste_wallet:
        print(f"- {nom_wallet[:-4]}")

    return chemin, liste_wallet

def calcul_gain(transactions):
    #current_datetime = datetime.datetime.now()
    total_gain_loss = 0.0
    try:
        for transaction in transactions:
            match = re.search(r'\[\[(.*?)\]\]', transaction)
            if match:
                transaction_info = match.group(1).split('][')
                prix_achat = float(transaction_info[2])
                quantite = int(transaction_info[3])
                url = transaction_info[5]

                nom_action, prix_actuel = scrapping(url)

                gain_perte_unitaire = round(prix_achat - prix_actuel, 4)

                print(f"Vous avez acheté {quantite} action(s) {nom_action} à {prix_achat}, le prix actuel est {prix_actuel}")

                if gain_perte_unitaire >= 0:
                    print(f"L'action {nom_action} a une plus-value de {gain_perte_unitaire} €")
                else:
                    print(f"L'action {nom_action} a une moins-value de {gain_perte_unitaire} €")

                total_gain_loss += gain_perte_unitaire * quantite

        if total_gain_loss > 0:
            print(f"\n##################\nLe wallet a une plus-value totale de {round(total_gain_loss, 4)} €")
        else:
            print(f"\n##################\nLe wallet a une moins-value totale de {round(total_gain_loss, 4)} €")

    except:
        print("\n##################\nERREUR : Problème de connexion\n\nVeuillez à bien être connecté à internet")

def creation_nom_wallet():
    chemin, liste_wallet = affichage_liste_wallet()

    nom_wallet = input("\nChoisissez le nouveau nom de votre wallet\n\nChoix : ")

    nom_wallet += ".txt"

    while nom_wallet in liste_wallet:
        print(f"\n##################\nERREUR : Le wallet existe {nom_wallet} déjà")

        affichage_liste_wallet()

        nom_wallet = input(f"\nChoisissez le nouveau nom de votre wallet\n\nChoix : ")

        nom_wallet += ".txt"

    chemin_nouveau_wallet = chemin + nom_wallet

    open(chemin_nouveau_wallet, "x")

    budget_wallet = int(input("\nQuel budget souhaitez-vous ?\n\n1) 1000 €\n2) 5000 €\n3) 10 000 €\n\nChoix : "))

    while budget_wallet not in [1, 2, 3]:
        budget_wallet = int(input("\n##################\nERREUR DE SAISIE\n\nQuel budget souhaitez-vous ?\n\n1) 1000 €\n2) 5000 €\n3) 10 000 €\n\nChoix : "))

    return nom_wallet, budget_wallet

def create(choix):
    nom_wallet, budget_wallet = creation_nom_wallet()

    code_isin = isin_wallet(choix)

    url_recup = url_wallet(code_isin)

    nom_action, price = scrapping(url_recup)

    write(nom_action, price, code_isin, url_recup, nom_wallet)

def choisir_nom_wallet():
    chemin, liste_wallet = affichage_liste_wallet()

    nom_wallet = input("\nQuel est le nom du wallet où vous souhaitez ajouter une action ?\n\nChoix : ")

    nom_wallet += ".txt"

    while nom_wallet not in liste_wallet:
        print("\n##################\nERREUR DE SAISIE")

        affichage_liste_wallet()

        nom_wallet = input("\nQuel est le nom du wallet où vous souhaitez ajouter une action ?\n\nChoix : ")

        nom_wallet += ".txt"

    return nom_wallet

"""
PARTIE PROCESSUS
"""
if __name__ == '__main__':
    choix = start()

    if choix == 1:
        code_isin = isin_wallet(choix)
        url_recup = url_wallet(code_isin)
        scrapping(url_recup)

    elif choix == 2:
        choix_2 = start_2()

        if choix_2 == 1:
            transactions = read()
            calcul_gain(transactions)

        elif choix_2 == 2:
            nom_wallet = choisir_nom_wallet()
            code_isin = isin_wallet(choix_2)
            url_recup = url_wallet(code_isin)
            nom_action, price = scrapping(url_recup)
            write(nom_action, price, code_isin, url_recup, nom_wallet)

    elif choix == 3:
        create(choix)

"""
- Display un tableau compte-rendu ou même graphique pour wallet (modif affichage par action / mettre tableau ?)
- Ajouter pour ETF
- Vendre action
- Ajout budget wallet
- Boucle ajout action (tant que user veut ajouter action)
"""

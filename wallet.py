import unidecode
import requests
import datetime
from bs4 import BeautifulSoup
import re
import os

def start():
    choix = 0

    while choix not in [1, 2, 3]:

        choix = int(input("Que souhaitez-vous ?\n1) Consulter action\n2) Comparer wallet\n3) Ajouter une action au wallet\nChoix : "))

        if choix == 1:
            return choix

        elif choix == 2:
            return choix

        elif choix == 3:
            return choix

def isin(choix):
    if choix == 1:
        code_isin = input("Rentrez le code ISIN de l'action que vous souhaitez consulter\nChoix : ")

    if choix == 3:
        code_isin = input("Rentrez le code ISIN de l'action que vous souhaitez ajouter\nChoix : ")

    return code_isin

def url(code_isin):
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

    print(f"Nom de l'action : {nom_action}")
    print(f'Prix actuel : {price}')
    print(f'Variation de prix : {variation}')

    return nom_action, price

def write(nom_action, price, code_isin, url_recup):
    nb_action = int(input("Combien d'action souhaitez-vous acheter ?\nChoix : "))

    prix_total = round(price * nb_action, 4)

    print(f"Vous avez acheté pour {prix_total} € d'action ")

    filename = "C://Users//fabi1//Documents//PYTHONxFinance//wallet.txt"
    with open(filename, "a") as f:
        f.write(f"\n[[{code_isin}][{nom_action}][{price}][{nb_action}][{datetime.datetime.now()}][{url_recup}]]")

def read():
    chemin = "C://Users//fabi1//Documents//PYTHONxFinance//"
    print("Voici tous les wallets que vous pouvez évaluer\nListe des wallets :")
    fichiers = os.listdir(chemin)

    # Affiche les noms des fichiers
    for nom_fichier in fichiers:
        print(nom_fichier)
    nom_wallet = input("Quel est le nom du wallet que vous souhaitez évaluer ?\nChoix : ")
    filename = chemin + nom_wallet

    with open(filename, "r") as f:
        transactions = f.readlines()
    return transactions

def calcul_gain(transactions):
    #current_datetime = datetime.datetime.now()
    total_gain_loss = 0.0
    for transaction in transactions:
        match = re.search(r'\[\[(.*?)\]\]', transaction)
        if match:
            transaction_info = match.group(1).split('][')
            prix_achat = float(transaction_info[2])
            quantite = int(transaction_info[3])
            url = transaction_info[5]

            nom_action, prix_actuel = scrapping(url)

            gain_perte_unitaire = round(prix_achat - prix_actuel, 4)

            if gain_perte_unitaire > 0:
                print(f"L'action {nom_action} a une plus-value de {gain_perte_unitaire} €")
            else:
                print(f"L'action {nom_action} a une moins-value de {gain_perte_unitaire} €")

            total_gain_loss += gain_perte_unitaire * quantite

    if total_gain_loss > 0:
        print(f"Le wallet a une plus-value totale de {round(total_gain_loss, 4)} €")
    else:
        print(f"Le wallet a une moins-value totale de {round(total_gain_loss, 4)} €")

if __name__ == '__main__':
    choix = start()

    if choix == 1:
        code_isin = isin(choix)
        url_recup = url(code_isin)
        scrapping(url_recup)

    elif choix == 2:
        transactions = read()
        calcul_gain(transactions)

    elif choix == 3:
        code_isin = isin(choix)
        url_recup = url(code_isin)
        nom_action, price = scrapping(url_recup)
        write(nom_action, price, code_isin, url_recup)

"""
Display un tableau compte-rendu ou même graphique
"""

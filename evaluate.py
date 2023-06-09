# coding=utf8

"""
AUTRE MANIERE AVEC BEAUTIFUL SOUP
def scrapping():
    url = 'https://tools.morningstar.fr/fr/stockreport/default.aspx?tab=10&vw=is&SecurityToken=0P00009WL3%5D3%5D0%5DE0WWE%24%24ALL&Id=0P00009WL3&ClientFund=0&CurrencyId=EUR'
    requete = requests.get(url).text
    soup = BeautifulSoup(requete, 'html.parser')
    tableau = soup.find('table',{'class':"right years5"})
    df = pd.read_html(str(tableau))
    # convert list to dataframe
    df = pd.DataFrame(df[0])
    df = df.values.tolist()
    print(df)
    return df
"""

import unidecode
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

def isin_evaluate():
    code_isin = input("\n##################\nRentrez le code ISIN de l'action que vous souhaitez analyser\n\nChoix : ")

    return code_isin

def url_evaluate(code_isin, url_utilise):
    query = ""
    url_recup = ""

    if url_utilise == 1:
        query = f"site:tradingsat.com donnees-financieres {code_isin}"
    if url_utilise == 2:
        query = f"site:tradingsat.com indicateurs-financiers {code_isin}"
    url = f"https://www.google.com/search?q={query}"

    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all('a')

    for result in results:
        try:
            lien = result.get("href")
            if url_utilise == 1:
                if f"{code_isin}/donnees-financieres" in lien:
                    url_recup = (lien.split('&')[0])[7:]
            elif url_utilise == 2:
                if f"{code_isin}/indicateurs-financiers" in lien:
                    url_recup = (lien.split('&')[0])[7:]
        except:
            pass

    return url_recup

def annee_actuelle():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    annee = date.year

    return annee

def change_virgule_espace_int(valeur):
    valeur = float(unidecode.unidecode(valeur).replace(" ", ""))

    return valeur

def scrapping_bilan_compte_resultat(lien_donnee): #try except si pas scrapping
    requete = requests.get(lien_donnee).text
    dataframe = pd.read_html(requete)
    liste_donnees = dataframe[0].values.tolist()
    return liste_donnees

def scrapping_ratio(lien_indic):
    requete = requests.get(lien_indic).text
    dataframe = pd.read_html(requete)
    liste_ratio = dataframe[0].values.tolist()
    return liste_ratio

def affichage_donnee(liste, nb_annee, type_donnee, ligne):
    i, j = 1, nb_annee-1
    tableau=[]
    while i != nb_annee:
        if "%" in liste[ligne][i] or "€" in liste[ligne][i]:
            valeur = float(liste[ligne][i].replace("%", "").replace("€", "").replace(" ", ""))
        else:
            valeur = liste[ligne][i]
        tableau.append(valeur)
        print(f"{type_donnee} {annee_actuelle() - j} = {valeur}")
        i+=1
        j-=1

    print("---")
    return tableau

def finder(liste, *args):
    i = 2
    if len(args) == 1:
        try:
            while args[0] not in liste[i][0]:
                i+=1
            ligne = i
            return ligne
        except:
            ligne = 0
            return ligne

    elif len(args) == 2:
        try:
            while args[0] not in liste[i][0]:
                i+=1
            ligne = i

            i = 2
            while args[1] not in liste[i][0]:
                i+=1
            ligne2 = i
            return ligne, ligne2
        except:
            ligne = 0
            ligne2 = 0
            return ligne, ligne2

def ca(liste_donnees):
    type_donnee = "Chiffre d'affaires"
    ligne = finder(liste_donnees, type_donnee)

    if ligne != 0:
        nom_donnee = "CA"
        nb_annee = len(liste_donnees[ligne])
        print("\n##################\n")
        tableau = affichage_donnee(liste_donnees, nb_annee, nom_donnee, ligne)

def resultat_net(liste_donnees):
    type_donnee = "Résultat net"
    ligne = finder(liste_donnees, type_donnee)

    if ligne != 0:
        nom_donnee = "Résultat Net"
        nb_annee = len(liste_donnees[ligne])
        tableau = affichage_donnee(liste_donnees, nb_annee, nom_donnee, ligne)

def bpa(liste_ratio):
    type_donnee = "Résultat net part du groupe dilué par action"
    ligne = finder(liste_ratio, type_donnee)

    if ligne != 0:
        nom_donnee = "BPA"
        nb_annee = len(liste_ratio[ligne])
        tableau = affichage_donnee(liste_ratio, nb_annee, nom_donnee, ligne)

def per(liste_ratio):
    type_donnee = "PER"
    ligne = finder(liste_ratio, type_donnee)

    if ligne != 0:
        nom_donnee = "P/E"
        per = liste_ratio[ligne][5]
        print(f"{nom_donnee} {annee_actuelle() - 1} = {per} \n---")

def bfr(liste_bilan): # à revoir
    bfr_annee_moins_5 = liste_bilan[9][1] - liste_bilan[25][1]
    bfr_annee_moins_4 = liste_bilan[9][2] - liste_bilan[25][2]
    bfr_annee_moins_3 = liste_bilan[9][3] - liste_bilan[25][3]
    bfr_annee_moins_2 = liste_bilan[9][4] - liste_bilan[25][4]
    bfr_annee_moins_1 = liste_bilan[9][5] - liste_bilan[25][5]

def roe(liste_donnees):
    type_donnee = "Résultat net"
    type_donnee2 = "Capitaux propres"

    ligne, ligne2 = finder(liste_donnees, type_donnee, type_donnee2)

    if ligne != 0:
        nb_annee = len(liste_donnees[ligne])
        i, j = 1, nb_annee-1
        nom_donnee = "ROE"
        tableau=[]

        while i != nb_annee:
            valeur = round(change_virgule_espace_int(liste_donnees[ligne][i]) / change_virgule_espace_int(liste_donnees[ligne2][i]) * 100, 2)
            tableau.append(valeur)
            print(f"{nom_donnee} {annee_actuelle() - j} = {valeur}")
            i+=1
            j-=1

    print("---")

def roce(liste_ratio):
    type_donnee = "Rentabilité Financière"
    ligne = finder(liste_ratio, type_donnee)

    if ligne != 0:
        nom_donnee = "ROCE"
        nb_annee = len(liste_ratio[ligne])
        tableau = affichage_donnee(liste_ratio, nb_annee, nom_donnee, ligne)

def gearing(liste_ratio):
    type_donnee = "Ratio d'endettement"
    ligne = finder(liste_ratio, type_donnee)

    if ligne != 0:
        nom_donnee = "Gearing"
        nb_annee = len(liste_ratio[ligne])
        tableau = affichage_donnee(liste_ratio, nb_annee, nom_donnee, ligne)

"""
PARTIE PROCESSUS
"""
if __name__ == '__main__':
    code_isin = isin_evaluate()
    lien_donnee = url_evaluate(code_isin, 1)
    lien_indic = url_evaluate(code_isin, 2)
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
    #div_par_action
    #div_payout_ratio
    #capitalisation/fonds propres

"""
GUI AVEC PHP qui lance python
- AI Login page
---
TODO : 
- PER Sectoriel
- Scrap secteur
- Scrapping différent secteur bancaire (à vérif)
- différencier ROE et ROCE 
- diff entre -400 et - (absence de données)
---
Module "pépite"
- Ressortir des actions avec ratios similaires ? (exemple action avec même sous-evaluation que Stellantis)
"""

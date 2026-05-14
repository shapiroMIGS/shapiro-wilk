# Test de normalité de Shapiro-Wilk

Projet M1 Statistiques — Université de Bourgogne Europe

## Auteurs
- OUSSENI Bicharati
- KOBA Kami

## Description

Ce projet étudie le test de normalité de Shapiro-Wilk (1965). L'objectif est d'expliquer la construction de la statistique $W$, de simuler numériquement sa distribution par méthode de Monte Carlo ($N_{sim} = 10^6$), et de reconstruire la table des quantiles critiques.

## Résultats principaux

- Erreur moyenne sur les quantiles reconstruits : **0,004**
- Le test est très puissant face aux lois asymétriques (ex : loi exponentielle) dès les petits échantillons
- Pour la loi uniforme, une taille **n ≥ 90** est nécessaire pour être fiable
- Application sur *Iris setosa* (Fisher, 1936) : $W = 0{,}9788$, p-valeur $= 0{,}423$ → normalité non rejetée

## Contenu du dépôt

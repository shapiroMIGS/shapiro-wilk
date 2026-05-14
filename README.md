## Résultats principaux

- Erreur moyenne sur les quantiles : **0,004**
- Le test est très puissant face aux lois asymétriques dès n petit
- Pour la loi uniforme, il faut **n ≥ 90** pour être fiable

## Application — Iris de Fisher

Le test a été appliqué aux longueurs de sépales de l'espèce *Iris setosa*
(50 observations, Fisher 1936) :

| Statistique | Valeur |
|-------------|--------|
| W_obs | 0,9788 |
| p-valeur | 0,423 |

**Conclusion** : la p-valeur étant largement supérieure à 5%, on ne rejette pas H₀.
Les données sont compatibles avec une distribution normale.

## Références

Shapiro, S.S. & Wilk, M.B. (1965). *An analysis of variance test for normality*. Biometrika, 52(3-4), 591-611.

Shapiro, S.S. & Francia, R.S. (1972). *An approximate analysis of variance test for normality*. Journal of the American Statistical Association.

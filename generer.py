import numpy as np
import os
import time

# Créer le dossier data s'il n'existe pas
os.makedirs("data", exist_ok=True)

np.random.seed(42)
tailles = range(3, 51)
Nsim = 100000

print("DÉMARRAGE DE LA GÉNÉRATION (n=3 à n=50)")
temps_debut = time.time()

for n in tailles:

    if os.path.exists(f"data/W_n{n}.txt") and os.path.exists(f"data/a_n{n}.txt"):
        print(f"n={n} déjà calculé, ignoré.")
        continue

    Z = np.array([np.sort(np.random.normal(0, 1, n)) for _ in range(Nsim)])
    m = np.mean(Z, axis=0)
    a = m / np.linalg.norm(m)
    np.savetxt(f"data/a_n{n}.txt", a, fmt="%.6e")

    W = np.array([(a @ z)**2 / np.sum((z - z.mean())**2) for z in Z])
    np.savetxt(f"data/W_n{n}.txt", W, fmt="%.6e")

    if n % 10 == 0 or n == 3:
        print(f"n={n} terminé.")

duree = (time.time() - temps_debut) / 60
print(f"FIN — Temps : {duree:.2f} minutes")



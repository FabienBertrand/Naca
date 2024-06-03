import numpy as np
import matplotlib.pyplot as plt


def naca_profile(numero_naca, longeur_corde, nombre_point, distribution_type):
    t = int(numero_naca[2:]) / 100  # On prend les 2 derniers chiffres NACA uniquement (cf : formule du devoir)

    # Donne xc selon le type de distribution
    if distribution_type == "linéaire":
        xc = np.linspace(0, 1, nombre_point)
    elif distribution_type == "non-uniforme":
        theta = np.linspace(0, np.pi, nombre_point)
        xc = 0.5 * (1 - np.cos(theta))
    else:
        raise ValueError("Le type de distribution doit être 'linéaire' ou 'non-uniforme'")

    # Calcul de yt
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)

    # Calcul de (xup, xdown, yup, ydown)
    xup = xc * longeur_corde
    yup = yt * longeur_corde
    xdown = xc * longeur_corde
    ydown = -yt * longeur_corde
    # remarque : yt, xup, xdown, yup et ydown sont sous forme de tableau numpy car dépendent de xc définit a partir de lindspace

    # Calcul épaisseur maximale + position
    epaisseur_max = np.max(yt) * longeur_corde * 2  # car yt est la demi-epaisseur adimentionné par la corde
    position_epaisseur_max = xc[np.argmax(yt)] * longeur_corde

    # Affichage des résultats
    print(f"Épaisseur maximale: {epaisseur_max:.4f} mètres")
    print(f"Position de l'épaisseur maximale: {position_epaisseur_max:.4f} mètres")

    # Affichage du profil
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.plot(xup, yup, label="Extrados")
    plt.plot(xdown, ydown, label="Intrados")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(f"Profil NACA {numero_naca}")
    plt.xlabel("Longueur de la corde (m)")
    plt.ylabel("Épaisseur (m)")
    plt.legend()
    plt.show()


# Informations à récupérer
numero_naca = input("Entrez le numéro du profil NACA (4 chiffres): ")
longeur_corde = float(input("Entrez la longueur de la corde (en mètres): "))
nombre_point = int(input("Entrez le nombre de points le long de la corde: "))
distribution_type = input("Entrez le type de distribution des points (linéaire/non-uniforme): ")

naca_profile(numero_naca, longeur_corde, nombre_point, distribution_type)

import numpy as np
import matplotlib.pyplot as plt

"""_Informations générales_
# ! Ce code génère et trace les signaux modulés en amplitude et leur spectre
# ! fréquentiel. Il contient également des fonctions pour calculer le cube d'un
# ! nombre et le volume d'une sphère.
# ? Signal modulant (message)
# ? Signal porteur (porteuse)

# * Functions:
# *    cube(x)
# *    volume_sphere(r)

Variables:
    fs (float): Fréquence d'échantillonnage en Hz.
    t (ndarray): Vecteur temps du signal.
    fm (float): Fréquence du signal modulant en Hz.
    am (float): Amplitude du signal modulant.
    ap (float): Amplitude de la porteuse.
    fp (float): Fréquence de la porteuse en Hz.
    s (ndarray): Signal AM.
    fft_s (ndarray): FFT du signal modulé.
    fft_f (ndarray): Fréquences de la FFT.
    x (int or float): Nombre pour le calcul du cube.
    r (float): Rayon de la sphère.

Le script exécute les étapes suivantes :
1. Définit la fréquence d'échantillonnage et le tableau temporel.
2. Définit les paramètres des signaux modulants et porteurs.
3. Crée le signal modulé en amplitude.
4. Calcule la FFT du signal modulé et la décale pour la visualisation.
5. Trace la représentation du domaine temporel du signal modulé.
6. Trace la représentation du domaine fréquentiel du signal modulé.
7. Calcule le cube d'un nombre.
8. Calcule le volume d'une sphère à partir de son rayon.
9. Affiche le volume de la sphère.

# TODO: Compléter le programme
"""

# * Fréquence d'échantillonnage et durée d'affichage
fs = 2e3  # en [Hz]
t = np.arange(0, 10, 1/fs)  # en [s]

# ? Création du signal modulant (message)
fm = 2      # * Fréquence du message (signal modulant) en [Hz]
am = 0.5    # * Amplitude du message
# ? Création du signal porteur
ap = 1      # * Amplitude de la porteuse
fp = 50     # * Fréquence de la porteuse en [Hz]
# ? Création du signal modulé
s = ap*(1+am*np.sin(2 * np.pi * fm * t)/ap)*np.sin(2 * np.pi * fp * t)

# Calcul de la FFT
fft_s = np.fft.fft(s)
fft_s = np.fft.fftshift(fft_s)
fft_f = np.fft.fftfreq(len(s), 1/fs)
fft_f = np.fft.fftshift(fft_f)

# !Courbe du signal
plt.figure(figsize=(12, 6))

# ? Courbe temporelle
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Représentation temporelle du signal')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 2.5)
plt.grid(which='major', color='#666666', linestyle='-', alpha=0.6)
plt.minorticks_on()
plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

# ? Courbe FFT
plt.subplot(2, 1, 2)
plt.plot(fft_f, 1/len(t)*np.abs(fft_s))
plt.title('Représentation dans le domaine fréquentiel')
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Amplitude')
plt.xlim(-1.1*fp, 1.1*fp)
plt.grid(which='major', color='#666666', linestyle='-', alpha=0.6)
plt.minorticks_on()
plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.show()


# ? Ajout de calculs avec des fonctions

def cube(x):
    """
    # TODO: Calcul le cube d'un nombre.

    Args:
        x (int or float): Le nombre.

    Returns:
        int or float: Le cube du nombre.
    """
    return x**3
        
def volume_sphere(r):
    """
    # TODO: Calcul le volume d'une sphère à partir de son rayon.

    Parameters:
    r (float): Le rayon de la sphère.

    Returns:
    float: Le volume de la sphère.
    """
    return 4/3 * np.pi * cube(r)

r = 5
v = volume_sphere(r)

print(f"Le volume de la sphère de rayon {r} [m] est : {v:.3f} [m^3].")
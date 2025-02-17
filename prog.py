import numpy as np
import matplotlib.pyplot as plt

"""_Informations générales_
# ! Ce code génère et trace les signaux modulés en amplitude et leur spectre
# ? Signal modulant (message)
# ? Signal porteur (porteuse)

# * Functions:
# *    None

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

Le script exécute les étapes suivantes :
1. Définit la fréquence d'échantillonnage et le tableau temporel.
2. Définit les paramètres des signaux modulants et porteurs.
3. Crée le signal modulé en amplitude.
4. Calcule la FFT du signal modulé et la décale pour la visualisation.
5. Trace la représentation du domaine temporel du signal modulé.
6. Trace la représentation du domaine fréquentiel du signal modulé.

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
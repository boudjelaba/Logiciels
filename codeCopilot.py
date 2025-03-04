import numpy as np
import matplotlib.pyplot as plt

# Définition des paramètres de la simulation
fs = 2e3  # Fréquence d'échantillonnage en [Hz]
t = np.arange(0, 10, 1/fs)  # Vecteur temps en [s]

# Paramètres du signal modulant (message)
fm = 2      # Fréquence du message en [Hz]
am = 0.5    # Amplitude du message

# Paramètres de la porteuse
ap = 1      # Amplitude de la porteuse
fp = 50     # Fréquence de la porteuse en [Hz]

# Génération du signal modulé en amplitude (AM)
s = ap * (1 + am * np.sin(2 * np.pi * fm * t) / ap) * np.sin(2 * np.pi * fp * t)

# Calcul de la transformée de Fourier du signal
fft_s = np.fft.fft(s)
fft_s = np.fft.fftshift(fft_s)  # Décalage pour centrer la fréquence zéro
fft_f = np.fft.fftfreq(len(s), 1/fs)
fft_f = np.fft.fftshift(fft_f)

# Création de la figure pour les représentations temporelle et fréquentielle
plt.figure(figsize=(12, 6))

# Représentation temporelle du signal
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Représentation temporelle du signal')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 2.5)
plt.grid(which='major', color='#666666', linestyle='-', alpha=0.6)
plt.minorticks_on()
plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

# Représentation fréquentielle du signal
plt.subplot(2, 1, 2)
plt.plot(fft_f, 1/len(t) * np.abs(fft_s))
plt.title('Représentation dans le domaine fréquentiel')
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Amplitude')
plt.xlim(-1.1 * fp, 1.1 * fp)
plt.grid(which='major', color='#666666', linestyle='-', alpha=0.6)
plt.minorticks_on()
plt.grid(which='minor', color='#999999', linestyle='-', alpha=0.2)

# Ajustement de la mise en page et affichage des graphiques
plt.tight_layout()
plt.show()

# Fonction pour calculer le cube d'un nombre
def cube(x):
    return x**3

# Fonction pour calculer le volume d'une sphère
def volume_sphere(r):
    return 4/3 * np.pi * cube(r)

# Calcul et affichage du volume d'une sphère de rayon 5 mètres
r = 5
v = volume_sphere(r)
print(f"Le volume de la sphère de rayon {r} [m] est : {v:.3f} [m^3].")

import numpy as np
import matplotlib.pyplot as plt

# tiempo
t = np.linspace(-1, 1, 1000)
dt = t[1] - t[0]

# senal rectangular
x1 = np.zeros(len(t))
x1[(t >= -0.25) & (t <= 0.25)] = 1

# senal seno
x2 = np.sin(2 * np.pi * 5 * t)

# escalon unitario
x3 = np.zeros(len(t))
x3[t >= 0] = 1

# graficar las senales
plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.title("Senal rectangular")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.title("Senal senoidal")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, x3)
plt.title("Escalon unitario")
plt.grid()

plt.tight_layout()
plt.show()

# transformada de Fourier de la senal seno
n = len(x2)
f = np.fft.fftfreq(n, dt)
X = np.fft.fft(x2)

plt.figure()
plt.plot(np.fft.fftshift(f), np.fft.fftshift(np.abs(X)))
plt.title("Espectro de magnitud")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()

# espectro de fase
plt.figure()
plt.plot(np.fft.fftshift(f), np.fft.fftshift(np.angle(X)))
plt.title("Espectro de fase")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase")
plt.grid()
plt.show()

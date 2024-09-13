import numpy as np
import librosa
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
import soundfile as sf

# Función para cargar y graficar el audio
def cargar_y_graficar_audio(archivo_audio, titulo):
    # Cargar el archivo de audio usando librosa
    signal, sr = librosa.load(archivo_audio, sr=None)
    
    # Crear el vector de tiempo en segundos
    tiempo = np.linspace(0, len(signal) / sr, num=len(signal))
    
    # Graficar la señal de audio
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo, signal)
    plt.title(titulo)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()  # Asegurarse de mostrar la gráfica
    
    return signal, sr

# Función para calcular SNR
def calcular_snr(signal, noisy_signal):
    # Calcula el ruido como la diferencia entre la señal ruidosa y la señal original
    noise = noisy_signal - signal
    
    # Potencia de la señal (promedio cuadrático)
    signal_power = np.mean(signal ** 2)
    
    # Potencia del ruido (promedio cuadrático)
    noise_power = np.mean(noise ** 2)
    
    # Evitar división por cero
    if noise_power == 0:
        return float('inf')  # Retorna infinito si no hay ruido
    
    # SNR en dB (decibelios)
    snr = 10 * np.log10(signal_power / noise_power)
    
    return snr

# Función para añadir ruido a una señal y graficarla
def añadir_ruido_y_graficar(signal, sr, nivel_ruido=0.5, titulo="Señal con Ruido"):
    # Añadir ruido blanco
    noisy_signal = signal + np.random.normal(0, nivel_ruido, signal.shape)
    
    # Calcular el vector de tiempo
    tiempo = np.linspace(0, len(signal) / sr, num=len(signal))
    
    # Graficar la señal con ruido
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo, noisy_signal, color='orange')
    plt.title(titulo)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.show()  # Mostrar la gráfica
    
    return noisy_signal

# Nueva función para calcular y graficar la FFT de una señal
def graficar_fft(signal, sr, titulo="Espectro de frecuencia"):
    # Calcular la FFT
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(fft_result), 1/sr)
    
    # Graficar la magnitud de la FFT
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(fft_result)//2])
    plt.title(titulo)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud')
    plt.show()  # Mostrar la gráfica

# Función para cargar múltiples archivos de audio
def cargar_multiples_audios(archivos):
    señales = []
    sr = None
    for archivo in archivos:
        signal, sr = librosa.load(archivo, sr=None)
        señales.append(signal)
    return np.array(señales), sr

# Función para realizar ICA (Análisis de Componentes Independientes)
def aplicar_ica(señales):
    ica = FastICA(n_components=len(señales))
    señales_separadas = ica.fit_transform(señales.T).T  # Transponemos para adecuar la forma
    return señales_separadas

# Función para graficar señales separadas
def graficar_señales(señales_separadas, sr):
    for i, señal in enumerate(señales_separadas):
        tiempo = np.linspace(0, len(señal) / sr, num=len(señal))
        plt.figure(figsize=(10, 4))
        plt.plot(tiempo, señal)
        plt.title(f'Señal separada {i+1}')
        plt.xlabel('Tiempo [s]')
        plt.ylabel('Amplitud')
        plt.show()  # Mostrar la gráfica

# Función para guardar las señales separadas en archivos de audio
def guardar_señales_audio(señales_separadas, sr, nombres_archivos):
    for i, señal in enumerate(señales_separadas):
        archivo_salida = nombres_archivos[i]
        sf.write(archivo_salida, señal, sr)
        print(f'Señal separada guardada en: {archivo_salida}')

# Procesamiento de múltiples señales con ICA, FFT y SNR
def procesar_con_ica_fft_snr(archivos, nivel_ruido=0.5):
    # Cargar múltiples señales
    señales, sr = cargar_multiples_audios(archivos)
    
    # Graficar FFT y calcular SNR para cada señal
    for i, señal in enumerate(señales):
        # Añadir ruido a la señal
        noisy_signal = añadir_ruido_y_graficar(señal, sr, nivel_ruido, f'Señal con Ruido - {archivos[i]}')
        
        # Calcular y mostrar el SNR
        snr_value = calcular_snr(señal, noisy_signal)
        print(f"SNR para {archivos[i]}: {snr_value:.2f} dB")
        
        # Graficar la FFT de la señal original
        graficar_fft(señal, sr, f'Espectro de frecuencia - {archivos[i]}')
    
    # Aplicar ICA para separar las señales
    señales_separadas = aplicar_ica(señales)
    
    # Graficar las señales separadas
    graficar_señales(señales_separadas, sr)
    
    # Guardar las señales separadas en archivos de audio
    nombres_archivos_separados = [f'separada_{i+1}.wav' for i in range(len(señales_separadas))]
    guardar_señales_audio(señales_separadas, sr, nombres_archivos_separados)

# Lista de archivos a procesar
archivos = ['ruido.wav', 'au1.wav', 'au2.wav']

# Procesar con ICA, FFT y SNR
procesar_con_ica_fft_snr(archivos)

# Procesamiento de Señales de Audio

Este proyecto realiza el procesamiento de señales de audio utilizando el Análisis de Componentes Independientes (ICA) y la Transformada Rápida de Fourier (FFT). El objetivo es separar señales de audio mezcladas y realizar un análisis de frecuencia en ellas.

## Descripción del Código

### Transformada Rápida de Fourier (FFT)

La **Transformada Rápida de Fourier (FFT)** es un algoritmo eficiente para calcular la Transformada Discreta de Fourier (DFT) y su inversa. La DFT es una herramienta matemática que descompone una señal en sus componentes de frecuencia. La FFT permite analizar el contenido espectral de una señal, es decir, determinar qué frecuencias están presentes en la señal y con qué amplitud.

En el código proporcionado, la FFT se utiliza para graficar el espectro de frecuencia de las señales de audio. La función `graficar_fft` realiza los siguientes pasos:
1. Calcula la FFT de la señal.
2. Obtiene las frecuencias correspondientes.
3. Grafica la magnitud de la FFT frente a la frecuencia.

### Análisis de Componentes Independientes (ICA)

El **Análisis de Componentes Independientes (ICA)** es una técnica de separación de señales que se utiliza para descomponer un conjunto de señales mixtas en componentes independientes. Esta técnica se basa en el supuesto de que las señales mixtas son combinaciones lineales de componentes independientes, y busca recuperar estas componentes originales.

En el código proporcionado, el ICA se utiliza para separar las señales de audio mezcladas. La función `aplicar_ica` realiza los siguientes pasos:
1. Inicializa un objeto `FastICA` con el número de componentes igual al número de señales mixtas.
2. Aplica el ICA a las señales para obtener las señales separadas.
3. Devuelve las señales separadas.

### Código Principal

El código principal (`main.py`) realiza los siguientes pasos:

1. **Carga de Audios**: La función `cargar_multiples_audios` carga las señales de audio desde archivos y las almacena en un arreglo.

2. **Añadir Ruido y Graficar**: La función `añadir_ruido_y_graficar` añade ruido blanco a las señales y las grafica. Esto simula la adición de ruido a las señales originales.

3. **Calcular y Mostrar SNR**: La función `calcular_snr` calcula la relación señal-ruido (SNR) entre la señal original y la señal ruidosa. El SNR es una medida de la calidad de la señal, donde un mayor SNR indica una mejor calidad.

4. **Graficar FFT**: La función `graficar_fft` grafica el espectro de frecuencia de cada señal original.

5. **Aplicar ICA**: La función `aplicar_ica` utiliza ICA para separar las señales mezcladas en sus componentes independientes.

6. **Guardar Señales Separadas**: La función `guardar_señales_audio` guarda las señales separadas en archivos de audio.

## Requisitos

Este proyecto requiere las siguientes bibliotecas de Python:
- `numpy`
- `librosa`
- `matplotlib`
- `scikit-learn`
- `soundfile`
- `scipy`

Instala las dependencias con el siguiente comando:
```bash
pip install -r requirements.txt

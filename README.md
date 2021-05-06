# Periodogram-Python
Implement and demonstrate periodogram in Python

Periodogram
A periodogram is a method of calculating the power spectral density (PSD) of a signal. The power spectral density (usually Power/Hz vs frequency, on a log-log plot) of this signal will have a peak at the frequency f. It is useful for identifying frequency content in a signal. A simple periodogram involves dividing the data into windows and computing the PSD of each window, then taking the mean of these individual PSDs. A raw PSD is a poor estimate in the statistical sense. A simple periodogram fixes this issue but doesn't solve spectral leakage which can be fixed by certain types of windows ( Hanning). here are different algorithms to compute it - Welch and Blackman-Tukey for example.
Advantages: A periodogram is used to identify the dominant periods (or frequencies) of a time series. This can be a helpful tool for identifying the dominant cyclical behaviour in a series, particularly when the cycles are not related to the commonly encountered monthly or quarterly seasonality. Noisy data produce noisy periodograms. Peaks in a periodogram may therefore not be due to the presence of any real periodic phenomenon at all. They may simply be random fluctuations in periodogram power caused by the presence of a noise component in the data. Peaks arising in this way are spurious: they are not due to any real periodicity in the observed phenomena, but are simply artefacts of chance events in the accompanying noise. Spurious peaks can be surprisingly large.




Example 1
Harmonic signals are integer multiples (2⋅f, 3⋅f…) of the fundamental frequencies. As example the fundamental frequency of 1Hz has harmonics in 2Hz, 3Hz and so on.

DFT calculate only fundamental frequencies. This means that each sine or cosine signal used to calculate the power of a frequency is uncorrelated with others and no exact harmonics are used in the transform. For that reason, there is only one peak for a perfect sine wave (Figure 1 a and b).
For those signals who are not perfect sinewaves, they have a different shape and their frequency fluctuates. Because the fundamental frequencies used in DFT are very close to each other it means that multiple peaks can be seen for non-sine wave periodic signals.
The sawtooth wave in Figure 1 c has the highest peak at its actual (normalized) frequency 0.025, the second peak at 0.049 and the third at 0.074. While these are not exact harmonics, they are very close and we often see these peaks appearing when we used DFT for actual measured signals.
The sawtooth and square waves actual contains multiple different frequencies because their rate of change varies. The sawtooth has a higher frequency when it falls than when it rises and the square wave has high frequency when it rises and falls, but zero frequency at the top and bottom.

![image](https://user-images.githubusercontent.com/58274552/117357490-4c754700-aeb5-11eb-82ea-da1a9145c631.png)

Example 2 
x = sin+ cos
Here we created a signal with a sine and a cosine wave.  The periodogram plot shows that main frequencies contained in the signal are around 0.08 and 0.12, the unit is relative to sampling rate.

![image](https://user-images.githubusercontent.com/58274552/117357540-5bf49000-aeb5-11eb-83d0-8e46eee8d3c4.png)

Reference :

1.	https://en.wikipedia.org/wiki/Periodogram
2.	https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html
3.	https://www.kite.com/python/docs/scipy.signal.periodogram


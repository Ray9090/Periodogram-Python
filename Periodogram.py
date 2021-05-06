from scipy import signal
from pylab import *
from pyageng import *

x = linspace(1, 80, 512)
def plot_signal(x):
    plot(x)
    axis('tight')
    ylim(-1.1, 1.1)
    xlabel('n (samples)')
    ylabel('Amplitude')

figure(figsize=(6.5,8))
subplot(321)
sx = sin(x)
plot_signal(sx)
title("a) Sinusoidal signal")
subplot(322)
pfft(sx)
title("b) Periodogram of sinusoidal signal")

subplot(323)
sax = signal.sawtooth(x)
plot_signal(sax)
title("c) Sawtooth signal")
subplot(324)
pfft(sax)
title("d) Periodogram of sawtooth signal")

sqx = signal.square(x)
subplot(325)
plot_signal(sqx)
title("e) Square signal")
subplot(326)
pfft(sqx)
title("f) Periodogram of square signal")

#Add space between subplots
subplots_adjust(hspace=0.5, wspace=0.4)

#Create a signal
x = sin(linspace(0., 500, 1024)) + 0.5*cos(linspace(0, 750, 1024))

f, Sk = signal.periodogram(x, nfft = 1024, return_onesided = True,
scaling = "spectrum")
# Check that sum(Sk) equals variance of x
sum(Sk) == var(x)
True

figure(figsize=(6.5,8))
subplot(211)
plot_signal((x)[0:250])
title("a) Signal")
subplot(212)
pyageng.pfft(x)
title("b) Periodogram ")
subplots_adjust(hspace=0.5, wspace=0.4)

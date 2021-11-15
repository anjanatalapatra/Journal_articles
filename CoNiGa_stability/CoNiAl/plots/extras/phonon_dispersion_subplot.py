import sys
sys.path.append("/home/anjana/Dropbox/bin")
from numpy import loadtxt, linspace
from plot_settings import save_fig_size
import matplotlib.pyplot as plt


freq_L21 = loadtxt('L21_eigenfreq.out') * 10 ** (-12)
freq_L10 = loadtxt('L10_eigenfreq.out') * 10 ** (-12)
freq_O = loadtxt('O_eigenfreq.out') * 10 ** (-12)
n = len(freq_O[:, 0])
x = linspace(0, 1, n)

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(x, freq_L21[:, 0], 'bo', x, freq_L21[:, 1], 'bo', x, freq_L21[:, 2], 'bo', x, freq_L21[:, 3], 'bo', x, freq_L21[:, 4], 'bo', x, freq_L21[:, 5], 'bo', x, freq_L21[:, 6], 'bo', x, freq_L21[:, 7], 'bo', x, freq_L21[:, 8], 'bo', x, freq_L21[:, 9],
         'bo', x, freq_L21[:, 10], 'bo', x, freq_L21[:, 11], 'bo', linewidth=2, markersize=2.5, markeredgecolor='none')
ax1.locator_params(axis='x', nbins=4)
ax1.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax1.set_ylabel('Frequency (THz)', fontsize=16)
ax1.set_title('L21', fontsize=16)
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
ax2.plot(x, freq_O[:, 0], 'bo', x, freq_O[:, 1], 'bo', x, freq_O[:, 2], 'bo', x, freq_O[:, 3], 'bo', x, freq_O[:, 4], 'bo', x, freq_O[:, 5], 'bo', x, freq_O[:, 6], 'bo', x,
         freq_O[:, 7], 'bo', x, freq_O[:, 8], 'bo', x, freq_O[:, 9], 'bo', x, freq_O[:, 10], 'bo', x, freq_O[:, 11], 'bo',
         x, freq_O[:, 13], 'bo', x, freq_O[:, 14], 'bo', x, freq_O[:, 15], 'bo', x, freq_O[:, 16], 'bo', x, freq_O[:, 17], 'bo', x, freq_O[:, 18], 'bo', x, freq_O[:, 19], 'bo', x,
         freq_O[:, 20], 'bo', x, freq_O[:, 21], 'bo', x, freq_O[:, 22], 'bo', x, freq_O[:, 23], 'bo', x, freq_O[:, 12], 'bo', linewidth=2, markersize=2.5, markeredgecolor='none')
ax2.locator_params(axis='x', nbins=4)
ax2.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax2.set_title('O', fontsize=16)
##---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
ax3.plot(x, freq_L10[:, 0], 'bo', x, freq_L10[:, 1], 'bo', x, freq_L10[:, 2], 'bo', x, freq_L10[:, 3], 'bo', x, freq_L10[:, 4], 'bo', x, freq_L10[:, 5], 'bo', x, freq_L10[:, 6], 'bo', x,
         freq_L10[:, 7], 'bo', x, freq_L10[:, 8], 'bo', x, freq_L10[:, 9], 'bo', x, freq_L10[:, 10], 'bo', x, freq_L10[:, 11], 'bo',
         x, freq_L10[:, 13], 'bo', x, freq_L10[:, 14], 'bo', x, freq_L10[:, 15], 'bo', x, freq_L10[:, 16], 'bo', x, freq_L10[:, 17], 'bo', x, freq_L10[:, 18], 'bo', x, freq_L10[:, 19], 'bo', x,
         freq_L10[:, 20], 'bo', x, freq_L10[:, 21], 'bo', x, freq_L10[:, 22], 'bo', x, freq_L10[:, 23], 'bo', x, freq_L10[:, 12], 'bo', linewidth=2, markersize=2.5, markeredgecolor='none')
ax3.locator_params(axis='x', nbins=4)
ax3.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax3.set_title('L10', fontsize=16)
plt.figtext(0.125, 0.91, '$\Gamma$')
plt.figtext(0.34, 0.91, '$X$')
plt.figtext(0.3975, 0.91, '$\Gamma$')
plt.figtext(0.6125, 0.91, '$X$')
plt.figtext(0.67, 0.91, '$\Gamma$')
plt.figtext(0.885, 0.91, '$X$')
save_fig_size('CNA_phonon_dispersion', 9, 6, 'pdf')
save_fig_size('CNA_phonon_dispersion', 9, 6, 'eps')

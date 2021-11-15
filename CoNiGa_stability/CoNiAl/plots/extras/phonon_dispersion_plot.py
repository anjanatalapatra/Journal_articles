import sys
sys.path.append("/home/anjana/Dropbox/bin")
from numpy import loadtxt, linspace, arange
from plot_settings import save_fig_size, set_lines_labels
from matplotlib.pyplot import plot, figure, locator_params


freq_L21 = loadtxt('L21_eigenfreq.out')
freq_L10 = loadtxt('L10_eigenfreq.out')
freq_O = loadtxt('O_eigenfreq.out')
x = linspace(0, 1, 50)
print len(x)
plot(x, freq_L21[:,0], 'b', x, freq_L21[:,1], 'r-', x, freq_L21[:,2], 'g-', x, freq_L21[:,3], 'g-', x, freq_L21[:,4], 'g-', x, freq_L21[:, 5], 'g-', x, freq_L21[:, 6], 'g-', x, freq_L21[:,7], 'g-', x, freq_L21[:,8], 'g-', x, freq_L21[:,9], 'g-', x, freq_L21[:,10], 'g-', x, freq_L21[:,11], 'g-', linewidth=2)
locator_params(axis = 'x', nbins = 4)
save_fig_size('L21_phonon_dispersion', 4, 7, 'pdf')
#set_lines_labels(16,[2,2,2,2,2,2,2,2,2,2,2,2,],[2])
figure()
plot(x, freq_L10[:,0], 'b', x, freq_L10[:,1], 'r-', x, freq_L10[:,2], 'g-', x, freq_L10[:,3], 'g-', x, freq_L10[:,4], 'g-', x, freq_L10[:,5], 'g-', x, freq_L10[:,6], 'g-', x, freq_L10[:,7], 'g-', x, freq_L10[:,8], 'g-', x, freq_L10[:,9], 'g-', x, freq_L10[:,10], 'g-', x, freq_L10[:,11], 'g-',linewidth = 2)
save_fig_size('L10_phonon_dispersion', 4, 7, 'pdf')
locator_params(axis = 'x', nbins = 4)
figure()
plot(x, freq_O[:,0], 'b', x, freq_O[:,1], 'r-', x, freq_O[:,2], 'g-', x, freq_O[:,3], 'g-', x, freq_O[:,4], 'g-', x, freq_O[:,5], 'g-', x, freq_O[:,6], 'g-', x, freq_O[:,7], 'g-', x, freq_O[:,8], 'g-', x, freq_O[:,9], 'g-', x, freq_O[:,10], 'g-', x, freq_O[:,11], 'g-',linewidth = 2)
locator_params(axis = 'x', nbins = 4)
save_fig_size('O_phonon_dispersion', 4, 7, 'pdf')


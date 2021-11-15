import sys
sys.path.append("/home/anjanat/Dropbox/bin")
sys.path.append("/home/anjana/Dropbox/bin")

from numpy import loadtxt, linspace
import matplotlib.pyplot as plt
from plot_settings import save_fig_size, set_axis_limits
# -------------------------------------------------------------Phonon DOS Plots---------------------------------------------------------------------------------------------##


f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
pvdos_L21 = loadtxt('CNA_pvdos_L21.out') * 10 ** (12)
nu_L21 = pvdos_L21[:, 0] * 10 ** (-24)
L21_pvdos_Co = (pvdos_L21[:, 2] + pvdos_L21[:, 3])
L21_pvdos_Al = pvdos_L21[:, 4]
L21_pvdos_Ni = pvdos_L21[:, 1]
L21_vdos = L21_pvdos_Co + L21_pvdos_Ni + L21_pvdos_Al
pvdos_O = loadtxt('CNA_pvdos_O.out') * 10 ** (12)
nu_O = pvdos_O[:, 0] * 10 ** (-24)
O_pvdos_Co = pvdos_O[:, 3] + pvdos_O[:, 4] + pvdos_O[:, 5] + pvdos_O[:, 6]
O_pvdos_Al = pvdos_O[:, 7] + pvdos_O[:, 8]
O_pvdos_Ni = pvdos_O[:, 1] + pvdos_O[:, 2]
O_vdos = O_pvdos_Co + O_pvdos_Ni + O_pvdos_Al
pvdos_L10 = loadtxt('CNA_pvdos_L10.out') * 10 ** (12)
nu_L10 = pvdos_L10[:, 0] * 10 ** (-24)
L10_pvdos_Co = pvdos_L10[:, 3] + pvdos_L10[
    :, 4] + pvdos_L10[:, 5] + pvdos_L10[:, 6]
L10_pvdos_Al = pvdos_L10[:, 7] + pvdos_L10[:, 8]
L10_pvdos_Ni = pvdos_L10[:, 1] + pvdos_L10[:, 2]
L10_vdos = L10_pvdos_Co + L10_pvdos_Ni + L10_pvdos_Al
ln1 = ax1.plot(nu_L21, L21_pvdos_Co, 'm--', linewidth=1.5,
               markeredgecolor='none', markersize=3.5, label='Co')
ln2 = ax1.plot(nu_L21, L21_pvdos_Ni, 'g-', linewidth=1.5,
               markeredgecolor='none', markersize=0.5, label='Ni')
ln3 = ax1.plot(nu_L21, L21_pvdos_Al, 'r:',
               label='Al', markeredgecolor='none', markersize=3.5, linewidth=2.5)
ln4 = ax1.plot(nu_L21, L21_vdos, 'b-', label='Total',
               markeredgecolor='none', markersize=3.5, linewidth=2.5)
lns = ln1 + ln2 + ln3 + ln4
labs = [l.get_label() for l in lns]
ln5 = ax2.plot(nu_O, O_pvdos_Co / 2, 'm--', linewidth=1.5,
               markeredgecolor='none', markersize=3.5, label='Co')
ln6 = ax2.plot(nu_O, O_pvdos_Ni / 2, 'g-', linewidth=1.5,
               markeredgecolor='none', markersize=0.5, label='Ni')
ln7 = ax2.plot(nu_O, O_pvdos_Al / 2, 'r:',
               label='Al', markeredgecolor='none', markersize=3.5, linewidth=2.5)
ln8 = ax2.plot(nu_O, O_vdos / 2, 'b-', label='Total',
               markeredgecolor='none', markersize=3.5, linewidth=2.5)
lns2 = ln5 + ln6 + ln7 + ln8
labs2 = [l.get_label() for l in lns2]
ax2.set_ylabel('Phonon DOS ($10^{-12}$)', fontsize=16)
ln9 = ax3.plot(nu_L10, L10_pvdos_Co / 2, 'm--', linewidth=1.5,
               markeredgecolor='none', markersize=3.5, label='Co')
ln10 = ax3.plot(nu_L10, L10_pvdos_Ni / 2, 'g-', linewidth=1.5,
                markeredgecolor='none', markersize=0.5, label='Ni')
ln11 = ax3.plot(nu_L10, L10_pvdos_Al / 2, 'r:',
                label='Al', markeredgecolor='none', markersize=3.5, linewidth=2.5)
ln12 = ax3.plot(nu_L10, L10_vdos / 2, 'b-',
                label='Total', markeredgecolor='none', markersize=3.5, linewidth=2.5)
lns3 = ln9 + ln10 + ln11 + ln12
labs3 = [l.get_label() for l in lns3]
plt.xlabel('Frequency (THz)', fontsize=16)
leg = plt.legend(bbox_to_anchor=(0.00, 3), loc='upper left', borderaxespad=0.)
# leg.get_frame().set_visible(False)
f.subplots_adjust(hspace=0)
plt.figtext(0.85, 0.85, '$L2_1$', fontsize=16)
plt.figtext(0.85, 0.57, '$O$', fontsize=16)
plt.figtext(0.85, 0.29, '$L1_0$', fontsize=16)
set_axis_limits(0, 5)
plt.ylim(0, 12)
save_fig_size('CNA_pvdos_all', 10, 8, 'pdf')
#save_fig_size('CNA_pvdos_all', 10, 8, 'eps')
# -------------------------------------------------------------Phonon Dispersion Plots---------------------------------------------------------------------------------------------##
freq_L21 = loadtxt('L21_eigenfreq.out') * 10 ** (-12)
freq_L10 = loadtxt('L10_eigenfreq.out') * 10 ** (-12)
freq_O = loadtxt('O_eigenfreq.out') * 10 ** (-12)
n = len(freq_O[:, 0])
x = linspace(0, 1, n)
y = linspace(0, 0, n)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
plt.figure()
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.plot(
    x, freq_L21[:, 0], 'bo', x, freq_L21[:, 1], 'bo', x, freq_L21[:, 2], 'bo', x, freq_L21[:, 3], 'bo', x, freq_L21[
        :, 4], 'bo', x, freq_L21[:, 5], 'bo', x, freq_L21[:, 6], 'bo', x, freq_L21[:, 7], 'bo', x, freq_L21[:, 8], 'bo', x, freq_L21[:, 9],
    'bo', x, freq_L21[:, 10], 'bo', x, freq_L21[:, 11], 'bo',  x, y, 'k--', linewidth=2, markersize=2.5, markeredgecolor='none')
ax1.locator_params(axis='x', nbins=4)
ax1.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax1.set_ylabel('Frequency (THz)', fontsize=16)
ax1.set_title('L21', fontsize=16)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
ax2.plot(
    x, freq_O[:, 0], 'bo', x, freq_O[:, 1], 'bo', x, freq_O[:, 2], 'bo', x, freq_O[
        :, 3], 'bo', x, freq_O[:, 4], 'bo', x, freq_O[:, 5], 'bo', x, freq_O[:, 6], 'bo', x,
    freq_O[:, 7], 'bo', x, freq_O[:, 8], 'bo', x, freq_O[
        :, 9], 'bo', x, freq_O[:, 10], 'bo', x, freq_O[:, 11], 'bo',
    x, freq_O[:, 13], 'bo', x, freq_O[:, 14], 'bo', x, freq_O[:, 15], 'bo', x, freq_O[
        :, 16], 'bo', x, freq_O[:, 17], 'bo', x, freq_O[:, 18], 'bo', x, freq_O[:, 19], 'bo', x,
    freq_O[:, 20], 'bo', x, freq_O[:, 21], 'bo', x, freq_O[:, 22], 'bo', x, freq_O[:, 23], 'bo', x, freq_O[:, 12], 'bo',  x, y, 'k--', linewidth=2, markersize=2.5, markeredgecolor='none')
ax2.locator_params(axis='x', nbins=4)
ax2.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax2.set_title('O', fontsize=16)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##
ax3.plot(
    x, freq_L10[:, 0], 'bo', x, freq_L10[:, 1], 'bo', x, freq_L10[:, 2], 'bo', x, freq_L10[
        :, 3], 'bo', x, freq_L10[:, 4], 'bo', x, freq_L10[:, 5], 'bo', x, freq_L10[:, 6], 'bo', x,
    freq_L10[:, 7], 'bo', x, freq_L10[:, 8], 'bo', x, freq_L10[
        :, 9], 'bo', x, freq_L10[:, 10], 'bo', x, freq_L10[:, 11], 'bo',
    x, freq_L10[:, 13], 'bo', x, freq_L10[:, 14], 'bo', x, freq_L10[:, 15], 'bo', x, freq_L10[
        :, 16], 'bo', x, freq_L10[:, 17], 'bo', x, freq_L10[:, 18], 'bo', x, freq_L10[:, 19], 'bo', x,
    freq_L10[:, 20], 'bo', x, freq_L10[:, 21], 'bo', x, freq_L10[:, 22], 'bo', x, freq_L10[:, 23], 'bo', x, freq_L10[:, 12], 'bo',  x, y, 'k--', linewidth=2, markersize=2.5, markeredgecolor='none')
ax3.locator_params(axis='x', nbins=4)
ax3.set_xlabel('$[\\xi,\\xi,0]$', fontsize=16)
ax3.set_title('L10', fontsize=16)
plt.figtext(0.125, 0.91, '$\Gamma$')
plt.figtext(0.34, 0.91, '$X$')
plt.figtext(0.3975, 0.91, '$\Gamma$')
plt.figtext(0.6125, 0.91, '$X$')
plt.figtext(0.67, 0.91, '$\Gamma$')
plt.figtext(0.885, 0.91, '$X$')
save_fig_size('CNA_phonon_dispersion', 8, 6, 'pdf')
#save_fig_size('CNA_phonon_dispersion', 9, 6, 'eps')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------##

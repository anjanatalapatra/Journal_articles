import sys
sys.path.append("/home/anjana/Dropbox/bin")
from numpy import loadtxt, arange, nan, linspace
from scipy import interpolate
from plot_settings import save_fig_size, legend
from pylab import plot, xlabel, ylabel, xlim, ylim
from matplotlib.pyplot import figure


GGA = loadtxt('GGA_heusler_CoNiAl_burgers_energy.dat')
LDA = loadtxt('LDA_heusler_CoNiAl_burgers_energy.dat')
x_GGA = GGA[:, 0]
y_GGA = GGA[:, 1]
x_LDA = LDA[:, 0]
y_LDA = LDA[:, 1]
f_GGA = interpolate.interp1d(
    x_GGA, y_GGA, kind='cubic', axis=-1, copy=True, bounds_error=True, fill_value=nan)
f_LDA = interpolate.interp1d(
    x_LDA, y_LDA, kind='cubic', axis=-1, copy=True, bounds_error=True, fill_value=nan)
xnew = arange(0, 1.55, 0.05)
ynew = f_GGA(xnew)
yLDA = f_LDA(xnew)
# y_0 = arange(-120, 60, 0.05)
# x_0 = ones_like(y_0)
plot(xnew, (ynew - ynew[0]) * 1000, 'b-o', xnew, (yLDA - yLDA[0]) * 1000, 'r-s')
xlabel('Reaction coordinate (Burgers path)', fontsize=16)
ylabel('Energy[meV/f.u]', fontsize=16)
legend('GGA', 'LDA', 2)
#save_fig_size('CNA_1D_burger_path', 8, 7, 'eps')
save_fig_size('CNA_1D_burger_path', 8, 7, 'png')
# --------------------------------------------------------------------------------------------------------------#
figure()
inverse_GGA = loadtxt('GGA_inverse_CoNiAl_burgers_energy.dat')
inverse_2D = loadtxt('GGA_inverse_CoNiAl_burgers_energy_2D.dat')
x_i_GGA = inverse_GGA[:, 0]
y_i_GGA = inverse_GGA[:, 1]
f_i_GGA = interpolate.interp1d(
    x_i_GGA, y_i_GGA, kind='cubic', axis=-1, copy=True, bounds_error=True, fill_value=nan)
e_i_2D = inverse_2D[:, 2]
x_2D = linspace(0, 1, num=50)
print len(x_2D)
print len(e_i_2D)
xnew = arange(0, 1.45, 0.05)
ynew = f_GGA(xnew)
yi_GGA = f_i_GGA(xnew)
plot(xnew, (ynew - ynew[0]) * 1000, 'b-o', xnew, (
    yi_GGA - yi_GGA[0]) * 1000, 'm-s')
xlim(0, 1.45)
xlabel('Reaction coordinate (Burgers path)', fontsize=16)
ylabel('Energy[meV/f.u]', fontsize=16)
legend('Heusler', 'Inverse heusler', 0)
#save_fig_size('CNA_heusler_inverse_heusler', 8, 7, 'eps')
save_fig_size('CNA_heusler_inverse_heusler', 8, 7, 'png')
# --------------------------------------------------------------------------------------------------------------#
fig = figure()
bain_heusler = loadtxt('heusler_ca_energy.dat')
x_h_bain = bain_heusler[:, 0]
y_h_bain = bain_heusler[:, 1]
ax = fig.add_subplot(111)
ln1 = ax.plot(xnew, (ynew - ynew[0]) * 1000, 'b-o', label='Burgers path')
ax.plot(1.1, (-24.18345 - ynew[0]) * 1000, 'b-o')
ax2 = ax.twiny()
ln2 = ax2.plot(x_h_bain, (y_h_bain - y_h_bain[
               9]) * 4000, 'r-s', label='Bain path')
lns = ln1 + ln2
labs = [l.get_label() for l in lns]
leg = ax.legend(lns, labs, loc=1)
leg.get_frame().set_visible(False)
ax.set_xlabel("Reaction coordinate (Burgers path)", fontsize=16)
ax.set_ylabel(r"Energy[meV/f.u]", fontsize=16)
ax2.set_xlabel("c/a ratio (Bain path)", fontsize=16)
#save_fig_size('CNA_burger_bain', 8, 7, 'eps')
save_fig_size('CNA_burger_bain', 8, 7, 'png')
# --------------------------------------------------------------------------------------------------------------#
fig = figure()
bain_inverse = loadtxt('inverse_ca_energy.dat')
x_i_bain = bain_inverse[:, 0]
y_i_bain = bain_inverse[:, 1]
ax = fig.add_subplot(111)
ln1 = ax.plot(xnew, (yi_GGA - yi_GGA[0]) * 1000, 'b-o', label='Burgers path')
# ln3 = ax.plot(x_2D, e_i_2D * 1.5, 'b-o', label='2D Burgers path')
ax2 = ax.twiny()
ln2 = ax2.plot(x_i_bain, (y_i_bain - y_i_bain[
               10]) * 4000, 'r-s', label='Bain path')
lns = ln1 + ln2  # + ln3
labs = [l.get_label() for l in lns]
leg = ax.legend(lns, labs, loc=1)
leg.get_frame().set_visible(False)
ax.set_xlabel("Reaction coordinate (Burgers path)", fontsize=16)
ax.set_ylabel(r"Energy[meV/f.u]", fontsize=16)
ax.set_xlim(0, 1)
ylim(-165, 65)
ax2.set_xlabel("c/a ratio (Bain path)", fontsize=16)
#save_fig_size('CNA_inverse_burger_bain', 8, 7, 'eps')
save_fig_size('CNA_inverse_burger_bain', 8, 7, 'png')
# --------------------------------------------------------------------------------------------------------------#
fig = figure()
D2 = loadtxt('GGA_heusler_CoNiAl_burgers_energy_2D.dat')
D2_inv = loadtxt('GGA_inverse_CoNiAl_burgers_energy_2D.dat')
x_2D = linspace(0, 1, num=50)
y_2D = D2[:, 2] * 1.26
x_i_2D = linspace(0, 1, num=50)
y_i_2D = D2_inv[:, 2] * 1.5
ax = fig.add_subplot(111)
ln1 = ax.plot(x_i_2D, (y_i_2D - y_i_2D[
              0]), 'r-s', label='Inverse Heusler-CoNiAl')
ln2 = ax.plot(x_2D, (y_2D - y_2D[0]), 'b-o', label='Heusler-CoNiAl')
lns = ln1 + ln2
labs = [l.get_label() for l in lns]
leg = ax.legend(lns, labs, loc=1)
leg.get_frame().set_visible(False)
ax.set_xlabel("Reaction coordinate (Burgers path)", fontsize=16)
ax.set_ylabel(r"Energy[meV/f.u]", fontsize=16)
ax2.set_xlabel("c/a ratio (Bain path)", fontsize=16)
#save_fig_size('CNA_2D_burger', 8, 7, 'eps')
save_fig_size('CNA_2D_burger', 8, 7, 'png')
# --------------------------------------------------------------------------------------------------------------#

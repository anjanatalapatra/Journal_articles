import sys
sys.path.append("/home/anjanat/Dropbox/bin")
sys.path.append("/home/anjana/Dropbox/bin")
import numpy as np
from plot_settings import *

def main():
	bain_heusler = np.loadtxt('ca_energy.dat')
	bain_inverse = np.loadtxt('ca_energy_inverse.dat')
	x_h = bain_heusler[:, 0]
	y_h = (bain_heusler[:, 1] + 5.99799)*1000
	x_i = bain_inverse[:, 0]
	y_i = (bain_inverse[:, 1]+ 6.03338325)*1000
	plot(x_h, y_h, 'b-o', x_i, y_i, 'r-s')
	xlabel('c/a ratio')
	ylabel('Energy[meV/atom]')
	legend('$Co-Ni-Al: heusler $','$Co-Ni-Al:inverse $',0)
	set_lines_labels(16,[2,2],[5,5])
	#set_axis_limits(0,5)
	save_fig_size('CoNiAl_bain',8,7,'pdf')
	#fig = plt.figure()

if __name__ == '__main__':
		main()

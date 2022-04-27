from ligotools import utils
from scipy.interpolate import interp1d

strain_H1, time_H1, chan_dict_H1 = loaddata('../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')


def test_whiten_len():
	Pxx_H1 = np.zeros(8193)
	freqs = np.zeros(8193)
	dt = time_H1[1] - time_H1[0]
	psd_H1 = interp1d(freqs, Pxx_H1)
	strain_H1_whiten = whiten(strain_H1,psd_H1,dt)
	assert len(strain_H1_whiten) == 131072

def test_write_wavfile_is_none():
    w_test = write_wavfile('audio/test.wav',int(4096), np.zeros(16384))
	assert w_test == None

def test_reqshift_len():
    assert len(reqshift(np.zeros(131072))) == 131072
	
def test_plotting_utility():
	assert plotting_utility('eventname')=='eventname'
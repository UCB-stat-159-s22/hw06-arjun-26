from ligotools import readligo


strain_H1, time_H1, chan_dict_H1 = loaddata('../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')

def test_loaddata_strain_len():
	assert len(strain_H1) == 131072
	
def test_loaddata_time_len():
    assert len(time_H1) == 131072

def test_loaddata_chandict_len():
    assert len(chan_dict_H1) == 13
	
def test_loaddata_chandict_type():
    assert type(chan_dict_H1) == 'dict'

	
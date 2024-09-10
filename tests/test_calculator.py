import numpy as np 
import sarathi

def test_age_estimator():
	param = sarathi.param()
	t0 = sarathi.age_estimator(param, 0)
	assert np.abs(t0-13.74)<0.01
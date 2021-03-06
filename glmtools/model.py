import numpy as np
from glmtools.make_xdsgn import DesignSpec
from scipy import stats, signal
import numpy.random as rnd
from matplotlib import pyplot as plt

class GLM:
	'''
	compute the response of glm to stimulus Stim

	Dynamics:  Filters the Stimulus with glmprs.k, passes this through a
	nonlinearity to obtain the point-process conditional intensity.  Add a
	post-spike current to the linear input after every spike.

	'''
	def __init__(self, dt, k, h, dc):
		'''

		:param k: stimulus filter
		:param h: post-spike filter
		'''
		self.k_ = np.asarray([k.T])
		self.h_ = h
		self.dc_ = dc
		self.dt_ = dt

	def simulate(self, stim):

		nlfun = lambda x: np.exp(x)

		nbins_per_eval = 1  	# Default number of bins to update for each spike

		dt = self.dt_			# bin size for simulation
		slen = len(stim)  		# length of stimulus
		rlen = slen		  		# length of binned spike response

		hlen = len(self.h_)		# length of post-spike filter

		nx = len(stim) 			# must have a second dimension for convolve2d to word
		_, nf = self.k_.shape

		istm = np.convolve(stim.squeeze(), np.flipud(self.k_.squeeze()), mode='full')
		istm = istm[:slen] + self.dc_

		# trim off the extra zeros afterward
		itot = np.concatenate((np.copy(istm.squeeze()), np.zeros_like(self.h_)))			# this will be the total filter output after postspike filter is added
		hcurr = np.zeros_like(itot)

		sps = np.zeros_like(itot)

		refreshRate = 1 / dt


		# loop through all times
		for iinxt in range(len(istm)):
			rrnxt = nlfun(itot[iinxt])			# pass through nonlinear function

			# if our current filter output passed through exp nonlinerity is not greater than random number don't spike
			if np.random.rand() < (1-np.exp(-rrnxt)):
				ispk = iinxt
				sps[ispk] = 1

				mxi = ispk + hlen

				ii_postspk = np.arange(ispk, mxi)

				if len(ii_postspk):
					itot[ii_postspk] = itot[ii_postspk] + self.h_
					hcurr[ii_postspk] += self.h_

		# trim off zero padding
		hcurr = hcurr[range(0, slen)]
		itot = itot[range(0, slen)]
		sps = sps[range(0, slen)]

		tsp = np.where(sps > 0)[0]
		return tsp, sps, istm, hcurr

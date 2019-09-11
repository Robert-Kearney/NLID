"""Module for nldat."""

class nldat(nltop):
	"""class nldat, data class for NLID library."""
	
	def __init__(self, dataset, *args, **kwargs):
		"""
		Init function for nltop.
		Args:
		Returns:
			None
		"""
		super(nldat, self).__init__(*args, **kwargs)
		self.chan_names = []
		dataset_shape = np.shape(dataset)
		n_samp = 0
		n_chan = 0
		n_real = 0
		if len(dataset_shape)==1:
			n_samp = dataset_shape[0]
		if len(dataset_shape)==2:
			n_samp = dataset_shape[0]
			n_chan = dataset_shape[1]
		if len(dataset_shape)==3:
			nsamp = dataset_shape[0]
			n_chan = dataset_shape[1]
			n_real = dataset_shape[2]
		self.dataset = dataset
		for chan_idx in range(n_chan):
			self.chan_names.append()

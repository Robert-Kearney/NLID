"""Module for nldat."""

class nldat(nltop):
	"""class nldat, data class for NLID library."""
	
	def __init__(self, *args, **kwargs):
		"""
		Init function for nltop.
		Args:
		Returns:
			None
		"""
		super(nldat, self).__init__(*args, **kwargs)
		self.chan_units = "Default Units"
		self.domain_incr = 1
		self.domain_start = 0
		self.domain_values = None
		self.data_size = None
		self.n_samp = 0
		self.n_chan = 0
		self.n_real = 0
		self.dataset = kwargs.get("dataset", None)
		chan_base_name = kwargs.get("chan_name", "x")
		self.data_size = np.shape(self.dataset)
		if len(self.data_size)==1:
			self.n_samp = dataset_shape[0]
		if len(self.data_size)==2:
			self.n_samp = dataset_shape[0]
			self.n_chan = dataset_shape[1]
		if len(self.data_size)==3:
			self.nsamp = dataset_shape[0]
			self.n_chan = dataset_shape[1]
			self.n_real = dataset_shape[2]
		self.chan_names = ["{}_{}".format(chan_base_name, x)
						   for x in range(n_chan)]
		

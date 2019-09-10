"""Module for nltop."""

class nltop(object):
	"""class nltop, parent class for all NLID classes."""
	
	def __init__(self, comment=None, version=None):
		"""
		Init function for nltop.
		Args:
			comment(string): comment
			version(string): version
		Returns:
			None
		"""
		if comment is None:
			comment = "Default comment"
		if version is None:
			version = "2.01"
		self.comment = comment
		self.version = version

	def set(self, **kwargs):
		"""
		Set function.
		Args:
			key worded arguemnts.
		Returns:
			None
		"""
		for key, value in kwargs.items():
			# Check to see if it is an attribute
			if hasattr(self, key):
				self.key = value
			elif hasattr(self, "parameter_set"):
				# Check to see if it is a parameter value
                # Must change so that handles parameters of different
                # names.
				self.parameter_set[key] = value
			else:
				NltopException("{} is not an attribute or a parameter".format(key))

	def get(self, key):
		"""
		Get all public attributes and their values.
		Args:
			key(string): attribute name
		Returns:
			value (string, float, ?)
		"""
		if hasattr(self, "parameter_set"):
			if key in self.parameter_set.keys:
				return self.parameter_set[key]
		if hasattr(self, key):
			return self.key
		NltopException("{} is not an attribute or a parameter".format(key))
					

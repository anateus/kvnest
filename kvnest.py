class KVNest(str):
	def __getitem__(self,key):
		return ':'.join((self,key))
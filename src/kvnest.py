from functools import partial
import inspect

class KVNest(str):
	"""A subclass of str that allows namespacing keys for use in redis as well as provide partial methods into redis."""

	def __new__(cls,*args,**kwargs):
		"""Override's str's __new__ so we can store the redis connection if one is provided"""
		if 'connection' in kwargs:
			connection = kwargs['connection']
			del kwargs['connection']

		obj = super(KVNest,cls).__new__(cls,*args,**kwargs)
		if 'connection' in locals():
			obj._redis = connection

		return obj
		
	def __getitem__(self,key):
		"""Concatenates the key and returns a new KVNest instead of indexing into the string"""
		return KVNest(':'.join((self,key)))

	def __getattribute__(self,name):
		"""Transparently returns partially applied versions of redis methods."""
		try:
			return super(KVNest,self).__getattribute__(name)
		except AttributeError, e:
			return partial(getattr(self._redis,name),str(self))
			# return super(KVNest,self).__getattribute__(name)
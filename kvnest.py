from functools import partial
import inspect

class KVNest(str):
	def __new__(cls,*args,**kwargs):
		if 'connection' in kwargs:
			connection = kwargs['connection']
			del kwargs['connection']

		obj = super(KVNest,cls).__new__(cls,*args,**kwargs)
		if 'connection' in locals():
			obj._redis = connection

		return obj
		
	def __getitem__(self,key):
		return KVNest(':'.join((self,key)))

	def __getattribute__(self,name):
		"""Transparently returns partially applied versions of redis methods."""
		
		# if we're not looking for the redis connection and we do have a connection, look to see if this exists within redis
		if name!='_redis' and hasattr(self,'_redis') and hasattr(self._redis, name): 
			
			redis_attr = getattr(self._redis,name)

			if inspect.ismethod(redis_attr) and 'redis' in redis_attr.im_class.__name__.lower():
				return partial(redis_attr,str(self))
			else:
				return super(KVNest,self).__getattribute__(name)
		else:
			return super(KVNest,self).__getattribute__(name)
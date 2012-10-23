kvnest
======

Objected Oriented Keys for Redis ... in Python.

This is a Python re-implementation of the Ruby [Nest](https://github.com/soveran/nest) library. One of the authors, [Michel Martens](https://github.com/soveran), hyped me to it his [RedisConf 2012](http://redisconf.com/) talk.

Usage
-----

This is the standard behavior:

    >>> k = KVNest('user')
    'user'
    >>> k['1']
    'user:1'
    >>> k['1']['friends']
    'user:1:friends'

But it also provides partially applied methods on redis. That is:

    >>> import redis
    >>> r = redis.Redis()
    >>> k = KVNest('foo',connection=r)
    >>> r.set('foo','bar')
    True
    >>> r.get('foo')
    'bar'

Now here's the cool part: 

    >>> k.get()
    'bar'

To Do
-----

* Add the structure necessary to make this easily installable as a package
* I do the pass-through to redis in an incredibly unsafe way, find a safer way!
* Think of a better name for this library


License
-------

Copyright (c) 2012 Michael katsevman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

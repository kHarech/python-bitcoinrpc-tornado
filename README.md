Async python BitcoinRPC for tornado
===================================

AsyncAuthServiceProxy is async version of AuthServiceProxy.

It can be used with tornado ioloop.

Usage example
-------------

    from bitcoinrpc_async.authproxy import AsyncAuthServiceProxy
    from tornado import ioloop, gen

    BITCOIN_RPC_URL = "http://user:password@127.0.0.1:8332"

    @gen.coroutine
    def show_block_count():
        service = AsyncAuthServiceProxy(BITCOIN_RPC_URL)
        result = yield service.getblockcount()
        print result

    io_loop = ioloop.IOLoop.instance()
    io_loop.add_callback(show_block_count)
    io_loop.start()

Install
-------

    # clone this repo, and run
    python setup.py install

Or using pip:

    pip install -e git://github.com/st4lk/python-bitcoinrpc-tornado.git#egg=bitcoinrpc_async_dev


AuthServiceProxy is an improved version of python-jsonrpc.

It includes the following generic improvements:

- HTTP connections persist for the life of the AuthServiceProxy object
- sends protocol 'version', per JSON-RPC 1.1
- sends proper, incrementing 'id'
- uses standard Python json lib

It also includes the following bitcoin-specific details:

- sends Basic HTTP authentication headers
- parses all JSON numbers that look like floats as Decimal

Installation:

- change the first line of setup.py to point to the directory of your installation of python 2.*
- run setup.py

Note: This will only install bitcoinrpc. If you also want to install jsonrpc to preserve 
backwards compatibility, you have to replace 'bitcoinrpc' with 'jsonrpc' in setup.py and run it again.

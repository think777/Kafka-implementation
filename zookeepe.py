import logging
from kazoo.client import KazooClient

#zookeeper starting
zk = KazooClient(hosts='127.0.0.1:6969')
zk.start()
zk.stop()
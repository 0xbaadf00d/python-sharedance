# -*- coding: utf-8 -*-
from struct import pack
import socket
import json


class   Sharedance:
    def __init__(self, host='localhost', port=1042, timeout=5):
        self._host = host
        self._port = port
        self._timeout = timeout if timeout > 0 else 5

    def __del__(self):
        self._hSock.close()

    def __connect(self):
        self._hSock = socket.socket()
        self._hSock.settimeout(self._timeout)
        self._hSock.connect((self._host, self._port))

    def Set(self, key, value):
        self.__connect()
        try:
            key = str(key)
            value = json.dumps(value)
            v_len = len(value)
            k_len = len(key)
            data  = 'S'
            data += pack("cccccccc", 
                         chr((k_len >> 24) & 0xff),
                         chr((k_len >> 16) & 0xff),
                         chr((k_len >> 8) & 0xff),
                         chr(k_len & 0xff),
                         chr((v_len >> 24) & 0xff),
                         chr((v_len >> 16) & 0xff),
                         chr((v_len >> 8) & 0xff),
                         chr(v_len & 0xff))
            data += key
            data += value
            self._hSock.send(data)
            ret = self._hSock.recv(50)
            if ret.strip() == "OK":
                return True
        except:
            pass
        return False

    def Fetch(self, key):
        self.__connect()
        try:
            key = str(key)
            k_len = len(key)
            data  = 'F'
            data += pack('cccc',
                         chr((k_len >> 24) & 0xff),
                         chr((k_len >> 16) & 0xff),
                         chr((k_len >> 8) & 0xff),
                         chr(k_len & 0xff))
            data += key
            self._hSock.send(data)
            value = self._hSock.recv(4096)
            value = json.loads(value)
        except:
            value = None
        return value

    def Delete(self, key):
        self.__connect()
        try:
            key = str(key)
            k_len = len(key)
            data  = 'D'
            data += pack('cccc',
                         chr((k_len >> 24) & 0xff),
                         chr((k_len >> 16) & 0xff),
                         chr((k_len >> 8) & 0xff),
                         chr(k_len & 0xff))
            data += key
            self._hSock.send(data)
            ret = self._hSock.recv(50)
            if ret.strip() == "OK":
                return True
        except:
            pass
        return False

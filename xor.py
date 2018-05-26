import os
from binascii import hexlify
import array
import binascii


def xor(a, b):
	return bytes([c ^ d for c, d in zip(a, b)])
	# li = []
	# string = ""
	# for byte1, byte2 in zip(a, b):
	# 	li.append(bytes(byte1 ^ byte2))
	# 	# binascii.unhexlify((bytes((byte1 ^ byte2))).decode('utf8'))
	# for item in li:

	# # return str(array.array('B', li).tostring())


def encrypt(key, plaintext):
    # Because input is a hex string, we convert to raw bytes to do XOR
    return xor(bytearray.fromhex(key), bytearray.fromhex(plaintext))


def decrypt(key, ciphertext):
    # Because input is a hex string, we convert to raw bytes to do XOR
    return xor(bytearray.fromhex(key), bytearray.fromhex(ciphertext))


def hex_encode(string):
    """Helper function to encode strings to hexstrings"""
    # Python has flaws, unless i'm doing something wrong..
    return hexlify(string.encode('utf-8')).decode('utf-8')


PLAINTEXT = "HELLO"
KEY = hexlify(os.urandom(len(PLAINTEXT))).decode('utf-8')

assert decrypt(KEY, encrypt(KEY, hex_encode(PLAINTEXT))) == hex_encode(PLAINTEXT)
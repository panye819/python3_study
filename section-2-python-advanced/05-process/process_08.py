#!/user/bin/python3
#!coding=utf-8
from multiprocessing import Process
import time

def test():
	for i in range(5):
		print("---test---")
		time.sleep(1)

p = Process(target=test)

p.start()

#!/user/bin/python3
#!coding=utf-8

import time
import threading

def  display():
	print("Happy every day!!")
	time.sleep(1)

if __name__ == '__main__':
	for x in xrange(5):
		t=threading.Thread(target=display)
		t.start()

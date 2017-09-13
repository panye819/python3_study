#!/user/bin/python3
#!coding=utf-8

import time
import threading

class  MyThread(threading.Thread):
	def run(self):
		for i in range(3):
			time.sleep(1)
			msg="I'm "+self.name+" @ "+str(i)
			print(msg)
def test():
	for i in range(5):
		t=MyThread()
		t.start()


if __name__ == '__main__':
	test()

#!/user/bin/python3
#!coding=utf-8
from multiprocessing import Process
import time

def test():
	i=0
	while i<4:
		print("---test---")
		time.sleep(1)
		i+=1

p=Process(target=test)
p.start()

a=0
while a<5:
	print("--main--")
	time.sleep(1)
	a+=1


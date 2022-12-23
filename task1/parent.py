import os
import random as rnd
import time
import sys

class Parent:
	@staticmethod
	def work(fork_count: int):
		processes = []
		for i in range(1, fork_count + 1):
			child_pid = os.fork()
			if child_pid == 0:
				rand_num = rnd.randint(5,10)
				os.execl(sys.executable, sys.executable, "child.py", str(rand_num))
			else:
				print('Parent[', os.getpid(), ']: I ran children process with PID', child_pid, '.')
				processes.append(child_pid)
		while processes:
			child_pid, exit_code = os.wait()
			if child_pid == 0:
				rand_num = rnd.randint(1, 10)
				time.sleep(rand_num)
			else:
				print('Parent[', os.getpid(), ']: Child with PID', child_pid, 'terminated. Exit Status', exit_code, '.')
				processes.remove(child_pid)

def main():
	Parent.work(int(sys.argv[1]))



main()

from multiprocessing import Process
import os

#创建子进程
def run_proc(name):
	print('Run child precess %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')
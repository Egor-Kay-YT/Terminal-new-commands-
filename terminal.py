from os import *
while True:
	path = getcwd() + ' $ '
	command = input(path)
	system(command)
	if command == 'test':
		print('test')
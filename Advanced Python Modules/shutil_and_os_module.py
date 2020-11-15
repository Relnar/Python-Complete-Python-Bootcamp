import os
import shutil

def main():
	print(os.getcwd())

	f = open('pratice.txt', 'w+')
	f.write('This is test string')
	f.close()

	print(os.listdir('/Users'))

	#shutil.move('pratice.txt', '/Advanced Python Modules')

	for folder, sub_folders, files in os.walk('/Advanced Python Modules'):
		print(f"{folder}")
		for sub_fold in sub_folders:
			print(f"{sub_fold}")
		for f in files:
			print(f"{f}")


if __name__ == "__main__":
	main()
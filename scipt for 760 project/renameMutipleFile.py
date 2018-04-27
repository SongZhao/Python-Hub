import subprocess
import sys
import os

fstring1 = "subj"
fstring2 = "_T1w_raw.nii"

def rename(x, y, z):
	change = False
	count = x
	for i in range(x, y):
		files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
		##print files
		for file in files:
			s = ''
			oFile = ''
			##print file
			if z < 10:
				s = 'sub-0' + str(z)
			else:
				s = 'sub-' + str(z)
			if s in file:
				print file
				print s
				if(count < 1000):
					num = '0' + str(count)
				else:
					num = str(count)
				oFile = fstring1 + num + fstring2 
				print oFile
				os.system("mv"+" " + file + " " + oFile)
		count += 1
		z += 1

def main():
	args = [arg for arg in sys.argv]
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	z = int(sys.argv[3])
	rename(x,y,z)


if __name__ == '__main__':
	main()
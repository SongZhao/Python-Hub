import wget   # sudo pip install wget
import gzip
import os
import shutil

outpath = "/home/song/Desktop/data760/ds105"
extract = "/home/song/Desktop/"

def main():
	os.mkdir(outpath)
	for path, folders, files in os.walk("/home/song/Desktop/ds000105_R2.0.2"):
		if "anat" in path:
				for zipFile in files:
					if "T1" in zipFile:
						zipFilePath = os.path.join(path,zipFile)
						print zipFilePath
						zipFile = zipFile[:-3]
						with gzip.open(zipFilePath, 'rb') as f_in:
							with open(os.path.join(outpath, zipFile), 'wb') as f_out:
								shutil.copyfileobj(f_in, f_out)
						#sFile = extract + zipFile
						#shutil.copy2(sFile, outpath)	

	print "completed"



if __name__ == '__main__':
	main()





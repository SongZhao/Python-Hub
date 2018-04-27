import wget

x = ""

def get():
	for i in range(10,17):
		x = "https://s3.amazonaws.com/openneuro/ds000117/ds000117_R1.0.0/uncompressed/sub-%d/ses-mri/anat/sub-%d_ses-mri_acq-mprage_T1w.nii" % (i,i)
		print x

		wget.download(x) 


get()

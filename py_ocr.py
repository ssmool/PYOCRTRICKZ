#asytrick
#github.com/ssmool
#eusmool@gmail.com
import easyocr

def getOCR(file_x):
	reader = easyocr.Reader(['ch_sim','en'])
	temp_x = open(file_x,'rb')
	srx_x = temp_x.read()
	r_x = reader.readtext(srx_x)
	x_t = 'str'
	lx = ''
	return r_x

def getOCRText(data):
	x_t = 'str'
	r_x = ''
	for index in data:
		for node in index:
			if(type(node) == type(x_t)):
				print(node)
				r_x += f'{str(node)} '
	return str(r_x).lower()

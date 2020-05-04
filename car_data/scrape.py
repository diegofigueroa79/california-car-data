import PyPDF2 as pypdf
import requests


def download_pdf(url_string):

	doc = requests.get(url)
	
	if doc.status_code == 200:
		with open('car_data.pdf', 'wb') as file:
			file.write(doc.content)
		return doc
	else:
		print("HTTP Response Status Code: " + str(doc.status_code))
		
	#return doc

def extract_text(pdf_path):

	pdfFileObj = open(pdf_path, 'rb')
	pdfReader_obj = pypdf.PdfFileReader(pdfFileObj)
	
	return pdfReader_obj

if __name__ == '__main__':
	
	url = 'https://www.dmv.ca.gov/portal/wcm/connect/fafd3447-8e14-4ff6-bb98-e85f3aa9a207/ca_dmv_stats.pdf?MOD=AJPERES&CVID='
	
	mypdf = download_pdf(url)

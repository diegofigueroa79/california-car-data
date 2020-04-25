import PyPDF2 as pypdf
import requests


url = 'https://www.dmv.ca.gov/portal/wcm/connect/fafd3447-8e14-4ff6-bb98-e85f3aa9a207/ca_dmv_stats.pdf?MOD=AJPERES&CVID='

doc = requests.get(url)
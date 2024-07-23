import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
	url = 'https://www.google.com/'
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		print(url)
		resp = requests.get(url, timeout = 10)
		resp.text
		resp.status_code
		print(f'Connection to {url} was successful.')
		return True
	except ConnectionError as e:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	except:
		print(f'Failed with unparsed reason.')
		return False

internet_connection_test()


import sys
print(sys.executable)

import sys
sys.path.append(r'C:\Users\infinitt\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages')
import requests
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

url = 'Put here the URL of the API Application'
params = {
    'client_id': 'if there is parameters in URL',
    'client_secret': 'if there is parameters in URL'
}

proxy = {
    'http': 'http://proxyip',
    'https': 'http://proxyip'
}
#here to disable the SSL Warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

num_requests = 0
total_time = 0

for barcodes in range(931320, 931450):
    data = {
        'method': 'checkCoolerByBarcode',
        'barcode': str(barcodes)
    }

    start_time = time.time()
    # Send POST request with query parameters, JSON data, and proxy
    response = requests.post(url, json=data, params=params, proxies=proxy, verify=False)
    elapsed_time = time.time() - start_time
    total_time += elapsed_time
    num_requests += 1
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the response content
        data = response.json()  # Assuming the API returns JSON data
        specific_value = data['IsSuccess'] # you can change this depend on the data response. in this case i have to get the IsSuccess record which indicate to ture of false for barcode
        
        print(f'Response for barcode {barcodes}: {specific_value}')
        
    else:
        print(f'Request for barcode {barcodes} was not successful. Status code: {response.status_code}')

average_time = total_time / num_requests
print(f'\nNumber of requests: {num_requests}')
print(f'Total time spent: {total_time} seconds')
print(f'Average time per request: {average_time} seconds')

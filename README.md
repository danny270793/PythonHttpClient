# HttpClient
A HttpCliente library for python, this library is a wrapper for urllib library
## Installation
To install the libary first install git
```bash
sudo apt-get install git
```
Clone the repository
```bash
git clone https://github.com/danny270793/HttpClient.git
```
Enter to the folder and install it on python 2
```bash
cd HttpClient
pip install .
```
Or with python 3
```bash
cd HttpClient
pip3 install .
```
## Usage
Create a http client for an endpoind
```python
from httpclient import HttpClient

httpClient=HttpClient('http://danny.telinksa.com/api')
```
Make a GET request with an argument id with value 25
```python
from httpclient import HttpClient

httpClient=HttpClient('http://danny.telinksa.com/api')

payload={'id':25}
response=httpClient.get(payload)
print(response)
```
Make a POST request with an argument id with value 25
```python
from httpclient import HttpClient

httpClient=HttpClient('http://danny.telinksa.com/api')

payload={'id':25}
response=httpClient.post(payload)
print(response)
```

## Follow me
* [Facebook](https://www.facebook.com/danny.vaca.9655)
* [Instagram](https://www.instagram.com/danny27071993/)
* [Youtube](https://www.youtube.com/channel/UC5MAQWU2s2VESTXaUo-ysgg)
* [Github](https://www.github.com/danny270793/)
* [LinkedIn](https://www.linkedin.com/in/danny270793)

## License
Copyright (c) Danny Vaca. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.
import requests

proxies = {
  'http': 'http://USERNAME:PASSWORD@unblock.smartproxy.com:60000',
  'https': 'http://USERNAME:PASSWORD@unblock.smartproxy.com:60000'
}

response = requests.request(
    'GET',
    'https://ip.smartproxy.com/',
    verify=False,
    proxies=proxies
)

print(response.text)

with open('result.html', 'w') as f:
    f.write(response.text)
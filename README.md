# Site Unblocker

## List of contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Making Requests](#making-requests)
- [Parameters](#parameters)
  
## Introduction

Site Unblocker is a powerful scraping solution with automatic proxy pool management and automated unblocking capabilities that enable you to access any website with even the most sophisticated anti-bot system.

It bypasses CAPTCHAs, geo-blocking, IP blocking, and other challenges to fetch raw HTML with JavaScript data.

Site Unblocker is ideal for saving costs on development and infrastructure maintenance.

## Authentication

Once you have an active Site Unblocker subscription, you can try sending a request right from the dashboard Site Unblocker > Proxy Setup tab simply by entering the desired website URL and clicking on Send Request. You will also see an example of curl request and live view rendering of the HTML website right below. 

You may also click on the Advanced Parameters tab to access all available parameters for your request, such as custom cookies, custom headers and a JavaScript rendering toggle.

## Making Requests

**``` -k ``` or the equivalent ```--insecure```  is required for Site Unblocker to work**

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" 
```


## Parameters

Additional parameters are sent as headers when making a request.

### Session


To utilize a single proxy for multiple requests, simply include the ```X-SU-Session-Id``` header with a randomly generated string as the session ID. This ID will be associated with a unique proxy, which will be used for all subsequent requests within a 10-minute timeframe. Once the 10 minutes have elapsed, a new proxy will be assigned to that specific session ID.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Session-Id: random123"
```

### Geo-location

You may specify your geolocation when making request to a particular website. The accepted geolocation values can be country, state, city or coordinates, and radius. 

**Country**

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Geo: Germany"
```

**City**

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Geo: Berlin, Germany"
```

**State**

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Geo: Arizona, United States"
```

**Coordinates & Radius**

The following example uses coordinates for The Bronx, New York City, USA.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Geo: lat: 40.8448, lng: -73.8654, rad: 20000"
```
### Headers

You may send additional headers with your request, they could be standard like ```User-Agent``` or custom ones depending on your specific target. Use ```X-SU-Custom-*``` to send a custom header, it can be named as desired e.g - ```X-SU-Custom-My-Header```

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Custom-My-Header: Custom header content here" \
-H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36" 
```

### Cookies

There is an option to send custom cookies with your request as well.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "Cookie: WOW=4206969; NICE=8008135"
```

### Custom Status Codes

A request is considered to be successful if it returns a status code in the 2xx or 4xx range. However, there are cases where websites may provide the necessary content along with a non-standard HTTPS status code. If any of your targets exhibit this behavior, you have the option to specify which status codes are acceptable and relevant to your needs.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Status-Code: 503, 501"
```

### POST Requests

In addition to facilitating GET requests, Site Unblocker also enables you to utilize POST requests to a web endpoint of your preference. This functionality allows you to send data to a specific website, resulting in a modified response from the target.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-X POST \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-d "Your content here"
```

### JavaScript Rendering


If the page you intend to scrape necessitates the execution of JavaScript in order to dynamically load all the necessary data you may enable JavaScript rendering without the need of using a headless browser.

**Receive rendered page content in HTML**

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Headless: html"
```

**Receive rendered page content as PNG**

The response will contain raw bytes of an image that can be saved in PNG format.

```
curl -k -v -x unblock.smartproxy.com:60000 \
-U "USERNAME:PASSWORD" "https://ip.smartproxy.com/" \
-H "X-SU-Headless: png"
```


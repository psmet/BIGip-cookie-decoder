# F5 Big-IP cookie decoder 

This python script will take a Big-IP persistence cookie and decode the value. This will allow you to determine the internal IP address(es) of a load balanced webserver. Typically, Big-IP cookies are composed by the **BIGipServer** prefix, the pool name and contain an encoded string (internal IP address and port of the load-balanced web server).

THis is an example of a Big-IP Cookie from the internet:

```
BIGipServer<pool_name>=1677787402.36895.0000
```

You can then run this through this tool  using from the command line:

```
BIGIP_decode_cookie.py BIGipServer<pool_name>=1677787402.36895.0000 
```

This would return you the following:

```
# python BIGIP_decode_cookie.py 
[*] Cookie to decode: BIGipServer<pool_name>=1677787402.36895.0000

[*] Pool name: <pool_name>
[*] Decoded IP and Port: 10.1.1.100:8080
```

Thanks to https://penturalabs.wordpress.com/2011/03/29/how-to-decode-big-ip-f5-persistence-cookie-values/ 

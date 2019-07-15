from whois import whois

#display info about a web page (eg: google.com)
data = input("Enter a domain: ")
webInfo = whois(data)

print(webInfo)
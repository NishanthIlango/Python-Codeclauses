import pyshorteners as ps   #This library is used to shorten the URL
url=input("Enter the URL:")
def short_url(url):
    u=ps.Shortener().tinyurl.short(url)
    print("The shorten URL is:",u)

short_url(url)
import urllib.request


with open('sites.txt', 'r') as f:
    urls = f.readlines()

#print(urls)
for url in urls:
    url = url.replace('\n', '')

    try:
        status_code = urllib.request.urlopen(url).getcode()
        website_is_up = status_code == 200
    except:
        website_is_up = False
    if website_is_up:
        print(url, " : ", website_is_up)

# status_code = urllib.request.urlopen(url).getcode()
# website_is_up = status_code == 200

# print(website_is_up)

# #Output
# True
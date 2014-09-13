import urllib2

# See assignment1.html instructions or README for how to get these credentials
yummly_app_id = "bcf5183a"
yummly_app_key = "f358a71979619f8ac9b56cea2f15e0e7"

_debug = 0

'''
Make a Yummly request
using the hard-coded credentials above.
'''
def fetchrecipes():
  url = "http://api.yummly.com/v1/api/recipes?_app_id=" + yummly_app_id + "&_app_key=" + yummly_app_key + "&q=onion+soup"
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchrecipes()

import urllib2
import sys

# See assignment1.html instructions or README for how to get these credentials
yummly_app_id = "bcf5183a"
yummly_app_key = "f358a71979619f8ac9b56cea2f15e0e7"

_debug = 0

'''
Make a Yummly request
using the hard-coded credentials above.
'''
def fetchrecipes(time_request):
  url = "http://api.yummly.com/v1/api/recipes?_app_id=" + yummly_app_id + "&_app_key=" + yummly_app_key + "&q=onion+soup" + time_request
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  for line in response:
    print line.strip()

def getTotalTime(max_time_in_minutes):
  max_time_in_seconds = max_time_in_minutes * 60
  print "Max time in seconds= " + str(max_time_in_seconds)
  return "&maxTotalTimeInSeconds=" + str(max_time_in_seconds)

def main():
  time = getTotalTime(int(sys.argv[1]))
  fetchrecipes(time)

if __name__ == '__main__':
  main()

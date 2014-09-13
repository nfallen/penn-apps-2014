import urllib2
import sys

# app id and app key
yummly_app_id = "bcf5183a"
yummly_app_key = "f358a71979619f8ac9b56cea2f15e0e7"

_debug = 0

'''
Make a Yummly request
using the hard-coded credentials above.
'''
def get_specific_recipe(recipe_id):
  url = "http://api.yummly.com/v1/api/recipe/" + recipe_id + "?_app_id=" + yummly_app_id + "&_app_key=" + yummly_app_key
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  for line in response:
    print line.strip()
                 
def main():
    recipe_id = str(sys.argv[1])
    print("recipe_id")
    get_specific_recipe(recipe_id)

if __name__ == '__main__':
    main()
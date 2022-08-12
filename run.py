import requests
from argparse import ArgumentParser

"""
Check whether an origin is already archived on Software Heritage

Parameter:
origin_url - url to public repository

Returns:
Link to archive - if origin is already archived, 
None - if origin is not archived
"""
def check_if_exists(origin_url):
    x = requests.get("https://archive.softwareheritage.org/api/1/origin/" + origin_url + "/get/")
    if x.status_code == 404:
        return None
    else:
        return "https://archive.softwareheritage.org/browse/origin/directory/?origin_url=" + origin_url

"""
Check whether an origin is already archived on Software Heritage

Parameter:
origin_url - url to public repository
visit_type - where repository lies; can be: git, svn, bzr, hg
"""
def archive_origin(origin_url, visit_type):
    x = requests.post("https://archive.softwareheritage.org/api/1/origin/save/" + visit_type + "/url/" + origin_url + "/")
    print(x.content)

# Use argument parser to get input for calling the functions
parser = ArgumentParser()
parser.add_argument("-o", "--origin", nargs='?', default='', dest='origin_url', required=True,
                    action='store',
                    help="Check if Origin exists in Software Heritage Archive")
parser.add_argument("-a", "--archive", nargs='?', default='git', dest='visit_type',
                    choices=['git', 'svn', 'bzr', 'hg'], action='store',
                    help="If Origin does not exist in Software Heritage Archive, make Save-Request to API. Argument has to be one of the following: git, svn, bzr, hg")                  
args = parser.parse_args()

# If origin_url was set using -o
if args.origin_url != None:
    result = check_if_exists(args.origin_url)
    print(result)
    # If origin is not archieved yet and visit_type was set, make save-request to Software Heritage
    if result == None and args.visit_type != None:
        archive_origin(args.origin_url, args.visit_type)
else:
    print('origin_url is None')
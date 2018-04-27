# >>> CraigslistHousing.show_filters(category='apa')
# Base filters:
# * bundle_duplicates = True/False
# * search_titles = True/False
# * posted_today = True/False
# * has_image = True/False
# * query = ...
# * search_distance = ...
# * zip_code = ...
# Section specific filters:
# * min_bedrooms = ...
# * min_bathrooms = ...
# * max_bedrooms = ...
# * private_room = True/False
# * wheelchair_acccess = True/False
# * no_smoking = True/False
# * is_furnished = True/False
# * max_ft2 = ...
# * max_bathrooms = ...
# * min_ft2 = ...
# * cats_ok = True/False
# * min_price = ...
# * dogs_ok = True/False
# * private_bath = True/False
# * max_price = ...
# * laundry = u'w/d in unit', u'w/d hookups', u'laundry in bldg', u'laundry on site', u'no laundry on site'
# * housing_type = u'apartment', u'condo', u'cottage/cabin', u'duplex', u'flat', u'house', u'in-law', u'loft', u'townhouse', u'manufactured', u'assisted living', u'land'
# * parking = u'carport', u'attached garage', u'detached garage', u'off-street parking', u'street parking', u'valet parking', u'no parking'

from craigslist import CraigslistHousing
from slackclient import SlackClient

SLACK_TOKEN = "ENTER_TOKEN_HERE"
SLACK_CHANNEL = "#housing"

#define areas that we want to live in
AREAS = {
    "russian-hill": [
        [-122.424929,37.795946],
        [-122.414543,37.805179]
    ],
    "pac-heights": [
        [-122.440493,37.787825],
        [-122.422799,37.804067]
    ],
    "hayes-duboce-mission": [
        [-122.4391754823,37.7571045379],
        [-122.4167884802,37.7800723458]
    ],
    "the-emma-zone": [
        [-122.472109,37.756633],
        [-122.427535,37.778873]
    ]
}

NEIGHBORHOODS = ["russian hill",
                 "pac heights",
                 "pacific heights",
                 "nob hill",
                 "hayes valley",
                 "duboce triangle",
                 "mission",
                 "nopa".
                 "inner sunset",
                 "cole valley",
                 "noe valley"]

#define geolocating function
def in_area(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

#get results from craiglist
cl_h = CraigslistHousing(site='sfbay', area='sfc', category='apa',
                         filters={'posted_today': True,
                                  'min_bedrooms': 1,
                                  'max_bedrooms': 3,
                                  'cats_ok': True,
                                  'max_price': 4100,
                                  'laundry': ['w/d hookups', 'w/d in unit', 'laundry in bldg'],
                                  'housing_type': ['apartment', 'condo', 'flat', 'house'],
                                  'parking': ['carport', 'attached garage', 'detached garage', 'off-street parking']})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    geotag = result["geotag"]
    location = result["where"]
    area_found = False
    area = ""
    for a, coords in AREAS.items():
        if in_area(geotag, coords):
            area = a
            area_found = True
    for hood in NEIGHBORHOODS:
        if hood in location.lower():
            area = hood

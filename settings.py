import os

##Twilio variables
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
MS_SID = os.environ["MS_SID"]
TARGET_PHONE_NUMBER = os.environ["PHONE_NUMBER"]

##Craigslist variables
CL_SITE = 'sfbay'
CL_AREA = 'sfc'
CL_CATEGORY = 'apa'
MAX_NUM_BEDROOMS = 1
MIN_NUM_BEDROOMS = 1
POSTED_TODAY = True
MAX_PRICE = 2300
MIN_PRICE = 1700
LAUNDRY_OPTIONS = ['w/d hookups', 'w/d in unit', 'laundry in bldg','laundry on site']
#PARKING_OPTIONS = ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking']
HOUSING_TYPE = ['apartment', 'condo', 'flat', 'house', 'loft']

##Housing variables
#define areas that we want to live in
AREAS = {
    "russian-hill": [
        [-122.424929,37.795946],
        [-122.410338,37.805179]
    ],
    "nob-hill":
    [
        [-122.421748, 37.788999],
        [-122.408916, 37.799477]
    ],
    "cow-hollow":
    [
        [-122.442464, 37.793427],
        [-122.426413, 37.800617]
    ]
}
#fall back neighborhoods to try and to find in the listing string
NEIGHBORHOODS = ["russian hill",
                 "nob hill",
                 "cow hollow"]

SLEEP_TIMER = 20 * 60

import os

##Slack variables
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")
if SLACK_TOKEN == "":
    print("No slack token configured, please add an EXPORT SLACK_TOKEN = to your bash_profile")
    exit()
SLACK_CHANNEL = "#housing"
SLACK_BOT_NAME = 'housingBot'

##Craigslist variables
CL_SITE = 'sfbay'
CL_AREA = 'sfc'
CL_CATEGORY = 'apa'
MAX_NUM_BEDROOMS = 3
MIN_NUM_BEDROOMS = 1
POSTED_TODAY = True
CATS_OK = True
MAX_PRICE = 4100
MIN_PRICE = 1000
LAUNDRY_OPTIONS = ['w/d hookups', 'w/d in unit', 'laundry in bldg']
PARKING_OPTIONS = ['carport', 'attached garage', 'detached garage', 'off-street parking']
HOUSING_TYPE = ['apartment', 'condo', 'flat', 'house']


##Housing variables
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
    "lower-pac-heights": [
        [-122.443505,37.78306],
        [-122.423056,37.791819]
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
#fall back neighborhoods to try and to find in the listing string
NEIGHBORHOODS = ["russian hill",
                 "pac heights",
                 "pacific heights",
                 "nob hill",
                 "hayes valley",
                 "duboce triangle",
                 "mission",
                 "nopa",
                 "inner sunset",
                 "cole valley",
                 "noe valley"]

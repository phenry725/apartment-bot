import os

##Slack variables
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")
if SLACK_TOKEN == "":
    print("No slack token configured, please add an EXPORT SLACK_TOKEN = to your bash_profile")
    exit()
SLACK_CHANNEL = "#housing"
SLACK_BOT_NAME = "housingBot"

##Craigslist variables
CL_SITE = 'sfbay'
CL_AREA = 'sfc'
CL_CATEGORY = 'apa'
MAX_NUM_BEDROOMS = 3
MIN_NUM_BEDROOMS = 1
POSTED_TODAY = True
MAX_PRICE = 4100
MIN_PRICE = 1000
LAUNDRY_OPTIONS = ['w/d hookups', 'w/d in unit', 'laundry in bldg','laundry on site']
PARKING_OPTIONS = ['carport', 'attached garage', 'detached garage', 'off-street parking', 'street parking']
HOUSING_TYPE = ['apartment', 'condo', 'flat', 'house', 'loft']


##Housing variables
#define areas that we want to live in
AREAS = {
    "area1": [
        [-122.459845,37.761251],
        [-122.424502,37.783121]
    ],
    "area2": [
        [-122.280165,37.795538],
        [-122.251299,37.823769]
    ]


    # "north-city": [
    #     [-122.424637,37.788507],
    #     [-122.399478,37.804217]
    # ],
    # "dem-heights": [
    #     [-122.44721,37.786682],
    #     [-122.422328,37.800982]
    # ],
    # "jtown-lph-wa-hayesvalley": [
    #     [-122.444552,37.770813],
    #     [-122.419307,37.788262]
    # ],
    # "panhandle": [
    #     [-122.453367,37.760502],
    #     [-122.428843,37.774267]
    # ],
    # "lower-city potrero hill": [
    #     [-122.412103,37.749715],
    #     [-122.388665,37.767276]
    # ],
    # "presidio": [
    #     [-122.480929,37.772603],
    #     [-122.445637,37.803769]
    # ]

}

# {
#     "russian-hill": [
#         [-122.424929,37.795946],
#         [-122.414543,37.805179]
#     ],
#     "pac-heights": [
#         [-122.440493,37.787825],
#         [-122.422799,37.804067]
#     ],
#     "lower-pac-heights": [
#         [-122.443505,37.78306],
#         [-122.423056,37.791819]
#     ],
#     "hayes-duboce-mission": [
#         [-122.4391754823,37.7571045379],
#         [-122.4167884802,37.7800723458]
#     ],
#     "the-emma-zone": [
#         [-122.472109,37.756633],
#         [-122.427535,37.778873]
#     ]
# }
#fall back neighborhoods to try and to find in the listing string
NEIGHBORHOODS = ["russian hill",
                 "soma",
                 "pac heights",
                 "pacific heights",
                 "lower pac hts",
                 "nob hill",
                 "hayes valley",
                 "duboce triangle",
                 "mission",
                 "nopa",
                 "panhandle",
                 "lower haight",
                 "marina",
                 "cow hollow",
                 "potrero hill",
                 "alamo square",
                 "inner sunset",
                 "cole valley",
                 "noe valley",
                 "west portal",
                 "forest hill"
                 ]

SLEEP_TIMER = 20 * 60

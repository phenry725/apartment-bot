from apartmentBot import scrape_for_apartments
import time
import settings
import traceback
import sys


while True:
    print("{}: Starting interval run.".format(time.ctime()))
    try:
        scrape_for_apartments()
    except KeyboardInterrupt:
        print("Exiting....")
        sys.exit(1)
    except Exception as exc:
        print("Error with the scraping:", sys.exc_info()[0])
        traceback.print_exc()
    else:
        print("{}: Done running. Sleeping.".format(time.ctime()))
        time.sleep(settings.SLEEP_TIMER)

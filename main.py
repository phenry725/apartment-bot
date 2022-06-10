from apartmentBot import scrape_for_apartments
import time
import settings
import traceback
import sys

counter = 0
while counter < 13:
    print("{}: Starting interval run.".format(time.ctime()))
    sys.stdout.flush()
    try:
        scrape_for_apartments()
        counter += 1
    except KeyboardInterrupt:
        print("Exiting....")
        sys.stdout.flush()
        sys.exit(1)
    except Exception as exc:
        print("Error with the scraping:", sys.exc_info()[0])
        sys.stdout.flush()
        traceback.print_exc()
    else:
        print("{}: Done running. Sleeping.".format(time.ctime()))
        sys.stdout.flush()
        time.sleep(settings.SLEEP_TIMER)

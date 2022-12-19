# Display per minute "Inside fun" Task in console.

import schedule
import time
def Fun():
    print("Inside fun")

def main():
    print("Inside task schedular")

    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()


# import schedule
# install command for Terminal - " pip install schedule "
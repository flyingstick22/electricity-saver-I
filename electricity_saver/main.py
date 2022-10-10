import schedule
import time
from day_ahead_prices import application

def main():
    
    print("\nProgramm running...(exit ctrl+C)\n")
    application()   # runs app function once at startup. Afterwards once per hour  
    
    schedule.every().hour.at(":00").do(application)   
      
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()






## Control your home electrical loads based on Day-ahead electricity prices
The aim of this small Python project is to enable load control based on hourly electricity prices and help people to cope with ongoing energy crisis in Europe.

### Intro

All day-ahead prices are requested from [ENTSO-E transparency platform](https://transparency.entsoe.eu/) and requires an API key. The API key is free and can be requested directly from ENTSO-E. Look from [here](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/) for more information.

The control device in this project is Shelly pro 4PM relay. It has four 230 V outputs and each output is activated or deactivated based on hourly electricity price.

The system default values are as follows:

Relay 1 is ON based on six lowest hourly day prices (= 6 hours ON / day)
Relay 2 goes OFF when electricity price is higher than 0.08 €/kWh (Excl. VAT)
Relay 3 goes OFF when electricity price is higher than 0.16 €/kWh (Excl. VAT)
Relay 4 goes OFF when electriciy price is higher than 0.32 €/kWh (Excl. VAT)

You can change these values in *shelly_controls.py* for your liking. 

### The beginning

Shelly relay needs to be installed first. In most countries 230 V installations belong to professionals so follow your country rules here. As soon as Shelly is up and running you have to connect that with your home network. Shelly pro 4PM relay supports ethernet or WiFi connections. What's also needed is a computer (python installed) that can run the scripts. It can be for example Rasperry PI or normal computer in the same home network with the Shelly relay.

### Code modifications

Some housekeeping needed before this thing works. First. You have to add a file called **.env** to the root. In this file you'll write your API-key as follows and save it.

''' ENTSO_API_KEY="add_your_own_entsoe_api_key_here" '''

In file called *shelly_controls.py*: change IP to match your shelly relay IP-address. You'll find IP e.g. from Shelly relay under "Status" screen.

'''  shelly_ip = "192.168.20.67"  ''' 

In file called *day_ahead_prices.py* change your country code and time zone. Right country codes can be found from [here](https://www.entsoe.eu/data/energy-identification-codes-eic/). In our example we are using Finland.

''' def get_prices():

    country = "FI"              #country code
    tz = "Europe/Helsinki"      #time zone '''

Save modified files and that's it.

### Running the code
....

### Next steps
....

















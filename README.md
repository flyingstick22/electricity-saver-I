# Control your home electrical loads based on Day-ahead electricity prices
The aim of this small Python project is to enable load control based on hourly electricity prices and help people to cope with ongoing energy crisis in Europe. Example country is Finland.

## Intro

The system uses simple python scripts to control Shelly relay. The relay for this project is [Shelly pro 4PM](https://shelly.cloud/knowledge-base/devices/shelly-pro-4pm/). It has four 230 V outputs and each output is activated or deactivated based on hourly electricity price. Shelly relays are widely available in Europe and have open API and good documentation for personal projects like this.

The system default values are as follows (you can change all these values in *shelly_controls.py* for your liking):

* Output 1 is ON based on **six** lowest hourly day prices (= 6 hours ON / day)<br>
* Output 2 goes OFF when electricity price (in that particular hour) is higher than 0.08 €/kWh (Excl. VAT)<br>
* Output 3 goes OFF when electricity price (in that particular hour) is higher than 0.16 €/kWh (Excl. VAT)<br>
* Output 4 goes OFF when electriciy price (in that particular hour) is higher than 0.32 €/kWh (Excl. VAT)<br>

Output one can be used for loads which needs to be xx hours per day ON but their timing is less critical. Such a loads could be, for example, electrical floor heating or water boiler. If six hours is not enough, you can easily increase the time. The benefit is, that output one is only using low priced hours and this way optimizes your electricity bill.


All day-ahead prices are requested from [ENTSO-E transparency platform](https://transparency.entsoe.eu/) and requires an API key. The API key is free and can be requested directly from ENTSO-E. Check [this](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/) for more information. All prices in the code are €/MWh and without taxes, dealer margins or transmission costs. You can change triggering limits based on your detailed information about your own electric tariffs. 

## The beginning

* Shelly relay needs to be installed first. In most countries 230 V installation belongs to professional so follow your country rules here. As soon as Shelly is up and running connect the relay to your home router with Ethernet cable or using WiFi. You'll also need a computer (python installed) that can run the scripts. It can be, for example, Rasperry PI or normal laptop. Important is that it is connected in same home network as Shelly relay.

## Code modifications

* Some modifications are needed before this thing works. First. Copy the folder called **electricity_saver**  and save it to your computer. You have to create a file name **.env** to the root. In this file you'll write your own API-key between " " marks as follows.

    ```` ENTSO_API_KEY="add_your_own_entsoe_api_key_here" ```` 

    You can request your own API key as mentioned [above](https://thesmartinsights.com/how-to-query-data-from-the-entso-e-transparency-platform-using-python/)

* In the file called *shelly_controls.py* --> change IP of your shelly relay. You'll find IP e.g. from Shelly relay under "Status" screen or from your router settings (check from the screen STA or ETH IP's (not AP) if your Shelly is connected to your home network.

    ````  shelly_ip = "192.168.20.67"  ````

* In file called *day_ahead_prices.py* change your country code and time zone if needed. Right country codes can be found from [here](https://www.entsoe.eu/data/energy-identification-codes-eic/). In our example code we are using Finland.

        country = "FI"              #country code
        tz = "Europe/Helsinki"      #time zone

    Save modified files and that's it.

## Running the code

* open the terminal/command prompt (Mac/Windows) and navigate to project folder (cd your_path/electricity_saver). As soon as your are in the right folder execute the main.py script by writing

        python main.py

Programm starts running and you should see something like this:

*add picture*

* In the first line you'll see daily minimum and maximum prices and current hourly price. Script updates price once per hour and control relay outputs. You'll see relay status



## Possible issues
....

















# IP-Info-Swiper ℹ️🔍
Python script that uses the ipwho.is and google maps API's to pull information about a given IP address and return it to the user

![Alt text](images/Screenshot_20260809_192758_Termux.jpg)

Prerequisites:

1. Ensure the latest version of python in installed in your terminal (python 3.x)
2. Ensure you have a virtual env for the required python libraries (If you don't, one can easily be created by executing the command "python3 -m venv env")

Recommendations:
* Use a VPN while using this tool (Proton or Mullvad are encouraged)
* Enable TOR in your terminal
* Run proxychains4 while executing the software (This comes pre-installed with Kali-Linux)

Installation & Execution:

* To install, simply type "git clone https://github.com/RavenTheBird789/IP-Info-Swiper" in your terminals command line

1. Run the command "source env/bin/activate" to activate your virtual env
2. Run the command "cd IP-Info-Swiper" to change into the directory of this project
3. Run the command "pip install -r requirements.txt" once in the directory to install the required third-party python libraries

* To run, simply type "python3 ip_info.py" in your terminals command line or use the alias command to create a shortcut to run the program in your terminal such as "alias ip="python3 ip_info.py""

Additional Information:

* The geolocation of the given IP address returned to the user (displayed via latitude and longitude) may not be 100% accurate

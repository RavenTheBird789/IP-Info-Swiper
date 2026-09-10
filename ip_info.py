#!/usr/bin/env python3
# IP Info Swiper
import requests
import json
import time
import os

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

# Global variables
equalSign = "="
emptySpace = " "
Wh = '\033[1;37m' # White color
Gr = '\033[1;32m' # Green color

def trademark(ip_info_func):
    def wrapper(*args, **kwargs):
        print(green(equalSign * 20))
        print(green(bold((emptySpace * 3) + "IP Info Swiper")))
        print(green(equalSign * 20))
        print(red("By: RavenTheBird789"))
        print(green(equalSign * 20))
        return ip_info_func(*args, **kwargs)
    return wrapper

def exit_animation():
    """Handles the graceful exit animation cleanly."""
    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(green(f"Exiting{'.' * i}"))
        time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    os._exit(0)

def get_ip_info(ip_address):
    """Fetch information about the given IP address using an external API."""
    try:
        req_api = requests.get(f"http://ipwho.is/{ip_address}", timeout=10)
    except requests.exceptions.RequestException:
        print(red("\n[!] Network error. Unable to connect to API."))
        time.sleep(3)
        return

    if req_api.status_code == 200:
        ip_data = json.loads(req_api.text)
        
        # Check if the API itself flagged the IP lookup as a failure
        if not ip_data.get("success", False):
            print(red(f"\n[!] API Error: {ip_data.get('message', 'Unknown error')}"))
            time.sleep(3)
            return

        time.sleep(2)
        print(f"{Wh}\n IP target       :{Gr}", ip_address)
        print(f"{Wh} Type IP         :{Gr}", ip_data.get("type", "N/A"))
        print(f"{Wh} Country         :{Gr}", ip_data.get("country", "N/A"))
        print(f"{Wh} Country Code    :{Gr}", ip_data.get("country_code", "N/A"))
        print(f"{Wh} City            :{Gr}", ip_data.get("city", "N/A"))
        print(f"{Wh} Continent       :{Gr}", ip_data.get("continent", "N/A"))
        print(f"{Wh} Continent Code  :{Gr}", ip_data.get("continent_code", "N/A"))
        print(f"{Wh} Region          :{Gr}", ip_data.get("region", "N/A"))
        print(f"{Wh} Region Code     :{Gr}", ip_data.get("region_code", "N/A"))
        print(f"{Wh} Latitude        :{Gr}", ip_data.get("latitude", "N/A"))
        print(f"{Wh} Longitude       :{Gr}", ip_data.get("longitude", "N/A"))
        
        # Keep lat/lon decimals intact for accurate mapping
        lat = ip_data.get('latitude', 0)
        lon = ip_data.get('longitude', 0)
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        
        print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu", "N/A"))
        print(f"{Wh} Postal          :{Gr}", ip_data.get("postal", "N/A"))
        print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code", "N/A"))
        print(f"{Wh} Capital         :{Gr}", ip_data.get("capital", "N/A"))
        print(f"{Wh} Borders         :{Gr}", ip_data.get("borders", "N/A"))
        
        # Safe extraction for nested dictionaries
        flag_data = ip_data.get("flag", {})
        print(f"{Wh} Country Flag    :{Gr}", flag_data.get("emoji", "N/A"))
        
        conn_data = ip_data.get("connection", {})
        print(f"{Wh} ASN             :{Gr}", conn_data.get("asn", "N/A"))
        print(f"{Wh} ORG             :{Gr}", conn_data.get("org", "N/A"))
        print(f"{Wh} ISP             :{Gr}", conn_data.get("isp", "N/A"))
        print(f"{Wh} Domain          :{Gr}", conn_data.get("domain", "N/A"))
        
        tz_data = ip_data.get("timezone", {})
        print(f"{Wh} ID              :{Gr}", tz_data.get("id", "N/A"))
        print(f"{Wh} ABBR            :{Gr}", tz_data.get("abbr", "N/A"))
        print(f"{Wh} DST             :{Gr}", tz_data.get("is_dst", "N/A"))
        print(f"{Wh} Offset          :{Gr}", tz_data.get("offset", "N/A"))
        print(f"{Wh} UTC             :{Gr}", tz_data.get("utc", "N/A"))
        time.sleep(2)
    else:
        print(red("\n[!] Server error: Unable to fetch IP information."))
        time.sleep(3)

@trademark
def main():
    while True:
        ip_address = input(green("Enter an IP address: ")).strip()
        get_ip_info(ip_address)
        
        # Loop prompt to avoid infinite recursion crashes
        while True:
            prompt = input(green("\nWould you like to use the tool again? (yes/no): ")).strip().lower()
            if prompt == "yes":
                os.system('cls' if os.name == 'nt' else 'clear')
                main()
            elif prompt == "no":
                exit_animation()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(red("Invalid Input"))
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

# Run the program
if __name__ == "__main__":
    main()

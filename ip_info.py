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
        ip_type = ip_data.get("type", "N/A")
        country = ip_data.get("country", "N/A")
        country_code = ip_data.get("country_code", "N/A")
        city = ip_data.get("city", "N/A")
        continent = ip_data.get("continent", "N/A")
        continent_code = ip_data.get("continent_code", "N/A")
        region = ip_data.get("region", "N/A")
        region_code = ip_data.get("region_code", "N/A")

        print(f"{Wh}\n IP target       :{Gr}", ip_address)
        print(f"{Wh} IP Type         :{Gr}", ip_type)
        print(f"{Wh} Country         :{Gr}", country)
        print(f"{Wh} Country Code    :{Gr}", country_code)
        print(f"{Wh} City            :{Gr}", city)
        print(f"{Wh} Continent       :{Gr}", continent)
        print(f"{Wh} Continent Code  :{Gr}", continent_code)
        print(f"{Wh} Region          :{Gr}", region)
        print(f"{Wh} Region Code     :{Gr}", region_code)
        print(f"{Wh} Latitude        :{Gr}", ip_data.get("latitude", "N/A"))
        print(f"{Wh} Longitude       :{Gr}", ip_data.get("longitude", "N/A"))
        
        # Keep lat/lon decimals intact for accurate mapping
        lat = ip_data.get('latitude', 0)
        lon = ip_data.get('longitude', 0)
        google_maps_url = f"https://www.google.com/maps/@{lat},{lon},8z"
        print(f"{Wh} Maps            :{Gr}", google_maps_url)

        EU = ip_data.get("is_eu", "N/A")
        Postal = ip_data.get("postal", "N/A")
        call_code = ip_data.get("calling_code", "N/A")
        capital = ip_data.get("capital", "N/A")
        borders = ip_data.get("borders", "N/A")

        print(f"{Wh} EU              :{Gr}", EU)
        print(f"{Wh} Postal          :{Gr}", Postal)
        print(f"{Wh} Calling Code    :{Gr}", call_code)
        print(f"{Wh} Capital         :{Gr}", capital)
        print(f"{Wh} Borders         :{Gr}", borders)
        
        # Safe extraction for nested dictionaries
        flag_data = ip_data.get("flag", {})
        flag = flag_data.get("emoji", "N/A")
        print(f"{Wh} Country Flag    :{Gr}", flag)
        
        conn_data = ip_data.get("connection", {})
        ASN = conn_data.get("asn", "N/A")
        ORG = conn_data.get("org", "N/A")
        ISP = conn_data.get("isp", "N/A")
        domain = conn_data.get("domain", "N/A")

        print(f"{Wh} ASN             :{Gr}", ASN)
        print(f"{Wh} ORG             :{Gr}", ORG)
        print(f"{Wh} ISP             :{Gr}", ISP)
        print(f"{Wh} Domain          :{Gr}", domain)
        
        tz_data = ip_data.get("timezone", {})
        ID = tz_data.get("id", "N/A")
        ABBR = tz_data.get("abbr", "N/A")
        DST = tz_data.get("is_dst", "N/A")
        offset = tz_data.get("offset", "N/A")
        UTC = tz_data.get("utc", "N/A")

        print(f"{Wh} ID              :{Gr}", ID)
        print(f"{Wh} ABBR            :{Gr}", ABBR)
        print(f"{Wh} DST             :{Gr}", DST)
        print(f"{Wh} Offset          :{Gr}", offset)
        print(f"{Wh} UTC             :{Gr}", UTC)

        time.sleep(2)
        file_num = 1
        while os.path.exists(f"ip_addr_info{file_num}.txt"):
            file_num += 1
        filename = f"ip_addr_info{file_num}.txt"
        with open(filename, "w", encoding="utf-8") as ip:
            print(f"The following information was ressolved from {ip_address}\nIP Type: {ip_type}\nCountry: {country}\nCountry Code: {country_code}\nCity: {city}\nContinent: {continent}\nContinent Code: {continent_code}\nRegion: {region}\nRegion Code: {region_code}\nLatitude: {lat}\nLongitude: {lon}\nMaps: {google_maps_url}\nEU: {EU}\nPostal: {Postal}\nCalling Code: {call_code}\nCapital: {capital}\nBorders: {borders}\nFlag: {flag_data}{flag}\nASN: {ASN}\nORG: {ORG}\nISP: {ISP}\nDomain: {domain}\nID: {ID}\nDST: {DST}\nOffset: {offset}\nUTC: {UTC}", file=ip)

        print(f"This information has been saved as {filename}")
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

if __name__ == "__main__":
    main()

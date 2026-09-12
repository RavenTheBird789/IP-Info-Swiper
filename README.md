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

* To run, simply type "python3 ip_info.py" in your terminals command line or use the alias command to create a shortcut to run the program in your terminal such as "alias ipinfo="python3 ip_info.py""

Global Execution (Optional)
* Alternatively, you can run the program globally by simply typing "ipinfo" from anywhere in your terminal, follow these steps (For macOS and Linux):
  1. Make the file executable by typing "chmod +x ip_info.py" in your terminal
  2. Copy the file to a new name using "cp ip_info.py ipinfo" then make that executable too with "chmod +x ipinfo"
  3. Create a local bin folder if you don't already have one using "mkdir -p ~/.local/bin"
  4. Move the file into it using "mv ipinfo ~/.local/bin/"
  5. Make sure that folder is in your PATH by adding "export PATH="HOME/.local/bin:PATH"" to your ~/.bashrc (or ~/.zshrc if you use zsh)
  6. Reload your terminal config using "source ~/.bashrc" (or ~/.zshrc)
  7. Type "ipinfo" from anywhere to run the program

* For Windows
  1. Make sure Python is added to your PATH (check by typing "python --version" in Command Prompt. If it shows a version number, you're set)
  2. Create a folder to hold your global scripts, such as "C:\Scripts" (You can make this anywhere, just don't forget the path)
  3. Copy "ip_info.py" into that folder and rename the copy "ipinfo.py"
  4. In the same folder, create a new text file named "ipinfo.bat"
  5. Open "ipinfo.bat" in Notepad and add this single line "@python "%~dp0ipinfo.py" %*"
  6. Save and close the file
  7. Add your folder to your PATH: press the Windows key, search "Environment Variables", click "Edit the system environment variables", click "Environment Variables", under "User variables" select "Path", click "Edit", click "New", then paste in your folder path (e.g. "C:\Scripts")
  8. Click OK on all the windows to save
  9. Close and reopen Command Prompt or Powershell
  10. Type "ipinfo" from anywhere to run the program

Additional Information:

* The geolocation of the given IP address returned to the user (displayed via latitude and longitude) may not be 100% accurate
* If the users input when prompted for an IP address is an empty string, then the ipwho.is API will return the corresponding data for the IP address of the user's device
* If you exceed the rate limit, further requests will return HTTP 429 (Too Many Requests). Access will be restored automatically after 24 hours (Read additional documentation for the ipwho.is API at https://ipwhois.io/documentation for further details)

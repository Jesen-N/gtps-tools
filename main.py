# Made by Jesen N#9071
import pkg_resources, sys, subprocess

required = {'pysimplegui', 'wget'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    print("installing module...")
    
import PySimpleGUI as sg
import wget, webbrowser

def hostmaker():
    ip = values["ip"]
    namehost = sg.popup_get_text("Your host name (Ex: gtps.txt):")
    if namehost is None:
        sg.popup_no_titlebar("Please input host name!")
    else:
        try:
            f = open(f"{namehost}", "w")
            f.write(f"{ip} growtopia1.com\n")
            f.write(f"{ip} growtopia2.com")
            f.close()
            sg.popup_no_titlebar("Your host has been created!", background_color='brown')
        except Exception as e:
            sg.popup_no_titlebar("Please input host name!")

def serverdata():
    ip = values["ip"]
    port = values["port"]
    f = open("server_data.php", "w")
    f.write(f"""server|{ip}
port|{port}
type|1
#maint|Maintenance message

beta_server|{ip}
beta_port|{port}

beta_type|1
meta|localhost
RTENDMARKERBS1001""")
    sg.popup_no_titlebar("Your server_data.php has been created!", background_color="brown")

def startserver():
    exe = values["exe"]
    proc = subprocess.Popen(f"start {exe}", shell=True, stderr=subprocess.PIPE)

def stopserver():
    exe = values["exe"]
    proc = subprocess.Popen(f"taskkill /f /im {exe}", shell=True, stderr=subprocess.PIPE)

def autoup():
    exe = values["exe"]
    if ".exe" in exe:
        try:
            f = open("autoup.bat")
            f.close()
            subprocess.Popen(f"start autoup.bat", shell=True, stderr=subprocess.PIPE)
        except FileNotFoundError:
            f = open("autoup.bat", "w")
            f.write(f"@echo off\n:loop\nstart /w {exe}\ngoto loop")
            f.close()
            subprocess.Popen(f"start autoup.bat", shell=True, stderr=subprocess.PIPE)
    else:
        sg.popup_no_titlebar("""Please write ".exe" to!""")

def dontshowui():
    try:
        f = open("dontshowui.bat")
        f.close()
        subprocess.Popen(f"start dontshowui.bat", shell=True, stderr=subprocess.PIPE)
    except FileNotFoundError:
        f = open("dontshowui.bat", "w")
        f.write(f"""REG ADD "HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" /f /v DontShowUI /t REG_DWORD /d 1\npause""")
        f.close()
        subprocess.Popen(f"start dontshowui.bat", shell=True, stderr=subprocess.PIPE)

    sg.popup_no_titlebar("If you get error acces denied, run GTPS Tools as administrator", background_color="brown")

def download(args):
    if args == "Discord Bot Status":
        print("Downloading Discord Bot Status...")
        wget.download("https://bit.ly/3zSZvxD")
        print("\nDone!")
        sg.popup("Succesfully downloaded!")

    elif args == "GTPS Controller Discord":
        print("Downloading GTPS Controller Discord...")
        wget.download("https://bit.ly/3jNFoLv")
        print("\nDone!")
        sg.popup("Succesfully downloaded!")

    elif args == "Visual Studio":
        print("Downloading Visual Studio...")
        webbrowser.open("https://tinyurl.com/5nstjz7b")
        print("\nDone!")

def xampp():
    layoutxampp = [[sg.Text("If you want setup please make sure run this app as administrator\n\nDo you want install xampp?")],
                [sg.Button("Yes", key="xamppwin"), sg.Button("No", key="xamppno")]]
    windowxampp = sg.Window("Auto Setup", layoutxampp)
    eventx, valuesx = windowxampp.read()
    if eventx == "xamppwin":
        print("Downloading Xampp Windows...")
        wget.download("https://bit.ly/3mNbg4M")
        print("\nDone!")
        sg.popup("Succesfully download xampp!")
        windowxampp.close()
        ruleport()
        
    elif eventx == "xamppno":
        windowxampp.close()
        ruleport()

def ruleport():
    port = values["port"]
    print("Added firewall rule port..")
    proc = subprocess.run("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""", shell=True, stderr=subprocess.PIPE)
    subprocess.run("""netsh advfirewall firewall delete rule name="80" protocol=TCP localport=80""")
    subprocess.run(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
    subprocess.run(f"""netsh advfirewall firewall delete rule name="{port}" protocol=UDP localport={port}""")
    subprocess.run("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
    subprocess.run("""netsh advfirewall firewall add rule name="80" dir=in action=allow protocol=TCP localport=80""")
    subprocess.run(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")
    subprocess.run(f"""netsh advfirewall firewall add rule name="{port}" dir=in action=allow protocol=UDP localport={port}""")
    sg.popup("Succesfully adding rule!")
    firewall()
    if proc.stderr:
        sg.popup("Please run as administrator!", title="Error!")

def firewall():
    print("Turn off windows defender firewall..")
    subprocess.run("""netsh advfirewall set privateprofile state off""")
    subprocess.run("""netsh advfirewall set publicprofile state off""")
    sg.popup("Succesfully turn off windows firewall!")

def about():
    layoutabout = [[sg.Text("This application made by Jesen N#9071")],
                [sg.Button("Link App"), sg.Button("Youtube")],
                [sg.Button("Close")]]
    windowabout = sg.Window("About", layoutabout)
    eventa, valuesa = windowabout.read()
    if eventa == "Link App":
        webbrowser.open("http://github.com/jesen-n/gtps-tools")
        windowabout.close()

    elif eventa == "Youtube":
        webbrowser.open('https://www.youtube.com/channel/UCLIxrhhnzp6FOAIzaXmmX3w')
        windowabout.close()

    elif eventa == "Close":
        windowabout.close()

sg.theme("DarkAmber")   # Add a touch of color
# All the stuff inside your window.
choices = ("Visual Studio", "Discord Bot Status", "GTPS Controller Discord")
layout = [[sg.Text("Ip    :"), sg.Input(key="ip", size=(20, 20))], 
        [sg.Text("Port:"), sg.Input(key="port", size=(20, 20)), sg.Text("Default: 17091")],
        [sg.Button("Host Maker"), sg.Button("Server Data Maker"), sg.Button("Auto Setup")], 
        [sg.Text("")],
        [sg.Text("Executable Server Name:"), sg.Input(key='exe', size=(20, 20))],
        [sg.Button("Start Server"), sg.Button("Stop Server"), sg.Button("Auto UP"), sg.Button("DontShowUI")],
        [sg.Text("")],
        [sg.Text("Downloads:")],
        [sg.Listbox(choices, size=(30, len(choices)), key='download', enable_events=True)],
        [sg.Text("")],
        [sg.Button("About", button_color="orange"), sg.Button("Quit", button_color="red")]]

# Create the Window
window = sg.Window("GTPS Tools V1.0", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None,  "Quit"):   # if user closes window or clicks cancel
        break

    elif event == "Host Maker":
        if values["ip"] == "":
            sg.popup("Please input ip!", title="Error!")
        elif values["port"] == "":
            sg.popup("Please input port!", title='Error!')
        else:
            hostmaker()

    elif event == "Server Data Maker":
        if values["ip"] == "":
            sg.popup("Please input ip!", title="Error!")
        elif values["port"] == "":
            sg.popup("Please input port!", title='Error!')
        else:
            serverdata()

    elif event == "Start Server":
        if values["exe"] == "":
            sg.popup("Please input exe name!", title="Error!")
        else:
            startserver()
    
    elif event == "Stop Server":
        if values["exe"] == "":
            sg.popup("Please input exe name!", title="Error!")
        else:
            stopserver()

    elif event == "Auto Setup":
        if values["ip"] == "":
            sg.popup("Please input ip!", title="Error!")
        elif values["port"] == "":
            sg.popup("Please input port!", title="Error!")
        else:
            xampp()

    elif event == "Auto UP":
        if values["exe"] == "":
            sg.popup("Please input exe name!", title="Error!")
        else:
            autoup()

    elif event == "DontShowUI":
        dontshowui()

    elif event == "About":
        about()
    
    elif values["download"]:
        if values["download"][0] == "Discord Bot Status":
            download("Discord Bot Status")
        elif values["download"][0] == "GTPS Controller Discord":
            download("GTPS Controller Discord")
        elif values["download"][0] == "Visual Studio":
            download('Visual Studio')
        else:
            break 
        
window.close() 

import os, requests, json, shutil, subprocess, time, threading, sys
from os.path import join, isfile, isdir, expandvars

host = "38.22.104.219"

roblox_version = requests.get("http://setup.roblox.com/versionQTStudio").text or "version-cab881b8584d4028"

plugins_dir = expandvars(r"%LOCALAPPDATA%\Roblox\Plugins")
if not isdir(plugins_dir): print("no plugins dir"); exit()

dir = join(r"C:\Program Files (x86)\Roblox\Versions", roblox_version)
if not isdir(dir): print("no folder", dir); exit()

studio_exe = join(dir, "RobloxStudioBeta.exe")
if not isfile(studio_exe): print("no exe"); exit()

ronion_plugin = requests.get("https://raw.githubusercontent.com/DoctorPoptart/Ronion/main/lua/ronion_plugin.lua")
plugin_path = join(plugins_dir, "ronion_plugin.lua")
with open(plugin_path, "w") as file:
    file.write(ronion_plugin.text)

roblox_content = join(dir, "content")
custom_content = join(roblox_content, "custom")

if isdir(custom_content): shutil.rmtree(custom_content)
os.mkdir(custom_content)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

subprocess.Popen(f'"{studio_exe}" -task StartClient -server {host} -port 53640')

print(os.getpid())
def kys():
    subprocess.Popen(f'taskkill /F /PID {os.getpid()}')

def isstudio_open():
    while process_exists("RobloxStudioBeta.exe"):
        pass

    kys()

threading.Thread(target=isstudio_open).start()
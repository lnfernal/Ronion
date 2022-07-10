import os, requests, json, shutil, subprocess
from os.path import join, isfile, isdir, expandvars

import PySimpleGUI as sg

from flask import Flask, request, Request

request: Request = request

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

subprocess.Popen(f'"{studio_exe}" -task StartClient -server 38.22.104.219 -port 53640')

app = Flask(__name__)

@app.route("/")
def downloader():
    filename = request.headers.get("filename")
    if filename:
        path = join(custom_content, filename)
        with open(path, "wb") as file:
            file.write(request.data)
        return "success"
    return "failed"

if __name__ == "__main__":
    app.run("127.0.0.1", port=47302)
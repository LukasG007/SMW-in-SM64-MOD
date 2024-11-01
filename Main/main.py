import pymem
import pygetwindow as gw
import time
import subprocess
from playsound import playsound #import play sound library

SM64_STAR_COUNT_ADDRESS = 0x8033B21A #Place in code where star count is held ;)
CAKE_CREDIT_ID =$904AC4B0 # FROM smwcentral.net 192 bytes	Level Data	Thank You cake picture at the end level layout script
# NEED TO ADD THE POINTER TO LEVEL ID SECTION AND THEN CHECK IF LEVEL ID MATCHES BOWSER 3, IF IT DOES THEN MONITOR FOR CHANGES IN THAT SECTION OF MEMORY
# ANY CHANGE = CREDITS HAVE LOADED SO WE RETURN TO SM64

YOU_GOT_STAR = "star.mp3"
You_BEAT_SMW = "credits.mp3"
BACK_TO_GAME = "back.mp3"

PROJECT64_PROCESS = "Project64.exe"
SNES9X_PROCESS = "snes9x.exe"

def get_star_count():
    pm = pymem.Pymem(PROJECT64_PROCESS)
    star_count = pm.read_int(SM64_STAR_COUNT_ADDRESS)
    pm.close_process()
    return star_count

def check_smw_completion():
    pm = pymem.Pymem(SNES9X_PROCESS)
    level_complete = pm.read_int(SMW_LEVEL_COMPLETION_ADDRESS)
    pm.close_process()
    return game_complete

def switch_to_emulator(emulator):
    window = gw.getWindowsWithTile(emulator)[0]
    window.activate()

def start_snes9x():
    subprocess.Popen([SNES9X_PROCESS, "path/to/rom.smc"]) #PUT YOUR PATH TO SMW ROM HERE!!!
    time.sleep(2) 
    switch_to_emulator(SNES9X_PROCESS)
    playsound(YOU_GOT_STAR)

def close_snes9x():
    for window in gw.getWindowsWithTile(SNES9X_PROCESS):
        window.close()
    playsound(BACK_TO_GAME)

def main():
    previous_star_count = get_star_count()

    while True:
        current_star_count = get_star_count()
        #Check if star count increased by comparing prev and current star count
        if current_star_count > previous_star_count
        print("Star Collected! Switching to SMW...")
        start_snes9x()

        while not check_smw_completion():
            time.sleep(1)

        print("SMW level completed! Returning to SM64...")
        close_snes9x()
        switch_to_emulator(PROJECT64_PROCESS)

        #update previous star_counter to avoid triggers that are false
        previous_star_count = current_star_count

    time.sleep(1)

    if __name__ == "__main__":
        main()
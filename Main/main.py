import pymem
import pygetwindow as gw
import time
import subprocess

SM64_STAR_COUNT_ADDRESS = 0x8033B21A
SMW_CREDIT_CHECK_ADDRESS = 0x00000000

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

def close_snes9x():
    for window in gw.getWindowsWithTile(SNES9X_PROCESS):
        window.close()

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
print("Herzlich Willkommen")

user_speed = input("Enter Speed in kmh: ")
speed_kmh = int(user_speed)

user_length = input("Enter Length in meter: ")
mainlength = int(user_length)

user_safetydistance = input ("Enter safetydistance: ")
safetydistance = int (user_safetydistance)


# main.py (Just for fun ^^)

import time
import sys

animation = "/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.1)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 3:  # The animation will last for 5 seconds
        break
sys.stdout.write("\rDone!")


def calc_blockdistance_and_time(brakedelay):
    # Speed in m/s
    v = speed_kmh * 1000 / 3600
    
    # Brakedistance calculation
    brakedistance = (v ** 2) / (2 * brakedelay)
    
    # Blockdistance calculation
    blockdistance = brakedistance + safetydistance
    
    # Time to cover blockdistance (in seconds)
    time_to_cover_blockdistance = blockdistance / v
    
    # Blocklength 
    signalblock = mainlength / blockdistance

    return blockdistance, time_to_cover_blockdistance, signalblock 

blockdistance, time_to_cover_blockdistance, signalblock = calc_blockdistance_and_time(0.65)

print(f"The blockdistance amounts to: {blockdistance:.2f} meters")
print(f"The time to cover the blockdistance is: {time_to_cover_blockdistance:.2f} seconds")
print(f"You have {signalblock:.0f} Blocksignals to place")


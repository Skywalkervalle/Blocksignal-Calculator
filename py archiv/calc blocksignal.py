def calc_blockdistance_and_time(speed_kmh, brakedelay, safetydistance, mainlength):
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

# Currently: Speed = 140 km/h, Brakedelay = 0.5 m/s², Safetydistance = 400 m, !! Mainlegth = 40 km !!
blockdistance, time_to_cover_blockdistance, signalblock = calc_blockdistance_and_time(200, 0.65, 600, 110000)

print(f"The blockdistance amounts to: {blockdistance:.2f} meters")
print(f"The time to cover the blockdistance is: {time_to_cover_blockdistance:.2f} seconds")
print(f"You have {signalblock:.0f} Blocksignals to place")

# def calc_blocktime (speed_kmh, safetydistance):
    #v = speed_kmh * 1000 / 3600
    # Drive time
    # blocktime = (blockdistance - safetydistance) * (speed_kmh/100)
    
    # return blocktime
    
# Currently: Speed = 140 km/h,
# blocktime = calc_blocktime (140, 4) 
# print(f"The blocktime amounts: {(blocktime):.3f} minutes.")
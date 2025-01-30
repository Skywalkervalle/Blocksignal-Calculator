def calc_blockdistance (speed_kmh, brakedelay, safetydistance):
    # Speed in m/s
    v = speed_kmh * 1000 / 3600
    
    # Brakedistance calc
    brakedistance = (v ** 2) / (2 * brakedelay)
    
    # Blockabstand calc
    blockdistance = brakedistance + safetydistance
    
    return blockdistance

# Currently: Speed = 140 km/h, Brakedelay = 0.5 m/s², Safetydistance = 900 m
blockdistance = calc_blockdistance (140, 0.5, 900)
print(f"The blockdistance amounts : {blockdistance:.2f} meters")

def calc_blocktime (speed_kmh):
    # Drive time
    blocktime = blockdistance * speed_kmh

    return blocktime

blocktime = calc_blocktime (140) 
print(f"The blocktime amounts: {blocktime:.2f}")
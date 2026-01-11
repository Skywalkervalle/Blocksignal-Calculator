import time
import sys

# Einführung
print("Herzlich Willkommen")

user_speed = input("Enter Speed in km/h: ")
speed_kmh = int(user_speed)

user_length = input("Enter Length in meter: ")
mainlength = int(user_length)

user_safetydistance = input("Enter safetydistance in meters: ")
safetydistance = int(user_safetydistance)

# Eingabe der Verzögerung durch Einfahrsignal in Metern
user_signal_delay_meters = input("Enter delay caused by the entrance signal (in meters): ")
signal_delay_meters = float(user_signal_delay_meters)

# Hauptanimation (Just for fun ^^)
animation = "/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.1)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 3:  # The animation will last for 3 seconds
        break
sys.stdout.write("\rDone!\n")

# Funktion zur Berechnung von Blockdistance und Zeit
def calc_blockdistance_and_time(brakedelay, signal_delay_meters):
    # Geschwindigkeit in m/s
    v = speed_kmh * 1000 / 3600
    
    # Bremsweg-Berechnung
    brakedistance = (v ** 2) / (2 * brakedelay)
    
    # Blockdistance Berechnung (Bremsweg + Sicherheitsabstand + Verzögerung durch das Einfahrsignal)
    blockdistance = brakedistance + safetydistance + signal_delay_meters
    
    # Zeit, um die Blockdistance zu überwinden (in Sekunden)
    time_to_cover_blockdistance = blockdistance / v
    
    # Blocklänge (Anzahl der Signalblöcke)
    signalblock = mainlength / blockdistance

    # Rückgabe der Berechnungen
    return blockdistance, time_to_cover_blockdistance, signalblock

# Aufruf der Funktion mit der Bremsverzögerung und Einfahrsignal-Verzögerung
blockdistance, time_to_cover_blockdistance, signalblock = calc_blockdistance_and_time(0.65, signal_delay_meters)

# Ausgabe der Berechnungen
print(f"The blockdistance amounts to: {blockdistance:.2f} meters")
print(f"The time to cover the blockdistance is: {time_to_cover_blockdistance:.2f} seconds")
print(f"You have {signalblock:.0f} Blocksignals to place")
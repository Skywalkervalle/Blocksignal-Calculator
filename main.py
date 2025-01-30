def berechne_blockabstand(geschwindigkeit_kmh, bremsverzoegerung, sicherheitsabstand):
    # Geschwindigkeit in m/s umrechnen
    v = geschwindigkeit_kmh * 1000 / 3600
    
    # Bremsweg berechnen
    bremsweg = (v ** 2) / (2 * bremsverzoegerung)
    
    # Blockabstand berechnen
    blockabstand = bremsweg + sicherheitsabstand
    
    return blockabstand

# Beispiel: Geschwindigkeit = 100 km/h, Bremsverzögerung = 0.5 m/s², Sicherheitsabstand = 500 m
blockabstand = berechne_blockabstand(140, 0.5, 900)
print(f"Der Blockabstand beträgt: {blockabstand:.2f} Meter")
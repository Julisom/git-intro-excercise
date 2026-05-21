# Funktion 1
def strom_berechnen(leistung, spannung):
    strom = leistung / spannung
    return strom
# Funktion 2
def spannungsfall(strom, widerstand):
    u_verlust = strom * widerstand 
    return u_verlust
# Funktion 3
def verlustleistung(strom, widerstand):
    p_verlust = (strom * strom) * widerstand
    return p_verlust


leistung = 2000   # Watt
spannung = 230    # Volt
widerstand = 0.5  # Ohm

strom = strom_berechnen(leistung, spannung)
u_verlust = spannungsfall(strom, widerstand)
p_verlust = verlustleistung(strom, widerstand)

print("Strom:", round(strom, 2), "A")
print("Spannungsfall:", round(u_verlust, 2), "V")
print("Verlustleistung:", round(p_verlust, 2), "W")

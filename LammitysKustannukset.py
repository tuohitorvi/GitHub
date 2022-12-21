#Tama ohjelma kyselee kayttajalta tietoja kiinteiston lammitystavasta, laskee valitun
#lammitysmuodon ja annettujen parametrien avulla paljonko lampoenergiaa saadaan ja
#paljonko se maksaa.
#(c) Martti Savolainen

class HeatingSystem:
    def __init__(self, source, duty_cycle, power, heating_period, e_price):
        self.source = source
        self.duty_cycle = duty_cycle
        self.power = power
        self.heating_period = heating_period
        self.e_price = e_price

    def heating_power(self):
        return self.duty_cycle * self.power

    def produced_energy(self):
        return self.heating_power() * self.heating_period

    def energy_cost(self):
        return ((self.produced_energy() * self.e_price) / 100)
        

# Tietojen syotto:

src = str(input('Mika lammitysmuoto? (puu / sahko / maalampo) '))
pwr = int(input('Lammityslaitteen teho (kW): '))
h_per = int(input('Lammitykseen kaytetty aika (h): '))
price = float(input('Energian hinta (snt/kWh): '))  

# 3 erilaista lammitystapaa:

puu = HeatingSystem(src, 0.7, pwr, h_per, price)
sahko = HeatingSystem(src, 1.0, pwr, h_per, price)
maalampo = HeatingSystem(src, 3.0, pwr, h_per, price)

# Tulostus:

if src == "puu":
    print("Lammitysteho puulammityksella: ", puu.heating_power(), " kW")
    print("Tuotettu lampoenergia puulammityksella: ", puu.produced_energy(), " kWh")
    print("Lammitys maksoi: ", puu.energy_cost(), " euroa")
elif src == "sahko":
    print("Lammitysteho sahkolammityksella: ", sahko.heating_power(), " kW")
    print("Tuotettu lampoenergia sahkolammityksella: ", sahko.produced_energy(), " kWh")
    print("Lammitys maksoi: ", sahko.energy_cost(), " euroa")
elif src == "maalampo":
    print("Lammitysteho maalammolla: ", maalampo.heating_power(), " kW")
    print("Tuotettu lampoenergia maalammolla: ", maalampo.produced_energy(), " kWh")
    print("Lammitys maksoi: ", maalampo.energy_cost(), " euroa")
else:
    print("Tuntematon lammitystapa!")

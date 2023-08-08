import sqlite3
import os
import csv

charger_db = "chargers.db"
charger_register = "national-charge-point-registry.csv"

"""
A class defining the charger infomation we care about
"""
class Charger:
    def __init__(self, id, name, town, lat, long, postcode, inService, sub, parkFee, connType, power):
        self.id = id
        self.name = str(name)
        self.town = town
        self.lat = lat
        self.long = long
        self.pc = postcode
        self.inService = True if (0 == inService) else False
        self.sub = True if (0 == sub) else False
        self.parkFee = True if (0 == parkFee) else False
        self.connType = connType
        self.power = power

    def __str__(self):
        """
        Format class as an entry for the datebase table
        """
        return f"(\"{self.id}\",\"{self.name}\",\"{self.town}\",{self.lat},{self.long},\"{self.pc}\",{self.inService},{self.sub},{self.parkFee},\"{self.connType}\",{self.power})"

# The global list of chargers
chargers = []

"""
Create the charger database from the list of chargers
"""
def create_database():
    global chargers
    print("Creating car charger database")

    if os.path.exists(charger_db):
        os.remove(charger_db)

    con = sqlite3.connect(charger_db)

    cur = con.cursor()

    cur.execute("CREATE TABLE charger(id,name,town,latitude,longitude,postcode,inService,subscriptionRequired,parkingFees,connectorType,power)")

    for i in range(len(chargers)):
        # print("Adding record " + str(i))
        cmd = "INSERT INTO charger VALUES" + str(chargers[i])
        # print(cmd)
        cur.execute(cmd)

    con.commit()
    con.close()

    print("database created")

"""
Read the charger data from the register
"""
def read_charger_data():
    print("Reading charger data from " + charger_register)

    csv_register = open(charger_register,"r")
    reader = csv.DictReader(csv_register)
    charger_id = 0
    charger_types = []

    for row in reader:
        if row['town'].isalpha and (float(row['latitude']) > 50.0):
            charger_id += 1
            # print(row['name'], row['town'],row['latitude'], row['longitude'])
            chargers.append(Charger(charger_id,
                                    row['name'],
                                    row['town'],
                                    row['latitude'], 
                                    row['longitude'],
                                    row['postcode'], 
                                    row['chargeDeviceStatus'], 
                                    row['subscriptionRequired'],
                                    row['parkingFeesFlag'],
                                    row['connector1Type'],
                                    row['connector1RatedOutputKW']))

            type = row['connector1Type']

            if type not in charger_types:
                 charger_types.append(type)

        else:
            print("Invalid data:",row['name'], row['town'],row['latitude'], row['longitude'])

    csv_register.close()
    print("Last id: " + str(charger_id))

    for type in charger_types:
        print(type)


 
"""
Main program starts here
"""
read_charger_data()

create_database()

print("Number of chargers added to database: {0}".format(len(chargers)))

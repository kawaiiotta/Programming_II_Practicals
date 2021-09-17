from silver_service_taxi import SilverServiceTaxi

silver_cab = SilverServiceTaxi("Silver Cab", 80, 2)
print(silver_cab)

silver_cab.drive(18)
print(silver_cab)
print(silver_cab.get_fare())


"""
Test for Taxi Class
"""

from taxi import Taxi

prius = Taxi("prius 1", 100)
prius.drive(18)
print(prius, prius.get_fare())
prius.start_fare()
prius.drive(100)
print(prius, prius.get_fare())

print(prius.get_fare())

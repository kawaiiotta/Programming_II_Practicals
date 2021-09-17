from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * self.price_per_km

    def get_fare(self):
        # return the price plus the initial fare
        distance_driven = super().get_fare() + self.flagfall
        return distance_driven

    def __str__(self):
        return "{}, plus flagfall of {}".format(super().__str__(), self.flagfall)

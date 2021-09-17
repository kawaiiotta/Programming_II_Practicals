from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = choose_taxi(taxis)
    distance = drive_taxi(current_taxi)
    current_taxi.drive(distance)
    print(current_taxi)
    print(current_taxi.get_fare())


def choose_taxi(taxis):
    print("Which Taxi do you wanna choose?")
    for i, taxi in enumerate(taxis):
        print(i, taxi)

    chosen = int(input())
    return taxis[chosen]


def drive_taxi(taxi):
    print("How far are you driving?")
    return float(input())


main()

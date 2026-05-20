class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city

def find_cheapest_flight(data):
    if data is None or not data:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data
    lowest_price = float(first_flight["price"])
    origin_city = first_flight["cityFrom"]
    origin_airport = first_flight["flyFrom"]
    destination_city = first_flight["cityTo"]
    destination_airport = first_flight["flyTo"]
    out_date = first_flight["route"][0]["local_departure"].split("T")[0]
    return_date = first_flight["route"][-1]["local_departure"].split("T")[0]

    return FlightData(
        lowest_price,
        origin_city,
        origin_airport,
        destination_city,
        destination_airport,
        out_date,
        return_date
    )
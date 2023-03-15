class Edge:
    def __init__(self, company, line, departure, arrival, start, end, start_lan, start_lon, stop_lat, stop_lon):
        self.company = company
        self.line = line

        departure_time = departure.split(":")
        departure_in_seconds = int(departure_time[0])*3600 + int(departure_time[1])*60 + int(departure_time[2])
        self.departure = departure_in_seconds

        arrival_time = arrival.split(":")
        arrival_in_seconds = int(arrival_time[0]) * 3600 + int(arrival_time[1]) * 60 + int(arrival_time[2])
        self.arrival = arrival_in_seconds

        self.start = start
        self.end = end
        self.start_lan = start_lan
        self.start_lon = start_lon
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon

    def __str__(self):
        return (self.company + " " +
        self.departure + " " +
        self.line + " " +
        self.arrival + " " +
        self.start + " " +
        self.end + " " +
        self.start_lan + " " +
        self.start_lon + " " +
        self.stop_lat + " " +
        self.stop_lon)
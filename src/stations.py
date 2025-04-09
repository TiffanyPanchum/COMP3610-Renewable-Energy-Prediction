from meteostat import Stations
from datetime import datetime

# Italy
stations = Stations()
stations = stations.nearby(41.8967, 12.4822)
stations = stations.inventory('hourly', datetime(2016, 1, 1))
station = stations.fetch(5)
print(station)

# Spain 
stations = Stations()
stations = stations.nearby(40.4167, 3.7033)
stations = stations.inventory('hourly', datetime(2016, 1, 1))
station = stations.fetch(5)
print(station)

# France
stations = Stations()
stations = stations.nearby(48.8575, 2.3514)
stations = stations.inventory('hourly', datetime(2016, 1, 1))
station = stations.fetch(5)
print(station)


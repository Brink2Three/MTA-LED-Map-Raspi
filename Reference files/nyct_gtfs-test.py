import os
from datetime import datetime, timedelta

from nyct_gtfs import NYCTFeed


def main():
    feed = NYCTFeed("1", api_key='API KEY HERE')
    trips = feed.filter_trips(line_id=["1"], travel_direction="N")
    print(trips[1])
    print(trips[2])
    print(trips[3])
    print(trips[4])
    print(trips[5])
    print(trips[6])
    print(trips[7])
    print(trips[8])
    print(trips[9])
    print(trips[10])
    trips = feed.filter_trips(line_id=["1"], travel_direction="S")
    print(trips[1])
    print(trips[2])
    print(trips[3])
    print(trips[4])
    print(trips[5])
    print(trips[6])
    print(trips[7])
    print(trips[8])
    print(trips[9])
    print(trips[10])


if __name__ == '__main__':
    main()
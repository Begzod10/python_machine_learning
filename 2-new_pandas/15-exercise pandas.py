import datetime
import pprint
import numpy as np
import pandas as pd

hotels = pd.read_csv("files/hotel_booking_data.csv")


# 1 -- hotels.head()
# 2 -- hotels.info()

# 3 -- print(len(hotels))
# 4 -- res = hotels.isnull().sum() -> bosh danniylarni hisoblab beradi
# 5 -- print(hotels['company'].isna().sum()) -> bosh danniylarni hisoblab beradi

# 6 -- null_values = hotels.drop('company', axis=1)
# 7 -- res = hotels.sort_values('adr', ascending=False)[['adr', 'name']] -> adr column value si boyicha teskari taxlab, name, adr column boyicha filterlab beradi
# 8 -- res = hotels.sort_values('adr', ascending=False)[['adr']].mean() == res = round(hotels['adr'].mean(), 2)
# 9 -- hotels['total_days'] = hotels['stays_in_week_nights'] + hotels['stays_in_weekend_nights']


# 10
# hotels['total_days'] = hotels['stays_in_week_nights'] + hotels['stays_in_weekend_nights']
# hotels['total_booking'] = hotels['adr'] * hotels['total_days']
# print(round(hotels['total_booking'].mean(), 2))

# 11
# res = hotels[hotels['total_of_special_requests'] == 5][['name', 'email']]

# 12
#
# num = len(hotels[hotels['is_repeated_guest'] == True])
# res = round((num / len(hotels)) * 100, 2)

# 13

# res = hotels['num_name'] = hotels['name'].apply(lambda name: name.split()[0]).value_counts()
# res = hotels['name'].apply(lambda name: name.split()[1]).value_counts()[:5]

# 14
# hotels['total_kids'] = hotels['children'] + hotels['babies']
# res = hotels.sort_values('total_kids', ascending=False)[['name', 'adults', 'total_kids', 'babies', 'children']]
# res = hotels['phone-number'].apply(lambda number: number[:3]).value_counts()[:3]

# 15
# res = hotels['arrival_date_day_of_month'].apply(lambda num: 0 < num <= 15).sum()
# res = hotels['arrival_date_day_of_month'].apply(lambda num: num in range(1, 16)).sum()
# print(res)

# hotel
# is_canceled
# lead_time
# arrival_date_year
# arrival_date_month
# arrival_date_week_number
# arrival_date_day_of_month
# stays_in_weekend_nights
# stays_in_week_nights
# adults
# children
# babies
# meal
# country
# market_segment
# distribution_channel
# is_repeated_guest
# previous_cancellations
# previous_bookings_not_canceled
# reserved_room_type
# assigned_room_type
# booking_changes
# deposit_type
# agent
# company
# days_in_waiting_list
# customer_type
# adr
# required_car_parking_spaces
# total_of_special_requests
# reservation_status
# reservation_status_date
# name
# email
# phone-number
# credit_card

def convert(day, month, year):
    return f'{day}-{month}-{year}'


# hotels = hotels.drop('index')

# hotels['date'] = datetime.datetime.strptime(str(hotels['arrival_date_year']) + str(hotels['arrival_date_month']) + str(
#     ['arrival_date_day_of_month']), "%Y-%B-%d")
# date = datetime.datetime.strptime(str(hotels['arrival_date_month']), "%B")

# vectorize -> The NumPy vectorize function (np. vectorize) is provided by the Python library. It accepts a nested sequence of objects or a NumPy array as input and returns a single NumPy array or a tuple of NumPy arrays as output.
hotels['date'] = np.vectorize(convert)(hotels['arrival_date_day_of_month'],
                                       hotels['arrival_date_month'],
                                       hotels['arrival_date_year'])
hotels['date'] = pd.to_datetime(hotels['date'])
res = hotels['date'].dt.day_name().value_counts()
print(res)


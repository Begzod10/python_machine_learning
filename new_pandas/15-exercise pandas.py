import pprint

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
res = hotels[hotels['total_of_special_requests'] == 5][['name', 'email']]

# 12

hotels['num_is_repeated_guest'] = hotels[hotels['is_repeated_guest'] == True]
print()
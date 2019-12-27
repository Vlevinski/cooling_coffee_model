# open database connectiontry:
occupancy = 105

try:
    a = 1
    # Fetch data from database
    if occupancy > 100:
        raise Exception('Occupancy cannot be greater than 100')
except Exception as e:
    # print the exception
    print(e)
finally:
    print('Closing database connection')
    # close database connection





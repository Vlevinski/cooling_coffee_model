class House:
    # define instance method
    def set_rooms(self, num_rooms):
        self.rooms = num_rooms# Create instance of the class - creating an actual house
house_small = House()# Calling instance method for instance 'house_small'
house_small.set_rooms(2)# Create another instance
house_big = House()
house_big.set_rooms(5)
print(f'# of rooms in small house: {house_small.rooms}')
print(f'# of rooms in big house: {house_big.rooms}')
#Output:
# of rooms in small house: 2
# of rooms in big house: 5


"""
Define an inheritance hierarchy 

The superclass is called 'Area'

Area must carry information such as the geofence (the set of location objects (check location.py file)) that mark the boundries of the area

2 subclasses called 'Restaurant' and 'Exhibit' inherit from the superclass

The restaurant subclass must contain information such as restaurant type (cafe, takeaway, etc) and more information 
that you feel is relevant

The Exhibit subclass must contain information such as animal, whether or not it is open or closed, etc and more information 
that you feel is relevant

"""

from src.location import Location

class Area:

  def __init__(self,name,geofence: list[Location]): # geofence is a list of location objects
    self.name = name
    self.geofence = geofence

  def add_location(self,location): # adds a location to the geofence
    self.geofence.append(location)

  def remove_location(self,location): # removes a location from the geofence
    self.geofence.remove(location)

  def get_geofence(self):
    return self.geofence


class Restaurant(Area):

  def __init__(self,name,geofence,restaurant_type,menu=None):
    super().__init__(name,geofence) # refers to the Area constructor (superclass) to determine the name and geofence
    self.restaurant_type = restaurant_type
    self.menu = menu if menu is not None else []

  def set_restaurant_type(self,restaurant_type): # sets the restaurant type
    self.restaurant_type = restaurant_type

  def get_restaurant_type(self): # gets the type of restaurant e.g. cafe, takeaway etc
    return self.restaurant_type

  def add_menu_item(self,item): # adds an item to the restaurant menu
    self.menu.append(item)

  def get_menu(self): # gets the menu of a restaurant
    return self.menu


class Exhibit(Area):

  def __init__(self,name,geofence,animal,is_open):
    super().__init__(name,geofence)
    self.animal = animal
    self.is_open = is_open

  def set_animal(self,animal): # sets the animal in an exhibit
    self.animal = animal

  def get_animal(self): # gets an animal in the exhibit
    return self.animal

  def open_exhibit(self): # opens an exhibit
    self.is_open = True

  def closed_exhibit(self): # closes an exhibit
    self.is_open = False

  def is_exhibit_open(self): # informs whether the exhibit is open or not
    return self.is_open
                  
  
  
    

 
     

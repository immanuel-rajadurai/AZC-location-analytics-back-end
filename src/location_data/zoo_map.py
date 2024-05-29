"""
Define the ZooMap class

The ZooMap class stores information about a zoo, including:
- The name of the zoo (String)
- The country where the zoo is located (String)
- The city where the zoo is located (String)
- The average number of visitors per year (int)

The class includes a method to display this information.
"""
class ZooMap:
    def __init__(self, name: str, country: str, city: str, average_visitors_per_year: int):
        # Initialize the attributes for the zoo map
        self.name = name  # Name of the zoo (String)
        self.country = country  # Country of the zoo (String)
        self.city = city  # City of the zoo (String)
        self.average_visitors_per_year = average_visitors_per_year  # Average number of visitors per year (int)

    def display_info(self):
        formatted_visitors = "{:,}".format(self.average_visitors_per_year)  # Format number with commas
        print(f"Name of the zoo: {self.name}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Average number of visitors per year: {formatted_visitors}")


# Example 
if __name__ == "__main__":
    # Create an instance of ZooMap
    zoo1 = ZooMap("London Zoo", "United Kingdom", "London", 1300000)
    zoo1.display_info()

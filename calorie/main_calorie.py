import requests
from selectorlib import Extractor


class User:
    """defines a user with information about weight,height and age"""

    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age


class Temperature:
    """defines the temperature using the user's city and country by web scrapping"""

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def get_temp(self):
        """returns the temperature"""
        r = requests.get('https://www.timeanddate.com/weather/' + self.country + '/' + self.city)
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        row_result = extractor.extract(c)
        ans = ""
        for i in row_result['temp'].split():
            if i.isdigit():
                ans += i
        result = float(ans)
        return result


class Calorie(Temperature, User):
    def __init__(self, city, country, weight, height, age):
        User.__init__(self, weight, height, age)
        Temperature.__init__(self, city, country)

    def calculate(self):
        """ returns the required calorie value"""
        calorie = 10 * self.weight + 6.5 * self.height + 5 - self.get_temp() * 10
        return calorie

'''
cal = Calorie("rome", "italy", 70, 135, 23)
print(cal.calculate())'''

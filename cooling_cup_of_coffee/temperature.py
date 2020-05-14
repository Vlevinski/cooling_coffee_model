# https://stackoverflow.com/questions/55313769/not-getting-expected-result-using-descriptor-in-python


class Temperature:
    """ Get temperature from value xC, or xK, or xF  in Celsius, Kelvin or Fahrenheit"""

    def __init__(self, value):
        self.value = value
        # self.celsius = self._Celsius()
        # self.kelvin = self._Kelvin()
        # self.fahrenheit = self.to_Fahrenheit()
        try:
            if value[-1].upper() in ['C', 'F', 'K']:
                self.value = value.upper()
            else:
                raise ValueError('Temperature must be C|F|K')
        except ValueError:
            print ("Value error, Jim")
        if self.value[-1] is "C": self._Celsius()
        elif self.value[-1] is "F": self._Fahrenheit()
        elif self.value[-1] is "K": self._Kelvin()

    def _Celsius(self):
        # _Fahrenheit = (value * 9 / 5) + 32;
        # _Kelvin = value + 273.15;
        print("Tt's Celsius, Jim. T:", end=" ")

    def _Fahrenheit(self):
        # _Celsius = (value - 32) * 5/9;
        # _Kelvin = _Celsius + 273.15;
        print("It's Fahrenheit, Jim  T:", end=" ")

    def _Kelvin(self):
        # _Celsius = value - 273.15;
        # _Fahrenheit = (_Celsius * 9 / 5) + 32;
        print("It's Kelvin, Jim T:", end=" ")


t = Temperature("23C")
print (t.value)

# https://stackoverflow.com/questions/55313769/not-getting-expected-result-using-descriptor-in-python


class Temperature:
    """ Get temperature from xC, or xK, or xF value, where value is Celsius, Kelvin or Fahrenheit"""

    def __init__(self, value):
        self.value = value
        # self.celsius = self._celsius()
        # self.kelvin = self._kelvin()
        # self.fahrenheit = self._fahrenheit()
        try:
            if value[-1].upper() in ['C', 'F', 'K']:
                self.value = value.upper()
            else:
                raise ValueError('Temperature must be C|F|K')
        except ValueError as e:
            print("Value error, Jim.", e)
        if self.value[-1] is "C":
            self._celsius()
        elif self.value[-1] is "F":
            self._fahrenheit()
        elif self.value[-1] is "K":
            self._kelvin()

    def _celsius(self):
        # _Fahrenheit = (value * 9 / 5) + 32;
        # _Kelvin = value + 273.15;
        print("Tt's Celsius, Jim. T:", end=" ")

    def _fahrenheit(self):
        # _Celsius = (value - 32) * 5/9;
        # _Kelvin = _Celsius + 273.15;
        print("It's Fahrenheit, Jim  T:", end=" ")

    def _kelvin(self):
        # _Celsius = value - 273.15;
        # _Fahrenheit = (_Celsius * 9 / 5) + 32;
        print("It's Kelvin, Jim T:", end=" ")


t = Temperature("23a")
print(t.value)

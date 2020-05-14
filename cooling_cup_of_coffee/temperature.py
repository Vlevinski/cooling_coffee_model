# https://stackoverflow.com/questions/55313769/not-getting-expected-result-using-descriptor-in-python


class Temperature:
    """ Get temperature from value xC, or xK, or xF  in Celsius, Kelvin or Fahrenheit"""

    def __init__(self, value):
        self.value = value
        # self.celsius = self._Celsius()
        # self.kelvin = self._Kelvin()
        # self.fahrenheit = self.to_Fahrenheit()
        if value[-1].upper() in ['C', 'F', 'K']:
            self.value = value.upper()
        else:
            raise ValueError('Temperature must be C|F|K')

    def _Celsius(self):
        # _Fahrenheit = (value * 9 / 5) + 32;
        # _Kelvin = value + 273.15;
        pass

    def _Fahrenheit(self):
        # _Celsius = (value - 32) * 5/9;
        # _Kelvin = _Celsius + 273.15;
        pass

    def _Kelvin(self):
        # _Celsius = value - 273.15;
        # _Fahrenheit = (_Celsius * 9 / 5) + 32;
        pass

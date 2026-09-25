class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise RuntimeError("Temperature must be at least 273.15")

        self._temperature = value

t = Temperature(273.15)
print(t.temperature)
t.temperature = -2
print(t.temperature)
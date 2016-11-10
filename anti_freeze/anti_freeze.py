import operator

from anti_freeze.fuzzy import Fuzzy


class AntiFreeze(object):

    # Values that can get from wind fuzzification
    SOFT_WIND = 'Suave'
    MODERATE_WIND = 'Moderado'
    VIVID_WIND = 'Vivo'

    # Values that can get from humidity fuzzification
    LOW_HUMIDITY = 'Bajo'
    MODERATE_HUMIDITY = 'Moderado'
    HIGH_HUMIDITY = 'Alto'

    # Inference values
    NOT_FREEZE = 'Sin helada'
    ADVECTION = 'Advección'
    RADIATION = 'Radiación'
    EVAPORATION = 'Evaporación'
    MIXED = 'Mixto'

    TABLE = {
        SOFT_WIND: {
            LOW_HUMIDITY: NOT_FREEZE,
            MODERATE_HUMIDITY: RADIATION,
            HIGH_HUMIDITY: EVAPORATION,
        },
        MODERATE_WIND: {
            LOW_HUMIDITY: ADVECTION,
            MODERATE_HUMIDITY: RADIATION,
            HIGH_HUMIDITY: MIXED,
        },
        VIVID_WIND: {
            LOW_HUMIDITY: ADVECTION,
            MODERATE_HUMIDITY: ADVECTION,
            HIGH_HUMIDITY: MIXED,
        },
    }

    def __init__(self):
        pass

    def __fuzzy_wind__(self, value=float()):
        values = {
            self.SOFT_WIND: Fuzzy.trapecio_abierto_izq(u=value, a=15.0, b=30.0),
            self.MODERATE_WIND: Fuzzy.triangular(u=value, a=15.0, b=30.0, c=45.0),
            self.VIVID_WIND: Fuzzy.trapecio_abierto_der(u=value, a=30.0, b=45.0),
        }

        return sorted(values.items(), key=operator.itemgetter(1), reverse=True).pop(0)

    def __fuzzy_humidity__(self, value=float()):
        values = {
            self.LOW_HUMIDITY: Fuzzy.trapecio_abierto_izq(u=value, a=25.0, b=50.0),
            self.MODERATE_HUMIDITY: Fuzzy.triangular(u=value, a=25.0, b=50.0, c=75.0),
            self.HIGH_HUMIDITY: Fuzzy.trapecio_abierto_der(u=value, a=50.0, b=75.0),
        }

        return sorted(values.items(), key=operator.itemgetter(1), reverse=True).pop(0)

    def fuzzy(self, wind=float(), humidity=float()):
        values = {
            'wind': self.__fuzzy_wind__(wind),
            'humidity': self.__fuzzy_humidity__(humidity),
        }

        return {
            'inference': self.TABLE[values['wind'][0]][values['humidity'][0]],
            'wind': values['wind'][0],
            'wind_value': values['wind'][1],
            'humidity': values['humidity'][0],
            'humidity_value': values['humidity'][1],
        }

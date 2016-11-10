from math import cos, pi


class Fuzzy(object):

    @staticmethod
    def trapecio_abierto_der(u=float(), a=float(), b=float()) -> float():
        if u > b:
            return 1.0
        elif u < a:
            return 0.0
        else:
            return (u - a) / (b - a)

    @staticmethod
    def trapecio_abierto_izq(u=float(), a=float(), b=float()) -> float():
        if u > b:
            return 0.0
        elif u < a:
            return 1.0
        else:
            return (b - u) / (b - a)

    @staticmethod
    def triangular(u=float(), a=float(), b=float(), c=float) -> float():
        if u < a or u > c:
            return 0.0
        elif a <= u < b:
            return (u - a) / (b - a)
        elif b <= u <= c:
            return (c - u) / (c - b)

    @staticmethod
    def trapezoidal(u=float(), a=float(), b=float(), c=float(), d=float()) -> float():
        if u < a or u > d:
            return 0.0
        elif b <= u <= c:
            return 1.0
        elif a <= u < b:
            return (u - a) / (b - a)
        elif c < u <= d:
            return (d - u) / (d - c)

    @staticmethod
    def curva_s(u=float(), a=float(), b=float()) -> float():
        if u > b:
            return 1.0
        elif u < a:
            return 0.0
        elif a <= u <= b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0

    @staticmethod
    def curva_z(u=float(), a=float(), b=float()) -> float():
        if u > b:
            return 0.0
        elif u < a:
            return 1.0
        elif a <= u <= b:
            return (1 + cos(((u - a) / (b - a)) * pi)) / 2.0

    @staticmethod
    def triangular_suave(u=float(), a=float(), b=float(), c=float) -> float():
        if u < a or u > c:
            return 0.0
        elif a <= u < b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
        elif b <= u <= c:
            return (1 + cos(((b - u) / (c - b)) * pi)) / 2.0

    @staticmethod
    def trapezoidal_suave(u=float(), a=float(), b=float(), c=float(), d=float()) -> float():
        if u < a or u > d:
            return 0.0
        elif a <= u <= c:
            return 1.0
        elif a <= u < b:
            return (1 + cos(((u - b) / (b - a)) * pi)) / 2.0
        elif c < u <= d:
            return (1 + cos(((c - u) / (d - c)) * pi)) / 2.0

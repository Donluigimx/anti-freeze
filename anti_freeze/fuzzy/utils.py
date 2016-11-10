
class Utils(object):

    @staticmethod
    def min(a=float(), b=float()) -> float():
        if a < b:
            return a
        else:
            return b

    @staticmethod
    def max(a=float(), b=float()) -> float():
        if a > b:
            return a
        else:
            return b

    @staticmethod
    def comp_and(ma_u=float(), mb_u=float()) -> float():
        return Utils.min(a=ma_u, b=mb_u)

    @staticmethod
    def comp_or(ma_u=float(), mb_u=float()) -> float():
        return Utils.max(a=ma_u, b=mb_u)

    @staticmethod
    def niega(ma_u=float()) -> float():
        return 1.0 - ma_u

    @staticmethod
    def implica_zadeh(ma_x=float(), mb_y=float()) -> float():
        return Utils.max(Utils.min(ma_x, mb_y), Utils.niega(ma_x))

    @staticmethod
    def implica_mamdani(ma_x=float(), mb_y=float()) -> float():
        return Utils.min(ma_x, mb_y)

    @staticmethod
    def implica_godel(ma_x=float(), mb_y=float()) -> float():
        if ma_x <= mb_y:
            return 1.0
        else:
            return mb_y
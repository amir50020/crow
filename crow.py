class Crow:

    def __init__(self, par_count, pa_count, eyes_count):
        self.__par_count = par_count
        self.__pa_count = pa_count
        self.__eyes_count = eyes_count

    def set_eyes_count(self, eyes_count):
        if type(eyes_count) != int:
            raise TypeError
        try:
            if eyes_count < 1:
                self.__eyes_count = eyes_count
            else:
                raise ValueError
        except ValueError:
            print("this is <1")
        try:
            if eyes_count > 2:
                self.__eyes_count = eyes_count
            else:
                raise ValueError
        except ValueError:
            print("this is <2")

    def set_par_count(self, par_count):
        if type(par_count) != int:
            raise Exception("this is not int")
        if par_count < 0:
            raise Exception("this is <0")
        self.__par_count = par_count

    def set_pa_count(self, pa_count):
        if type(pa_count) != int:
            raise Exception("this is not int ")
        if pa_count < 0:
            raise Exception("this is  <0")
        self.__pa_count = pa_count

    def get_par_count(self):
        return self.__par_count

    def get_pa_count(self):
        return self.__pa_count

    def get_eyes_count(self):
        return self.__eyes_count

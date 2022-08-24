class Crow:
    def __init__(self, par_count, pa_count):
        self.__par_count = par_count
        self.__pa_count = pa_count

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

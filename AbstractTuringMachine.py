from abc import ABC, abstractmethod, abstractproperty

class AbstrakcyjnaMaszynaTuringa(ABC):

    @abstractproperty
    def ListStanow(self):
        pass

    @abstractproperty
    def Przejscia(self):
        pass

    #######################################

    @abstractmethod
    def WykonajKrok(self, ZnakZTasmy):
        pass

    @abstractmethod
    def Uruchom(self, Tasma):
        pass

    @abstractmethod
    def CzyStanJestPoczatkowy(self, Stan):
        pass

    @abstractmethod
    def CzyStanJestKoncowy(self, Stan):
        pass
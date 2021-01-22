class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = "caliente"):
        #Privado lo que no le interesa al cliente
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()


    def _llenar_tanque_agua(self, temperatura):
        print (f"Llenando el tanque con agua a {temperatura}")

    def _anadir_jabon(self):
        print("Anadiendo jabon")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("centrifugando ropa")


if __name__ == "__main__":
    Lavadora = Lavadora()
    Lavadora.lavar()

from ingredients import proteics, vegetables, doughs

class Pizza:
    """ Aplique atributos de clase para ejeuctar los punto 5.a y 5.e """
    proteic = None
    vegetable1 = None
    vegetable2 = None
    type_dough = None
    validate = None
 
    """
    Aplique el constructor __init__ para inicar el 
    objeto al momento de crear una nueva instancia
    """
    def __init__(self, proteic = None, vegetable1 = None, vegetable2 = None, type_dough = None):
        self.proteic = proteic
        self.vegetable1 = vegetable1
        self.vegetable2 = vegetable2
        self.type_dough = type_dough
        self.validate = False

    @staticmethod
    def elementValidate(element, posible_list):
        return element in posible_list
    
    def placeOrder(self):
        self.proteic = input("Ingrediente Proteico: ")
        self.vegetable1 = input("Ingrese Vegetal 1: ")
        self.vegetable2 = input("Ingrese Vegetal 2: ")
        self.type_dough = input("¿Qué tipo de masa desea?: ")

        if(
            self.elementValidate(self.proteic, proteics) and
            self.elementValidate(self.vegetable1, vegetables) and
            self.elementValidate(self.vegetable2, vegetables) and
            self.elementValidate(self.type_dough, doughs)
        ):
            self.validate = True
        else:
            self.validate = False
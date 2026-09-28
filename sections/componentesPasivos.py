
class ComponentesPasivos:
    def __init__(self, resistencia, condensadores, inductores):
        self.resistencia = resistencia
        self.condensadores = condensadores
        self.inductores = inductores
        



class Resistencia:
    def __init__(self, ohmios, potencia):
        self.ohmios = ohmios
        self.potencia = potencia

    
    def tipos_resistencia(self, tipo_resistencia):
        While True:
            print("*" * 80)
            print("1) RESISTENCIA \n2) POTENCIOMETRO")
            print("*" * 80)
            try:
                op = int(input("\nEscribe la opción: "))
                if op == 1:
                    print("Resistencia: ")
    
                    #Aquí iria la muestra de componentes de resistencia con su información
                elif op == 2: 
                    print("Potenciometros")
                    #Aquí iría los potenciometros con sus ohmios y sus pines
                elif op == 3 :
                    print("Atras ")
                    #Regreso hacia Atras, hacia el menu de los componentes, ya sea resistencias o capacitores.
                    break
                else:
                    print("Opción invalida, escribe una opoción valida")
            except valueError:
                print("Debes ingresar un núnemro valido")


    def lista_resistencia_disponibles(self):
        print("\nEstas son las listas de Capicidad que existen: \n")
    
    def lista_potenciometros_disponibles(self, potenciometro):
        return "hola"




class Potenciometro(Resistencia):
    def __init__(self,ohmios, potencia, pines):
        super().__init__(self,ohmios, potencia)
        self.ohmios = ohmios
        self.potencia = potencia
        self.pines = pines

    def cantidad_pines(self, pines):










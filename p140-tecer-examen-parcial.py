class Jugador:
    def __init__(self, nombre, año_nac, sexo, becado):
        self.nombre = nombre
        self.año_nac = año_nac
        self.sexo = sexo
        self.becado = becado
        self.costo = 0  

    def __str__(self):
        estado_beca = "Becado" if self.becado else "Sin Beca"
        return f"Nombre: {self.nombre:<20} AñoNac: {self.año_nac:<5} Sexo: {self.sexo:<8} Beca: {estado_beca}"

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []  

    def agregar_jugador(self, jugador):
        jugador.costo = self.costo if not jugador.becado else 0
        self.jugadores.append(jugador)

    def total_hombres(self):
        total = 0
        if self.jugadores[0].sexo == "Hombre": total += 1
        if self.jugadores[1].sexo == "Hombre": total += 1
        if self.jugadores[2].sexo == "Hombre": total += 1
        return total

    def total_mujeres(self):
        total = 0
        if self.jugadores[0].sexo == "Mujer": total += 1
        if self.jugadores[1].sexo == "Mujer": total += 1
        if self.jugadores[2].sexo == "Mujer": total += 1
        return total

    def subtotal_categoria(self):
        return sum(jugador.costo for jugador in self.jugadores)

    def __str__(self):
        jugadores_info = "\n".join(str(jugador) for jugador in self.jugadores)
        return (f"> {self.nombre} - {self.rango} - ({len(self.jugadores)})\n{jugadores_info}\n"
                f"- SubTotal : ${self.subtotal_categoria():,.2f}")

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def total_hombres(self):
        total = 0
        total += self.categorias[0].total_hombres()
        total += self.categorias[1].total_hombres()
        total += self.categorias[2].total_hombres()
        return total

    def total_mujeres(self):
        total = 0
        total += self.categorias[0].total_mujeres()
        total += self.categorias[1].total_mujeres()
        total += self.categorias[2].total_mujeres()
        return total

    def total_ingresos(self):
        total = 0
        total += self.categorias[0].subtotal_categoria()
        total += self.categorias[1].subtotal_categoria()
        total += self.categorias[2].subtotal_categoria()
        return total

    def __str__(self):
        categorias_info = "\n\n".join(str(categoria) for categoria in self.categorias)
        return (f"\nAcademia: {self.nombre}\nPropietario: {self.propietario}\nDomicilio: {self.domicilio}\n\n"
                f"Total de Categorias: {len(self.categorias)}\nTotal de Hombres: {self.total_hombres()}\n"
                f"Total de Mujeres: {self.total_mujeres()}\n\n>> Datos generales de las Categorías\n\n"
                f"{categorias_info}\n\n-> Total : ${self.total_ingresos():,.2f}")

# Datos de prueba
def main():
    academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")

    # Crear las categorías y agregar jugadores
    categoria1 = Categoria("Junior A", "2006/2007/2008", 1250)
    categoria1.agregar_jugador(Jugador("Alexander Lopez", 2006, "Hombre", False))
    categoria1.agregar_jugador(Jugador("Uriel Puga", 2007, "Hombre", True))
    categoria1.agregar_jugador(Jugador("Alejandra Escalona", 2008, "Mujer", False))

    categoria2 = Categoria("Junior B", "2009/2010/2011", 850)
    categoria2.agregar_jugador(Jugador("Armando Santana", 2009, "Hombre", False))
    categoria2.agregar_jugador(Jugador("Daniel Mijares", 2010, "Hombre", False))
    categoria2.agregar_jugador(Jugador("Antonio Hernandez", 2011, "Mujer", True))

    categoria3 = Categoria("Pony A", "2012/2013/2014", 700)
    categoria3.agregar_jugador(Jugador("Andrea Solis", 2012, "Mujer", True))
    categoria3.agregar_jugador(Jugador("Marissa Hernandez", 2013, "Mujer", True))
    categoria3.agregar_jugador(Jugador("Diana Soto", 2014, "Mujer", False))

    # Agregar categorías a la academia
    academia.agregar_categoria(categoria1)
    academia.agregar_categoria(categoria2)
    academia.agregar_categoria(categoria3)

    # Imprimir reporte final
    print("REPORTE DE LA ACADEMIA\n", academia)

if __name__ == "__main__":
    main()

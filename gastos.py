gastos = []


def pedir_monto():
    while True:
        texto = input("Monto: ")
        try:
            return float(texto)
        except ValueError:
            print("Eso no es un número. Intenta de nuevo.")


def agregar():
    descripcion = input("nombre del gasto: ").strip()
    if descripcion == "":
        print("nombre de el gasto no puede estar vacía.")
        return

    monto = pedir_monto()

    categoria = input("Categoría (ej: costo de vida, trabajo): ").strip().lower()
    if categoria == "":
        categoria = "otros"

    gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    gastos.append(gasto)
    print("Gasto agregado.")


def listar():
    if not gastos:
        print("No hay gastos todavía.")
        return

    for g in gastos:
        print(f"- {g['descripcion']}: {g['monto']} € [{g['categoria']}]")


def total():
    suma = sum(g["monto"] for g in gastos)
    print(f"Total: {suma} €")


def por_categoria():
    categorias = {g["categoria"] for g in gastos}
    if not categorias:
        print("No hay gastos todavía.")
        return

    for cat in sorted(categorias):
        subtotal = sum(g["monto"] for g in gastos if g["categoria"] == cat)
        print(f"- {cat}: {subtotal} €")


def grandes():
    caros = [g for g in gastos if g["monto"] > 100]
    if not caros:
        print("No hay gastos mayores a 100 €.")
        return

    for g in caros:
        print(f"- {g['descripcion']}: {g['monto']} €")


print("=== GESTOR DE GASTOS ===")
print("1  agregar gasto")
print("2  listar gastos")
print("3  ver total")
print("4  ver total por categoría")
print("5  gastos mayores a 100 €")
print("salir  terminar")

while True:
    opcion = input("\nOpción: ").strip().lower()

    if opcion == "salir":
        print("¡Hasta luego!")
        break
    elif opcion == "1":
        agregar()
    elif opcion == "2":
        listar()
    elif opcion == "3":
        total()
    elif opcion == "4":
        por_categoria()
    elif opcion == "5":
        grandes()
    else:
        print("Opción no válida. Mira el menú de arriba.")

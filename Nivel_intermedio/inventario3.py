class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_actual = 0
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor

    def actualizar_stock(self, cantidad):
        self.stock_actual += cantidad

    def calcular_ganancia_potencial(self):
        return (self.valor_venta - self.valor_compra) * self.stock_actual

def registrar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
    stock_maximo = int(input("Ingrese el stock máximo permitido: "))
    proveedor = input("Ingrese el nombre del proveedor del producto: ")
    return Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)

def visualizar_productos(productos):
    print("Lista de productos:")
    for producto in productos:
        print(f"Código: {producto.codigo}")
        print(f"Nombre: {producto.nombre}")
        print(f"Valor de compra: {producto.valor_compra}")
        print(f"Valor de venta: {producto.valor_venta}")
        print(f"Stock actual: {producto.stock_actual}")
        print(f"Stock mínimo: {producto.stock_minimo}")
        print(f"Stock máximo: {producto.stock_maximo}")
        print(f"Proveedor: {producto.proveedor}")
        print()

def actualizar_stock(productos, codigo_producto, cantidad):
    for producto in productos:
        if producto.codigo == codigo_producto:
            producto.actualizar_stock(cantidad)
            print("Stock actualizado correctamente.")
            return
    print("El producto no se encontró.")

def informe_productos_criticos(productos):
    productos_criticos = [producto for producto in productos if producto.stock_actual < producto.stock_minimo]
    if productos_criticos:
        print("Productos críticos:")
        for producto in productos_criticos:
            print(f"Nombre: {producto.nombre}")
            print(f"Stock actual: {producto.stock_actual}")
            print(f"Stock mínimo: {producto.stock_minimo}")
            print()
    else:
        print("No hay productos críticos en este momento.")

def calcular_ganancia_potencial_total(productos):
    ganancia_total = sum(producto.calcular_ganancia_potencial() for producto in productos)
    return ganancia_total

# Función principal del programa
def main():
    productos = []

    # Registro de productos
    print("Registro de productos:")
    while True:
        producto = registrar_producto()
        productos.append(producto)
        continuar = input("¿Desea registrar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break

    # Visualización de productos
    print("\nVisualización de productos:")
    visualizar_productos(productos)

    # Actualización de stock
    codigo_producto = input("Ingrese el código del producto a actualizar el stock: ")
    cantidad = int(input("Ingrese la cantidad a agregar o restar al stock: "))
    actualizar_stock(productos, codigo_producto, cantidad)

    # Informe de productos críticos
    print("\nInforme de productos críticos:")
    informe_productos_criticos(productos)

    # Cálculo de ganancia potencial total
    ganancia_total = calcular_ganancia_potencial_total(productos)
    print("\nLa ganancia potencial total es:", ganancia_total)

# Ejecución del programa
if __name__ == "__main__":
    main()

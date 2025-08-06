#Our first class ED-1
import java.util.ArrayList;
import java.util.Scanner;

class Venta {
    int id;
    String producto;
    int cantidad;
    double precioUnitario;

    public Venta(int id, String producto, int cantidad, double precioUnitario) {
        this.id = id;
        this.producto = producto;
        this.cantidad = cantidad;
        this.precioUnitario = precioUnitario;
    }

    public double calcularTotal() {
        return cantidad * precioUnitario;
    }

    public void mostrar() {
        System.out.println("ID: " + id + ", Producto: " + producto +
                           ", Cantidad: " + cantidad + ", Precio Unitario: " + precioUnitario +
                           ", Total: " + calcularTotal());
    }
}

public class SistemaVentas {
    public static void main(String[] args) {
        ArrayList<Venta> ventas = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- MENÚ DE VENTAS ---");
            System.out.println("1. Crear nueva venta");
            System.out.println("2. Listar ventas");
            System.out.println("3. Buscar por ID");
            System.out.println("4. Modificar venta");
            System.out.println("5. Eliminar venta");
            System.out.println("6. Calcular ingreso total");
            System.out.println("7. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("ID: ");
                    int id = sc.nextInt();
                    sc.nextLine(); // limpiar buffer
                    System.out.print("Producto: ");
                    String producto = sc.nextLine();
                    System.out.print("Cantidad: ");
                    int cantidad = sc.nextInt();
                    System.out.print("Precio unitario: ");
                    double precio = sc.nextDouble();
                    ventas.add(new Venta(id, producto, cantidad, precio));
                    System.out.println("Venta agregada correctamente.");
                    break;

                case 2:
                    if (ventas.isEmpty()) {
                        System.out.println("No hay ventas registradas.");
                    } else {
                        for (Venta v : ventas) {
                            v.mostrar();
                        }
                    }
                    break;

                case 3:
                    System.out.print("ID de la venta a buscar: ");
                    int buscarId = sc.nextInt();
                    boolean encontrado = false;
                    for (Venta v : ventas) {
                        if (v.id == buscarId) {
                            v.mostrar();
                            encontrado = true;
                            break;
                        }
                    }
                    if (!encontrado) {
                        System.out.println("Venta no encontrada.");
                    }
                    break;

                case 4:
                    System.out.print("ID de la venta a modificar: ");
                    int modificarId = sc.nextInt();
                    sc.nextLine();
                    for (Venta v : ventas) {
                        if (v.id == modificarId) {
                            System.out.print("Nuevo producto: ");
                            v.producto = sc.nextLine();
                            System.out.print("Nueva cantidad: ");
                            v.cantidad = sc.nextInt();
                            System.out.print("Nuevo precio unitario: ");
                            v.precioUnitario = sc.nextDouble();
                            System.out.println("Venta modificada correctamente.");
                            break;
                        }
                    }
                    break;

                case 5:
                    System.out.print("ID de la venta a eliminar: ");
                    int eliminarId = sc.nextInt();
                    ventas.removeIf(v -> v.id == eliminarId);
                    System.out.println("Venta eliminada si existía.");
                    break;

                case 6:
                    double totalIngresos = 0;
                    for (Venta v : ventas) {
                        totalIngresos += v.calcularTotal();
                    }
                    System.out.println("Ingreso total: $" + totalIngresos);
                    break;

                case 7:
                    System.out.println("Saliendo del sistema...");
                    break;

                default:
                    System.out.println("Opción inválida.");
            }
        } while (opcion != 7);

        sc.close();
    }
}

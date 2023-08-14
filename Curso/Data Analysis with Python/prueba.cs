
// Supongamos que deseo calcular el iva 


// incorrecto 
x = z * 1.12;

// correcto
calculoIVA = precioProducto * 1.12;


// Incorrecto 
void Saludo1(){
    Console.write("Saludo #1")
    Console.write("Hola")
    Console.write("Empecemos")
}
void Saludo2(){
    Console.write("Saludo #2")
    Console.write("Hola")
    Console.write("Empecemos")
}
void Saludo3(){
    Console.write("Saludo #3")
    Console.write("Hola")
    Console.write("Empecemos")
}


// Correcto
void Saludo1(){
    Console.write("Saludo #1")
    Util.Saludar();
}

void Saludo2(){
    Console.write("Saludo #2")
    Util.Saludar();

}

public class Util{
    public static void Saludar(){

        Console.write("Hola")
        Console.write("Empecemos")
    }
}


        // Correcto
        List<Persona> personas = new List<Persona>();

        
        personas.Add(new Persona { Nombre = "Luis", Edad = 26 });
        personas.Add(new Persona { Nombre = "Juan", Edad = 30 });
        personas.Add(new Persona { Nombre = "Jessica", Edad = 20 });

        // Acceder a los datos de la lista
        foreach (var persona in personas)
        {
            Console.WriteLine("Nombre: " + persona.Nombre + ", Edad: " + persona.Edad);
        }


// Incorrecto
        nombres[0] = "Luis";
        edades[0] = 25;

        nombres[1] = "Juan";
        edades[1] = 30;

        nombres[2] = "Jessica";
        edades[2] = 20;

        // Acceder a los datos en los arreglos
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine("Nombre: " + nombres[i] + ", Edad: " + edades[i]);
        }


// Incorrecto
 private static int contador = 0;

    public Empleado()
    {
        contador++;
    }

    public static int ObtenerCantidadEmpleados()
    {
        return contador;
    }

// Correcto
private static double pi = 3.14159;

    public static double CalcularAreaCirculo(double radio)
    {
        return pi * radio * radio;
    }

// Correcto
    public void Metodo1()
    {
        if (condicion)
        {
            // Código
        }
        else
        {
            // Código
        }
    }

    public void Metodo2()
    {
        foreach (var item in lista)
        {
            // Código
        }
    }

// Incorrecto
public class MiClase {
    public void Metodo1() {
        if (condicion) {
            // Código
        } else {
            // Código
        } }

    public void Metodo2() {
        foreach (var item in lista) {
            // Código
        } } }



    // Correcto 
    // Calcular el área de un círculo
    public double CalcularAreaCirculo(double radio)
    {
        double area = Math.PI * radio * radio;
        return area;
    }


    // Incorrecto
      // Declaración de variables
    double area;

    // Método para calcular el área de un círculo
    public double CalcularAreaCirculo(double radio)
    {
        // Multiplica el radio por sí mismo y luego por Pi
        area = Math.PI * radio * radio; // Fórmula del área de un círculo
        return area; // Devuelve el valor del área
    }
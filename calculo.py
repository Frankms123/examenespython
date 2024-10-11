import random
# this part get the number of employees and employees names and salary and returjn the employees and salary
def obtener_empleados():
    while True:
        try:
            num_empleados = int(input("Ingrese la cantidad de empleados: "))
            if num_empleados > 0 and num_empleados <= 5:
                break
            print("Por favor ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    empleados = []
    salarios_hora = []
    for i in range(num_empleados):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        while True:
            try:
                salario = float(input(f"Ingrese el salario por hora para {nombre}: "))
                if salario > 0:
                    break
                print("El salario debe ser mayor que 0.")
            except ValueError:
                print("Por favor ingrese un número válido.")
        empleados.append(nombre)
        salarios_hora.append(salario)
    return empleados, salarios_hora

# this part initialize the data cube with random numbers and determine the number of weeks in the month and return the number of weeks
def inicializar_cubo(cubo):
    semanas_en_mes = random.randint(4, 5)
    
    for empleado in range(5):
        for semana in range(5):
            for dia in range(5):
                if semana < semanas_en_mes:
                    cubo[empleado][semana][dia] = random.randint(1, 12)
                else:
                    cubo[empleado][semana][dia] = 0
    
    return semanas_en_mes
 
 # this part print the data cube in tabular format 
def imprimir_cubo(cubo, empleados, semanas_en_mes):
    dias = ["L", "M", "X", "J", "V"]
    
    print("\nRegistro de Horas Trabajadas")
    print("=" * 80)
    
    print("Datos", end="")
    for semana in range(semanas_en_mes):
        print(f"         Semana {semana + 1}", end="")
    print()
    
    print("      ", end="")
    for semana in range(semanas_en_mes):
        for dia in dias:
            print(f"{dia:>3}", end="")
        print("   ", end="")
    print()
    
    for idx_emp, empleado in enumerate(empleados):
        print(f"{empleado:<6}", end="")
        for semana in range(semanas_en_mes):
            for dia in range(5):
                horas = cubo[idx_emp][semana][dia]
                print(f"{horas:>3}", end="")
            print("   ", end="")
        print()

# this part calculate the nomina for all employees and print the result in tabular format
def calcular_nomina(cubo, empleados, salarios_hora, semanas_en_mes):
    print("\nNómina Mensual")
    print("=" * 80)
    print(f"{'Empleado':<15} | {'Horas Norm.':<12} | {'Horas Ext.':<12} | {'Salario Norm.':<15} | {'Salario Ext.':<15} | {'Total':<15}")
    print("-" * 80)
    
    for idx_emp, empleado in enumerate(empleados):
        horas_normales = 0
        horas_extras = 0
        
        for semana in range(semanas_en_mes):
            for dia in range(5):
                horas = cubo[idx_emp][semana][dia]
                if horas <= 8:
                    horas_normales += horas
                else:
                    horas_normales += 8
                    horas_extras += horas - 8
        
        pago_normal = horas_normales * salarios_hora[idx_emp]
        pago_extra = horas_extras * (salarios_hora[idx_emp] * 1.5)
        pago_total = pago_normal + pago_extra
        
        print(f"{empleado:<15} | {horas_normales:<12.1f} | {horas_extras:<12.1f} | {pago_normal:<14.2f} | {pago_extra:<14.2f} | {pago_total:<14.2f}")
    
    print("=" * 80)

#thsi part is the main function in the program to show the results of the calculations procedures
def main():
    print("Sistema de Registro de Horas y Cálculo de Nómina")
    print("====================================================")
    
    empleados, salarios_hora = obtener_empleados()
    
    cubo = [[[0 for dia in range(5)] for semana in range(5)] for empleado in range(5)]
    
    semanas_en_mes = inicializar_cubo(cubo)
    

    imprimir_cubo(cubo, empleados, semanas_en_mes)
    calcular_nomina(cubo, empleados, salarios_hora, semanas_en_mes)

if __name__ == "__main__":
    main()
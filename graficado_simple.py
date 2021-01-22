"""
Importamos

figure es el espacio que se despliega, la ventana
output_file = permite determinar el nombre del archivo que se creara 
show = servidor prende y muestra el HTML en el browser

COMANDOS INICIAR SISTEMA 
1. Estar dentro de la carpeta correcta
2. iniciamos ambiente virtual = " env\Scripts\activate.bat "
3. py graficado_simple.py

"""
#plotting = graficado
from bokeh.plotting import figure, output_file, show

#Entry point
if __name__ == '__main__':
    #Nombre
    output_file('graficado_simple.html')
    #Donde generamos los datos
    fig = figure()
    
    #input de enteros
    total_vals = int(input('Cuantos valores quieres graficar?'))
    #los x se guardan en una lista con el rango del total de ingresados
    x_vals = list(range(total_vals))
    
    y_vals = []

    #generar los valores de y
    for x in x_vals:
        val = int(input(f'Valor Y para {x}'))
        y_vals.append(val)

    #dado que es una linea, ambos arrays son iguales, width = grosor
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
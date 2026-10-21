"""
EJERCICIO 2: CALCULADORA DE SALARIO NETO 

o Definir el salario bruto anual de un empleado (ej. 28500.50) y la retención del IRPF (ej. 
15.5%). 

o Calcular la retención anual, el salario neto anual y la mensualidad en 12 pagas. Imprimir el 
resumen formateado tabularmente alineado a la derecha con dos decimales. 
"""

# Definiendo variables
salario_bruto_anual = 28500.50
IRPF = 15.5
retencion_irpf_anual = (IRPF/100) * salario_bruto_anual
salario_neto_anual = salario_bruto_anual - retencion_irpf_anual
salario_neto_mensual = salario_neto_anual / 12
## Calcular retención, salario neto y mensualidad 
print(f"Salario bruto anual: {salario_bruto_anual:.2f} €")
print(f"Retención IRPF: {retencion_irpf_anual:.2f} €")
print(f"Salario neto anual: {salario_neto_anual:.2f} €")
print(f"Salario neto mensual: {salario_neto_mensual:.2f} €")
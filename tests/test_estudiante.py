"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva, se_superponen, hay_conflicto


# Ejemplo de estructura, sin solución del caso:
# def test_nombre_del_comportamiento():
#     datos = [...]
#     antes = deepcopy(datos)
#     resultado = modificar_reserva(datos, ...)
#     assert resultado == "..."
#     assert datos == antes  # Cuando la operación debe conservar TODO.
def test_intervalos_overlap():
    resultado = se_superponen(540,600,600,660)
    assert resultado is False

def test_reserva_mismo_intervalo():
    reservas = [(1,540,600),(2,540,600)]
    modificar_reserva(reservas,0,0,0)
    assert id(reservas[0]) != id(reservas[1])

def test_modificar_reserva_outoftime():
    reservas = [(1,540,600)]
    modificar_reserva(reservas,1,500,600)
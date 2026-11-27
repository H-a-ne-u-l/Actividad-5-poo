from enumerados import TipoCargo, TipoGenero

class Empleado:
    def __init__(self, nombre: str, apellidos: str, cargo: TipoCargo, genero: TipoGenero,
                 salario_dia: float, dias_trabajados: int, otros_ingresos: float,
                 pagos_salud: float, aporte_pensiones: float):
        """Constructor que inicializa los atributos de un empleado."""
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__cargo = cargo
        self.__genero = genero
        self.__salario_dia = salario_dia
        self.__dias_trabajados = dias_trabajados
        self.__otros_ingresos = otros_ingresos
        self.__pagos_salud = pagos_salud
        self.__aporte_pensiones = aporte_pensiones

    def get_nombre(self) -> str:
        return self.__nombre

    def get_apellidos(self) -> str:
        return self.__apellidos

    def get_cargo(self) -> TipoCargo:
        return self.__cargo

    def get_genero(self) -> TipoGenero:
        return self.__genero

    def get_salario_dia(self) -> float:
        return self.__salario_dia

    def get_dias_trabajados(self) -> int:
        return self.__dias_trabajados

    def get_otros_ingresos(self) -> float:
        return self.__otros_ingresos

    def get_pagos_salud(self) -> float:
        return self.__pagos_salud

    def get_aporte_pensiones(self) -> float:
        return self.__aporte_pensiones

    def calcular_nomina(self) -> float:
        """Calcula el salario mensual neto del empleado."""
        return ((self.__salario_dia * self.__dias_trabajados) + self.__otros_ingresos
                - self.__pagos_salud - self.__aporte_pensiones)

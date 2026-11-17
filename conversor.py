"""Funcoes simples para conversao de temperatura."""


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return celsius * 9 / 5 + 32

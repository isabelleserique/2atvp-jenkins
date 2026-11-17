"""Versao que compila, mas possui um erro logico proposital."""


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_para_fahrenheit(celsius: float) -> float:
    # Erro proposital: 5/9 deveria ser 9/5.
    return celsius * 5 / 9 + 32

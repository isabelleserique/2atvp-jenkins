"""Versao propositalmente invalida para demonstrar falha no build."""


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def celsius_para_fahrenheit(celsius: float) -> float
    #SyntaxError.
    return celsius * 9 / 5 + 32

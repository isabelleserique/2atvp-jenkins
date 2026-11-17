"""Testes automatizados do conversor de temperaturas."""

import pytest

from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius


def test_fahrenheit_para_celsius_no_ponto_de_congelamento() -> None:
    assert fahrenheit_para_celsius(32) == pytest.approx(0)


def test_fahrenheit_para_celsius_no_ponto_de_ebulicao() -> None:
    assert fahrenheit_para_celsius(212) == pytest.approx(100)


def test_fahrenheit_para_celsius_com_valor_negativo() -> None:
    assert fahrenheit_para_celsius(-40) == pytest.approx(-40)


def test_celsius_para_fahrenheit_no_ponto_de_congelamento() -> None:
    assert celsius_para_fahrenheit(0) == pytest.approx(32)


def test_celsius_para_fahrenheit_no_ponto_de_ebulicao() -> None:
    assert celsius_para_fahrenheit(100) == pytest.approx(212)


def test_celsius_para_fahrenheit_com_valor_negativo() -> None:
    assert celsius_para_fahrenheit(-40) == pytest.approx(-40)

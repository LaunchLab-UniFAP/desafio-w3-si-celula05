"""Testes do relatorio de rastreabilidade."""

import argparse
import unittest
from datetime import date

from src.rastreabilidade_si import Commit, gerar_relatorio, periodo_da_semana, validar_data


def criar_commit(hash_git: str, autor: str, email: str) -> Commit:
    return Commit(hash_git, autor, email, "2026-09-17T10:00:00-03:00", "feat: teste")


class PeriodoDaSemanaTest(unittest.TestCase):
    def test_retorna_segunda_e_domingo(self) -> None:
        self.assertEqual(
            periodo_da_semana(date(2026, 9, 17)),
            (date(2026, 9, 14), date(2026, 9, 20)),
        )

    def test_valida_data_iso(self) -> None:
        self.assertEqual(validar_data("2026-09-17"), date(2026, 9, 17))
        with self.assertRaises(argparse.ArgumentTypeError):
            validar_data("17/09/2026")


class GerarRelatorioTest(unittest.TestCase):
    inicio = date(2026, 9, 14)
    fim = date(2026, 9, 20)

    def test_sem_commits_e_inconclusivo(self) -> None:
        relatorio = gerar_relatorio([], self.inicio, self.fim, tolerancia=1)
        criterio = relatorio["criterio_isonomia"]
        self.assertEqual(criterio["status"], "INCONCLUSIVA")
        self.assertFalse(criterio["isonomia_validada"])

    def test_distribuicao_equilibrada(self) -> None:
        commits = [
            criar_commit("a" * 40, "Ana", "ANA@example.com"),
            criar_commit("b" * 40, "Beto", "beto@example.com"),
        ]
        relatorio = gerar_relatorio(commits, self.inicio, self.fim, tolerancia=0)
        criterio = relatorio["criterio_isonomia"]
        self.assertEqual(criterio["status"], "EQUILIBRADA")
        self.assertTrue(criterio["isonomia_validada"])

    def test_distribuicao_desequilibrada(self) -> None:
        commits = [
            criar_commit("a" * 40, "Ana", "ana@example.com"),
            criar_commit("b" * 40, "Ana", "ANA@example.com"),
            criar_commit("c" * 40, "Beto", "beto@example.com"),
        ]
        relatorio = gerar_relatorio(commits, self.inicio, self.fim, tolerancia=0)
        criterio = relatorio["criterio_isonomia"]
        self.assertEqual(criterio["status"], "DESEQUILIBRADA")
        self.assertEqual(criterio["diferenca_encontrada"], 1)


if __name__ == "__main__":
    unittest.main()

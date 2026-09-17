"""Testes da projecao epidemiologica."""

import math
import unittest

from src.endemia import calcular_projecao_focos


class CalcularProjecaoFocosTest(unittest.TestCase):
    def test_calcula_um_ciclo_pelo_modelo_multiplicativo(self) -> None:
        self.assertEqual(calcular_projecao_focos(10, 1.5), 15.0)

    def test_aceita_zero(self) -> None:
        self.assertEqual(calcular_projecao_focos(0, 1.5), 0.0)
        self.assertEqual(calcular_projecao_focos(10, 0), 0.0)

    def test_rejeita_valores_negativos(self) -> None:
        with self.assertRaisesRegex(ValueError, "focos_atuais"):
            calcular_projecao_focos(-1, 1.5)
        with self.assertRaisesRegex(ValueError, "taxa_reproducao"):
            calcular_projecao_focos(10, -0.1)

    def test_rejeita_valores_nao_numericos_e_booleanos(self) -> None:
        for valor in ("10", None, True):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    calcular_projecao_focos(valor, 1.5)  # type: ignore[arg-type]

    def test_rejeita_valores_nao_finitos(self) -> None:
        for valor in (math.inf, -math.inf, math.nan):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    calcular_projecao_focos(10, valor)


if __name__ == "__main__":
    unittest.main()

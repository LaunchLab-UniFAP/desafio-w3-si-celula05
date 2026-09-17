"""Testes do manifesto de governanca de dados."""

import json
import unittest
from pathlib import Path


class GovernancaDadosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        caminho = Path(__file__).resolve().parents[1] / "docs" / "governanca_dados.json"
        cls.manifesto = json.loads(caminho.read_text(encoding="utf-8"))

    def test_declara_licenca_mit(self) -> None:
        self.assertEqual(self.manifesto["licenca_distribuicao"], "MIT")
        self.assertEqual(
            self.manifesto["detalhes_licenca_open_source"]["identificador_spdx"],
            "MIT",
        )

    def test_proibe_dados_identificaveis_de_pacientes(self) -> None:
        compliance = self.manifesto["compliance_lgpd"]
        self.assertTrue(compliance["anonimizacao_obrigatoria"])
        self.assertFalse(compliance["dados_identificaveis_de_pacientes_permitidos"])

    def test_declara_regras_minimas_do_git(self) -> None:
        regras = self.manifesto["regras_git"]
        self.assertTrue(regras["bloquear_push_main_direto"])
        self.assertTrue(regras["exigir_conventional_commits"])
        self.assertTrue(regras["exigir_revisao_por_pull_request"])


if __name__ == "__main__":
    unittest.main()

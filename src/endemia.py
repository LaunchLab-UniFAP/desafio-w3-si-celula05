"""Projecao de focos epidemiologicos para o ciclo seguinte."""

from __future__ import annotations

import math
from numbers import Real


def _validar_valor(nome: str, valor: Real) -> float:
    """Valida e normaliza uma entrada numerica nao negativa e finita."""

    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise TypeError(f"{nome} deve ser um numero real.")

    valor_normalizado = float(valor)
    if not math.isfinite(valor_normalizado):
        raise ValueError(f"{nome} deve ser finito.")
    if valor_normalizado < 0:
        raise ValueError(f"{nome} nao pode ser negativo.")
    return valor_normalizado


def calcular_projecao_focos(focos_atuais: Real, taxa_reproducao: Real) -> float:
    """Projeta os focos para um ciclo pelo modelo multiplicativo.

    A taxa representa o fator de reproducao de um unico ciclo. Por exemplo,
    uma taxa de ``1.5`` aplicada a 10 focos resulta em 15 focos projetados.
    """

    focos = _validar_valor("focos_atuais", focos_atuais)
    taxa = _validar_valor("taxa_reproducao", taxa_reproducao)
    return focos * taxa


def main() -> None:
    """Executa um exemplo simples da projecao."""

    print("--- MONITORAMENTO DE ENDEMIAS UniFAP ---")
    print(f"Total Projetado: {calcular_projecao_focos(10, 1.5):g}")


if __name__ == "__main__":
    main()

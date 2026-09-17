"""Audita os commits da semana e indica a distribuição entre colaboradores."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path


HASH_GIT = re.compile(r"^[0-9a-f]{40}$")


@dataclass(frozen=True)
class Commit:
    """Representa uma evidência rastreável do histórico Git."""

    hash: str
    autor: str
    email: str
    data: str
    mensagem: str


def periodo_da_semana(referencia: date | None = None) -> tuple[date, date]:
    """Retorna a segunda-feira e o domingo da semana de referência."""

    referencia = referencia or date.today()
    inicio = referencia - timedelta(days=referencia.weekday())
    fim = inicio + timedelta(days=6)
    return inicio, fim


def validar_data(valor: str) -> date:
    """Converte uma data ISO informada pela linha de comando."""

    try:
        return date.fromisoformat(valor)
    except ValueError as erro:
        raise argparse.ArgumentTypeError(
            f"Data inválida: {valor}. Use o formato AAAA-MM-DD."
        ) from erro


def coletar_commits(repositorio: Path, inicio: date, fim: date) -> list[Commit]:
    """Coleta commits não relacionados a merge em todas as branches locais."""

    formato = "%H%x1f%an%x1f%ae%x1f%aI%x1f%s%x1e"
    comando = [
        "git",
        "-C",
        str(repositorio),
        "log",
        "--all",
        "--no-merges",
        f"--since={inicio.isoformat()} 00:00:00",
        f"--until={fim.isoformat()} 23:59:59",
        f"--pretty=format:{formato}",
    ]

    try:
        resultado = subprocess.run(
            comando,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError as erro:
        raise RuntimeError("O executável git não foi encontrado no sistema.") from erro
    except subprocess.CalledProcessError as erro:
        detalhe = erro.stderr.strip() or "Falha desconhecida ao consultar o Git."
        raise RuntimeError(detalhe) from erro

    commits: list[Commit] = []
    for registro in resultado.stdout.split("\x1e"):
        campos = registro.strip().split("\x1f")
        if campos == [""]:
            continue
        if len(campos) != 5 or not HASH_GIT.fullmatch(campos[0]):
            raise RuntimeError("O Git retornou um registro de commit inválido.")
        commits.append(Commit(*campos))

    return commits


def gerar_relatorio(
    commits: list[Commit], inicio: date, fim: date, tolerancia: int
) -> dict[str, object]:
    """Gera um relatório e avalia a isonomia pela quantidade de commits."""

    contagem = Counter(commit.email.lower() for commit in commits)
    nomes = {commit.email.lower(): commit.autor for commit in commits}
    total = len(commits)

    contribuidores = [
        {
            "autor": nomes[email],
            "email": email,
            "quantidade_commits": quantidade,
            "percentual": round((quantidade / total) * 100, 2) if total else 0.0,
        }
        for email, quantidade in sorted(
            contagem.items(), key=lambda item: (-item[1], item[0])
        )
    ]

    if len(contagem) < 2:
        status = "INCONCLUSIVA"
        isonomia_validada = False
        diferenca = total
    else:
        quantidades = list(contagem.values())
        diferenca = max(quantidades) - min(quantidades)
        isonomia_validada = diferenca <= tolerancia
        status = "EQUILIBRADA" if isonomia_validada else "DESEQUILIBRADA"

    return {
        "periodo": {"inicio": inicio.isoformat(), "fim": fim.isoformat()},
        "total_commits": total,
        "total_contribuidores": len(contagem),
        "criterio_isonomia": {
            "metrica": "Diferenca entre as quantidades de commits por autor",
            "tolerancia_maxima": tolerancia,
            "diferenca_encontrada": diferenca,
            "status": status,
            "isonomia_validada": isonomia_validada,
            "observacao": (
                "A contagem de commits é um indicador quantitativo e deve ser "
                "analisada junto ao conteúdo das contribuições."
            ),
        },
        "contribuidores": contribuidores,
        "commits": [asdict(commit) for commit in commits],
    }


def exibir_relatorio(relatorio: dict[str, object]) -> None:
    """Exibe no terminal os principais dados da auditoria."""

    periodo = relatorio["periodo"]
    criterio = relatorio["criterio_isonomia"]
    print("=== RELATÓRIO DE RASTREABILIDADE ===")
    print(f"Período: {periodo['inicio']} a {periodo['fim']}")
    print(f"Commits auditados: {relatorio['total_commits']}")
    print(f"Contribuidores: {relatorio['total_contribuidores']}")

    for colaborador in relatorio["contribuidores"]:
        print(
            f"- {colaborador['autor']} <{colaborador['email']}>: "
            f"{colaborador['quantidade_commits']} commit(s) "
            f"({colaborador['percentual']}%)"
        )

    print(f"Status da distribuição: {criterio['status']}")
    print(criterio["observacao"])
    print("\nEvidências:")
    for commit in relatorio["commits"]:
        print(
            f"- {commit['hash']} | {commit['data']} | "
            f"{commit['autor']} | {commit['mensagem']}"
        )


def criar_parser() -> argparse.ArgumentParser:
    """Configura os argumentos aceitos pelo script."""

    inicio_padrao, fim_padrao = periodo_da_semana()
    parser = argparse.ArgumentParser(
        description="Audita os hashes e a distribuição dos commits da semana."
    )
    parser.add_argument("--desde", type=validar_data, default=inicio_padrao)
    parser.add_argument("--ate", type=validar_data, default=fim_padrao)
    parser.add_argument(
        "--repositorio",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--tolerancia",
        type=int,
        default=1,
        help="Diferença máxima de commits aceita entre os autores (padrão: 1).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Exibe o relatório completo em JSON.",
    )
    parser.add_argument(
        "--falhar-sem-isonomia",
        action="store_true",
        help="Retorna código 1 quando a distribuição não estiver equilibrada.",
    )
    return parser


def main() -> int:
    """Executa a auditoria solicitada pela linha de comando."""

    argumentos = criar_parser().parse_args()
    if argumentos.desde > argumentos.ate:
        raise SystemExit("A data inicial não pode ser posterior à data final.")
    if argumentos.tolerancia < 0:
        raise SystemExit("A tolerância não pode ser negativa.")

    try:
        commits = coletar_commits(
            argumentos.repositorio.resolve(), argumentos.desde, argumentos.ate
        )
    except RuntimeError as erro:
        raise SystemExit(f"Erro ao auditar o repositório: {erro}") from erro

    relatorio = gerar_relatorio(
        commits, argumentos.desde, argumentos.ate, argumentos.tolerancia
    )

    if argumentos.json:
        print(json.dumps(relatorio, ensure_ascii=False, indent=2))
    else:
        exibir_relatorio(relatorio)

    if argumentos.falhar_sem_isonomia:
        criterio = relatorio["criterio_isonomia"]
        return 0 if criterio["isonomia_validada"] else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

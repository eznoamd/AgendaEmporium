"""
CLI unificado para migração e seed do banco.

Uso básico:
    python artisan.py migrate   # roda apenas a migração principal
    python artisan.py seed      # roda apenas o seed (population)
    python artisan.py all       # roda migração e depois seed
"""

import argparse
import sys
from pathlib import Path

from work.migrate import SQLiteMigrator
from work.population import main as run_population
from utils.path import get_database_path, get_sql_path

def _print_header() -> None:
    print("=" * 60)
    print(" Artisan - Migração e Seed do Banco ")
    print("=" * 60)


def run_migrate(db_file: Path, sql_file: Path) -> None:
    print("[artisan] Iniciando migração do banco...")
    migrator = SQLiteMigrator(db_file)
    migrator.run_script(sql_file)
    print("[artisan] Migração concluída com sucesso.\n")


def run_seed() -> None:
    print("[artisan] Iniciando seed (população do banco)...")
    original_argv = sys.argv
    sys.argv = ["population.py"]
    try:
        run_population()
        print("[artisan] Seed executado com sucesso.\n")
    finally:
        sys.argv = original_argv


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CLI unificado para migração e população do banco de dados"
    )

    subparsers = parser.add_subparsers(
        title="comandos disponíveis",
        dest="command",
        required=True
    )

    # --- migrate ---
    migrate_parser = subparsers.add_parser(
        "migrate",
        help="Efetua a migração do banco com base na pasta sql"
    )

    # --- seed ---
    seed_parser = subparsers.add_parser(
        "seed",
        help="Efetua a população do banco já existente"
    )

    # --- all ---
    all_parser = subparsers.add_parser(
        "all",
        help="Executa a migração e população do banco"
    )

    args = parser.parse_args()

    _print_header()

    db_file = get_database_path()
    sql_file = get_sql_path()

    try:
        if args.command == "migrate":
            run_migrate(db_file, sql_file)

        elif args.command == "seed":
            run_seed()

        elif args.command == "all":
            run_migrate(db_file, sql_file)
            run_seed()

    except Exception as exc:
        print(f"[artisan] Erro ao executar comando '{args.command}': {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()

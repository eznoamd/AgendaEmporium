import sqlite3
import argparse
from pathlib import Path


class SQLiteMigrator:
    """
    Responsável por executar scripts SQL em um banco SQLite.
    """

    def __init__(self, db_file: Path):
        self.db_file = db_file

    def run_script(self, sql_file: Path):
        if not sql_file.exists():
            raise FileNotFoundError(f"Arquivo SQL não encontrado: {sql_file}")

        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                sql_script = sql_file.read_text(encoding="utf-8")
                cursor.executescript(sql_script)

            print(f"✔ Banco '{self.db_file}' migrado com sucesso usando '{sql_file}'")

        except sqlite3.Error as e:
            raise RuntimeError(f"Erro no SQLite: {e}") from e


class MigrationCLI:
    """
    Interface de linha de comando para migrações SQLite.
    """

    DEFAULT_DB_NAME = "../data/database/database.db"

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Script de migração SQLite"
        )
        self._configure_arguments()

    def _configure_arguments(self):
        self.parser.add_argument(
            "script",
            help="Nome do script SQL (sem extensão ou com .sql)"
        )

        self.parser.add_argument(
            "--db",
            default=self.DEFAULT_DB_NAME,
            help=f"Arquivo do banco de dados (padrão: {self.DEFAULT_DB_NAME})"
        )

    def parse(self):
        args = self.parser.parse_args()

        sql_file = Path(args.script)
        if sql_file.suffix != ".sql":
            sql_file = sql_file.with_suffix(".sql")

        db_file = Path(args.db)

        return sql_file, db_file


def main():
    cli = MigrationCLI()
    sql_file, db_file = cli.parse()

    migrator = SQLiteMigrator(db_file)
    migrator.run_script(sql_file)


if __name__ == "__main__":
    main()

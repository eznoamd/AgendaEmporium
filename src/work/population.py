import argparse
import sqlite3
from work.seed.initial_seeder import InitialDataSeeder
from utils.path import get_database_path


def main():

    parser = argparse.ArgumentParser(description="Seed do banco de dados")
    parser.add_argument("--only", help="Rodar apenas um seed específico")
    parser.add_argument("--reset", action="store_true", help="Resetar seed antes de aplicar")

    args = parser.parse_args()

    conn = sqlite3.connect(get_database_path())

    try:
        with conn:
            seeders = [
                InitialDataSeeder(conn),
            ]

            for seeder in seeders:
                if args.only and seeder.name != args.only:
                    continue

                if args.reset:
                    seeder.reset()

                seeder.run()

    except Exception as exc:
        print("Erro ao rodar seed: %s", exc)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

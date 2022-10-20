from functools import lru_cache
import csv

@lru_cache
def read(path):
    try:
        with open(path, encoding="utf-8") as file:
            jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

            return [job for job in jobs_reader]


    except FileNotFoundError as exc:
        print("Arquivo não encontrado")
    
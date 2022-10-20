from functools import lru_cache
import csv

@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """


    try:
        with open(path, encoding="utf-8") as file:
            jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

            jobs = [job for job in jobs_reader]

            return jobs


    except FileNotFoundError as exc:
        print("Arquivo não encontrado")
    
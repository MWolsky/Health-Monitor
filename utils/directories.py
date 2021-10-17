from pathlib import Path
import os

def project_root() -> Path:
    return Path(os.getcwd())

def join_dir(dir: str) -> Path:
    return project_root().joinpath(dir)

def sqlite_dir() -> Path:
    sqlite_dir = 'sqlite'
    return join_dir(sqlite_dir)

def utils_dir() -> Path:
    utils_dir = 'utils'
    return join_dir(utils_dir)

def sqlqueries_dir() -> Path:
    queries_dir = 'sql_queries'
    return join_dir(queries_dir)

def sqlcommands_dir() -> Path:
    commands_dir = 'sql_commands'
    return sqlite_dir().joinpath(commands_dir)


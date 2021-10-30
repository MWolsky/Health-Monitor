from pathlib import Path


def project_root() -> Path:
    return Path(__file__).parent.parent.parent


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


def dir_test() -> Path:
    tests_dir = 'tests'
    return project_root().joinpath(tests_dir)


def resources_tests_dir() -> Path:
    resources_dir = 'resources'
    return dir_test().joinpath(resources_dir)

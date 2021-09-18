import utils.directories as hlp


def open_sql_file(filename: str):
    fullname = filename + '.sql'
    with open (hlp.sqlqueries_dir().joinpath(fullname)) as file:
        f = file.read()
        return f

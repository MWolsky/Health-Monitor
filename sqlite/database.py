import sqlite3 as sql3

class SqliteDataBase:
    def __init__(self, name: str) -> None:
        self.con = sql3.connect(f'{name}.db')
        self.cur = self.cursor()

    def cursor(self) -> sql3.Cursor:
        """ Creates Cursor required to execute SQL statements

        Returns:
            sql3.Cursor: database Cursor object
        """
        return self.con.cursor()

    def close_connection(self) -> None:
        """ Closes database connection
        """
        self.con.close()

    def commit_changes(self) -> None:
        """ Commits (saves) changes to database
        """
        self.con.commit()

    def execute(self, statement: str, named_params: dict = None) -> None:
        """Executes given SQL statement

        Args:
            statement (str): SQL statement provided in text
        """
        if named_params:
            self.cur.execute(statement, named_params)
        else:
            self.cur.execute(statement) 

    def execute_many(self, statement: str, parameters: list) -> None:
        """ Executes given parametrized SQL statement with parameters list

        Args:
            statement (str): SQL statement provided in text
            parameters (list): Parameters list to be passed in given order
        """
        self.cur.executemany(statement, parameters)

    def execute_batch(self, statements: str) -> None:
        """ Executes batch of SQL statements

        Args:
            statements (str): SQL statement provided in text
        """
        self.cur.executescript(statements)


class HealthMonitorSQLiteDB(SqliteDataBase):
    super().__init__(name='HealthMonitor')

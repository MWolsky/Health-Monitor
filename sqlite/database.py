import sqlite3 as sql3
from typing import List, Union, Dict, Tuple
from core.utils.helpers import open_sql_file
from logging import getLogger
logger = getLogger(__name__)


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

    def execute(self, statement: str, parameters: Union[List, Dict] = None) -> None:
        """Executes given SQL statement

        Args:
            statement (str): SQL statement provided in text
        """
        if parameters:
            self.cur.execute(statement, parameters)
        else:
            self.cur.execute(statement) 

    def execute_many(self, statement: str, parameters: List[Union[Tuple, Dict]]) -> None:
        """ Executes given parametrized SQL statement with parameters list

        Args:
            statement (str): SQL statement provided in text
            parameters (list): Parameters list to be passed in given order or dictionary with named parameters
        """
        self.cur.executemany(statement, parameters)

    def execute_batch(self, statements: str) -> None:
        """ Executes batch of SQL statements

        Args:
            statements (str): SQL statement provided in text
        """
        self.cur.executescript(statements)

    def list_tables(self) -> List:
        """Lists all existing tables in DB"""
        self.execute("SELECT * FROM sqlite_master WHERE type='table';")
        return self.cur.fetchall()

    def list_indexes(self) -> List:
        """Lists all existing indexes in DB"""
        self.execute("SELECT * FROM sqlite_master WHERE type='index';")
        return self.cur.fetchall()

    def drop_table(self, tablename: str):
        """Drops given table"""
        self.execute(f"DROP TABLE {tablename}")

    def drop_all_table(self):
        tables = self.list_tables()
        logger.info(f'Existing tables: {[i[1] for i in tables]}')
        for i in tables:
            logger.info(f'Dropping: {i[1]} table')
            self.drop_table(i[1])




class HealthMonitorSQLiteDB(SqliteDataBase):
    def __init__(self) -> None:
        super().__init__('HealthMonitor')
        self.con.execute('PRAGMA foreign_keys = 1')

    def create_tables(self) -> None:
        """Executes batch sql file to create all tables 
        """
        sql_statement = open_sql_file('create_tables')
        logger.info(f'Executing: {sql_statement}')
        self.execute_batch(sql_statement)

    def create_indexes(self):
        """Executes batch statement to create indexes on existing tables"""
        sql_statement = open_sql_file('create_indexes')
        logger.info(f"Executing: {sql_statement}")
        self.execute_batch(sql_statement)

from sqlite.database import HealthMonitorSQLiteDB

if __name__ == "__main__":
    db = HealthMonitorSQLiteDB()
    db.create_tables()
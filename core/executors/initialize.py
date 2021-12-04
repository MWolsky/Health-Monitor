from config.constants import project_start
from core.executors.create_data_model_tables import strava_tables, my_fitness_pal_tables_since, date_table
from sqlite.database import HealthMonitorSQLiteDB


def main():
    print('querying dates')
    table_dates = date_table()
    print('querying strava')
    tables_strava = strava_tables()
    cardio_table = tables_strava['cardio']
    weights_table = tables_strava['weights']
    laps_table = tables_strava['laps']
    print('querying mfp')
    tables_mfp = my_fitness_pal_tables_since(project_start)
    calories = tables_mfp['calories']
    meals = tables_mfp['meals']
    print('creating_tables')
    hm_db = HealthMonitorSQLiteDB()
    hm_db.create_tables()

    hm_db.insert_pandas('date_table', table_dates)
    hm_db.insert_pandas('cardio', cardio_table)
    hm_db.insert_pandas('laps', laps_table)
    hm_db.insert_pandas('weights', weights_table)
    hm_db.insert_pandas('calories', calories)
    hm_db.insert_pandas('meals_daily', meals)
    print('querying MY TABLES:')
    m_dates = hm_db.select_all('date_table')
    print(f'Shape of date_tables: {m_dates.shape}')
    m_cardio = hm_db.select_all('cardio')
    print(f'Shape of cardio: {m_cardio.shape}')
    m_laps = hm_db.select_all('laps')
    print(f'Shape of laps: {m_laps.shape}')
    m_weights = hm_db.select_all('weights')
    print(f'Shape of weights: {m_weights.shape}')
    m_calories = hm_db.select_all('calories')
    print(f'Shape of calories: {m_calories.shape}')
    m_meals = hm_db.select_all('meals_daily')
    print(f'Shape of m_meals: {m_meals.shape}')


if __name__ == "__main__":
    main()

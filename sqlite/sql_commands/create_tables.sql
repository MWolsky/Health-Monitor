CREATE TABLE cardio (
    [activity_id] INT PRIMARY KEY,
    [date] DATE NOT NULL,
    [activity_start_time] NVARCHAR(255),
    [name] NVARCHAR(255),
    [type] NVARCHAR(255) NOT NULL,
    [average_cadence] real,
    [average_heartrate] real,
    [average_speed] real,
    [distance] real,
    [elapsed_time] INT,
    [max_speed] real,
    [max_heartrate] real,
    [moving_time] INT,
    [total_elevation_gain] INT,
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE laps (
    [lap_id] INT PRIMARY KEY,
    [activity_id] INT,
    [name] NVARCHAR(255),
    [average_cadence] real,
    [average_heartrate] real,
    [average_speed] real,
    [distance] real,
    [elapsed_time] INT,
    [lap_index] INT,
    [max_speed] real,
    [max_heartrate] real,
    [moving_time] INT,
    [split] INT,
    [total_elevation_gain] INT,
    [pace] real,
    [difficulty_index] real,
    FOREIGN KEY ([activity_id]) REFERENCES cardio([activity_id])
);

CREATE TABLE weights (
    [activity_id] INT PRIMARY KEY,
    [date] DATE NOT NULL,
    [activity_start_time] NVARCHAR(255),
    [type] NVARCHAR(255) NOT NULL,
    [name] NVARCHAR(255),
    [average_heartrate] real,
    [distance] real,
    [elapsed_time] INT,
    [max_heartrate] real,
    [moving_time] INT,
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE calories (
    [date] DATE PRIMARY KEY,
    [goal_calories] INT,
    [goal_carbohydrates] INT,
    [goal_fat] INT,
    [goal_protein] INT,
    [goal_sodium] INT,
    [goal_sugar] INT,
    [total_calories] INT,
    [total_carbohydrates] INT,
    [total_fat] INT,
    [total_protein] INT,
    [total_sodium] INT,
    [total_sugar] INT,
    [calories_net] INT,
    [carbohydrates_net] INT,
    [fat_net] INT,
    [protein_net] INT,
    [sodium_net] INT,
    [sugar_net] INT,
    [complete_day] INT,
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE meals_daily (
    [date]  DATE NOT NULL,
    [meal_type]  NVARCHAR(255) NOT NULL,
    [food_name]  NVARCHAR(255) NOT NULL,
    [total_calories] real,
    [total_carbohydrates]    real,
    [total_fat]    real,
    [total_protein]    real,
    [total_sodium]  real,
    [total_sugar]    real,
    [quantity] real,
    [unit] NVARCHAR(255)
);

CREATE TABLE supplements (
    [date] DATE NOT NULL,
    [supplement] NVARCHAR(255) NOT NULL,
    [amount] INT NOT NULL,
    PRIMARY KEY ([date], [supplement])
);

CREATE TABLE date_table (
    [date] DATE PRIMARY KEY,
    [year] INT,
    [month] INT,
    [day] INT
);


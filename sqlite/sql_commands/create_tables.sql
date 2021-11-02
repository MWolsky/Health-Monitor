CREATE TABLE IF NOT EXISTS cardio (
    [training_id] INT PRIMARY KEY,
    [date] DATE NOT NULL,
    [name] NVARCHAR(255),
    [type] NVARCHAR(255) NOT NULL,
    [average_cadence] real,
    [average_heartrate] real,
    [average_speed] real,
    [distance] real,
    [elapsed_time] INT,
    [max_speed] real,
    [max_heartrate] real
    [moving_time] INT,
    [total_elevation_gain] INT,
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE IF NOT EXISTS laps (
    [lap_id] INT PRIMARY KEY,
    [training_id] INT,
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
    FOREIGN KEY ([training_id]) REFERENCES cardio([training_id])
);

CREATE TABLE IF NOT EXISTS weights (
    [training_id] INT PRIMARY KEY,
    [date] DATE NOT NULL,
    [type] NVARCHAR(255) NOT NULL,
    [name] NVARCHAR(255),
    [average_heartrate] real,
    [distance] real,
    [elapsed_time] INT,
    [max_heartrate] real,
    [moving_time] INT,
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE IF NOT EXISTS calories (
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
    FOREIGN KEY ([date]) REFERENCES date_table([date])
);

CREATE TABLE IF NOT EXISTS supplements (
    [date] DATE NOT NULL,
    [supplement] NVARCHAR(255) NOT NULL,
    [amount] INT NOT NULL,
    PRIMARY KEY ([date], [supplement])
);

CREATE TABLE IF NOT EXISTS date_table (
    [date] DATE PRIMARY KEY,
    [year] INT,
    [month] INT,
    [day] INT
);


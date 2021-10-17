CREATE TABLE IF NOT EXISTS plan_cardio (
    [training_id] TEXT PRIMARY KEY,
    [date] TEXT NOT NULL,
    [type] TEXT NOT NULL,
    [sub_type] TEXT,
    [description] TEXT,
    [aim] TEXT
    [distance] INTEGER,
    [tempo] TEXT,
    [heart_rate] INTEGER
);

CREATE TABLE IF NOT EXISTS plan_weights (
    [training_id] TEXT PRIMARY KEY,
    [date] TEXT NOT NULL,
    [type] TEXT NOT NULL,
    [sub_type] TEXT,
    [description] TEXT,
    [aim] TEXT,
    [excercise] TEXT,
    [series] INTEGER,
    [reps] INTEGER,
    [weight] INTEGER,
    [rest] INTEGER
);

CREATE TABLE IF NOT EXISTS plan_utility (
    [training_id] TEXT PRIMARY KEY,
    [date] TEXT NOT NULL,
    [type] TEXT NOT NULL,
    [sub_type] TEXT,
    [description] TEXT,
    [aim] TEXT
    [time] INTEGER
);
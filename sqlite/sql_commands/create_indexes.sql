--cardio table
CREATE INDEX IX_cardio_training_id_and_date ON cardio ([training_id], [date]);
--laps table
CREATE INDEX IX_laps_training_id ON laps (training_id);
--weights table
CREATE INDEX IX_weights_training_id_and_date ON weights ([training_id], [date]);
--calories table
CREATE INDEX IX_calories_date ON cardio ([date]);
--supplements table
CREATE INDEX IX_supplements_date ON supplements ([date]);
--date table
CREATE INDEX IX_date_date ON date_table ([date]);
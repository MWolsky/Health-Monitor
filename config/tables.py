from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Table:
    name: str
    primary_key: str


@dataclass
class TrainingPlan(Table):
    training_id: str
    date: date
    type: str 
    sub_type: str
    description: str
    aim: str
    

@dataclass
class Cardio(TrainingPlan):
    distance: int
    tempo: str
    heart_rate: int


@dataclass
class Weights(TrainingPlan):
    excercise: str
    series: int
    reps: int
    weight: int
    rest: int


@dataclass
class Utility(TrainingPlan):
    time: int


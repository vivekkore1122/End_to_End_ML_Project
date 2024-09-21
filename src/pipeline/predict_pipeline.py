import sys
import os
import pandas as pd
from src.exception import CustomExection
from src.logger import logging
from src.uitls import load_object
from src.exception import CustomExection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class PredictionPipline:
    def __init__(self) -> None:
        pass


    def predict(self,features):
        try:

            model_ptha=os.path.join("artifacts",'model.pkl')
            preprocessor_path=os.path.join("artifacts",'preprocessor.pkl')
            print("Before loading")
            model=load_object(file_path=model_ptha)
            preprocesser=load_object(file_path=preprocessor_path)
            print("After load")
            data_scaled=preprocesser.transform(features)
            preds=model.predict(data_scaled)

            return  preds
        
        except Exception as e :
            raise CustomExection(e,sys)
        
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomExection(e, sys)



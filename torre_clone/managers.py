#utilities
from typing import Dict, Any, Tuple, List, Optional, Union
import warnings
#Django
from django.db import connection
from django.db.models import Model
from django.db.models.query import QuerySet

"""
Father class of all tables managers
"""
class DataManager:

    def __init__(self, model: Model, fields: Dict[str, Any]=None, get_query: str=None, update_query: str =None) -> None:
        if fields is Dict and model is Model:
            self.fields: Optional[Dict[str, Any]] = fields
            self.__model: Model = model
            self.__get_query: Optional[str] = get_query
            self.__update_query: Optional[str] = update_query
        else:
            warnings.warn("The variable types are different")

    @property
    def get_query(self) -> Optional[str]:
        """query's getter"""
        return self.__get_query

    
    @property
    def model(self):
        """model's getter"""
        return self.__model

    @property
    def update_query(self) -> Optional[str]:
        """query's getter"""
        return self.__update_query

    @get_query.setter
    def get_query(self, get_query: str) -> None:
        self.__get_query = get_query

    @model.setter
    def model(self, model: Model) ->None:
        self.__model = model

    @update_query.setter
    def update_query(self, update_query: str) -> None:
        self.__get_query = update_query

    def crate_table(self, data) -> None:
        self.model.objects.create(**data)

    def create_update_query(self, key_identificator: str, unique_value: str, table: str) -> None:
        if self.fields is not None and key_identificator is not None and unique_value is not None:
            if type(key_identificator) is str and type(unique_value) is str:
                update_query = f'UPDATE {table} SET  '

                for key, value in self.fields.items():
                    if value == None:
                        continue
                    update_query += f'{key} = "{value}", '

                update_query = update_query[:-2]
                update_query += f' WHERE  {key_identificator} = "{unique_value}" '



                self.update_query = update_query 
                
            else:
                warnings.warn("Key and value must be a string")
        else:
            warnings.warn("Fields and id vars can't be empty")

    def data_exists(self, data: Dict[str, Any]) -> Model:
        if data is Dict:
            model: Model

            try:
                model = self.model.objects.get(**data)
            except self.model.DoesNotExist:
                model = self.model(**data)
                model.save()

            return model
        
        else:
            warnings.warn("Data must be a dict")

    def update_field(self) -> None:
        cursor = connection.cursor()
        cursor.execute(self.update_query)
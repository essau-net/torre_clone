#utilities
from typing import Dict, Any, Tuple, List
from django.db.models import Model
import warnings

"""
Father class of all tables managers
"""
class TablesManagers:
    def __init__(self, fields: Dict[str, Any], model: Model) -> None:
        if fields is Dict and model is Model:
            self.fields: Dict[str, Any] = fields
            self.__model: Model = model
        else:
            warnings.warn("The variable types are different")
    
    @property
    def model(self) -> Model:
        """model's getter"""
        return self.__model

    def data_exists(self, data: Dict[str, str]) -> bool:
        if data is Dict:
            self.model.objects.filter(**data)
    
    def get_data(self, sql_query: str, id: str='%') ->Tuple[List[str], ...] :
        pass


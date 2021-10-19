#utilities
from typing import Dict, Any, Tuple, List, Union
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

    def data_exists(self, data: Dict[str, Union[str, int]]) -> bool:
        if data is Dict:
            exists = self.model.objects.filter(**data)

            if exists:
                return True
            
            else:
                return False
        
        else:
            warnings.warn("Data must be a dict")
    
    def get_data(self, sql_query: str, id: str='%') ->Tuple[List[str], ...] :
        pass


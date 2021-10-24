#Utilities
from datetime import datetime
from imghdr import what
from pathlib import Path
from typing import Dict,Any, Optional
import os
import re
#Django
from django.db.models import Model
#Local


from torre_clone.managers import DataManager
from torre_clone.settings import MEDIA_ROOT
from users.models import User

class UserManager(DataManager):

    model: Model = User

    def __init__(self, fields: Dict[str, Any] = None, get_query: str = None, update_query: str = None) -> None:
        self.fields = fields
        self.__get_query: str = get_query
        self.__update_query: str = update_query

    @property
    def get_query(self) -> Optional[str]:
        return self.__get_query
    @property
    def update_query(self) -> None:
        return self.__update_query
    
    @get_query.setter
    def get_query(self, get_query) -> None:
        self.__get_query: str = get_query

    @update_query.setter
    def update_query(self, update_query: str) -> Path:
        self.__update_query:str = update_query
        
    def save_image(self, username: str, image: Any) -> None:
        directory: Path = MEDIA_ROOT / username
        exist_directory = os.path.isdir(directory)
        
        #Getting extension
        img_type: str = str(image.content_type)
        img_type = re.sub(r'^.*?/', '', img_type)

        identifier: str = str(datetime.now()) +'.' + img_type

        if exist_directory is False:
            os.mkdir(directory)
        
        
        path: Path = directory / identifier #Where is going to save the image

        #create image
        with open(path, "wb+") as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        destination.close()

        perfil_image: str = f'{username}/{identifier}' #Url to save in database

        return perfil_image

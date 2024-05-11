# it includes pydantic classes we are going to use
# we are going to have any sort of data we have in the application as well as model classes that define the structure of data
#
from enum import Enum
from pydantic import BaseModel,validator
from datetime import date


# ENUM is to limit data for a particular field
class GenreURLChoices(Enum):
    X = "x"
    Y = "y"
    Z = "z"
    
class GenreChoices(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"


# some bands ma y have none, or mu;ltiple albums
class Album(BaseModel):
    title: str
    release_date: date


# class BandDataClass(BaseModel):
#     # { 'id':1. 'name':'the band', 'genre': 'rock}
#     id: int
#     name: str
#     genre: str
#     albums: list[Album] = []  # name: annotation type = default_value
class BandBaseDataClass(BaseModel):
    """ 
    An abstract class that'll be inherited. It contains common fields
    """
    name: str
    genre: GenreChoices
    albums: list[Album] = []  # name: annotation type = default_value


class BandCreateDataClass(BandBaseDataClass):
    # adding data  validator: convert genre into titlecase
    @validator('genre',pre=True) # pre=True to run before normal validation
    def title_case_genre(cls, value):
        return value.title()
    
class BandWithIDDataClass(BandBaseDataClass):
    id: int
    
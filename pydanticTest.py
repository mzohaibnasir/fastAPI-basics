"""

Pydantic allows us to create classes that inherit from BaseModels. 
These classes contain fields that define the structure of piece of data

Pydantic's BaseModel class is a powerful tool for defining data structures in Python. Here's a detailed explanation:

## Pydantic BaseModels:

1. BaseModels are classes that inherit from `pydantic.BaseModel`
2. They provide a way to define the schema (structure) of data objects for validation, serialization, and deserialization.
3. Each field in a BaseModel represents a piece of data within the overall structure.
## Defining Fields:

1. You define fields within a BaseModel class using type annotations (similar to static typing in other languages).
2. These annotations specify the expected data type for each field.


# Type annotations are a that provides a way to specify the expected data type for variables, function arguments, and return values
"""

# from pydantic import BaseModel
from schemas import GenreURLChoices, BandDataClass
from main import BANDS


# return [BandDataClass(**b) for b in BANDS]


# for b in BANDS:
#     # print(*b)
#     # print(**b)
#     print(BandDataClass(**b))


if __name__ == "__main__":  # code to be executed only when the script is run directly
    print([BandDataClass(**b) for b in BANDS])
# *b unpacks a list into positional arguments
# **b unpacks a dictionary into keyword arguments


print(__name__)

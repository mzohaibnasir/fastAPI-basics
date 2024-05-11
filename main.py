from fastapi import FastAPI, HTTPException, Path,Query
# from schemas import GenreURLChoices, BandDataClass
from schemas import GenreURLChoices, BandBaseDataClass,BandCreateDataClass,BandWithIDDataClass
from typing import Annotated
# from enum import Enum
import uvicorn

fastapp = FastAPI()


# class GenreURLChoices(Enum):
#     X = "x"
#     Y = "y"
#     Z = "z"


# creating list endpoint
BANDS = [
    {"id": 1, "name": "A", "genre": "X"},
    {"id": 2, "name": "B", "genre": "Y"},
    {"id": 3, "name": "C", "genre": "Z"},
    {"id": 3, "name": "S", "genre": "Z"},
    {
        "id": 4,
        "name": "A",
        "genre": "Z",
        "albums": [{"title": "Title", "release_date": "1971-07-21"}],
    },
]


@fastapp.get("/")
async def index() -> dict[str, int]:
    return {"hello": 786}


@fastapp.get("/about")
async def about() -> str:
    return "An exceptional Company."


###############################3 TWO ENDPOINTS
# to return list of data
# @fastapp.get("/bands")
# async def bands() -> list[dict]:
#     return BANDS


# @fastapp.get("/bands")
# async def bands() -> list[BandDataClass]:
# return [BandDataClass(**b) for b in BANDS]  # with BandDataClass we have validation


# @fastapp.get("/bands")
# async def bands(
#     genre: GenreURLChoices | None = None,  # fn will look for query parameter `genre``
#     has_albums: bool = False,
# ) -> list[BandDataClass]:
#     if genre:
#         return [BandDataClass(**b) for b in BANDS if b["genre"].lower() == genre.value]

#     return [BandDataClass(**b) for b in BANDS]  # with BandDataClass we have validation
#     # `| None = None` to return all of bands. when default is None mean qquery parameter is not required


# @fastapp.get("/bands")
# async def bands(
#     genre: GenreURLChoices | None = None,  # fn will look for query parameter `genre``
#     has_albums: bool = False,
# ) -> list[BandWithIDDataClass]:
#     band_list = [BandWithIDDataClass(**b) for b in BANDS]
#     if genre:
#         band_list = [b for b in band_list if b.genre.value.lower() == genre.value]
#     if has_albums:
#         band_list = [b for b in band_list if len(b.albums) > 0]
#     return band_list  # with BandDataClass we have validation
#     # `| None = None` to return all of bands. when default is None mean qquery parameter is not required



@fastapp.get("/bands")
async def bands(
    genre: GenreURLChoices | None = None,  # fn will look for query parameter `genre``
    q:Annotated[str|None,Query(max_length=10)]=None
) -> list[BandWithIDDataClass]:
    band_list = [BandWithIDDataClass(**b) for b in BANDS]
    if genre:
        band_list = [b for b in band_list if b.genre.value.lower() == genre.value]
    if q:
        band_list = [b for b in band_list if q.lower() in b.name.lower() ]
    return band_list  # with BandDataClass we have validation
    # `| None = None` to return all of bands. when default is None mean qquery parameter is not required




"""
2. GenreURLChoices | None: This specifies the expected type and optionality of the parameter.
- GenreURLChoices: This likely refers to a custom enumeration class defined elsewhere in your code. This class presumably defines the allowed valid values for the genre parameter. By using an enumeration, you ensure that only valid genres are accepted by the endpoint.
- | None: The pipe symbol (|) acts as a union operator, indicating that the parameter can either be of type GenreURLChoices or None.
- = None: This sets the default value of the genre parameter to None. If the client doesn't explicitly provide a genre parameter in the request, it will be treated as None.
"""


##################################################################################
# to return band by id
"""
@fastapp.get("/bands/{band_id}", status_code=200)
async def band(band_id: int) -> dict:
    band = next(
        (b for b in BANDS if b["id"] == band_id), None
    )  # next( iterator, default) # one value not multiple values at a time

    # x = (i for i in BANDS if i["id"] == 2)  # round brackets for generator
    # # list(x)
    # print(next(x))
    # print(next(x))
    # print(next(x, "xxx"))

    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band
"""


"""
Annotation cant work alone. FastAPI know how to work QUERY type. FastAPI's query is needed for Annotation to work
Fastapi uses annotation to add metadata to request parameter
we  can use that using Query from FastAPI and Annotated from typing"""

@fastapp.get("/bands/{band_id}", status_code=200)
async def band(band_id: Annotated[int,Path(title="The band ID- go to Redoc")]) -> BandWithIDDataClass:
    band = next(
        (BandWithIDDataClass(**b) for b in BANDS if b["id"] == band_id), None
    )  # next( iterator, default) # one value not multiple values at a time

    # x = (i for i in BANDS if i["id"] == 2)  # round brackets for generator
    # # list(x)
    # print(next(x))
    # print(next(x))
    # print(next(x, "xxx"))

    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


# @fastapp.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: str) -> list[dict]:
#     return [b for b in BANDS if b["genre"].lower() == genre.lower()]


# @fastapp.get("/bands/genre/{genre}")
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [b for b in BANDS if b["genre"].lower() == genre.value]


@fastapp.get("/bands/genre/{genre}")
async def bands_for_genre(genre: GenreURLChoices) -> list[BandWithIDDataClass]:
    return [BandWithIDDataClass(**b) for b in BANDS if b["genre"].lower() == genre.value]


# GenreURLChoices will return more descriptive error

################################


""" 
# POST request:

when you need to send data from a client(browser) to your API, you send it as a request body.
A request body is data sent by the client to your API. 
A response body is data your API sends to the client.
API always have to sent a response bosy but clients don't necessary need to send request bodies all the time.
To decalre a requast body we'll declare pydantic models

"""

# create new band

@fastapp.post("/bands")
async def create_band_class(band_data:BandCreateDataClass)->BandWithIDDataClass: 
    # with BandCreateDataClass, fastapi will automatically extract data from request body
    id = BANDS[-1]["id"]+1
    band = BandWithIDDataClass(id=id, **band_data.model_dump()).model_dump() # to get resultant dict
    BANDS.append(band)
    return band
    



########################################


if __name__ == "__main__":  # code to be executed only when the script is run directly
    uvicorn.run(
        "main:fastapp", host="127.0.0.1", port=5000, log_level="info", reload=True
    )


############################################################################
"""
The command uvicorn main:app refers to:
    main: the file main.py (the Python "module").
    app: the object created inside of main.py with the line app = FastAPI().
    
It is equivalent to:
    `from main import app`
"""

""" or uvicorn main:app --reload"""


"""
Query parameters: 
   Query is a set of key-value pairs after `?` in a URL, separated by `&` characters. `?` is query 
separator and not part of query string. passes query string string directly to program i.e. `q=19&color=purple`
"""

from typing import Annotated,get_type_hints, get_origin,get_args
from fastapi import Query
from functools import wraps

# def double(x:int)->int:
#     return x*2

# def double(x:Annotated[int, (0,100)])->int:
#     type_hints = get_type_hints(double,include_extras=True)
#     print(type_hints)
#     hint = type_hints['x']
#     print("x: ",hint)
#     if get_origin(hint) is Annotated:
#         hint_type,*hint_args = get_args(hint)
#         print(f"HINT: {hint_type}")
#         print(f"Value: {hint_args}")
#         miny,maxy= hint_args[0]
#         print(f"min: {miny}, max: {maxy}")
        
#         if not (miny<=x<=maxy):
#             raise ValueError(f"{x} falls outside of the boundary {miny}->{maxy}")
            
#     return x*2


def check_value_range(func):
    @wraps(func)
    def wrapped(x):
        type_hints = get_type_hints(double,include_extras=True)
        print(type_hints)
        hint = type_hints['x']
        print("x: ",hint)
        if get_origin(hint) is Annotated:
            hint_type,*hint_args = get_args(hint)
            print(f"HINT: {hint_type}")
            print(f"Value: {hint_args}")
            miny,maxy= hint_args[0]
            print(f"min: {miny}, max: {maxy}")
            
            if not (miny<=x<=maxy):
                raise ValueError(f"{x} falls outside of the boundary {miny}->{maxy}")
        
        return func(x)
    return wrapped



@check_value_range
def double(x:Annotated[int, (0,10)])->int:
    return x*2


result=double(11)
print(result)


# Annotation cant work alone. FastAPI know how to work QUERY type. FastAPI's query is needed for Annotation to work
# FastAPI uses annotation to add metadata to request parameter
# we can use that using Query from FastAPI and Annotated from typing
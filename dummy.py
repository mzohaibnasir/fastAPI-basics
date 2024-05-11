# creating list endpoint
BANDS = [
    {"id": 1, "name": "A", "genre": "X"},
    {"id": 2, "name": "B", "genre": "Y"},
    {"id": 3, "name": "C", "genre": "Z"},
]


# to return band by id
@fastapp.get("/bands/{band_id}")
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b["id"] == band_id), None)
    if band is None:
        # status code 404
        raise HTTPException(status_code=404, detail="Band not found!")
    return band


print(())

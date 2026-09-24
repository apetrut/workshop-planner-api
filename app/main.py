from fastapi import FastAPI, HTTPException, Path

from app.models import Workshop, WorkshopInput

app = FastAPI(title="Workshop Planner API")

NOT_IMPLEMENTED = "Workshop persistence is not implemented"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/workshops", response_model=Workshop, status_code=201)
def create_workshop(workshop: WorkshopInput) -> Workshop:
    raise HTTPException(status_code=501, detail=NOT_IMPLEMENTED)


@app.get("/workshops", response_model=list[Workshop])
def list_workshops() -> list[Workshop]:
    raise HTTPException(status_code=501, detail=NOT_IMPLEMENTED)


@app.get("/workshops/{id}", response_model=Workshop)
def get_workshop(workshop_id: str = Path(alias="id")) -> Workshop:
    raise HTTPException(status_code=501, detail=NOT_IMPLEMENTED)


@app.put("/workshops/{id}", response_model=Workshop)
def replace_workshop(
    workshop: WorkshopInput, workshop_id: str = Path(alias="id")
) -> Workshop:
    raise HTTPException(status_code=501, detail=NOT_IMPLEMENTED)


@app.delete("/workshops/{id}", status_code=204)
def delete_workshop(workshop_id: str = Path(alias="id")) -> None:
    raise HTTPException(status_code=501, detail=NOT_IMPLEMENTED)

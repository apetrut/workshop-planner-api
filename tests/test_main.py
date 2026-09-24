from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

VALID_WORKSHOP = {
    "title": "Intro to FastAPI",
    "description": "Hands-on session",
    "startTime": "2026-10-01T09:00:00",
    "endTime": "2026-10-01T11:00:00",
    "organizerId": "org-1",
    "status": "scheduled",
}


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_openapi_declares_expected_routes() -> None:
    schema = client.get("/openapi.json").json()
    paths = schema["paths"]
    assert set(paths["/workshops"]) == {"post", "get"}
    assert set(paths["/workshops/{id}"]) == {"get", "put", "delete"}
    assert "get" in paths["/health"]

    create_op = paths["/workshops"]["post"]
    create_response_schema = (
        create_op["responses"]["201"]["content"]["application/json"]["schema"]
    )
    assert create_response_schema["$ref"].endswith("Workshop")
    request_schema = (
        create_op["requestBody"]["content"]["application/json"]["schema"]
    )
    request_schema_ref = request_schema["$ref"]
    assert request_schema_ref.endswith("WorkshopInput")

    list_op = paths["/workshops"]["get"]
    list_schema = (
        list_op["responses"]["200"]["content"]["application/json"]["schema"]
    )
    assert list_schema["type"] == "array"
    assert list_schema["items"]["$ref"].endswith("Workshop")

    workshop_schema = schema["components"]["schemas"]["Workshop"]
    workshop_input_schema = schema["components"]["schemas"]["WorkshopInput"]
    expected_fields = {
        "title", "description", "startTime", "endTime", "organizerId", "status"
    }
    assert expected_fields <= set(workshop_input_schema["properties"])
    assert expected_fields | {"id"} <= set(workshop_schema["properties"])


def test_create_workshop_returns_501() -> None:
    response = client.post("/workshops", json=VALID_WORKSHOP)
    assert response.status_code == 501


def test_list_workshops_returns_501() -> None:
    response = client.get("/workshops")
    assert response.status_code == 501


def test_get_workshop_returns_501() -> None:
    response = client.get("/workshops/abc-123")
    assert response.status_code == 501


def test_replace_workshop_returns_501() -> None:
    response = client.put("/workshops/abc-123", json=VALID_WORKSHOP)
    assert response.status_code == 501


def test_delete_workshop_returns_501() -> None:
    response = client.delete("/workshops/abc-123")
    assert response.status_code == 501


def test_create_workshop_malformed_returns_422() -> None:
    malformed = dict(VALID_WORKSHOP)
    malformed.pop("title")
    response = client.post("/workshops", json=malformed)
    assert response.status_code == 422

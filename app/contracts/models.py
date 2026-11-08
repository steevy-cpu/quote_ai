"""Initial shared request contract; no application services are implemented."""
from dataclasses import dataclass, fields


@dataclass(frozen=True)
class CustomerRequest:
    schema_version: str
    request_id: str
    customer_name: str
    customer_email: str
    message: str

    @classmethod
    def from_dict(cls, payload: dict) -> "CustomerRequest":
        if not isinstance(payload, dict):
            raise ValueError("Request must be a JSON object")
        expected = {field.name for field in fields(cls)}
        if set(payload) != expected:
            raise ValueError("Request fields do not match schema version 0.1")
        if any(not isinstance(value, str) or not value.strip()
               for value in payload.values()):
            raise ValueError("All request fields must be nonempty strings")
        if payload["schema_version"] != "0.1":
            raise ValueError("Unsupported schema_version")
        return cls(**payload)

import json
from pathlib import Path
import unittest

from app.contracts.models import CustomerRequest

ROOT = Path(__file__).resolve().parents[2]


class RequestContractTests(unittest.TestCase):
    def setUp(self):
        self.payload = json.loads(
            (ROOT / "data/samples/customer_request.json").read_text()
        )

    def test_example_round_trip(self):
        request = CustomerRequest.from_dict(self.payload)
        self.assertEqual(request.request_id, "demo-request-001")
        self.assertEqual(request.message, self.payload["message"])

    def test_missing_and_unknown_fields_rejected(self):
        missing = dict(self.payload)
        missing.pop("message")
        for payload in (missing, dict(self.payload, typo="unexpected")):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                CustomerRequest.from_dict(payload)

    def test_empty_or_wrong_type_rejected(self):
        for value in ("", "   ", None, 2500, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                CustomerRequest.from_dict(dict(self.payload, message=value))

    def test_unsupported_version_rejected(self):
        with self.assertRaises(ValueError):
            CustomerRequest.from_dict(dict(self.payload, schema_version="2.0"))

    def test_non_object_rejected(self):
        with self.assertRaises(ValueError):
            CustomerRequest.from_dict([])


if __name__ == "__main__":
    unittest.main()

"""Regression tests for PromptVersion.published_at nullability.

A version only has a ``published_at`` timestamp once it has been set to
``live``. For ``draft``, ``stable`` and ``archived`` versions the server
returns ``published_at: null``, so the field must be optional; otherwise
deserializing any non-live version raises pydantic ``ValidationError``.
"""
import datetime

from px0.models.prompt_version import PromptVersion
from px0.models.list_versions200_response import ListVersions200Response


def _draft_payload():
    return {
        "id": "ver_1",
        "prompt_id": "prm_1",
        "version": 1,
        "template": "Hello {{.name}}!",
        "status": "draft",
        "created_at": "2024-01-01T00:00:00Z",
        "published_at": None,
        "tags": [],
    }


def test_draft_version_with_null_published_at_deserializes():
    version = PromptVersion.from_dict(_draft_payload())
    assert version is not None
    assert version.published_at is None
    assert version.status == "draft"


def test_published_at_omitted_entirely_deserializes():
    payload = _draft_payload()
    del payload["published_at"]
    version = PromptVersion.from_dict(payload)
    assert version.published_at is None


def test_live_version_keeps_published_at():
    payload = _draft_payload()
    payload["status"] = "live"
    payload["published_at"] = "2024-01-02T03:04:05Z"
    version = PromptVersion.from_dict(payload)
    assert isinstance(version.published_at, datetime.datetime)


def test_null_published_at_is_dropped_by_to_dict():
    version = PromptVersion.from_dict(_draft_payload())
    assert "published_at" not in version.to_dict()


def test_list_versions_with_a_draft_element_deserializes():
    response = ListVersions200Response.from_dict({"versions": [_draft_payload()]})
    assert response is not None
    assert response.versions[0].published_at is None

import pytest

from app.main import main


def test_empty_document_id(monkeypatch):

    monkeypatch.setattr(
        "builtins.input",
        lambda _: ""
    )

    with pytest.raises(ValueError, match="Document ID cannot be empty"):
        main()


def test_empty_document_text(monkeypatch):

    inputs = iter([
        "test-document",
        ""
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    with pytest.raises(ValueError, match="Document text cannot be empty"):
        main()
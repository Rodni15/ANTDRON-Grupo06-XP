"""Smoke tests iniciales para validar estructura base y CI antes de implementar las HU."""

from pathlib import Path


def test_paquetes_python_existen():
    root = Path(__file__).resolve().parent.parent
    assert (root / "main.py").is_file()
    assert (root / "src" / "pkAntCiberDronContract" / "__init__.py").is_file()
    assert (root / "src" / "ant" / "__init__.py").is_file()


def test_import_paquetes_base():
    import ant  # noqa: F401
    import pkAntCiberDronContract  # noqa: F401

"""Import each shipped language as a real package module so STRINGS is covered.

test_languages.py validates key parity, but it (like production load_language)
exec's the files via spec_from_file_location. Coverage never attributes that to
opensak.lang.*, and the first such spec-exec also poisons coverage's trace
decision for that file — so a later import wouldn't be recorded either.

Importing here at collection time means coverage's first encounter with each
language file is the genuine package import: this module is collected before
test_languages and before the e2e fixtures call load_language(), so the eight
files are attributed to opensak.lang.* (0% -> 100%).
"""

import importlib

import pytest

from opensak.lang import AVAILABLE_LANGUAGES

_MODULES = {code: importlib.import_module(f"opensak.lang.{code}") for code in AVAILABLE_LANGUAGES}


@pytest.mark.parametrize("code", sorted(AVAILABLE_LANGUAGES))
def test_language_module_exposes_strings(code):
    strings = _MODULES[code].STRINGS
    assert isinstance(strings, dict)
    assert strings

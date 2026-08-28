"""Unit tests for shared justfile quoting assertions."""

from tests.justfile_quoting import find_unquoted_recipe_path_interpolations


def test_finds_each_unquoted_occurrence_on_a_mixed_line() -> None:
    text = 'recipe:\n    cd "{{root}}" && cp {{root}}/x.tsv out\n'
    assert find_unquoted_recipe_path_interpolations(text, {"root"}) == [
        "line 2: {{root}}"
    ]


def test_finds_whitespace_variant_and_new_path_function() -> None:
    text = "recipe:\n    cd {{ justfile_directory() }} && true\n"
    assert find_unquoted_recipe_path_interpolations(
        text, {"justfile_directory()"}
    ) == ["line 2: {{ justfile_directory() }}"]


def test_accepts_single_and_double_quotes() -> None:
    text = "recipe:\n    cd '{{ root }}' && cp \"{{root}}/x.tsv\" out\n"
    assert find_unquoted_recipe_path_interpolations(text, {"root"}) == []

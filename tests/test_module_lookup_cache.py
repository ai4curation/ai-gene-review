"""Batch ontology caching must not leak across adapters or hide transient failures."""

from ai_gene_review.validation import module_validator as mv


def test_label_cache_shared_across_files_and_scoped_to_adapter(monkeypatch):
    calls = []
    class Adapter:
        def __init__(self, name):
            self.name = name
        def label(self, curie):
            calls.append((self.name, curie))
            return self.name
        def entity_aliases(self, curie):
            return ["alias"]
    monkeypatch.setattr(mv, "_get_cached_adapter", Adapter)
    cache = {}
    first = mv._build_oak_resolver({"GO": "first"}, cache)
    second = mv._build_oak_resolver({"GO": "first"}, cache)
    other = mv._build_oak_resolver({"GO": "other"}, cache)
    assert first("GO:1") == second("GO:1") == ("ok", "first", {"alias"})
    assert other("GO:1") == ("ok", "other", {"alias"})
    assert calls == [("first", "GO:1"), ("other", "GO:1")]


def test_transient_lookup_failure_is_retried(monkeypatch):
    results = iter([RuntimeError("temporarily offline"), "recovered"])
    class Adapter:
        def label(self, curie):
            result = next(results)
            if isinstance(result, Exception):
                raise result
            return result
    monkeypatch.setattr(mv, "_get_cached_adapter", lambda _: Adapter())
    cache = {}
    first = mv._build_oak_resolver({"GO": "same"}, cache)
    assert first("GO:1")[0] == "unavailable"
    assert first("GO:1")[0] == "unavailable"
    assert mv._build_oak_resolver({"GO": "same"}, cache)("GO:1") == ("ok", "recovered", set())

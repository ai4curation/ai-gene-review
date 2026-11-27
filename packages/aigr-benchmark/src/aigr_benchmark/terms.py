"""GO terms that carry no information as benchmark targets or CAFA-style truths."""

#: Root and generic binding terms, excluded from targets unless a spec overrides them.
DEFAULT_EXCLUDED_TERMS = frozenset(
    {
        "GO:0005515",  # protein binding
        "GO:0005488",  # binding
        "GO:0003674",  # molecular function
        "GO:0008150",  # biological process
        "GO:0005575",  # cellular component
    }
)

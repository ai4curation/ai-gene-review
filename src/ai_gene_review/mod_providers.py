"""Model organism databases whose curated gene descriptions are used as review sources.

Kept free of network and ETL imports so validation can use it.
"""

from typing import Dict, Tuple

# Alliance MOD prefix -> (filename slug, display name).
MOD_PROVIDER: Dict[str, Tuple[str, str]] = {
    "WB": ("wormbase", "WormBase"),
    "FB": ("flybase", "FlyBase"),
    "SGD": ("sgd", "SGD"),
    "MGI": ("mgi", "MGI"),
    "RGD": ("rgd", "RGD"),
    "ZFIN": ("zfin", "ZFIN"),
    "Xenbase": ("xenbase", "Xenbase"),
}


def is_mod_description_file(name: str) -> bool:
    """True for a ``GENE-deep-research-<mod>.md`` MOD gene description file.

    >>> is_mod_description_file("fshr-1-deep-research-wormbase.md")
    True
    >>> is_mod_description_file("fshr-1-deep-research-falcon.md")
    False
    """
    return any(name.endswith(f"-deep-research-{slug}.md") for slug, _ in MOD_PROVIDER.values())

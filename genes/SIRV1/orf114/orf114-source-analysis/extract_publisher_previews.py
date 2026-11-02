#!/usr/bin/env python3
"""Extract inspected publisher passages without editing normal reference caches.

Run from any directory with Python 3. The generated evidence artifact links each
passage to its canonical PMID/DOI and hashes the actual immutable cache input.
It is a reproducible excerpt collection, not a substitute full-text publication.
"""

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCES = [
    {
        "pmid": "40240860",
        "doi": "10.1038/s41586-025-08649-0",
        "url": "https://www.nature.com/articles/s41586-025-08649-0",
        "cache": "url_https___www.nature.com_articles_s41586-025-08649-0.md",
        "passages": [
            "cannot inhibit subtype III-B CRISPR immunity when expressed from the viral genome, but exhibit anti-CRISPR activity when expressed from a plasmid.",
        ],
    },
    {
        "pmid": "40240860",
        "doi": "10.1038/s41586-025-08649-0",
        "url": "https://www.nature.com/articles/s41586-025-08649-0/figures/1",
        "cache": "url_https___www.nature.com_articles_s41586-025-08649-0_figures_1.md",
        "passages": [
            "Plasmid-borne expression of AcrIII-1 homologues (p.gp37, p.gp29) exhibits type III-B anti-CRISPR activity.",
        ],
    },
    {
        "pmid": "40240860",
        "doi": "10.1038/s41586-025-08649-0",
        "url": "https://www.nature.com/articles/s41586-025-08649-0/figures/2",
        "cache": "url_https___www.nature.com_articles_s41586-025-08649-0_figures_2.md",
        "passages": [
            "c, Schematic of SIRV2 Para-gp29 virus.",
            "d, Growth curves of CRISPR-III-B-positive cultures infected with parental SIRV2 or SIRV2 Para-gp29 (MOI, 0.1) with (ACV medium) or without (SCV medium) gp29 induction with 0.2% arabinose.",
        ],
    },
    {
        "pmid": "40240850",
        "doi": "10.1038/s41586-025-08650-7",
        "url": "https://www.nature.com/articles/s41586-025-08650-7",
        "cache": "url_https___www.nature.com_articles_s41586-025-08650-7_error_cookies_not_supported.md",
        "passages": [
            "AcrIII-1 and Crn2 are cA4-specific ring nucleases in vitro",
            "the acrIII-1 gene from the archaeal rudivirus SIRV1 was shown to overcome type III CRISPR immunity in S. islandicus M.16.4 when expressed from a plasmid, allowing infection with the virus SSeV1.",
        ],
    },
]


def main():
    manifest = []
    text = [
        "# Canonical 2025 AcrIII-1 publisher-preview evidence",
        "",
        "Generated from normally fetched publisher caches; not complete article text.",
        "Canonical publication identities are PMID:40240860 and PMID:40240850.",
        "The legacy cookies query survives only in the input cache filename, not the article identity.",
        "No third-party reproduction is used by this extraction.",
        "",
    ]
    for source in SOURCES:
        path = ROOT / "publications" / source["cache"]
        raw = path.read_bytes()
        content = raw.decode()
        for passage in source["passages"]:
            assert passage in content, (path, passage)
        text += [
            f"## PMID:{source['pmid']} — DOI:{source['doi']}",
            "",
            f"Publisher location: {source['url']}",
            f"Input: publications/{source['cache']}",
            f"SHA256: {hashlib.sha256(raw).hexdigest()}",
            "",
        ]
        text += [f"> {passage}\n" for passage in source["passages"]]
        manifest.append({**source, "sha256": hashlib.sha256(raw).hexdigest()})
    (OUT / "publisher-preview-excerpts.md").write_text("\n".join(text) + "\n")
    (OUT / "publisher-preview-extraction.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    )


if __name__ == "__main__":
    main()

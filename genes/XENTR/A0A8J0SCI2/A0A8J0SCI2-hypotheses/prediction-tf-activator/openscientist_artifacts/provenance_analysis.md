# Provenance — sequence analysis for A0A8J0SCI2

Source: UniProt REST `https://rest.uniprot.org/uniprotkb/A0A8J0SCI2.json` (fetched 2026-07-09).

## Inputs
- Length: 265 aa
- Sequence:
```
MGSSQNTLQMMDNNHDENSHQSLHKSHITNNKLRRKYSCNECQKHFNNKRDFHIHQRSHKREKPFSCSECGKCFSYQSRLNHHQRTHTGEKPFSCSECGKCFSRKFYRDCHQRTHTGEKPFSCSECGKCFSYQSRLSRHQRTHTGEKPFSCPECGKCFSRKVYRDCHQRTHTGEKPFSCSECGKCFSSKFYRDCHQRTHTGEKPFSCSECGKCFSQQSDLKIHYKTHTGEKPFSCSECGKCFLRKSQLDRHERTHKGEKPFSYSK
```

## Code (executed via MCP execute_code, Python)
```python
import requests, re
from collections import Counter
d = requests.get("https://rest.uniprot.org/uniprotkb/A0A8J0SCI2.json").json()
seq = d["sequence"]["value"]
pat = re.compile(r'C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H')   # C2H2 fingerprint
fingers = [(m.start()+1, m.end()) for m in pat.finditer(seq)]
linkers = re.findall(r'T[GS]E[KR]P', seq)                  # canonical TGEKP linkers
acidic = sum(seq.count(x) for x in "DE") / len(seq)
```

## Computed results
- **C2H2 finger motif hits (8):** 39–59, 67–87, 95–115, 123–143, 151–171, 179–199, 207–227, 235–255
- **UniProt-annotated C2H2 domains (8):** 37–64, 65–92, 93–120, 121–148, 149–176, 177–204, 205–232, 233–260
- **Canonical TGEKP linkers:** 6 × `TGEKP`
- **N-terminal region before finger 1:** 36 aa (residues 1–27 annotated Disordered; 1–12 polar-residue compositional bias)
- **Acidic (D+E) fraction:** 0.098 (no acidic activation domain)
- **Domain databases:** InterPro IPR013087 (Znf_C2H2_type), IPR036236 (Znf_C2H2_sf); Pfam PF00096 (zf-C2H2 ×5); PANTHER PTHR24381 / SF440; **no** KRAB/BTB/SCAN/effector domain reported.

## GO annotations currently on the entry
| GO ID | Term | Evidence |
|-------|------|----------|
| GO:0000981 | DNA-binding transcription factor activity, RNA Pol II-specific | IBA:GO_Central |
| GO:0000978 | RNA Pol II cis-regulatory region sequence-specific DNA binding | IBA:GO_Central |
| GO:0006357 | regulation of transcription by RNA Pol II | IBA:GO_Central |
| GO:0005634 | nucleus | IBA:GO_Central |
| GO:0008270 | zinc ion binding | IEA:UniProtKB-KW |
| GO:0006351 | DNA-templated transcription | IEA:UniProtKB-KW |

## AlphaFold structural check (AF-A0A8J0SCI2-F1, v6)
Fetched via `https://alphafold.ebi.ac.uk/api/prediction/A0A8J0SCI2`; per-residue pLDDT parsed from CA B-factors.

| Region | Residues | Mean pLDDT | Fraction >70 |
|--------|----------|-----------|--------------|
| N-terminus | 1–36 | 36.8 | 0.03 (disordered) |
| Zinc-finger core | 37–260 | 90.6 | 0.99 (confidently folded) |
| C-terminus | 261–265 | 43.4 | — (disordered) |
| Whole model | 1–265 | 82.4 | global |

The confidently folded region coincides exactly with the 8 annotated C2H2 domains; the flanking regions that could host a transactivation/effector module are unstructured. No independent folded effector domain exists.

## GO ontology check (QuickGO API)
- **GO:0000981** "DNA-binding transcription factor activity, RNA Pol II-specific" — def: "…that **modulates** the transcription of specific gene sets transcribed by RNA polymerase II." (direction-neutral)
- **GO:0001228** "…transcription **activator** activity, RNA Pol II-specific" — def: "…that **activates or increases** transcription…"; is_a ancestors = {GO:0000981, GO:0003700, GO:0140110, GO:0001216, GO:0003674}. **GO:0000981 ∈ ancestors → GO:0001228 is a strict child.**
- **GO:0001227** "…transcription **repressor** activity…" — the sibling directional term; equally unsupported here.

Conclusion: the ProtNLM2 term adds an unsupported directional (activator) constraint to the already-annotated, direction-neutral parent.

## Interpretation
A canonical, effectorless 8×C2H2 array, structurally confirmed by AlphaFold; the predicted activator term is a strict directional child of the supported parent with no evidence for the added direction. Direction of regulation (activator vs repressor) is not encoded in the array and cannot be inferred from sequence. The predicted activator-specific term GO:0001228 is over-specific relative to the direction-neutral GO:0000981 already supported by phylogenetic (IBA) evidence.

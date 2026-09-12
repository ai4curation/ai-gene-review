# AP5B1 (beta-5 adaptin): does it carry the beta-adaptin clathrin-binding apparatus?

Reproducible analysis for the AP5B1 gene review. Every number and every residue position
below is emitted by `clathrin_box_scan.py`, which fetches at run time: sequences from
UniProt, Pfam domain boundaries from InterPro, secondary-structure and REGION features from
UniProt, and the modelled residue ranges of PDB 8YAB chain B from the PDBe polymer-coverage
API. Nothing is hardcoded; expected sequence lengths are asserted so a changed accession
fails loudly. Cross-check any figure in this document against `run-output.txt` or
`results.json` — if it is not in one of those, it does not belong here.

```
cd genes/human/AP5B1/AP5B1-bioinformatics
uv run python clathrin_box_scan.py --json results.json
```

`run-output.txt` is the captured output of the run described here; `results.json` is the full
machine-readable result set.

## Why this test

The beta subunits of AP-1, AP-2 and AP-3 are built as N-terminal alpha-solenoid trunk ->
long unstructured hinge -> C-terminal appendage. Clathrin is recruited by short linear
motifs **in the hinge**: the clathrin box L(phi)x(phi)[DE] (AP2B1 `LLNLD`, AP1B1 `LLNLD`),
the type-II `LLDLL` box, and the W-box `PWxxW`. The question for AP5B1 is whether a protein
that is unambiguously beta-adaptin-like by fold retains that recruitment apparatus, because
AP-5 is reported to work without clathrin.

Hirst et al. 2011 (PMID:22022230) asserted, for the then-unnamed beta-5 sequence
DKFZp761E198, that (i) the classical clathrin box is missing, (ii) `LLDLL` and `YQW` are
missing, (iii) the one `WDW` present lies "in the middle of the alpha-helical solenoid" and
is therefore unavailable, and (iv) beta-5 "lacks a long unstructured linker separating the
solenoid and appendage domains". Those statements predate both the Pfam models for AP5B1
(PF21587-PF21590, added 2023) and the cryo-EM structure (PDB 8YAB, 2025). This script
re-tests all four against the current records, with the four classical beta adaptins as
controls.

## Results

Sequence lengths verified against UniProt at run time: AP5B1 878 aa, AP1B1 949 aa,
AP2B1 937 aa, AP3B1 1094 aa, AP4B1 739 aa.

### 1. Clathrin box: present as a sequence match, absent as an accessible motif

| Protein | L(phi)x(phi)[DE] matches | matches outside any Pfam domain | position |
|---|---|---|---|
| **AP5B1** | 1 (`LLRLE`@841) | **0** | inside PF21590 (AP5B1_C, 781-873) |
| AP1B1 | 1 (`LLNLD`@632) | 1 | in the 534-720 hinge |
| AP2B1 | 1 (`LLNLD`@631) | 1 | in the 534-711 hinge |
| AP3B1 | 3 | 0 | all inside folded domains |
| AP4B1 | 1 (`LVGID`@523) | 1 | at the trunk boundary (523) |

The consensus is short enough that a chance match is expected in a 878-residue protein, and
AP5B1 has exactly one. What distinguishes it from the AP-1/AP-2 case is position: the AP1B1
and AP2B1 boxes sit in the long unstructured hinge, where a linear motif can reach clathrin;
the AP5B1 match sits inside the folded C-terminal Pfam domain. **The claim survives in the
form that matters**: AP5B1 has no clathrin box in an accessible linker.

### 2. `LLDLL` and `YQW`: absent, exactly as reported

Both are absent from AP5B1 (and from all four controls). This reproduces Hirst et al.
verbatim.

### 3. `WDW`: present, inside the solenoid, and unavailable — the 2011 reading holds

AP5B1 has one `WDW`, at 223-225. Hirst et al. placed it "in the middle of the alpha-helical
solenoid" and concluded it is therefore unlikely to reach clathrin. The structure released
fourteen years later agrees. From the run:

* **residues 223-229 are modelled in PDB 8YAB chain B**, whose modelled span is 7-631. The
  motif is inside the solenoid, not C-terminal to it and not in a linker between structural
  modules.
* it sits between two solenoid helices — nearest UniProt feature before is `Helix 182-203`,
  nearest after is the MobiDB-lite `Region 234-260 (Disordered)` — and is flanked by two
  unmodelled stretches, **213-222 and 230-260**. So it is a short ordered island in a poorly
  ordered inter-helical loop of the trunk, not an exposed hinge of the AP-1/AP-2 kind.
* the only reason it superficially looks inter-domain is that Pfam's AP5B1-specific models
  leave 105-262 uncovered. That is a model-coverage gap, not a structural boundary: the same
  region is continuously part of the cryo-EM-resolved trunk, and §4 below notes the Pfam
  coverage caveat in general.

A first pass of this analysis read the absence of a covering Pfam domain and a covering
UniProt feature as evidence that the residue is outside the solenoid. That was an
over-reading of an absence: neither database annotates inter-helical loops, and the PDBe
coverage check — added afterwards, and now part of the script — settles it directly. The
2011 claim is confirmed, not qualified.

Two further points make the conclusion independent of where exactly the tripeptide sits:

* the validated W-box consensus is `PWxxW`, and **`PWxxW` is absent from AP5B1** (and from
  all four controls). A bare `WDW` tripeptide is not a W-box.
* the biochemistry is independent of the sequence argument entirely: beta-5 is not enriched
  in — or even detectable in — the clathrin-coated-vesicle fraction, and tagged AP-5 does not
  colocalise with clathrin heavy chain (PMID:22022230).

### 4. Hinge: AP5B1 has the shortest trunk-to-appendage linker of the five

Taking the trunk as the longest Pfam domain and measuring to the next domain C-terminal to
it:

| Protein | trunk | next domain | linker length |
|---|---|---|---|
| **AP5B1** | PF21588 (263-627) | PF21589 | **62 aa** |
| AP1B1 | PF01602 (12-533) | PF02883 | 187 aa |
| AP2B1 | PF01602 (12-533) | PF02883 | 178 aa |
| AP3B1 | PF01602 (44-581) | PF14797 | 90 aa |
| AP4B1 | PF01602 (11-522) | PF09066 | 99 aa |

AP5B1's is the shortest, and by a factor of ~3 against the two clathrin-dependent beta
subunits. This confirms the fourth claim. Two independent checks from different sources agree
on where the AP5B1 trunk ends, both emitted by the run: the UniProt secondary-structure
features derived from PDB 8YAB span residues 10-629, and the modelled range of 8YAB chain B
itself ends at 631 — against PF21588 ending at 627.

**Caveat, stated rather than buried:** PF21587-PF21590 were built on the AP5B1 family
itself, whereas PF01602 (Adaptin_N) is a pan-family model, so the boundary calls are not
derived the same way in the test subject and the controls. The 62-vs-178/187 difference is
large enough to survive that asymmetry, and the cryo-EM helix range corroborates the AP5B1
boundary, but the numbers should be read as domain-model spans, not as measured disorder.

## Conclusion

AP5B1 is a beta adaptin by fold and by PSI-BLAST/HHpred assignment, but it is not a
clathrin-recruiting beta adaptin. It lacks the type-II box, the `YQW`, and the `PWxxW`
W-box outright; its single clathrin-box consensus match is buried in a folded C-terminal
domain rather than presented in a linker; and the trunk-to-appendage linker that carries
the box in AP1B1/AP2B1 is a third the length in AP5B1. This is the sequence-level
counterpart of the cell-biological result that AP-5 does not associate with clathrin, and
it is why the AP-1/AP-2 beta-subunit annotation `GO:0030276 clathrin binding` should not
be transferred to AP5B1.

Separately relevant to annotation transfer, and **not** produced by this script: AP5B1 is
not in the beta-adaptin PANTHER family. AP1B1, AP2B1, AP3B1 and AP4B1 are all `PTHR11134`
(ADAPTOR COMPLEX SUBUNIT BETA FAMILY MEMBER, 17,626 proteins); AP5B1 is the sole occupant of
`PTHR34033` (AP-5 COMPLEX SUBUNIT BETA-1, 1,227 proteins, one subfamily SF1 whose five
reviewed members are the human, mouse, rat, bovine and Xenopus AP5B1 orthologues). PAINT
therefore cannot leak AP-1/2/3/4 beta-subunit terms onto AP5B1 through the family tree.
Sources for this paragraph, all checkable in committed files or by one API call: the five
family assignments come from the UniProt `DR PANTHER` lines for each accession, and the
PTHR34033 counts and member list from `interpro/panther/PTHR34033/PTHR34033-metadata.yaml`
and `PTHR34033-entries.csv`.

# MAD2L2 (FANCV / REV7) — AIGR vs Affinage

**Affinage record:** run 2026-06-10 · 47 discoveries · self-eval `win` (faith 100%) · gates passed.

## Agreement (brief)

Affinage and the AIGR review converge on the multifunctional core biology, which the
AIGR review already captured well across 3 `core_functions` and ~79 adjudicated annotations:

- **HORMA-domain adaptor** with a multivalent "safety-belt" surface (`GO:0030674`
  protein-macromolecule adaptor activity).
- **Pol zeta accessory subunit / translesion synthesis** — bridges catalytic REV3L with REV1;
  requires REV7 dimerization (`GO:0016035` zeta DNA polymerase complex; `GO:0019985` /
  `GO:0042276` TLS).
- **Shieldin component** (SHLD1/2/3–REV7) downstream of 53BP1–RIF1, suppressing 5′ end
  resection to enforce NHEJ over HR (`GO:2001034` +NHEJ, `GO:2000042` −HR, `GO:0035861`
  site of DSB); telomere fusion and CSR roles included.
- **APC/C inhibition** via direct binding to activators CDH1 and CDC20 (`GO:1904667`
  −Ub-ligase activity, `GO:0005680` APC/C, `GO:0051301` cell division).
- **FANCV / Fanconi anemia** identity; nuclear localization; secondary transcription
  (TCF4/Wnt, ELK1–JNK) and EMT roles, correctly demoted by AIGR to `KEEP_AS_NON_CORE`.

The large majority of Affinage's 47 PMIDs were already cited/adjudicated in the AIGR
review (Pol zeta: 20164194, 22828282, 23143872, 11485998; shieldin: 29656893, 29789392,
34354233; APC/C: 11459825, 11459826; mitotic/partner biology: 10366450, 11717438, 17296730,
17541814, 17719540, 19443654, 21063390; TLS/DDR: 15988022, 24449906).

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| MF GO grounding | `mechanism_profile` gives coarse parents: `GO:0060090` molecular adaptor, `GO:0098772` molecular function regulator, `GO:0003677` DNA binding | Specific `GO:0030674` adaptor activity split across the TLS, shieldin, and APC/C roles | **AIGR right.** Affinage's own note flags the profile as coarse. `GO:0003677` DNA binding is not supported — REV7 has no known direct sequence-specific DNA-binding activity; it acts through protein partners. Do not import. |
| Localization grounding | `GO:0005634` nucleus + `GO:0000228` nuclear chromosome | nucleus/nucleoplasm + `GO:0035861` site of DSB / `GO:0090734` site of DNA damage / `GO:0005819` spindle | **AIGR right/finer.** AIGR's damage-site and complex-specific CC terms are more informative than the generic `GO:0000228`. |
| Pathway layer | Reactome DNA Repair, DNA Replication, Cell Cycle, Disease | process terms grounded per-annotation | **AIGR right.** The Reactome buckets are over-general parents; AIGR's per-annotation BP terms carry the actual biology. |
| APC/C inhibition | central mitotic-control finding (PMID:11459825/11459826) | ACCEPTED as core (−Ub ligase / APC/C / cell division) | **Agreement.** Both correct; no conflict. |
| Replication fork protection (PMID:36075897) | listed as a 2022 High-confidence finding — shieldin-independent, REV3L/REV1-dependent fork protection limiting MRE11 resection | **absent** | **Affinage surfaced a real gap.** Well-evidenced, MAD2L2-focused Nat Commun study; **incorporated** as a NEW `GO:0110027` annotation (see below). |
| FANCV / Fanconi anemia (PMID:27500492) | stated as disease identity | asserted in `description` but **uncited** anywhere in the review | **Affinage right that it needs a citation.** The FANCV claim had no supporting reference; **incorporated** PMID:27500492 onto the DNA-repair annotation. |
| Germ-cell / PGC maintenance, TRIP13/p31comet disassembly, CHAMP1 competition, p53 signaling (24356953, 23463509, 24009519, 31915374, 33051298, 36044844, 38557443, 38515112) | folded into the narrative | absent or only implicitly covered | **AIGR defensibly conservative.** Mostly mouse PGC biology, mechanism-of-regulation, or single-group recent human findings; real but peripheral to the human core functions. Noted, not imported. |

No factual conflict forces an AIGR reversal. The GO-layer disagreements are the expected
coarse/over-general (and one unsupported `DNA binding`) grounding; the substantive value was
two MAD2L2-focused papers filling genuine gaps.

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| 27500492 | REV7/MAD2L2 is Fanconi anemia gene **FANCV** (biallelic inactivation, REV7-V85E; patient FA phenotype rescued by WT REV7) | Added to `references` (relevance HIGH, VERIFIED) + verbatim `supported_by` on the existing `GO:0006281` DNA repair annotation — supplies the previously-missing citation for the `description`'s FANCV claim |
| 36075897 | MAD2L2 protects/restarts stalled replication forks by limiting MRE11-dependent resection, **independent of shieldin** and requiring **REV3L/REV1** | Added to `references` (relevance HIGH, VERIFIED) + one **NEW** annotation `GO:0110027` (negative regulation of DNA strand resection involved in replication fork processing), evidence IMP, with two verbatim `supported_by` quotes |

Both are MAD2L2-focused functional studies. The `GO:0110027` term was verified against OLS
(real, non-obsolete, `biological_process`) and is correctly branched. No existing decision was
weakened. Other Affinage-only PMIDs (25799990, 25799992, 30046110, 30111544, 30154076, 24356953,
23463509, 24009519, 31484720, 31796627, 31915374, 32499490, 33051298, 34521823, 36044844, 38557443,
38515112, 3897794, 7871890, 10366450, 10660610, 12529368, 16227619, 20088965, 23287467, 26697843,
28440919, 28887307, 29160738, 29360267, 29697047, 32811646) were reviewed and **not** incorporated:
they corroborate already-captured roles, are non-human/ortholog or mouse-developmental, describe
regulation of (not new) MAD2L2 functions, or are single-group recent findings — none altering a
curation call on the human gene.

## Net assessment

The AIGR review is the stronger artifact on GO grounding, scoping, and evidence adjudication:
Affinage's `mechanism_profile` collapses to over-general parents and even asserts an unsupported
`DNA binding` MF, so its GO layer should not be imported. Affinage's real value is its **dense,
dated, PMID-anchored narrative**, which surfaced (1) a genuine citation gap for the FANCV/Fanconi
anemia identity and (2) a well-evidenced, shieldin-independent **replication fork protection** role
(REV3L/REV1-dependent) that the review had missed — the one substantive functional addition beyond
the Pol-zeta / shieldin / APC/C triad. Both were incorporated conservatively without disturbing any
existing decision. **1 new annotation (`GO:0110027`), 2 papers incorporated, review remains ✓ Valid.**

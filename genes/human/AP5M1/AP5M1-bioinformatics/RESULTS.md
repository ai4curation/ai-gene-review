# AP5M1 (Q9H0R1) — bioinformatics support for the annotation review

Two claims in the AP-5 literature are stated but never quantified, and both bear
directly on how AP5M1 should be annotated. Each is tested here from live UniProt,
RCSB and PANTHER data. Nothing is hardcoded; delete `cache/` and re-run.

```
uv run python mu2_cargo_pocket.py   # -> mu2_cargo_pocket.tsv, mu2_cargo_pocket-output.txt
uv run python mu_alignment.py       # -> mu_alignment.fasta, mu_cargo_pocket_mapping.tsv, mu_alignment-output.txt
uv run python check_goa_reconciliation.py   # -> goa_reconciliation-output.txt
```

---

## 1. Does mu-5 retain a functional YxxPhi cargo-binding site? (`mu2_cargo_pocket.py`, `mu_alignment.py`)

**Question.** AP5M1 carries a mu-homology domain (UniProt `DOMAIN 206..476 MHD`,
PROSITE PS51072, CDD `cd09256 AP_MuD_MHD`), and in AP-1/AP-2 the MHD is the
YxxPhi sorting-signal receptor. Hirst et al. assert twice that mu-5 has lost that
site — *"The key residues in the μ subunits that bind to YXXΦ sorting signals
[21] are altered in C14orf108, suggesting that if C14orf108 is involved in cargo
recognition, it probably interacts with a different type of motif"*
(PMID:22022230) and *"the highly conserved cargo binding sites found in the other
AP complexes are absent in AP-5"* (PMID:29381698) — but neither paper names the
residues. So the claim is repeated, not checked.

**Method, part 1 — derive the pocket from the structure, not from memory.**
`mu2_cargo_pocket.py` downloads PDB **1BXX** (RCSB title: *"MU2 ADAPTIN SUBUNIT
(AP50) OF AP2 ADAPTOR (SECOND DOMAIN), COMPLEXED WITH TGN38 INTERNALIZATION
PEPTIDE DYQRLN"*), identifies the peptide chain by length and asserts it contains
the `YQRL` motif, then takes every mu2 residue with a heavy atom within **4.5 Å**
of a heavy atom of the peptide. Author numbering in 1BXX is verified
residue-by-residue against the UniProt Q96CW1 sequence (all 256 observed
residues, 159–435) before any position is reported, so the output is in Q96CW1
numbering. Result: **14 residues**, partitioning into a Tyr subsite
(F174, L175, D176, K203, W421, V422, R423) and a Phi subsite
(L175, V401, R402, Y403, L404, K420, W421, V422).

**Method, part 2 — map them.** `mu_alignment.py` builds a MAFFT L-INS-i
alignment of the five human AP mu subunits plus the mouse and *Arabidopsis*
AP5M1 orthologues (both are PTHR16082 members per
`interpro/panther/PTHR16082/PTHR16082-entries.csv`) and reads each mu2 pocket
position out of the other sequences. Positions are reported in each protein's own
numbering; every aligned sequence is asserted to de-gap back to its UniProt
sequence.

**Alignment positive control.** AP5M1 is the most divergent member of the panel
(18.0% identity to AP2M1, against 29.9% for AP4M1 and 27.2% for AP3M1), so the
alignment itself needs checking. PMID:40081374 states independently that *"a
missense affecting Tyr284 of AP4M1, [is] the corresponding amino acid residue of
Tyr313 in AP5M1"*. The alignment reproduces exactly that correspondence, and puts
a tyrosine at that column in all seven sequences (AP2M1 Y277, AP1M1 Y267, AP3M1
Y262, AP4M1 Y284, AP5M1 Y313, mouse Ap5m1 Y313, *Arabidopsis* AP5M Y399). The MHD
region of the alignment is therefore reproducing a published correspondence, not
inventing one.

**Result.**

| mu2 | AP1M1 | AP3M1 | AP4M1 | **AP5M1** | mouse Ap5m1 | subsite |
|---|---|---|---|---|---|---|
| F174 | F172 | Y180 | F188 | **S210** | S210 | Tyr |
| L175 | L173 | F181 | L189 | **I211** | I211 | Tyr + Phi |
| D176 | D174 | D182 | D190 | **S212** | S212 | Tyr |
| K203 | R201 | C209 | K217 | **K240** | K240 | Tyr |
| V401 | V392 | V389 | V421 | **A446** | A446 | Phi |
| R402 | R393 | N390 | R422 | **D447** | D447 | Phi |
| Y403 | Y394 | R391 | F423 | **Q448** | Q448 | Phi |
| L404 | L395 | L392 | L424 | **H449** | H449 | Phi |
| V418 | A405 | P401 | P436 | **K460** | K460 | — |
| I419 | L406 | F402 | H437 | **I461** | I461 | — |
| K420 | P407 | K403 | K438 | **S462** | S462 | Phi |
| W421 | W408 | G404 | W439 | **A463** | A463 | Tyr + Phi |
| V422 | V409 | V405 | V440 | **H464** | Y464 | Tyr + Phi |
| R423 | R410 | K406 | R441 | **R465** | R465 | Tyr |

AP5M1 retains **3 of 14** (K240, I461, R465). The comparators retain 11/14
(AP4M1), 10/14 (AP1M1) and 5/14 (AP3M1); the *Arabidopsis* orthologue retains
0/14.

The residues making the closest approaches to the signal tyrosine itself — F174
(3.75 Å), D176 (**2.43 Å**, the shortest contact in the whole interface), W421
(3.06 Å) — are in AP5M1 **S210, S212 and A463**: no aromatic, no acidic side
chain, no bulk, at any of the three. That pattern is unique to mu-5 in this
panel. AP4M1 and AP1M1 keep all three; even AP3M1, which like AP-4 and AP-5 works
without clathrin, keeps an aromatic (Y180) and the aspartate (D182) and loses
only the tryptophan.

**Caveat, stated rather than hidden.** AP5M1's low identity to AP2M1 means the
per-column confidence is lower here than in a closely related pair, and a
substitution count is partly a function of divergence. Two things argue the
result is not merely divergence: the correspondence in this exact region is
independently corroborated (Y313 ↔ Y284, above), and the mouse orthologue — 85.1%
identical to human AP5M1 — gives the identical answer at 13 of 14 positions.

**Conclusion.** The Hirst statements check out, and can be sharpened: it is
specifically the tyrosine-binding subsite of the MHD that mu-5 has lost. AP5M1
has an MHD fold but no evidence of a YxxPhi receptor, and no motif of any kind has
been identified for AP-5. This supports annotating AP5M1's molecular contribution
as structural/assembly within AP-5 rather than as cargo-binding, and it is the
reason no `GO:0008565 protein transporter activity`-style cargo-recognition term
is proposed in the review.

## 2. Are the reported MUDENG caspase-3 sites real aspartates in the MHD? (`mu_alignment.py`)

PMID:23665015 reports caspase-3 cleavage of MUDENG/AP5M1 at **D276** and **D290**
and places them "in the adaptin domain". Both positions are aspartate in the
canonical Q9H0R1 sequence (UniProt sequence version 2, 490 aa) and both lie
inside the annotated MHD (206–476). The sequence claim is therefore consistent;
this is recorded because the cell-death literature for this protein is otherwise
overexpression-based, and it is the one part of it that makes a checkable
statement about the protein itself.

## 3. GOA ↔ review reconciliation (`check_goa_reconciliation.py`)

Not a biological result: a mechanical check that every row of
`AP5M1-goa.tsv` maps to exactly one `existing_annotations` entry in
`AP5M1-ai-review.yaml` with identical normalised `supporting_entities`, and that
the review adds no non-`NEW` row GOA does not have. See `goa_reconciliation-output.txt`.

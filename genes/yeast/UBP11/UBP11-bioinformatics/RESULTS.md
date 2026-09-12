# UBP11 (P36026) bioinformatics analysis — USP catalytic-domain integrity

## Question

Is *S. cerevisiae* UBP11 (YKR098C) a **catalytically competent** ubiquitin-specific
protease, or a degenerate/pseudo-DUB? A competent DUB molecular-function annotation is
only defensible from the domain if the peptidase C19 (USP) catalytic residues are intact.

## Method

`analyze_ubp11.py` parses the local UniProt flat file (`../UBP11-uniprot.txt`), extracts
the protein sequence and feature table, reports the residues actually present at the two
annotated `ACT_SITE` positions, checks the peptidase C19 family declaration, and scans
for the PROSITE USP signatures. Nothing is hardcoded; run with `uv run python analyze_ubp11.py`.

## Results

| Feature | Value |
|---|---|
| Length | 717 aa |
| Declared family (UniProt SIMILARITY) | peptidase C19 family |
| Annotated USP domain | residues 298–707 (410 aa) |
| Catalytic nucleophile (ACT_SITE) | **Cys307** — present (context `NPC**C**NTC…`, canonical Cys box) |
| Catalytic proton acceptor (ACT_SITE) | **His649** — present (context `NLING**H**YTSVV…`, His box) |

Both members of the catalytic dyad expected for a USP/peptidase-C19 cysteine protease
(nucleophilic Cys + proton-acceptor His) are **present at their annotated positions**.
The Cys307 sits in the recognizable Cys box motif and His649 in the His box, the two
short conserved motifs that together form the C19 active site.

### Caveats (honest limitations)

- The script's *simplified* in-house PROSITE regexes are approximate: the USP_1/Cys-box
  pattern did not produce an exact match and the USP_2/His-box pattern produced a spurious
  match upstream of the real His box. The **authoritative** signature evidence is UniProt's
  own PROSITE annotation, which lists `PS00972` (USP_1), `PS00973` (USP_2) and `PS50235`
  (USP_3 profile) as all matching. The catalytic-residue check (from UniProt `ACT_SITE`
  features) is the load-bearing result here, and it is unambiguous.
- This analysis confirms *catalytic competence by domain*; it says nothing about the
  physiological **substrate** or **linkage specificity** of UBP11, which remain unknown
  (see the gene review's knowledge gaps).

## Verdict

**Catalytically competent cysteine-type deubiquitinase by domain.** The USP catalytic
dyad (Cys307/His649) is intact within a 410-aa peptidase C19 domain, so a
`cysteine-type deubiquitinase activity` (GO:0004843) molecular function is well supported
at the domain level. This is consistent with the in vitro demonstration of ubiquitin-cleaving
activity for Ubp11p (PMID:10527495) and the family-level survey showing 14/17 yeast DUBs,
Ubp11p included, have ubiquitin-cleaving activity (PMID:11076031).

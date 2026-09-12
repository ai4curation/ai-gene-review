# knh4 (SPBC1E8.05) — S. pombe — review notes

## Identity (verified)

- **Standard name:** knh4 (PomBase); **systematic name:** SPBC1E8.05; **synonym:** gaz2.
- **UniProt:** O42970 (entry name YB95_SCHPO), "Uncharacterized serine-rich protein C1E8.05", 317 aa, Precursor (has signal peptide).
- **PomBase product:** "conserved fungal cell surface protein, Kre9/Knh1 family, Knh4"
  (queried via PomBase JSON API 2026-07-06). `name_descriptions: ['Kre9(Nine) Homolog']`
  → **KNH = Kre-Nine Homolog** (homolog of *S. cerevisiae* Kre9), NOT Knr4/Smi1.
- **Characterisation status:** "conserved unknown" (dark gene).
- **Taxonomic distribution:** fungi only. Ortholog: *S. japonicus* SJAG_03521 (PMID:21511999).
- **Deletion viability:** viable (knh4Δ is non-essential).

### IMPORTANT correction to task framing
The dispatch brief described knh4 as a "Knr4/Smi1-homology (KNH)" family protein. This is
**incorrect**. The Pfam domain `PF10342 Kre9_KNH` and InterPro `IPR018466 Kre9/Knh1-like_N`
refer to the **Kre9/Knh1** family (β-1,6-glucan cell-wall assembly), and PomBase's
`name_descriptions` explicitly reads "Kre9(Nine) Homolog". Knr4/Smi1 is an entirely
different (cytoplasmic, cell-wall-synthesis-regulating) family. This review treats knh4 as a
**Kre9/Knh1-family cell-surface glycoprotein**. Paralogs are therefore the *S. pombe* Kre9/Knh1
family members (the essential Kre9 ortholog + other non-essential Knh/gaz paralogs), NOT knr4.

## Domain / sequence features (from knh4-uniprot.txt, inline)

- SIGNAL 1..16 (ECO:0000255) → secreted/cell-surface.
- CHAIN 17..317 mature protein.
- InterPro IPR018466 "Kre9/Knh1-like_N"; Pfam PF10342 "Kre9_KNH" (one copy, N-terminal).
- PANTHER PTHR40633 "SRP1/TIP1-like Cell Wall Component"; subfamily SF1
  "GPI ANCHORED SERINE-THREONINE RICH PROTEIN".
- REGION 150..259 Disordered; COMPBIAS 150..238 + 247..259 Low complexity — long
  Ser/Thr-rich low-complexity tract (classic cell-wall O-glycoprotein architecture).
- CARBOHYD 42 N-linked (predicted). KW: Glycoprotein; Signal.
- C-terminus (…LKTGINALVAVGVVSAIALFL) is hydrophobic — consistent with a GPI-anchor
  signal (the protein is experimentally treated as GPI-anchored, see PMID:34738170).

Interpretation: a secreted, heavily O-/N-glycosylated, GPI-anchored cell-surface protein with
a single N-terminal Kre9/Knh1 fold and a long Ser-rich disordered stalk. This is a
**non-catalytic scaffold** architecture (the Kre9/Knh1 family has no known enzymatic activity).

## KNOWN (knh4-specific evidence)

1. **GPI-anchored cell-surface protein.** Identified as one of 33 predicted *S. pombe* GPI
   proteins by a genome-wide GPI-consensus screen [PMID:12845604 "only 33 GPI candidates were
   identified"]. UniProt: signal peptide + hydrophobic C-terminus + Glycoprotein keyword.
   PomBase CC: GO:0009986 cell surface (TAS, PMID:12845604).
2. **Non-enzymatic support of cell-surface β-glucan.** In a genome-wide screen for suppressors
   of the growth defect of N-glycosylation-defective *och1Δ* cells, SPBC1E8.05 (with pwp1+) was
   identified as a high-copy suppressor; both encode GPI-anchored proteins. Deletion analysis:
   [PMID:34738170 "neither gene was essential for cell viability; however, both mutants were
   sensitive β-glucanase, suggesting that Pwp1p and the protein encoded by SPBC1E8.05
   non-enzymatically support β-glucan on the cell-surface of S. pombe"]. This is the single
   most direct functional statement about knh4. → FYPO:0001190 "sensitive to cell wall-degrading
   enzymes" for knh4Δ (cell growth assay, PMID:34738170).
3. **Non-essential.** knh4Δ is viable (Bioneer genome-wide deletion set, PMID:20473289; and
   PMID:34738170). Many other large-scale phenotypes exist (salt/detergent/oxidant
   sensitivities, nitrogen-source growth) but these are pleiotropic high-throughput screen hits,
   not mechanistic.

## NOT known / knowledge gaps (honest)

- **Molecular activity is unknown.** Kre9/Knh1-family proteins are non-catalytic; whether knh4
  binds, cross-links, or scaffolds β-1,6-glucan (the proposed S. cerevisiae Kre9/Knh1 role) has
  not been shown biochemically for knh4. UniProt MF = ND.
- **Specific pathway role vs the essential family member.** The essential *S. pombe* Kre9
  ortholog carries the core β-1,6-glucan-formation function; knh4 is one of several apparently
  redundant non-essential paralogs. knh4's individual contribution is not resolved.
- **Redundancy.** knh4Δ single mutant is viable with only mild cell-wall phenotypes → strong
  functional redundancy among the Kre9/Knh1 paralogs is likely but not directly tested for knh4.
- **In-vivo β-glucan role.** The β-glucanase sensitivity implies a cell-wall β-glucan support
  role, but direct biochemical demonstration (β-glucan quantity/structure in knh4Δ) is lacking.

## Family biology (context, S. cerevisiae / general — NOT knh4-specific)

- S. cerevisiae Kre9p and its homolog Knh1p are cell-surface O-glycoproteins required for
  β-1,6-glucan synthesis/assembly (cross-linking β-1,6-glucan into the wall); kre9Δ knh1Δ is
  synthetically lethal (WebSearch, PubMed:8810042 KNH1 paper; general reviews). KRE9 is the major
  gene, KNH1 redundant. Used here only as family context, not as knh4 evidence.

## GO annotations to review (from goa.tsv)

1. GO:0003674 molecular_function (ND, GO_REF:0000015) — root, no data.
2. GO:0008150 biological_process (ND, GO_REF:0000015) — root, no data.
3. GO:0009986 cell surface (TAS, PMID:12845604) — GPI-protein prediction; defensible.

## Candidate GO terms (OLS4-verified)

- BP: GO:0006077 (1->6)-beta-D-glucan metabolic process; GO:0006078 biosynthetic process;
  GO:0031505 fungal-type cell wall organization; GO:0071554 cell wall organization.
- CC: GO:0009986 cell surface (existing); GO:0009277 fungal-type cell wall.
- Note: GPI "anchored component of membrane" GO terms (GO:0031225/GO:0046658) are OBSOLETE
  (topology, not a component) — do not use.

## Deep research status
Automated deep research FAILED: `deep-research-falcon` hits the python3.9 `dict | None` bug;
the `deep_research_wrapper.py` uv path errored on template variables (`Missing template
variables: gene_info, ...`) and the perplexity-lite fallback returned HTTP 401 (quota
exhausted). Per project policy I did NOT fabricate a `-deep-research-<provider>.md` file.
This review is grounded in UniProt (O42970), PomBase (SPBC1E8.05 JSON API), GOA, OLS4, and the
cached primary literature (PMID:34738170, 12845604, 20473289, 21511999) plus web/PubMed family
context.

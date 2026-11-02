# C18orf32 (Q8TCD1) notes

## 2026-10-08 review session (MICROPROTEINS Tier 2)

Gene: C18orf32, UPF0729 protein, 76 aa, PE1 (protein level), HGNC protein-coding, MANE
NM_001035005.4. Canonical-ORF small protein (not an alternative-ORF peptide), so the
standard `genes/human/C18orf32/` folder is correct. Domain: Pfam DUF4512 (PF14975),
PANTHER PTHR13456 (UPF0729). N-terminal hydrophobic region (1-37), C-terminal disordered
region (46-76).

### Literature found (PubMed esearch "C18orf32": 5 hits; plus GPI screen)

- PMID:12761501 (Matsuda 2003, abstract only): genome-scale overexpression screen of
  150,000 cDNAs in HEK293 with an NF-kB luciferase reporter; source of the "putative
  NF-kappa-B-activating protein" name and the HMP row. No follow-up on C18orf32 in the
  abstract [PMID:12761501 "we identified 299 cDNAs that activate the NF-kappaB pathway"].
- PMID:23864651 (Huang 2013): MYTH screen with GLP-1R bait; C18orf32 not named in the
  cached text (likely in a supplementary interactor table). Source of IPI GLP1R row.
- PMID:29275994 (Bersuker 2018, full text): APEX2 proximity labelling of LD proteome.
  Key points:
  - ER under basal conditions, redistributes to LDs with oleate [PMID:29275994 "In the
    absence of oleate, GFP-tagged c18orf32 was present in the ER (Figure S7A)"].
  - Endogenous protein on LDs, antibody validated by KO [PMID:29275994 "Endogenous
    c18orf32 was distributed in puncta most apparent at the periphery of LD clusters,
    confirming that the localization of c18orf32 at LDs is not an artifact of
    overexpression"].
  - N-terminal hydrophobic domain necessary and sufficient for ER/LD targeting.
  - Constitutively degraded by gp78 (AMFR)/derlin-1 ERAD, VCP- and proteasome-dependent;
    DERL1 and AMFR co-purify [PMID:29275994 "Affinity purification revealed that
    c18orf32-S interacts with both derlin-1 and gp78"]. These are the IPI rows: they reflect
    C18orf32 being an ERAD substrate, not an MF of C18orf32.
  - KO had no LD phenotype [PMID:29275994 "Deletion of c18orf32 did not significantly alter
    the LD distribution after oleate treatment or starvation"]; minor lipidomic changes.
- PMID:29255114 (Liu 2018, JCB, full text; found via PubMed): haploid screen for factors
  needed for GPI-inositol deacylation by PGAP1 identified C18orf32 among 7 genes; KO gives
  partial PIPLC resistance [PMID:29255114 "Their KO caused partial resistance of GPI-APs
  against PIPLC, suggesting that they were required for efficient GPI-inositol
  deacylation."]. Molecular function unknown [PMID:29255114 "C18orf32 is a small protein
  with 76 amino acids, and its molecular function has not been reported."]. PGAP1
  expression/stability/localization unchanged in KO cells (Fig 3).
- PMID:35107634 (Salian 2022, abstract only): homozygous c.90dupC (p.Phe31Leufs*3) in two
  siblings with neurodevelopmental disorder (GPIBD25); KO HEK293 PIPLC-resistance rescued by
  WT but not mutant cDNA; mutant protein in ER and nuclear aggregates. Source of the EXP ER
  row (abstract says the mutant was in ER; WT localization presumably in full text).
- PMID:41351175 (Kumar 2025, Cell Commun Signal, full text): single-group study claiming
  C18orf32 on SEC22B-positive secretory autophagosomes, binding SEC22B via its C-terminus,
  and required for LD secretion; liver knockdown causes steatosis. Interesting but
  unreplicated; much of the binding evidence is docking/in vitro affinity; Fig 1E is a GO
  enrichment of interactors. Not used for NEW annotations.
- PMID:41218492 (chimeric RNA RPL17-C18orf32) and PMID:37438770 (blood transcriptome),
  PMID:27833855 (KLHL23 readthrough): not about the C18orf32 protein's function; not cited.

### Assessment

- Locations ER and LD: well supported by two independent groups (IDA, EXP); ACCEPT all
  five CC rows.
- Protein binding x3: REMOVE (bare protein binding). DERL1/AMFR binding reflects the
  protein being an ERAD client; GLP1R is a MYTH hit with a hydrophobic segment.
- NF-kB HMP: overexpression reporter hit from a genome-scale screen; no follow-up in
  23 years; MARK_AS_OVER_ANNOTATED.
- GPI anchor: the KO phenotype (partial PIPLC resistance; rescue) shows necessity for
  efficient PGAP1-mediated inositol deacylation, but nothing says what C18orf32 does.
  PGAP1 performs the deacylation. Per the participation test, no NEW BP is proposed;
  raised as a question. No MF term fits.

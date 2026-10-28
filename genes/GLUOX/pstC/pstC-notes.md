# pstC (GOX0706, UniProtKB:Q5FT13) — Gluconobacter oxydans 621H

## Identity

- UniProtKB:Q5FT13 (Q5FT13_GLUOX), TrEMBL, 326 aa, ordered locus GOX0706, reference
  proteome UP000006375, NCBITaxon:290633 (G. oxydans strain 621H).
- Name assigned by rule: `DE RecName: Full=Phosphate transport system permease protein
  {ECO:0000256|RuleBase:RU363054}`. RuleBase is a curated UniRule system, so the family
  call is well grounded although the entry is unreviewed (`PE 3: Inferred from homology`).
- Signatures: NCBIfam TIGR02138 (phosphate_pstC); InterPro IPR011864 (Phosphate ABC
  transporter, permease protein PstC), IPR000515 (MetI-like ABC transporter type-1
  transmembrane domain), IPR035906 (MetI-like superfamily); Pfam PF00528 (BPD_transp_1);
  PROSITE PS50928 (ABC_TM1, `FT DOMAIN 88..318`); CDD cd06261 TM_PBP2; PANTHER
  PTHR30425:SF1 PHOSPHATE TRANSPORT SYSTEM PERMEASE PROTEIN PSTC.
- The subfamily call is specific (TIGR02138 and IPR011864 are PstC, not the paralogous
  PstA), which is what justifies treating this as the PstC half of the translocation pore
  rather than a generic MetI-like permease.

## Function and topology

- [file:GLUOX/pstC/pstC-uniprot.txt "Part of the binding protein-dependent transport system for
  phosphate; probably responsible for the translocation of the substrate across the
  membrane."] (`CC FUNCTION`, ECO:0000256|RuleBase:RU363054)
- [file:GLUOX/pstC/pstC-uniprot.txt "SUBCELLULAR LOCATION: Cell inner membrane"] with
  `Multi-pass membrane protein` (`CC SUBCELLULAR LOCATION`, RuleBase).
- Six PROSITE-ProRule/RuleBase transmembrane helices are annotated (34..62, 82..114,
  121..152, 172..195, 256..275, 295..318), the canonical MetI-like fold of an ABC-importer
  permease.
- [PMID:40425722 "The Pst phosphate-specific transport system is a transmembrane protein
  complex located in the bacterial inner membrane. The transmembrane sub-units PstA and
  PstC bind to the periplasmic phosphate-binding protein, PstS, and to the cytoplasmic
  signaling protein, PstB"]

PstC is therefore one of the two transmembrane subunits of the PstSCAB ABC importer: it
forms part of the translocation pathway, but the transport reaction is a property of the
assembled complex (PstS delivers Pi; PstB hydrolyses ATP). The review records that as
`contributes_to` the complex-level activity rather than as an independently enabled
transporter activity, following the subunit convention used for `genes/PSEPK/ureA`.

## InterPro2GO defect: GO:0005315 is on the wrong branch

The current InterPro2GO mapping file maps the PstC family to a **secondary active**
transporter term:

```
InterPro:IPR011864 Phosphate ABC transporter, permease protein PstC > GO:phosphate transmembrane transporter activity ; GO:0005315
```

GO:0005315 "phosphate transmembrane transporter activity" is a direct child of GO:0015291
secondary active transmembrane transporter activity, and its definition says transport "is
driven by a chemiosmotic source of energy. Secondary active transporters include symporters
and antiporters" (verified via OLS). PstSCAB is an ABC importer: primary active, ATP-driven.
The correct term is GO:0015415 "ATPase-coupled phosphate ion transmembrane transporter
activity" (`ATP + H2O + phosphate(out) = ADP + phosphate + phosphate(in)`), which is under
GO:0042626 / GO:0015399, **not** under GO:0005315 — so this is a wrong-branch mapping, not an
over-general one. Recorded as a `review.source_defects` entry (resource OTHER = InterPro,
slot `interpro2go`, `WRONG_TERM`/`REPOINT`), and the row is `MODIFY`-ed to GO:0015415.

The same file maps IPR011864 to GO:0006817 phosphate ion transport (correct but more general
than GO:0035435, which the evidence supports) and to GO:0016020 membrane (true, but entailed
by the accepted GO:0005886 plasma membrane row).

## Bioleaching context (not annotated)

Transposon disruption of `pstC` in *G. oxydans B58* gives the most acidic biolixiviant of the
whole knockout collection and improved REE extraction:

- [PMID:34795278 "The most acidic biolixiviant was produced by a disruption in the phosphate
  transport gene δpstC at pH 2.09. In fact, 4 of the 11 mutant strains that produced a more
  acidic biolixiviant were disrupted in genes involved in the phosphate-specific transport
  system (δpstA, δpstB, δpstC, and δpstS)."]
- [PMID:34795278 "Under phosphate-limiting conditions, the PstSCAB phosphate transporter will
  activate the histidine kinase PhoR, which in turn phosphorylates the transcription factor
  PhoB and activates the pho regulon, enabling phosphate solubilization and uptake"]
- [PMID:34795278 "We speculate that by disrupting pstSCAB or PhoR, we prevent G. oxydans from
  sensing when there is adequate phosphate in its environment and when to stop producing
  biolixiviants."]
- A clean deletion was less acidic than the transposon disruption
  [PMID:40425722 "ΔpstC did not produce additional bioleaching improvement."], so even the
  direction of the effect is not a simple loss-of-function readout.

No GO annotation is derived from this. The work is in strain B58 (locus tags `GO_nnnn`), not
in 621H whose GOX0706 product is reviewed here; and the phenotype is necessity/derepression
evidence — removing a transporter removes a repressive input to the Pho regulon. Under the
CLAUDE.md `NEW` bar, the entity that performs the regulatory step is PhoR/PhoB, and the
entity that performs acidification is the PQQ-dependent membrane glucose dehydrogenase, so
neither a regulation-of-acidification term nor a bioleaching term is proposed for PstC. It is
raised in `suggested_questions`/`suggested_experiments` instead.

## Notes on the sources (not source defects)

- [PMID:40425722] calls PstB "the cytoplasmic signaling protein" and, in the introduction,
  says "pstS, which encodes a phosphate signaling protein; and pstC, pstA, and pstB, which
  encode an ABC-type phosphate transporter". PstB is the ABC ATPase and PstS the periplasmic
  substrate-binding protein; signalling is a property of the assembled PstSCAB–PhoU–PhoR
  system. Prose looseness in the publication, not a database defect.
- CMMMech `data/records/allanite-concentrate.yaml` describes Q5FT13 as "Phosphate ABC
  transporter permease subunit PstC (GOX0706) disrupted in engineered Gluconobacter oxydans
  strains to derepress acidogenesis". The subunit identity is well supported; "to derepress
  acidogenesis" is a mechanistic inference from B58 disruption phenotypes that the engineered
  strains do not isolate (CMMMech's own `supports: partial` and its note on the Figure S2 /
  main-text pstS label discrepancy capture this). The strain used for the allanite work in
  Schmitz et al. (2025) was ΔpstS, not ΔpstC. No edit was made to CMMMech.

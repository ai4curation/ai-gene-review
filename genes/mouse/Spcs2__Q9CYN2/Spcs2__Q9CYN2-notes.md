# Spcs2 (mouse, Q9CYN2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: canonical Swiss-Prot product Q9CYN2 (SPCS2_MOUSE, 226 aa, Ensembl canonical
Spcs2-201, MGI:1913874). The folder `genes/mouse/Spcs2/` is keyed to the 74-aa
alternative-transcript fragment A0A140LHW5; this folder reviews the full-length
protein in its own right. No ProtNLM2 files or prediction-evidence folders were
opened.

### Deep research

`just deep-research-falcon mouse Spcs2__Q9CYN2 --fallback perplexity-lite` failed:
falcon returned "Exception: Failed to authenticate" and the perplexity-lite fallback
returned HTTP 401 (insufficient quota). No deep-research file exists. The review
uses the cached literature read directly (below) and the UniProt record.

### Evolutionary grounding

- Q9CYN2 is in PANTHER PTHR13085:SF0 "SIGNAL PEPTIDASE COMPLEX SUBUNIT 2", the same
  subfamily as human Q15005 (SPCS2), dog Q28250 (SPCS2) and yeast Q04969 (Spc2)
  (`interpro/panther/PTHR13085/PTHR13085-entries.csv`). There is a single SF for the
  characterised members, so no subfamily-specific divergence is at issue.
- PAINT node PTN000317824 (taxon:2759, Eukaryota) carries three IBD terms
  (`interpro/panther/PTHR13085/PTHR13085-paint.tsv`):
  GO:0005787 signal peptidase complex (seeds SGD Spc2, human Q15005, dog Q28250),
  GO:0045047 protein targeting to ER (seed SGD Spc2 only),
  GO:0051604 protein maturation (seeds SGD Spc2, human Q15005; dated 2026-05-29,
  apparently the re-placement after GO obsoleted GO:0006465 signal peptide processing).
- PAINT did NOT propagate yeast Spc2's SGD IMP `contributes_to` GO:0008233 peptidase
  activity (PMID:10921929). Treated as a deliberate omission: no MF annotation is
  proposed as NEW here.
- Mouse Spcs2 is 1:1 with human SPCS2 (CTD 9789; same 226-aa length, MGI orthology).

### What is experimentally established IN MOUSE

Essentially nothing functional. UniProt PE=1 rests on large-scale proteomics only:
initiator Met removal and N-acetyl-Ala2 in brain postsynaptic density preparations
(PMID:16452087) and tissue-atlas MS (PMID:21183079). There are no mouse IDA/IMP/IPI GO
annotations. Every function below is inferred from orthologs within PTHR13085:SF0.

### Evidence from orthologs (all in PTHR13085:SF0)

- Mammalian (canine microsome) topology: SPC25 spans the membrane twice with both
  termini cytosolic and essentially no lumenal domain, so it is unlikely to be
  catalytic [PMID:8632014 "Both polypeptides span the membrane twice with their N and C termini facing the cytosol and contain only very small, if any, lumenal domains"].
- Human SPC cryo-EM (two paralogs, SEC11A or SEC11C + SPCS1/2/3): a transmembrane
  window built by all subunits thins the bilayer and sets h-region length specificity
  [PMID:34388369 "a transmembrane window collectively formed by all subunits locally thins the bilayer"].
- Human SPC with bound signal peptide (Nat Commun 2026, full text): SPCS2 is not a
  main contact for the SP h-region; cross-linking places SPCS2 near Sec61beta, which
  would position the SPC next to the Sec61alpha lateral gate
  [PMID:42173868 "The TM helix of SPCS2 displays a limited set of contacts"].
- Yeast Spc2: nonessential, but needed for signal peptidase activity at high temperature;
  synthetic lethal with sec11 [PMID:8910564 "Spc2p, but not Spc1p, is important for signal peptidase activity and cell viability at high temperatures"].
  Depletion lowers SPC activity in vitro and destabilises Spc1/Sec11/Spc3; Spc2
  associates with Sbh1/Sbh2 (Sec61/Ssh1 beta subunits) [PMID:10921929].
  Spc2 loss impairs substrate discrimination and cleavage-site choice, and reduces
  membrane thinning in MD [PMID:39565596].

### Decisions

- GO:0005787 signal peptidase complex (IBA, IEA, ISO): ACCEPT, core.
- GO:0005789 ER membrane (IEA, ISO, ISS): ACCEPT, core.
- GO:0016020 membrane (IEA InterPro): MODIFY to GO:0005789 (already on the gene).
- GO:0016485 protein processing (IEA, ISO from human IDA): ACCEPT. SPCS2 passes the
  participation test as a structural contributor to the cleaving complex (membrane
  window, stabilisation of Sec11), not as a substrate.
- GO:0051604 protein maturation (IBA, IEA): MODIFY to GO:0016485 (descendant already
  on the gene). Not removed; the claim is true but broad.
- GO:0045047 protein targeting to ER (IBA, seed SGD IMP/IGI/IPI from PMID:8910564):
  MARK_AS_OVER_ANNOTATED. The SPC acts on chains already targeted to and translocating
  across the ER membrane; it does not direct proteins to the ER. Not REMOVE, out of
  deference to the experimental SGD seed and the PAINT placement; the defensible
  process is protein processing.
- No NEW annotations. Downstream phenotypes are not annotated.

### Open points

- Whether mammalian SPCS2 is required for SPC assembly/stability in vivo (as Spc2 is
  for Spc1 in yeast) has not been tested in mouse.

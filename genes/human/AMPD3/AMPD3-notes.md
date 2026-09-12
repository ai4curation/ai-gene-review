# AMPD3 (human) review notes

UniProtKB: Q01432 | HGNC:470 | Gene: AMPD3 | AMP deaminase 3 (erythrocyte isoform, "isoform E")

## Core biology

AMPD3 is the erythrocyte isoform of AMP deaminase (EC 3.5.4.6). It catalyses the
hydrolytic deamination of AMP:

  AMP + H2O + H+ = IMP + NH4+   (Rhea:RHEA:14777)
  [AMPD3-uniprot.txt CATALYTIC ACTIVITY; ECO:0000269|PubMed:9291127]

It is a zinc metalloenzyme (binds 1 Zn2+ per subunit, catalytic) and functions as a
homotetramer [AMPD3-uniprot.txt COFACTOR + SUBUNIT]. It belongs to the
metallo-dependent hydrolases superfamily, adenosine and AMP deaminases family
[AMPD3-uniprot.txt SIMILARITY].

Three human AMPD isoforms exist: E (AMPD3, erythrocyte / broadly expressed), L (AMPD2)
and M (AMPD1, muscle). All are cytosolic tetramers with qualitatively the same catalytic
activity [reactome R-HSA-76590 summary "Cytosolic AMP deaminase (AMPD) catalyzes the
hydrolysis of AMP to yield IMP and ammonia. Three isoforms of AMPD, E, L, and M ... All
occur as tetramers and all have qualitatively the same catalytic activity"].

## Physiological role

In red blood cells AMP deaminase regulates the adenylate energy charge and the
adenine-nucleotide pool by draining AMP to IMP (+ NH3), pulling the myokinase/adenylate
kinase equilibrium (2 ADP <=> ATP + AMP) and thus keeping ATP/ADP high while lowering the
total adenine-nucleotide pool. UniProt FUNCTION: "AMP deaminase plays a critical role in
energy metabolism" [ECO:0000305|PubMed:9291127].

## Disease: AMPDDE (erythrocyte AMP deaminase deficiency), MIM:612874

Benign / clinically asymptomatic. UniProt DISEASE: "A metabolic disorder due to lack of
activity of the erythrocyte isoform of AMP deaminase. It is a clinically asymptomatic
condition characterized by a 50% increase in steady-state levels of ATP in affected
cells. Individuals with complete deficiency of erythrocyte AMP deaminase are healthy and
have no hematologic disorders." Multiple loss-of-function missense variants documented
(e.g. R573C, enzyme inactive) [PubMed:8004104, 7881427, 9598089, 11139257].

## Pathway placement

UniProt PATHWAY: "Purine metabolism; IMP biosynthesis via salvage pathway; IMP from AMP:
step 1/1." UniPathway UPA00591 / UER00663. So the AMP->IMP deamination is the single step
of the salvage arm that regenerates IMP from AMP. Reactome places AMPD3 in "Purine
salvage" (R-HSA-74217) and in the R-HSA-76590 reaction.

## Reference notes

- PMID:9291127 (Mahnke-Zizelman et al. 1997, Biochem J): abstract-only in cache
  (full_text_available: false). Titled for *rat* AMPD3 isoform C, but the abstract
  explicitly establishes cross-species homology: "baculoviral expression of rat and human
  AMPD3 proteins produces enzymes that are chromatographically and kinetically similar
  ... rat isoform C and human isoform E are homologous cross-species AMPD3 proteins." This
  is the UniProt FUNCTION / CATALYTIC ACTIVITY / PATHWAY reference for human AMPD3
  (ECO:0000269 / ECO:0000305|PubMed:9291127). It is the source for the two TAS annotations
  (GO:0003876, GO:0006196). Treat as supporting human AMPD3 MF + AMP catabolism.

- PMID:25910212 (Sahni et al. 2015, Cell): systematic "edgotyping" interactome study. It
  is the IntAct source (WITH UniProtKB:P08238 = HSP90AB1) for the IPI "protein binding"
  annotation. UniProt INTERACTION lists Q01432-P08238 (HSP90AB1) NbExp=2. This is a
  chaperone/QC interaction from a high-throughput screen, not an informative molecular
  function -> MARK_AS_OVER_ANNOTATED (bare protein binding; do not REMOVE per policy).

## Localization

Cytosol (GO:0005829) is correct and is the IBA/Reactome-supported location for AMPD3
[uniprot GO line "C:cytosol; IBA:GO_Central"; reactome R-HSA-76590 "Cytosolic AMP
deaminase"].

The extracellular-region / secretory-granule-lumen / ficolin-1-rich-granule-lumen
annotations (GO:0005576, GO:0034774, GO:1904813) all derive from Reactome neutrophil
degranulation proteomics (R-HSA-6798748 "Exocytosis of secretory granule lumen proteins",
R-HSA-6800434 "Exocytosis of ficolin-rich granule lumen proteins"). These are bulk
granule-proteome catalog memberships, not evidence of a bona fide secreted / granule
function for a cytosolic purine-metabolism enzyme -> MARK_AS_OVER_ANNOTATED.

## Annotation-by-annotation plan (GOA)

1. GO:0003876 AMP deaminase activity, IBA -> ACCEPT (core MF)
2. GO:0006188 IMP biosynthetic process, IBA -> MODIFY (AMPD makes IMP by *deamination/catabolism*
   of AMP, not de novo IMP biosynthesis; better = GO:0006196 AMP catabolic process). Keep essence.
3. GO:0046033 AMP metabolic process, IBA -> ACCEPT (broad but correct)
4. GO:0003876 AMP deaminase activity, IEA (GO_REF:0000120) -> ACCEPT (dup of core MF)
5. GO:0006753 nucleoside phosphate metabolic process, IEA (ARBA) -> ACCEPT (broad, correct)
6. GO:0009168 purine ribonucleoside monophosphate biosynthetic process, IEA InterPro -> MODIFY
   (same "biosynthetic" mis-framing; better GO:0006196 AMP catabolic process)
7. GO:0019239 deaminase activity, IEA InterPro -> ACCEPT (broad parent of core MF)
8. GO:0032264 IMP salvage, IEA (UniPathway) -> ACCEPT (matches UniProt PATHWAY: IMP biosynthesis
   via salvage; AMP->IMP is the salvage step regenerating IMP)
9. GO:0005515 protein binding, IPI (PMID:25910212, HSP90AB1) -> MARK_AS_OVER_ANNOTATED (bare)
10. GO:0006196 AMP catabolic process, IEA (Ensembl) -> ACCEPT (core BP)
11. GO:0034101 erythrocyte homeostasis, IEA (Ensembl ortholog) -> KEEP_AS_NON_CORE (RBC context,
    but not the molecular core function; AMPD3 deficiency is benign so it is not required for
    erythrocyte homeostasis)
12. GO:0046031 ADP metabolic process, IEA (Ensembl) -> MARK_AS_OVER_ANNOTATED (AMPD3 acts on AMP,
    not ADP; ortholog electronic over-propagation of a broad energy-metabolism grouping)
13. GO:0046032 ADP catabolic process, IEA (Ensembl) -> MARK_AS_OVER_ANNOTATED (not an ADP enzyme)
14. GO:0046033 AMP metabolic process, IEA (Ensembl) -> ACCEPT (dup, correct)
15. GO:0046034 ATP metabolic process, IEA (Ensembl) -> MARK_AS_OVER_ANNOTATED (indirect at best)
16. GO:0046039 GTP metabolic process, IEA (Ensembl) -> REMOVE (AMPD3 has no GTP activity; wrong
    electronic inference)
17. GO:0003876 AMP deaminase activity, ISS (O08739 mouse) -> ACCEPT (dup core MF)
18. GO:0005576 extracellular region, TAS Reactome -> MARK_AS_OVER_ANNOTATED (granule proteome)
19. GO:0005576 extracellular region, TAS Reactome -> MARK_AS_OVER_ANNOTATED (dup)
20. GO:0034774 secretory granule lumen, TAS Reactome -> MARK_AS_OVER_ANNOTATED
21. GO:1904813 ficolin-1-rich granule lumen, TAS Reactome -> MARK_AS_OVER_ANNOTATED
22. GO:0005829 cytosol, TAS Reactome -> ACCEPT (correct core location)
23. GO:0003876 AMP deaminase activity, TAS (PMID:9291127) -> ACCEPT (core MF, literature)
24. GO:0006196 AMP catabolic process, TAS (PMID:9291127) -> ACCEPT (core BP, literature)
</content>
</invoke>

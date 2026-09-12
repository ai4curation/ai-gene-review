# ETNK2 (Ethanolamine kinase 2) — review notes

UniProt: Q9NVF9 (EKI2_HUMAN). HGNC:25575. Gene ID 55224. Chromosome 1.
EC 2.7.1.82. 386 aa. Isoforms: 1 (canonical, Q9NVF9-1), 2 (Q9NVF9-2), 3 (Q9NVF9-3).

## Core biology (from local UniProt file)

ETNK2 is ethanolamine kinase 2, a cytosolic enzyme catalyzing the first,
committed step of the CDP-ethanolamine (Kennedy) branch of phosphatidylethanolamine
(PE) biosynthesis: it phosphorylates ethanolamine using ATP to give
phosphoethanolamine (+ ADP + H+).

- FUNCTION: "Catalyzes the ATP-dependent phosphorylation of ethanolamine to
  phosphoethanolamine (By similarity). Highly specific for ethanolamine
  phosphorylation and does not exhibit choline kinase activity (By similarity)."
  [file:human/ETNK2/ETNK2-uniprot.txt] (ECO:0000250|UniProtKB:A7MCT6 — inferred from
  the mouse ortholog A7MCT6).
- CATALYTIC ACTIVITY: "ethanolamine + ATP = phosphoethanolamine + ADP + H(+)";
  Rhea:RHEA:13069; EC=2.7.1.82. [file:human/ETNK2/ETNK2-uniprot.txt]
- PATHWAY: "Phospholipid metabolism; phosphatidylethanolamine biosynthesis;
  phosphatidylethanolamine from ethanolamine: step 1/3." (UniPathway UPA00558 /
  UER00741) [file:human/ETNK2/ETNK2-uniprot.txt]
- SIMILARITY: "Belongs to the choline/ethanolamine kinase family."
  [file:human/ETNK2/ETNK2-uniprot.txt]
- TISSUE SPECIFICITY: "Expressed in kidney, liver, ovary, testis and prostate."
  (ECO:0000269|PubMed:11044454) [file:human/ETNK2/ETNK2-uniprot.txt]. Consistent with
  HPA "Tissue enhanced (kidney, liver, testis)".

The catalytic activity, function, and pathway on the human entry are propagated by
similarity (ECO:0000250) from the mouse ortholog Etnk2 (A7MCT6). ETNK2 is
ethanolamine-specific, in contrast to ETNK1, and has a more restricted expression
pattern (liver, kidney, reproductive tissue) versus the broader ETNK1.

## Tissue-specificity / EKI2 characterization

PMID:11044454 (Lykidis, Wang, Karim, Jackowski 2001, J Biol Chem, "Overexpression of
a mammalian ethanolamine-specific kinase accelerates the CDP-ethanolamine pathway")
is the source cited by UniProt for the TISSUE SPECIFICITY statement and characterizes
the mammalian ethanolamine-specific kinase (EKI2). Cited here by title only from the
UniProt record; the full text is not in the local publications cache, so no verbatim
quote is used in the review beyond the UniProt-sourced tissue statement.

## Cellular location

- GO:0005829 cytosol — TAS from Reactome:R-HSA-1483222 ("ETA is phosphorylated to
  PETA by CHK/ETNK"). Reactome summary: "In the cytosol, ethanolamine (ETA) is
  phosphorylated to phosphoethanolamine (PETA) by choline kinase (CHK) dimer or by
  ethanolamine kinase 1/2 (ETNK1/2) (Lykidis et al. 2001, Gallego-Ortega et al.
  2009)." [reactome/R-HSA-1483222.md]
- GO:0005737 cytoplasm — IBA from GO_Central. Consistent with cytosolic localization
  but less specific than cytosol.

## Protein interactions (HuRI)

GO has six GO:0005515 "protein binding" IPI annotations, all from PMID:32296183
(Luck et al. 2020, "A reference map of the human binary protein interactome" = HuRI),
assigned by IntAct. Interactors: ATN1 (Q86V38), CYSRT1 (A8MQ03), HNRNPK (P61978-2),
KRTAP12-2 (P59991), MID2 (Q9UJV3-2), STX1A (Q16623). These same six interactions are
listed in the UniProt INTERACTION block (NbExp=3 each). HuRI is a systematic all-by-all
Y2H binary interactome screen — abstract: "we present a human 'all-by-all' reference
interactome map of human binary protein interactions, or 'HuRI'." [PMID:32296183].
These are high-throughput binary interactions with no established functional relevance
to ETNK2's enzymatic role; several partners (keratin-associated protein KRTAP12-2,
cysteine-rich tail protein CYSRT1) are common Y2H "sticky"/frequent-flier-type hits.
"protein binding" (GO:0005515) is uninformative for molecular function and these are
marked as over-annotated (not removed, per policy for IPI).

## Existing annotation inventory (from goa.tsv)

1. GO:0004305 ethanolamine kinase activity — IBA — GO_REF:0000033 — enables — ACCEPT (core MF)
2. GO:0005737 cytoplasm — IBA — GO_REF:0000033 — is_active_in — MODIFY -> cytosol (GO:0005829)
3. GO:0006646 phosphatidylethanolamine biosynthetic process — IBA — GO_REF:0000033 — involved_in — ACCEPT (core BP)
4. GO:0004305 ethanolamine kinase activity — IEA — GO_REF:0000120 — enables — ACCEPT (core MF; EC/Rhea-based)
5. GO:0005515 protein binding — IPI x6 — PMID:32296183 — enables — MARK_AS_OVER_ANNOTATED
6. GO:0006646 phosphatidylethanolamine biosynthetic process — IEA — GO_REF:0000041 (UniPathway) — involved_in — ACCEPT
7. GO:0005829 cytosol — TAS — Reactome:R-HSA-1483222 — located_in — ACCEPT (core CC)

(GOA seed collapses the six PMID:32296183 IPIs to a single "protein binding" annotation.)

## Core functions

- MF: ethanolamine kinase activity (GO:0004305) — enables
- MF: ATP binding (GO:0005524) — enables (substrate/cofactor; UniProt KW ATP-binding)
- BP: phosphatidylethanolamine biosynthetic process (GO:0006646) — involved_in
- CC: cytosol (GO:0005829)

ATP binding (GO:0005524) is not in GOA's process/component set but is present as the
UniProtKB-KW-based F:ATP binding in the UniProt DR block ("GO:0005524; F:ATP binding;
IEA:UniProtKB-KW") and is consistent with the kinase mechanism.
</content>
</invoke>

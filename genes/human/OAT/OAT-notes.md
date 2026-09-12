# OAT (Ornithine aminotransferase) — review notes

UniProt: P04181 (OAT_HUMAN). HGNC:8091. Gene on chromosome 10. EC 2.6.1.13.
MANE-Select transcript ENST00000368845.6 / NP_000265.1.

## Core biology (from local files)

OAT is the nuclear-encoded, mitochondrial-matrix, pyridoxal-5'-phosphate (PLP)-dependent
aminotransferase (class-III PLP-dependent / aminotransferase-3 family) that reversibly
transfers the delta-amino group of L-ornithine to 2-oxoglutarate (alpha-ketoglutarate),
producing L-glutamate 5-semialdehyde (which spontaneously cyclizes to
delta-1-pyrroline-5-carboxylate, P5C) and L-glutamate.

- Reaction (UniProt CATALYTIC ACTIVITY, Rhea:RHEA:25160): "L-ornithine + 2-oxoglutarate =
  L-glutamate 5-semialdehyde + L-glutamate; EC=2.6.1.13"
  [file:human/OAT/OAT-uniprot.txt].
- FUNCTION: [file:human/OAT/OAT-uniprot.txt "Catalyzes the reversible interconversion of L-ornithine and"]
  (continues "2-oxoglutarate to L-glutamate semialdehyde and L-glutamate.").
- Cofactor: pyridoxal 5'-phosphate, covalently bound as N6-(pyridoxal phosphate)lysine at
  Lys-292 (active-site Schiff base) [file:human/OAT/OAT-uniprot.txt MOD_RES 292;
  PMID:3754226 identified PLP at Lys-292].
- Pathway: "Amino-acid biosynthesis; L-proline biosynthesis; L-glutamate 5-semialdehyde
  from L-ornithine: step 1/1" (UniPathway UPA00098 / UER00358)
  [file:human/OAT/OAT-uniprot.txt].
- Quaternary structure: homohexamer [file:human/OAT/OAT-uniprot.txt "Homohexamer."];
  confirmed in PMID:23076989 ("the homoexameric enzyme ornithine-delta-aminotransferase").
- Location: mitochondrion matrix [file:human/OAT/OAT-uniprot.txt "Mitochondrion matrix"];
  IDA to mitochondrial matrix in PMID:23076989 (GOA line).
- Family: class-III PLP-dependent aminotransferase
  [file:human/OAT/OAT-uniprot.txt "Belongs to the class-III pyridoxal-phosphate-dependent"].

## Metabolic role / directionality

OAT links the ornithine pool (urea cycle / arginine metabolism) to the glutamate/proline/P5C
pool. In most tissues it operates catabolically (net ornithine -> P5C/glutamate); in the
small intestine it runs biosynthetically toward ornithine/citrulline/arginine. Physiological
directionality is annotated in both directions in UniProt (RHEA:25161 left-to-right;
RHEA:25162 right-to-left) and captured as two Reactome reactions R-HSA-70654 (forward) and
R-HSA-70666 (reverse). The tissue-enhanced expression in intestine (UniProt HPA:
"Tissue enhanced (intestine)") is consistent with the gut biosynthetic role.

## Disease

Deficiency causes gyrate atrophy of the choroid and retina (GACR; MIM:258870), an autosomal
recessive chorioretinal degeneration with hyperornithinemia, early cataract, and type II
muscle-fiber atrophy, leading to blindness. Many missense alleles characterized.

- PMID:1737786 (Brody et al. 1992): surveyed OAT alleles; "ornithine delta-aminotransferase
  is a nuclear-encoded mitochondrial matrix enzyme which catalyzes the reversible
  interconversion of ornithine and alpha-ketoglutarate to glutamate semialdehyde and
  glutamate"; site-directed mutagenesis + CHO expression "confirms that several of these
  mutations inactivate ornithine delta-aminotransferase and cause gyrate atrophy". This is
  the basis for the IMP -> GO:0004587 annotation (loss-of-function mutants abolish activity).
- PMID:23076989 (Doimo et al. 2013): functional analysis of missense mutants expressed in a
  yeast OAT-ortholog-deletion strain; "All mutations markedly reduced enzymatic activity";
  mutants "failed to assemble to form the active OAT hexamer". Basis for IMP -> GO:0004587
  and IDA -> mitochondrial matrix (subcellular location determined).
- PMID:2793865 (Inana et al. 1989): H319Y processing mutant; supports OAT as mitochondrial
  enzyme whose deficiency causes gyrate atrophy; used for the TAS visual perception
  annotation (disease context).
- PMID:3456579 (Inana et al. 1986): cloned human OAT cDNA; "a nonabundant mitochondrial
  matrix enzyme that is severely deficient in a hereditary chorioretinal degenerative
  disease (gyrate atrophy)". Basis for NAS mitochondrial matrix location and TAS
  GO:0004587.

## Annotation review reasoning

Core molecular function = GO:0004587 (current label "L-ornithine transaminase activity",
= ornithine delta-aminotransferase, EC 2.6.1.13), supported experimentally (IMP in two
papers) and directly cofactor-supported by PLP binding GO:0030170 (PLP at Lys-292).

Location: mitochondrial matrix (GO:0005759) is the specific, experimentally supported
compartment (IDA PMID:23076989; NAS PMID:3456579; TAS Reactome). Broader "mitochondrion"
(GO:0005739, IDA HPA / HTP / IBA / Ensembl-IEA) and "cytoplasm" (IBA, from UniProt DR) are
correct-but-less-precise; keep matrix as core, keep the mitochondrion annotations as
non-core / accept-as-general.

BP:
- L-proline biosynthetic process (GO:0055129, IEA UniPathway) — core; OAT is step 1/1 of
  the L-glutamate-5-semialdehyde-from-ornithine sub-pathway feeding proline synthesis.
- L-arginine catabolic process (GO:0006527, IBA) — accept (ornithine, from arginine via
  arginase, is catabolized by OAT); part of arginine/ornithine catabolism.
- visual perception (GO:0007601, TAS PMID:2793865) — this is a disease phenotype
  (gyrate atrophy affects the retina), NOT a direct molecular role of the enzyme in the
  visual-perception process. Keep as non-core (retina is affected by deficiency) — the
  enzyme does not "do" phototransduction; mark as over-annotation of the biological process.

MF over-annotations:
- transaminase activity (GO:0008483, IEA ARBA) — parent of the specific 0004587; less
  precise, mark as over-annotated (redundant with the specific term).
- protein binding (GO:0005515, IPI PMID:32814053) — bare protein binding from a large
  Y2H/interactome screen (APP interaction, EBI-721662/EBI-77613); uninformative; the
  APP interaction is not an established OAT function. MARK_AS_OVER_ANNOTATED (do not remove
  IPI per policy).
- identical protein binding (GO:0042802, IPI PMID:23076989) — reflects the homohexamer;
  informative as self-association. Accept as non-core (supports oligomerization, not a
  distinct catalytic MF).

PMID:32814053 (Haenig et al. 2020) is an interactome-mapping paper focused on
neurodegenerative-disease proteins; the OAT-APP interaction it reports is a high-throughput
Y2H hit, not a validated functional partnership. Relevance LOW for OAT function.

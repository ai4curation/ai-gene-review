# AFMID (Q63HM1) review notes

## Identity and function

AFMID = arylformamidase, also called kynurenine formamidase (KFA / KFase) and
N-formylkynurenine formamidase (FKF). UniProt recommended name is
"Kynurenine formamidase", EC 3.5.1.9.

It catalyzes the **second step of the kynurenine pathway** of tryptophan
degradation: hydrolysis of N-formyl-L-kynurenine to L-kynurenine + formate.

Verbatim UniProt (file:human/AFMID/AFMID-uniprot.txt):
- FUNCTION: "Catalyzes the hydrolysis of N-formyl-L-kynurenine to L-kynurenine, the second step in the kynurenine pathway of tryptophan degradation. Kynurenine may be further oxidized to nicotinic acid, NAD(H) and NADP(H). Required for elimination of toxic metabolites."
- CATALYTIC ACTIVITY: "Reaction=N-formyl-L-kynurenine + H2O = L-kynurenine + formate + H(+)" ... "EC=3.5.1.9".
- PATHWAY: "Amino-acid degradation; L-tryptophan degradation via kynurenine pathway; L-kynurenine from L-tryptophan: step 2/2."
- SUBUNIT: "Homodimer."
- SUBCELLULAR LOCATION: "Cytoplasm, cytosol ... Nucleus ... Predominantly cytosolic. Some fraction is nuclear."
- SIMILARITY: "Belongs to the kynurenine formamidase family."
- DOMAIN/catalytic mechanism: HGGXW motif (residues 95-99) forms the oxyanion hole; catalytic Ser164 (ACT_SITE "Nucleophile"), plus ACT_SITE 247 and 279 (the Ser-His-Asp/Glu catalytic triad of an alpha/beta-hydrolase-fold serine hydrolase).

Structural/family classification (file:human/AFMID/AFMID-uniprot.txt DR lines):
- ESTHER: human-AFMID; Kynurenine-formamidase (alpha/beta-hydrolase / esterase-lipase superfamily)
- MEROPS: S09.977 (prolyl oligopeptidase family clan — serine hydrolase)
- Pfam PF07859 Abhydrolase_3; Gene3D 3.40.50.1820 alpha/beta hydrolase; SUPFAM SSF53474 alpha/beta-Hydrolases
- HAMAP MF_03014 (KFase); InterPro IPR027519 KFase_ver/fungi-typ
- PANTHER PTHR48081:SF33 KYNURENINE FORMAMIDASE
This is a serine-hydrolase-fold enzyme; its true molecular function is the specific
hydrolase GO:0004061 (arylformamidase activity), which sits under
GO:0016811 (hydrolase activity, acting on C-N bonds, in linear amides) < GO:0016787.

## Pathway context

The kynurenine pathway: L-tryptophan --(TDO2/IDO1, GO:0004833/GO:0072328)-->
N-formyl-L-kynurenine --(AFMID)--> L-kynurenine --(KYNU kynureninase / KMO /
KAT)--> ... --> quinolinate --> NAD+ de novo biosynthesis. AFMID is thus a
committed step feeding both kynurenine-derived neuroactive metabolites and
de novo NAD+ biosynthesis (GO:0034354).

Reactome: R-HSA-71240 Tryptophan catabolism (UniProt DR line).
UniPathway: UPA00333, UER00454 (L-kynurenine from L-tryptophan step 2/2).

Human relevance: biallelic AFMID variants have been linked to a phenotype
with elevated tryptophan-pathway metabolites; AFMID feeds NAD+ de novo
synthesis, connecting it to NAD-deficiency biology seen for downstream
kynurenine-pathway enzymes (cf. KYNU, PMID:28792876). (Not used as a
verbatim-quoted supporting reference here; recorded as background only.)

## GOA annotation review summary (file:human/AFMID/AFMID-goa.tsv)

Molecular function:
- GO:0004061 arylformamidase activity (IEA, GO_REF:0000120 UniRule/EC/RHEA) -> ACCEPT. This is the true catalytic MF (EC 3.5.1.9), core.
- GO:0016787 hydrolase activity (IBA GO_REF:0000033; and IEA GO_REF:0000002 InterPro) -> MODIFY to GO:0004061; "hydrolase activity" is the correct branch but far too general when the specific arylformamidase activity is known.
- GO:0005515 protein binding (IPI, PMID:32296183) x3 (DDIT4L/Q96D03, MED18/Q9BUE0, MEI4/A8MW99) -> MARK_AS_OVER_ANNOTATED. All three are HuRI high-throughput Y2H hits (also in UniProt INTERACTION). Bare "protein binding" is uninformative and these HT-Y2H interactions have no established functional meaning for a cytosolic metabolic enzyme. Policy: do not REMOVE an IPI protein-binding annotation.

Biological process:
- GO:0006569 L-tryptophan catabolic process (IBA GO_REF:0000033; IEA GO_REF:0000002 InterPro) -> ACCEPT. Core BP.
- GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan (IEA GO_REF:0000104) -> ACCEPT (core; kynurenine pathway feeds de novo NAD+).

Cellular component:
- GO:0005737 cytoplasm (IBA GO_REF:0000033 is_active_in; IEA GO_REF:0000104 located_in) -> ACCEPT / KEEP. Consistent with cytosolic enzyme; cytosol is the more precise term.
- GO:0005829 cytosol (IEA GO_REF:0000044 UniProtKB-SubCell) -> ACCEPT. Most precise, matches "Predominantly cytosolic".
- GO:0005634 nucleus (IEA GO_REF:0000120 from UniProtKB-SubCell SL-0191) -> KEEP_AS_NON_CORE. UniProt records a nuclear fraction ("Some fraction is nuclear"), but this is HAMAP-rule-propagated and the core catalytic role is cytosolic; keep but not core.

Note: GO:0019441 "L-tryptophan catabolic process to L-kynurenine" is OBSOLETE in
the current ontology (verified in go.db: label "obsolete L-tryptophan catabolic
process to L-kynurenine"), so it is NOT used in core_functions. GO:0006569 is the
valid catabolic BP.

## Core functions chosen

- MF: GO:0004061 arylformamidase activity (EC 3.5.1.9) — the specific serine-hydrolase
  activity, hydrolyzing N-formyl-L-kynurenine to L-kynurenine + formate.
- BP: GO:0006569 L-tryptophan catabolic process; GO:0034354 'de novo' NAD+ biosynthetic
  process from L-tryptophan (downstream role of kynurenine pathway).
- Location: GO:0005829 cytosol (predominantly cytosolic).

## Provenance for references

- file:human/AFMID/AFMID-uniprot.txt — authoritative UniProt record (Q63HM1), used for
  FUNCTION, CATALYTIC ACTIVITY, PATHWAY, SUBUNIT, LOCATION, family, catalytic mechanism.
- PMID:32296183 (Luck et al. 2020, HuRI reference interactome) — source of the three
  GO:0005515 protein-binding IPI annotations; high-throughput Y2H, no gene-specific
  functional claim for AFMID.

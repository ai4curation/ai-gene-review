# ODC1 (Ornithine decarboxylase 1) — review notes

UniProt: P11926 (DCOR_HUMAN). Gene: ODC1. HGNC:8109. Human (NCBITaxon:9606).
EC 4.1.1.17. 461 aa.

## Core biology

ODC1 is **ornithine decarboxylase**, the PLP (pyridoxal 5'-phosphate)-dependent
lyase that catalyzes the **first and rate-limiting step of polyamine biosynthesis**:
decarboxylation of L-ornithine to putrescine + CO2.

- Reaction (UniProt CATALYTIC ACTIVITY): "L-ornithine + H(+) = putrescine + CO2"
  (Rhea:22964; EC 4.1.1.17) [file:human/ODC1/ODC1-uniprot.txt].
- Function (UniProt): "Catalyzes the first and rate-limiting step of polyamine
  biosynthesis that converts ornithine into putrescine, which is the precursor for
  the polyamines, spermidine and spermine" [file:human/ODC1/ODC1-uniprot.txt;
  ECO:0000269|PubMed:17900240].
- Cofactor: pyridoxal 5'-phosphate (ChEBI:CHEBI:597326), covalently attached as
  N6-(pyridoxal phosphate)lysine at Lys69 [file:human/ODC1/ODC1-uniprot.txt MOD_RES 69].
- Pathway: "Amine and polyamine biosynthesis; putrescine biosynthesis via
  L-ornithine pathway; putrescine from L-ornithine: step 1/1" (UniPathway
  UPA00535/UER00288) [file:human/ODC1/ODC1-uniprot.txt].

## Quaternary structure — obligate homodimer

- UniProt SUBUNIT: "Homodimer. Only the dimer is catalytically active, as the
  active sites are constructed of residues from both monomers" [file:human/ODC1/ODC1-uniprot.txt].
- The crystal structure paper confirms the dimeric enzyme with two active sites at
  the dimer interface: "The two active sites are found at the dimer interface,
  between the N-terminal domain of one monomer and the C-terminal domain of the
  other, with Lys 69 and Cys 360 contributing to each active site from opposite
  monomers" [PMID:17407445 full text, "The two active sites are found at the dimer
  interface"]. ACT_SITE 360 is "Proton donor; shared with dimeric partner"
  [file:human/ODC1/ODC1-uniprot.txt]. Structure of human ODC solved at 2.1 Å
  [PMID:10623504].
- Reactome models the dimerization step: "Cytosolic pyridoxal phosphate-conjugated
  ornithine decarboxylase 1 (PXLP-K69-ODC1) monomers dimerize to form catalytically
  active ODC" [Reactome:R-HSA-9955574].

## Kinetics / catalytic validation

- KM = 0.08 mM for L-ornithine; kcat = 3.3 sec^-1 [file:human/ODC1/ODC1-uniprot.txt;
  ECO:0000269|PubMed:17407445]. Catalytic activity assigned EC 4.1.1.17 from this
  structural/biochemical study [PMID:17407445]. This is the basis for the
  IDA/EXP annotations of ornithine decarboxylase activity (GO:0004586).

## Regulation — antizyme / antizyme inhibitor axis (the ODC hallmark)

ODC is one of the most tightly regulated enzymes known; it has a very short
half-life and is degraded by a ubiquitin-independent mechanism.

- UniProt ACTIVITY REGULATION: "Inhibited by antizymes (AZs) OAZ1, OAZ2 and OAZ3 in
  response to polyamine levels. AZs inhibit the assembly of the functional homodimer
  by binding to ODC monomers. Additionally, OAZ1 targets ODC monomers for
  ubiquitin-independent proteolytic destruction by the 26S proteasome"
  [file:human/ODC1/ODC1-uniprot.txt; PMID:17900240].
- Antizyme (OAZ1/2/3) binds ODC monomers, blocks productive dimerization, and
  targets ODC to the 26S proteasome without ubiquitination
  [Reactome:R-HSA-350567; R-HSA-353125; R-HSA-350562].
- Antizyme inhibitor AZIN1 counteracts antizyme by sequestering it
  [Reactome:R-HSA-350567].
- NQO1 stabilizes ODC and protects it from proteasomal degradation
  [Reactome:R-HSA-350578].
- Structural basis of antizyme regulation solved as ODC:OAZ1 (PMID:26305948) and
  ODC:OAZ1:AZIN complexes (PMID:26443277) [cited in UniProt DR; not separately in GOA].

Note on GO:0042978 "ornithine decarboxylase activator activity": this term
("Binds to and increases ornithine decarboxylase activity") describes an
antizyme-inhibitor–like activator, NOT the enzyme itself. ODC1 is the decarboxylase,
not its activator; the antizyme inhibitors (AZIN1/AZIN2) are the activators of ODC.
The GO:0042978 EXP annotation (via Reactome, PMID:10623504) is a directionality
over-annotation and is marked as over-annotated (experimental → not removed).

## Localization

- Cytosolic enzyme. UniProt-curated GO (DR lines): C:cytoplasm ISS, C:cytosol TAS
  (Reactome). Reactome consistently describes "cytosolic ornithine decarboxylase"
  [Reactome:R-HSA-70692]. IBA is_active_in cytoplasm [ODC1-goa.tsv]. Cytoplasm/cytosol
  is the core localization.

## Post-translational modification / inhibition

- S-nitrosylation inhibits the enzyme; S-nitrosylated on Cys360 in the active site
  [file:human/ODC1/ODC1-uniprot.txt PTM; PMID:10462479, PMID:11461922]. (Not in GOA.)
- Phosphoserine 303 (by CK2) [file:human/ODC1/ODC1-uniprot.txt MOD_RES 303].

## Response to virus (weak)

- ODC1 protein/mRNA down-regulated in response to enterovirus 71 (EV71) infection
  in rhabdomyosarcoma cells [PMID:16548883, abstract: "Western blot analyses of APOB,
  CLU, DCAMKL1 and ODC1 proteins correlated protein and transcript levels"; UniProt
  INDUCTION "Down-regulated in response to enterovirus 71 (EV71) infection"]. This is
  the basis of the GO:0009615 "response to virus" IEP annotation. It reflects
  differential expression in one viral-infection transcriptomic/proteomic study, not
  a dedicated antiviral function of ODC1; kept as non-core.

## Interactome (high-throughput) annotations

Bare GO:0005515 "protein binding" IPI annotations come from proteome-scale binary
interactome / AP-MS screens (Rolland 2014 PMID:25416956; Luck 2020 PMID:32296183;
Huttlin 2017 PMID:28514442, 2021 PMID:33961781; Sahni 2015 PMID:29892012;
Fragoza 2019 PMID:31515488). Partners recorded in GOA WITH/FROM:
- Q9UMX2 = OAZ3 (ornithine decarboxylase antizyme 3) — biologically meaningful
  (antizyme binding; UniProt INTERACTION lists OAZ3).
- Q92993 = KAT5 (histone acetyltransferase KAT5/TIP60).
- Q9H8Y8 = GORASP2 (Golgi reassembly-stacking protein 2).
Per policy, bare "protein binding" IPI is not removed; marked over-annotated (the term
is uninformative). The biologically informative binding — antizyme (OAZ) and antizyme
inhibitor (AZIN) — is captured in core_functions and via the regulation annotations.

## Disease

- Bachmann-Bupp syndrome (BABS, MIM:619075): autosomal dominant; global developmental
  delay, alopecia/hypotrichosis, macrocephaly, facial dysmorphism, white-matter
  abnormalities. Caused by **gain-of-function C-terminal truncating variants** distal
  enough to escape nonsense-mediated decay, giving ODC1 superactivity/stabilization
  [file:human/ODC1/ODC1-uniprot.txt DISEASE; PMID:30239107 (448-461 del),
  PMID:30475435 (419-461 del)]. VAR_085001 characterized as "gain-of-function variant
  resulting in increased putrescine biosynthesis ... increased ODC1 protein levels in
  patient red blood cells" [file:human/ODC1/ODC1-uniprot.txt VARIANT 448..461].
- ODC is a well-established oncology target (polyamines drive proliferation); DFMO
  (eflornithine) is the classic irreversible inhibitor [PMID:17407445; DrugBank
  DB06243 Eflornithine].

## Annotation review summary

Core molecular function: ornithine decarboxylase activity (GO:0004586) + PLP binding
(GO:0030170; not in GOA — proposed) + homodimerization (GO:0042803).
Core biological process: putrescine biosynthetic process (GO:0009446) / polyamine
biosynthetic process (GO:0006596).
Core localization: cytosol / cytoplasm (GO:0005829 / GO:0005737).

Over-annotations / non-core:
- GO:0042978 ornithine decarboxylase activator activity — wrong-direction; ODC is the
  enzyme, activation is the antizyme inhibitor's role → MARK_AS_OVER_ANNOTATED.
- GO:0003824 catalytic activity (IEA) — too general (root-ish MF) → MODIFY to GO:0004586.
- GO:0005515 protein binding (IPI ×10) — uninformative → MARK_AS_OVER_ANNOTATED.
- GO:0009615 response to virus (IEP) — single expression study → KEEP_AS_NON_CORE.
- GO:0042176 regulation of protein catabolic process (ISS/IEA) — reflects ODC being a
  substrate of antizyme-directed degradation, not ODC regulating catabolism → this is
  ODC's own regulated turnover, arguably KEEP_AS_NON_CORE (ODC is target, and its
  C-terminus is a degradation determinant), but the term reads as ODC *regulating*
  protein catabolism, which is over-interpreted → MARK_AS_OVER_ANNOTATED / non-core.
</content>
</invoke>

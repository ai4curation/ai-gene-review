# MTHFD1 (P11586) review notes

## Identity and overview

MTHFD1 = C-1-tetrahydrofolate synthase, cytoplasmic (C1-THF synthase); UniProt P11586 (C1TC_HUMAN).
Synonyms MTHFC, MTHFD. HGNC:7432, GeneID 4522, chromosome 14. 935 aa, homodimer, cytoplasmic.

It is a **trifunctional** folate one-carbon enzyme that interconverts the one-carbon oxidation
states of tetrahydrofolate (THF). Three catalytic activities on one polypeptide, in two structural
domains:

- N-terminal D/C domain (residues ~2-291): methylenetetrahydrofolate dehydrogenase (NADP+) +
  methenyltetrahydrofolate cyclohydrolase.
- Larger C-terminal domain (residues ~310-935): formyltetrahydrofolate synthetase (formate--THF ligase).

[file:human/MTHFD1/MTHFD1-uniprot.txt "The N-terminal methylenetetrahydrofolate dehydrogenase and
methenyltetrahydrofolate cyclohydrolase (D/C) domain carries both the"] and
[file:human/MTHFD1/MTHFD1-uniprot.txt "The larger C-terminal formyltetrahydrofolate synthetase domain"].

## Three catalytic reactions (from UniProt CATALYTIC ACTIVITY)

1. **Methylenetetrahydrofolate dehydrogenase (NADP+), EC 1.5.1.5** (GO:0004488):
   (6R)-5,10-methylene-THF + NADP+ = (6R)-5,10-methenyl-THF + NADPH. RHEA:22812.
2. **Methenyltetrahydrofolate cyclohydrolase, EC 3.5.4.9** (GO:0004477):
   (6R)-5,10-methenyl-THF + H2O = (6R)-10-formyl-THF + H+. RHEA:23700.
3. **Formyltetrahydrofolate synthetase / formate--THF ligase, EC 6.3.4.3** (GO:0004329):
   (6S)-THF + formate + ATP = (6R)-10-formyl-THF + ADP + phosphate. RHEA:20221.

All three EC/reactions are explicit in the UniProt record (lines 11-17, 305-325) with ECO:0000269
experimental evidence from PubMed:1881876, PubMed:10828945, PubMed:18767138.

## Biological role

The three activities interconvert one-carbon-loaded THF species that feed distinct biosynthetic
demands: 10-formyl-THF for **de novo purine** biosynthesis (formate + THF -> 10-formyl-THF via the
synthetase; also 5,10-methenyl-THF -> 10-formyl-THF via the cyclohydrolase); 5,10-methylene-THF for
**thymidylate** synthesis (via thymidylate synthase) and for **serine/glycine** and, downstream of
5-methyl-THF, **methionine/homocysteine remethylation**.

UniProt FUNCTION [file:human/MTHFD1/MTHFD1-uniprot.txt "differentially required in nucleotide and amino
acid biosynthesis,"] and [file:human/MTHFD1/MTHFD1-uniprot.txt "being required for purine biosynthesis"].
PATHWAY: [file:human/MTHFD1/MTHFD1-uniprot.txt "One-carbon metabolism; tetrahydrofolate interconversion."]

Core catalytic and pathway assignments:
- GO:0004488 methylenetetrahydrofolate dehydrogenase (NADP+) activity — IDA PMID:1881876, PMID:10828945, PMID:18767138 [MTHFD1-goa.tsv lines 25,31,32].
- GO:0004477 methenyltetrahydrofolate cyclohydrolase activity — IDA PMID:10828945, PMID:1881876 [goa lines 30,36].
- GO:0004329 formate-tetrahydrofolate ligase activity — IDA PMID:18767138, PMID:1881876; IMP PMID:25633902 [goa lines 26,29,35].
- GO:0035999 tetrahydrofolate interconversion — IDA PMID:10828945, PMID:1881876 [goa lines 34,38].
- GO:0009257 10-formyltetrahydrofolate biosynthetic process — IDA PMID:1881876 [goa line 37].
- GO:0006164 purine nucleotide biosynthetic process — IMP PMID:18767138 (formate incorporation into DNA reduced in KO cells) [goa line 33].
- GO:0046655 folic acid metabolic process — IMP PMID:25633902 [goa line 27].
- GO:0071265 L-methionine biosynthetic process — IMP PMID:25633902 (patient fibroblasts show reduced methionine formation from [14C]-formate) [goa line 28].
- Cytosol GO:0005829 — IDA (HPA) and IBA [goa lines 24,2].

## Key experimental evidence (cached, all abstract-only — full_text_available: false)

- **PMID:1881876** (Hum & MacKenzie 1991, Protein Eng): expressed D/C domain (res 1-301) and
  synthetase domain (304-935) separately in E. coli; both fold into active enzymes. Establishes the
  three activities and two-domain architecture. Supports GO:0004488, GO:0004477, GO:0004329.
  Quote: [PMID:1881876 "Both domains formed active enzymes thereby demonstrating their ability to fold independently."]
- **PMID:10828945** (Schmidt et al. 2000, Biochemistry): crystal structures of the human D/C
  domain (DC301) with NADP and inhibitors; identifies catalytic residues (Lys56, Tyr52, Ser49,
  Cys147) and proposes reaction mechanism for dehydrogenase + cyclohydrolase. Supports GO:0004488,
  GO:0004477. Quote: [PMID:10828945 "we propose a reaction mechanism for both activities, the
  dehydrogenase and the cyclohydrolase."]
- **PMID:18767138** (Christensen et al. 2009, Hum Mutat): p.Arg653Gln variant; measured enzyme
  activity/stability and formate flux; in Mthfd1-KO cells transfected with R653Q, formate
  incorporation into DNA reduced (de novo purine synthesis disrupted). Supports GO:0004329,
  GO:0004488, and GO:0006164 (purine biosynthesis). Quote: [PMID:18767138 "indicating a disruption
  of de novo purine synthesis."]
- **PMID:25633902** (Burda et al. 2015, J Inherit Metab Dis): four new MTHFD1-deficiency patients;
  patient fibroblasts show severely reduced methionine formation from [14C]-formate, responsive to
  folic/folinic acid. Supports GO:0046655 (folic acid metabolism), GO:0071265 (methionine
  biosynthesis), and the synthetase activity IMP GO:0004329. Quote: [PMID:25633902 "Patient
  fibroblast studies revealed severely reduced methionine formation from [(14)C]-formate"].

## Disease

- **Neural tube defects, folate-sensitive (NTDFS)** MIM:601634 — susceptibility; R653Q maternal risk
  (UniProt DISEASE; PMID:12384833, PMID:16552426, PMID:9611072). R653Q also increases congenital
  heart defect risk (PMID:18767138).
- **Combined immunodeficiency and megaloblastic anemia with/without hyperhomocysteinemia (CIMAH)**
  MIM:617780 — autosomal recessive inborn error of folate metabolism; variants S49F, L51P, R173C,
  T269I, E225* (PMID:21813566, PMID:25633902, PMID:27707659).
- **Colorectal cancer** susceptibility association (PMID:17000706); R134K minor-allele association.

## Annotation review decisions (summary)

Core = the three catalytic MFs + tetrahydrofolate interconversion / one-carbon (folate) metabolism +
cytosol location. These are strongly supported by IDA/IMP experimental annotations and structural work.

- **ACCEPT** the three catalytic MF IDAs (GO:0004488, GO:0004477, GO:0004329) and their IBA backups;
  ACCEPT GO:0035999 tetrahydrofolate interconversion (IDA/IBA); ACCEPT cytosol (IDA HPA + IBA).
- **ACCEPT / KEEP_AS_NON_CORE** the well-supported downstream BP roles: GO:0009257
  10-formyl-THF biosynthesis (IDA), GO:0006164 purine nucleotide biosynthesis (IMP), GO:0046655
  folic acid metabolic process (IMP), GO:0071265 L-methionine biosynthesis (IMP) — these are genuine
  consequences of the enzyme's one-carbon chemistry but are downstream/pathway-level, so non-core.
- Redundant IEA duplicates of the catalytic MFs (ARBA/InterPro) and duplicate cytosol/cytoplasm IEAs:
  ACCEPT (correct) but note redundancy with the experimental annotations.
- **GO:0003824 catalytic activity** (IEA InterPro): MARK_AS_OVER_ANNOTATED — root-level, uninformative
  given the three specific catalytic MFs.
- **GO:0005524 ATP binding** (IEA): ACCEPT — the synthetase domain binds ATP (UniProt BINDING 380..387,
  ATP-binding keyword), consistent, but non-core (supports the ligase MF).
- **GO:0005515 protein binding** (IPI PMID:24169621): the paper is an HCV host-interactome MS screen;
  MTHFD1 not discussed in the abstract. Bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED
  (policy: never REMOVE a bare protein-binding IPI).
- **Developmental / ortholog-transfer BPs** (ISS/IEA from mouse Mthfd1 Q922D8 and Q3V3R1):
  neural tube closure, embryonic neurocranium/viscerocranium morphogenesis, heart development, somite
  development, neutrophil homeostasis, transsulfuration. These are whole-animal phenotypic consequences
  of impaired folate one-carbon metabolism in a knockout, not molecular functions of the human protein;
  KEEP_AS_NON_CORE (developmental/pleiotropic), except transsulfuration (see below).
- **GO:0019346 transsulfuration** (IEA Ensembl ortholog): MTHFD1 acts in folate one-carbon metabolism
  and homocysteine *remethylation*, not the transsulfuration pathway (homocysteine -> cystathionine ->
  cysteine, via CBS/CTH). MARK_AS_OVER_ANNOTATED as a mis-scoped ortholog transfer (IEA, so arguable,
  but retained per no-REMOVE-when-uncertain on the specific mechanism; flagged as likely wrong pathway).
- **Exosome / membrane localizations** (HDA GO:0070062 extracellular exosome x3; GO:0016020 membrane):
  high-throughput MS of exosome/membrane fractions; MTHFD1 is a soluble cytosolic enzyme, common
  contaminant of exosome/membrane proteomics. KEEP_AS_NON_CORE (not core localization) — HDA, not REMOVE.
- **GO:0005739 mitochondrion** (TAS PMID:3528153): PMID:3528153 is about the *yeast* mitochondrial C1-THF
  synthase isozyme (ADE3-related, the MTHFD2 counterpart) and explicitly states the cytoplasmic
  C1-THF synthase is NOT mitochondrial. The human cytoplasmic MTHFD1 is cytosolic; the mitochondrial
  paralogs are MTHFD2/MTHFD2L/MTHFD1L. This TAS mitochondrion annotation is a mislocalization →
  MARK_AS_OVER_ANNOTATED (TAS/curator, not experimental for this gene; do not REMOVE).
- Reactome cytosol TAS annotations: ACCEPT (correct location, correct reactions).
</content>
</invoke>

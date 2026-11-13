---
title: "mcrA across clades: methyl- and alkyl-coenzyme M reductase alpha subunits"
species: [METTM, METTH, METJA, METKA, METBF, METAC, 9EURY]
genes: [mcrA]
autolink_exclude: [Delta]
---

# mcrA across clades

[Back to the ARCHAEA project](../ARCHAEA.md)

**Bottom line.** The methyl-coenzyme M reductase (MCR) alpha subunit was reviewed
in eight proteins spanning four methanogen orders, an anaerobic methanotroph
(ANME-2d) and an ethane oxidizer. In methanogens, GOA's annotation of this
subunit is correct but uniform and coarse: every ortholog carries the same
electronic and ISS rows, the process term is the generic methanogenesis, and no
ortholog has a complex or cofactor annotation. Outside methanogens the same
pipeline is wrong. InterPro2GO maps all seven MCR alpha signatures to
methanogenesis, so a methanotroph and an ethane oxidizer receive a process they do
not perform. The ethane-specific enzyme also receives a methyl-specific activity
through the domain-level signatures, even though it lacks the MCR alpha family
signature. Four GO terms are missing (coenzyme F430 binding, ethyl-coenzyme M
reductase activity, ethane catabolism, anaerobic oxidation of methane), and the
MCR complex definition assumes the methane-forming direction.

## Scope

One reviewed (Swiss-Prot) alpha subunit was taken per methanogen order where one
exists, plus the best-characterized enzyme (*M. marburgensis*). The two
non-methanogen clades have only unreviewed entries; the two used here are the
full-length entries closest to a structurally characterized enzyme. Paralogous
MCR II alpha subunits (mrtA) are out of scope.

| Clade (order) | Organism | Gene folder | UniProt | Physiology | Evidence on the protein itself |
|---|---|---|---|---|---|
| Methanobacteriales | *Methanothermobacter marburgensis* | METTM/mcrA | P11558 | H2/CO2 methanogen | Purified enzyme, kinetics, structures, localization |
| Methanobacteriales | *M. thermautotrophicus* Delta H | METTH/mcrA | O27232 | H2/CO2 methanogen | Isoenzyme purification (existing review) |
| Methanococcales | *Methanocaldococcus jannaschii* | METJA/mcrA | Q58256 | H2/CO2 methanogen | None; sequence only |
| Methanopyrales | *Methanopyrus kandleri* | METKA/mcrA | Q49605 | H2/CO2 methanogen | Crystal structure (1E6V) |
| Methanosarcinales | *Methanosarcina barkeri* Fusaro | METBF/mcrA | P07962 | H2/CO2, methanol, acetate | Crystal structure (1E6Y) |
| Methanosarcinales | *M. acetivorans* C2A | METAC/mcrA | Q8THH1 | acetate, methanol, methylamines | Cryo-EM structures (existing review) |
| ANME-2d (*Ca.* Methanoperedentaceae) | *Ca.* Methanoperedens nitratireducens | 9EURY/mcrA__A0A284VQI9 | A0A284VQI9 | nitrate-driven methane oxidation | None; same-genus ortholog structures |
| GoM-Arc1 (*Ca.* Methanoperedentaceae) | *Ca.* Ethanoperedens thermophilum | 9EURY/mcrA__A0A7R9R780 | A0A7R9R780 | ethane oxidation | Crystal structure (7B1S, 0.99 A) |

ANME-1 (*Ca.* Methanophagales) could not be included. UniProt has no full-length
ANME-1 McrA, and RCSB maps the ANME-1 MCR structure (PDB 3SQG) to K4Q4L0, a
162-residue environmental fragment from an unrelated study.

## Results by review

| UniProt | GOA rows | Actions | Main change |
|---|---|---|---|
| P11558 | 9 | 8 ACCEPT, 1 MODIFY, 2 NEW | methanogenesis narrowed to the CO2 route; complex and F430 binding added |
| O27232 | 6 | 5 ACCEPT, 1 MODIFY, 2 NEW | harmonized: F430 binding added |
| Q58256 | 5 | 4 ACCEPT, 1 MODIFY, 2 NEW | CO2 route; complex and F430 binding by similarity |
| Q49605 | 5 | 4 ACCEPT, 1 MODIFY, 2 NEW | CO2 route; complex and F430 binding from the structure |
| P07962 | 5 | 4 ACCEPT, 1 MODIFY, 2 NEW | methanogenesis split into CO2, methanol and acetate routes |
| Q8THH1 | 5 (+4 retired) | 4 ACCEPT, 1 MODIFY, 2 NEW | harmonized: generic methanogenesis now MODIFY to the acetate and methanol routes |
| A0A284VQI9 | 2 | 1 ACCEPT, 1 MODIFY, 2 NEW | methanogenesis corrected to methane catabolic process |
| A0A7R9R780 | 2 | 2 MODIFY, 1 NEW | methanogenesis corrected to alkane catabolic process; methyl-specific activity replaced by proposed ethyl-coenzyme M reductase activity |

All eight reviews validate. Their GOA rows were fetched on 2026-11-13; the two
existing reviews' GOA files were unchanged.

## Findings

### 1. The methanogen annotation is correct and uniform

Each methanogen ortholog has the same five rows: cytoplasm (SubCell IEA and ISS from
P11558), coenzyme-B sulfoethylthiotransferase activity (GO:0050524; combined IEA and
ISS) and methanogenesis (InterPro2GO). Only P11558 adds experimental rows: four EXP
and one IDA for the activity, and an EXP for cytoplasm. All the activity and
location rows were accepted. The sequence comparison supports the transfer. All six
methanogen sequences conserve the F430 axial glutamine and every coenzyme M and
coenzyme B contact of P11558. The one exception is a Tyr-to-Phe change at a
coenzyme M contact in both *Methanosarcina* sequences
([RESULTS](mcrA-across-clades/RESULTS.md)).

One P11558 row cites the wrong paper: the IDA for activity from the 1988 gene-cloning
paper (PMID:2448287). The full text, read from a PDF supplied during review, contains
no activity assay; the only protein work is Western-blot detection of the subunits
expressed in *E. coli*. The claim stays accepted because four EXP rows support it, the
reference is marked miscited, and a source defect asks for the row (assigned by MENGO
in 2013) to be withdrawn.

### 2. Methanogenesis should name the route

GO:0015948 methanogenesis is true for every methanogen MCR but less specific than the
evidence allows. For the obligately CO2-reducing Methanobacteriales, Methanococcales
and Methanopyrales orthologs, the row is modified to GO:0019386 methanogenesis, from
carbon dioxide. For the multi-route *Methanosarcina* orthologs, every route with a
GO child is listed: CO2, methanol and acetate for *M. barkeri*, and acetate and
methanol for *M. acetivorans*. The earlier *M. acetivorans* review kept the generic
term because GO has no methylamine-route child. That reasoning was revised: each
child is_a methanogenesis, so listing the children loses nothing.

### 3. InterPro2GO puts methanogenesis on enzymes that consume alkanes

All seven InterPro entries behind the MCR alpha rows map to both GO:0015948 and
GO:0050524: the family IPR016212 and the domain entries IPR003183, IPR008924,
IPR009024, IPR009047, IPR015811 and IPR015823 (interpro2go of 2026-07-06).

- **ANME-2d McrA (A0A284VQI9).** The activity row is correct, because GO:0050524 is
  written as a reversible reaction. Purified methanogenic MCR runs it in the
  methane-activating direction (PMID:20520712), and the ANME-2d MCR structures
  resemble methanogenic ones (PMID:40913044). The methanogenesis row is wrong: the
  organism oxidizes methane by reverse methanogenesis (PMID:23892779). It was
  modified to GO:0046188 methane catabolic process. ANME-2 MCRs fall inside
  IPR016212 and cannot be separated from Methanosarcinales MCRs by signature, so
  the fix needs a taxon condition.
- **Ethyl-coenzyme M reductase alpha (A0A7R9R780).** This protein does not match the
  family entry IPR016212. Both of its rows come from the domain entries alone. The
  organism grows only on ethane and forms ethyl-coenzyme M with its single MCR-type
  enzyme (PMID:32317322). Methanogenesis was modified to GO:0043448 alkane catabolic
  process. The methyl-specific activity was modified to a proposed ethyl-coenzyme M
  reductase activity, with GO:0050497 alkylthioltransferase activity as the existing
  parent. Restricting the domain-level mappings to proteins that also match IPR016212
  would fix this class.
- **UniProt (ARBA).** Both unreviewed entries take their name, EC number, reaction,
  pathway and physiological direction from ARBA rules written for methanogenic MCR.
  The ECR entry is named coenzyme-B sulfoethylthiotransferase (EC 2.8.4.1) although
  UniProt cites the ECR structure paper, and the ANME-2d entry is given the
  methane-forming direction.

Neither unreviewed entry has a cellular-component row in GOA, so what is wrong on
them is the process row (and, for the ethane enzyme, the activity row), not a
location. No cytoplasm row was added for them, to keep `NEW` rows conservative,
although MCR is cytoplasmic in methane-oxidizing biofilms (PMID:23533332) and ECR
was purified as a soluble enzyme.

These are recorded as `source_defects` (resource `INTERPRO` on the process and activity
rows, `UNIPROT` on the cited UniProt text) and are listed as pattern 17 in
[annotation-patterns](annotation-patterns.md).

### 4. The active site tracks the substrate, not the lineage

Pairwise alignment of each sequence to P11558 at 13 positions found the following
([script and results](mcrA-across-clades/RESULTS.md)):

- **Methanogens (four orders).** Every position is conserved except Tyr444->Phe in
  the *Methanosarcina* sequences.
- **ANME-2d.** Every position is conserved except Gln332->Met, a change the ANME-2d
  structures also report.
- **Ethyl-CoM reductase.** Four positions are changed. The F430 nickel ligand
  Gln147 is Met181, as in the crystal structure (PMID:34210888); the coenzyme B
  contact Arg225 is Ala; Gln332 is Asn; and the S-methylcysteine site Cys452 is Gln.

Sequence conservation of a modification site does not show the modification is
present. *M. barkeri* and the ANME-2d MCRs both keep the glutamine at the
2-methylglutamine site without methylating it.

### 5. Ontology gaps

Proposed or raised in the reviews:

- **coenzyme F430 binding**, under GO:0046906 tetrapyrrole binding. Proposed in all
  eight reviews, with GO:0046906 used as the existing term on a NEW row in each. The
  definition covers modified F430 (dimethylated in the ethane enzyme, methylthio in
  ANME-1).
- **ethyl-coenzyme M reductase activity**, under GO:0050497. No GO or Rhea reaction
  exists for ethyl-coenzyme M.
- **Ethane catabolic process** and **anaerobic oxidation of methane** (reverse
  methanogenesis) as process terms (suggested questions).
- **Direction of GO:0044674 methyl coenzyme M reductase complex.** Its definition
  describes methane formation, which fits ANME MCR poorly and excludes ECR. The
  complex row was not added for ECR.
- **Methanogenesis from methylamines** (already raised in the *M. acetivorans*
  review).

## Harmonization of the two existing reviews

- **O27232 (METTH).** Added the F430 (tetrapyrrole) binding row and the proposed term,
  so every review in the set records F430 binding the same way. The earlier notes had
  declined a cofactor term; the *M. acetivorans* review had since settled on
  tetrapyrrole binding rather than nickel cation binding.
- **Q8THH1 (METAC).** Methanogenesis was changed from ACCEPT to MODIFY, listing the
  acetate and methanol children (finding 2). The F430 term justification was
  corrected: it said the nickel ligand is always glutamine, which the ethane enzyme
  disproves.

## Literature searches

PubMed (E-utilities) was searched on 2026-11-13 for the following. No
deep-research provider was configured, so each gene has hand-written notes.

- MCR from each organism: "methyl-coenzyme M reductase Methanopyrus kandleri",
  "... Methanocaldococcus jannaschii", "... Methanosarcina barkeri purification".
- Structures: "Comparison of three methyl-coenzyme M reductases from
  phylogenetically distant organisms" and "methyl-coenzyme M reductase Black Sea
  mats structure".
- ANME: Haroon et al. 2013 nitrate-dependent AOM, Scheller et al. 2010 reverse
  reaction, and "Methanoperedens methyl-coenzyme M reductase".
- Ethane and butane oxidizers: "Ethanoperedens thermophilic anaerobic oxidation of
  ethane", "ethane activation crystal structure key enzyme", the butane alkyl-CoM
  paper, and Chen et al. 2019 on *Ca.* Argoarchaeum.

UniProt was searched for every reviewed IPR016212 entry, for entries with PDB
structures, and for full-length ANME-1 and *Ca.* Syntrophoarchaeum entries.

## Not yet covered

- **MCR II (mrtA) paralogs**: P21110 (METTH), P58815 (METTM), Q60391 (METJA) and
  Q49174 (*M. fervidus*). Each has three GOA rows. They would test whether isoenzyme
  differences belong in GO.
- **Other methanogen lineages** with only unreviewed entries: Methanomicrobiales,
  Methanocellales, Methanomassiliicoccales, *Methanothrix*. Also the MCRs of
  Bathyarchaeia and Verstraetearchaeota from metagenomes.
- **Butane and propane alkyl-CoM reductases** of *Ca.* Syntrophoarchaeum (eight
  UniProt entries outside IPR016212) and the hydrocarbon-degrading *Ca.* Methanoliparum
  (PMID:34937940). These should follow the ECR pattern.
- **A curated rule** (`rules/curated/`) excluding ANME lineages from the
  methanogenesis InterPro2GO mapping, and an `interpro2go` SSSOM entry for the
  domain-level mappings.
- **The beta and gamma subunits** (McrB and McrG), which share some of the same
  signatures; IPR008924 is shared by the alpha and beta subunits.

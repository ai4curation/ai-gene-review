---
title: "48 unreviewed phosphorylation candidates for an interactive demo"
species: [mouse, rat, DROME, DANRE]
autolink_gene_symbols: false
---

# Unreviewed phosphorylation demo candidates

**48 protein-coding genes: 31 mouse, 13 rat, 2 fly, and 2 zebrafish.**
Selected on 2026-09-28 PDT (2026-09-29 UTC). All have a current positive
`involved_in` annotation to the target process, no positive protein-kinase
activity annotation in the current fetched GOA, and no gene or prediction
review file in this checkout when checked by symbol, UniProt aliases, primary
accession, and secondary accessions. Even partial review stubs are excluded.
This is a list of **review candidates**, not completed reviews or predetermined
REMOVE decisions. No review stubs have been created; follow-up curation is
tracked in [#3997](https://github.com/ai4curation/ai-gene-review/issues/3997).

[Parent project](../../PHOSPHORYLATION_REFACTOR.md) ·
[Candidate table with identifiers and rationales](candidates.tsv) ·
[Plain species/gene list](genes.txt) ·
[62 exact source annotation rows](annotations.tsv)

**ARBA follow-up:** [Generic-rule audit](arba-audit/README.md) checked all 90
conditions of ARBA00027234 and found 370 matching Swiss-Prot proteins, all
carrying protein-kinase annotations. No current QuickGO rows explicitly named
this rule or the four tested phosphorylation-descendant rules. No defensible
ARBA-derived additions were made; the demo list remains 48 genes.

## Demo use

The first 12 entries are suggested starting points, mixing wrong-substrate,
substrate, phosphatase, signaling, and cross-species propagation examples.
There are **39 high-priority candidates and 9 medium-priority discussion cases**.
Priority describes the strength/usefulness of the triage hypothesis, not a
completed evidence assessment. The medium group contains scaffolds and
complex-associated proteins for which direct participation could justify an
annotation even without intrinsic kinase activity.

The list contains 35 genes not previously individually triaged in the old
project's cross-species tables and 13 already discussed there without gene
review YAMLs. `prior_project_triage` makes that distinction explicit. Orthologs
are separate species/gene targets, not independent mechanistic examples.
The main list uses protein-coding genes with verified UniProt accessions so it
can be used with the usual gene-fetch workflow.

## Why there are no human candidates

The rerun of the local human protein-phosphorylation-minus-protein-kinase
query returned 42 objects. Every gene-symbol hit already had a review; the
remaining object was the Cyclin A1–CDK2 **complex**, not an unreviewed gene.
A live QuickGO check also exposed four accession/alias-only hits (O15302,
Q15453, Q96GZ3, Q9H4D1); UniProt identifies these as kinase proteins, so they
were excluded. Human LIMD1 and TOLLIP from the generic-phosphorylation query
are also already reviewed. This is the result of this screen, not a claim
that every possible human phosphorylation error has been exhausted.

## Method and safeguards

1. Reran the project set difference in local go-db snapshots: `goa_human`,
   `goa_mouse`, `mgi`, `rgd`, `fb`, `zfin`, and `tair`. The broader follow-up
   also checked `wb`, `sgd`, and `pombase` for additional candidates.
2. Focused on `GO:0006468 protein phosphorylation` and **is-a/part-of**
   descendants, subtracting positive `GO:0004672 protein kinase activity`
   and descendants. Required biological-process aspect; part-of traversal
   can otherwise include molecular-function terms. Explicitly excluded
   activation/regulation terms and `NOT` assertions on both sides.
3. Required the positive relation to be exactly `involved_in`. The large
   MGI candidate expansion mostly used `acts_upstream_of_or_within`; those
   are not claims of direct participation and were excluded. GO documents
   the distinction in its [annotation relations guide](https://www.geneontology.org/docs/go-annotations/).
4. Added five generic `GO:0016310 phosphorylation` cases (mouse and rat Limd1 and
   Tollip, zebrafish tollip), using subtraction of **all kinase activity** for
   this discovery arm. Added one carbohydrate-phosphorylation case,
   `rat/Epm2a`, a glycogen phosphatase. Thus 42 genes have protein-specific
   phosphorylation rows, 5 generic phosphorylation rows, and 1 carbohydrate
   phosphorylation row. Legitimate small-molecule kinases were not selected
   merely because they lack protein-kinase activity.
5. Refetched all annotations for selected UniProt products from QuickGO,
   checked current ontology descendants, and inspected current UniProt
   identity/function records. All 48 lack positive protein-kinase activity
   rows. This is supporting triage evidence, not proof of absence of catalysis.
6. Excluded known kinase subunits Phka1/Phka2/Phkb, the Hspa9
   autophosphorylation case, the TP53RK-binding protein, unresolved Q6PIU9,
   true kinases missed by names, and noncoding RNA hits. The prior Arabidopsis
   examples TOPP4/CDC25/RIN4/PI4KA1 currently use the broader upstream/within
   relation in QuickGO, so they are not in this direct-participation demo set.
7. Matched repository reviews using symbols and aliases within species and
   primary/secondary UniProt accessions across the repository. No shortlisted
   gene has an existing review file. This check is scoped to the checkout,
   not unmerged work in other branches or unpublished reviews.

The [SQL](find_candidates.sql) reproduces discovery against a local snapshot.
Source databases have different dates, so the local query is a candidate
generator; the live row check determines eligibility. The dated
[snapshot](snapshot.json) retains current ontology responses, UniProt identity
and function records, all fetched molecular-function rows, the selected
process rows, and total annotation counts. `annotations.tsv` preserves
qualifiers, evidence, reference, WITH/FROM, assigning group, date, and annotation
extensions. Multiple GOA rows and duplicate protein records are not counted as
multiple genes (e.g. mouse Pick1).

## Ranked list

Codes follow the parent project: **S** substrate, **W** wrong substrate,
**O** opposite reaction, **R** regulator/signaling, **C** complex attribution,
**U** ubiquitin-system mechanism. They are hypotheses to investigate.
Each UniProt link supports protein identity/function; GO IDs and references
identify the actual candidate assertion. Complete row-level provenance is in
`annotations.tsv`, including orthology donors for ISO/ISS annotations.

### Mouse — 31

| Rank | Gene / UniProt | Target GO term(s) | Evidence | Priority / pattern | Why investigate |
|---|---|---|---|---|---|
| 1 | **`mouse/Glyctk`** [Q8QZY2](https://www.uniprot.org/uniprotkb/Q8QZY2/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO, ISS | high / W-sugar | Glycerate kinase phosphorylates glycerate, not protein. Check the propagated protein-phosphorylation assertion. |
| 2 | **`mouse/Ilf3`** [Q9Z1X4](https://www.uniprot.org/uniprotkb/Q9Z1X4/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IDA, ISO | high / S | RNA-binding protein activated by PKR-mediated phosphorylation; likely substrate-as-participant transfer. |
| 3 | **`mouse/Klhl3`** [E0CZ16](https://www.uniprot.org/uniprotkb/E0CZ16/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IGI, IMP | high / U | CUL3 ubiquitin-ligase substrate adaptor controls WNK1/WNK4 abundance. The cited mouse study measures the downstream WNK-SPAK/OSR1-NCC phosphorylation cascade. |
| 4 | **`mouse/Ppme1`** [Q8BVQ5](https://www.uniprot.org/uniprotkb/Q8BVQ5/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IMP | high / R-enzyme | Protein phosphatase methylesterase demethylates/inhibits PP2A; the cited study explains increased IRF3 phosphorylation through reduced dephosphorylation. |
| 5 | **`mouse/Pkd1`** [O08852](https://www.uniprot.org/uniprotkb/O08852/entry) | [GO:0018105](https://www.ebi.ac.uk/QuickGO/term/GO:0018105) | IMP | high / R-receptor | Polycystin-1 participates in receptor/channel signaling. The cited study measures flow-induced HDAC5 phosphorylation downstream of polycystins. |
| 6 | **`mouse/Cdc25b`** [P30306](https://www.uniprot.org/uniprotkb/P30306/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / O | CDC25 phosphatase removes inhibitory phosphate from CDKs, thereby activating a kinase; distinguish dephosphorylation from regulation. |
| 7 | **`mouse/Thy1`** [P01831](https://www.uniprot.org/uniprotkb/P01831/entry) | [GO:0046777](https://www.ebi.ac.uk/QuickGO/term/GO:0046777) | ISO | high / R-ligand | GPI-anchored cell-surface protein; the rat reference reports FAK autophosphorylation triggered by Thy-1, not autophosphorylation of Thy-1. |
| 8 | **`mouse/Prrt1`** [O35449](https://www.uniprot.org/uniprotkb/O35449/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IMP | high / R-adapter | AMPAR auxiliary protein changes basal GRIA1 phosphorylation and receptor trafficking; distinguish modulation from phosphate transfer. |
| 9 | **`mouse/Il15`** [P48346](https://www.uniprot.org/uniprotkb/P48346/entry) | [GO:0007260](https://www.ebi.ac.uk/QuickGO/term/GO:0007260) | ISO | high / R-cytokine | Cytokine activates receptor-associated JAK/STAT signaling; JAK kinases execute STAT phosphorylation. |
| 13 | **`mouse/Adm2`** [Q7TNK8](https://www.uniprot.org/uniprotkb/Q7TNK8/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / R-ligand | Peptide hormone signals through CALCRL-RAMP receptors; test regulation versus direct phosphorylation. |
| 14 | **`mouse/Calca`** [P70160](https://www.uniprot.org/uniprotkb/P70160/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / R-ligand | Calcitonin/CGRP precursor produces receptor ligands; downstream phosphorylation does not establish catalysis by the ligand. |
| 15 | **`mouse/Cops2`** [P61202](https://www.uniprot.org/uniprotkb/P61202/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | medium / C | COP9 signalosome component; UniProt attributes associated phosphorylation to CK2/PKD. Check whether structural participation justifies the process term. |
| 16 | **`mouse/Cops8`** [Q8VBV7](https://www.uniprot.org/uniprotkb/Q8VBV7/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | medium / C | COP9 signalosome component; associated CK2/PKD perform phosphorylation. Complex membership alone is insufficient to resolve participation. |
| 17 | **`mouse/Erc1`** [Q99MI1](https://www.uniprot.org/uniprotkb/Q99MI1/entry) | [GO:0007252](https://www.ebi.ac.uk/QuickGO/term/GO:0007252) | ISO | medium / R-adapter | ELKS scaffold recruits I-kappaB to the IKK complex. Direct substrate recruitment could justify participation: retain as a discussion case. |
| 18 | **`mouse/Grm5`** [Q3UVX5](https://www.uniprot.org/uniprotkb/Q3UVX5/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / R-receptor | Metabotropic glutamate GPCR activates downstream kinases; distinguish receptor signaling from direct phosphorylation. |
| 19 | **`mouse/Hcst`** [Q9QUJ0](https://www.uniprot.org/uniprotkb/Q9QUJ0/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / S-adapter | DAP10 transmembrane adaptor provides phosphotyrosine docking sites for signaling proteins; test substrate/adaptor versus catalyst attribution. |
| 20 | **`mouse/Il21`** [Q9ES17](https://www.uniprot.org/uniprotkb/Q9ES17/entry) | [GO:0007260](https://www.ebi.ac.uk/QuickGO/term/GO:0007260) | ISO | high / R-cytokine | Cytokine triggers JAK/STAT signaling; investigate transfer of a STAT-phosphorylation readout to the ligand. |
| 21 | **`mouse/Il24`** [Q925S4](https://www.uniprot.org/uniprotkb/Q925S4/entry) | [GO:0042501](https://www.ebi.ac.uk/QuickGO/term/GO:0042501) | ISO | high / R-cytokine | Cytokine activates receptor signaling; test whether STAT serine phosphorylation was a downstream readout. |
| 22 | **`mouse/Ip6k3`** [Q8BWD2](https://www.uniprot.org/uniprotkb/Q8BWD2/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / W-inositol | Inositol hexakisphosphate kinase makes inositol pyrophosphates. Its known substrate is a small molecule, not a protein. |
| 23 | **`mouse/Limd1`** [Q9QXD8](https://www.uniprot.org/uniprotkb/Q9QXD8/entry) | [GO:0016310](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) | ISO, ISS | high / S-adapter | LIM-domain scaffold/regulator; generic phosphorylation annotation is transferred from human LIMD1, whose project review identifies a substrate-related issue. |
| 24 | **`mouse/Maml1`** [Q6T264](https://www.uniprot.org/uniprotkb/Q6T264/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | medium / R-adapter | Transcriptional coactivator recruits CDK8 and enhances NOTCH phosphorylation. Assess direct complex participation versus regulation. |
| 25 | **`mouse/Pdgfb`** [P31240](https://www.uniprot.org/uniprotkb/P31240/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468), [GO:0018108](https://www.ebi.ac.uk/QuickGO/term/GO:0018108) | ISO, ISS | high / R-ligand | PDGF ligand activates receptor tyrosine kinases; distinguish ligand action from receptor-catalyzed phosphorylation. |
| 26 | **`mouse/Pick1`** [Q62083](https://www.uniprot.org/uniprotkb/Q62083/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO, ISS | medium / R-adapter | PDZ adaptor binds PKC and organizes substrates/receptors. Direct scaffolding may warrant participation; read the assay before deciding. |
| 27 | **`mouse/Ppp3cb`** [P48453](https://www.uniprot.org/uniprotkb/P48453/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IMP | high / O | Calcineurin catalytic subunit is a protein phosphatase. Examine whether phosphorylation changes reflect indirect regulation of kinases. |
| 28 | **`mouse/Ptpn6`** [P29351](https://www.uniprot.org/uniprotkb/P29351/entry) | [GO:0018108](https://www.ebi.ac.uk/QuickGO/term/GO:0018108) | ISO | high / O | SHP-1 is a protein tyrosine phosphatase; a positive tyrosine-phosphorylation assertion requires scrutiny of the regulatory mechanism. |
| 29 | **`mouse/Rara`** [P11416](https://www.uniprot.org/uniprotkb/P11416/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO | high / S-tf | Retinoic-acid nuclear receptor/transcription factor; inspect the donor evidence for phosphorylation of RARA rather than by RARA. |
| 30 | **`mouse/Runx3`** [Q64131](https://www.uniprot.org/uniprotkb/Q64131/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO, ISS | high / S-tf | DNA-binding transcription factor; investigate propagation of a substrate phosphorylation assay. |
| 31 | **`mouse/Sqstm1`** [Q64337](https://www.uniprot.org/uniprotkb/Q64337/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IMP | medium / R-adapter | p62 scaffold binds ATF2; the cited paper identifies p38 as the ATF2 kinase. Check whether p62 contributes directly to the phosphorylation step. |
| 32 | **`mouse/Tollip`** [Q9QZ06](https://www.uniprot.org/uniprotkb/Q9QZ06/entry) | [GO:0016310](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) | ISO, ISS | high / R-adapter | Ubiquitin/autophagy adaptor regulates IRAK1 phosphorylation. Trace the human donor, whose old annotation cites a problematic PMID. |
| 33 | **`mouse/Usp25`** [P57080](https://www.uniprot.org/uniprotkb/P57080/entry) | [GO:0007252](https://www.ebi.ac.uk/QuickGO/term/GO:0007252) | IMP | high / U | Deubiquitinase regulates TRAF signaling and downstream I-kappaB phosphorylation; test whether a regulatory process is more appropriate. |
| 34 | **`mouse/Ywhaz`** [P63101](https://www.uniprot.org/uniprotkb/P63101/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISO, ISS | medium / R-adapter | 14-3-3 adaptor binds phosphoserine/threonine clients and modulates signaling. Evaluate direct participation versus regulation. |

### Rat — 13

| Rank | Gene / UniProt | Target GO term(s) | Evidence | Priority / pattern | Why investigate |
|---|---|---|---|---|---|
| 10 | **`rat/Epm2a`** [Q91XQ2](https://www.uniprot.org/uniprotkb/Q91XQ2/entry) | [GO:0046835](https://www.ebi.ac.uk/QuickGO/term/GO:0046835) | IEA, ISO | high / O-carbohydrate | Laforin is a glycogen phosphatase that prevents glycogen hyperphosphorylation; carbohydrate phosphorylation is the opposite reaction. |
| 37 | **`rat/Gas6`** [Q63772](https://www.uniprot.org/uniprotkb/Q63772/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / R-ligand | Ligand activates TAM receptor tyrosine kinases; the receptor, not GAS6, transfers phosphate. |
| 38 | **`rat/Glyctk`** [Q0VGK3](https://www.uniprot.org/uniprotkb/Q0VGK3/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / W-sugar | Glycerate kinase phosphorylates glycerate, not protein. Check the propagated protein-phosphorylation assertion. |
| 39 | **`rat/Grm5`** [P31424](https://www.uniprot.org/uniprotkb/P31424/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IDA | high / R-receptor | Metabotropic glutamate GPCR activates downstream kinases; distinguish receptor signaling from direct phosphorylation. |
| 40 | **`rat/Ilf3`** [Q9JIL3](https://www.uniprot.org/uniprotkb/Q9JIL3/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / S | RNA-binding protein activated by PKR-mediated phosphorylation; likely substrate-as-participant transfer. |
| 41 | **`rat/Limd1`** [B5DEH0](https://www.uniprot.org/uniprotkb/B5DEH0/entry) | [GO:0016310](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) | ISS | high / S-adapter | LIM-domain scaffold/regulator; generic phosphorylation annotation is transferred from human LIMD1, whose project review identifies a substrate-related issue. |
| 42 | **`rat/Pdgfb`** [Q05028](https://www.uniprot.org/uniprotkb/Q05028/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468), [GO:0018108](https://www.ebi.ac.uk/QuickGO/term/GO:0018108) | ISS | high / R-ligand | PDGF ligand activates receptor tyrosine kinases; distinguish ligand action from receptor-catalyzed phosphorylation. |
| 43 | **`rat/Pick1`** [Q9EP80](https://www.uniprot.org/uniprotkb/Q9EP80/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | IDA | medium / R-adapter | PDZ adaptor binds PKC and organizes substrates/receptors. Direct scaffolding may warrant participation; read the assay before deciding. |
| 44 | **`rat/Ppp3cb`** [P20651](https://www.uniprot.org/uniprotkb/P20651/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / O | Calcineurin catalytic subunit is a protein phosphatase. Examine whether phosphorylation changes reflect indirect regulation of kinases. |
| 45 | **`rat/Prrt1`** [Q6MG82](https://www.uniprot.org/uniprotkb/Q6MG82/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / R-adapter | AMPAR auxiliary protein changes basal GRIA1 phosphorylation and receptor trafficking; distinguish modulation from phosphate transfer. |
| 46 | **`rat/Thy1`** [P01830](https://www.uniprot.org/uniprotkb/P01830/entry) | [GO:0046777](https://www.ebi.ac.uk/QuickGO/term/GO:0046777) | IDA | high / R-ligand | GPI-anchored cell-surface protein; the rat reference reports FAK autophosphorylation triggered by Thy-1, not autophosphorylation of Thy-1. |
| 47 | **`rat/Tollip`** [A2RUW1](https://www.uniprot.org/uniprotkb/A2RUW1/entry) | [GO:0016310](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) | ISS | high / R-adapter | Ubiquitin/autophagy adaptor regulates IRAK1 phosphorylation. Trace the human donor, whose old annotation cites a problematic PMID. |
| 48 | **`rat/Ywhaz`** [P63102](https://www.uniprot.org/uniprotkb/P63102/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | medium / R-adapter | 14-3-3 adaptor binds phosphoserine/threonine clients and modulates signaling. Evaluate direct participation versus regulation. |

### Fruit fly — 2

| Rank | Gene / UniProt | Target GO term(s) | Evidence | Priority / pattern | Why investigate |
|---|---|---|---|---|---|
| 11 | **`DROME/Dref`** [Q94883](https://www.uniprot.org/uniprotkb/Q94883/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468), [GO:0046777](https://www.ebi.ac.uk/QuickGO/term/GO:0046777) | ISS | high / S-tf | DNA replication-related transcription factor carries ISS transfers from CAMKK2. Check the donor/target functional mismatch. |
| 36 | **`DROME/Glyctk`** [Q9VQC4](https://www.uniprot.org/uniprotkb/Q9VQC4/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / W-sugar | Glycerate kinase phosphorylates glycerate, not protein. Check the propagated protein-phosphorylation assertion. |

### Zebrafish — 2

| Rank | Gene / UniProt | Target GO term(s) | Evidence | Priority / pattern | Why investigate |
|---|---|---|---|---|---|
| 12 | **`DANRE/glyctk`** [Q08BL7](https://www.uniprot.org/uniprotkb/Q08BL7/entry) | [GO:0006468](https://www.ebi.ac.uk/QuickGO/term/GO:0006468) | ISS | high / W-sugar | Glycerate kinase phosphorylates glycerate, not protein. Check the propagated protein-phosphorylation assertion. |
| 35 | **`DANRE/tollip`** [Q7ZV43](https://www.uniprot.org/uniprotkb/Q7ZV43/entry) | [GO:0016310](https://www.ebi.ac.uk/QuickGO/term/GO:0016310) | ISS | high / R-adapter | Ubiquitin/autophagy adaptor regulates IRAK1 phosphorylation. Trace the human donor, whose old annotation cites a problematic PMID. |

## Useful literature entry points

These spot-checks establish why several newly selected mouse genes are good
questions for a demo; they are not full annotation reviews.

- **Klhl3:** [PMID:24821705](https://pubmed.ncbi.nlm.nih.gov/24821705/)
  identifies impaired WNK1/WNK4 ubiquitination/degradation and consequent
  activation of the WNK–OSR1/SPAK–NCC phosphorylation cascade. The question is
  whether the ligase adaptor belongs to regulation of that process.
- **Ppme1:** [PMID:31213650](https://pubmed.ncbi.nlm.nih.gov/31213650/)
  explains how PME-1 inactivates PP2A through demethylation, increasing IRF3
  phosphorylation. The mechanism is control of a phosphatase.
- **Pkd1:** [PMID:20181743](https://pubmed.ncbi.nlm.nih.gov/20181743/)
  measures flow-induced HDAC5 phosphorylation downstream of polycystin signaling.
- **Sqstm1:** [PMID:32385399](https://pubmed.ncbi.nlm.nih.gov/32385399/)
  identifies p38 as the ATF2 kinase and p62 as an ATF2-binding scaffold. This is
  intentionally a medium-priority case: determine whether scaffolding contributes
  directly to the reaction or acts elsewhere in the signaling/transcriptional response.
- **Usp25:** [PMID:23042150](https://pubmed.ncbi.nlm.nih.gov/23042150/)
  reports that USP25 deficiency increases I-kappaB/JNK phosphorylation and
  identifies TRAF5/TRAF6 deubiquitination as the mechanism.

Do not reject experimental rows from titles or abstracts alone. Read the
relevant full text during the demo; use UNDECIDED when the necessary evidence
cannot be accessed. Being noncatalytic is not, by itself, a reason to remove a
process annotation from a direct participant or scaffold.

## Recheck before the demo

From the repository root:

```bash
# Offline: checks the dated evidence and detects reviews added since selection.
uv run --script projects/PHOSPHORYLATION_REFACTOR/demo/verify_candidates.py

# Live: also refreshes GOA, ontology descendants, and UniProt identities.
uv run --script projects/PHOSPHORYLATION_REFACTOR/demo/verify_candidates.py --live

# Discover more mouse candidates from a local go-db snapshot.
duckdb -readonly ~/repos/go-db/db/mgi.ddb -csv \
  < projects/PHOSPHORYLATION_REFACTOR/demo/find_candidates.sql
```

The verifier exits nonzero for an existing review, a duplicate, a taxon
mismatch, positive protein-kinase activity, a missing candidate process row,
or a change in the listed terms/evidence/references. It does not make curation
decisions. It leaves the dated snapshot and gene files untouched.

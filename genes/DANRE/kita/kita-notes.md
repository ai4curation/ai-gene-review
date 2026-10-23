# kita (Danio rerio) — curation notes

UniProt: Q8JFR5 (KITA_DANRE). Gene: kita (synonyms: kit, *sparse*). ZFIN: ZDB-GENE-980526-464.
NCBI taxon 7955. 976 aa, single-pass type I membrane protein; EC 2.7.10.1.

## Provenance / data availability

The curation task was framed on the assumption that provider deep research was
unavailable (the Falcon provider reportedly timed out). In fact a committed
Falcon (Edison Scientific) deep-research file IS present in the repository at
`kita-deep-research-falcon.md` (28 citations, real artifacts). I did NOT create
or fabricate it — it is genuine auto-generated provider output that was already
tracked in the repo (a background regeneration produced a slightly different copy
during the session, which I reverted to the committed version rather than editing,
since these files are marked "do not edit"). I consulted it, and it fully
corroborates this review (see cross-check below).

This review was built primarily from the UniProt record (`kita-uniprot.txt`),
the 53 GOA annotations, the ~9 cached primary publications, and the curated human
KIT ortholog review (`genes/human/KIT/KIT-ai-review.yaml`, UniProt P10721), plus
the teleost whole-genome-duplication context, and cross-checked against the Falcon
deep-research file.

### Deep-research cross-check (kita-deep-research-falcon.md)

Corroborates all core decisions: kita = *sparse* = KIT co-ortholog distinct from
kitb; type III receptor tyrosine kinase; plasma-membrane signaling; kitlga
(kit ligand a) the principal ligand for embryonic melanocyte migration/survival;
~60% of embryonic melanocytes retained in kita-null then dying after ~4 dpf;
RAS/MAPK-dependent melanocyte-progenitor differentiation during regeneration.
Additional nuance from newer literature not in the cached primary set: an
erythroid-progenitor role (Oltova et al. 2020, preprint — kita required for
kit-ligand/Epo cooperation) and ovarian/oocyte expression (Yao & Ge 2010,
expression-based). Critically, the deep research explicitly assigns the
cutaneous sensory-axon / Src-family-kinase maintenance phenotype (Tuttle et al.
2022) to **kitb, NOT kita** — consistent with the fact that no sensory-axon term
was annotated to kita here.

## Gene identity and evolutionary context

kita is one of two zebrafish co-orthologs of mammalian *KIT*, arising from the
teleost whole-genome duplication; the paralog is *kitb*.
[PMID:17257055 "the two zebrafish copies arose from a duplication event in the teleost lineage"].
kita corresponds to the classical pigment-pattern mutant *sparse*
[PMID:10393121 "the pigment pattern mutation sparse corresponds to an orthologue of"].
kita retains the ancestral melanocyte/pigment role clearly, whereas kitb is
expressed differently (Rohon-Beard neurons, trigeminal ganglion, ear) and is not
involved in melanocyte development, i.e. does not compensate for kita in pigment
cells (Hultman et al. 2007; introduction of PMID:17257055).

## Molecular function (conserved core)

Class III receptor tyrosine kinase / SCF receptor. Domain architecture (UniProt):
5 extracellular Ig-like C2 domains (ligand binding + receptor contacts), single TM
helix (516-536), split cytoplasmic protein-kinase domain (580-922), ATP-binding
site and Mg2+ sites, multiple autophosphorylation tyrosines. UniProt: "Tyrosine-
protein kinase that acts as a cell-surface receptor for the cytokine kitlg/scf".
CATALYTIC ACTIVITY EC 2.7.10.1 (RHEA:10596). Belongs to the CSF-1/PDGF receptor
subfamily. PANTHER PTHR24416:SF46. Reactome: Signaling by SCF-KIT (R-DRE-1433557),
Regulation of KIT signaling, RAF/MAP kinase cascade, PIP3/AKT.

The cognate ligand in zebrafish is **kitla** (SCF/Kit-ligand ortholog): kitla
morphants phenocopy the kita null and kitla-induced hyperpigmentation is
kita-dependent [PMID:17257055 "kitla is the functional ligand to kita"];
[PMID:17257055 "most or all of the kita receptor's function in the embryo are promoted by its"].
This grounds the specific molecular function **stem cell factor receptor activity
(GO:0005020)** — more informative than the generic IBA `growth factor binding` and
IEA `cytokine binding` currently annotated.

## Core biological process

Kit signaling pathway (GO:0038109) / cell-surface RTK signaling (GO:0007169) at the
plasma membrane (GO:0005886), as part of a signaling receptor complex (GO:0043235).
These, plus the two molecular functions, are the CORE. Downstream lineage/
developmental outputs are treated as KEEP_AS_NON_CORE (mirrors the human KIT
review, where hematopoietic/mast/germ-cell/pigment outputs are all non-core).

## Zebrafish-specific physiology (from cached primary literature)

- **Melanocyte migration + survival** (embryonic): kita required for both.
  [PMID:10393121 "required both for normal migration and for survival of embryonic"] melanocytes.
- **Melanocyte differentiation**: NOT required during normal embryonic development,
  but required when melanoblast development is delayed
  [PMID:15300437 "for differentiation of embryonic melanocytes during normal development"];
  contrast with mammals where kit "is required for migration, survival and
  differentiation of all neural"-crest melanocytes
  [PMID:15300437 "is required for migration, survival and differentiation of all neural"].
- **Adult pigment pattern**: kita is required by early-metamorphic (EM)
  melanophores; kit mutants lack EM but retain kit-independent late-metamorphic (LM)
  melanophores [PMID:17287252 "require the kit receptor tyrosine kinase, as kit mutants lack these cells but"];
  [PMID:17287252 "kit-dependent EM melanophores that arise in a"] dispersed pattern.
- **Pigmentation** (discovery screen): *sparse* among 94 pigment loci
  [PMID:9007256 "we have isolated 285 mutations"] [PMID:9007256 "affecting all aspects of zebrafish larval pigmentation"].
- **Melanocyte stem cell (MSC) fate/establishment**: reduced Kit signaling reduces
  larval melanocyte regeneration via an MSC establishment defect
  [PMID:23364331 "kit functions in larval melanocyte regeneration to establish the MSC"];
  [PMID:23364331 "the regeneration defect in kita mutants is not due to defects in MSC recruitment"].
- **Melanophore survival / apoptosis**: kita-null (kitw34) melanophores die
  prematurely by apoptosis [PMID:23724125 "kitw34 zebrafish have a null mutation in kit tyrosine kinase receptor and only lose melanophores prematurely due to increased apoptosis"].
  (bnc2/bonaparte context: [PMID:19956727 "null alleles of sparse (kit) in zebrafish or a closely related species retain substantial numbers of melanophores"].)
- **GI motility**: kita (Sparse) required for coordinated GI motility via
  interstitial cells of Cajal (ICC) [PMID:23297728 "kit function is required for development of coordinated motility patterns" — actual: "kita function is required for development of coordinated motility patterns"];
  [PMID:23297728 "Sparse mutants exhibit a reduced contraction frequency and an enlarged GI tract"];
  [PMID:23297728 "Kit signaling is required for development and maintenance of ICC"].

## Key divergence from mammalian KIT

Unlike mouse/human KIT, zebrafish kita is **NOT essential for hematopoiesis or
primordial germ cell development**
[PMID:10393121 "not essential for hematopoiesis or primordial germ cell development"].
This is target-specific divergence following the teleost duplication (functions
partitioned between kita/kitb and/or with kit ligands kitla/kitlb). Consequently
the phylogenetic (IBA) annotations transferred from the ancestral Kit node for
hematopoietic progenitor / B-cell differentiation are kept but flagged NON-CORE
for kita, with the zebrafish dispensability noted.

## Annotation decisions summary

- Molecular function: MODIFY generic `protein kinase activity` → `transmembrane
  receptor protein tyrosine kinase activity`; ACCEPT `protein tyrosine kinase
  activity`, the two `transmembrane receptor protein tyrosine kinase activity`
  rows, and `ATP binding`. MODIFY `growth factor binding` (IBA) and `cytokine
  binding` (IEA) → `stem cell factor receptor activity` (GO:0005020), the specific
  ligand-binding function grounded on the kita–kitla relationship.
- Location/complex: ACCEPT `plasma membrane` (x2), `signaling receptor complex`.
- Core process: ACCEPT `Kit signaling pathway` (x2), `cell surface receptor
  protein tyrosine kinase signaling pathway`.
- Developmental/lineage outputs (melanocyte differentiation, migration,
  pigmentation, developmental pigmentation, melanocyte migration, melanocyte
  apoptotic process, stem cell fate commitment, GI smooth muscle contraction,
  positive regulation of proliferation / cell migration / JAK-STAT, cell
  migration): KEEP_AS_NON_CORE (downstream of the core receptor activity).
- Hematopoietic progenitor cell differentiation + B cell differentiation (IBA):
  KEEP_AS_NON_CORE, flagged as zebrafish-dispensable (divergence).
- `Fc receptor signaling pathway` (IEA from InterPro IPR027263): REMOVE — kita is
  the SCF receptor, not an Fc receptor; no biological basis for participation in
  the Fc receptor signaling pathway; this is a spurious InterPro2GO mapping.
- No `protein binding` (GO:0005515) rows present, so no REMOVE/MODIFY of that term
  needed here.
- No `NEW` terms proposed: the core MFs are already representable via ACCEPT/MODIFY;
  substrate/participation and comparator tests do not justify additional process
  terms.

## Re-review 2026-09-29
- Audit of the existing 53-row review (recently curated with a Kit-signaling module). No PENDING rows; actions left largely intact.
- Fixed the one IBA MODIFY row lacking propagation_review: GO:0019838 growth factor binding (IBA, family node PANTHER:PTN004704336) MODIFY -> GO:0005020 stem cell factor receptor activity. Added propagation_review (root_cause TERM_SCOPING_PROBLEM, GRANULARITY_MISMATCH): the type-III RTK family node correctly carries generic growth-factor binding, but kita's specific ligand is the SCF ortholog kitla [PMID:17257055 "kitla is the functional ligand to kita"], so the specific child term is the informative one.
- Added reference_review (relevance + VERIFIED correctness) to all 10 PMID references.
- Confirmed the two other MODIFY rows (GO:0004672 -> GO:0004714 RTK activity; GO:0019955 cytokine binding -> GO:0005020) and the REMOVE of GO:0038093 Fc receptor signaling pathway (IEA mis-mapping) as sound. Validation: 0 errors.

### Follow-up after PR review (2026-10-09)

- The GO:0038093 Fc receptor signaling pathway REMOVE row rested on the unreferenced claim that teleosts lack IgE and an FcepsilonRI alpha subunit. Cached the teleost immunoglobulin review PMID:33439286 (Bilal, Etayo & Hordvik, Immunogenetics 2021; abstract only) and added it to `references` with a reference_review (LOW relevance, VERIFIED), and the row now carries [PMID:33439286 "In teleosts, three immunoglobulin isotypes, IgM, IgT, and IgD, are present"].
- The abstract lists the complete teleost isotype set rather than naming IgE; the reason now says explicitly that the absence of IgE/FcepsilonRI alpha is inferred from that list and is not directly quotable from the cached abstract. No action changed. Validation: zero errors; the pre-existing deep-research warning remains.

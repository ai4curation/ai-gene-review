# mcm-4 (C. elegans) review notes

## Identity
- UniProt: Q95XQ8 (MCM4_CAEEL), 823 aa
- Gene: mcm-4; synonyms **let-358**, **lin-6**; ORF Y39G10AR.14
- WormBase locus; member of MCM2-7 family (PANTHER PTHR11630, "DNA REPLICATION LICENSING FACTOR MCM FAMILY MEMBER")
- Taxon: NCBITaxon:6239

## Core function (well established)
mcm-4 encodes the C. elegans ortholog of MCM4, a subunit of the heterohexameric
MCM2-7 pre-replication complex / replicative helicase. As part of the CMG
(CDC45–MCM–GINS) helicase it unwinds template DNA during S-phase. Conserved
roles: replication licensing, DNA synthesis (elongation), and the DNA replication
checkpoint coupling M-phase entry to S-phase completion.

## Key evidence from cached publications

### PMID:21146520 (Korzelius et al., 2011, Dev Biol) — full text available, PRIMARY
- Cloned **lin-6 and showed lin-6 = mcm-4**, encoding the C. elegans MCM4 ortholog,
  member of the MCM2-7 pre-RC / replicative helicase complex.
  [PMID:21146520 "lin-6 corresponds to mcm-4 and encodes an evolutionarily conserved component of the MCM2-7 pre-RC and replicative helicase complex"]
- lin-6/mcm-4 mutants lack DNA synthesis in postembryonic somatic lineages while
  entry into mitosis continues → **checkpoint defect** (M phase entry uncoupled from
  S phase completion). [PMID:21146520 "lin-6 is required for the checkpoint that couples M phase entry to S phase completion"]
- MCM-4 protein expressed in all dividing cells during embryonic and postembryonic
  development; **associates with chromatin in late anaphase**. → supports nucleus /
  chromosome / chromatin localization. [PMID:21146520 "associates with chromatin in late anaphase"]
- Tissue-specific: epidermis (hypodermis) expression sufficient to rescue growth
  retardation/lethality; somatic gonad and germline cope with loss of zygotic mcm-4.
- Supports GO: MCM complex, DNA replication, replication initiation, DNA strand
  elongation, replication checkpoint, nucleus, chromosome.
- EXP located_in chromosome and IDA located_in nucleus both trace to this paper.
- NAS premeiotic DNA replication, NAS MCM complex also from this paper (likely
  curator narrative statements).

### PMID:31283754 (Wang et al., 2019, PLoS Genet) — full text available, PRIMARY
- NMAD-1 (DNA demethylase) study. **NMAD-1 physically interacts with MCM-4** (and
  TOP-2), components of the DNA replication machinery.
  [PMID:31283754 "MCM-4 is a component of the minichromosome maintenance complex which is responsible for licensing origins for DNA replication and is the DNA helicase complex responsible for unwinding the DNA at the origins of replication"]
- Source of IPI "protein binding" (GO:0005515) annotation. Real interaction but
  "protein binding" is uninformative per curation guidelines.

### PMID:7262539 (Sulston & Horvitz, 1981, Genetics) — ABSTRACT ONLY (no full text)
- Classic "Isolation and genetic characterization of cell-lineage mutants of the
  nematode C. elegans" — the original lin mutant screen where **lin-6(e1466) was
  isolated**. [confirmed via PMID:21146520 "first systematic search for mutants with defects in the normally invariant postembryonic cell lineages... (Sulston and Horvitz, 1981)"]
- This is the basis for the IMP annotations to **nervous system development
  (GO:0007399), gonad development (GO:0008406), locomotion (GO:0040011)**.
- These are pleiotropic downstream phenotypes of a general postembryonic DNA
  replication defect in dividing cells — NOT evidence that mcm-4 has a dedicated
  developmental/neuronal/locomotor molecular role. Candidate for
  KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED. Cannot read full text (abstract only),
  so retain rather than REMOVE — defer to curator on the IMP, but mark non-core.

## Annotation triage summary (pre-agent)
- MF: DNA helicase activity (GO:0003678), single-stranded DNA helicase activity
  (GO:0017116, contributes_to), ssDNA binding (GO:0003697), DNA binding
  (GO:0003677), ATP binding (GO:0005524), ATP hydrolysis (GO:0016887) → core,
  consistent with MCM subunit acting within the hexamer.
- CC: MCM complex (GO:0042555), nucleus (GO:0005634), chromosome (GO:0005694) → core.
- BP: DNA replication, replication initiation, mitotic DNA replication initiation,
  DNA strand elongation, premeiotic DNA replication, BIR (GO:0000727) → replication
  processes; some IBA-propagated may be over-specific (e.g. BIR).
- BP developmental (nervous system, gonad, locomotion) → non-core pleiotropy.
- protein binding (IPI) → uninformative; NMAD-1 interaction is real.

## Deep research status
Falcon deep research (`just deep-research-falcon worm mcm-4 --fallback perplexity-lite`)
was launched in parallel with publication caching. The wrapper reported a 600s timeout
(and the `perplexity-lite` fallback was unavailable in this environment), but falcon in
fact completed after ~1406s and wrote `mcm-4-deep-research-falcon.md` (51 citations) plus
artifacts. The report **corroborates the entire review**: it confirms the
lin-6/let-358 = mcm-4 = MCM4 identity, the complex-level ATPase/helicase activities
(incl. the MCM4/6/7 subcomplex biochemistry), the replication checkpoint role, the
epidermis-specific requirement, and the nuclear→diffuse(NEBD)→late-anaphase chromatin
localization dynamics. No annotation decision needed changing.

New context (not annotation-changing): a 2024 study (Memar et al., Nat Commun) reports a
replication-*independent* role for the CMG helicase in asymmetric cell-fate divergence
(via the GINS subunit PSF-2, not mcm-4 directly), proposed to act through
chromatin/histone handling at the egl-1 locus. Captured as a new suggested_question and
noted in the deep-research reference_review; MCM-4's strongest evidence remains canonical
licensing/helicase. The deep-research file is now cited (additional_reference_ids +
supported_by) on the ssDNA helicase activity annotation.

### Thorough integration pass (follow-up)
Wove the deep-research findings into the relevant annotations beyond the single
ssDNA-helicase citation:
- DNA helicase activity (GO:0003678, IEA) and ATP hydrolysis (GO:0016887, IEA): added
  the MCM4/6/7 subcomplex biochemistry (intrinsic ssDNA-dependent ATP hydrolysis;
  ATPase/helicase with ATP hydrolysis in the MCM ring driving translocation/unwinding).
- nucleus (GO:0005634, IDA) and chromosome (GO:0005694, EXP): added the cell-cycle
  localization dynamics (nuclear interphase → diffuse at NEBD → not on metaphase
  chromatin → reassociates in late anaphase).
- Added Ruijtenberg, van den Heuvel & The 2011 (doi:10.5772/19397) to references,
  surfaced by deep research; marked correctness=UNVERIFIED because it has no PMID, is
  not in the GOA, and was not independently retrieved/read in this review.
All deep-research supporting_text quotes validate against the cached report.



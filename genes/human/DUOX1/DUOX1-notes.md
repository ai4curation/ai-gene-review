# DUOX1 notes


## 2026-09-08 paired human–horse review



DUOX1 is a membrane NADPH oxidase that assembles with DUOXA1 and generates extracellular hydrogen peroxide. Its transmembrane hemes and cytosolic FAD/NADPH-binding machinery conduct electron transfer, while intracellular EF-hand elements mediate calcium regulation. The extracellular N-terminal region has a peroxidase-like fold but lacks the intrinsic peroxidase activity of a conventional mammalian peroxidase. DUOX1-derived peroxide contributes to epithelial defense and redox signaling.

## Two domains with very different catalytic implications

The heme-containing membrane oxidase/dehydrogenase machinery transfers reducing equivalents from NADPH through FAD and hemes to oxygen. The extracellular peroxidase-like domain is a different structural region. Direct biochemical work finds that the isolated human peroxidase-like domain lacks heme binding and intrinsic peroxidase activity; the C. elegans homolog behaves differently. The human NOT-peroxidase annotation is therefore supported, without negating the heme required by the membrane oxidase. High- and low-calcium structures of DUOX1–DUOXA1 establish EF-hand-dependent conformational regulation. The selected horse deletion removes major elements of that regulatory region, making exact-sequence transfer much less secure than ordinary family identification. Hormone synthesis requires coupling peroxide production to separate peroxidases and the appropriate tissue context.

## Decisive inspected evidence

From [PMID:33420071](https://pubmed.ncbi.nlm.nih.gov/33420071/):

> Dual oxidases (DUOXs) produce hydrogen peroxide by transferring electrons from intracellular NADPH to extracellular oxygen. They are involved in many crucial biological processes and human diseases, especially in thyroid diseases. DUOXs are protein complexes co-assembled from the catalytic DUOX subunits and the auxiliary DUOXA subunits and their activities are regulated by intracellular calcium concentrations.

## Evidence inventory

- [PMID:19460756: Caenorhabditis elegans and human dual oxidase 1 (DUOX1) "peroxidase" domains: insights into heme binding and catalytic activity.](https://pubmed.ncbi.nlm.nih.gov/19460756/). [DOI:10.1074/jbc.M109.013581](https://doi.org/10.1074/jbc.M109.013581). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:33420071: Structures of human dual oxidase 1 complex in low-calcium and high-calcium states.](https://pubmed.ncbi.nlm.nih.gov/33420071/). [DOI:10.1038/s41467-020-20466-9](https://doi.org/10.1038/s41467-020-20466-9). Full text is available in the repository cache.
- [PMID:25761904: When an Intramolecular Disulfide Bridge Governs the Interaction of DUOX2 with Its Partner DUOXA2.](https://pubmed.ncbi.nlm.nih.gov/25761904/). [DOI:10.1089/ars.2015.6265](https://doi.org/10.1089/ars.2015.6265). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.

## Transfer to the selected horse protein

The exact target is [A0A9L0SQG9](https://www.uniprot.org/uniprotkb/A0A9L0SQG9/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/DUOX1/DUOX1-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: cell leading edge, cellular response to cytokine stimulus, cuticle development, protein binding, protein heterodimerization activity, regulation of thyroid hormone generation, response to cAMP, response to virus, superoxide anion generation, superoxide-generating NAD(P)H oxidase activity, thyroid hormone generation. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Re-reviewed all 75 existing annotations from scratch against the literature and the
PANTHER/PAINT evidence. No ProtNLM2 output was opened or used.

### Identity of the benchmark accession

Q9NRD9 is the canonical, reviewed UniProt entry for human DUOX1 (DUOX1_HUMAN, 1551 aa,
`Flags: Precursor`), the same product this folder is keyed to. It is not a fragment, an
isoform or an alternative gene model: the length matches the 1551-residue ThOX1 ORF
reported at cloning [PMID:10806195 "open reading frames of 1551 (ThOX1) and 1548 amino
acids (ThOX2)"], and all catalytic machinery is present — three EF-hand domains
(815-850, 851-886, 895-930), the ferric-oxidoreductase domain (1096-1236), the FAD-binding
FR-type domain (1270-1376), seven transmembrane segments in the record's feature table,
and heme, FAD, NADPH and Ca(2+) ligand sites. A second splice isoform (Q9NRD9-2,
VSP_017262/VSP_017263) exists and is recorded in `alternative_products`; no annotation in
GOA is isoform-scoped.

### Evolutionary grounding

Q9NRD9 is in PANTHER subfamily PTHR11972:SF75 (DUAL OXIDASE 1), with rat Q8CIY2, pig
Q8HZK3, dog Q9MZF4 and mouse A2AQ92. DUOX2 (Q9NRD8) is the sister subfamily SF67; the
C. elegans Duox bli-3 (O61213) is SF175, a different subfamily again.

The PAINT record (`interpro/panther/PTHR11972/PTHR11972-paint.tsv`) separates two activities
that the GOA rows conflate:

- `GO:0016174` NAD(P)H oxidase H2O2-forming activity sits at **PTN000944147**, the
  DUOX-specific node, seeded by Q9NRD9 itself plus DUOX2, pig DUOX2, dog DUOX1, fly Duox
  and *C. elegans* bli-3.
- `GO:0016175` superoxide-generating NAD(P)H oxidase activity and `GO:0042554` superoxide
  anion generation sit at **PTN000239643**, the deep NOX/DUOX ancestor, seeded by NOX-branch
  members (P04839/NOX2, Q96PH1/NOX5, Q9Y5S8, mouse Nox1/Nox3, dictyostelid NoxA/NoxB).

That is a deliberate curatorial split, and it matches the biochemistry: the mature thyroid
oxidase releases H2O2 rather than superoxide, and superoxide is seen only from the immature
ER form or when the DUOXA N-terminus is altered [PMID:15972824 "it was shown that mature
thyroid NADPH oxidase does not release O2*- but H2O2"; "the partially glycosylated form of
Duox2, located in the endoplasmic reticulum, generates superoxide in a calcium-dependent
manner"], with the DUOXA1 C-terminus directing DUOX1 output to H2O2 [PMID:22814254 "the
COOH-terminal end of DUOXA1 is responsible for DUOX1-dependent H(2)O(2) generation"].
Both superoxide rows were therefore MODIFYed to their H2O2 counterparts, with a
`propagation_review` recording the node inspection, rather than removed.

### Changes made (75 rows, all re-decided)

- ACCEPT 42, KEEP_AS_NON_CORE 19, MODIFY 11, REMOVE 2, TOO_GENERAL 1, UNDECIDED 0
  (the previous pass left 20 rows UNDECIDED; every one is now decided).
- **REMOVE `GO:0042335` cuticle development (IMP, PMID:11514595).** The phenotype is a
  *C. elegans* RNAi result [PMID:11514595 "Ce-Duox1 is expressed in hypodermal cells
  underlying the cuticle of larval animals."; "Thus, Ce-Duox catalyzes the cross-linking of
  tyrosine residues involved in the stabilization of cuticular extracellular matrix."].
  The paper's human work is a separate in vitro experiment on the expressed peroxidase
  domain. bli-3 is in subfamily SF175, not SF75, and its peroxidase-homology domain binds
  heme covalently while the human one does not [PMID:19460756 "In contrast, CeDUOX1(1-589)
  binds heme covalently, exhibits a modest peroxidase activity, but does not oxidize
  bromide ion."], so neither the phylogeny nor the chemistry licenses the transfer.
- **REMOVE `GO:0006979` response to oxidative stress (IEA, InterPro IPR010255).** The
  signature that triggers it is the peroxidase-homology domain, which in human DUOX1 binds
  no heme [PMID:33420071 "key residues for heme binding, such as the heme ligand histidine,
  are missing in the PHD of hDUOX1"], and the mapping inverts the biology: DUOX1 makes
  reactive oxygen rather than responding to it.
- **MODIFY the five bare `GO:0005515` rows to `GO:0046982`** protein heterodimerization
  activity (partners DUOXA1 Q1HG43 and DUOXA2 Q1HG44), per the repo protein-binding policy.
- **MODIFY `GO:0019221` cytokine-mediated signaling pathway to `GO:0071345`.** The cited
  experiment measured transcript induction [PMID:16111680 "Duox1 expression was increased
  several-fold by treatment with the Th2 cytokines IL-4 and IL-13"]; DUOX1 is a target of
  cytokine signalling, not a transducer within the pathway.
- **MODIFY `GO:0050661` NADP binding to `GO:0070402` NADPH binding** (descendant already
  carried, resolved in the structure).
- **TOO_GENERAL for `GO:0009615`** response to virus: `GO:0140374` antiviral innate immune
  response, kept here, is its descendant and is what the evidence shows.
- `GO:0051591` response to cAMP kept (non-core) with a recorded caveat: the IDA's own source
  reports the opposite of what it is cited for [PMID:15062544 "functional studies show that
  both hThOX promoters are not positively controlled by cAMP"]; the term survives on the
  curated UniProt induction statement ("INDUCTION: By forskolin (at protein level).").
- The NOT `GO:0004601` row is kept, now with independent structural support
  [PMID:33420071 "we did not observe any heme density in the structure of hDUOX1 PHD,
  suggesting PHD is probably not enzymatic functional in term of peroxidase activity"],
  and with the conflicting PMID:11514595 report recorded in that paper's `reference_review`
  (correctness: DISPUTED) rather than ignored.
- `description` rewritten as a project-independent summary; one `core_function`
  (`GO:0016174`, in `GO:0043020`, at `GO:0016324`/`GO:0005886`, directly involved in
  `GO:0050665`); `reference_review` added to all 15 literature references.

### Ontology gap recorded

UniProt gives DUOX1 a third curated catalytic activity, NAADPH + O2 + H(+) = NAADP(+) +
H2O2 (Rhea:86235, ECO:0000269|PubMed:34784249), and GO has no molecular function for it
(`GO:0016174` is defined on NAD(P)H). Recorded as a `proposed_new_terms` entry only; no
annotation is proposed, and the T-cell calcium phenotype in that paper was DUOX2-specific
for the early microdomains.

### Family review

`interpro/panther/PTHR11972/PTHR11972-review.yaml` places Q9NRD9 in SF75 and treats
`GO:0004601` as UNRESOLVED at family level because of the PMID:11514595 / PMID:19460756
conflict. No disagreement with the subfamily placement used here. The family review's
caution that "ferric reduction, superoxide production and hydrogen-peroxide production must
be assigned to the appropriate branch" is exactly what the two MODIFYs implement; a note
for whoever next edits that file is that the branch assignment is now resolvable from the
PAINT node split described above.

### Deep research

`just deep-research-falcon human DUOX1 --fallback perplexity-lite` failed: the falcon
provider errored and the perplexity-lite fallback timed out at 600 s. No new
deep-research file was produced, and none was fabricated. The review was written from the
15 cached publications (two with full text: PMID:33420071 and PMID:39126279, plus
PMID:11514595), the UniProt record and the PANTHER/PAINT files.

### Modules

No module under `modules/` references DUOX1 or Q9NRD9, and `gocams/index.tsv` has no entry
for it. None created.

### Relative to review next

Mouse Duox1 (UniProtKB:A2AQ92, MGI:2139422, 1551 aa, PTHR11972:SF75 — the same subfamily),
the true ortholog and the donor of the ISS (GO_REF:0000024) and Ensembl Compara
(GO_REF:0000107) rows on this gene, and the organism in which the in vivo antiviral
phenotype was established [PMID:34168077 "Upon influenza airway challenge, Duox1-/- mice
have enhanced mortality, morbidity, and impaired lung viral clearance."]. There is no
`genes/mouse/Duox1/` folder, so it needs a review.

## 2026-10-27 — Mouse ortholog (`genes/mouse/Duox1/`), `PTHR11972` family update, and mucosal DUOX1–LPO module

- Completed the paired ortholog review in `genes/mouse/Duox1/Duox1-ai-review.yaml` (`UniProtKB:A2AQ92`, `MGI:2139422`), incorporating the 3.2–3.3 Å cryo-EM structures of the mouse DUOX1–DUOXA1 complex in 1:1 heterodimer and 2:2 dimer-of-heterodimer states (`PMID:32929281`), the in vivo airway influenza defense study (`PMID:34168077`), and the bladder urothelial mechanosensory ATP–Ca2+–DUOX1 H2O2 study (`PMID:20233719`).
- Confirmed consistent action decisions across the human (`DUOX1`) and mouse (`Duox1`) ortholog pair, including removal of the erroneous `GO:0042335` (`cuticle development`) and `GO:0004601` (`peroxidase activity`) / `GO:0006979` (`response to oxidative stress`) annotations that had propagated between human `DUOX1`, *C. elegans* `bli-3`, and mouse `Duox1`.
- Created the reusable pathway module `modules/mucosal_duox1_lactoperoxidase_antimicrobial_system.yaml` capturing the apical epithelial DUOX1–DUOXA1 H2O2 generation and secreted lactoperoxidase (`LPO`) hypothiocyanite (`OSCN-`) antimicrobial/antiviral system, and updated `interpro/panther/PTHR11972/PTHR11972-review.yaml` with the PAINT node split (`PTN000944147` vs `PTN000239643`) and structural findings from `PMID:32929281` and `PMID:33420071`.


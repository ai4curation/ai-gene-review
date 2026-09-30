# BBS10 (Q8TAM1) — Gene Review Notes

## Summary of identity and function

BBS10 (C12orf58; HGNC:26291) is a **vertebrate-specific, chaperonin-like protein** of the
group II / TCP-1 (CCT/TRiC) chaperonin family. It is one of three "chaperonin-like" BBS
proteins (with MKKS/BBS6 and BBS12). Together with the CCT/TRiC chaperonin and BBS7 these
form the **BBS-chaperonin complex**, which acts as an **assembly factor (chaperone) for the
BBSome** — it is NOT a stable structural subunit of the mature BBSome (GO:0034464).

- "BBS10 encodes a vertebrate-specific chaperonin-like protein and is a major BBS locus."
  [PMID:16582908 title]. UniProt: "Belongs to the TCP-1 chaperonin family"; RecName "BBSome
  complex assembly protein BBS10"; FUNCTION "Probable molecular chaperone that assists the
  folding of proteins upon ATP hydrolysis."
- The catalytic chaperonin/ATPase activity of BBS10 itself has NOT been demonstrated
  biochemically; it is inferred from the conserved Cpn60/TCP-1 (Pfam PF00118; InterPro
  IPR002423) domain. UniProt flags FUNCTION as "Probable."

## BBS-chaperonin complex / BBSome assembly

[PMID:20080638 "a novel complex composed of three chaperonin-like BBS proteins (BBS6, BBS10,
and BBS12) and CCT/TRiC family chaperonins mediates BBSome assembly... Chaperonin-like BBS
proteins interact with a subset of BBSome subunits and promote their association with CCT
chaperonins. CCT activity is essential for BBSome assembly... BBS6, BBS10, and BBS12 are
necessary for BBSome assembly"].
- UniProt SUBUNIT: "Component of a complex composed at least of MKKS, BBS10, BBS12, TCP1,
  CCT2, CCT3, CCT4, CCT5 and CCT8" [ECO:0000269|PubMed:20080638].
- UniProt INTERACTION: BBS10 binds BBS12 (Q6ZW61), BBS7 (Q8IWZ6), BBS9 (Q3SYG4).
- Disease mutations (e.g. R34P, V240G, S311A, S329L) reduce BBS10 interaction with BBS7/BBS9
  and/or BBS12, linking assembly-factor function to pathology [PMID:20080638; PMID:16582908].
- D81N mutagenesis "Greatly decreases all interactions with BBS7, BBS9 and BBS12 indicating
  that this residue may be required for overall protein conformation" (UniProt FT MUTAGEN).

[PMID:22500027 "Three additional BBS genes (BBS6, BBS10, and BBS12) have homology to type II
chaperonins and interact with CCT/TRiC proteins and BBS7 to form a complex termed the
BBS-chaperonin complex. This complex is required for BBSome assembly... we show that the
BBS-chaperonin complex plays a role in BBS7 stability."] — full text available. This paper
characterizes the ordered, chaperonin-assisted assembly of the BBSome core
(BBS7-BBS2-BBS9), supporting the IMP annotation to regulation of protein-containing complex
assembly (GO:0043254) and chaperone-mediated protein complex assembly (GO:0051131).

## Subcellular location

- UniProt SUBCELLULAR LOCATION: "Cell projection, cilium"; Note "Located within the basal
  body of the primary cilium of differentiating preadipocytes" [ECO:0000269|PubMed:19190184].
  Basis for IEA GO:0005929 (cilium, UniProtKB-SubCell). BBS10 acts as a cytoplasmic assembly
  chaperone; the ciliary/basal-body localization is reported in the adipogenesis context.

## Transcriptional regulation annotation (GO:0061629) — scrutiny

[PMID:22302990 abstract] is primarily about **BBS7** having a nuclear role and interacting
with the PcG protein RNF2 (Q99496). "Our data supports a similar role for other BBS proteins."
The IPI annotation of BBS10 → RNA Pol II transcription factor binding (with RNF2, UniProtKB:
Q99496), assigned by MGI, is peripheral and not a core function of BBS10. Full text not in
cache (full_text_available: false) — defer rather than remove; mark as non-core /
over-annotation candidate.

## Photoreceptor / cilium phenotype annotations (PMID:17980398) — scrutiny

[PMID:17980398 abstract] "Retinal morphology in patients with BBS1 and BBS10 related
Bardet-Biedl Syndrome evaluated by Fourier-domain optical coherence tomography." This is a
**clinical OCT imaging study** describing retinal dystrophy and photoreceptor disruption in
BBS1- and BBS10-mutation patients. It documents a disease phenotype (loss-of-function ->
retinal degeneration) but does NOT provide mechanistic evidence that BBS10 protein is
directly "involved in" photoreceptor cell maintenance (GO:0045494) or "non-motile cilium
assembly" (GO:1905515) at the molecular level. These BHF-UCL IMP annotations are
phenotype-derived and represent downstream/indirect consequences via impaired BBSome
assembly, not a direct molecular role. Full text available. Treat as non-core; the cilium
assembly defect is indirect (BBS10 is an assembly chaperone, not a structural ciliary/IFT
protein).

## Interactome (protein binding) annotations

- IPI GO:0005515 protein binding from PMID:20080638 (partners BBS7 Q8IWZ6, BBS9 Q3SYG4,
  BBS12 Q6ZW61) — bona fide BBS-chaperonin complex interactions.
- IPI GO:0005515 from PMID:28514442 (BioPlex; "Architecture of the human interactome") and
  PMID:33961781 ("Dual proteome-scale networks", BioPlex 3.0) — both with BBS7 (Q8IWZ6).
  High-throughput AP-MS; consistent with the BBS10-BBS7 interaction.
Per curation guidelines, GO:0005515 "protein binding" is uninformative and should not be
treated as core; the underlying interactions are better captured by the assembly-factor BP
terms and complex membership.

## GO term reference notes
- GO:0051082 "unfolded protein binding" is now an OBSOLETE term (deprecated in favor of
  protein folding chaperone activity). Do NOT propose it.
- GO:0044183 "protein folding chaperone": "Binding to a protein or a protein-containing
  complex to assist the protein folding process."
- GO:0140662 "ATP-dependent protein folding chaperone": same, "driven by ATP hydrolysis."
- GO:0034464 "BBSome": structural ciliary complex of the 7 core BBS proteins + BBIP10 —
  BBS10 is NOT a member (it is the assembly factor).

## Core function conclusion
BBS10's core, defining role is as an **ATP-binding, chaperonin-like assembly factor** that,
within the BBS-chaperonin complex (with MKKS/BBS6, BBS12, CCT/TRiC, BBS7), mediates assembly
of the BBSome core. BP: chaperone-mediated protein complex assembly (GO:0051131) and
regulation of protein-containing complex assembly (GO:0043254). MF: ATP binding
(GO:0005524), with probable protein-folding-chaperone activity (GO:0044183 / GO:0140662, not
experimentally proven). All ciliary/retinal phenotypes are downstream of impaired BBSome
assembly.

## ClinGen project re-review — 2026-09-30

This re-review retains the twelve inherited source assertions and restores two partner-specific assertions from the unchanged GOA file. The normal local seeder, run with title fetching disabled and output confined to a temporary file, also restores eight missing supporting-entity lists. The fourteen distinct source tuples now match the raw GOA records. It supersedes the earlier vertebrate-specific description, the ATP-binding catalytic core, and the two authored NEW assertions for folding-chaperone activity and cytoplasm. Those two additions were assigned an IBA/GO_REF provenance without an actual PAINT assertion; withdrawing them does not delete a source annotation or assert that BBS10 cannot occur in the cytoplasm.

The recovered PMID:20080638 sources name BBS12/Q6ZW61 and BBS7/Q8IWZ6. The inherited partner from that paper is BBS9/Q3SYG4. Selected original Results explicitly describe the corresponding co-immunoprecipitation associations; no purified affinity or substrate-folding activity is inferred. The BioPlex sources name BBS7, with their precise supplementary-record limitations retained. Each recovered source received a separate annotation consultation. The final fourteen source decisions are four ACCEPT, eight KEEP_AS_NON_CORE and two MODIFY, with no NEW assertion.

### Assembly function and molecular uncertainty

The demonstrated role is BBSome assembly. BBS10 associates with BBS proteins and helps organize the BBS-chaperonin machinery. Its substoichiometric recovery supports a transient or regulatory role, without establishing constitutive membership in either that machinery or the mature BBSome. The normal cache for [PMID:20080638](https://pubmed.ncbi.nlm.nih.gov/20080638/) is abstract-only. Selected original Results and Discussion were read separately, including the D81N interaction experiments. Disruption of several associations can reflect an altered protein conformation; it is not a selective test of ATP binding or hydrolysis.

In human 293T cells, BBS10 depletion and overexpression have opposing effects on BBS6 association with CCT proteins. These results support regulation of the assembly machinery; chaperone-mediated BBSome assembly is its related downstream process. Patient fibroblasts also show defective BBSome assembly. The adjacent thermolysin experiments concern Bbs6-null cells and cannot be attributed to a direct BBS10 folding assay. [PMID:22500027](https://pubmed.ncbi.nlm.nih.gov/22500027/)

The single core therefore records these two experimentally supported processes and an explicit molecular-function gap. It does not assign a folding MF, a CCT ATPase activity, or stable BBSome membership. The original ATP-binding IEA is retained as non-core sequence-based evidence. GO:0044183 requires assistance with folding of a bound protein; association with a folding system alone does not establish that activity. The ontology's open [assembly-chaperone term request](https://github.com/geneontology/go-ontology/issues/31631) is relevant context, not an existing GO identifier to assert.

### Localization, partner specificity and cell context

The cilium source annotation is refined to GO:0036064, ciliary basal body. Original immunolocalization Results include endogenous BBS10 in human primary renal proximal tubular epithelial cells and differentiating human preadipocytes. The Falcon artifact's IMCD wording is not used as the basis for this refinement. Selected primary Results and figure captions were inspected; microscopy images and supplementary Methods were not independently assessed. [PMID:19190184](https://pubmed.ncbi.nlm.nih.gov/19190184/)

Ciliogenesis varies with experimental context. Two BBS10 RNAi reagents reduce ciliation in differentiating human preadipocytes, whereas the c91fs95 patient fibroblasts in the assembly study retain cilia despite defective BBSome formation. The clinical retinal study supplies a separate human phenotype. These observations support contextual non-core associations without a universal requirement for BBS10 in every ciliogenesis assay. [PMID:19190184](https://pubmed.ncbi.nlm.nih.gov/19190184/), [PMID:22500027](https://pubmed.ncbi.nlm.nih.gov/22500027/), [PMID:17980398](https://pubmed.ncbi.nlm.nih.gov/17980398/)

The BBS10-RNF2 row is refined to ubiquitin protein ligase binding. The original Figure 3C and Results explicitly include tagged BBS10 co-immunoprecipitation with tagged RNF2; the Methods identify HEK293 cells. The endogenous interaction, yeast assay and downstream transcriptional experiments emphasize other BBS proteins and are not transferred to BBS10. RNF2 is the E3-ligase partner, not an established sequence-specific RNA polymerase II DNA-binding transcription factor. The normal cache remains abstract-only; the original selected Results, caption and Methods were inspected separately. [PMID:22302990](https://pubmed.ncbi.nlm.nih.gov/22302990/)

Supported generic interactions are deliberately retained as non-core under the supplied ActionEnum. The exact high-throughput supplementary bait-prey records were not independently resolved, so no specific cell line, purified binary contact or additional activity is invented from those rows. [PMID:28514442](https://pubmed.ncbi.nlm.nih.gov/28514442/), [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/)

### Evolution and research boundaries

The later phylogenetic analysis reports chaperonin-like BBS homologs outside vertebrates. This removes support for the earlier vertebrate-specific generalization, without constituting a new phylogenetic reconstruction or biochemical activity inference here. The complete indexed abstract and limited indexed primary passages were read. [PMID:24010126](https://pubmed.ncbi.nlm.nih.gov/24010126/)

The existing Falcon report and its artifact are preserved as prior provider research. They are not primary verification of any citation. All available source annotations received an independent annotation consultation. The GO-CAM index contains no BBS10/Q8TAM1 match. Complete article images, supplements and PAINT family topology were not reconstructed. Publication full-text flags were checked against actual content; partial caches were not treated as complete papers.

A later primary study, [PMID:40914337](https://pubmed.ncbi.nlm.nih.gov/40914337/), was checked before finalization. Its complete PubMed abstract reports reduced stability and partner association for BBS10/BBS12 variants, with altered ciliary length in human-cell models. The publisher access attempt returned403; full Results, Methods and figures remain unread. The abstract's primary-cilium localization wording does not distinguish the basal body from the axoneme and does not establish exclusive localization. The basal-body refinement remains grounded in the independently inspected earlier localization experiments. This later work supports variant-dependent assembly context without resolving autonomous ATPase or folding activity. It is added as a bounded reference, not as a new process annotation.

### Validation of this revision

Focused schema, term, reference and best-practice validation passed on 2026-09-30. The 6 advisories comprise 5 supported generic-binding rows retained as non-core under the supplied ActionEnum and one unused-provider-evidence advisory. The unchanged provider report is a lead map; primary publications support the annotation decisions. Rendering passed. No repository-wide validation pass is claimed.


## 2026-09-30 — evidence and citation follow-up

Short verbatim anchors now accompany the basal-body refinement, the context-specific ciliogenesis evidence and the two experimental assembly annotations. The BBS-chaperonin regulation quote is moved from the core to its experimental row; the redundant fragment in the molecular-function gap is removed. The RNF2 refinement has a structured source citation and an explicit link to the inspected Results/Figure 3C/Methods. Its abstract-only normal cache does not contain the BBS10 assay, so no replacement quotation is invented. The basal-body and ciliogenesis snippets refer to the BBS10/BBS12 experiments; the complete conditions remain in the rationales and reference assessment.

The biological summary now includes TCP-1/CCT family membership and the BBS7-BBS2-BBS9 assembly intermediate. The core distinguishes participation in BBSome assembly from regulation of the machinery's formation. The molecular activity remains unresolved; no proposed catalytic term is added without direct evidence. Colonless PMID identifiers and missing spaces in the review are corrected. Earlier notes containing 'returned403' should read 'returned 403'; the original journal entries remain intact.

The PMID:17980398 and PMID:33961781 caches contain full-text content. Their earlier full-text-unavailable flags were incorrect and are removed; limited reading and uninspected supplementary interaction records remain explicitly documented. Five supported generic associations remain KEEP_AS_NON_CORE under the supplied ActionEnum. In particular, independent BBS10-BBS7 co-immunoprecipitation supports the biological interaction represented by the two BioPlex rows, without claiming that the exact BioPlex records were independently audited. Neither REMOVE nor UNDECIDED is selected solely to satisfy the generic-binding advisory. No source tuple, action or alternative product is changed.

# Bacterial methionine-cycle preflight — 2026-11-07

The existing module is suitable for a dedicated audit, but its MetE branch is not a reliable generic bacterial remethylation model. The six existing cycle reviews comprise 58 rows. KT2440 PP_2698/Q88JF1 is a compact 344-aa MetE-like protein next to DUF1852 PP_2699/Q88JF0; the most defensible working hypothesis is MesD/MesX, not a demonstrated canonical folate-dependent MetE reaction. Preserve this as an inference until the gene consultant completes target-specific assessment.

The frozen main reference is `bb89a377830600d2850d64215e0da94a47a06c6a`. `module-original.yaml`, `main-snapshot.json`, and `existing/` retain the exact main versions. No curated files, ordinary publication caches, provider reports, or other worktrees were changed in this preflight. No normal publication fetches or new gene reviews were run.

## Existing work and ownership

The exact module path was checked against every changed-file page of 278 open PRs. No dedicated taxonomic methionine-cycle audit was found. Two open PRs overlap mechanically: #5076 bulk PANTHER grounding and #3802 validation/representative normalization. Their exact patches and heads are captured; neither supersedes this source review. #5076 proposes eukaryotic exemplars in the bacterial module, so its patch should not be adopted blindly.

ECOLI CheR P07364 already has a COMPLETE 18-row review on main. The main review can supply the concrete SAM-to-SAH methylation exemplar without a new curation assertion or universal family assignment. PR #6100 owns a different, unmerged CheR revision. Reuse main byte-identically or coordinate with that owner; do not silently import its changes. `cher-overlap.json` distinguishes both hashes. Native E. coli receptor-vesicle methylation is supported by the accessible abstract of PMID15916610; the curated UniProt reaction explicitly produces SAH. Some classic CheR structural/purification references concern Salmonella, so do not present every cited assay as native E. coli.

Five of the six declared PANTHER families have existing review documents; PTHR35799 (LuxS) does not. Family membership, source PAINT placement, donor specificity and loss assertions still require the dedicated family audit. No new family/PTN IDs were guessed here.

## Proposed biological boundary

Retain the bacterial cycle from methionine activation, through a chemically demonstrated SAH-producing SAM methyl-transfer reaction, to homocysteine recovery and remethylation. Neither all SAM-dependent enzymes nor a generic methyltransferase-like fold qualifies: radical cleavage, aminopropyl transfer, and SAM used only as a cofactor can have different products. LuxS catalytic SRH cleavage is distinct from downstream AI-2 signaling phenotypes.

The alternatives should not be declared exhaustive after encoding only SahH/Pfs-LuxS and MetE/MetH. Source-supported additions are:

* **SAH deamination then SIH hydrolysis:** Thermotoga maritima MSB8 TM_0936/Q9X034 and TM_0172/O51933 were both purified and tested in PMID17603473. The latter also hydrolyzes SAH directly. This is a matched biochemical route, not confirmed native flux: the paper expressly leaves an alternative physiological adenosine-deaminase role open. The official 2PLM polymer matches current Q9X034 exactly, 406/406 aa. The earlier possible numbering discrepancy was investigated and rejected.
* **MesD plus MesX:** native ADP1 ACIAD3523/Q6F6Z8 and ACIAD3524/Q6F6Z7 give the smallest exact strain-matched comparative pair. PMID18319726 establishes native methionine auxotrophy and ACIAD3524 complementation; PMID33534785 identifies the compact protein as MesD. The actual oxygen/folate/B12 complementation experiments in the latter paper use S. koreensis DSMZ15582 Ga0059261_2929/2928. Do not label those as ADP1 assays. No exact current UniProt mapping was established for the Sphingomonas loci, so no accession is proposed for them.
* **MesB/core-MetE:** D. mccartyi CBDB1 cbdbA481/CAI82680, current A0A916P3S8_DEHMC, is directly characterized in PMID32034217. Purified protein transfers methyl from methylcobalamin to homocysteine and fails the tested folate-donor reaction. Native donation by AcsCD or another corrinoid protein remains hypothesized; an unmeasured donor interface must not be manufactured as a complete pathway node.

The minimum matched panels and official seed identifiers are in `candidate-panels.json`. These new pairs/exemplars establish individual alternatives; they are not complete native methionine-cycle panels. For a complete canonical E. coli candidate, the existing Pfs/LuxS and main CheR can be combined with reviewed MetK P0A817 and one of canonical MetE P25665 or MetH P13009, subject to exact source/strain validation. A MYCS2 mc²155 MetE/MetH pair (A0R6Q9/A0QZX6) adds native cofactor-context evidence without claiming a full cycle or universal essentiality.

## Evidence limits that affect the model

MesD's physiological methyl donor is unknown. MesX is experimentally required in the characterized pair, but its precise methyl-generating chemistry is unresolved. Oxygen dependence in the Sphingomonas experiment should be explicit, and a conserved-pair inference must remain distinct from a direct KT2440 assay.

The SAH-deamination branch has direct paired enzymology but no native flux proof. It should pass an appropriately labeled biochemical-capacity profile and remain uncertain under a strict demonstrated-native-flux profile. Absence of that proof does not justify deleting the alternative chemistry.

MetH presence does not guarantee activity without usable cobalamin. ADP1 and M. smegmatis illustrate different cofactor contexts; the latter's native riboswitch alters which alternative supports growth. PMID35289639 corrects authorship/acknowledgments of the M. smegmatis study, not its result. The authentic correction text is archived separately.

PMID42570567, electronically published 2026-08-07 (despite a December issue date), adds X. campestris XC1 MesD, S-methylmethionine-dependent MmuM, and split MetHaHb evidence. Only its abstract was read here. Full text and exact XC1 identity remain unresolved; do not substitute an ATCC33913 protein. This flags a real additional donor/context boundary for the audit, not a validated complete representative panel.

## Access and reproducibility

`reference-ledger.json` contains 12 manually assessed sources and 11 short, checked quotations. Three genuine reviews were assessed. PMID36891755 was acquired as complete XML. PMID21166890's relevant full publisher-rendered sections were read. PMID18953685's indexed full-text catalytic section was read, but direct PMC requests returned a challenge and Europe PMC XML failed; there is no complete local full-text claim for that review. Failed XML/challenge responses are retained as access records and must not be used as scientific text. The incorrectly decoded supplementary PDF text is not supporting evidence; the actual PDF and correctly extracted table are retained.

Run `uv run python <this-directory>/build_preflight.py` to regenerate the ledgers and quote/identity proof. Source paths in this cache-only preflight are deliberately frozen here. A subsequent dedicated audit must copy selected bytes into durable analysis paths with an explicit old/new path and SHA256 receipt, rather than silently repoint this handoff. Public source reads contain no credentials. No provider report was authored or fabricated.

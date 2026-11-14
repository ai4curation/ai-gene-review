# Mla literature, taxon and identity preflight

Read-only consultation, 2026-11-07. Authoritative snapshot: origin/main commit `bb89a377830600d2850d64215e0da94a47a06c6a`. All writes are confined to this ignored preflight directory. No normal publication caches, curated records, worktrees or PRs were created or changed. `main-snapshot.json` identifies the module, twelve COMPLETE gene reviews (105 ordered rows), six family reviews and three module histories. Snapshot bytes are independently checked against the pinned commit.

## Duplicate-work assessment

The captured sweep inspected all file pages for 280 open PRs. `expanded-overlap.json` tests the exact module prefix and every existing member/family folder, including companion notes and source files. Only [PR5076](https://github.com/ai4curation/ai-gene-review/pull/5076), head `97f8a6c606f51aeb2a364cf14c43850833410473`, overlaps: its Mla patch changes six PSEPK `preferred_term` labels and adds the ECOLI MlaB representative P64602 plus the PTHR35849:SF1 selector to the existing MlaB role. There are no overlapping gene or family files. This is a broad PANTHER grounding change, not a duplicate scientific/taxon audit. Proceed with the dedicated audit while preserving the valid label and MlaB grounding changes and handling the eventual module merge explicitly. This is a dated snapshot, not a guarantee against future PR changes.

## Sources read and evidence boundaries

`source-ledger.json` contains manually adjudicated, source-exact short excerpts and source hashes. Three genuine reviews were read in full relevant sections: PMID36459067, PMID38802775 and PMID35850151. The last is a 2022 review with a 2026 PMC manuscript deposit; do not call it a 2026 review. PMID31420510 is explicitly a Perspective and is additional context, not a fourth assay or a substitute for the three reviews. Failed accesses are retained and clarified in `access-clarifications.json`; a failed XML request does not erase the subsequently acquired complete HTML.

The strongest characterized directional model is ATP-coupled retrograde phospholipid transfer. PMID34873038 measures spontaneous exchange in both directions between MlaC and MlaFEDB, with ATP enhancing retrograde transfer and suppressing reverse movement. It does not establish powered anterograde transport. PMID39080293 tests the MlaC–MlaD interface and reconstituted transfer; PMID40168124 directly measures outer-membrane complex-to-carrier loading and PG enrichment. These point-to-point/reconstituted measurements must not be called an independently measured native whole-cell flux in every lineage.

The ATCC17978 anterograde interpretation in PMID30638443 is materially challenged by PMID32880370, including membrane fractionation and an obgE strain-background confound. The corrective OMV pulse-chase experiment is itself a proxy, not a purified complete transport assay. Record the evidence dispute rather than representing both directions as equally established interchangeable module variants.

Two inherited source-scope problems need correction during the audit:

* PMID28388411 directly measures MlaC binding to MlaFEDB and MlaA–OmpF by biolayer interferometry. Its statement about lipid handoff belongs to the proposed discussion model. Preserve the binding/structure finding and use later direct transfer work for measured lipid movement.
* The inherited PMID39080293 text calls the probe phosphatidyl glycerol (PE). The actual relevant figure caption identifies NBD-PE. Correct the biological finding from the actual source, without silently rewriting the immutable publication cache.

PMID31235958 was available here only as the pinned cached abstract. Its ATP-independent MlaD-to-MlaC transfer claim can be reported at that access scope, not as a newly read full primary. PMC6424457/PMID30845186 was acquired as a Neisseria discovery candidate but was not used to establish a final representative panel.

## Recommended additional representatives

The smallest useful addition is the five-protein Bordetella reference panel plus one Pseudomonas carrier exemplar. It adds a characterized MlaB-independent architecture and a distinct carrier cargo observation without padding the panel with a second complete gamma-proteobacterial set.

| Suggested organism/gene | Official accession | Role | Evidence boundary |
|---|---|---|---|
| BORPE/BP3757 | Q7VT00 | MlaF ATPase | Native B213 perturbation; reference-lineage bridge |
| BORPE/BP3758 | Q7VSZ9 | MlaE membrane component | Conserved locus/architecture inference in the same operon |
| BORPE/BP3759 | Q7VSZ8 | MlaD MCE component | Conserved locus/architecture inference |
| BORPE/BP3760 | Q7VSZ7 | MlaA outer-membrane component | Conserved locus/architecture inference |
| BORPE/BP3761 | Q7VSZ6 | MlaC carrier | Conserved locus/architecture inference |
| PSEAE/ttg2D (PA4453) | Q9HVW4 | MlaC-family carrier | Native PAO1 cargo plus separately bounded heterologous structure |

Official UniProt snapshots establish the five Bordetella Tohama I loci and taxon257313. PMID36518166 Figure1A identifies their F/E/D/A/C order. Authentic Supplementary TableS1 identifies B213 as a streptomycin-resistant derivative of Tohama I. This is a strain-lineage/locus bridge; complete experimental B213 protein sequences were not compared byte-for-byte. The official B213 query returned no entries, which is not evidence of biological absence. Native evidence directly perturbs MlaF, not each of the five proteins independently. The strongest surface-PE phenotype involves combined MlaF/OMPLA disruption, and growth depends on medium/context. Do not claim unconditional essentiality or directly measured whole-pathway direction from these phenotypes.

PMID33837253 distinguishes PAO1 periplasmic cargo from the heterologously produced structural construct. Official RCSB6HSY entity1 contains an exact 193-residue segment of the 215-residue Q9HVW4 precursor, with construct additions recorded in `identity-proof.json`. It is not a claim that the 207-residue deposited construct is identical to the entire precursor. Two diacyl phospholipids or one cardiolipin can occupy the carrier; permeability phenotypes do not demonstrate antibiotic export. No candidate review exists at the proposed paths in the pinned main snapshot.

## Module and family recommendations

Preserve the broad bacterial diderm mechanism with positive cargo/interface/context gates. Do not narrow the taxon scope simply to keep universal six-protein requirements. The current universal MlaB requirement needs an alternative compatible F/E/D realization lacking identifiable B: B. pertussis primary evidence supports this architectural distinction. In E. coli, MlaB supports ATPase stability/assembly, and overexpressed MlaF can rescue a B deletion under tested conditions (PMID32602838). Neither observation means B is universally dispensable, nor that every generic ABC ATPase can replace MlaF.

Keep the mechanistic roles distinct: MlaA outer-membrane lipid handling with compatible porin context; MlaC soluble carrier; MlaD periplasmic MCE assembly/interface; MlaE membrane transport component; MlaF ATPase; MlaB lineage/context-dependent assembly or regulatory contribution. Use positive complex contributions instead of assigning an isolated subunit the complete coupled transport reaction. E. coli OmpC/F observations do not establish those exact porins as universal partners in Bordetella or Pseudomonas.

Existing family reviews are PTHR30035 (A), PTHR36573 (C), PTHR43023 (F), PTHR30188 (E), PTHR33371 (D), PTHR35849 (B). These are candidates for phylogenetic/term-scope reassessment, not universal activity selectors. Exact official membership snapshots for the new panel are provided. Do not equate generic ABC, MCE, STAS or shared-fold membership with the complete phospholipid route; retain compatible taxon, cargo and partner evidence. Pqi/Let, Tol–Pal and PldA provide adjacent mechanisms/context, not automatically substitutable Mla roles. Chloroplast TGD and mycobacterial Mce/YrbE systems are not verified Mla phospholipid realizers merely because of structural homology.

The extended Bacteroides MlaD architecture discussed in the 2022 review remains predictive/speculative, not a measured MlaA/C-independent full pathway. The 2026 Pseudomonas MlaC–MlaD and Campylobacter MlaC preprints are discovery leads only. Proposed Campylobacter RND coupling has no demonstrated lipid-transfer interface or established accession bridge here. Keep these as explicit gaps rather than invented alternative nodes.

## Reproducibility and release

Run `uv run python .cache/module-audit-logs/mla-preflight-20261107/verify.py` from the original root worktree. It verifies pinned source bytes, exact excerpts, identity sequence comparisons, the limited PR patch and supplement authenticity. Network acquisition scripts preserve provenance but need not be rerun to verify the frozen material. The final handoff covers every artifact here, including unsuccessful access bodies clearly marked as such. Transfer into the dedicated audit must preserve bytes and record old/new path hashes; do not silently repoint this original release. No module or gene history is warranted for this cache-only preflight.

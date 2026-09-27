# WIP1 (Arabidopsis thaliana, Q8GXA4) review notes

Context: plant KASH-side comparator for `modules/linc_complex.yaml`. Human comparators: SYNE1-4 (nesprins), KASH5.

## Biology (with provenance)

- WIPs interact with RanGAP1 in vivo; colocalize at NE and cell plate; WIP1 on outer NE by immunogold; wip1 wip2 wip3 dislocates RanGAP1 from root-tip NE [PMID:17600715].
- WIP-WIT heterocomplex anchors RanGAP1; WIP1 raises WIT1-RanGAP1 binding; no WIP1 self-interaction or WIP1-WIP2a/WIP3 interaction in planta [PMID:18591351 "By contrast, WIP1 does not interact with itself"].
- WIPs are plant KASH proteins binding AtSUN1/2 via the perinuclear tail (C-terminus ...PEPDTVVPT; VVPT deletion reduces SUN binding); required for WIP1 and RanGAP1 NE localization and elongated nuclear shape [PMID:22270916].
- Cter-SUN and mid-SUN (SUN3) bind the WIP1 KASH domain [PMID:25217773].
- WIT2 recruits myosin XI-i to SUN-WIP bridges for nuclear shape [PMID:25759303]; myosin XI-i/WIT linker for nuclear movement [PMID:23973298].
- AtPSS1 kinesin binds WIP1 (Y2H, BiFC) [PMID:25330379]; meiotic role speculative.

## Citation problem

- PMID:20579133 (GOA IntAct IPI, WIP1-RANGAP1) resolves to a root-canal-sealer dental paper -> WRONG_IDENTIFIER. IntAct PSICQUIC: record IMEx IM-19345, first author "Xu et al. (2007)"; live QuickGO still carries the row. Likely intended PMID:17600715, but that paper has IMEx IM-19776, so no replacement asserted.

## Decisions

- SUN1/SUN2/SUN3/WIT2 and WIT1 (myosin study) protein-binding rows -> MODIFY GO:0140444.
- RanGAP1 rows and WIT1 (RanGAP study) -> MODIFY GO:0043495.
- AtPSS1 -> MODIFY GO:0019894 kinesin binding.
- WIP2 (x2) and PYL9 -> REMOVE (uninformative).
- Homo-/heterodimerization -> UNDECIDED (conflicting in planta data; source abstract-only).
- Cell plate -> KEEP_AS_NON_CORE (WIPs dispensable for RanGAP1 cell-plate targeting [PMID:19011093]).
- NEW GO:0005640 nuclear outer membrane (IDA, PMID:17600715).

## Deep research

Falcon deep research for WIP1 had not been generated at time of the initial review (see update below).

## Module implications

- WIP1 is a functional analog of animal KASH proteins (KASH-like tail, SUN binding, ONM) but not a PANTHER/InterPro KASH homolog (PTHR34562, IPR044696 WIP1/2/3); supports modelling plant KASH as a separate taxon variant.
- Cytoskeletal coupling is indirect (via WIT2 to actin motor myosin XI-i), analogous to nesprin-3 coupling via plectin; plant LINC is actin-based, so GO:0106094 ("microtubule tethering") fits poorly.
- Plant-specific extra role: anchoring RanGAP1 at the NE (a role taken by RanBP2 in animals).

## 2026-09-27 update: Falcon deep research incorporated

- Read `WIP1-deep-research-falcon.md` (retrieval support only). Claims checked against cached primary papers:
  - SUN2-WIP1-RanGAP1 bridging co-IP design confirmed in PMID:22270916 ("AtRanGAP1-GFP and RFP-Myc-AtSUN2 were coexpressed with either AtWIP1 or AtWIP1XT in N. benthamiana leaves."); added to the RanGAP1 (PMID:17600715) row together with the deep-research statement.
  - VVPT requirement for SUN1 binding confirmed in PMID:22270916 ("both the exchange of the PNS tail and the deletion of VVPT greatly reduced binding between AtWIP1 and AtSUN1"); added to the SUN1 row.
  - Pollen vegetative-nucleus migration: verified and cached PMID:26409047 (PubMed esummary: "SUN anchors pollen WIP-WIT complexes at the vegetative nuclear envelope and is necessary for pollen tube targeting and fertility", J Exp Bot 2015). Added to references, description and core function 1 support; the nuclear-migration question now cites it. No NEW process term added: evidence is dominant-negative SUN2 and wip/wit quintuple mutants (family-level), so paralog-specific participation is not resolved.
  - Redundancy caveat from deep research cited on the nucleus organization IGI row.
- No actions changed. Status remains COMPLETE; validation passes.

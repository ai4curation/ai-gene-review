

## 2026-11-07 nitrogen-regulatory PTS review

Reviewed all original rows and core functions under the annotation-reviewer policy. Complete original reviews and removed author reference/core assertions are preserved additively in `analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107/before.json`; raw UniProt, GOA, existing provider output and historical row payloads are unchanged. No newly authored annotation rows were added. Module/GOA records were removed from scientific reference lists because they describe assertions rather than independent evidence.

PMID:18296519 establishes the principal native PEP → PtsP → NPr/PtsO → PtsN relay. Exact primary text: “Our results show that the source of phosphate available to the system is PEP and that the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI(Ntr) to NPr to EIIA(Ntr).” The full article at `analysis/module_audits/bacterial_nitrogen_regulatory_pts/literature-acquisition-20261107/PMID_18296519-pmc-body.txt` identifies MAD2 (a KT2440 derivative), nonpolar mutants and plasmid-expressed E-tagged PtsN, followed by native electrophoresis/immunoblotting. These are physiological phosphorylation-state experiments, not target purified-protein kinetic measurements. Exact Results: “This indicated that PtsO is the only phosphate-delivering protein for PtsN under these conditions.” refers to the carbohydrate-free test condition. Fructose enables FruB cross-talk; succinate does not. Do not make PtsP/NPr universally necessary across media, equate pathway order with physical assembly, or import E. coli reverse-transfer kinetics into native P. putida.

Official GO definitions/ancestry are frozen in `analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107/go-terms.json` and `go-ancestors.json`. GO:0009401 and GO:0008982 describe carbohydrate uptake/phosphorylation, not every PTS-like protein. Target native evidence, rather than the broad family label alone, distinguishes the regulatory branch. Cytoplasm for PtsP/NPr is an explicit functional/architecture inference; their ARBA-only localization statements are not independent support. PtsN cytoplasmic fluorescence is experimentally reported.

PMID:26224366 reports: “Measurements of kdpFp promoter activity in different pts mutants showed that PtsN is responsible for repression of kdpFABC transcription.” Bacterial two-hybrid interaction supports a target-specific physical signaling link, but the accessible abstract does not distinguish kinase inhibition, phosphatase activation or other mechanisms. E. coli kinase activation (PMID:19400808) is comparative, not target activity. The kinase-activator IEA is UNDECIDED; the former general kinase-regulator replacement/core is withdrawn, rather than manufacturing an inhibitor conclusion. Historical potassium-transport regulation remains justified as regulation of transporter expression, not measured potassium flux.

PMID:21236318 reports: “Both genetic and biochemical evidence revealed that the non-phosphorylated form of PtsN is the protein species that inhibits PDH.” The described methods are tagged-PtsN co-immunoprecipitation/MS, isogenic cellular-extract activity and fluorescent-fusion co-localization. Retain enzyme-inhibitor activity with these limits, not an assertion of purified binary inhibition or isolated AceE kinetics. The core uses this supported effector activity with intracellular signaling; the prior MF-less relay core is subsumed in its context. Signal participation rests on actual downstream effector work, not being a phosphoacceptor substrate alone. All four historical NEW rows are retained.

Primary-source access: the canonical 18296519 cache is partial, and the parent acquired the complete PMC body additively. Native KdpD (26224366) and PDH (21236318) sources remain abstract-only after acquisition attempts; claims are limited to explicitly reported methods/results. Existing generated research is retained as secondary discovery material. The centrally attempted Falcon request failed authentication (HTTP 403); no fabricated provider report was created. Manual primary-source review supplies the assessment. No family evolutionary placement or universal cross-species effector is asserted.


## 2026-11-08 — consistent Ntr/sugar scope and evidence limits

The action discriminator is target evidence, not species labels or donor count: P. putida has a native sugar-independent route and a documented failure of PtsN to replace fructose EIIA; Caulobacter separates its Ntr effectors from sugar permeases and its mannose assignments originate in an incorrect transporter EC mapping. E. coli has measured cross-system phosphate exchange in vitro but lacks demonstrated native sugar-uptake participation for the Ntr branch, so physiological process assignment is over-annotation rather than an absolute negative. Bona fide E. coli/Bacillus HPr controls retain the sugar process because they feed sugar-specific EIIA proteins in the native carbohydrate route; common ancestry at PTN002135312 does not erase this functional divergence.

Where the only localization assertion is ARBA-derived, compartment adjudication remains UNDECIDED and the core location is omitted. PtsN–KdpD target interaction plus regulatory output supports direction-neutral regulator inference without claiming an isolated kinase assay. Source annotation payloads are unchanged.


## 2026-11-11 — target-specific cross-system evidence

The term describes carbohydrate transport/phosphorylation, whereas native PtsN acts in a sugar-independent regulatory branch. The native Discussion also reports that PtsN cannot replace the EIIA(Fru) domain of FruB for phosphorylation of FruA. Shared EIIA architecture and conditional FruB input do not establish sugar-transport activity. For PtsN, the direct failure to phosphorylate FruA through EIIA substitution supports REMOVE despite its receipt of FruB-derived phosphate; receiving that input does not perform the sugar-transfer step.


## 2026-11-11 — incoming main journal retained

The following is the incoming review journal; current target-specific adjudication follows below.

# ptsN (Pseudomonas putida KT2440) notes

## Provenance

- Re-reviewed while completing the bacterial nitrogen-regulatory PTS module
  (modules/bacterial_nitrogen_regulatory_pts.yaml). No new deep-research provider
  report was generated: no provider API key is configured in this session.
- Primary evidence: PMID:18296519 (full text; in vivo relay order PEP to PtsP to
  PtsO/NPr to PtsN, and FruB cross-talk), PMID:17416664, PMID:26224366 and
  PMID:21236318 (abstracts).

## Decisions in this pass

- Sugar-PTS process and carbohydrate phosphotransferase rows remain removed, now with
  quoted support ("comprise a branch of the system unrelated to sugar traffic") and
  source_defects naming the InterPro2GO / UniRule mappings.
- Correct-but-general MF rows (transferase, kinase, phosphorus-group transferase) are
  MODIFY to the specific activity rather than KEEP_AS_NON_CORE.
- For NPr (PP_0948) the phosphocarrier step is captured with GO:0016775
  (phosphotransferase activity, nitrogenous group as acceptor), matching the E. coli
  NPr review (genes/ECOLI/ptsO).


## 2026-11-11 — reconcile merged parallel PTS review

Retain target-specific cross-system judgments and assay limits from this audit. Incorporate incoming experimentally coded proposals and retire their historical TAS predecessors in place where present. Incoming source-defect records are retained when consistent with the current action; broad sugar-process rejection is superseded where direct target cross-system chemistry supports over-annotation. Core relay activities and all original machine source rows remain unchanged.

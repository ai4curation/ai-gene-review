

## 2026-11-07 nitrogen-regulatory PTS review

Reviewed all original rows and core functions under the annotation-reviewer policy. Complete original reviews and removed author reference/core assertions are preserved additively in `analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107/before.json`; raw UniProt, GOA, existing provider output and historical row payloads are unchanged. No newly authored annotation rows were added. Module/GOA records were removed from scientific reference lists because they describe assertions rather than independent evidence.

PMID:18296519 establishes the principal native PEP → PtsP → NPr/PtsO → PtsN relay. Exact primary text: “Our results show that the source of phosphate available to the system is PEP and that the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI(Ntr) to NPr to EIIA(Ntr).” The full article at `analysis/module_audits/bacterial_nitrogen_regulatory_pts/literature-acquisition-20261107/PMID_18296519-pmc-body.txt` identifies MAD2 (a KT2440 derivative), nonpolar mutants and plasmid-expressed E-tagged PtsN, followed by native electrophoresis/immunoblotting. These are physiological phosphorylation-state experiments, not target purified-protein kinetic measurements. Exact Results: “This indicated that PtsO is the only phosphate-delivering protein for PtsN under these conditions.” refers to the carbohydrate-free test condition. Fructose enables FruB cross-talk; succinate does not. Do not make PtsP/NPr universally necessary across media, equate pathway order with physical assembly, or import E. coli reverse-transfer kinetics into native P. putida.

Official GO definitions/ancestry are frozen in `analysis/module_audits/bacterial_nitrogen_regulatory_pts/psepk-review-20261107/go-terms.json` and `go-ancestors.json`. GO:0009401 and GO:0008982 describe carbohydrate uptake/phosphorylation, not every PTS-like protein. Target native evidence, rather than the broad family label alone, distinguishes the regulatory branch. Cytoplasm for PtsP/NPr is an explicit functional/architecture inference; their ARBA-only localization statements are not independent support. PtsN cytoplasmic fluorescence is experimentally reported.

The prior kinase rejection conflated kinase with ATP-only independent catalysis. GO:0016301 requires phosphate transfer, “usually from ATP”; it therefore accommodates the demonstrated NPr phosphohistidine-donor role. ACCEPT kinase and MODIFY generic transferase to that existing term. The historical NEW GO:0016772 is retained in place with `retired: true`: it is a verified ancestor of the accepted existing kinase term and supplies no additional coverage. Its original identity/evidence/qualifier and NEW lifecycle remain intact, with the old judgment in before.json. GO:0004673 requires ATP and GO:0009927 names a hybrid-kinase/response-regulator relay, so neither is an appropriate more specific replacement. Historical protein phosphorylation is retained because NPr transfers phosphate, not merely because it is phosphorylated. Current ptsH/PP_0948 corresponds to literature ptsO/NPr; this does not turn every HPr-family member into NPr.

Primary-source access: the canonical 18296519 cache is partial, and the parent acquired the complete PMC body additively. Native KdpD (26224366) and PDH (21236318) sources remain abstract-only after acquisition attempts; claims are limited to explicitly reported methods/results. Existing generated research is retained as secondary discovery material. The centrally attempted Falcon request failed authentication (HTTP 403); no fabricated provider report was created. Manual primary-source review supplies the assessment. No family evolutionary placement or universal cross-species effector is asserted.

Final chemical-specificity refinement in this session: the same-role E. coli HPr control and live GO examination identified GO:0016775, phosphotransferase activity, nitrogenous group as acceptor. This supersedes the intermediate kinase-ACCEPT choice above. Both existing MF rows are MODIFY to GO:0016775; core function uses it. It is a descendant of GO:0016740/GO:0016772, but not GO:0016301: the kinase change is explicitly a chemical-acceptor refinement across branches, not a false ancestry claim or a claim that non-ATP transfer cannot be kinase activity. Immediate children were checked; none describes the NPr His-to-His transfer more accurately. Snapshots are npr-phosphotransfer-{term,ancestors,children}.json. The redundant historical NEW GO:0016772 remains retired.


## 2026-11-08 — consistent Ntr/sugar scope and evidence limits

The action discriminator is target evidence, not species labels or donor count: P. putida has a native sugar-independent route and a documented failure of PtsN to replace fructose EIIA; Caulobacter separates its Ntr effectors from sugar permeases and its mannose assignments originate in an incorrect transporter EC mapping. E. coli has measured cross-system phosphate exchange in vitro but lacks demonstrated native sugar-uptake participation for the Ntr branch, so physiological process assignment is over-annotation rather than an absolute negative. Bona fide E. coli/Bacillus HPr controls retain the sugar process because they feed sugar-specific EIIA proteins in the native carbohydrate route; common ancestry at PTN002135312 does not erase this functional divergence.

Where the only localization assertion is ARBA-derived, compartment adjudication remains UNDECIDED and the core location is omitted. PtsN–KdpD target interaction plus regulatory output supports direction-neutral regulator inference without claiming an isolated kinase assay. Source annotation payloads are unchanged.


## 2026-11-10 — phosphate-flow direction and propagation status

The P. putida NPr/EINtr sugar-process assignment is over-annotated in light of real in vivo FruB-to-Ntr cross talk, without borrowing the PtsN-specific negative replacement assay. E. coli EINtr GlcNAc rejection now has propagation metadata matching its measured acceptor-specificity argument. Original annotation payloads are unchanged.


## 2026-11-11 — target-specific cross-system evidence

Native P. putida NPr receives phosphate from FruB in vivo, so cross-system flow involving this target is demonstrated. That input does not establish that NPr contributes to coupled sugar uptake and phosphorylation; the physiological sugar-process assignment is therefore marked over-annotated. The direction is FruB to NPr, and the PtsN-specific failure to substitute for fructose EIIA is not a negative assay of NPr.


## 2026-11-11 — incoming main journal retained

The following is the incoming review journal; current target-specific adjudication follows below.

# ptsH (Pseudomonas putida KT2440) notes

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


## 2026-11-11 — review follow-up: evidence and source routing

Quote the Discussion inference that FruB delivers phosphate to NPr where that target-specific claim distinguishes NPr from PtsP. Route InterPro2GO and TreeGrafter source defects to INTERPRO and PANTHER respectively, retaining their claims and requested corrections. No annotation payload or action changes.

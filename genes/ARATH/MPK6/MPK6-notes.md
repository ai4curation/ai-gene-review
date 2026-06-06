# MPK6 (Q39026, At2g43790) — curation notes

## Identity and core molecular function
- Arabidopsis mitogen-activated protein kinase 6; CMGC/MAPK family, TEY-motif (TXY motif at 221-223). EC 2.7.11.24. Kinase domain residues 63-348; ATP-binding K92 (invariant Lys) essential.
- Core MF = MAP kinase activity (GO:0004707) / protein serine/threonine kinase activity. Activated by dual phosphorylation on Thr221/Tyr223 [PMID:10713056 "AtMPK6 is phosphorylated on threonine and tyrosine residues in elicited cells"].
- Substrate consensus is proline-directed L/P-x-S/T-P-R/K [PMID:22631074 "a preference towards the sequence L/P-P/X-S-P-R/K for both kinases"].
- K92M/K93M abolish kinase activity (UniProt MUTAGEN) [PMID:11875555 "MUTAGENESIS OF LYS-92 AND LYS-93"]. Crystal structures 5CI6, 6DTL.

## Upstream activators (MAPKKs) — these are the IPI "protein binding" partners
- MKK2 (Q9S7U9), MKK4 (O80397), MKK5 (Q8RXG3), MKK6 (Q9FJV0); also MKK3, MKK7, MKK9. MAPKKKs: MEKK1, YODA, ANP1, MKKK20.
- These IPI bare protein-binding annotations (PMID:15225555, 19513235, 21798944, 32612234, 27913741) are uninformative and were marked REMOVE; the cascade relationship is captured by MAPK cascade (GO:0000165).

## Substrates (also annotated as bare protein binding -> REMOVE)
- ERF104 (Q9FKG1) [PMID:19416906 "the in vivo enzyme-substrate interaction of the Arabidopsis thaliana MAP kinase, MPK6, with an ethylene response factor (ERF104)"]
- MYB41 (Q9M0J5), Ser251 [PMID:22575450 "Ser(251) in MYB41 was identified as the site phosphorylated by MPK6"]
- VQ4 (O82170), IKU1/VQ14 (Q5M750) [PMID:24750137 "target a subclass of 'VQ-motif'-containing proteins to regulate immune responses"]
- LIP5 (Q9SZ15) [PMID:25010425 "LIP5 is a target of pathogen-responsive ... MPKs"]
- PTI1-4/CARK3 (O80719), OXI1 [PMID:21276203 "OXI1 and PTI1-4 were substrates of MPK3 and MPK6 in vitro"]
- ICE1 (AT3G26744) [PMID:29056553 "MPK3- and MPK6-Mediated ICE1 Phosphorylation Negatively Regulates ICE1 Stability and Freezing Tolerance"]
- BASL (Q5BPF3), YDA (Q9CAD5) [PMID:25843888 "BASL polarity protein controls a MAPK signaling feedback loop"]
- AHL13 (AT4G17950) [PMID:33419940 "AT-hook motif nuclear localized protein AHL13 in PAMP-triggered immunity"]
- WRKY34/WRKY2 [PMID:24830428 "Phosphorylation of a WRKY transcription factor by MAPKs is required for pollen development"]
- Also ACS2/ACS6 and EIN3 (UniProt FUNCTION; ethylene), SPCH (stomatal).

## Negative regulators (phosphatases) — phosphatase binding GO:0019902 kept (informative)
- PP2C AP2C1; PTP1/MKP1 (O82656) [PMID:19789277, PMID:27029354]; MKP2/DSPTP1B (Q9M8K7) [PMID:20626661].
- PTP1 IPI from PMID:27029354 is annotated as phosphatase binding (GO:0019902) — kept as ACCEPT since it is more informative than bare protein binding.

## Localization
- Cytoplasm (resting) and nucleus (upon activation/phosphorylation) [PMID:15500467 "activation and nuclear translocation ... during ozone exposure"; PMID:31235876 nuclear, stomatal].
- Cytosol HDA [PMID:28887381]. Cell cortex via BASL recruitment [PMID:25843888]. Preprophase band, phragmoplast, TGN, PM in dividing root cells [PMID:19832943 "distinct fine spots in the pre-prophase band and phragmoplast ... plasma membrane (PM) and the trans-Golgi network (TGN)"].

## Pleiotropy / biological processes (mostly KEEP_AS_NON_CORE)
- Immunity (FLS2->MEKK1-MKK4/MKK5-MPK3/MPK6) [PMID:11875555]; camalexin biosynthesis [PMID:18378893]; priming [PMID:19318610]; bacterial/fungal defense [PMID:11875555, 21947882].
- Hormones: ethylene [PMID:12628921], jasmonate (MKK3-MPK6, MYC2) [PMID:17369371], ABA (MKK1/MKK5) [PMID:18248592, 27913741].
- Abiotic stress: ROS/oxidative/H2O2 [PMID:10717008, 11577197, 17933903], osmotic [PMID:12220631], cold/salt (MKK2) [PMID:15225555], freezing (ICE1) [PMID:29056553], UV-B [PMID:21790814], abiotic activation [PMID:11123804], harpin [PMID:11500556].
- Development: stomatal patterning/ACD [PMID:25843888, 31235876], inflorescence architecture (ERECTA) [PMID:23263767], ovule [PMID:18364464], pollen development/tube guidance [PMID:24830428, 24717717], root development/cell division [PMID:19832943], leaf senescence (MKK9) [PMID:19251906], L-glutamate root response [PMID:29344832].
- Strong functional redundancy with MPK3 throughout (mpk3 mpk6 double often embryo-lethal).

## Curation decisions summary
- 76 existing_annotations reviewed (matches 76 non-header GOA rows after header).
- ACCEPT (28): core MF (MAP kinase / protein serine kinase / protein kinase activity, ATP binding), MAPK cascade, signal-transduction terms, principal localizations (nucleus, cytoplasm, cytosol), phosphatase binding, protein phosphorylation.
- KEEP_AS_NON_CORE (33): the many downstream biological processes and specialized localizations (cell cortex, TGN, phragmoplast, preprophase band) for this pleiotropic kinase.
- REMOVE (15): all 15 bare GO:0005515 protein binding IPI entries (uninformative; partners are MKKs/substrates better captured by cascade/kinase terms). Phosphatase binding (GO:0019902) retained as the informative alternative for phosphatase interactions.
- No publications were inaccessible (all 43 cached), so no UNDECIDED was needed.

## Proposed
- New MF term idea: "MAP kinase substrate binding" (child of protein kinase binding GO:0019901) to capture the many kinase-substrate IPIs informatively instead of discarding them as generic protein binding.

## Deep research synthesis (Falcon / Edison Scientific, file:ARATH/MPK6/MPK6-deep-research-falcon.md)
The Falcon deep-research report corroborates and does not contradict the existing review. Key points used to strengthen `supported_by` evidence:
- Core MF: MPK6 is a "Proline-directed CMGC MAP kinase; terminal kinase in MAPK cascades activated by dual Thr/Tyr phosphorylation in the TxY motif" that "phosphorylates downstream substrates including transcription factors, enzymes, RNA-metabolism proteins, and developmental regulators, often redundantly with MPK3." Added to MAP kinase activity, protein serine kinase activity and core_functions.
- MAPK cascade architecture: "MAPKs are terminal kinases in a conserved signaling architecture in which upstream kinases sequentially activate MAP2Ks and then MAPKs." Added to GO:0000165.
- Immunity (defense response to bacterium): "the MEKK1–MKK4/5–MPK3/MPK6 PTI module downstream of FLS2 that contributes to pathogen resistance"; "MPK6 is a core component of immune MAPK cascades activated by pattern recognition receptors."
- Ethylene: "MPK6 phosphorylates ACC synthase isoforms (e.g., ACS6) to affect stability and ethylene output" — supports response to ethylene.
- Development (stomatal): "MPK3/MPK6 phosphorylate SPEECHLESS (SPCH) downstream of the YODA–MKK4/5 module, modulating stomatal initiation and lineage progression" — supports nucleus localization and developmental core function.
- Freezing/ICE1: compiled substrates "include MYB41, MYB15, HsfA2, ICE1, DCP1 ... with outcomes such as enhanced DNA binding, altered protein stability, and nuclear accumulation" — supports response to freezing (ICE1).
- Localization: substrates span nucleus and cytoplasm — "This implies a functional distribution spanning nucleus and cytoplasm"; "classic reports note stress-triggered nuclear translocation of MAPKs."
- New 2023-2024 findings NOT added as GOA annotations (no verifiable GO IDs in current GOA/UniProt): MPK6 in stress granules / P-bodies via DCP1 phosphorylation (He et al. 2024 preprint); MYB36 phosphosites in endodermal SGN3/CIF signaling (Ma et al. 2024, Nature Plants); cat2-1 / glutathione modulation of flg22-induced MPK3/6 kinetics (Yang et al. 2024 preprint). These are recorded here for future review but are largely preprints and would need verifiable curated GO terms before annotation.
- No `action: UNDECIDED` entries existed; none required resolution (all 43 cited publications were accessible).

## PR #1417 review fix (2026-06-06): title-as-evidence supporting_text

- GO:0019902 phosphatase binding (original_reference_id PMID:27029354, IPI vs PTP1/O82656 — confirmed against GOA line 55). The original reference IS correct: PMID:27029354 directly documents the MPK6-PTP1 physical interaction by BiFC ("PTP1 interacted with MPK6 in the cytoplasm and nucleus (Fig. 7, lane 4, panel 4)"). The problem was the supporting_text being the bare paper title (about SnRK1). Replaced with that verbatim BiFC quote and added PMID:19789277 via additional_reference_ids with verbatim quote ("PROTEIN TYROSINE PHOSPHATASE1 (PTP1) also interacts with MPK6, but the ptp1 null mutant shows no aberrant growth phenotype"). original_reference_id left as PMID:27029354 per GOA.
- Other bare-title supporting_text replaced with real verbatim quotes on ACCEPT/KEEP annotations:
  - GO:0005634 nucleus (IEA, PMID:15500467) and GO:0005737 cytoplasm (PMID:15500467): title fragment -> "activated AtMPK3 and AtMPK6 are translocated to the nucleus during the early stages of O3 treatment".
  - GO:0005938 cell cortex (two entries, PMID:25843888): title / paraphrase -> verbatim "Phosphorylated BASL functions as a scaffold and recruits the MAPKKK YODA and MPK3/6 to spatially concentrate signaling at the cortex". (The earlier "Recruited by BASL at the cell cortex in a polarized manner" was a paraphrase, not an exact substring.)
- Remaining bare-title supporting_text instances are all on action: REMOVE annotations (uninformative protein binding being removed) and high-throughput interactome screens; left as-is as lower priority.
- Validation: `uv run ai-gene-review validate genes/ARATH/MPK6/MPK6-ai-review.yaml` -> Valid (2 pre-existing unrelated warnings). All supporting_text now exact substrings of cited sources.

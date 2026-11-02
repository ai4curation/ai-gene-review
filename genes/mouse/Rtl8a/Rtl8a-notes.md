# Rtl8a notes

Mouse Rtl8a/Rtl8b encode identical 113-aa capsid-only proteins; rodent-specific N-terminal NLS; nuclear(nucleoli), and nucleus+cytoplasm in PFC neurons [PMID:39875098 "the former in the nuclei (nucleoli) and the latter in the cytoplasm"; "these proteins are localized in both the nucleus (indicated by arrows) and cytoplasm of neurons"]. Rtl8a/8b DKO: late-onset obesity, reduced social response, apathy, reduced GABRB2 [PMID:39875098 "become obese from young adulthood"]. No GOA annotations -> NEW only.
Conserved adaptor role from human RTL8-UBQLN2/PEG10 [PMID:40680123; PMID:35247097].
NEW: nucleus (IDA), protein-macromolecule adaptor activity (ISS), positive regulation of protein localization to nucleus (ISS).

## Deep research integration (OpenScientist, 2026-10-24)

Report read as leads and checked against cached sources.

- Contradiction: the report says endogenous mouse Rtl8a loss-of-function phenotypes "are not yet well characterized in the retrieved literature". The Rtl8a/8b double-knockout study [PMID:39875098] already characterizes late-onset obesity, reduced social response and apathy-like behaviour; the report missed it. The review is unchanged on this point.
- Verified and added: the UBQLN2-RTL8 interaction was confirmed in mouse brain [PMID:35247097 "confirmed the interaction between UBQLN2 and RTL8 both in vitro using recombinant proteins and in vivo using mouse brain tissue"], added to the adaptor activity row. RTL8 is incorporated into PEG10 VLPs and lowers their abundance [PMID:39775359 "the closely related gene product RTL8 could be incorporated into PEG10-derived VLPs and decreased their abundance"], added to the core function description and support. Note that 39775359 used human RTL8C.
- Nucleolar localization: human RTL8 "Under endogenous and overexpressed conditions, RTL8 localizes to nucleoli." [PMID:35247097]; the mouse paper says "in the nuclei (nucleoli)" [PMID:39875098]. The nucleus NEW row was kept rather than narrowed to nucleolus, because in prefrontal-cortex neurons the mouse signal is nuclear plus cytoplasmic without a nucleolar call; nucleolus (GO:0005730) is a reasonable future refinement.
- Stress-granule recruitment of UBQLN2 by PEG10 requires RTL8 [PMID:40680123]; no stress-granule location asserted for RTL8 itself.
- The report's paralog-collective caveat (assays detect "RTL8" collectively) is quoted as support for the existing knowledge gap.

No action changes.

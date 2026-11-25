# CASP7 notes

## 2026-09-30

- Seeded and completed the human CASP7 review from cached PubMed records,
  Reactome, UniProt, GOA, GO-CAM models, and the PTHR10454 PAINT context.
- Accepted CASP7's core activity as an Asp-directed cysteine endopeptidase in
  apoptotic execution and kept the broad `GO:0006915 apoptotic process` PAINT
  and TAS rows as `MODIFY` to `GO:0097194 execution phase of apoptosis`.
- Captured the CASP7-specific N-terminal exosite/RNA mechanism from
  PMID:31586028: CASP7 binds RNA and other nucleic acids through lysines in its
  N terminus, and RNA bridges CASP7 to PARP1 and other RNA-binding substrates
  to enhance proteolysis.
- Kept the TNF receptosome and membrane-pore repair branch as a distinct CASP7
  core role: CASP7 proteolytically matures pro-acid sphingomyelinase/SMPD1 in
  support of extracellular ceramide production and membrane repair, represented
  in the local SMPD1 pore-repair GO-CAMs.
- Removed uninformative high-throughput `GO:0005515 protein binding` rows from
  BioPlex and binary interactome screens, while leaving the PMID:11084335 IAP
  row `UNDECIDED` because the cached ML-IAP/BIRC7 abstract does not verify the
  GOA BIRC2-CASP7 edge.
- Removed the CAFA-derived DFF40/CAD catalytic rows that used CASP7 as a
  staurosporine readout in PMID:22253444 rather than establishing CASP7
  nuclease or endopeptidase activity.
- Treated abstract-only or ambiguous papers cautiously: ATP11C cleavage
  (PMID:24904167), p23/telomerase regulation (PMID:19740745), the 2023 GSDMD
  paper (PMID:37327784), and PAK2-dependent CASP7 localization rows
  (PMID:21555521) are `UNDECIDED` where the abstract does not prove a
  CASP7-specific assertion.
- Marked the broad electronic `GO:0009617 response to bacterium` row as
  over-annotated for CASP7 because the supported biology is the more direct
  SMPD1 protein-maturation step downstream of membrane damage.


## 2026-10-25 comparative apoptotic-execution review

Systematically examined all 101 rows, preserving every imported annotation payload. Decisions judge the biological claim, not the evidence code: independently established cysteine endopeptidase activity, cytosolic/nuclear localization and apoptotic execution are retained/refined even when one original citation is not sufficient alone. No experimental claim is rejected merely because the cached abstract foregrounds a different protein. Bare protein-binding removals mean uninformative annotation, not false interaction.

Species and paralogs: human CASP3/CASP7 have distinct natural-substrate profiles (PMID:18723680). Mouse CASP7 can cleave ICAD efficiently and contributes to strain-dependent compensation for Casp3 loss (PMID:15525783). The 129X1/SvJ versus C57BL/6J comparison in PMID:12152782 must not be conflated with the 129S1/SvImJ comparison in PMID:15525783. These results do not establish universal redundancy or a single obligatory executioner across tissues.

CASP6: full PMID:32029622 establishes direct CASP3/CASP7 cleavage of procaspase-6 in vitro (Fig. 6A), inhibitor-sensitive procaspase-6 processing in primary hepatocytes (Fig. 6B), and a CASP6–BID mitochondrial feedback mechanism; Fig. 6H uses HepG2 cells. It does not justify a universal initiator-caspase activation route. Full PMID:32298652 and public primary Figure 6A identify mouse CASP6/RIPK3 constructs despite the HEK293T host; native infection experiments also use mouse cells/mice. Human prior NEW adaptor annotation is retired/UNDECIDED; conserved contextual human immune claims remain explicitly comparative. Mouse IAV findings do not imply a requirement for all inflammasome triggers.

CASP7: full PMID:35705808 establishes mouse SMPD1 processing and membrane-pore repair. CASP7 performs proteolytic maturation; SMPD1 performs ceramide-producing lipid hydrolysis. Repair delays lysis in the tested settings, so this mechanism is not universally pro-lytic. PMID:22464733 distinguishes PARP1 cleavage from PARP1 poly-ADP-ribosylation activity.

Evidence handling: checked existing primary caches and retained unresolved precise cellular/stimulus claims as UNDECIDED where evidence could not establish the claim. 0 pre-existing nonverbatim deep-research quotations were removed from the optional quotation field; source citations and review rationales remain, with direct primary evidence preferred for core functions. Provider reports remain immutable. Existing reports were used where present; missing Falcon reports were attempted with perplexity-lite fallback, and failures are recorded in .cache/module-audit-logs/apoptosis-caspase-*-research.log. No missing report was fabricated. Sources were fetched through normal helpers only.

Verified UniProt PANTHER placement: PTHR10454 CASPASE; CASP3/Casp3 SF198 CASPASE-3, CASP6/Casp6 SF206 CASPASE-6, CASP7/Casp7 SF31 CASPASE-7. These are membership checks, not assertions of identical physiological deployment.

The annotation-reviewer consultation confirmed that true same-target catalytic/location claims should not be removed for citation weakness, and that substrate cleavage is not the same as the substrate's enzymatic reaction. Notes are comparative; only target-specific claims are asserted in the review.

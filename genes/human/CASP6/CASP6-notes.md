# CASP6 notes

## 2026-09-30

- Re-audited the completed CASP6 review after refreshing GOA and UniProt. GOA
  still has the same 256 source rows and the YAML has no stale or missing rows.
  Tightened the two remaining broad `GO:0006915` apoptotic-process assertions
  to `GO:0097194 execution phase of apoptosis` while keeping separate
  intrinsic-apoptotic-signaling and ZBP1/RIPK3 PANoptosis entries for the
  RIPK1/BID feedback and viral innate-immunity contexts.
- Completed a manual CASP6 review from cached PubMed records, Reactome events,
  UniProt, GOA, the PTHR10454 PAINT context, and the existing
  `Liver apoptosis regulation by CASP6` GO-CAM after provider-backed deep
  research was unavailable.
- Accepted CASP6's core Asp-directed cysteine endopeptidase activity,
  proteolytic self-activation, broad apoptotic role, RIPK1 cleavage in intrinsic
  apoptosis, and BID/hepatocyte and lamina/SATB1/vimentin substrate contexts as
  valid protease biology.
- Added a conservative `NEW` `GO:0060090 molecular adaptor activity` assertion
  for the protease-independent RIPK3/ZBP1 scaffolding role in influenza
  A-induced PANoptosis, supported by PMID:32298652.
- Removed 201 of 202 generic `GO:0005515 protein binding` rows and modified the
  SATB1 row to the informative CASP6 cysteine endopeptidase activity. Most
  removed rows came from the PMID:32814053 systematic yeast two-hybrid
  neurodegeneration interactome or other high-throughput interactome maps.
- Treated several evidence gaps cautiously: the ATP11C/flippase cleavage row,
  the Caco-2 epithelial differentiation row, the HSP70/GATA1 cytosol row, and
  the Human Protein Atlas fibrillar-center localization row are `UNDECIDED`
  pending full-text, supplemental, or image-level confirmation.
- Accepted the valid Reactome cytosol and nucleoplasm localization rows as
  core CASP6 compartment evidence. The remaining mixed-action warnings are
  intentional source-specific exceptions: an abstract-only ATP11C row, an
  abstract-only HSP70/GATA1 cytosol row, a TP53 expression event that projects
  CASP6 as product rather than actor, and a CAFA row from a DFF40/CAD paper
  without CASP6-specific evidence.
- Marked the HIP14 palmitoylation row as `MARK_AS_OVER_ANNOTATED` for CASP6
  because CASP6 is the inhibited target in that experiment, removed the TP53
  expression Reactome cytosol projection, and removed the CAFA staurosporine
  row from the DFF40/CAD paper because the cached full text contains no
  CASP6-specific evidence.

## 2026-09-28

- Seeded the human CASP6 review with `just fetch-gene human CASP6`, creating
  `CASP6-uniprot.txt`, `CASP6-goa.tsv`, and a 256-row
  `CASP6-ai-review.yaml` stub.
- Attempted Falcon deep research with `just deep-research-falcon human CASP6`,
  but no deep-research provider API keys were configured
  (`OPENAI_API_KEY`, `EDISON_API_KEY`, `ASTA_API_KEY`, `PERPLEXITY_API_KEY`),
  so no `CASP6-deep-research-falcon.md` was generated.


## 2026-10-25 comparative apoptotic-execution review

Systematically examined all 257 rows, preserving every imported annotation payload. Decisions judge the biological claim, not the evidence code: independently established cysteine endopeptidase activity, cytosolic/nuclear localization and apoptotic execution are retained/refined even when one original citation is not sufficient alone. No experimental claim is rejected merely because the cached abstract foregrounds a different protein. Bare protein-binding removals mean uninformative annotation, not false interaction.

Species and paralogs: human CASP3/CASP7 have distinct natural-substrate profiles (PMID:18723680). Mouse CASP7 can cleave ICAD efficiently and contributes to strain-dependent compensation for Casp3 loss (PMID:15525783). The 129X1/SvJ versus C57BL/6J comparison in PMID:12152782 must not be conflated with the 129S1/SvImJ comparison in PMID:15525783. These results do not establish universal redundancy or a single obligatory executioner across tissues.

CASP6: full PMID:32029622 establishes direct CASP3/CASP7 cleavage of procaspase-6 in vitro (Fig. 6A), inhibitor-sensitive procaspase-6 processing in primary hepatocytes (Fig. 6B), and a CASP6–BID mitochondrial feedback mechanism; Fig. 6H uses HepG2 cells. It does not justify a universal initiator-caspase activation route. Full PMID:32298652 and public primary Figure 6A identify mouse CASP6/RIPK3 constructs despite the HEK293T host; native infection experiments also use mouse cells/mice. Human prior NEW adaptor annotation is retired/UNDECIDED; conserved contextual human immune claims remain explicitly comparative. Mouse IAV findings do not imply a requirement for all inflammasome triggers.

CASP7: full PMID:35705808 establishes mouse SMPD1 processing and membrane-pore repair. CASP7 performs proteolytic maturation; SMPD1 performs ceramide-producing lipid hydrolysis. Repair delays lysis in the tested settings, so this mechanism is not universally pro-lytic. PMID:22464733 distinguishes PARP1 cleavage from PARP1 poly-ADP-ribosylation activity.

Evidence handling: checked existing primary caches and retained unresolved precise cellular/stimulus claims as UNDECIDED where evidence could not establish the claim. 0 pre-existing nonverbatim deep-research quotations were removed from the optional quotation field; source citations and review rationales remain, with direct primary evidence preferred for core functions. Provider reports remain immutable. Existing reports were used where present; missing Falcon reports were attempted with perplexity-lite fallback, and failures are recorded in .cache/module-audit-logs/apoptosis-caspase-*-research.log. No missing report was fabricated. Sources were fetched through normal helpers only.

Verified UniProt PANTHER placement: PTHR10454 CASPASE; CASP3/Casp3 SF198 CASPASE-3, CASP6/Casp6 SF206 CASPASE-6, CASP7/Casp7 SF31 CASPASE-7. These are membership checks, not assertions of identical physiological deployment.

The annotation-reviewer consultation confirmed that true same-target catalytic/location claims should not be removed for citation weakness, and that substrate cleavage is not the same as the substrate's enzymatic reaction. Notes are comparative; only target-specific claims are asserted in the review.

PMID:8710882 normal fetch succeeded on retry (abstract only; PMC XML/HTML/PDF unavailable through helper). Explicit recombinant human CASP6-versus-CASP3 comparison supports lamin-A specificity. PMID:8663580 separately reports granzyme-B-mediated Mch2 processing. Neither supports a universal initiator-caspase activation route.

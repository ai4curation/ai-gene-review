# ANAPC2 notes

## Deep research status

Requested Falcon deep research was attempted with fallback:

`just deep-research-falcon human ANAPC2 --fallback perplexity-lite`

The Falcon provider timed out after the wrapper's 600 second timeout. The configured
`perplexity-lite` fallback then failed with a Perplexity API 401 quota error. No
`ANAPC2-deep-research-falcon.md` or fallback deep-research report was produced, so
this review uses the fetched UniProt record, cached publications, Reactome cache,
PANTHER family metadata, and project-local PN projection reports.

## PN projection evaluation

The PN projection report lists three ANAPC2 gene-GO projections:

- `GO:0005680 anaphase-promoting complex`: `already_in_goa_exact`, so no new
  annotation is needed [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv].
- `GO:0000151 ubiquitin ligase complex`: `entailed_by_goa_closure` from existing
  `GO:0005680 anaphase-promoting complex` and `GO:0031461 cullin-RING ubiquitin
  ligase complex`, so no new direct annotation is needed [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv].
- `GO:0160072 ubiquitin ligase complex scaffold activity`: `new_to_goa` from the
  PN code `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin|degenerate,
  APC sununit` [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv].

Conservative decision: ANAPC2 is not a canonical cullin like CUL1-CUL5, but the
cached literature supports a cullin-like APC/C scaffold role. UniProt describes
ANAPC2 as belonging to the cullin family and states that ANAPC2 with ANAPC11
constitutes the catalytic APC/C component [genes/human/ANAPC2/ANAPC2-uniprot.txt].
The structural papers describe the catalytic module as Apc2-Apc11 and the
cullin Apc2/RING Apc11 pair as the site where substrates are ubiquitinated
[PMID:16364912; PMID:26083744]. The biochemical reconstitution paper shows that
human APC2 with APC11 forms a minimal ligase module sufficient to ubiquitinate
securin and cyclin B1 with Ubc4 or UbcH10, while lacking substrate specificity
alone [PMID:11739784]. I therefore added `GO:0160072` as a proposed `NEW`
annotation rather than automatically changing existing GOA.

## Annotation review summary

Core ANAPC2 function is as the cullin-like scaffold subunit of the APC/C
E3 ubiquitin ligase catalytic module. It works with ANAPC11 and E2 enzymes to
ubiquitinate APC/C substrates, especially in mitotic cell-cycle transitions and
APC/C-dependent proteasomal degradation [PMID:16364912; PMID:18485873;
PMID:26083744; PMID:29033132].

Neuron-development annotations transferred from mammalian orthology were kept
as non-core only where they directly match the UniProt CDC20-APC/C
presynaptic-differentiation context. Broader or more specific axon, dendrite,
and synaptic-plasticity terms were marked as over-annotated because the local
support does not establish those exact process labels for human ANAPC2. Generic
`protein binding` annotations were not treated as core because they primarily
record individual physical interactions and are less informative than the APC/C
scaffold and ubiquitin ligase module interpretation.

## Falcon deep research findings (2026-06-07)

A Falcon (Edison Scientific) deep research report was generated successfully on
2026-06-07 (the earlier timeout noted above has now been superseded). Synthesis of
KEY findings, flagged as CONFIRMS / NEW / PROVISIONAL relative to the existing
review:

- CONFIRMS: ANAPC2/APC2 is the cullin-family catalytic scaffold subunit of the
  APC/C, pairing with the RING subunit ANAPC11 to form the Apc2-Apc11 cullin-RING
  catalytic core that recruits and activates ubiquitin-loaded E2 enzymes; APC/C is
  a RING E3 that does not form a covalent E3~Ub intermediate. This matches the
  existing core_functions and ACCEPT annotations [PMID:30449648 Watson 2019
  "Posing the APC/C E3 ubiquitin ligase"; PMID:11739784 minimal Apc2-Apc11 module].

- NEW (structural detail, mechanism): Time-resolved cryo-EM of active human APC/C
  during substrate polyubiquitination shows a two-E2 division of labor where the
  priming E2 UBE2C/UBCH10 is "clasped" by the APC11 RING and the APC2 WHB region,
  while the elongation E2 UBE2S C-terminal peptide (CTP) binds a groove formed by
  APC2-APC4; UBE2S CTP allosterically stabilizes a catalytically active "CRL up"
  state and increases UBE2C recruitment. APC2 thus directly contributes E2-docking
  surfaces (WHB; APC2-APC4 groove) and a mobile "CRL up/down" catalytic arm
  [PMID:37735619 Bodrug 2023 "Time-resolved cryo-EM (TR-EM) analysis of substrate
  polyubiquitination by the RING E3 APC/C", doi:10.1038/s41594-023-01105-5]. This
  enriches but does not contradict the existing K11-ubiquitination / scaffold
  annotations.

- NEW (structural feature): High-resolution (2.9-3.2 A) cryo-EM of apo-APC/C and
  APC/C^CDH1:EMI1 identified a previously unreported zinc-binding module in APC2
  that confers structural stability, with zinc ions experimentally confirmed; the
  same structures resolve EMI1 contacts and CDH1 N-terminal helix
  [PMID:39567505 Hofler 2024, Nat Commun, doi:10.1038/s41467-024-54398-5]. NEW
  domain-level detail for ANAPC2 not previously in the review.

- NEW (disease link / substrate axis): In KrasG12D-driven lung tumorigenesis,
  APC/C^CDH1 cooperates with UBE2C to ubiquitylate and degrade DEPTOR, activating
  mTORC signaling; knockdown of APC2 (or CDH1) increased DEPTOR protein,
  indicating APC2-containing APC/C is required for DEPTOR turnover. This adds a
  specific human substrate (DEPTOR) and an oncogenic-pathway context (mTOR)
  [PMID:36548081 Zhang 2023 "The UBE2C/CDH1/DEPTOR axis...", doi:10.1172/JCI162434].
  Treated as substrate/pathway context, not a new core MF.

- CONFIRMS/CONTEXT: APC/C is restrained by the spindle assembly checkpoint via the
  mitotic checkpoint complex (MCC: CDC20, BUBR1, MAD2, BUB3) and by the EMI1
  pseudo-substrate inhibitor, which contacts CDH1, APC10, APC11 RING, the APC2 WHB,
  and the APC2-APC4 groove; phosphoregulation (CDK1, PLK1) controls coactivator
  exchange. Consistent with existing Reactome-derived KEEP_AS_NON_CORE
  localization/regulation annotations and PMID:23708001 (Emi1).

- PROVISIONAL / low-confidence (NOT used to change annotations): OpenTargets lists
  ANAPC2 disease associations (colorectal carcinoma, neurodegenerative disease,
  aplastic anemia, skeletal phenotypes) with limited evidence depth; hypothesis-
  generating only. Also note the report cites a bioRxiv preprint version of the
  Hofler work (hofler2024newstructuralfeatures, doi:10.1101/2023.08.31.555674) —
  the peer-reviewed Nat Commun version (PMID:39567505) is used instead.

Curation decision: incorporated the three peer-reviewed primary papers
(PMID:37735619, PMID:39567505, PMID:36548081) as statement-only references and
added one suggested question and one suggested experiment around the newly
described APC2 E2-docking surfaces and zinc-binding module. No existing annotation
`action` was changed, since all new findings enrich rather than contradict the
existing cullin-like scaffold / catalytic-module interpretation.

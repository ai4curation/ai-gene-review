# Msed_0406 (A4YDT1, HBCL1_METS5) curation notes

## 2026-11-02 session

### Sources and limits

- Deep research: no provider was available in this environment. `scripts/deep_research_wrapper.py`
  reported "Provider 'perplexity' not available. Available: openscientist, claude_code" and
  "Provider 'asta' not available". No `-deep-research-<provider>.md` file was written; the review
  rests on the UniProt record, the two Kelly-lab papers and PANTHER/PAINT data.
- PMID:23258541 (Hawkins et al. 2013, JBC) is cached abstract-only (PMC3567653 is not in the PMC
  open-access subset; an eutils PMC fetch returned only front matter). The kinetics below are taken
  from the curated UniProt record, whose statements cite PubMed:23258541 with ECO:0000269 and were
  therefore read from the full text by UniProt curators.
- PMID:24532060 (Hawkins et al. 2014, AEM) fetched this session; abstract-only.
- Structure paper for PDB 8BIQ/8BIT: "Adapting an acyl CoA ligase from Metallosphaera sedula for
  lactam formation by structure-guided protein engineering", Front. Catal. 2024,
  doi:10.3389/fctls.2024.1360129 (from the PDBe publications API). No PMID found; not cited in
  the review.

### What the protein is

- UniProt RecName "4-hydroxybutyrate--CoA ligase 1", EC 6.2.1.40, with acetate, butyrate and
  propionate CoA-ligase AltNames, all with ECO:0000269 PubMed:23258541.
- AMP-forming ligase (Pfam PF00501 AMP-binding, PF13193 AMP-binding_C; CDD cd05972 MACS_like;
  PANTHER PTHR43605:SF10). Same subfamily as P. putida PP_2213 and B. subtilis YtcI.
- UniProt FUNCTION: [file:METS5/Msed_0406/Msed_0406-uniprot.txt "Involved in the
  3-hydroxypropionate/4-hydroxybutyrate cycle which incorporates carbon dioxide into cellular
  carbon. Catalyzes the ligation of coenzyme A (CoA) to 4-hydroxybutyrate (4HB)."]

### Physiological substrate

- [PMID:23258541 "transcriptomic analysis of cells grown under strict H(2)-CO(2) autotrophy was
  consistent with the involvement of Msed_0406 and Msed_0394"]
- [PMID:23258541 "Recombinant versions of these enzymes catalyzed the ligation of CoA to 4HB"]
  Msed_0406 is ~8-fold faster than Msed_0394 (1.69 vs 0.22 umol/min/mg).
- [PMID:24532060 "the final four enzymes of the 3HP/4HB cycle, 4-hydroxybutyrate-CoA ligase (AMP
  forming) (Msed_0406), 4-hydroxybutyryl-CoA dehydratase (Msed_1321), ... were produced
  recombinantly in Escherichia coli, combined in vitro, and shown to convert 4HB to acetyl-CoA"]
- [PMID:24532060 "flux between the succinate and acetyl-CoA branches in the 3HP/4HB pathway is
  governed by 4-hydroxybutyrate-CoA ligase"]
- Kinetics from UniProt (kcat / Km, computed here, s-1 mM-1): propionate 16.2/0.38 = 43;
  butyrate 8.4/0.32 = 26; valerate 5.6/0.74 = 7.6; acetate 6.4/2.03 = 3.2; 3HB 2.6/0.81 = 3.2;
  4HB 1.8/2.0 = 0.9. In vitro the enzyme is a broad short-chain (C2-C5) acyl-CoA synthetase, and
  4HB is its poorest measured substrate.
- Verdict: the physiological substrate is 4HB. The argument is pathway context, not kinetics:
  4HB is a cycle intermediate that must be activated; Msed_0406 is induced under autotrophy; the
  reconstituted four-enzyme segment runs from 4HB; and no other cycle step needs free acetate,
  propionate or butyrate activation (propionyl-CoA is made from acryloyl-CoA, acetyl-CoA by the
  thiolase). M. sedula has a conserved acetate/propionate synthetase, Msed_1353
  [PMID:23258541 "the acetate/propionate synthetase (Msed_1353), an enzyme that is highly
  conserved among the Sulfolobales"], which can be named as the cell's enzyme for those two
  reactions.

### Annotation decisions (summary)

- GO:0004321 fatty-acyl-CoA synthase (TreeGrafter IEA): REMOVE; synthase/synthetase confusion from
  PAINT IBD on PTN001944787 (only seed RGD Acsm4, PMID:12709059 reporting ligase activity). Source
  defect against GO_CENTRAL, as in PP_2213.
- GO:0006633 fatty acid biosynthetic process (IEA): REMOVE. Msed_0406 activates 4HB in a pathway
  that cleaves the C4 unit to two acetyl-CoA; it forms no fatty acid. The IBD's mammalian seeds
  (Acsm1, Acsm3, PMID:11470804) point to oxidation: [PMID:11470804 "acyl-CoAs produced by MACS1
  and Sa protein are utilized mainly for oxidation."]. Differs from PP_2213 (MARK_AS_OVER_ANNOTATED)
  because here the process the enzyme does take part in is known and is not fatty acid synthesis.
- GO:0006637 acyl-CoA metabolic process: ACCEPT (forms 4-hydroxybutyryl-CoA).
- GO:0015645 fatty acid ligase: MODIFY -> GO:0031955 short-chain fatty acid-CoA ligase activity.
- GO:0031956 medium-chain (C6-C12) fatty acid-CoA ligase (IDA + IEA): MODIFY -> GO:0031955. All
  measured substrates are C2-C5. Caveat: full text not read; if the paper also assayed C6+ acids
  the medium-chain term would be a genuine side activity.
- GO:0003987 acetyl-CoA synthetase and GO:0050218 propionate-CoA ligase (IDA + IEA):
  MARK_AS_OVER_ANNOTATED. Real, kinetically respectable in vitro activities; no evidence they are
  used in vivo; Msed_1353 is the conserved acetate/propionate enzyme. Not REMOVE: the activity is
  not noise (higher than with 4HB), and the IDA rows rest on a full text not read here.
- GO:0016020 membrane (SubCell IEA from a predicted TM helix 105-125): REMOVE. The segment is a
  helix inside the N-terminal ANL domain in the crystal structure (FT HELIX 107..119 from 8BIQ) of
  the full-length (2-564) protein; ANL superfamily ACSM enzymes are soluble. Source defect against
  UniProt (PROBABLE).
- NEW GO:0015977 carbon fixation (IDA, PMID:24532060). Participation test: Msed_0406 itself
  catalyses a cycle step (4HB + CoA + ATP -> 4HB-CoA). Comparator check: other M. sedula cycle
  enzymes carry carbon-fixation terms in QuickGO (2026-11-02): Msed_1456 GO:0043427 IDA
  PMID:18165310; Msed_1353 GO:0043427 IEA. GO:0043427 "carbon fixation by 3-hydroxypropionate
  cycle" is defined as the Chloroflexus cycle ending in glyoxylate, and the 4HB branch is not part
  of it, so the parent GO:0015977 is used and a 3HP/4HB-cycle term is proposed.
- No GO term exists for 4-hydroxybutyrate-CoA ligase (EC 6.2.1.40; RHEA:23128): QuickGO search
  "4-hydroxybutyrate" and "hydroxybutyrate-CoA ligase" returned no such term. Proposed as a new
  term; used as proposed_molecular_function in core_functions.

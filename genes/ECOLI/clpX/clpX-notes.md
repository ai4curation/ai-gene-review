# clpX (E. coli K-12, P0A6H1) review notes

Deep research was unavailable for this review (no deep-research API keys in the
container), so no `-deep-research-<provider>.md` file exists. These notes were
compiled directly from the cached publications in `publications/`, the UniProt
record, and PubMed searches. The GONUTS wiki (gowiki.tamu.edu) was tried for the
CACAO papers (PMID:21317324, PMID:11278349) on 2026-10-29 but returned only a
"temporarily offline" maintenance page, so no student evidence text could be read.

## Identity and activity

- ClpX is the AAA+ unfoldase / specificity subunit of the ClpXP protease. It was first
  purified as a lambda O-degrading activity together with ClpP
  [PMID:8226769 "These results suggest that ClpX protein directs ClpP protease to specific substrates."].
- Hexameric ring, stabilised by ATP; ClpP double heptamer docked by one or two ClpX rings
  [PMID:9575205 "ClpX subunits (Mr 46, 000) associate to form a six-membered ring (Mr approximately 280, 000) that is stabilized by binding of ATP or nonhydrolyzable analogs of ATP."].
- ClpX binding increases ClpP peptidase activity (activator role)
  [PMID:9575205 "ClpX and ClpA interactions with ClpP result in structurally analogous complexes and induce similar conformational changes that affect the accessibility and the catalytic efficiency of ClpP active sites."].
- N-terminal C4 zinc-binding domain; Zn(II) required for oligomerisation, ClpP binding
  and proteolysis [PMID:11278349 "ClpX, free of Zn(II), cannot oligomerize, bind to ClpP, or participate in ClpXP-dependent proteolysis."].
- Mechanical unfolding: ATP consumption scales with substrate stability
  [PMID:12941278 "endows ClpX with a robust unfolding activity required for its biological roles in degradation and complex disassembly."];
  optical-trap observation of unfolding by ClpX alone and ClpXP
  [PMID:21529717 "We report direct observations of mechanical, force-induced protein unfolding by the ClpX unfoldase from E. coli, alone, and in complex with the ClpP peptidase."].
- Asymmetric hexamer structures, nucleotide-loadable/unloadable subunits
  [PMID:19914167; PMID:23622246; PMID:25866879].

## Substrates and adaptors

- SsrA-tagged proteins degraded by ClpXP and ClpAP in vitro with purified components
  [PMID:9573050 "required a substrate with a wild-type SsrA tail, the presence of both ClpP and either ClpA or ClpX, and ATP."].
- SspB adaptor docks via its disordered C-terminal peptide
  [PMID:14536075 "A synthetic peptide containing the 10 C-terminal residues of SspB binds ClpX, stimulates its ATPase activity"].
- RseA(1-108) degradation releases sigma-E (extracytoplasmic stress)
  [PMID:15371343 "ClpXP functions in concert with SspB to efficiently recognize and degrade RseA(1-108), and thereby releases sigma(E)."].
- FtsZ is a substrate; ClpX N-domain recognises polymers [PMID:19541655];
  genetic interplay with division mutants [PMID:21317324 "Our results demonstrate that ClpXP modulates division in cells lacking MinC by a mechanism that requires ATP-dependent degradation."].
- UvrA degraded by ClpXP after UV recovery [PMID:19183285].

## CACAO rows (assigned_by CACAO)

1. GO:0016887 ATP hydrolysis activity, IDA, PMID:11278349 — abstract states ClpX is an ATPase
   and dissects the single ATP site; ATPase assays presumably in full text (not cached). Term
   correct; ACCEPT.
2. GO:0004176 ATP-dependent peptidase activity, IDA, PMID:9573050 — in vitro reconstitution of
   SsrA-tagged substrate degradation by purified ClpX + ClpP + ATP. Activity of the ClpXP
   holoenzyme (ClpP holds the active sites); matches the paper; ACCEPT (complex-level activity).
3. GO:0043335 protein unfolding, IDA, PMID:21529717 — optical-trap single-molecule unfolding;
   exact match; ACCEPT.
4. GO:0051301 cell division, IGI with ftsZ, PMID:21317324 — clpX deletion suppresses ftsZ84
   filamentation and exacerbates delta-minC filamentation; the paper's own conclusion is that ClpXP
   *modulates* division by degrading FtsZ. Phenotype read as process: ClpX does not perform
   division, it tunes FtsZ levels. MODIFY to GO:0051302 regulation of cell division.
5. GO:0004176 ATP-dependent peptidase activity, IDA, PMID:8226769 — purification of the
   ATP-dependent lambda O-degrading ClpXP protease; matches; ACCEPT.

## Other notable issues

- GO:0009376 HslUV protease complex (CAFA IDA, PMID:14536075; IBA PTN000137358 seeded only by
  P0A6H1 itself). ClpX is not a subunit of HslUV (HslU/HslV); the paper is about SspB-ClpXP
  delivery complexes. The correct complex is GO:0009368 endopeptidase Clp complex. Wrong-complex
  term — recorded as a source defect, MODIFY.

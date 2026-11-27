# NBDY (NoBody; A0A0U1RRE5) review notes

## 2026-09-30 session

### Gene product
- 68-aa intrinsically disordered microprotein encoded by a smORF in the lncRNA-annotated
  locus LINC01420 (Xq). UniProt: "Was previously thought to be non-coding but has been
  shown to be translated and functional." Whole chain predicted disordered (MobiDB-lite);
  C-terminal proline-rich region.
- Conserved in mammals only; no homology to known domains
  [PMID:27918561 "NoBody exhibits sequence conservation with computationally predicted small mammalian proteins of similar length, but not with any larger proteins or domains of known function"].

### Discovery paper: D'Lima et al. 2017 (PMID:27918561, full text cached)
- Affinity purification-MS: "only twelve proteins were specifically enriched >2-fold by
  NoBody, all of which are components of mRNA decapping and 5'-to-3' mRNA decay complexes".
- Direct binding to EDC4: GST pull-down plus benzophenone photo-crosslinking
  [PMID:27918561 "Combined, these in-cell and in vitro experiments are consistent with a direct interaction between NoBody and EDC4"].
  Residues 22-41 necessary and sufficient; alanine scan: L30 and W34 required.
- EDC4 knockdown abolishes co-purification of other decapping factors
  [PMID:27918561 "These data indicate Nobody interacts with the decapping complex via direct interactions with EDC4"].
- P-bodies: overexpression disperses P-bodies (not degradation of components), requires the
  peptide not the RNA; siRNA knockdown increases P-bodies 1.5-2x
  [PMID:27918561 "We observed a 1.5- to 2-fold increase in P-bodies per cell when NoBody was silenced"].
- Localization: at low expression co-localizes with EDC4 in P-bodies
  [PMID:27918561 "This suggests that NoBody localizes to P-bodies at low expression levels."].
- NMD substrate (Calu-6 p53 mRNA): knockdown DECREASED, overexpression INCREASED steady-state
  p53 mRNA. Authors explicitly say decay rate not measured
  [PMID:27918561 "though the effect of NoBody on the decay rate of this mRNA has not been established"]
  and interpret as negative regulation of decay
  [PMID:27918561 "is most consistent with negative regulation of mRNA decay in cells by NoBody"].
  => The GOA IDA "nuclear-transcribed mRNA catabolic process" (GO:0000956) is based on this
  steady-state measurement. NBDY does not catalyse any step of mRNA breakdown; the direction of
  the effect (if anything) is inhibitory. Not participation.

### Na et al. 2020 Biochemistry (PMID:33059440, full text cached)
- Endogenous NBDY binds EDC4 WD40 domain directly; DCP1A EVH1 binds NBDY C-terminal polyproline.
- NBDY KO HEK293T: 3x more P-bodies, rescued by re-expression; decreased viability.
- TimeLapse-seq: >1400 half-lives changed (1200 stabilized, 226 destabilized)
  [PMID:33059440 "NBDY KO dysregulates >1400 RNA half-lives, with 1200 cellular RNAs post-transcriptionally stabilized and 226 destabilized relative to WT"].
- DCP2 substrates stabilized OR destabilized depending on 5' UTR length; requires EDC4
  interaction (W34A).
- NBDY does not change in vitro decapping activity of immunopurified complex
  [PMID:33059440 "We concluded that NBDY does not affect the in vitro enzymatic activity of the decapping complex"].
- Non-DCP2 targets stabilized indirectly through reduced synthesis of NMD factor transcripts.
- => Best process term for this: GO:0043488 regulation of mRNA stability ("Includes processes
  that both stabilize and destabilize mRNAs"). Used as MODIFY replacement for GO:0000956.

### Na et al. 2021 JACS (PMID:34346674, full text)
- NBDY + RNA undergo LLPS in vitro (complex coacervation with polyU; needs PEG crowder;
  critical concentration 150 uM - far above cellular).
- Phosphorylation: T40 at G2/M (CDK-dependent), S61 after EGF (PKC; PKCalpha phosphorylates in
  vitro). Non-phosphorylatable mutants abrogate mitotic / EGF-induced P-body loss.
  [PMID:34346674 "Expression of the nonphosphorylatable NBDY S61A mutant in the NBDY KO background abrogated EGF-dependent P-body disappearance"].
- Strengthens GO:0010607 negative regulation of cytoplasmic mRNA processing body assembly.
- In vitro RNA LLPS not proposed as NEW (reductionist, high concentration; RNA binding not
  shown to be sequence-specific or relevant in cells).

### Bloch et al. 2023 PLoS One (PMID:36877681) - EDC4 two-hybrid; NBDY-EDC4 interaction in cells
requires EDC4 N-terminal WD40 region. Supports EDC4 binding.

### Cheng et al. 2025 RNA (PMID:40360209)
- NBDY 22-41 binds EDC4 C-terminal domain directly and competes EDC4-EDC4 self-association;
  disrupts P-bodies without affecting tethered mRNA decay
  [PMID:40360209 "NBDY 22–41 did not affect mRNA degradation under SMG7-induced conditions"].
  Further argues against NBDY participating in mRNA catabolism per se.

### Liu & Wang 2023 JACS Au (PMID:37772172): MD simulation of ATP effect on NBDY clusters. Low
relevance, computational only.

### LINC01420 cancer papers: treat the locus as lncRNA; not about the NBDY protein. Not used.

### Decisions
- P-body IDA/IEA: ACCEPT.
- GO:0010607 IDA: ACCEPT (core).
- GO:0000956 IDA: MODIFY -> GO:0043488 regulation of mRNA stability.
- protein binding IPI (EDC4, DCP1A): REMOVE per repo protein-binding policy (interactions are real
  and direct, but the term is uninformative; no specific MF term available for a non-enzymatic
  EDC4-binding regulator). Removal does not dispute the interactions.
- No NEW annotations. Considered RNA decapping complex (GO:0098745) membership - left as question.
- Core MF: no suitable GO MF; leave molecular_function unset.

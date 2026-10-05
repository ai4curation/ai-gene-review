# mcs6 (crk1 / mop1; SPBC19F8.07; UniProt Q12126) — curation notes

Working journal for the AI gene review of *S. pombe* Mcs6, the CDK7 ortholog.
Inputs: `mcs6-uniprot.txt`, `mcs6-goa.tsv`, `mcs6-deep-research-falcon.md` (Edison/Falcon, 38 citations),
and cached publications. Full text is cached only for PMID:15829570, PMID:19328067 and PMID:22508988;
all other cited papers are abstract-only, which shaped several "accept and defer to the curator" calls below.

## Identity

- `crk1` was cloned as a second fission-yeast CDK and shown to be allelic to the `mcs6` mitotic-catastrophe
  suppressor locus [PMID:8557037 "We demonstrate that crk1 is allelic to the mcs6 mitotic catastrophe suppressor"].
  Independently cloned as `mop1` (MO15-related) [PMID:8557036 "We have isolated an essential S.pombe gene, mop1, whose product is closely related to MO15 and to Saccharomyces cerevisiae Kin28"].
- 335 aa, CMGC/CDK family, CDK7 subfamily (InterPro IPR037770). Essential: deletion spores arrest with septa
  and condensed chromatin [PMID:8557037 "crk1 is essential for viability and delta crk1 cells arrest with septa and condensed chromatin"].

## Complex

- Binds the cyclin H-like Mcs2 [PMID:8557037 "Crk1 associates with the Mcs2 mitotic catastrophe suppressor, a cyclin H-like molecule"];
  Mop1/Mcs2 also pair with the heterologous human cyclin H / MO15 [PMID:8557036 "Mop1 and Mcs2 can associate with the heterologous partners human cyclin H and MO15, respectively"].
- Third subunit Pmh1 (MAT1/Tfb3-like RING protein; PMID:15555586, not cached). The trimer was reconstituted in
  insect cells and Pmh1 links it to core TFIIH [PMID:15829570 "We next reconstituted the Mcs6–Mcs2–Pmh1 complex in baculovirus-infected insect cells";
  "Pmh1 was shown to bind Mcs6, Mcs2, and components of core TFIIH when expressed in S. pombe"]. Two Pmh1 pools:
  ~200 kDa free trimer and ~700 kDa TFIIH-sized complex.
- UniProt: "One of the nine subunits forming the core-TFIIH basal transcription factor. Interacts with mcs2 and tfb3."

## Activities

1. **CAK (Cdc2 Thr167 kinase).** Crk1-Mcs2 phosphorylates human Cdk2 Thr160 and activates it
   [PMID:8557037 "The Crk1-Mcs2 complex possesses CAK activity in vitro in that it phosphorylates human Cdk2 on Thr160"]; IP Mop1-Mcs2 is both a CTD kinase and a CAK
   [PMID:8557036 "immunoprecipitated Mop1-Mcs2 acts both as an RNA polymerase II CTD kinase and as a CAK"].
   In vivo, Cdc2 activation fails only when both Mcs6 and Csk1 are lost
   [PMID:10226032 "Thus, fission yeast contains two partially redundant CAKs: the Mcs6-Mcs2 complex and Csk1";
   "Cdc2 was not activated and the cells underwent a cell division arrest prior to mitosis"]. Single mcs6/pmh1
   conditional mutants keep Cdc2 T-loop phosphorylation
   [PMID:15829570 "pmh1-26 cells were proficient at phosphorylating the CDK T-loop, possibly due to compensation by Csk1"].
2. **Pol II CTD Ser5 (and Ser7) kinase.** In vitro Mcs6 makes H14 (Ser5-P)-reactive CTD; analog-sensitive
   inhibition lowers Ser5-P in vivo [PMID:19328067 "Inhibition of Mcs6 caused dose- and time-dependent decreases in Ser5 phosphorylation in vivo"].
   Mcs6 also phosphorylates Ser7 and is required for Ser7-P in vivo
   [PMID:22508988 "Mcs6 phosphorylated Ser7 in vitro and was required for Ser7-P in vivo"; "Immunoblot analysis indicated that Mcs6 phosphorylates Ser2, Ser5, and Ser7, as did human Cdk7"].
3. **Priming for Cdk9 / capping.** Mcs6 activity is needed to recruit Cdk9/Pcm1 and pre-phosphorylation by Mcs6
   stimulates Cdk9 ~8–10-fold [PMID:19328067 "Mcs6 activity is sufficient-and necessary-to recruit the Cdk9/Pcm1 (mRNA cap methyltransferase) complex";
   "Prior phosphorylation by Mcs6 stimulated Cdk9 activity ~8–10-fold"]. PIC assembly and Pol II promoter occupancy
   are unaffected by Mcs6 inhibition; the defect is post-PIC [PMID:19328067 "PIC assembly occurred normally at the eng1+ promoter even when Mcs6as was inhibited"].

## Upstream regulation

- Csk1 phosphorylates Mcs6 Ser165 (T-loop) and is a "CAK-activating kinase"
  [PMID:9857180 "we identify the fission yeast Csk1 kinase as an in vivo activating kinase of the Mcs6-Mcs2 CAK defining Csk1 as a CAK-activating kinase (CAKAK)"];
  Csk1 activates both monomeric and Mcs2-bound Mcs6 [PMID:10226032 "Csk1 activated both the monomeric and the Mcs2-bound forms of Mcs6"].
  Pmh1 bypasses the need for T-loop phosphorylation [PMID:15829570 "even the unphosphorylatable T160A/S165A mutant could be recovered in active form upon coexpression of Pmh1"];
  mcs6-S165A cells grow normally [PMID:22508988 "growth of mcs6 S165A cells, in which the Mcs6 activation loop is mutated to prevent phosphorylation by a CAK, was not impaired"].
- UniProt phosphosites: Ser162, Ser165, Ser318 (PMID:18257517, phosphoproteome).

## Transcriptional output

- Only modest global effect; ~5% of transcripts fall >2-fold, enriched for Sep1/Ace2 cell-separation genes
  [PMID:15829570 "a one-third reduction in a severe mcs6 mutant after prolonged incubation at 36°C";
  "transcripts dependent on the forkhead transcription factor Sep1, which are expressed coordinately during mitosis, were repressed in Mcs6 complex mutants"].
- Deep research (Falcon) adds from uncached full texts: Saiz & Fisher 2002 (mcs6-ts1 loses CTD kinase but keeps Cdc2 T-loop-P;
  double CAK loss arrests with 1C DNA), Hermand 2001 (linear Csk1→Mcs6→Cdc2 model vs branched network),
  Yague-Sanz 2023 (Mcs6 inhibition does not change H3 occupancy at Pol III loci).

## Localization

- YFP screen: nucleus and cytoplasm (PMID:16823372; PomBase HDA rows nucleus / cytoplasm / cytosol). ChIP recovers
  Mcs6 at eng1+ [PMID:19328067 "Mcs6 activity was not required for its own recruitment (Figure S3)"].
  GO-CAMs `66187e4700001573` (RNA capping) and `6796b94c00000168` (elongation) place Mcs6 S5-kinase activity in chromatin / nucleus.

## Curation decisions (summary)

- All GO:0004693 / GO:0008353 / GO:0140836 / GO:0070985 / GO:0005675 / GO:0006367 / GO:0032968 / GO:0060261 /
  GO:0001111 rows: ACCEPT. Mcs6 is a genuine cyclin-dependent kinase, so the CAK1-review logic (Cak1 is monomeric →
  MODIFY CDK terms to plain Ser/Thr kinase) does NOT transfer here.
- GO:0005515 protein binding (IPI with Mcs2): MODIFY → GO:0030332 cyclin binding (Mcs2 is the cyclin H ortholog).
- GO:0097472 (IDA PMID:9857180): MODIFY → GO:0004693 (Ser/Thr-specific child, consistent with the other five rows).
- GO:0004674 rows: MODIFY → GO:0004693 (PMID:10226032; assayed enzyme is the Mcs6-Mcs2 complex) and →
  GO:0140837 S7 kinase + GO:0140836 S5 kinase (PMID:22508988, the primary Ser7-kinase paper). Position-specific
  CTD kinase terms verified in QuickGO (GO:0140834 S2, GO:0140836 S5, GO:0140837 S7).
- Cytoplasm (HDA, IBA, IEA) and cytosol (HDA): KEEP_AS_NON_CORE; nucleus/chromatin are the functional sites.
- Abstract-only papers whose abstracts do not name Mcs6 (PMID:15182371 TFIIH in vitro system; PMID:20605454 Lsk1/S2P;
  PMID:23122962 Cdk11): ACCEPT and defer to the PomBase curator; the functions are clearly right for the gene and the
  same activities are shown in full-text-cached papers.
- GO:0060261 (IMP, positive regulation of initiation): ACCEPT, noting the full text shows PIC assembly is normal and the
  defect is post-PIC (promoter clearance / early elongation, covered by GO:0001111 and GO:0032968).
- No NEW annotations. Comparator check for the CAK process terms (QuickGO, 2026-09-27): no S. pombe gene carries
  GO:0045737 (positive regulation of CDK activity), so it was not used even in core_functions; csk1 carries GO:0000086
  G2/M transition by EXP from PMID:10226032 (same double-mutant paper) and Cak1 carries it in SGD, but mcs6 does not.
  GO:0000086 is kept in core_functions (module `g2_m_transition.yaml` models Mcs6 as the fission-yeast CAK variant)
  and the discrepancy is raised as a suggested question rather than a NEW row. This leaves one validator warning.
- Reference `file:SCHPO/mcs6/mcs6-deep-research-falcon.md` is cited once (heterologous CAK complementation of Mcs6+Mcs2).

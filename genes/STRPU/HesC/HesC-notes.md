# HesC (Sp-HesC; UniProt A0A7M7RIK0; LOC592057) - curation notes

## Identity of the UniProt entry

- A0A7M7RIK0 is an unreviewed TrEMBL genome-project entry (RefSeq XP_796692.2 / XM_791599.5,
  GeneID 592057, EnsemblMetazoa LOC592057; NCBI Gene description "transcription factor HES-4").
  There are no `RX PubMed=` lines in the record, so the link to the literature gene `hesC`
  had to be established from sequence.
- Revilla-i-Domingo, Oliveri & Davidson 2007 blocked hesC translation with a morpholino
  "complementary to the sequence of the first 25 bp of the coding region of hesC" whose
  sequence is 5'-GTTGGTATCCAGATGAAGTAAGCAT-3' [PMID:17636127]. The reverse complement,
  ATGCTTACTTCATCTGGATACCAAC, encodes MLTSSGYQ, which is exactly the N-terminus of
  A0A7M7RIK0 (MLTSSGYQQMDMCSNRPRTAKHL...). The same 25-mer is present verbatim in the
  RefSeq CDS XM_791599.5 (the xref of this accession) and in the EST clone CX199264 that
  the paper used as its in situ probe ("A DIG-labeled HesC probe was transcribed from the
  HesC cDNA clone yde51c06 ( CX199264 ; from a S. purpuratus EST library)" [PMID:17636127]).
  Checked 2026-09-26 with NCBI efetch.
- The protein has the expected Hairy/E(spl) architecture: bHLH (aa 16-73), Orange domain
  (aa 88-121) and a C-terminal WRPW tetrapeptide (aa 269-272), matching the paper's
  description that HesC "contains the two characteristic domains of the family: the
  C-terminus WRPW motif (used to recruit TLE/Grg/Groucho and mediate transcriptional
  repression)" [PMID:17636127].
- Conclusion: A0A7M7RIK0 is the hesC gene product of the endomesoderm GRN literature.
  Confidence: high (identical N-terminal coding sequence, identical EST, single
  HES-family gene at this locus).

## What the gene is

Sp-HesC is a bHLH-Orange (Hairy/Enhancer-of-split, HES family) transcriptional repressor.
It is the "Repressor of micromeres" (R of mic) whose existence was predicted from the logic
of the micromere/skeletogenic GRN before the gene was identified [PMID:17636127 "The
double-negative specification gate was logically required from the results of numerous
prior experiments, but the identity of the gene encoding the second repressor remained
elusive. Here we show that hesC is this gene, and we demonstrate experimentally all of its
predicted functions, including global repression of micromere-specific regulatory genes."].

## Place in the GRN

### Inputs (regulation of hesC itself)
- Pmar1 represses hesC in the micromere lineage. hesC was found in a screen of 46
  candidate regulatory genes for down-regulation on global pmar1 mRNA overexpression
  [PMID:17636127 "Five of the 46 regulatory genes tested were found to be significantly
  down-regulated at both time points in the two experiments performed. These genes were
  six3 , smadIP , awh , hesC , and foxJ1"]. The interaction is inferred to be direct on
  kinetic grounds (zygotic hesC starts ~2 h after pmar1; delta ~2 h after hesC).
- Blimp1 later represses hesC in the non-skeletogenic mesoderm (NSM) and keeps it off in
  the ingressed skeletogenic mesoderm, through a Blimp1 site in the first intron
  [PMID:19104065 "Mutation of this site in a hesC reporter construct caused expression to
  remain strong in the NSM territory"; "Blimp1 represses hesC and HesC represses delta ."].
- Delta-Notch signaling activates hesC through a Su(H) site at +2 of the transcription
  start, accounting for the very high hesC reporter activity in Veg2 endoderm
  [PMID:19104065 "In fact, a consensus Su(H) target site exists at +2 from the start of
  transcription in the hesC gene"; "the hesC cis -regulatory system responds negatively to
  Blimp1 repression and positively to Delta-Notch signaling"].

### Expression
- Low maternal level, then steep zygotic rise 8-12 h post-fertilization [PMID:17636127
  "hesC is maternally expressed, but only at low levels. The level of hesC transcript then
  increases steeply between 8 and 12 h after fertilization, indicating zygotic
  transcription."].
- At 8 h it is essentially ubiquitous; by 12 h it has cleared from exactly the 12 cells of
  the skeletogenic micromere lineage, which are the cells that express delta; double WMISH
  shows hesC and delta domains are mutually exclusive [PMID:17636127 "Therefore, zygotic
  expression of hesC had occurred everywhere in the embryo except the micromere lineage"].
- Later hesC turns off in the NSM and apical plate before delta comes on in each
  territory, and is very high in Veg2 endoderm at mesenchyme blastula [PMID:19104065].

### Outputs (targets of HesC repression)
- Global repression of the micromere-specific regulatory genes delta, alx1, ets1 and tbr.
  hesC MASO raised delta and alx1 transcripts 4-7 fold by 12 h and ets1/tbr by 24 h, with
  pmar1 unaffected; delta became ubiquitous; all cells ingressed as mesenchyme, phenocopying
  pmar1 overexpression [PMID:17636127 "the amount of transcript of delta and alx1 had
  increased 4- to 7-fold above normal in the two experiments performed"; "Thus, HesC
  functions to repress micromere lineage specification in all cells other than the
  micromere lineage"; "As logically required, blockade of hesC mRNA translation and global
  overexpression of pmar1 mRNA have the same effect, which is to cause all of the cells of
  the embryo to express micromere-specific genes."].
- delta: direct repression through a class C E-box (CACGCG) palindrome at +359 in the
  proximal delta CRM (-90 to +484); mutating it gives ubiquitous reporter expression
  [PMID:19104065 "These results indicate that the expression of delta in the NSM results
  from activation by Runx and repression by HesC through sites in the proximal CRM."].
  Earlier cis-regulatory separation of activator and repressor regions in the delta R11
  module already excluded an indirect mechanism [PMID:17636127 "These results exclude the
  possibility that there is an indirect effect such that HesC represses another gene that
  is in turn responsible for delta activation"].
- alx1: two functional HesC sites (proximal and distal) defined by BAC recombineering;
  mutating either gives striking ectopic expression [PMID:21723273 "In the complete
  context of the alx1 GFP BAC, when either the proximal or distal HesC binding site is
  mutated, striking ectopic expression results"; "Thus we have experimentally identified,
  and by mutation functionally characterized the genomic target sites responsible for
  direct spatial repression by the hesc gene product, and for activation by Ets1."].
- tbr: early skeletogenic expression is controlled by an intron enhancer plus a proximal
  region containing a HesC site [PMID:19679118 "In the context of the complete genomic
  locus, early skeletogenic expression is controlled by an intron enhancer plus a proximal
  region containing a HesC site as predicted from network analysis."].
- Summary in the 2008 global-logic paper: [PMID:18413610 "The primary regulatory genes of
  the skeletogenic micromere specification GRN are subject to direct HesC repression."].

### Mechanism
- HES-family repressor: bHLH DNA binding, Orange domain, C-terminal WRPW that recruits
  Groucho/TLE [PMID:19104065 "encoding group E bHLH and Orange domains and a C-terminal
  WRPW motif thought to recruit the Groucho/TLE corepressor"]. [PMID:17636127 "Because
  HesC has a WRPW sequence, like all of its orthologues, it must act as a repressor, and we
  have shown that it does not interfere with pmar1 expression."]
- No in vitro DNA-binding assay (EMSA) and no anti-HesC antibody/localization data exist
  for the sea urchin protein; the binding-site assignments rest on site mutagenesis in
  reporter constructs plus the family consensus E-box/N-box preference.

## Caveats and later work
- Sharma & Ettensohn 2010 found by quantitative FISH that alx1 and delta are activated in
  prospective skeletogenic cells before hesC transcripts are down-regulated there, and
  argue the double-repression model is insufficient on its own [PMID:20181745 "we find
  that two pivotal early genes in the network, alx1 and delta, are activated in
  prospective skeletogenic cells prior to the downregulation of hesC expression"]. This
  concerns the timing/initiation of derepression, not HesC's repressor function, which is
  supported by the cis-regulatory site mutations.
- The HesC role in the double-negative gate is a euechinoid novelty: in the cidaroid
  Prionocidaris baculosa hesC expression and function are inconsistent with the gate
  [PMID:24924196], and starfish HesC can substitute for sea urchin HesC when expressed in
  the urchin embryo, with klf2 proposed as the ancestral upstream mesoderm regulator
  [PMID:40554761 "We show that starfish HesC is able to perform the function of endogenous
  HesC in the context of sea urchin embryogenesis."].
- In other euechinoids (Hemicentrotus, Scaphechinus) hesC knockdown increases larval
  mesenchyme cell number [PMID:27046223 "The number of larval mesenchyme cells increased
  when the translation of hesC was inhibited"].
- In the cidaroid Eucidaris tribuloides hesc acts downstream of Delta/Notch in ectodermal
  lateral inhibition, consistent with the ancestral Notch-target role of Hes genes
  [PMID:29249002]; in S. purpuratus hesC is Notch-responsive (Su(H) site) and expressed
  in the apical plate, but a neurogenic function has not been tested directly.

## GO curation decisions (see ai-review.yaml)
- Core MF: DNA-binding transcription repressor activity, RNA polymerase II-specific
  (GO:0001227), proposed NEW on the cis-regulatory evidence (delta, alx1, tbr sites).
- Core BP: negative regulation of transcription by RNA Pol II (existing IBA, accepted) and
  NEW negative regulation of mesodermal cell fate specification (GO:0042662, IMP): HesC
  itself performs the repression step that keeps the skeletogenic (mesodermal) regulatory
  state off outside the micromere lineage.
- Not proposed: regulation of Notch signaling (HesC controls where the delta gene is
  transcribed; this is one transcriptional step removed from the pathway itself) and any
  skeletogenesis/biomineralization term (downstream consequence).
- The IBA anterior/posterior pattern specification row is marked over-annotated: the
  vertebrate/nematode evidence at that PAINT node reflects segmentation-clock and seam-cell
  functions with no counterpart shown for sea urchin HesC, whose documented function is
  along the animal-vegetal axis in a lineage-specific gate.

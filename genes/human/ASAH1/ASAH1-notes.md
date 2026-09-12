# ASAH1 (acid ceramidase / N-acylsphingosine amidohydrolase 1) review notes

UniProt: Q13510 (ASAH1_HUMAN). 395 aa precursor. EC 3.5.1.23 (acid ceramidase),
also EC 3.5.1.109 (glucosylceramidase/glycosylceramide deacylase, alternative
catabolism), and a low N-acylethanolamine hydrolase activity.

Deep research: falcon is OUT OF CREDITS (HTTP 402), so no `-deep-research-falcon.md`
was generated. This review is grounded in the UniProt record, the seeded GOA TSV, and
the cached `publications/PMID_*.md` entries. Not fabricating a deep-research file.

## Core biology (verified)

- Lysosomal acid ceramidase. Hydrolyses ceramide -> sphingosine + free fatty acid at
  acidic pH. "Acid ceramidase (AC) is the lysosomal enzyme that degrades ceramide into
  sphingosine and fatty acid" [PMID:10610716]. "hydrolyzes the sphingolipid ceramide
  into sphingosine and free fatty acid" [PMID:8955159].
- Synthesised as a ~53-55 kDa single precursor, autoproteolytically cleaved into
  disulfide-linked alpha (~13 kDa, aa 22-142) and beta (~40 kDa, aa 143-395) subunits.
  Catalytic nucleophile = N-terminal Cys143 of the beta subunit (Ntn hydrolase, MEROPS
  C89). Cleavage is autocatalytic and uses the same Cys; cleavage triggers a
  conformational change that activates the enzyme [PMID:29692406, PMID:30525581,
  PMID:11451951, PMID:7744740].
- Activated in the lysosome by the accessory protein saposin-D (SapD); the crystal
  structure identifies a hydrophobic surface for membrane attachment where substrate is
  delivered "facilitated by the accessory protein, saposin-D" [PMID:29692406].
- Lysosomal targeting is mannose-6-phosphate-receptor-dependent; secretion is
  extremely low [PMID:11451951, PMID:7744740].
- Also has a reverse (ceramide synthase) activity in vitro/in situ (sphingosine + FA ->
  ceramide) at a higher pH optimum (~5.5) [PMID:12764132, PMID:12815059] — this is the
  basis for the "ceramide biosynthetic process" IDA annotations.
- Alternative (spillover) glycosphingolipid catabolism: when GBA1 (Gaucher) or GLA
  (Fabry) are deficient, ASAH1 deacylates the accumulating glucosylceramide/globoside
  to glucosylsphingosine/lysoGb3 [PMID:26898341 (not cached), UniProt MISCELLANEOUS].

## Disease

- Farber lipogranulomatosis (FRBRL, MIM:228000): AR lysosomal storage disorder,
  ceramide accumulation. [PMID:8955159, PMID:10610716, PMID:12638942, ...]
- SMA with progressive myoclonic epilepsy (SMA-PME, MIM:159950): AR; hypomorphic ASAH1
  alleles (e.g. T42M reduces activity to ~32% of normal) [PMID:22703880, PMID:27026573].

## Annotation review reasoning summary

Core MF = GO:0017040 N-acylsphingosine amidohydrolase activity (== acid ceramidase,
EC 3.5.1.23). This is the exact term in the GOA (rows 2, 8, 18, 21-27, 33, 34, 43-45)
across IBA/IEA/IDA/EXP/IMP — strongly supported. ACCEPT the experimental instances;
ACCEPT the IBA/IEA. This is the single core molecular function.

Core BP = ceramide/sphingolipid catabolic process. GOA has GO:0046514 ceramide
catabolic process (IDA/IMP/IEA), GO:0030149 sphingolipid catabolic process (IDA),
GO:0006685 sphingomyelin catabolic process (IDA). ceramide catabolic (GO:0046514) is
the most precise BP for the forward reaction; used as core BP.

Core CC = lysosome / lysosomal lumen. GO:0005764 lysosome (IDA PMID:12764132) and
GO:0043202 lysosomal lumen (TAS Reactome) both well supported; the enzyme is a soluble
luminal hydrolase, so lysosomal lumen (GO:0043202) is the precise location.

### Localization annotations
- Lysosome / lysosomal lumen / endolysosome lumen: ACCEPT (core).
- extracellular region / extracellular space / extracellular exosome / secreted:
  KEEP_AS_NON_CORE. Secretion is real but "extraordinarily low" [PMID:11451951];
  exosome/granule/secretome MS detections are bystander localization, not the site of
  function. Neutrophil granule lumen (tertiary / ficolin-1-rich) Reactome TAS: keep
  non-core (secretome). NOT early endosome / NOT ER (negated IDA PMID:12764132): ACCEPT
  as informative negations.
- nucleus / cytoplasm (IEA & isoform-2 context): KEEP_AS_NON_CORE. UniProt notes a
  nuclear/cytoplasmic localization "most probably for isoforms devoid of a signal
  peptide" and specifically for isoform 2 in the NR5A1/SF-1 story [PMID:22927646].
  These are not the lysosomal enzyme's core site.

### MF over-annotations / generalizations
- GO:0016811 (hydrolase acting on C-N linear amides) IDA PMID:15655246: parent of the
  amidohydrolase activity; MARK_AS_OVER_ANNOTATED (redundant/general vs GO:0017040).
- GO:0017064 fatty acid amide hydrolase activity (IEA InterPro): ASAH1 does have a low
  N-acylethanolamine hydrolase activity [PMID:15655246], so the essence is not wrong,
  but it is a minor/secondary in-vitro activity attributed by an InterPro family map;
  KEEP_AS_NON_CORE.
- GO:0005515 protein binding IPI PMID:22927646 (NR5A1/SF-1): bare protein binding is
  uninformative; the real function is nuclear-receptor binding / transcriptional
  corepression by isoform 2. MARK_AS_OVER_ANNOTATED (per policy do not REMOVE an IPI).

### BP annotations
- ceramide biosynthetic process (GO:0046513 IDA PMID:12764132/12815059): the reverse
  synthase activity is real in vitro but its physiological (in vivo) relevance is
  debated; KEEP_AS_NON_CORE.
- sphingosine biosynthetic process (GO:0046512): sphingosine is the direct product of
  ceramide hydrolysis; ACCEPT as a valid product-forming BP but non-core relative to
  catabolism.
- sphingolipid metabolic process (GO:0006665 IEA), fatty acid metabolic process
  (GO:0006631 IEA InterPro): broad; KEEP_AS_NON_CORE / general parents.
- regulation of programmed necrotic cell death (GO:0062098), cellular response to TNF
  (GO:0071356) — ISS/IEA from mouse ortholog Q9WV54: KEEP_AS_NON_CORE (indirect,
  by-similarity, ceramide-signalling downstream role).
- keratinocyte differentiation (GO:0030216 IMP PMID:17713573): real but tissue/context
  role via sphingolipid signalling; KEEP_AS_NON_CORE.
- regulation of steroid biosynthetic process (GO:0050810 IMP PMID:22261821) &
  transcription corepressor / NR5A1 binding: adrenocortical isoform-2 moonlighting
  role; KEEP_AS_NON_CORE.

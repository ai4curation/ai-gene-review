# ASAH1 review notes

The opening record below is preserved as historical work. Its original action choices, isoform-2 attribution, absolute saposin-D requirement and unqualified substrate/secretion statements are superseded by the dated reassessment that follows. The historical heading "verified" does not describe the current evidence scope.

## Historical review record (superseded where corrected below)

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


## 2026-09-28: source restoration and updated evidence assessment

The existing review has 53 authored decisions and three alternative products. A deterministic seed into a separate working file restores 16 WITH/FROM lists and one additional IC source assertion (GO:0036021, PMID:27498570, GO:0036019 in WITH/FROM). It changes the working status from INITIALIZED to IN_PROGRESS. All previous decisions and other source fields are preserved at this preparatory stage. The superficially similar original IC row remains present. No canonical source cache was edited.

The complete abstracts of all 18 cached papers were read. Most caches are abstract-only; PMID:23533145, PMID:27498570 and PMID:29692406 carry fuller text. Availability metadata is not a claim that the entire article or its supplements was inspected. Below, experimental details from selected body sections are distinguished from abstract-level evidence.

The 2018 structure study uses inactive C143A proenzymes from naked mole rat and minke whale and an autocleaved human enzyme, all expressed in insect cells. The selected Results, figure captions, expression methods and liposome-assay methods inspected support the catalytic and maturation model. The human assay used anionic ceramide-containing liposomes at pH 4. Saposin D increases activity, but enzyme activity is present without it; "requires saposin D" is too absolute. The Discussion explicitly says the biochemical and mutational results suggest that saposin D does not form a complex with acid ceramidase. Neither a complex membership assertion nor a substrate-bound crystal structure should be inferred: the ceramide positioning is modeled. Full supplement and image-pixel inspection has not been performed. [PMID:29692406](https://pubmed.ncbi.nlm.nih.gov/29692406/).

Secretion depends on the experimental context. Normal fibroblasts and the 2001 COS expression system show low secretion, whereas the 2003 amplified CHO overexpression system secreted most enzyme into medium for purification. The latter observation does not establish an extracellular physiological core, but it rules out an unqualified claim that secretion is always extremely low. [PMID:7744740](https://pubmed.ncbi.nlm.nih.gov/7744740/), [PMID:11451951](https://pubmed.ncbi.nlm.nih.gov/11451951/), [PMID:12815059](https://pubmed.ncbi.nlm.nih.gov/12815059/).

The broad amide-hydrolase annotation cites a comparative study that explicitly assayed acid ceramidase as well as NAAA. It reports N-lauroylethanolamine hydrolysis by acid ceramidase. Its NAAA-focused title is not evidence of paralog confusion, and narrowing this row only to ceramide hydrolysis would omit the distinct assayed substrate. The earlier over-annotation rationale therefore needs revision. [PMID:15655246](https://pubmed.ncbi.nlm.nih.gov/15655246/).

The nuclear SF-1 study reports a receptor interaction in H295R cells; generic binding can be refined to a supported receptor-binding function. A general nuclear location does not on its own prove which endogenous splice product was present. The new review must keep any isoform assignment at the actual experimental or UniProt-inference level. [PMID:22927646](https://pubmed.ncbi.nlm.nih.gov/22927646/).

Two additional primary sources were independently identified. Ferraz et al. (2016) reports genetic and pharmacological evidence for acid-ceramidase-dependent formation of glucosylsphingosine and globotriaosylsphingosine when lysosomal glycosidases are deficient. Its complete official PubMed abstract was read; this is a substrate-overload pathway, not evidence that every glycosphingolipid is normally degraded this way. [PMID:26898341](https://pubmed.ncbi.nlm.nih.gov/26898341/).

Nobumoto et al. (2026) uses differentiated human keratinocytes and ASAH1-containing HEK293T culture supernatant to investigate ceramide-class selectivity. The indexed primary Results and captions for figures 6–8, selected Discussion and cell-culture Methods were read. Differentiation markers were largely comparable after 14 days in knockout and control cells despite altered ceramide profiles. This does not by itself overturn the earlier calcium-induced differentiation experiment, which used different conditions. The enzyme assay used culture supernatant, not purified enzyme, and omitted saposin D. Its substrate preferences and limits should be described at that scope. No complete-body, image-pixel or supplement inspection is claimed. [PMID:41570988](https://pubmed.ncbi.nlm.nih.gov/41570988/), [PMID:17713573](https://pubmed.ncbi.nlm.nih.gov/17713573/).

The required falcon/fallback research attempt in this session failed on network resolution. The current manual notes do not masquerade as a provider report. Each additional paper was requested once through the normal fetcher; both attempts failed on DNS resolution with no cache output. Source recovery is needed before final validation and publication of a review citing them.

### Current annotation decisions and source limits

All 54 source objects are retained, including both distinct endolysosome IC assertions and both NOT localization assertions; all three alternative products remain unchanged. The working review has 25 ACCEPT, 25 KEEP_AS_NON_CORE, two MODIFY and two UNDECIDED decisions. There are no NEW rows. The generic SF-1 interaction is refined to GO:0016922 nuclear receptor binding, and the N-lauroylethanolamine experiment refines the broad linear-amide hydrolase class to GO:0017064 fatty acid amide hydrolase activity. Both current GO definitions were checked. These are existing-row refinements, not additional redundant assertions.

The two exosome target inventories (PMID:23533145 and PMID:19056867) remain unverified and are explicitly UNDECIDED. The separate PMID:25645918 extracellular row is retained with curator deference and independent secretion evidence, while its exact target glycopeptide/sputum context remains unverified. Neither missing table establishes contamination or a false annotation.

The PAINT node PANTHER:PTN002005684 is preserved. Direct human biochemistry supports the inherited activity, and human Q13510 in the descendant evidence is expected, not circular. Exact ancestral scope and alignment were not replayed; its source status remains UNRESOLVED rather than implying a reconstructed phylogeny.

A third additional primary source, Strelow et al. (2000), expresses full-length human acid ceramidase in mouse L929 cells and reports protection from TNF-induced caspase-independent death. Official PubMed identity, the complete abstract and selected original plasmid/assay Results were inspected independently. This is independent target-construct corroboration for the existing TNF/death regulation rows, not reconstruction of the mouse Q9WV54 donor chain, a human-tissue experiment, direct TNF binding or a demonstrated RIPK/MLKL mechanism. The current GO:0062098 definition describes regulation of programmed necrotic death; it does not require a particular necroptosis pathway. [PMID:10974027](https://pubmed.ncbi.nlm.nih.gov/10974027/), [GO:0062098](https://amigo.geneontology.org/amigo/term/GO:0062098).

The independent original-paper consultation also inspected PMID:22927646 Fig. 3/Methods, PMID:15655246 human constructs and comparative substrate assays, PMID:12764132 fibroblast localization Results/Fig. 7, and the Reactome Q13510 processed-chain participant hierarchy. The root read every existing cached abstract and selected 2018 structural and 2026 keratinocyte paper sections. This division of actual reading is recorded without claiming every complete body, figure image or supplement was read. Cache availability flags describe the normal cache, not the completeness of external reading.

Each of PMID:26898341, PMID:41570988 and PMID:10974027 had exactly one ordinary fetch attempt, which failed on network resolution and produced no normal cache. Raw diagnostics were discarded; structured attempt records retain error categories and hashes. All three identities were independently verified. A fixed recovery batch is pending; this working draft is not a published or fully validated final review.


### Source53 closure and final evidence attachments

The three additional normal publication records are now imported without overwrite. PMID:10974027 and PMID:41570988 contain XML-derived body text; PMID:26898341 remains abstract-only. The complete metadata and abstracts were reread against these exact records. Selected original Methods/Results for the human-ASAH1/mouse-L929 experiment and the human keratinocyte/supernatant assays agree with the bounded interpretations above. The earlier pending-cache statements record the preparation stage and are now resolved. This source closure does not resolve the two source-specific exosome inventories.

The final draft attaches literal normal-cache passages for the TNF construct, the saposin-D omission and the 14-day differentiation interpretation. A reference finding records glycosphingolipid deacylation under glycosidase deficiency with an abstract-only flag. All 50 quoted passages are literal substrings of their designated normal cache, all availability flags match cache metadata, and all 21 PMID titles match their records. The 54 original/restored source objects, three alternative products and two NOT flags are preserved. Validation, rendering and independent final consultation are recorded separately.

The final source-boundary check further distinguishes the necrotic-death donor annotation from the independent TNF experiment. PMID:10974027 describes atypical apoptosis and explicitly reports no cell swelling or membrane rupture. Its human-construct evidence corroborates general TNF/caspase-independent death regulation, not the exact programmed-necrotic-death class; retention of that class defers to the preserved mouse donor annotation. No action changes follow from this clarification.

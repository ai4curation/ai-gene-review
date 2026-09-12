# irg-2 (C49G7.5, WBGene00016783) — research notes

UniProt: O16224 (IRG2_CAEEL). 278 aa. Chromosome V. Gene name irg-2 = "infection
response gene 2". ORF C49G7.5. This is a research journal; provenance is recorded
inline as `[PMID:xxxx "verbatim quote"]`.

## Identity / disambiguation
- irg-2 = C49G7.5 = WBGene00016783. Confirmed across sources:
  - UniProt: `GN Name=irg-2 {ECO:0000312|WormBase:C49G7.5}; ORFNames=C49G7.5`.
  - Irazoqui et al. 2010 gene table lists `[PMID:20617181 "C49G7.5, WBGene00016783, AF016418"]`.
  - Note the paralogous ORFs in the same cosmid (C49G7.7, C49G7.10) are DIFFERENT
    genes and must not be conflated with irg-2 (=C49G7.5). Several microarray tables
    list C49G7.7 / C49G7.10 separately, so string-matching "C49G7" alone is unsafe.

## Protein-level facts (what the sequence tells us)
- 278 aa, 33 kDa, single CHAIN, no signal peptide, no transmembrane region.
- UniProt annotates only a disordered REGION (152–179) with a polar-residue
  compositional bias (163–179); no catalytic motif, no recognizable domain.
- No PANTHER family assigned at fetch time; UniProt "protein family" field is empty.
- Contrast with the paralog-in-name irg-1, which at least carries a predicted
  NADAR/YbiA-like domain (IPR012816). irg-2 has NO such domain prediction — it is
  even darker at the sequence level than irg-1.
- PE=2 (evidence at transcript level): the protein itself has never been detected;
  everything known about irg-2 concerns its *mRNA* induction, not its protein.

## KNOWN (established, cited)

### 1. irg-2 is a transcriptional infection-response gene induced by P. aeruginosa
- Estes et al. 2010 defined the "infection response gene" (irg) class as genes
  "induced in C. elegans by infection with the bacterial pathogen Pseudomonas
  aeruginosa, but ... not induced by an isogenic attenuated gacA mutant"
  [PMID:20133860 "We focused on genes that are induced in C. elegans by infection with the bacterial pathogen Pseudomonas aeruginosa, but are not induced by an isogenic attenuated gacA mutant."].
  irg-1 is the named reporter of that class; irg-2 is one of the additional class
  members induced by the same virulent-PA14 program. This is the basis of the GOA
  IEP annotations (GO:0140367, GO:0050829), both attributed to PMID:20133860.
- Troemel et al. 2006 (p38 MAPK microarray study) independently place irg-2 (as
  C49G7.5) among the top P. aeruginosa-induced genes at 4 h
  [PMID:17096597 "We tested induction of the top five genes upregulated by P. aeruginosa versus E. coli at 4 h"].

### 2. Induction is via the ZIP-2 bZIP surveillance pathway
- Estes et al. 2010: the RNAi TF screen "identified zip-2, a bZIP transcription
  factor that is required for inducing irg-1, as well as several other genes"
  [PMID:20133860 "This screen identified zip-2, a bZIP transcription factor that is required for inducing irg-1, as well as several other genes, and is important for defense against infection by P. aeruginosa."].
- Hahm et al. 2020 directly measured irg-2 as a ZIP-2 target: it rises with age and
  the rise is ZIP-2-dependent
  [PMID:32350153 "the expression of the ZIP-2 targets irg-1 (Figure 2A) and irg-2 (Figure 2B) increased 24.0-fold and 15.5-fold, respectively, from day 1 to day 8 of adulthood"],
  [PMID:32350153 "indicating that the age-dependent increases in irg-1 and irg-2 expression were largely dependent on ZIP-2."].
  This is the strongest single-gene, full-text-verified statement about irg-2:
  irg-2 is a bona fide ZIP-2 transcriptional target, not merely a co-regulated
  bystander.

### 3. Induction is PMK-1 (p38 MAPK) INDEPENDENT
- Troemel et al. 2006 tested PMK-1-dependence of the top PA-induced genes and found
  irg-2 (C49G7.5) is in the PMK-1-independent set
  [PMID:17096597 "The remaining two genes (C49G7.5 and F53E10.4) must therefore be induced via a PMK-1"].
- Consistent with UniProt INDUCTION: dependent on zip-2, independent of pmk-1
  p38MAPK, dbl-1 TGF-beta, and kgb-1 JNK pathways (ECO:0000269|PubMed:20133860).

### 4. Induction is triggered by translational inhibition (surveillance immunity)
- Dunbar et al. 2012 showed the zip-2/irg pathway is switched on by pathogen-induced
  block of translation, sensed via endocytosed Exotoxin A
  [PMID:22520465 "P. aeruginosa infection inhibits mRNA translation in the intestine via the endocytosed translation inhibitor Exotoxin A, which leads to an increase in ZIP-2 protein levels."],
  and more generally by "disruption of several core host processes, including
  inhibition of mRNA translation"
  [PMID:22520465 "In the absence of infection we find that the zip-2/irg-1 pathway is upregulated following disruption of several core host processes, including inhibition of mRNA translation."].
  UniProt attributes irg-2 FUNCTION/INDUCTION by ToxA and cycloheximide to this
  paper (ECO:0000269|PubMed:22520465). NOTE: the cached PMID_22520465.md is
  ABSTRACT-ONLY (full_text_available: false); the abstract names irg-1, not irg-2,
  but UniProt curators read the full text and attributed irg-2 to it. Per repo
  policy I do not overturn that; I cite the abstract-level surveillance mechanism
  and defer irg-2-specific detail to the curator.

### 5. Broader expression context
- HEP annotation (GO:0045087) traces to Shapira et al. 2006, a genome-wide screen
  that found endodermal GATA factor ELT-2 governs intestinal infection responses
  [PMID:16968778 "Gene expression and functional RNAi-based analyses identified the tissue-specific GATA transcription factor ELT-2 as a major regulator of an early intestinal protective response to infection with the human bacterial pathogen Pseudomonas aeruginosa."].
  irg-2 is one of the ELT-2/infection-responsive transcripts in that dataset — hence
  the HEP (high-throughput expression pattern) evidence code. This ties irg-2 to the
  intestinal epithelium as the likely site of expression.
- Bgee (via UniProt) reports expression in pharyngeal muscle cell and 2 other cell
  types — consistent with a low-level, tissue-restricted transcript that is
  strongly infection-inducible.
- irg-2 recurs in later P. aeruginosa / mitochondrial-UPR immunity expression
  datasets (Irazoqui et al. 2010, PMID:20617181; the mitochondrial-UPR immunity
  study, PMID:25274306) as an infection-responsive transcript, reinforcing that its
  signature is transcriptional induction, not a measured activity.

## NOT KNOWN (the deliverable for this dark gene)
1. **Molecular function — entirely unknown.** No catalytic activity, no binding
   partner, no biochemical assay. GOA carries GO:0003674 (molecular_function) as ND.
   Unlike irg-1, irg-2 has no domain prediction to even hypothesize an activity.
2. **Is the IRG-2 protein required for defense?** Every claim is expression-based
   (IEP/HEP). No irg-2 loss-of-function survival phenotype on P. aeruginosa has been
   reported; whether IRG-2 protein contributes to resistance vs. is a passive readout
   of ZIP-2 activation is undetermined. (Estes 2010 shows zip-2 — the regulator — is
   needed for defense; that is not the same as showing irg-2 the effector is.)
3. **Subcellular localization** of IRG-2 protein — unknown. It is intestinally
   expressed at the tissue level but the protein has never been localized (PE=2).
4. **Direct antimicrobial activity** — untested. It is grouped with "antimicrobial
   effectors" by pathway position, not by any demonstrated bactericidal/bacteriostatic
   activity.
5. **Regulatory logic beyond ZIP-2** — the ZIP-2/CEBP-2 cis-elements in the irg-2
   promoter, and whether irg-2 and irg-1 are co-regulated identically, are not mapped.
6. **Conservation / orthology** — eggNOG ENOG502TKK2 (Eukaryota) and OrthoDB group
   exist, but no functionally characterized ortholog anchors a function; effectively
   a nematode-restricted sequence orphan for functional purposes.

## Annotation-by-annotation plan (GOA has 4)
1. GO:0140367 antibacterial innate immune response — IEP, PMID:20133860 → ACCEPT
   (BP-level, expression-based; the defining role). Non-core caveat: functional
   requirement unproven.
2. GO:0003674 molecular_function — ND, GO_REF:0000015 → ACCEPT (honestly reflects an
   MF-dark gene; this IS the knowledge gap, not a curation defect).
3. GO:0050829 defense response to Gram-negative bacterium — IEP, PMID:20133860 →
   ACCEPT (P. aeruginosa is Gram-negative; specific and expression-supported).
4. GO:0045087 innate immune response — HEP, PMID:16968778 → ACCEPT (broader parent;
   independent high-throughput expression support; C. elegans immunity is all innate).

No REMOVE/MODIFY warranted: all four are expression-based BP/ND annotations that are
internally consistent with the literature. The honest gap is the missing MF, captured
in `knowledge_gaps`, not fixable by re-labeling an existing annotation.

## Deep research provenance note
- `just deep-research-falcon worm irg-2 --fallback perplexity-lite`: the first falcon
  attempt timed out (Edison API saturated by many concurrent jobs) and the
  perplexity-lite fallback 401'd on quota; the falcon RETRY then succeeded and wrote a
  genuine `irg-2-deep-research-falcon.md` (Edison Scientific Literature, 39 citations,
  ~1300s). It is committed and cited only for its high-level synthesis that IRG-2 is
  functionally uncharacterized ("No enzymatic activity has been assigned to the
  protein"), which independently corroborates the GOA ND molecular_function.
- IMPORTANT: the falcon report also makes specific claims via unverifiable PMID-token
  citations — notably an ENDU-2/heat-stress transcriptional-regulation model (Xu 2023)
  and a WormCat/immunity-linked-genes framing (Fanelli 2023), and it alludes to
  loss-of-function phenotypes. None of these token citations could be resolved to
  cached, PubMed-verified papers, so they are DELIBERATELY NOT imported into the
  review. If those papers are later located and verified, the "effector-vs-reporter"
  knowledge gap (gap 2) should be revisited. The review otherwise rests on UniProt
  (O16224), the GOA TSV, and the six cached publications below, all quote-verified
  against the local `publications/` cache.

## References gathered (verified against cache)
- PMID:20133860 Estes 2010 PNAS — irg class definition, zip-2 (abstract-only). HIGH.
- PMID:22520465 Dunbar 2012 Cell Host Microbe — translational-inhibition surveillance
  (abstract-only; UniProt attributes irg-2 induction). HIGH.
- PMID:17096597 Troemel 2006 PLoS Genet — C49G7.5=irg-2 PMK-1-independent (full text). HIGH.
- PMID:32350153 Hahm 2020 Aging — irg-2 ZIP-2 target, aging/mito surveillance (full text). HIGH.
- PMID:16968778 Shapira 2006 PNAS — ELT-2/intestinal immunity, HEP source (abstract-only). MEDIUM.
- (Context only, not added as review refs: PMID:20617181 Irazoqui 2010 gene table;
  PMID:25274306 mito-UPR immunity table.)

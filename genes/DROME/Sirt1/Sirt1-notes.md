# Sirt1 (Sir2, dSir2, CG5216, FBgn0024291, UniProtKB:Q9VK34) review notes

Date: 2026-11-16. De-novo review for the MOD descriptions project (IBA-novel batch).

## Sources used

- FlyBase hand-written description (`Sirt1-deep-research-flybase.md`), UniProt Q9VK34, GOA (51 rows).
- No Falcon/Perplexity deep research (no API keys). Literature searched with WebSearch and PubMed
  E-utilities; queries recorded below.
- PANTHER 19.0 tree for PTHR11085 and the PAINT IBD.gaf snapshot: `Sirt1-bioinformatics/RESULTS.md`.
- Existing reviews read for comparison: `genes/human/SIRT1` and the family review
  `interpro/panther/PTHR11085/PTHR11085-review.yaml` (coordinator checkout).
- QuickGO's `includeFields=taxonName` returned HTTP 500 on 2026-11-16; the GOA file was fetched through a
  wrapper that drops that include field and fills the taxon name from taxon id 7227.

## Literature queries run

- WebSearch: "Drosophila Sir2 Sirt1 H4K16 acetylation H3K9 acetylation mutant histone deacetylase specificity"
  (led to Parsons et al. 2003, PMID:12571358).
- WebSearch: "Feller Forne Imhof Becker 2015 histone acetylome systematic perturbation Sir2 depletion H4K16
  H3K9 Drosophila S2 cells" (author copy of PMID:25578876 read from the LMU repository).
- PubMed E-utilities: Banerjee 2012 (PMID:22411915), Whitaker 2013 (PMID:24036492), Reis 2010
  (PMID:21085633), Das 2009 (PMID:19270680), Bauer 2009 (PMID:19851477, not used), Åström 2003
  (PMID:12663533), Rogina & Helfand 2004 (PMID:15520384).

## Enzyme activity and histone specificity

- dSir2 is an NAD-dependent histone deacetylase; recombinant dSIR2 deacetylates all four H4 tail lysines
  [PMID:11281647 "dSIR2 is an NAD-dependent histone deacetylase"]
  [PMID:11281647 "All these proteins have in vitro deacetylase activity and are able to deacetylate core histone H4 at all four acetylatable lysine residues (5, 8, 12, and 16)."].
- Purified recombinant dSir2 has broad lysine specificity
  [PMID:12571358 "found that dSir2 deacetylates a broad range of acetylated lysine residues"].
  The full text (PMC149880, read online; the local cache is abstract-only) gives the sites: "dSir2
  catalyzes the deacetylation of K9 and K14 of H3 and K5, K12, and K16 of H4 as well as K18 and K23 of H3
  and K5 and K20 of H2B"; only H4K8 is weakly deacetylated. This is the fly evidence for the H3K9, H3K14
  and H4K16 IBA rows (in vitro, NAD-dependent, broad).
- dSir2 also deacetylates H3K56ac [PMID:19270680 "whereas Drosophila Sir2 and human SIRT1 and SIRT2 deacetylate H3K56ac"].
- Produces O-acetyl-ADP-ribose like other Sir2 enzymes
  [PMID:11812793 "We demonstrate that the production of O-acetyl-ADP-ribose is evolutionarily conserved among Sir2-like enzymes from yeast, Drosophila, and human."].
- In vivo, histone specificity is not site-selective: in Kc cells depletion of any of the eight KDACs
  (SIR2 included) raised many H4 and most H3 acetylation motifs alike (Feller et al. 2015, author copy:
  "Unlike KATs, KDACs are characterised by relaxed substrate specificity."); abstract quote
  [PMID:25578876 "Systematic depletion of known or suspected acetyltransferases and deacetylases revealed specific alterations of histone acetylation signatures"].
  Ethanol inebriation lowers Sir2 and raises H3 acetylation in brain
  [PMID:27170122 "Acute inebriation strongly reduces Sir2 levels and increases histone H3 acetylation in the brain."].
- Non-histone substrates: HNF4 [PMID:27058248 "We show that Sir2 exerts these effects by deacetylating and stabilizing dHNF4 through protein interactions."],
  FASN K813 [PMID:36459649 "Lastly, we find that K813 is deacetylated by Sirt1, which brings FASN activity to baseline level."],
  Su(H) [PMID:27623778 "Moreover, Sirt1 participates in the deacetylation of the CSL transcription factor Suppressor of Hairless."],
  FOXO [PMID:22876196 "Increased Dyrk1a activated Sirt1 to regulate the deacetylation of FOXO, which potentiated FOXO-induced sNPF/NPY expression and in turn promoted food intake."].

## Silencing

- Heterochromatic silencing (PEV): dSir2 mutants are recessive suppressors of PEV
  [PMID:12524341 "The dSir2 mutants are viable, fertile, and recessive suppressors of position-effect variegation (PEV)"];
  the effect is modest [PMID:12663533 "We did observe a modest, strictly recessive suppression of white(m4) position-effect variegation and a shortening of life span in dsir2 homozygous mutants"].
- Not required for telomeric silencing
  [PMID:12086602 "is required for heterochromatic silencing, but unlike ySir2, is not required for silencing at telomeres"].
- Polycomb silencing and polytene chromosome binding
  [PMID:15498488 "Evidence is presented that Drosophila SIR2 is also involved in epigenetic silencing by the Polycomb group proteins."]
  [PMID:15498488 "SIR2 binds to many euchromatic sites on polytene chromosomes and colocalizes with E(Z) at most sites."].
- copia repression with PARG [PMID:16219773 "Reducing the level of either PARG or the silencing protein SIR2 weakens copia transcriptional repression."].
- Euchromatic repression with Hairy/Dpn/E(spl): physical and genetic interaction [PMID:12086602].
  Rosenberg & Parkhurst's claims that dSir2 is essential and needed for segmentation and sex
  determination were not reproduced with a clean null
  [PMID:12663533 "homozygosity for dsir2(17) had no apparent deleterious effects on viability, developmental rate, or sex ratio, and it fully complemented sir2(ex10)"]
  [PMID:12663533 "Moreover, through a genetic test, we ruled out the reported effect of dSir2(ex10) on Sex-lethal expression."].
  Independent nulls are viable and fertile [PMID:12524341; PMID:19951294 "These Sir2 null mutant flies were fully viable and fertile, and showed no obvious morphological or behavioral defects."].
- In vitro, dSir2 represses transcription from hyperacetylated histone-DNA templates
  [PMID:12571358 "we observed potent (50- to 100-fold) NAD-dependent transcriptional repression by purified dSir2"].

## Physiology

- Metabolism: fat body Sir2 limits fat storage [PMID:21085633 "We show that knockdown of Sir2 in the larval fat body results in increased fat levels."];
  adult fat body Sir2 for fat mobilisation [PMID:22411915]; insulin sensitivity via HNF4 [PMID:27058248].
- Apoptosis: overexpression drives JNK/FOXO-dependent apoptosis; loss partly blocks UV-induced apoptosis
  [PMID:18562277 "we find that a loss-of-function sir2 mutant partially prevents apoptosis induced by UV irradiation in the eye"].
- Ethanol responses: Sir2 in mushroom bodies [PMID:27170122]; Sir2 null mutants alter ethanol tolerance [PMID:19951294].
- Feeding: Mnb/Dyrk1a-Sir2-FOXO-sNPF [PMID:22876196].
- Notch: Sirt1 promotes Notch signalling in SOP specification and wing [PMID:27623778].

## Lifespan controversy

- Overexpression extends lifespan and Sir2 is needed for DR effects [PMID:15520384 "We demonstrate that an increase in Drosophila Sir2 (dSir2) extends life span, whereas a decrease in dSir2 blocks the life-span-extending effect of calorie reduction or rpd3 mutations."].
- Burnett et al. 2011: with matched transgenic controls there is no effect, and DR works without dSir2
  [PMID:21938067 "We found that dietary restriction increased fly lifespan independently of dSir2."].
- Whitaker et al. 2013: modest (2 to 5-fold) induction extends lifespan, higher levels are toxic
  [PMID:24036492 "Using approaches that allow us to titrate dSir2 expression, we describe here a strong dose-dependent effect of dSir2 on life span."].
- Loss-of-function shortens lifespan in some studies [PMID:12663533; PMID:17159295 "Suppression of the Sir2 in neurons and ubiquitous silencing of the Sir2-like genes shortened life spans."],
  not in others [PMID:12524341 title: "does not affect life span"]. The lifespan role is unresolved.
- GOA has a NOT|involved_in determination of adult lifespan row from Burnett et al. (IMP). The paper
  refutes the overexpression and dietary-restriction claims but its authors state
  [PMID:21938067 "Our findings do not rule out a role for sirtuins in determination of metazoan lifespan"].
  The NOT row is REMOVED as over-reaching; the positive IMP (Kusama 2006) is KEEP_AS_NON_CORE.

## PAINT node placement (Sirt1-bioinformatics/RESULTS.md)

Fly Sirt1 is the 1:1 ortholog of human SIRT1 (single member of PTN000872223). PTN000872222 (Eukaryota):
corepressor, DNA damage response, subtelomeric heterochromatin, H3K9/H3K14/H4K16 NAD-dependent
deacetylase. PTN000872223 (Metazoa-Choanoflagellida): negative regulation of transcription, rDNA
heterochromatin, nucleoplasm, nuclear inner membrane (the last two seeded by human SIRT1 only).

## Verdicts on the non-duplicative IBA rows

| Term | Action | Short reason |
|---|---|---|
| GO:0003714 transcription corepressor activity | ACCEPT | binds Hairy/Dpn/E(spl) repressors; NAD-dependent repression in vitro |
| GO:0005637 nuclear inner membrane | MARK_AS_OVER_ANNOTATED | single human seed; fly protein is nucleoplasmic/chromatin |
| GO:0006974 DNA damage response | KEEP_AS_NON_CORE | UV-induced apoptosis partly Sir2-dependent; H3K56ac deacetylation |
| GO:0031509 subtelomeric heterochromatin formation | REMOVE | yeast-only seeds; fly Sir2 not needed for telomeric silencing |
| GO:0032041 H3K14 deacetylase, NAD-dependent | ACCEPT | purified dSir2 deacetylates H3K14 (PMC149880) |
| GO:0033553 rDNA heterochromatin | MARK_AS_OVER_ANNOTATED | single human seed (eNoSC); no fly data |
| GO:0045892 negative regulation of DNA-templated transcription | ACCEPT | Hairy, PcG, copia silencing |
| GO:0046969 H3K9 deacetylase, NAD-dependent | ACCEPT | purified dSir2 deacetylates H3K9 (PMC149880) |
| GO:0046970 H4K16 deacetylase, NAD-dependent | ACCEPT | two fly in vitro studies |

The GO:0000781 chromosome, telomeric region IEA is derived mechanically from the GO:0031509 IBA and is
removed with it.

## UniProt FUNCTION defects

- "Mildly suppresses the heterochromatin-mediated silencing phenomenon known as position-effect
  variegation (PEV)." Direction inverted: the mutants suppress PEV, so the protein promotes silencing.
- "Required for epigenetic silencing of the polycomb group proteins." Should be silencing by PcG proteins.
- "Required maternally for establishing proper segmentation of the embryo. Involved in sex
  determination." From Rosenberg & Parkhurst 2002 with the ex10 allele; not reproduced with clean nulls
  (Åström 2003, Newman 2002, Kong 2010).

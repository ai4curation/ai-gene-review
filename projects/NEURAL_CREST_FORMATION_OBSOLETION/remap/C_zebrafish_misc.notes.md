# Group C remap notes: zebrafish case-by-case, X. tropicalis sox9, chick Id2

Input: `C_zebrafish_misc.input.tsv` (38 rows). Output: `C_zebrafish_misc.tsv`.
Checker: `check_remap.py` reports 0 errors. Papers were cached with `just fetch-pmid` on 2026-10-09.
Replacement GO labels were checked on QuickGO. GO has no term for neural crest cell
apoptosis or survival; QuickGO and OLS searches return nothing.

Most ZFIN rows carry `acts_upstream_of_or_within`. The curator therefore claimed
requirement, not direct participation. Where the evidence is a late or non-specific
morphant phenotype, the replacement is the general GO:0014033 or a regulation term,
not a specification term.

## zeb2a / zeb2b (sip1a/sip1b), PMID:18351671: REPLACE with GO:0014033 (28 rows, IMP and IGI)
- The cache has the abstract only (`full_text_available: false`). The PMC full text
  (PMC2443937) came back empty from the PubMed MCP.
- The abstract reports that knockdown of both genes leads to "a significant reduction/loss of
  the post-otic cranial neural crest", with downstream loss of arch and enteric
  precursors. It does not say whether specification, survival or migration fails.
  Zeb2/Sip1 is a BMP-signalling inhibitor, and mouse Sip1 has a known role in delamination,
  but the abstract does not support a specific step. We use GO:0014033 and keep the curator's qualifier.
- Decision is the same for every accession of each paralog. The full text could tighten
  this, for example to delamination or migration.

## polr1b, PMID:31649276 (UniProt, involved_in): REPLACE with GO:0006360 transcription by RNA polymerase I
- Full text was checked. Morphants show reduced 47S pre-rRNA, with Pol III 5S unaffected,
  p53-dependent apoptosis of the neuroepithelium "fated to differentiate into NCCs", and fewer
  migrating sox10+/foxd3+ cells. sox10+ NCCs were themselves TUNEL-negative.
- polr1b does Pol I transcription. The crest phenotype comes from the precursors' need for
  ribosomes, which is a necessity effect, not a crest step (see CLAUDE.md "Do not add what
  curators deliberately declined to add"). The paper directly measures pre-rRNA, so it
  supports GO:0006360. Comparator: the ribosome-biogenesis genes in group B (TCOF1, NOLC1)
  should be handled the same way.
- **Uncertainty:** the alternative is REMOVE with no replacement. A GO:0014033 call was not used
  because nothing specific to crest is shown.

## cnbpa, PMID:21999883: REPLACE with GO:0014033
- The cache has the abstract only. Cnbp knockdown alters the balance of proliferation and
  apoptosis in cranial crest and "skeletogenic neural crest cell fate", which is a
  derivative-level fate, not crest identity. Specification is not supported, so the general
  term is used.

## chd7, PMID:22363697: REPLACE with GO:0014033
- Full text was checked. The only crest assay is fli1:GFP cranial crest segments at 34–36 hpf,
  which are reduced or disorganized. The authors say it is unresolved whether this is migration
  or arch patterning. A specification role for CHD7 is cited from other work (PBAF, Bajpai 2010),
  not shown here. General term.

## snw1, PMID:21358802: REPLACE with NTR neural plate border formation and GO:1905297 positive regulation of neural crest cell fate specification
- Full text was checked. SNW1 acts upstream of BMP receptors and sets a horseshoe-shaped domain
  of BMP activity at the neural plate border. Zebrafish morphants lose sox10/foxd3 and the neural
  plate expands. BMP2b expressed at the border rescues crest fate.
- This is a signalling-modulator case under the project rule. The border-formation NTR reflects
  the shifted neural/non-neural border. The regulation term reflects the indirect, upstream
  qualifier. GO:0030513 positive regulation of BMP signaling pathway would also be defensible,
  but it is not a crest remap.

## hsbp1b, PMID:24380799: REPLACE with GO:1905296 negative regulation of neural crest cell fate specification
- Full text was checked. Knockdown expands the expression domains of tfap2a, snai2 and foxd3
  at 12 hpf and raises Hsf1 activity and Hsp expression. The direction of the effect is
  negative. The mechanism (Wnt? Hsf1?) is unresolved, which fits a regulation term.
  The evidence is morpholino-only.

## sox10 (zebrafish), PMID:34099848: REPLACE with GO:0014036
- Full text was checked. The genotype is a cis-regulatory deletion (sox10min promoter / peak5
  enhancer). It reduces or abolishes embryonic sox10 expression and perturbs adult pigment
  stripes. The paper does not assay crest specification as such.
- GO:0014036 is chosen for gene-level consistency with the reviewed Xenopus SoxE genes
  (sox8, sox9-a, sox10). **Uncertainty:** judged on this paper alone, GO:0014033 would be the
  defensible call.

## sox9 (X. tropicalis, Xenbase), PMID:22927467: REPLACE with GO:0014036
- Full text was checked. The experiments are in X. laevis embryos; the Xenbase mapping
  to the tropicalis gene is not questioned. Non-SUMOylatable Sox9 induces crest precursors,
  and Grg4 represses crest markers (Slug, Sox10) in a way that depends on SoxE SUMOylation.
  This is consistent with sox9-a (GO:0014036).

## Id2 (chick O73933), PMID:15242799 (IEP, AgBase): REMOVE
- The cache has the abstract only. Ablating cardiac crest causes outflow-tract Id2 expression
  to be lost, so Id2 expression depends on the presence of crest. That makes Id2 a
  downstream readout, and the evidence is expression-only. No process replacement
  (project rule: "expression is not participation").

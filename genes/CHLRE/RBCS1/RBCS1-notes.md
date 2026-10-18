# RBCS1 (P00873) review notes

## Deep research

Ran `scripts/deep_research_wrapper.py CHLRE RBCS1 falcon --fallback perplexity-lite` once
(2026-10-03). Falcon failed with HTTP 402 (Payment Required) from the Edison API, and
the perplexity-lite fallback failed because the `perplexity` provider is not available
in this environment. I did not retry. This review uses the cached primary literature
and the UniProt record instead.

## Identity

- Nuclear gene CHLRE_02g120100v5; 185-aa precursor with a 45-aa chloroplast transit
  peptide (UniProt TRANSIT 1..45, ECO:0000269 PMID:11641402); the mature chain
  (46..185) is N-methylated at Met-46.
- Two small-subunit genes in Chlamydomonas [PMID:3820291 "The two genes encode variant
  small subunits that differ by four amino acid residues. Both genes are expressed"].

## Complex and catalysis

- L8S8 holoenzyme [PMID:11641402 "Overall, the structure shows high similarity to the
  previously determined structures of L8S8 Rubisco enzymes."].
- Active site is in the large subunit; the SSU modulates kinetics [PMID:20424165
  "Although the large subunit contains the active site, a family of rbcS nuclear genes
  encodes the Rubisco small subunits, which can also influence the carboxylation
  catalytic efficiency and CO(2)/O(2) specificity of the enzyme."].
- Deletion of both RBCS genes: photosynthesis-deficient and rescued by either gene
  [PMID:8942995 "Thus, either small subunit is sufficient for holoenzyme assembly and
  function."]; the large subunit is not made without the SSU [PMID:8942995 "In the
  absence of small subunits, expression of chloroplast-encoded large subunits appears to
  be inhibited at the level of translation."].
- Curation consequence: GO:0016984 should be **contributes_to** for the SSU. The UniRule
  IEA ("enables") is applied to all RbcS, for example Arabidopsis P10795 and spinach
  P00870 (checked in QuickGO). No other RbcS review exists in this repository to follow
  (grep of genes/ for Rubisco small subunit found none), so I followed the
  non-catalytic-subunit precedent in genes/PSEAE/pqsB (MARK_AS_OVER_ANNOTATED, then
  contributes_to in the core function).

## Pyrenoid role (SSU helices)

- The helices control pyrenoid formation [PMID:23112177 "higher plant-like helices
  knock out the pyrenoid, whereas native algal helices establish a pyrenoid."]. The
  reciprocal mutant was built in native RBCS1 [PMID:23112177 "The reverse construct
  (substituting the algal helices with the spinach helices) was undertaken on a vector
  that contained the native Chlamydomonas RbcS1"].
- Plant-SSU hybrids are catalytically proficient but lack pyrenoids [PMID:20424165 "It
  appears that small subunits contain the structural elements responsible for targeting
  Rubisco to the algal pyrenoid"].
- Cryo-EM: 8 EPYC1 sites per holoenzyme, one per SSU [PMID:33230314 "each Rubisco
  holoenzyme has eight binding sites for EPYC1, one on each Rubisco small subunit.
  Interface mutations disrupt binding, phase separation and pyrenoid formation."].
  The RBCS1 point mutants D23A/E24A and M87D/V94D lack the pyrenoid matrix.
- Y2H interaction depends on the SSU helices [PMID:31504763 "Interaction is crucially
  dependent on the two surface-exposed α-helices of the Chlamydomonas SSU."].
- Rubisco plus EPYC1 are necessary and sufficient for LLPS [PMID:30498228].
- RbcS1-Venus in the pyrenoid matrix [PMID:28938114 "A portion of the RbcS1-Venus and
  EPYC1-Venus signals rapidly dispersed from the pyrenoid matrix into the stroma"].

## Decisions

- chloroplast IEA: ACCEPT. pyrenoid: NEW (IDA, PMID:28938114).
- carbon fixation, reductive pentose-phosphate cycle IEA: ACCEPT. The SSU is a
  structural subunit of the enzyme that catalyses the step, so it contributes
  structure to it.
- ribulose-bisphosphate carboxylase activity IEA (enables): MARK_AS_OVER_ANNOTATED, to
  be stated as contributes_to.
- chloroplast Rubisco complex GO:0009573: NEW.
- I did not add a NEW BP for pyrenoid or membraneless organelle assembly. The SSU helices
  are a structural part of the condensate, so a case can be made, but GO has no
  pyrenoid-assembly term and adding a process to the client of the condensate was
  judged too far without curator input. Raised as a suggested question and knowledge gap.

## Module consistency (modules/pyrenoid_ccm.yaml)

The module lists RBCS1 as an active unit of GO:0009573, with no required_function. The
annoton function is GO:0016984 in GO:0019253 at the pyrenoid. All of this is consistent
with the review: contributes_to GO:0016984, in_complex GO:0009573, location GO:1990732,
process GO:0019253.

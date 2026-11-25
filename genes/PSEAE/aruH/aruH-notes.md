# aruH (PA4976, Q9HUI9) review notes

No deep-research API was available. Manual research on 2026-11-05 from the cached
publications (PMID:17416668 abstract; PMID:17416670 full text), a Europe PMC
title search ("aruH" / "arginine transaminase" AND Pseudomonas; PubMed MCP and
E-utilities were returning errors) and the UniProt record (reviewed).

## Biology

- AruH is a class I PLP-dependent aminotransferase that catalyses the first step
  of the arginine transaminase (ATA) pathway, L-arginine + pyruvate to
  2-ketoarginine + L-alanine [PMID:17416668 "High-performance liquid chromatography
  and mass spectrometry (MS) analyses were employed to detect the presence of the
  transamination products 2-ketoarginine and L-alanine, thus demonstrating the
  proposed biochemical reaction catalyzed by AruH"]. The recombinant enzyme was
  purified to homogeneity; ping-pong kinetics, Km 13.9 mM for L-arginine and
  1.6 mM for pyruvate, pH optimum 9.0, homodimer.
- Substrate range Arg > Lys > Met > Leu > Orn > Gln [PMID:17416668 "it has a novel
  substrate specificity with an order of preference of Arg > Lys > Met > Leu > Orn >
  Gln"].
- Genetics: an aruH knockout abolishes the arginine-inducible
  arginine:pyruvate transaminase activity of an aruF background and its growth on
  arginine [PMID:17416670 "This ATase activity was abolished when an aruH knockout
  was introduced into the strain."]. The ATA pathway is the second aerobic
  arginine catabolic route after the AST pathway; aruHI are induced by arginine
  via AruRS.
- AruH is not the AspC aspartate transaminase it was originally annotated as
  [PMID:17416670 "we concluded that AruH is not the homologue of E. coli AspC"].
- GO term: GO:0047635 L-alanine:oxo-acid transaminase activity has RHEA:13833
  (L-arginine + pyruvate = 5-guanidino-2-oxopentanoate + L-alanine, EC 2.6.1.84)
  as a narrowMatch xref, so it is the most specific existing GO term for the AruH
  reaction (no EC 2.6.1.84-specific term exists in go-basic, checked
  2026-11-05). GO:0047635 is_a GO:0140385 is_a GO:0008483, so the generic
  transaminase rows are TOO_GENERAL.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002482828 | GO:0008483 transaminase activity | 2 | 57 (41 taxa) | GO:0008483, IDA, PMID:17416668 (PseudoCAP; UniProt has the same IDA) | SOUND | Purified recombinant AruH transaminates arginine with pyruvate; products identified by HPLC and MS; abstract states it outright. Under-specific (GO:0047635 fits better) but true. | Synechocystis AspC Q55128 (EXP GO:0004069 aspartate transaminase, PMID:24302739, PMID:25070637) | Yes |

The node mixes arginine:pyruvate and aspartate transaminases, so the generic
transaminase term is the right level. No PSEUDOCAP or GO_CENTRAL defect: the
PseudoCAP row is true, merely general, and UniProt independently made the same
IDA.

## Action summary

ACCEPT: GO:0047635 (IEA), GO:0006527 (IDA, IMP, IEA). KEEP_AS_NON_CORE: GO:0030170
(IDA, IEA). TOO_GENERAL: GO:0003824, GO:0006520, GO:0008483 (IBA, IDA, IEA).

# DTD1 (YDL219W, Q07648) — S. cerevisiae D-aminoacyl-tRNA deacylase

## Deep research status

- 2026-10-20: `just deep-research-falcon yeast DTD1 --fallback perplexity-lite` failed.
  Falcon (Edison API) returned "Failed to authenticate"; the perplexity-lite fallback
  returned HTTP 401 (insufficient quota). No deep-research file exists. The review was
  done from the cached primary literature, the UniProt record and the PANTHER/PAINT
  context below.
- PubMed search ("DTD1 OR YDL219W OR D-tyrosyl-tRNA deacylase" AND yeast) returned only
  one yeast DTD1 functional paper (PMID:10766779); the D-amino acid screen
  (PMID:10918062) also covers yeast. The other hits concern human DUE-B or fission yeast.

## Experimental findings in S. cerevisiae itself

- DTD1 shares 34% identity with E. coli Dtd. Overexpression raises D-Tyr-tRNA(Tyr)
  deacylase activity in crude extracts about 100-fold; deletion lowers it by >90% and
  makes growth more sensitive to D-Tyr [PMID:10766779 "Overexpression in the yeast of the
  DTD1 gene from a multicopy plasmid increased D-Tyr-tRNA(Tyr) deacylase activity in crude
  extracts by two orders of magnitude"; "Upon disruption of the chromosomal gene,
  deacylase activity was decreased by more than 90%"].
- Yeast TyrRS makes D-Tyr-tRNA(Tyr) in vitro, so the substrate forms in vivo
  [PMID:10766779 "the capacity of purified S. cerevisiae tyrosyl-tRNA synthetase to produce
  D-Tyr-tRNA(Tyr) could be shown"].
- In a screen of all 19 D-amino acids, only D-Tyr and D-Leu were more toxic to dtd1
  deletion cells. The authors infer that D-Leu-tRNA(Leu) is also a substrate, but
  this is a genetic inference. The abstract does not report a D-Leu-tRNA(Leu)
  deacylation assay [PMID:10918062 "Toxic effects of d-tyrosine and d-leucine were
  reinforced upon deprivation of the deacylase. This observation suggests that..."].
- Cytoplasmic GFP localisation in the genome-wide screen (PMID:14562095, HDA).

So, experimentally established **in yeast**: D-Tyr-tRNA(Tyr) deacylase activity
(extract activity depends on DTD1 dosage), cytoplasmic localisation, and protection
against D-Tyr (plus D-Leu) toxicity. Inferred only: activity on D-Leu-tRNA(Leu)
(genetic), Gly-tRNA(Ala) deacylation (family), homodimer and the Gly-cisPro mechanism
(structural homology).

## Evolutionary grounding

- PANTHER PTHR10472:SF5 (D-AMINOACYL-TRNA DEACYLASE 1). This is the same subfamily as
  human DTD1 (Q8TEA8). The family also includes E. coli Dtd. HAMAP MF_00518, NCBIfam
  TIGR00256, Pfam PF02580 (UniProt record).
- PAINT node PTN000049487: yeast DTD1 (SGD:S000002378) is an experimental donor, together
  with mouse Dtd1 and E. coli Dtd (P0A6M4). The node propagates D-tyrosyl-tRNA(Tyr)
  deacylase activity, tRNA metabolic process and cytoplasm. It does **not** propagate
  Gly-tRNA(Ala) deacylase activity (GO:0106026). That may be deliberate, or the node may
  predate the term. Either way, yeast GO:0106026 rests only on ISS from P. falciparum DTD
  (Q8IIS0) and a Rhea IEA.
- The Gly-cisPro motif is conserved in yeast DTD1: the sequence at residues 135-150 is
  SLTNE**GP**VTIILDSDQ (G140-P141), matching UniProt's MOTIF annotation (by similarity
  to Q8IIS0). The structural basis of L-chiral rejection by this cross-subunit
  dipeptide comes from P. falciparum DTD [PMID:24302572].
- Gly-tRNA(Ala) deacylation is conserved in vitro across E. coli, P. falciparum,
  Leishmania, Drosophila and zebrafish DTDs. Yeast DTD1 was not tested
  [PMID:28362257 "DTD's activity on non-cognate Gly-tRNAAla is conserved across all
  bacteria and eukaryotes"].

## Notes for transfer to human DTD1

Yeast is a donor for the activity/cytoplasm IBA, not for any DUE-B DNA-replication
biology. The DNA-binding C-terminal extension of human DUE-B has no counterpart in
the 150-aa yeast protein, so yeast cannot ground those functions.

## Nonsense suppression (SGD description follow-up, 2026-11-01)

SGD says DTD1 "may affect nonsense suppression via alteration of the protein synthesis
machinery". The source is an overexpression screen for genes that alter tRNA-mediated
nonsense suppression in a Mod5-limited strain [PMID:10618371 "We identified SAL6 , TEF4 , and
YDL219w, all of which likely affect nonsense suppression via alteration of the protein synthesis
machinery."]. Overexpressed YDL219w did not change i6A tRNA levels. This is a one-off
overexpression phenotype with no mechanism, so it is recorded as peripheral and is not
annotated. It fits the deacylase role in keeping translation accurate but does not test it.

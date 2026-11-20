# MET17 notes (YLR303W, P06106; MET15/MET25)

- O-acetylhomoserine sulfhydrylase / homocysteine synthase, PLP enzyme [PMID:36455053 "Met17p catalyzes the fixation of inorganic sulfide with O-acetylhomoserine (OAHS) to form homocysteine"]; in vitro assays [PMID:36379252 "We then carried out in vitro reactions using the canonical OAH and H2S substrates as well as PLP, a cofactor critical for Met15 activity."]
- Alternative homocysteine synthase Hsu1/Yll058w rescues met17 [PMID:36379252 "Thus, Met15 is not essential for inorganic sulfur assimilation in yeast."]
- Dual OAS/OAH sulfhydrylase in vitro [PMID:795806 "catalyzing the sulfhydrylation of both O-acetyl-L-serine (OAS) and O-acetyl-L-homoserine (OAH)"], but OAS route not native [PMID:15042590 "This pathway is not conserved in yeast, where cysteine is synthesized in a four-step pathway starting with homoserine and having O-acetylhomoserine, homocysteine and cystathionine as intermediates."]; [UniProt:P06106 "therefore has no metabolic role in cysteine biosynthesis and may only"].
- PLP: [PMID:795806 "Lysine appeared to be the pyridoxal binding site"].

## Curation observations
- Cysteine synthase activity rows kept as non-core (real in vitro, not physiological).
- Obsolete GO:0019346 transsulfuration (InterPro) REMOVED; threonine metabolism RCA (P4-PWY-1) REMOVED.
- The PTHR43797 cytoplasm IBA is sound for Met17's soluble activity but was
  marked `MODIFY` to cytosol because the gene already carries accepted cytosol
  rows from yeast-specific evidence.

## 2026-10-24 re-review

Fetched `yeast/MET17` with `just fetch-gene yeast MET17`; GOA, UniProt,
and the existing review were already current. `just fetch-gene-pmids yeast
MET17` cached all 10 GOA PMIDs. Falcon deep research and the Perplexity
fallback were attempted but no research-provider API keys were configured, so
this pass used cached publications, UniProt, manual PubMed/web search, and
the local PTHR43797 PAINT table.

The compact `PTHR43797` family has a current `PTN002887184` node carrying
`GO:0005737`, `GO:0051009`, and `GO:0071269`. The same node still appears on
the stale 2023 `GO:0004124` IBA row in GOA, but the current PAINT export no
longer places cysteine synthase activity there.

Direct and newer evidence:

- Classical biochemistry established that the same purified yeast enzyme
  sulfhydrylates both O-acetylserine and O-acetylhomoserine in vitro
  [PMID:795806 "catalyzing the sulfhydrylation of both O-acetyl-L-serine (OAS) and O-acetyl-L-homoserine (OAH)"].
  The 1994 recombinant MET17/MET25 paper expressed the gene in E. coli and
  found the gene product indistinguishable from the enzyme purified from yeast
  [PMID:7765825 "The Saccharomyces cerevisiae MET17/MET25 gene encoding O-acetyl-L-serine (OAS).O-acetyl-L-homoserine (OAH) sulfhydrylase"].
- Mulet et al. showed that the O-acetylserine route is not native to yeast;
  cysteine is normally made from homoserine through O-acetylhomoserine,
  homocysteine, and cystathionine, while heterologous plant serine
  O-acetyltransferase can create an alternative pathway that uses Met17's
  O-acetylserine sulfhydrylase side activity [PMID:15042590 "This pathway is not conserved in yeast, where cysteine is synthesized in a four-step pathway starting with homoserine and having O-acetylhomoserine, homocysteine and cystathionine as intermediates."].
- Two 2022 studies independently found that `YLL058W`/`HSU1` can bypass
  `met17` loss by reassimilating accumulated H2S and forming homocysteine,
  but they kept Met17 as the efficient canonical homocysteine synthase
  [PMID:36379252 "an alternative homocysteine synthase encoded by the previously uncharacterized gene YLL058W enables cells lacking Met15 to assimilate enough inorganic sulfur for survival and proliferation"];
  [PMID:36455053 "Hsu1p acts as a homocysteine synthase and allows the cells to substitute for Met17p by reassimilating hydrosulfide ions leaked from met17Δ cells into O-acetyl-homoserine and forming homocysteine"].
- Sonal et al. 2023 independently confirmed that met17 deletion cells can
  grow on sulfate in a density- and gas-exchange-dependent manner through
  Hsu1, while also emphasizing that purified Met17's OAS sulfhydrylase
  side activity is unlikely to be relevant in vivo in S. cerevisiae
  [PMID:38060626 "the locus YLL058W (HSU1) enables met17Δ cells to assimilate hydrogen sulfide"].

Manual searches for newer MET17/MET15 homocysteine synthase literature found
the 2023 Hsu1/gas-exchange paper as the newest direct primary paper changing
the old strict-auxotrophy framing. Later 2024-2025 hits used `met17` as an
established sulfur-assimilation block, or concerned MET17 promoters and
metabolic engineering, rather than revising the Met17 function itself.

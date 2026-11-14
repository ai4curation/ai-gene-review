# estA (PA5112, UniProtKB:O33407) notes

Accession check: the reviewed entry for PA5112 is O33407 (ESTA_PSEAE, 646 aa).
Q9HUP2, which appears in the WITH/FROM of the carboxylic ester hydrolase IBA, is
a different protein: PA4921, an unreviewed GDSL lipase/acylhydrolase (PANTHER
PTHR45648) that is the second seed of that IBD through a PseudoCAP IDA choline
esterase row (PMID:22192836). Checked by UniProt REST and QuickGO, 2026-10-28.

No deep-research provider was available; the notes below come from my own
reading of the cached abstracts (all key EstA papers are abstract-only in the
cache; PMC full text of PMID:17631636 was requested via the PubMed MCP but came
back empty) and of the UniProt record.

## What EstA is

- Outer-membrane autotransporter with an N-terminal GDSL/SGNH esterase passenger
  domain and a C-terminal 12-stranded beta-barrel. Discovered as the residual
  esterase in a lipase-negative mutant [PMID:10559163 "A lipase-negative deletion
  mutant of Pseudomonas aeruginosa PAO1 still showed extracellular lipolytic
  activity toward short-chain p-nitrophenylesters"].
- Surface exposure of the catalytic domain: [PMID:10559163 "Trypsin treatment of
  whole cells released a significant amount of esterase, indicating that the
  enzyme was located in the outer membrane with the catalytic domain exposed to
  the surface"].
- Full-length crystal structure (PDB 3KVN): [PMID:20060837 "EstA has a relatively
  narrow, 12-stranded beta-barrel that is covalently attached to the passenger
  domain via a long, curved helix"]; [PMID:20060837 "The esterase active-site
  residues are located at the apical surface of the passenger"].
- Substrates: short-chain p-nitrophenyl esters (C4-C6), Tweens, beta-naphthyl
  butyrate; triacylglycerols and acyl-CoAs negligible (UniProt CC FUNCTION, from
  PMID:17631636 and PMID:20931591). [PMID:20931591 "TesA, EstA and EstP were
  shown to function as esterases with different affinities and catalytic
  efficacies towards p-nitrophenyl butyrate"]; [PMID:20931591 "Of all the enzymes
  tested, only SrLip revealed lipase, phospholipase, esterase, thioesterase and
  Tweenase activities"]. So EstA is a carboxylesterase (EC 3.1.1.1), not a true
  lipase. UniProt kinetics: KM 0.7 mM for p-nitrophenyl butyrate.
- Family: GDSL autotransporter esterases (EstP of P. putida, ApeE of
  Salmonella, McaP etc.) [PMID:21598370 "The esterase EstA of Pseudomonas
  aeruginosa is a typical enzyme of this type"].

## Phenotypes (Wilhelm et al. 2007, PMID:17631636, abstract only)

- [PMID:17631636 "an estA deletion mutant produced only marginal amounts of
  rhamnolipids"]; overexpression increases rhamnolipid.
- Motility and biofilm: [PMID:17631636 "the other kinds of motility displayed by
  P. aeruginosa PAO1, swimming and twitching, were also affected by an estA
  mutation"].
- Active-site S->A variant (EstA*) does not complement any phenotype
  [PMID:17631636 "None of the mutant phenotypes could be complemented by
  expression of EstA*"]. This shows that esterase activity is needed, and (with
  the 1999 paper) supports the esterase MF; it does not identify the step.
- UniProt (curated): "the exact role of EstA in these processes is unclear".
- Overexpression in a mucoid (alginate-producing) strain [PMID:20360178
  "Overexpression of estA resulted in a loss of twitching motility, although it
  enhanced the ability to swim and swarm"], and the authors themselves say the
  effects are "directly or indirectly" exerted.
- Overexpression raises rhamnolipid titre 3.9-fold [PMID:28837648 "the modified
  strain produced up to 3.9 times more RMLs than the WT"]; biotechnological, no
  mechanism.

## Interpretation

Rhamnolipid synthesis is performed by RhlA (HAA synthesis from
beta-hydroxyacyl-ACP), RhlB and RhlC (rhamnosyltransferases), which act at the
cytoplasm/inner membrane. EstA is a surface-exposed outer-membrane esterase that
has negligible activity on acyl-CoA and triacylglycerols. No paper identifies a
rhamnolipid intermediate as an EstA substrate. The requirement of EstA is
therefore a necessity phenotype of unknown mechanism (possibly membrane
remodelling, release of rhamnolipid, or signalling), not participation in a
biosynthetic step. Swimming, twitching and swarming are all lost in the mutant;
these disparate motility systems (flagellar, type IV pilus) point to a
pleiotropic, likely rhamnolipid/surface-mediated effect, not to EstA acting in
the flagellar machinery.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN005219546 | GO:0052689 carboxylic ester hydrolase activity | 2 (O33407, Q9HUP2/PA4921) | 960 (51 taxa) | GO:0052689 IMP PMID:17631636 (PseudoCAP); also GO:0106435 IDA PMID:20931591 (UniProt) | SOUND | Active-site S38A variant is inactive; esterase activity of purified/surface EstA measured in 1999, 2007 and 2010 papers, KM for pNP-butyrate known; GDSL/SGNH catalytic triad conserved and structurally resolved. IBD is appropriate for a family of GDSL esterases. On EstA itself the term is correct but general (GO:0106435 carboxylesterase activity is supported). |
| PTN005219546 | GO:0008610 lipid biosynthetic process | 1 (O33407, sole seed) | 960 (51 taxa) | GO:0008610 IMP PMID:17631636 (UniProt) and GO:0009247 glycolipid biosynthetic process IMP PMID:17631636 (PseudoCAP) | INDIRECT-PHENOTYPE | Both seed rows rest on the estA deletion lacking rhamnolipid. EstA is an outer-membrane, surface-exposed esterase with no activity on acyl-CoA; the biosynthetic steps are catalysed by RhlA/RhlB/RhlC; UniProt itself states the role is unclear. A necessity phenotype is not participation. The IBD therefore projects an unsupported biosynthetic process to 960 GDSL autotransporter esterases in 51 taxa; it should be withdrawn. |

Note: strictly the GO:0008610 seed row was assigned by UniProt; the PseudoCAP row
(GO:0009247) is a descendant term from the same paper and also supports the
node. Both are recorded as source defects (UNIPROT and PSEUDOCAP), and the IBD
is recorded as a GO_CENTRAL defect.

Other PseudoCAP rows (not seeds):
- GO:0044010 single-species biofilm formation IMP: phenotype, kept as non-core
  (widely accepted GO practice for bacterial biofilm IMP), no defect.
- GO:0071973 flagellum-dependent cell motility IMP: over-annotation; twitching
  (pilus) is lost too, so the term asserts a mechanism that is not shown.
- GO:0071978 swarming IDA PMID:20360178: the evidence is an overexpression
  phenotype, which GO codes as IMP, not IDA; also indirect.

## Open questions

- Which ester substrate does EstA hydrolyse in vivo, and how does that affect
  rhamnolipid levels (biosynthesis, export, or turnover/regulation)?
- Does the effect on rhamnolipid act via the quorum-sensing regulators of rhlAB?

## 2026-11-14: full text of PMID:17631636 read

The earlier pass through this gene was made from the abstract alone, because
`ai-gene-review fetch-pmid 17631636 --force` cannot retrieve PMC2045186 by
either the HTML or the PDF route and leaves the cache abstract-only. The
publisher version was supplied directly (J Bacteriol 189:6695-6703,
doi:10.1128/JB.00023-07) and has now been read in full. Because the cache still
holds only the abstract, nothing below is quoted as `supporting_text` in the
review: quotes there must be verbatim substrings of the cached file, and a quote
the validator cannot check is worse than a paraphrase that is honest about its
source. The findings are recorded as `findings[].statement` and in row reasons.

What the full text settles:

- **Rhamnolipid is not made by EstA.** The authors state there is no obvious
  function in the rhamnolipid biosynthesis pathway that would directly require an
  esterase, and no rhamnolipid accumulates inside the mutant, which rules out a
  block in export or hydrolytic turnover. Their preliminary transcriptome work
  finds *rhlB* and *rhlC* significantly downregulated in the *estA* mutant, so
  EstA sits upstream of the enzymes that do the biosynthetic work, acting
  "probably by hydrolysis of a yet-unknown compound". This strengthens the
  `MARK_AS_OVER_ANNOTATED` calls on GO:0008610 and GO:0009247 rather than
  changing them. I considered escalating to `REMOVE` and did not: the requirement
  is real and depends on catalytic activity (the Ser38->Ala variant fails to
  complement), so the rows are not false, they assert the wrong relation for a
  genuine dependency.
- **The motility defect does not run through rhamnolipid.** Adding wild-type
  amounts of rhamnolipid back to the mutant's medium does not restore motility;
  the authors conclude the rhamnolipid deficiency is not the reason for the
  motility defects. My earlier reason on GO:0048870 proposed exactly that
  mechanism and was wrong; it has been corrected.
- **The flagellar row is the weakest of the motility rows.** Type IV pilus genes
  (*pilA*, *pilX*, *pilG*, *pilB*) are downregulated, which the authors say
  explains twitching and swarming, but they report no change in flagellar gene
  expression that would explain the loss of swimming. GO:0071973 therefore names
  the one motility form the paper cannot account for.
- **The biofilm phenotype is secondary to non-motility,** not to rhamnolipid:
  mutant biofilms show reduced surface coverage and large aggregates separated by
  low-density regions, "as expected for nonmotile strains that can expand only by
  clonal growth". The earlier reason attributed it to rhamnolipid and has been
  corrected.
- **Ser38 is the catalytic nucleophile.** It is the serine of the GDSL motif
  (31-STLVVFGDSLSDAGQF-46) in the displayed O33407 sequence, and UniProt carries
  both `ACT_SITE 38 /note="Nucleophile"` and a `MUTAGEN 38` feature citing this
  paper, so the paper's numbering matches the canonical sequence directly.
- The authors are explicit that the phenotypes "have no obvious physiological or
  regulatory link and thus cannot be explained satisfyingly and in a
  comprehensive way at the moment".

Answers an open question above: the rhamnolipid effect is **not** mediated by
quorum sensing. The *A. tumefaciens* AHL bioassay shows the *estA* mutant
produces AHLs at wild-type levels, so the EstA-dependent effect on rhamnolipid is
not a consequence of altered autoinducer levels. The other open question (which
ester substrate EstA hydrolyses in vivo) remains open, and the authors say
settling it will require lipid-composition analysis plus fuller transcriptome
data.

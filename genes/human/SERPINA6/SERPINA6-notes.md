# SERPINA6 (corticosteroid-binding globulin, CBG, transcortin; UniProt P08185) — review notes

Journal of the review. Residue numbers are on the 405-residue UniProt precursor (HGVS p.) unless
marked *mature*; mature = precursor - 22 (signal peptide 1-22). Almost all CBG papers and all PDB
entries use mature numbering.

## 2026-11-26 Session 1: setup and provenance

- `just fetch-gene human SERPINA6`: 15 GOA rows, PANTHER PTHR11461:SF34.
- Deep research. The default provider (falcon) and its perplexity-lite fallback are not installed in this
  environment (`Provider 'falcon' not available. Available: asta, openscientist, claude_code`).
  `just deep-research-asta human SERPINA6` completed (`SERPINA6-deep-research-asta.md`, retrieval-only; its
  first hits are off-target transcriptomics papers, so it was used only as a recall list).
  `just deep-research-openscientist human SERPINA6` was launched twice (the first run was lost to a
  container restart); see the last section for its status.
- Own literature search (PubMed, 2026-11-26). Queries and yields:
  - `(SERPINA6[Title/Abstract] OR "corticosteroid-binding globulin"[Title]) AND (mutation OR variant OR deficiency)` — 105 hits, top 60 cached.
  - `"corticosteroid-binding globulin" AND (neutrophil elastase OR reactive centre loop OR crystal structure OR chymotrypsin OR LasB)` — 52 hits, top 40 cached.
  - `(Serpina6 OR "corticosteroid-binding globulin") AND (knockout OR "deficient mice" OR null mice)` — 28 hits, all cached.
  - `corticosteroid-binding globulin variants cortisol-binding Greek woman` — 1 hit (PMID:22948765, CBG Athens).
  - Full text was available from PMC for about a third of the cached papers; the primary variant papers
    (PMID:1504007, 8212073, 10634411, 11502797, 20610591, 22013108, 22337907, 22948765, 25322275) are
    abstract-only in the cache.
- Search for any report of protease inhibition by CBG: none found. Every paper that addresses the
  question describes CBG as a substrate, not an inhibitor (below).

## What the protein is and does

**Plasma carrier of glucocorticoids and progesterone.** CBG is a liver-made secreted glycoprotein that
carries most circulating cortisol.
[PMID:3299377 "CBG mRNA is relatively abundant in the liver but is also present in the lung, testis, and kidney"]
[PMID:24424442 "Corticosteroid-binding globulin (CBG) binds more than 90% of circulating cortisol and is a non-inhibitory member of the family of serine protease inhibitors (SERPINS)"]
[PMID:19011238 "Corticosteroid-binding globulin (CBG) is a non-inhibitory serine proteinase inhibitor (serpin) that transports cortisol and progesterone in blood"]
[PMID:7195404 "The binding affinities of 21 endogenous steroids for both testosterone-binding globulin (TeBG) and corticosteroid-binding globulin (CBG) were determined under equilibrium conditions"]
[Reactome:R-HSA-1449687 "functions as a plasma transporter of corticosteroids such as progesterone, aldosterone, cortisol and 11-deoxycorticosterone"]

**A serpin that is a protease substrate, not an inhibitor.** The serpin fold was recognised from the
cDNA [PMID:3299377 "there is a remarkable similarity between the amino acid sequences of CBG and of alpha 1-antitrypsin"],
but the one direct test shows no inhibition:
[PMID:2370299 "unlike A1-PI, CBG does not alter the activity of this enzyme, but is cleaved by it at a single location close to its carboxy-terminus, and this reduces its molecular size by 5 kDa with the concomitant release of more than 80% of CBG-bound cortisol"].
Neutrophil elastase cuts the reactive-centre loop (RCL) at Val344-Thr345 (mature)
[PMID:38042488 "rapidly and specifically cleaves the RCL at Val344–Thr345"]; chymotrypsin and
*Pseudomonas aeruginosa* LasB also cut the loop
[PMID:24424442 "Here we show, for the first time, rapid chymotrypsin cleavage of the RCL of CBG"]
[PMID:24848868 "Among the bacteria tested, medium from Pseudomonas aeruginosa actively disrupted the cortisol-binding activity of CBG"].

**Serpin S-to-R transition repurposed as a hormone-release switch.** Cleavage inserts the loop into
beta-sheet A and lowers steroid affinity through helix D and its connecting loop.
[PMID:18513745 "CBG has adapted an allosteric mechanism of the serpins to allow equilibrated release of the hormones by a flip-flop movement of the intact reactive loop into and out of the beta-sheet"]
[PMID:17644521 "complete insertion of the proteolytically cleaved RCL into the serpin fold occurs in concert with a displacement and unwinding of helix D that would disrupt the steroid-binding site"]
[PMID:21325280 "a much larger effect occurs allosterically due to stretching of the connecting loop to the top of the D helix (hD)"]
Affinity also falls with temperature, so fever releases cortisol
[PMID:23783094 "with a doubling for every 2°C rise in body temperature"]. Whether elastase-cleaved CBG
circulates is disputed: [PMID:30452386 "Human CBG with a NE-cleaved RCL and low affinity for steroids is absent in blood samples"].

**Glycosylation.** Six N-x-S/T sequons (precursor 31, 96, 176, 260, 330, 369; mature 9, 74, 154, 238, 308, 347).
The glycan at mature Asn238 is needed for steroid binding and the one at Asn347 in the RCL tunes proteolysis.
[PMID:29273683 "mutations of conserved N-glycosylation sites at N238 in human CBG and N230 in rat CBG disrupt steroid binding"]
[PMID:27339896 "site-specific CBG N-glycosylation regulates the bioavailability of cortisol in inflamed environments by fine-tuning the RCL proteolysis by endogenous and exogenous elastases"]

**Physiology: a buffered reservoir, not only a passive carrier.**
[PMID:16980625 "The absence of CBG resulted in a lack of corticosterone binding activity in serum and in an approximately 10-fold increase in free corticosterone levels in CBG-null mice"]
[PMID:16980625 "the mice exhibited increased activity of the pituitary axis of hormonal control, normal levels of gluconeogenetic enzymes, and fatigue, as well as an aggravated response to septic shock"]
[PMID:20022933 "free corticosterone concentrations are normal at rest but present a reduced surge after stress in transcortin-deficient mice"]
[PMID:22930537 "the impact of CBG genetic deficiency on various behavioral patterns reported previously stems from a smaller CORT reservoir in blood"]
[PMID:21054475 "CBG null patients lack a CBG-bound pool of readily releasable cortisol"]
The two mouse lines disagree on resting free corticosterone (10-fold raised in PMID:16980625, normal in
PMID:20022933); both agree that total hormone and the stress surge are reduced.
Local release by neutrophil elastase is supported in vivo:
[PMID:39788946 "NE and AAT regulate local tissue glucocorticoid bioavailability in vivo"].
CBG also shapes adrenal development in a sex-dependent way in rodents
[PMID:36112420 "sex differences in adrenal growth, morphology and gene expression profiles that emerge during puberty in rats are dependent on concomitant increases in plasma CBG produced by the liver"];
this is an indirect, endocrine-feedback effect and is not treated as a function of the protein.

## Disease: corticosteroid-binding globulin deficiency (MIM 611489, MONDO:0012675)

All reported disease alleles are **loss of function**: either no protein (null alleles), less secreted
protein, or protein that binds cortisol weakly or not at all. No gain-of-function and no
dominant-negative allele is reported, and none is expected for a monomeric carrier: heterozygotes for
null alleles have about half the normal CBG
[PMID:11502797 "Plasma immunoreactive corticosteroid-binding globulin was undetectable in null homozygotes, and mean corticosteroid-binding globulin levels were reduced by approximately 50%"]
[PMID:34308089 "Plasma CBG levels were reduced approximately 50% in the proband and mother"],
which is a gene-dosage (haploinsufficiency) effect on the carrier pool. Inheritance is best described
as semidominant/codominant for the biochemical trait
[PMID:6499234 "CBG deficiency, a benign condition, is compatible with a codominant or recessive autosomal trait inheritance"].

Biochemical hallmark: low total cortisol with normal free cortisol and ACTH.
[PMID:20610591 "All mutant homozygotes have very low total serum cortisol, but normal free serum cortisol levels"]
[PMID:10634411 "an increase in the percentage of nonprotein-bound cortisol offsets the low cortisol levels to give approximately normal concentrations of free cortisol in serum"]
Clinical picture: fatigue, chronic pain, relative hypotension, with incomplete penetrance.
[PMID:11502797 "Homozygotes and heterozygote null mutation subjects had a high prevalence of hypotension and fatigue"]
[PMID:21795453 "Of 12 Lyon participants (four males and eight females), eight (two males and six females) had chronic widespread pain"]
[PMID:22013108 "often in association with fatigue and chronic pain, albeit with incomplete penetrance"]
Penetrance is genuinely low: a secretion-defective allele carried by about 1 in 36 Han Chinese produced no
clinical difference in pregnancy [PMID:25695888 "reported no unusual clinical symptoms"], and the original
report called the condition benign (PMID:6499234).

**Open question (disease mechanism).** Why fatigue and pain arise when free cortisol is normal is
unresolved. Candidate explanations in the literature: loss of the releasable CBG-bound pool, so the
stress surge and local delivery are blunted (PMID:21054475, PMID:22930537, PMID:20022933); altered
ultradian pulsatility [PMID:20610591 "The only biochemical feature to distinguish the symptomatic subject was increased cortisol pulsatility"];
ascertainment bias in families found through fatigue clinics. The authors of the largest kindred say so:
[PMID:11502797 "The mechanism of the association between fatigue and relative hypotension is not established by these studies"].

## Variants placed on the protein (from `SERPINA6-bioinformatics/RESULTS.md`)

Everything in this section is computed by `SERPINA6-bioinformatics/02_analyze.py`; numbers are quoted
from its `RESULTS.md`.

- Numbering check: all 20 literature variants have the reported reference residue at the converted
  position. One naming trap: the common polymorphism at canonical Ser246 was first reported the right way
  round [PMID:1504007 "another which encodes a Ser----Ala substitution at residue 224"]; gnomAD gives
  p.Ser246Ala an allele frequency of 0.48. Later papers that write "A224S" swap reference and alternate.
  `[file:human/SERPINA6/SERPINA6-bioinformatics/RESULTS.md "reference and alternate are swapped relative to the UniProt canonical sequence"]`
  (Until the 2026-11-28 review round the input file encoded this variant as A224S, so earlier text and the
  first history record say 19 of 20; the record is now S224A with A224S as a checked alias.)
- "p.Gly237Val" in PMID:20610591 is mature numbering written with a p. prefix: c.776G>T changes codon 259,
  i.e. p.Gly259Val. Leu93/Leu115 and Glu102/Glu124 are both the reported residue in either numbering, so
  only the cDNA position disambiguates them (c.344T>A, c.371A>G).
- Steroid pocket (heavy atom within 4.0 A of cortisol or progesterone in 2VDY, 4C49, 4BB2), mature
  numbering: A18, S19, V22, Q232, T240, F242, R260, I263, N264, S267, F366, H368, W371. The four UniProt
  binding-site positions (254, 286, 390, 393) are all inside this set.
- RCL: P1 is mature Thr349 (precursor 371) by the register of PMID:19011238; elastase cuts the P6-P5
  bond, releasing a 39-residue C-terminal fragment. The AlphaFold model has the loop exposed (native-like,
  low pLDDT); all human crystal structures are loop-cleaved.

| Variant (mature) | HGVS p. | Assay result (source) | Where it sits | Structural reading | Class |
|---|---|---|---|---|---|
| Null/Adelaide | p.Trp11Ter | no CBG (PMID:11502797) | signal peptide | stop before the mature chain | null, LoF |
| Santiago | p.Leu5CysfsTer26 | 50% CBG in heterozygotes (PMID:22013108) | signal peptide | frameshift, no mature chain | null, LoF |
| Montevideo | p.Val55GlyfsTer44 | 50% CBG in heterozygotes (PMID:34308089) | first helix | truncated at 14% of the precursor | null, LoF |
| A51V | p.Ala73Val | binds normally, poorly secreted (PMID:22337907) | buried, second helix | fully buried Ala (RSA 0.01); larger side chain in the core | secretion-defective LoF |
| I48N | p.Ile70Asn | secretion defect (PMID:25322275) | buried, second helix | polar residue in the hydrophobic core | secretion-defective LoF |
| P246Q | p.Pro268Gln | secretion defect (PMID:25322275) | buried, invariant Pro | loss of a conserved buried proline | secretion-defective LoF |
| Athens W371S | p.Trp393Ser | no binding (PMID:22948765) | pocket, 2.9 A from steroid | removes the indole that stacks on the steroid; invariant in 73 orthologues | binding LoF |
| R260L | p.Arg282Leu | no binding (PMID:25322275) | pocket, 3.2 A | removes a steroid-contacting Arg and its salt bridge to Asp23 | binding LoF |
| Lyon D367N | p.Asp389Asn | 4-fold lower affinity (PMID:10634411); no measurable binding (PMID:22948765); almost devoid of binding, heat-labile (PMID:20226861) | buried, 4.6 A from steroid | carboxylate caps the 366-371 loop (H-bonds to F369 N, T370 N and OG1) that carries pocket residues F366, H368, W371 | binding LoF |
| G237V | p.Gly259Val | no binding (PMID:20610591) | next to glycosylated Asn238 | Gly has phi +111; a beta-branched Val cannot adopt it; neighbour of pocket residue H368 and of the Asn238 sequon | binding LoF |
| Leuven L93H | p.Leu115His | 3-fold lower affinity (PMID:1504007) | helix 4 (serpin helix D), 13 A | part of a His14-His89-Leu93 contact cluster on helix D | binding LoF, second shell, mechanism unresolved |
| H14Q / H14R | p.His36Gln / p.His36Arg | lower affinity / capacity (PMID:25322275) | N-terminal segment, 9 A | same cluster | binding LoF, second shell, mechanism unresolved |
| H89Y | p.His111Tyr | lower affinity (PMID:25322275) | helix 4, 13 A | same cluster; Tyr is wild type in rodent CBG | binding LoF, second shell, mechanism unresolved |
| E102G | p.Glu124Gly | low binding capacity (PMID:22337907) | strand, 15 A, exposed | loses a salt bridge to Lys159; mechanism not resolved | binding LoF, unexplained |
| I279F | p.Ile301Phe | lower affinity, protease-resistant (PMID:25322275) | buried strand, 15 A | fully buried; larger side chain in the sheet the RCL inserts into | binding LoF, unexplained |
| I179V | p.Ile201Val | slower loss of binding after protease (PMID:25322275) | buried strand | conservative change in the sheet | altered protease response |
| R64Q / R64W | p.Arg86Gln / p.Arg86Trp | normal (PMID:22337907) | third helix, 21 A | remote | benign |
| S224A ("A224S") | p.Ser246Ala | normal affinity (PMID:1504007) | exposed strand, 17 A | common polymorphism, AF 0.48 | benign |

`[file:human/SERPINA6/SERPINA6-bioinformatics/RESULTS.md "Of these, pairs whose side chains are in contact (<= 4.5 A, AlphaFold model): H14-H89 (3.24 A); H14-L93 (3.61 A); H89-L93 (3.01 A)"]`

Mechanistic reading by class:

1. **Null alleles** (signal-peptide stop or frameshift, early frameshift): no steroid-binding protein.
2. **Secretion-defective missense** (A51V, I48N, P246Q): fully buried residues of the serpin core, far
   from the steroid; the protein that does fold binds normally (A51V). Loss of quantity.
3. **Pocket missense** (W371S, R260L, and second-shell D367N, G237V): direct loss of steroid contacts or
   of the local geometry that positions them. Loss of affinity with normal quantity.
4. **Helix D cluster** (H14, H89, L93): three positions 9-13 A from the steroid whose side chains touch
   each other. Helix D and its connecting loop are the published allosteric link between the RCL and the
   steroid site (PMID:18513745, PMID:17644521, PMID:21325280), which made a shared allosteric effect an
   attractive reading. The OpenScientist hypothesis run on exactly this question (last section) supports
   the geometry and not the single mechanism, so the class is left as unresolved.

Population genetics agrees with a mild, tolerated loss of function: pLI is 0 and LOEUF is 1.06; 42
high-confidence loss-of-function alleles are in gnomAD v4 including one homozygote for the Montevideo
frameshift; Leuven has 3 homozygotes and A51V has 9.
`[file:human/SERPINA6/SERPINA6-bioinformatics/RESULTS.md "Constraint: pLI = 0; observed/expected loss-of-function = 0.72 (90% CI 0.50-1.06; 19 observed, 26.4 expected)"]`
AlphaMissense is uninformative here: 9 of 13 experimentally defective missense variants are scored likely
benign, including Athens W371S, which abolishes binding. The likely cause is that the gene is under
almost no purifying selection, so sequence-based predictors see little signal.

### Disagreements between sources (recorded, not resolved)

- **Lyon D367N severity.** PMID:10634411 measured a 4-fold affinity reduction in recombinant protein
  (CHO cells); PMID:22948765 found no measurable cortisol binding of recombinant D367N; and a third
  expression system (293-EBNA) found it nearly inactive and heat-labile
  [PMID:20226861 "Certain mutants are almost devoid of cortisol binding activity (Q232R and CBG Lyon), some display higher sensitivity for heat inactivation (G335V, Q232R and CBG Lyon)"].
  Two of three recombinant studies therefore say near-null. All are abstract-level reads. The structural
  placement (buried carboxylate capping the pocket loop) fits a destabilised, heat-sensitive site.
  PMID:20226861 was pointed out by the companion dismech session and then fetched and read here; it also
  states [PMID:20226861 "So far no CBG serpin partner protease has been identified."].
- **Resting free corticosterone in Cbg-/- mice**: 10-fold raised (PMID:16980625) versus normal (PMID:20022933).
- **Review text error.** PMID:41180195 says of Leu93His "this mutation was named CBG A224S"; it is CBG Leuven.
- **ClinVar.** Lyon and Leuven are "Conflicting classifications of pathogenicity"; given allele
  frequencies of 3.6e-4 and 2.5e-3 with homozygotes, and low penetrance, that conflict is expected.

## Annotation review decisions (summary)

- `GO:0004867` serine-type endopeptidase inhibitor activity (IBA, IEA, TAS): REMOVE. Contradicted by the
  direct assay (PMID:2370299) and by the field's consistent description of CBG as non-inhibitory. The TAS
  paper (PMID:3299377) reports sequence homology with serpins; its abstract makes no inhibitor claim, and
  the full text is not in the cache, so the row-level source defect is filed as a query, not a correction.
  The IBA comes from PAINT node PTN008970140 (chordate clade-A serpins); the CBG clade is PTN008322172.
  The family review asks PAINT for a loss (IRD) at that node.
- `GO:0005496` steroid binding: the IDA row (crystal structure with cortisol) is refined to
  `GO:1903794` cortisol binding; the IEA row (ortholog transfer) stops at steroid binding and is kept.
- `GO:0140104` molecular carrier activity: EXP row refined to `GO:0005319` lipid carrier activity (a
  steroid is a lipid; GO has no steroid-hormone carrier term, proposed below); IEA row kept.
- `GO:0005576` extracellular region: accepted on all six rows (`GO:0005615` extracellular space is
  obsolete in the validation release, so no refinement is available).
- `GO:0070062` extracellular exosome (HDA): kept as non-core; an abundant plasma glycoprotein co-isolated
  with urinary vesicles.
- `GO:0006704` glucocorticoid biosynthetic process (Reactome TAS): REMOVE. CBG catalyses nothing; it is
  in the Reactome pathway only through the plasma-binding reaction R-HSA-1449687. The mouse GO-CAM
  `gomodel:68b0f0d000007538` models Serpina6 as a carrier with no `part_of` process, which is the same
  judgement. Mouse knockouts change adrenal gene expression (PMID:31570737, PMID:36112420), an indirect
  endocrine effect.
- NEW `GO:0009914` hormone transport. Comparator check (QuickGO, exact term, 2026-11-26): the other
  hormone-carrier serpin SERPINA7 (TBG) carries the child term `GO:0070327` thyroid hormone transport by
  IMP (39 human annotations to that term, so the query can return positives); vitamin D-binding protein
  GC carries `GO:0051180` vitamin transport. CBG does the carrying itself, so the participation test is
  met. GO has no glucocorticoid- or steroid-hormone-transport term; proposed.

Curation gaps (not knowledge gaps): GO lacks "steroid hormone carrier activity" and "steroid hormone
transport"; human SERPINA6 lacks any BP annotation other than the Reactome row removed above.

## OpenScientist

- `just deep-research-openscientist human SERPINA6` — general gene research.
- `just gene-hypothesis-research openscientist human SERPINA6 --annotation-index 1 --as-function-hypothesis`
  — neutral test of "SERPINA6 has serine-type endopeptidase inhibitor activity (GO:0004867)".
- `just gene-hypothesis-research openscientist human SERPINA6 --focus-type free-text --slug helix-d-allosteric-variant-cluster ...`
  — do H14/H89/L93 variants act through helix D?

All three were first launched on 2026-11-26 and lost when the container restarted (empty output
directories); relaunched 2026-11-28. The local `SERPINA6-bioinformatics/RESULTS.md` was not given to
OpenScientist.

### 2026-11-28: deep-research report received

`SERPINA6-deep-research-openscientist.md` (with `_artifacts/`) completed in about 25 minutes. It was
written without sight of the local analysis and agrees with it on every point that matters for the
review: non-inhibitory serpin carrier, S-to-R transition repurposed for release, liver-made and
extracellular, Lyon on the pocket wall and Leuven on helix D.
`[file:human/SERPINA6/SERPINA6-deep-research-openscientist.md "there is no protease inhibition: the loop is a substrate that is consumed, not a bait that forms the covalent acyl-enzyme complex defining an inhibitory serpin"]`
Differences checked:

- Its contact distances are shorter than mine (Trp371 1.85 A versus 2.87 A; Asp367 4.08 A versus 4.59 A).
  The 4C49 cortisol model carries hydrogen atoms; recomputing with hydrogens reproduces 1.85 and 4.08 A.
  My analysis uses heavy atoms only, so the two agree.
- Its pocket (4.5 A cutoff, 15 residues) adds Phe26 and Asp367 to my 13 (4.0 A cutoff).
- New to me and not independently verified: cleaved and intact CBG have the same half-life in rabbit
  (PMID:25636722); the elastase P1 and P1' residues are poorly conserved in rodents, so the human cleavage
  site should not be assumed for mouse models; the reported membrane CBG receptor has two affinities
  8700-fold apart and no molecular identity. None of these changes an annotation decision.

### 2026-11-28: hypothesis report received (helix D variant cluster)

`SERPINA6-hypotheses/helix-d-allosteric-variant-cluster/openscientist.md`. Verdict: partially supported.
It confirms, from the crystal structures and without sight of my analysis, that mature His14, His89 and
Leu93 do not contact the steroid (9-15 A away) and that they touch each other. It rejects the stronger
claim I had floated, that one shared helix D mechanism explains all of these variants:
`[file:human/SERPINA6/SERPINA6-hypotheses/helix-d-allosteric-variant-cluster/openscientist.md "The claim that one shared allosteric mechanism centred on helix D explains all four substitutions is not supported as written."]`

Its three grounds, and what I checked:

- H14R is a capacity defect, H14Q and H89Y affinity defects (PMID:25322275 abstract says the same), so the
  phenotypes differ in kind.
- Tyrosine, the residue H89Y introduces, is the wild-type residue in rodent CBG. Checked in my own
  alignment after adding the count to `02_analyze.py`: rat and mouse CBG have Tyr at this position and so
  do 10 of 73 orthologues. A human-specific context must therefore be needed for H89Y to lower affinity.
  `[file:human/SERPINA6/SERPINA6-bioinformatics/RESULTS.md "CBG H89Y: 10"]`
- Only His89 and Leu93 are in helix D; His14 is in the N-terminal segment that packs against it and that
  carries steroid contacts Ala18, Ser19 and Val22. The report proposes that the coupling runs through this
  N-terminal segment and the Phe369-Thr370 strand next to His368 and Trp371, not through the helix D
  connecting loop.

Consequence for the review: the variant table above keeps "contact cluster on helix D" as a description of
position, but the class is now "second-shell packing node, mechanism unresolved", not "allosteric via
helix D". The knowledge gap in the review YAML was reworded accordingly. One difference left open: the
report finds the cluster partly solvent-exposed in the cleaved crystal structures, whereas the AlphaFold
(native-like) model buries His14 (RSA 0.03); the two describe different conformational states.

### 2026-11-28: hypothesis report received (GO:0004867 as a neutral function hypothesis)

`SERPINA6-hypotheses/function-hypothesis-go-0004867/openscientist.md`. The job was given only the term,
its IBA evidence and the reference, with no review decision. Verdict: over-annotated, refuted at the level
of direct activity, which matches the REMOVE on the three rows.
`[file:human/SERPINA6/SERPINA6-hypotheses/function-hypothesis-go-0004867/openscientist.md "It does not inhibit serine proteases. CBG is the substrate in every protease experiment published on it"]`

- It surfaced a primary source my search missed, which I fetched and read:
  [PMID:3143075 "Apparently evolution has completely adapted the serpin structure for its new role in these proteins as a transport agent, as there is no evidence of any retained protease inhibitory activity."]
  This is now cited on the removed rows.
- It agrees with the local analysis on the register (P1 = mature Thr349-Ser350; elastase cuts P6-P5).
- Its caveat is fair and is adopted: the refutation rests on an explicit negative statement, the
  elastase experiment in which the enzyme stayed active (PMID:2370299) and the absence of any reported
  inhibition constant or covalent complex, not on a published kinetic assay of zero inhibition.
- Not re-computed here (leads for the family review): 36 of 38 reviewed human serpins carry GO:0004867 by
  IBA, including SERPINA7, AGT, SERPINB11, SERPINF1 and SERPINH1; the reactive-bond residue is conserved
  in only 12 of 22 SERPINA6 species. It also warns that rat CBG behaves differently (PMID:23300763), so
  the human result should not be transferred across species without checking.

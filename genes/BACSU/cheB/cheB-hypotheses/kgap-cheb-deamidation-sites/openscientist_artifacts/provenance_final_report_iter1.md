# BACSU cheB (Q05522): can the native receptor deamidation sites be named?

Hypothesis slug: `kgap-cheb-deamidation-sites`. Source: `genes/BACSU/cheB/cheB-ai-review.yaml`, free-text focus.

## Executive judgment

**Unresolved, leaning over-annotated for CheB.** No native receptor deamidation
site can be assigned to *Bacillus subtilis* CheB. The sequence comparison the
hypothesis asked for does place McpB Gln371 in methylation helix 1 on a column
equivalent to a demonstrated *E. coli* deamidation site, so the candidate is not
refuted. It cannot be promoted either, for three reasons that are separable.

1. The alignment register is ambiguous by two heptads. One method puts McpB Q371
   at the Tar Q295 column, another puts it at the Tar Q309 column. Both columns
   happen to be demonstrated deamidation sites, so the conclusion "equivalent to
   a demonstrated site" survives, but the specific equivalence does not.
2. The method fails its own internal negative control. The single *B. subtilis*
   deamidation site that has actually been demonstrated, McpC Gln609, is not
   recovered by the same anchored alignment, which maps the Tar MH2 site to McpC
   Glu617 instead.
3. A demonstrated competing enzyme exists in the same cell. CheD, not CheB, is
   the enzyme shown to deamidate *B. subtilis* chemoreceptors (PMID 12011078),
   and CheD is the enzyme credited with the one named site, McpC Q609
   (PMID 22931217). The CheB deamidase attribution in this organism is explicitly
   described in the primary literature as a carry-over from *E. coli*.

The one part of the hypothesis that is cleanly answered is the maturation
question. *B. subtilis* McpB is made with glutamines at two of its four
modification positions, Gln371 and Gln595 (PMID 10825179), and at least one of
them is methylated in vivo. Deamidation is therefore an obligatory step for
McpB, not a dispensable one. That raises the stakes on the enzyme assignment
rather than settling it.

Per the hypothesis instruction: **no GO annotation for deamidation should be
proposed for Q05522, because no site can be named.**

## What a demonstrated site looks like

CheB-dependent deamidation has been shown directly only in *Escherichia coli*,
on Tsr (MCPI), Tar (MCPII) and Trg.

Kehry, Bond, Hunkapiller and Dahlquist (PMID 6304723) sequenced radiolabelled
tryptic peptides K1 and R1 from Tsr, found that a site in K1 cannot accept
methyl groups in the absence of the CheB-dependent modification, and correlated
the peptide sequence with the *tsr* gene sequence to conclude the modification
is "the enzymatic deamidation of glutamine to methyl-accepting glutamic acid".
Kehry, Engstrom, Dahlquist and Hazelbauer (PMID 6300110) found at least three
CheB-dependent sites on Trg and measured the pKa of the newly created group at
2.2-5.8, consistent with a free carboxylate. Barnakov, Barnakova and Hazelbauer
(PMID 10485883) used deamidation of intact versus pentapeptide-truncated Tar as
a quantitative in vitro assay.

I verified the residue identities directly from UniProt rather than taking them
from review text:

| Receptor | Site 1 | Site 2 | Site 3 | Site 4 |
|---|---|---|---|---|
| Tar, *E. coli* P07017 | **Q295** | E302 | **Q309** | E491 |
| Tar, *S. typhimurium* P02941 | **Q295** | E302 | **Q309** | E491 |
| Tsr, *E. coli* P02942 | **Q297** | E304 | **Q311** | E493 |

Sites 1 and 3 are encoded as glutamine; sites 2 and 4 as glutamate. The
equivalence that the hypothesis identifies as the heart of the inference holds
in the reference organism: the deamidated glutamine occupies the same heptad
column that carries a methyl-accepting glutamate in the paralogue. Tar Q295 and
Tsr Q297 are in the same column; Tar E302 and Tsr E304 are in the same column.

One feature of the *E. coli* system does not transfer. CheB docks on the
C-terminal NWETF pentapeptide, and removing it cripples deamidation
(PMID 10485883). The *B. subtilis* receptors have no such pentapeptide. I
checked the C-termini: McpA `...ELRDMTKRFKIE`, McpB `...ELRDLTKQFKIE`,
McpC `...QELMNTIAKFTL`, TlpA `...LRDLTKQFKVDK`, TlpB `...LQDITKKFKIES`,
TlpC `...SQFKMINQAENG`. None carries NWETF or NWESF.

## Mapping onto the B. subtilis receptors

Full-length alignment is not usable: global Needleman-Wunsch of Tar against McpB
gives 12.8 percent identity and places Tar Q295 at McpB Ala431, which is plainly
wrong. I anchored instead on the conserved signalling-domain tip motif
`G[FLIV][ASG]VVA[DEG]EVR`, which occurs exactly once per receptor:
Tar 393, Tsr 395, McpA 510, McpB 511, McpC 505, TlpA 510, TlpB 510, TlpC 416.
Methylation helix 1 is N-terminal to this anchor and methylation helix 2 is
C-terminal to it, so topology, and not sequence similarity alone, assigns each
site to a helix. On that basis McpB Q371 is in MH1 and McpB Q595, E630 and E637
are all in MH2; Tar Q295/E302/Q309 are in MH1 and Tar E491 in MH2.

Two register tests then disagree.

| Test | Register | Tar Q295 maps to | Tar E302 maps to | Tar Q309 maps to | Margin over next register |
|---|---|---|---|---|---|
| Joint ungapped scan of Tar 280-330 | offset +76 | McpB **Q371** | McpB **Q378** | McpB H385 | 42 vs 38 (4 units) |
| 25-residue window on Tar Q309 | offset +62 | McpB A357 | McpB N364 | McpB **Q371** | 37 vs 26 (11 units) |
| 25-residue window on Tsr Q311 | offset +62 | - | - | McpB **Q371** | 40 vs 28 (12 units) |

The two-heptad discrepancy is exactly the failure mode the hypothesis warned
about. The second register is driven by a strong short motif: Tar 304-313
`AASMEQLTAT` versus McpB 366-375 `AASSEQLTAS`, 8 of 10 identical with the
glutamine in register. The first register has a margin of only 4 BLOSUM units,
which is not decisive.

**Answer to the one check that would promote or demote the candidate:** McpB
Gln371 falls at a column equivalent to a demonstrated deamidation site under
*both* registers, because both candidate columns (Tar Q295, Tar Q309) are
demonstrated CheB-dependent deamidation sites. The candidate is therefore not
demoted. It is also not promoted to a named site, because the equivalence cannot
be stated as a specific column and because of the control failure below.

Other receptors at the primary register:

| Receptor | At Tar Q295 column | At Tar E302 column | At Tar Q309 column |
|---|---|---|---|
| McpA (P39214) | **Q377** | H384 | **Q391** |
| McpB (P39215) | **Q371** | **Q378** | H385 |
| McpC (P54576) | E393 | T400 | S407 |
| TlpA (P39216) | E370 | **Q377** | H384 |
| TlpB (P39217) | E370 | **Q377** | H384 |
| TlpC (P39209) | N311 | **Q318** | D325 |

MH2 registers are weaker: best-versus-next margins of 3 to 15 BLOSUM units, and
the Tar E491 column maps to McpB Asp623, McpA Glu615, McpC Glu617, TlpA Asp622,
TlpB Asp622, TlpC Glu542. None of McpB's three MH2 modification sites (Q595,
E630, E637) lands on the mapped Tar E491 column, which indicates an insertion or
a different site complement in the *B. subtilis* MH2.

### Negative control for the method

McpC Gln609 is the only *B. subtilis* receptor glutamine for which deamidation
has been demonstrated (PMID 22931217). The same anchored procedure maps the Tar
MH2 site E491 to McpC Glu617, eight residues away, and places no *B. subtilis*
glutamine on that column. A procedure that cannot recover the one known answer
should not be trusted to name new sites. This is the strongest single reason to
leave the McpB Q371 candidacy where it is.

### Base-rate caution

Glutamine is common in these helices. In the McpB MH1 window (tip-130 to tip-70)
7 of 60 residues are Gln; in the MH2 window 8 of 90. A single mapped column lands
on a glutamine by chance roughly 9-12 percent of the time, so a column hit alone
is weak evidence.

## Is deamidation an essential maturation step in this organism?

Yes for McpB, and the answer comes from the sequence plus one mutagenesis result.
Zimmer, Tiu, Collins and Ordal (PMID 10825179) name the four McpB modification
sites as Gln371, Gln595, Glu630 and Glu637. I confirmed these residue identities
in P39215. Because glutamine cannot accept a methyl ester, Q371 and Q595 must be
converted to glutamate before CheR can act. That conversion demonstrably happens:
McpB(E630D,E637D), which retains only the two glutamine sites, still released
methanol on asparagine addition.

So *B. subtilis* McpB is in the same situation as *E. coli* Tar and Tsr: made
with glutamines at some modification positions, requiring deamidation before
methylation. This is an essential maturation step. McpA, by contrast, has no
glutamine at positions 371 or 595, and McpC carries its demonstrated glutamine
at 609 in MH2.

## Which enzyme does it

This is where the hypothesis's framing needs revision. *B. subtilis* has a
dedicated deamidase that *E. coli* lacks.

Kristich and Ordal (PMID 12011078) showed that CheD "catalyzes amide hydrolysis
of specific glutaminyl side chains of the *B. subtilis* chemoreceptor McpA" and
presented evidence for McpB and McpC as well, stating plainly that "previously,
deamidation of *B. subtilis* receptors was thought to be catalyzed by the CheB
methylesterase, as is the case for *E. coli* receptors."

Glekas et al. (PMID 22931217) narrowed this and created a conflict: "CheD
deamidates Q609 in McpC and does not deamidate McpB." They showed mcpC-Q609E
restores chemotaxis in a *cheD* background, that McpC-Q609E activates CheA much
more than unmodified McpC, and that CheD binds McpC-Q609E better.

UniProt reflects this: P40404 is annotated "Chemoreceptor glutamine deamidase
CheD (EC 3.5.1.44)", the same EC number carried on Q05522 (CheB).

The net position for McpB Q371 and Q595 is that they are orphaned. CheD is
reported not to deamidate McpB; CheB has never been assayed for deamidase
activity on any *B. subtilis* receptor in any paper I could retrieve. CheB
remains a candidate by elimination, which is not evidence.

## Can a catalytic mutant separate the two activities?

No, not with the allele that exists. West, Martinez-Hackert and Stock
(PMID 7608974) solved the Salmonella CheB catalytic domain and identified a
single active site containing Ser164, His190 and Asp286, describing the enzyme
as hydrolysing "receptor glutamine or methylglutamate side-chains to glutamic
acid". Both reactions run through one serine nucleophile.

I located the nucleophile elbow by motif rather than by global alignment, because
*E. coli* and *B. subtilis* CheB share only 17 percent identity full length. Each
protein has exactly one GxSxGG: *E. coli* CheB G162-A-**S164**-T-G-G and
*B. subtilis* CheB G171-T-**S173**-T-G-G. So *B. subtilis* Ser173 is the
structural equivalent of *E. coli* Ser164.

Bunn and Ordal (PMID 14731274) used cheB(S173C) and saw no methanol release on
attractant addition or removal. That is a nucleophile knockout, so it removes
esterase and any deamidase activity together. It carries no information about the
deamidation contribution. No separation-of-function CheB allele has been reported
for this organism.

## GO curation implications (leads requiring curator verification)

- **GO:0050568 protein-glutamine glutaminase activity** (or any deamidase MF term)
  on Q05522: do **not** promote. Retain only as an IEA/ISS-level inference with a
  clear statement that it is family-derived, or mark it non-core. No
  *B. subtilis* substrate residue can be named; the demonstrated deamidase in this
  organism is CheD (P40404); CheB's receptor docking determinant (NWETF) is absent
  from all six *B. subtilis* chemoreceptors. Adding an experimental or
  author-statement evidence code is not supported.
- **GO:0008984 protein-glutamate methylesterase activity** on Q05522: retain as
  core MF. This is independently supported in *B. subtilis* by methanol-release
  assays and by the cheB(S173C) active-site mutant (PMID 14731274).
- **GO:0006935 chemotaxis / GO:0000160 phosphorelay signal transduction system**:
  unaffected by this analysis.
- McpB Gln371 should be described in the review as a **candidate methylation site
  that must be deamidated before methylation, with the responsible enzyme
  unassigned**, citing PMID 10825179 for the site and PMID 22931217 for the
  statement that CheD does not deamidate McpB. It should not be described as a
  CheB deamidation site.
- Consider adding CheD (P40404) as the organism-specific alternative in any
  free-text that currently attributes receptor deamidation to CheB.

## Mechanistic scope

The immediate molecular activity under test is hydrolysis of a glutamine side
chain amide on a chemoreceptor helix, producing a glutamate that CheR can then
esterify. This is distinct from the demethylation reaction (hydrolysis of an
existing methyl ester), even though both are catalysed by the same serine in
*E. coli* CheB. Everything downstream, including kinase activation state, tumble
bias, methanol release kinetics and chemotactic efficiency, is a pathway
consequence and does not by itself identify which enzyme performed the
deamidation. The methanol-release assays used throughout the *B. subtilis*
literature report esterase output, not deamidase output, so they cannot be used
to infer deamidation directly.

## Conflicts and alternatives

- **Direct conflict between two primary papers.** PMID 12011078 reports CheD
  deamidates McpB; PMID 22931217 reports CheD does not deamidate McpB. Both are
  from the Ordal group. The 2012 result is site-resolved and functionally
  anchored, the 2002 result is described as "evidence" for McpB rather than a
  site assignment, so the 2012 statement is the stronger of the two, but the
  conflict is unresolved in the published record.
- **Database carry-over.** The *B. subtilis* CheB deamidase attribution is a
  carry-over from *E. coli*, and PMID 12011078 says so in those words. The
  EC 3.5.1.44 number on Q05522 is family-level, not substrate-level.
- **Organism-specific architecture.** *E. coli* has no CheD. The presence of a
  dedicated deamidase in *B. subtilis* is a reason to expect the *E. coli* labour
  division not to transfer, independent of any alignment.
- **Repeat-driven alignment artefact.** The methylation helices are heptad
  repeats. The two-heptad register discrepancy here is a concrete instance; a
  report that fixed one register without showing the alternative would have
  invented a specific site.
- **Missing docking determinant.** *E. coli* CheB deamidation depends on the
  NWETF pentapeptide. Its absence from all *B. subtilis* receptors removes the
  one mechanistic feature known to make CheB an efficient deamidase.

## Knowledge gaps

1. **No direct assay of B. subtilis CheB deamidase activity exists.** Checked:
   PubMed searches on CheB plus deamidation plus *Bacillus*, on CheD, on McpB
   methylation sites, and on the CheB catalytic domain. Matters because the entire
   deamidase attribution for Q05522 rests on family inference. Resolved by an in
   vitro assay of purified CheB (and phospho-CheB) against McpB bearing Q371 and
   Q595, read out by mass spectrometry or by the +1 Da / isoelectric shift.
2. **The enzyme that deamidates McpB Q371 and Q595 is unknown.** Checked:
   PMID 12011078 and PMID 22931217 disagree. Matters because deamidation is an
   obligatory maturation step for McpB. Resolved by comparing McpB modification
   state in wild-type, Δ*cheD*, Δ*cheB* and Δ*cheB* Δ*cheD* backgrounds by intact-
   mass or targeted peptide mass spectrometry.
3. **The MH1 register for McpB is not fixed.** Checked: two independent anchored
   alignment methods, disagreeing by two heptads. Matters because it determines
   whether Q371 is the site-1 or site-3 equivalent, which bears on whether CheD or
   CheB would be expected to act. Resolved by structure-based alignment of a
   predicted or experimental McpB cytoplasmic-domain model to the Tsr or
   *T. maritima* receptor structures (I did not run a structure comparison here;
   no *B. subtilis* chemoreceptor cytoplasmic-domain structure was retrieved).
4. **No separation-of-function CheB allele.** Checked: only cheB(S173C), a
   nucleophile mutant (PMID 14731274), combined with the single-active-site
   structure (PMID 7608974). Matters because the contribution of deamidation
   cannot be ranked against demethylation without one. Resolved by substrate-
   groove mutations that differentially affect amide versus ester hydrolysis,
   or by comparing cheB-null complemented with McpB Q371E/Q595E receptors.
5. **MH2 site complement of B. subtilis receptors.** Checked: the anchored
   alignment places none of McpB Q595/E630/E637 on the Tar E491 column, margins
   3-15 BLOSUM units. Matters because Q595 is the second obligatory deamidation
   site. Resolved by the same structure-based alignment as gap 3.

## Discriminating tests

1. **Mass spectrometry of McpB across enzyme deletions.** Express McpB as the sole
   receptor in wild-type, Δ*cheB*, Δ*cheD* and Δ*cheB* Δ*cheD*; measure the
   deamidation state of the Q371 and Q595 peptides. This is the single experiment
   that would either name a CheB site or close the question.
2. **In vitro deamidation with purified components.** Purified CheB, phospho-CheB
   and CheD against McpB cytoplasmic fragments carrying Q371/Q595, with McpC Q609
   as a positive control for CheD and Tar Q295/Q309 as a positive control for CheB.
3. **Genetic epistasis with pre-deamidated receptors.** If McpB Q371E,Q595E
   rescues chemotaxis in a Δ*cheD* Δ*cheB* background better than wild-type McpB
   does, deamidation is the limiting step and the responsible enzyme is whichever
   deletion the rescue bypasses.
4. **Structure-based alignment.** Superpose an AlphaFold or experimental model of
   the McpB cytoplasmic domain on the *E. coli* Tsr or *T. maritima* TM1143
   signalling domain and read the register off the structure instead of the
   sequence. This would settle gap 3 cheaply and is the analysis I would run next.
5. **Comparative genomics.** Test across Firmicutes whether receptors with
   glutamines at MH1 adaptation positions co-occur with *cheD* presence. If the
   glutamine complement tracks *cheD* and not *cheB*, the deamidase labour
   division in this clade is CheD's.

## Curation leads

Candidate references with exact snippets to verify:

- PMID 12011078: "Previously, deamidation of B. subtilis receptors was thought to
  be catalyzed by the CheB methylesterase, as is the case for E. coli receptors."
  Use to flag the CheB deamidase statement as a known carry-over.
- PMID 22931217: "The reason for the difference between the chemoreceptors is
  because CheD deamidates Q609 in McpC and does not deamidate McpB." Use to name
  the one demonstrated *B. subtilis* site and to show McpB is not a CheD substrate.
- PMID 10825179: "all combinations of putative methylation sites Gln(371),
  Gln(595), Glu(630), and Glu(637) were substituted with aspartate". Use to
  support "McpB is made with glutamines at two modification positions", and note
  the same abstract says the sites were assigned "based upon the Escherichia coli
  consensus sequence".
- PMID 6304723: "suggests that CheB-dependent modification of MCPI is the
  enzymatic deamidation of glutamine to methyl-accepting glutamic acid". Use as
  the primary demonstration, in *E. coli*.
- PMID 7608974: "The methylesterase active site is tentatively identified as a
  cleft at the C-terminal edge of the beta-sheet containing residues Ser164,
  His190 and Asp286." Use to justify that cheB(S173C) cannot separate activities.
- PMID 14731274: "no methanol release was observed for an active site point
  mutant, cheB(S173C)". Use for the same point.

Suggested action changes:

- Change any free text asserting that *B. subtilis* CheB deamidates chemoreceptors
  to state that the activity is inferred from the enzyme family, that CheD is the
  demonstrated receptor deamidase in this organism, and that no CheB substrate
  residue is known.
- Downgrade McpB Gln371 from "candidate CheB substrate" to "modification site
  requiring deamidation by an unassigned enzyme".
- Keep methylesterase as the core molecular function.

Suggested questions for the curator:

- Does the review currently cite PMID 12011078 or PMID 22931217? If not, both
  should be added, because they are the organism-specific evidence.
- Is EC 3.5.1.44 on Q05522 inherited from the UniProt family rule? If so, say so
  in the review.

## Limitations of this analysis

The alignments are my own anchored Needleman-Wunsch and Smith-Waterman
implementations with BLOSUM62 and affine gaps, run on UniProt sequences fetched
live; no HMM profile alignment (HMMER, Pfam) and no structure superposition was
run, because neither was available in the execution environment. The register
conclusions should be treated as provisional for that reason, and the control
failure on McpC Q609 means they should not be used to name sites. PubMed search
in this environment returned small result sets for several queries, so I may have
missed a paper; in particular I could not retrieve Terwilliger and Koshland's
Tar site-mapping work directly and relied on sequence verification of the
positions instead. Code and computed tables are in `provenance/`
(`evidence_matrix.csv`, `column_mapping_table.csv`) with three figures.

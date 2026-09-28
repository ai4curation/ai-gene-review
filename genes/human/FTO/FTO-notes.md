# FTO (human, Q9C0B1) — curation journal

Reviewer notes for `FTO-ai-review.yaml`. Provenance is inline as
`[PMID:xxxxx "<verbatim supporting text>"]`.

## 1. What the protein is

FTO is a nuclear (and, in some cell lines, partly cytoplasmic) Fe(II)/2-oxoglutarate-dependent
oxygenase of the AlkB superfamily. It was discovered through obesity GWAS and only afterwards
shown to be an enzyme: the founding paper demonstrated 2OG-dependent demethylation of a
methylated nucleobase in single-stranded DNA by the mouse orthologue
[PMID:17991826 "We find that recombinant murine Fto catalyzes the Fe(II)- and 2OG-dependent
demethylation of 3-methylthymine in single-stranded DNA, with concomitant production of
succinate, formaldehyde, and carbon dioxide."] and its nuclear localization
[PMID:17991826 "Consistent with a potential role in nucleic acid demethylation, Fto localizes to
the nucleus in transfected cells."].

The fold is AlkB-like with an extra C-terminal domain and a loop that excludes duplex nucleic
acids [PMID:20376003 "FTO comprises an amino-terminal AlkB-like domain and a carboxy-terminal
domain with a novel fold."]. That loop is the structural reason FTO works on single-stranded
substrates only [PMID:20376003 "Structural comparison shows that this loop selectively competes
with the unmethylated strand of the DNA duplex for binding to FTO, suggesting that it has an
important role in FTO selection against double-stranded nucleic acids."].

Loss of catalytic activity in humans is not a mild phenotype: the homozygous R316Q variant causes
a lethal recessive polymalformation syndrome
[PMID:19559399 "Here we show that a R316Q mutation, inactivating FTO enzymatic activity, is
responsible for an autosomal-recessive lethal syndrome."], establishing that the enzymatic
function matters in vivo [PMID:19559399 "These findings indicate that FTO is essential for normal
development of the central nervous and cardiovascular systems in human"].

## 2. THE LOCUS IS NOT THE PROTEIN (important for the BP annotations)

The FTO *locus* carries the strongest common-variant association with BMI, but the causal
mechanism runs through neighbouring genes, not through FTO protein. Claussnitzer et al. showed
the causal SNP disrupts an ARID5B motif in FTO intron 1 and derepresses a preadipocyte enhancer
acting at 1.2 Mb on IRX3/IRX5
[PMID:26287746 "The rs1421085 T-to-C single-nucleotide variant disrupts a conserved motif for the
ARID5B repressor, which leads to derepression of a potent preadipocyte enhancer and a doubling of
IRX3 and IRX5 expression during early adipocyte differentiation."], with the phenotype being a
beige-to-white adipocyte shift
[PMID:26287746 "This results in a cell-autonomous developmental shift from energy-dissipating
beige (brite) adipocytes to energy-storing white adipocytes, with a reduction in mitochondrial
thermogenesis by a factor of 5, as well as an increase in lipid storage."]. Their own conclusion
names IRX3/IRX5, not FTO
[PMID:26287746 "Our results point to a pathway for adipocyte thermogenesis regulation involving
ARID5B, rs1421085, IRX3, and IRX5, which, when manipulated, had pronounced pro-obesity and
anti-obesity effects."]. UniProt records the same caveat verbatim in its OBESITY disease comment
("It is unclear whether variations associated with obesity directly affect FTO function or alter
the expression of adjacent genes such as IRX3, rather than FTO itself").

**Curation consequence.** GOA carries two IMP annotations to FTO sourced from PMID:26287746:
`GO:0010883 regulation of lipid storage` and `GO:0090335 regulation of brown fat cell
differentiation`. Neither is a perturbation of the FTO *protein*; both are enhancer/IRX3/IRX5
experiments at the FTO *locus*. I did not use REMOVE (project rule: do not overrule an
experimental annotation whose full text I have not read — here I did read the full text, but the
conservative action is still available and mouse Fto protein data provide independent, weaker
support for an adiposity role). I set `GO:0090335` to MARK_AS_OVER_ANNOTATED and kept
`GO:0010883` as non-core (it also has IBA and mouse-orthology IEA support), recording the
locus/protein distinction in both `reason` fields. If a GO curator revisits this, the cleanest fix
is to re-home the PMID:26287746 annotations to IRX3 and IRX5.

## 3. Dispute layer 1 — chemistry: hydroxylase or demethylase?

Kaur et al. 2025 (NAR) compared FTO with ALKBH5, ALKBH2/3 and bacterial AlkB by MS and real-time
NMR. They open by noting the field is not settled
[PMID:40874592 "While ALKBH5 has consistently been reported to catalyse m6A demethylation, there
are conflicting reports concerning the FTO products."] and conclude that the enzymatic product of
FTO is the hemiaminal, N6-hydroxymethyladenosine (hm6A), not adenosine
[PMID:40874592 "The results imply that, at least in isolated form, FTO preferentially acts as a
hydroxylase, producing a hemiaminal product, rather than a demethylase, distinguishing it from
ALKBH5."]. Demethylation happens, but off-enzyme and slowly
[PMID:40874592 "The nascent hemiaminal product undergoes relatively slow non-enzyme catalysed
fragmentation giving adenosine/formaldehyde."]. Their full-text summary is unambiguous
[PMID:40874592 "The combined results clearly demonstrate that, in contrast to the other tested
oxygenases, isolated FTO preferentially acts as a hydroxylase rather than a demethylase,
highlighting a need for further investigations into the biological roles of hm6A and hm6Am."].
They also flag that standard mapping/quantification workflows may destroy the real product
[PMID:40874592 "Some reported methods used to analyse FTO products/mRNA modification might not
preserve hm6A/hm6Am adducts and other hemiaminal-type covalent modifications that are relatively
unstable in aqueous environments"].

How much should this move GO? My reading:

- It does **not** invalidate `GO:0016706 2-oxoglutarate-dependent dioxygenase activity`. That term
  states the cofactor chemistry only and is the one MF assertion on this gene that no side of
  either dispute contests. I kept it as an accepted, dispute-proof statement of catalytic
  identity.
- It **does** strain the definitions of `GO:0035515 oxidative RNA demethylase activity`
  ("Catalysis of the removal of a methyl group...") and `GO:1990931 mRNA N6-methyladenosine
  dioxygenase activity` ("...releases oxidized methyl group on N6-methyladenosine as
  formaldehyde"), because under Kaur's model neither the methyl removal nor the formaldehyde
  release is enzyme-catalysed. But the caveat "at least in isolated form" is load-bearing: in
  cells the measured endpoint is loss of the methyl mark, seen repeatedly by independent groups
  [PMID:22002720 "FTO knockdown with siRNA led to increased amounts of m(6)A in mRNA, whereas
  overexpression of FTO resulted in decreased amounts of m(6)A in human cells."]. I therefore did
  not downgrade the demethylase terms on chemistry grounds; I recorded the mechanism dispute in
  `reason` and proposed a new MF term for the hydroxylase (hm6A-forming) activity so the
  distinction can be curated if it is confirmed in cells.

There is no GO term for m6A/m6Am *hydroxylase* activity and none for N6-hydroxymethyladenosine
formation (checked via QuickGO search, 2026-09). Proposed in `proposed_new_terms`.

## 4. Dispute layer 2 — substrate: mRNA m6A, or snRNA/mRNA-cap m6Am and tRNA m1A?

**Solid, uncontested activities.**

- snRNA / U6: [PMID:30197295 "We further identified additional RNA substrates of FTO, including
  m1A in tRNA, m6A in U6 RNA, internal and cap m6Am in snRNAs."]
- tRNA m1A, with a striking magnitude contrast against mRNA marks
  [PMID:30197295 "Interestingly, the m1A level in tRNA is dramatically affected by FTO-mediated
  demethylation in comparison to m6A and cap m6Am in polyadenylated RNAs in Fto knockout mouse
  cells and tissues."] and a functional consequence
  [PMID:30197295 "We also show that FTO can directly repress translation by catalyzing m1A tRNA
  demethylation."]
- 5' cap m6Am: [PMID:28002401 "Moreover, we find that m6Am is selectively demethylated by fat mass
  and obesity-associated protein (FTO). FTO preferentially demethylates m6Am rather than
  N6-methyladenosine (m6A), and reduces the stability of m6Am mRNAs."]
- The Jaffrey lab's own summary of its prior work
  [PMID:41279954 "We found that FTO primarily demethylates m6Am in snRNAs, with much more subtle
  activity towards m6Am in mRNA"]
- Ancestral AlkB-type ssDNA/ssRNA alkylation-lesion activity, in vitro
  [PMID:18775698 "We demonstrate here the oxidative demethylation of 3-methylthymine (3-meT) in
  single-stranded DNA (ssDNA) and 3-methyluracil (3-meU) in single-stranded RNA (ssRNA) by
  recombinant human FTO protein in vitro."], strictly single-stranded
  [PMID:18775698 "They showed negligible activities against 3-meT in double-stranded DNA
  (dsDNA)."]. UniProt flags in vivo relevance as "unsure"; I kept the DNA/RNA-repair terms but as
  non-core.

**The contested claim: internal mRNA m6A as a physiological substrate.**

The classic support is real in vitro activity plus cellular m6A dot-blot/LC-MS changes
[PMID:22002720 "We report here that fat mass and obesity-associated protein (FTO) has efficient
oxidative demethylation activity targeting the abundant N6-methyladenosine (m(6)A) residues in
RNA in vitro."] and nuclear-speckle colocalization
[PMID:22002720 "We further show the partial colocalization of FTO with nuclear speckles, which
supports the notion that m(6)A in nuclear RNA is a major physiological substrate of FTO."].
Additional experimental hooks: heat-shock 5'UTR m6A protection
[PMID:26458103 "Upon heat shock stress, the nuclear YTHDF2 preserves 5'UTR methylation of
stress-induced transcripts by limiting the m(6)A 'eraser' FTO from demethylation."]; inhibitor
chemistry premised on m6A demethylation
[PMID:25452335 "Here, we have identified meclofenamic acid (MA) as a highly selective inhibitor of
FTO."]; and structure-guided probes
[PMID:26457839 "Here, we identified that fluorescein derivatives can selectively inhibit FTO
demethylation, and the mechanisms behind these activities were elucidated after we determined the
X-ray crystal structures of FTO/fluorescein and FTO/5-aminofluorescein."].

The counter-evidence is Nicholson et al. 2025, **a bioRxiv preprint (not peer reviewed)**. Using
direct nanopore RNA sequencing — quantitative and single-nucleotide, unlike MeRIP — they report
[PMID:41279954 "We find that the stoichiometry of m6A sites throughout the transcriptome and
especially at MYC-specific sites are unaffected despite depletion of FTO activity by knockout,
knockdown, or pharmacologic inhibition."], while the same cells show the expected snRNA m6Am
response [PMID:41279954 "All measured snRNA-associated m6Am sites exhibited large increases in
stoichiometry upon FTO depletion"] — i.e. an internal positive control that FTO really was
depleted. Their methodological objection to the AML literature is specific
[PMID:41279954 "However, the evidence that supports the idea that FTO demethylates m6A in AML
relies on methods that are non-quantitative and unable to reveal m6A stoichiometry changes before
or after FTO depletion."] and their conclusion is a call to reinvestigate rather than a
retraction [PMID:41279954 "Overall, our findings do not support an 'm6A eraser' role for FTO in
AML cell lines under the conditions tested, and they suggest that the reported demethylation
functions of FTO on m6A should be reinvestigated using quantitative m6A mapping methods."].
They further report the FTO inhibitor FB23-2 is cytotoxic in FTO-null cells, which if it holds
undercuts a chunk of the pharmacological argument.

Against that, the m6A-eraser model remains the working hypothesis of an active drug-discovery
literature published the same year: a structure-based dual-competitive inhibitor
[PMID:41190354 "FTO is overexpressed in AML, promoting pathogenesis through c-Myc upregulation."],
whose prodrug "suppressed AML cell viability, reduced m6A levels, downregulated c-Myc and CEBPA,
and upregulated ASB2 and RARA"; and a degrader
[PMID:40815637 "We confirmed that FTO degradation increases m6A modifications on mRNAs associated
with ribosome biogenesis, promoting their YTHDF2-mediated decay."]. Note that the degrader paper
is orthogonal to the inhibitor-specificity objection (degradation, not active-site occupancy),
which makes it the stronger of the two for the pro-m6A side — though it still measures m6A by
antibody-dependent methods.

**How much should a preprint move a curation call? — my explicit position.**

A preprint should not by itself flip an annotation supported by multiple independent experimental
records, and I did not use REMOVE anywhere on the strength of PMID:41279954. But "not decisive"
is not "not admissible", and three features make this one weigh more than a typical preprint:

1. It is *methodologically orthogonal*, not a failed replication. Nanopore direct-RNA
   stoichiometry does not share MeRIP's principal failure mode (peak-height variability), which
   is exactly what is being challenged.
2. It carries an internal positive control — the snRNA m6Am increase — that independently
   confirms FTO activity was abolished. A null result with a working positive control is much
   stronger than a bare null.
3. It converges with pre-existing, peer-reviewed observations from the same and other labs that
   FTO's preferred cellular substrate is m6Am rather than m6A (PMID:28002401; PMID:30197295's
   magnitude contrast; PMID:40162895's quantitative m6Am landscape), and with a peer-reviewed
   chemistry paper arriving from an unrelated direction (PMID:40874592).

The appropriate response is therefore **demotion, not deletion**: `GO:1990931` is kept on the gene
(the in vitro activity is not in doubt) but marked non-core, with the dispute written into
`reason`; `GO:1990984 tRNA demethylase activity`, the snRNA role, and the generic
`GO:0035515 oxidative RNA demethylase activity` carry the core function. GOA already hedges the
substrate question by carrying both `GO:1990931` (mRNA) and `GO:1990984` (tRNA); this review makes
that hedge explicit rather than inventing it.

## 5. Localization

Nucleus is the dominant and best-supported compartment (EXP/IDA/ISS/IBA/IEA rows), with nuclear
speckles (PMID:22002720) and a genuine cytoplasmic pool that is cell-line dependent
[PMID:30197295 "Here we demonstrate that the cellular distribution of FTO is distinct among
different cell lines, affecting the access of FTO to different RNA substrates."]. All CC
annotations accepted; none of them is in dispute.

## 6. Term-level notes

- `GO:0016180 snRNA processing` (IDA, PMID:30197295) — the experiment shows snRNA *modification*
  (demethylation of m6A/m6Am in snRNAs), not conversion of a primary transcript to a mature
  snRNA. MODIFY to `GO:0040031 snRNA modification` (a child of GO:0016180) and
  `GO:0035513 oxidative RNA demethylation`.
- `GO:0044065 regulation of respiratory system process` (IEA from mouse orthology) — a distal
  organismal phenotype of an Fto-null animal, not something the protein does. MARK_AS_OVER_ANNOTATED.
- `GO:0008198 ferrous iron binding` (IDA, PMID:20376003) — correct cofactor binding, but it is the
  cofactor rather than the function; non-core. The cached record for PMID:20376003 is abstract
  only and the abstract does not state iron binding explicitly, so no `supporting_text` is quoted
  for this row; the assignment rests on the curator's reading of the structure paper.
- `GO:0035516 broad specificity oxidative DNA demethylase activity` — retained non-core. Note FTO
  is *not* fully "broad specificity" in the sense of the term definition: UniProt records no
  activity towards 1-methylguanine and none towards double-stranded DNA.

## 7. Open questions carried into `suggested_questions`

1. Is hm6A (or hm6Am) detectable in cellular RNA, and is it the physiological FTO product?
2. Does any quantitative, antibody-free method detect FTO-dependent internal mRNA m6A changes in
   any cell type?
3. If FTO inhibitors/degraders kill AML cells largely FTO-independently or via snRNA m6Am rather
   than mRNA m6A, what is the actual target engagement?
4. Should GO split m6Am (cap and snRNA) demethylase activity from mRNA m6A dioxygenase activity?

## 8. Status

Validated with `uv run --no-dev ai-gene-review validate --verbose --terms
genes/human/FTO/FTO-ai-review.yaml`. All PENDING actions replaced; `status: COMPLETE`.

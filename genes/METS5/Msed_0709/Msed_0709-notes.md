# Msed_0709 (A4YEN2, MCR_METS5) — curation notes

Metallosphaera sedula DSM 5348; malonyl-CoA/succinyl-CoA reductase (NADP+), EC 1.2.1.75
(also EC 1.2.1.76 activity). ARCHAEA project gene.

**Provenance note:** automated deep-research providers (falcon, openai) were unavailable
in this session (API authentication failures). No `-deep-research-*.md` file was created.
Literature research was done manually via NCBI E-utilities, the cached publications, and
UniProt REST. All PMIDs below were verified by E-utilities esummary and cached with
`just fetch-pmid`.

## Identity and activity

- Partially purified from M. sedula; gene identified through the S. tokodaii ortholog.
  [PMID:17041055 "Extracts of Metallosphaera sedula contained NADPH-specific malonyl-CoA reductase activity that was 10-fold up-regulated under autotrophic growth conditions."]
- Reaction: [PMID:17041055 "The enzyme catalyzes the following reaction: malonyl-CoA + NADPH + H+ --> malonate-semialdehyde + CoA + NADP+."]
- Cofactor specificity: [PMID:17041055 "The enzyme was specific for NADPH (Km = 25 microM) and malonyl-CoA (Km = 40 microM)."]
  (These kinetics are for the recombinant S. tokodaii enzyme.) No NAD binding/use is reported.
- Thiol/cysteine mechanism: [PMID:17041055 "Its activity was stimulated by Mg2+ and thiols and inactivated by thiol-blocking agents, suggesting the existence of a cysteine adduct in the course of the catalytic cycle."]
- The enzyme is also the succinyl-CoA reductase of the cycle (promiscuous):
  [PMID:19684143 "Interestingly, succinyl-CoA reductase turned out to be identical to malonyl-CoA reductase."]
  The succinyl-CoA reductase partially purified from autotrophic M. sedula was identified
  by peptide mass fingerprinting as Msed_0709:
  [PMID:19684143 "The enzyme preparation catalyzed malonyl-CoA and succinyl-CoA reduction with NADPH at the same rate"]
  [PMID:19684143 "These data showed that malonyl-CoA reductase is a promiscuous enzyme and acts nearly equally well with malonyl-CoA and succinyl-CoA."]
  [PMID:19684143 "In our previous study of malonyl-CoA reductase ( 1 ), the ability to reduce succinyl-CoA efficiently was erroneously overlooked."]
- Structure (S. tokodaii ortholog): homotetramer; NADP+ and CoA occupy the same bispecific
  site in succession. [PMID:23325803 "MCR is a homotetramer."]
  [PMID:23325803 "Structural analysis revealed an unexpected reaction cycle in which NADP + and CoA successively occupy identical binding sites."]
  Covalent acyl-cysteine (thioester) intermediate by analogy with the ASD Cys-aspartyl adduct.

## Pathway

- 3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) CO2-fixation cycle of autotrophic
  Sulfolobales. [PMID:18079405 "We discovered that an autotrophic member of the archaeal order Sulfolobales, Metallosphaera sedula, fixed CO2 with acetyl-coenzyme A (acetyl-CoA)/propionyl-CoA carboxylase as the key carboxylating enzyme."]
- MCR catalyses two reductive steps: malonyl-CoA -> malonate semialdehyde (first half) and
  succinyl-CoA -> succinate semialdehyde (second half, regenerating acetyl-CoA).
  [PMID:23325803 "Yet, the archaeal enzyme catalyzes also the reduction of succinyl-CoA onwards in the autotrophic cycle ( 10 ), which is required for regeneration of the starting molecule acetyl-CoA"]
- Heterologous use: Msed_0709 ("E2") was one of five M. sedula genes expressed in
  Pyrococcus furiosus to make 3-hydroxypropionate from CO2 + H2.
  [PMID:23530213 "E2 (malonyl/succinyl-CoA reductase, Msed_0709)"]
- MCR is unrelated to the bifunctional Chloroflexus MCR (convergent evolution).
  [PMID:17041055 "It does not exhibit any significant similarity with malonyl-CoA reductase from Chloroflexus aurantiacus."]

## Evolution: ASD paralog, not ASD

- [PMID:17041055 "Malonyl-CoA reductase has 38% amino acid sequence identity to aspartate-semialdehyde dehydrogenase, suggesting a common ancestor for both proteins."]
- [PMID:23325803 "The two paralogous MCR and ASD enzymes show ∼40% amino acid sequence identity in the same organism, and their genes mcr and asd have different chromosomal locations."]
- [PMID:23325803 "The mcr gene occurs only in autotrophic Sulfolobales underlining its role in the carbon fixation cycle and its neighbor genes are generally not conserved among different species."]
- [PMID:23325803 "The asd gene clusters together with threonine synthase, aspartokinase, and ornithine carbamoyltransferase, among other genes, which is in line with its role in the biosynthesis of amino acids of the aspartate family."]
- [PMID:19684143 "The gene for malonyl-CoA/succinyl-CoA reductase (Msed_0709) is located between genes encoding hypothetical proteins; no known gene of the 3-hydroxypropionate/4-hydroxybutyrate cycle is located nearby."]

### Own check of the M. sedula ASD paralog (UniProt REST, 2026-10-15)

Query `organism_id:399549 AND (ec:1.2.1.11 OR family:"aspartate-semialdehyde dehydrogenase")`
returned two proteins: A4YEN2 (Msed_0709, this gene) and A4YHF3 (Msed_1700, unreviewed).
Msed_1700 neighbours are Msed_1698 threonine synthase and Msed_1699 aspartokinase, i.e. the
asd context described in PMID:23325803. So Msed_1700 is the genuine ASD of M. sedula.

Correction (2026-10-15, from the Msed_1700 review): an earlier version of these notes said
that Msed_1700 carries NCBIfam TIGR00978 (asd_EA) and PRK08664 and that A4YEN2 lacks them.
That was wrong: the A4YEN2 UniProt record (Msed_0709-uniprot.txt) also lists TIGR00978 and
NF006416 (PRK08664.1). The paralogs are separated by CDD models instead: Msed_1700 matches the
archaeal/fungal ASD models cd18130 and cd02315, Msed_0709 the MCR models cd23940 and cd24150
(genes/METS5/Msed_1700/Msed_1700-bioinformatics/RESULTS.md).

Both paralogs fall in PANTHER PTHR46718:SF1 and share identical InterPro signatures, so they
receive identical GO sets (ASD activity, threonine biosynthesis, NAD binding, NADP binding,
dimerization). Conversely, ARBA (ARBA00067001) names the true ASD Msed_1700 "malonyl CoA
reductase (malonate semialdehyde-forming), EC 1.2.1.75". The neofunctionalized paralog and
the ancestral enzyme are not separated by either pipeline — a paralog over-annotation in both
directions. (Not cited as a supporting_text source because it is a live database query.)

## Annotation decisions (summary)

- GO:0004073 ASD activity (TreeGrafter) — REMOVE: paralog over-annotation; ASD role is
  Msed_1700's; substrate pocket remodelled around the missing ammonium group.
- GO:0009088 threonine biosynthesis (TreeGrafter) — REMOVE, same reason.
- GO:0008652 amino acid biosynthetic process (InterPro dimerization domain) — REMOVE.
- GO:0016620 aldehyde/oxo oxidoreductase, NAD(P) acceptor — ACCEPT (most specific existing
  term; GO has no term for EC 1.2.1.75 or EC 1.2.1.76 — checked ec2go and QuickGO search).
- GO:0050661 NADP binding — ACCEPT (NADPH-specific; NADP+ co-crystal structure of ortholog).
- GO:0051287 NAD binding — REMOVE: enzyme is NADPH-specific.
- GO:0046983 protein dimerization — KEEP_AS_NON_CORE (homotetramer).
- NEW GO:0015977 carbon fixation. GO:0043427 "carbon fixation by 3-hydroxypropionate cycle" is
  the Chloroflexus glyoxylate-forming cycle by definition, so it is not used; a 3HP/4HB-cycle
  term is proposed.
- Proposed new terms: malonyl-CoA reductase (NADP+) activity (EC 1.2.1.75, RHEA:26446);
  succinyl-CoA reductase (NADP+) activity (EC 1.2.1.76); carbon fixation by
  3-hydroxypropionate/4-hydroxybutyrate cycle.

# pppL (SP-STP) — Streptococcus pyogenes M1 GAS — curation notes

UniProt Q99YM9 (Q99YM9_STRP1, unreviewed), 246 aa, locus SPy_1626, gene `pppL`,
commonly called **SP-STP** in the literature. Co-transcribed with and immediately
downstream of the eukaryote-type Ser/Thr kinase SP-STK (SPy_1625).

**Provenance note:** no deep-research provider was available in this container
(no API keys), so `just deep-research` was not run and no `-deep-research-*.md`
file exists for this gene. Literature work here was done directly: the three
cited PMIDs were re-fetched with full text where PMC allowed
(`cache_publication(force=True)`, which upgraded PMID:21917918 and PMID:22262847
from abstract-only to full text; PMID:16487973 remains abstract-only, J Mol Biol
is not in PMC). The GONUTS wiki page for PMID:21917918 was checked for the
students' recorded evidence but `gowiki.tamu.edu` is currently serving only
"temporarily offline while we perform upgrades", so the CACAO-side reasoning
could not be inspected.

## Family and catalytic machinery

PPM/PP2C-type metal-dependent Ser/Thr phosphatase: InterPro IPR015655 (PP2C),
IPR001932, Pfam PF13672 (PP2C_2), PROSITE PS51746 (PPM_2 domain, residues
2–240), EC 3.1.3.16 [file:STRP1/pppL/pppL-uniprot.txt "DOMAIN 2..240"].
UniProt's PROSITE-ProRule cofactor note: "Binds 2 magnesium or manganese ions
per subunit." The family assignment is stated in the primary literature too
[PMID:21917918 "The latter possesses conserved I-XI motifs belonging to a
distinct class of metal-dependent PPM/PP2C-type serine/threonine phosphatase"].

Metal preference is experimental: [PMID:16487973 "Enzyme activities of SP-STK and
SP-STP primarily depended on Mn(2+)."] Mg(2+) is only a UniRule/ProRule
expectation for the fold, not tested for this protein.

## Catalysis and substrates

- Endogenous substrate work in the founding paper: the kinase/phosphatase couple
  acts on a histone-like protein (SP-HLP), and only threonine was reversibly
  modified [PMID:16487973 "The site on the substrate for reversible
  phosphorylation by these enzymes was found to be only the threonine residue."]
- Response regulators of two-component systems are the physiologically important
  substrates. SP-STK phosphorylates WalR on Thr, and SP-STP removes it
  [PMID:21917918 "SP-STK was able to phosphorylate SP-WalR ( Fig. 3 C )
  specifically at threonine residues, as is evident by TLC"; PMID:21917918 "The
  SP-STP was able to dephosphorylate the SP-STK-phosphorylated SP-WalR"].
- Same for CovR [PMID:21917918 "The specificity of SP-STK mediated CovR
  phosphorylation was confirmed by its subsequent dephosphorylation by the
  cognate SP-STP"; PMID:21917918 "the TLC revealed that SP-STK mediates
  phosphorylation of CovR specifically at its threonine residues"].
- Host substrate: histone H1. In vitro dephosphorylation of CDK1-phosphorylated
  H1 [PMID:22262847 "the purified SP-STP was able to dephosphorylate the H1∼P
  histone"] and loss of the Thr146 phospho-epitope in nuclei of treated cells
  [PMID:22262847 "A significant reduction in the reactivity of anti-Pan
  H1-reacting 27-kDa protein in the nuclear extract obtained from the
  SP-STP-treated Detroit cells with anti- Thr(P)-146 H1 antibody"].

So every mapped dephosphorylation event in this protein's literature is on a
**threonine**; no serine site has been demonstrated, although the PPM fold and
EC 3.1.3.16 cover both.

## Localization

Cytoplasmic plus secreted, by antibody detection [PMID:16487973 "SP-STP,
primarily a cytoplasmic protein, was found to be a major secretory protein of
GAS and essential for bacterial survival."] (the 2011 paper later showed stp is
not in fact essential for survival, only for virulence). Secreted SP-STP enters
host pharyngeal cells and reaches the nucleus [PMID:22262847 "More than 70% of
the total cells displayed the labeled SP-STP within the nucleus"], and
ectopically expressed SP-STP is nuclear [PMID:22262847 "The ectopically
expressed wild-type SP-STP was found to be in the nucleus and conferred
apoptosis of Detroit 562 pharyngeal cells"].

## Bacterial phenotypes of the non-polar stp mutants (PMID:21917918)

Two M1 backgrounds, M1SF370 (M1ΔSTP) and M1T15448 (M1T1ΔSTP), complemented from
a low-copy plasmid.

- **Chains and septa.** Long chains, thickened walls, and
  [PMID:21917918 "revealed unusual staining patterns with multiple asymmetric and
  parallel septa formation"]; the authors' own conclusion is regulatory
  [PMID:21917918 "indicated that SP-STP plays a role in the regulation of septa
  formation and in turn cell division in GAS"]. The proposed mechanism runs
  through WalR phosphorylation and CdhA up-regulation [PMID:21917918 "an increase
  in the level of CdhA protein in the culture supernatants of early log
  phase-grown mutant strains"]. No evidence that SP-STP is itself part of a
  division-site-selection machinery (no Min/Noc/DivIVA-like activity shown).
- **Capsule.** [PMID:21917918 "In both of the STP mutants, we observed a 3–4-fold
  decrease in the capsule production"], with 14–100-fold lower *has* transcript
  and restoration on complementation — i.e. SP-STP positively regulates capsule
  synthesis, via CovR. Note the contrast with the kinase: deleting SP-STK
  *increases* capsule.
- **Fatty acids.** [PMID:21917918 "both saturated fatty acid (SFA) and unsaturated
  fatty acid (UFA) content in the mutant were 2–3-fold up-regulated"] with
  [PMID:21917918 "we also observed down-regulation of the fabT homolog of GAS,
  marR / SPy1755 (3–6-fold), in both of the mutant strains"]. Lipid analysis
  (Table 1) was done for M1SF370 only. Direction: loss of STP → more fatty acid,
  so STP is a negative regulator of fatty acid biosynthesis — but indirectly,
  through the FabT repressor and the STK/STP couple, which the authors state as
  speculation.
- **Adherence/invasion.** [PMID:21917918 "The results showed a significantly
  reduced adherence pattern for the M1ΔSTP strain and unaltered adherence for the
  M1T1ΔSTP mutant in comparison with their corresponding wild-type strains"] and
  [PMID:21917918 "the M1ΔSTP mutant was found to be more invasive than the
  M1T1ΔSTP mutant, reiterating the strain-specific STP-mediated regulation in GAS
  adherence and invasion"], with the discussion stating
  [PMID:21917918 "although the M1ΔSTP mutant lost the ability to adhere to
  pharyngeal cells, the adherent mutant strain was 6-fold more invasive"].
  **Entry into host therefore goes up, not down, when stp is deleted**, and the
  adherence effect is strain-specific — so "positive regulation by symbiont of
  entry into host" has the sign backwards for the one measurable entry readout.
- Mutants were efficiently phagocytosed and attenuated in mice.

## Host apoptosis (PMID:22262847)

Strong, multi-assay: [PMID:22262847 "significantly lower inhibition of
proliferation of pharyngeal cells treated with GAS strains devoid of SP-STP
(M1ΔSTP and M1T1ΔSTP, 5 and 18%, respectively) unlike the wild-type GAS strains
(>90% inhibition)"], restored by complementation; purified protein sufficient and
specific versus the *E. faecalis* homolog EF-STP [PMID:22262847 "only SP-STP and
not EF-STP displayed dose-dependent proliferation inhibition of Detroit
pharyngeal cells"]; annexin-V, JC-1 mitochondrial depolarization, caspase
cleavage and inhibitor blockade [PMID:22262847 "The programmed cell death induced
by SP-STP, which requires active transcription and de novo protein synthesis, is
also caspase-dependent"]; in vivo TUNEL [PMID:22262847 "a significant number of
TUNEL-positive cells were found in the lungs of wild-type M1SF370-infected mice
as compared with the lungs of M1ΔSTP-infected mice"]; and requirement for
catalytic activity/structure [PMID:22262847 "the entry of SP-STP into the
cytoplasm is dependent on its secondary structure as the catalytically inactive
SP-STP with an altered structure is unable to internalize and cause apoptosis"]
(D36A/D192A/D231A). Caveats: two cell lines of four responded, and most work is
on Detroit 562.

## CACAO-specific observations

All eight experimental rows in the GOA file are `assigned_by: CACAO`; the only
non-CACAO rows are two UniProt IEAs. Judgments and the reason each lands where it
does are in the review file. Patterns worth recording for the project page:

1. **Phenotype read as process, with wrong granularity** — GO:0000918 *division
   septum site selection* from the septation phenotype. The paper's own wording is
   "regulation of septa formation"; SP-STP is a signalling phosphatase upstream of
   WalR/CdhA, not a component of the site-selection machinery.
2. **Sign inverted** — GO:0075294 *positive regulation by symbiont of entry into
   host*. The mutant is *more* invasive (6-fold), and the adherence decrease is
   seen in only one of the two strains. Neither direction is established, so the
   sign-free parent (GO:0052372) is what the data support. This is a new shape for
   the taxonomy: not "phenotype as process" but **phenotype as process with the
   sign read off the wrong readout** (adherence standing in for entry).
3. **Right claim, weaker paper than the one that shows it** — GO:0062085 *positive
   regulation of capsule polysaccharide biosynthetic process* is keyed to
   PMID:16487973, whose isogenic mutants were kinase mutants
   [PMID:16487973 "Three isogenic mutants, lacking either the entire SP-STK, or one
   of its two domains"] and in which capsule went *up*; the abstract does assert
   that these proteins modulate capsule
   [PMID:16487973 "the ability of these three proteins to modulate the expression
   of the major virulence factors, the M protein and the capsule"], and the full
   text is unavailable, so the row is kept — but the quantified stp-mutant evidence
   for the positive direction is in PMID:21917918.
4. **Correct but general MF** — GO:0004721 from the 2006 biochemistry, where the
   same paper restricts the modified residue to threonine; the specific child
   GO:0004722 is already annotated.
5. Rows 3–5 of the taxonomy aside, the three best CACAO rows here (GO:0004722 IDA,
   GO:0035970 IDA, GO:0052151 IMP) are accurate and well chosen; this gene is not
   an instance of "paper not about the gene".

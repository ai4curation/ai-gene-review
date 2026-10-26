# ENDOG notes

## 2026-09-30

ENDOG is a nuclear-encoded, mitochondrial DNA/RNA endonuclease with a mitochondrial
transit peptide and catalytic Mg-dependent nuclease fold. The human protein is in the
same PANTHER `PTHR13966:SF5` subfamily as mouse Endog, yeast NUC1, and worm cps-6,
which supports the broad DNA/RNA nonspecific endonuclease PAINT transfers.

The best direct human and mammalian process evidence splits into three branches:

- **Modified nuclear DNA cleavage and recombination.** Robertson et al. purified EndoG
  as the activity in mouse liver extracts that preferentially cleaves
  5-hydroxymethylcytosine-modified DNA, showed recombinant EndoG cleavage, and showed
  that 5hmC stimulates conservative recombination in an EndoG-dependent manner
  [PMID:25355512 Endonuclease G preferentially cleaves 5-hydroxymethylcytosine-modified
  DNA creating a substrate for recombination., "recombinant EndoG preferentially
  recognizes and cleaves a core sequence"; "promote conservative recombination in an
  EndoG-dependent manner"].
- **Mitochondrial DNA turnover.** Wiehe et al. used human-cell knockdown, knockout,
  re-expression, and nuclease-mutant assays to show that ENDOG stimulates mitochondrial
  DNA depletion and compensatory mitochondrial DNA replication in a nuclease-dependent
  manner, especially under oxidative stress [PMID:29719607 Endonuclease G promotes
  mitochondrial genome cleavage and replication., "EndoG stimulates both mtDNA
  replication"].
- **Starvation autophagy.** Wang et al. showed that starvation-released, GSK3beta-
  phosphorylated ENDOG binds YWHAG/14-3-3gamma, freeing TSC2 and VPS34 from YWHAG to
  suppress mTORC1 and initiate autophagy; they also support an endonuclease-dependent
  DNA damage-response branch of the same autophagy phenotype [PMID:33473107
  Endonuclease G promotes autophagy by suppressing mTOR signaling and activating the DNA
  damage response., "mTOR pathway suppression and autophagy initiation"; "enhances its
  interaction with 14-3-3"].

The inherited apoptotic DNA-fragmentation row is plausible and should stay specific:
ENDOG can itself cleave DNA after mitochondrial release, so `GO:0006309 apoptotic DNA
fragmentation` is preferable to any broad `GO:0006915 apoptotic process` row. It is not
the central CAD/DFF40 nuclease, though, and the more recent human papers point toward
mtDNA maintenance, 5hmC-biased cleavage/recombination, and starvation autophagy as the
core ENDOG axes.

The rat-derived stimulus rows for mechanical stimulus, calcium, glucose, hypoxia,
estradiol, oxidative stress, and hydrogen-peroxide cell death look over-propagated into
human. They describe conditions or cell-death outcomes in which rat Endog was mobilized
rather than a molecular step performed by human ENDOG. The DNAJA4 and ITLN2 protein
binding rows from high-throughput interactome/chaperone studies were removed as generic
edges with no ENDOG-specific functional interpretation.

## 2026-10-26 — family, orthologs, human disease, and the dataset landscape

### Family and evolution

ENDOG sits in PANTHER PTHR13966 subfamily SF5 with worm CPS-6, yeast NUC1, fission
yeast pnu1 and the secreted bacterial nucleases NucA (*Serratia*, *Nostoc*). Two
sibling subfamilies matter for interpretation. SF19 is EXOG, a metazoan paralog
produced by duplication of an ancestral mitochondrial endo/exonuclease
[PMID:18187503 "during metazoan evolution duplication of an ancestral nuclease gene
obviously generated the paralogous EndoG- and EXOG-protein subfamilies in higher
eukaryotes"]; a Wing domain converts it into a 5' exonuclease for mtDNA base-excision
repair [PMID:28466855 "A Wing domain, absent in other ββα-Me members, suppresses
endonuclease activity"]. SF17 is secreted insect salivary DNases, one of which
destroys neutrophil extracellular traps to help *Leishmania* survive
[PMID:24516388 "Lundep hydrolyzes both ss- and dsDNA with little sequence
specificity"]. So the same His-Me finger fold is used for mtDNA housekeeping, for
mtDNA repair, and — on a secreted branch — for host-DNA destruction.

Regulation by a dedicated inhibitor is conserved in outline. Flies have EndoGI
[PMID:19129189 "We propose that EndoGI protects the cell against low levels of EndoG
outside mitochondria"], and two 2026 papers independently identify KU80 as the
mammalian equivalent [PMID:41837724 "The KU80 C-terminal domain (CTD) shares
structural homology with Drosophila EndoG inhibitor (EGI), directly binds ENDOG and
inhibits its nuclease activity in vitro"].

Ortholog phenotypes do not transfer cleanly. Worm CPS-6 and fly EndoG degrade
paternal mtDNA [PMID:27338704, PMID:22421049], but mouse Endog knockouts have normal
spermatogenesis and sperm mtDNA [PMID:39373150 "our results indicate that ENDOG is
not essential for spermatogenesis or the elimination of sperm mtDNA in mice"].

### Human disease: mitochondrial, not immune

One genetically defined patient is reported: biallelic ENDOG variants with absent
protein, progressive external ophthalmoplegia, mitochondrial myopathy and multiple
mtDNA deletions in muscle [PMID:35326425 "we report biallelic ENDOG variants
identified by NGS in a patient with progressive external ophthalmoplegia,
mitochondrial myopathy and multiple mtDNA deletions in muscle"], plus low-level
heteroplasmic point mutations in fibroblasts [PMID:35326425 "we detected an
accumulation of low-level heteroplasmy mtDNA point mutations compared with
age-matched controls"]. dismech's Gene Table of Neuromuscular Disorders transcription
classifies ENDOG under `mitochondrial_myopathies`. MONDO has no ENDOG-specific term;
such a disease would sit under MONDO:0000090 progressive external ophthalmoplegia
with mitochondrial DNA deletions.

The other established mammalian phenotype is cardiac. Rat systems genetics mapped a
blood-pressure-independent left-ventricular-mass locus to Endog [PMID:21979051 "we
found a loss-of-function mutation in Endog that is associated with increased LVM and
impaired cardiac function"], with depleted mitochondria and elevated ROS in the
knockout heart [PMID:21979051 "the Endog-deleted mouse heart had depleted
mitochondria, mitochondrial dysfunction and elevated levels of reactive oxygen
species"]; the hypertrophy is ROS-dependent [PMID:29502044 "Cardiomyocyte hypertrophy
induced by Endonuclease G deficiency requires reactive oxygen radicals
accumulation"].

**No immune phenotype is reported for ENDOG loss in any organism.** Human LoF is
entirely unconstrained in gnomAD v4 (pLI 4.5e-08; o/e LoF 0.97, 22 observed vs 22.6
expected; LOEUF 1.39), so heterozygous LoF is not selected against and no
dominant immune phenotype is plausible. This is the opposite of DNASE1L3, whose loss
causes monogenic SLE.

### The immune-adjacent mechanism that *is* supported — in yeast

Two recent yeast papers put the EndoG family on the mtDNA-escape route that feeds
cytosolic DNA sensing. Nuc1 degrades mtDNA destined to leave the organelle
[PMID:41638207 "We identify the mechanism by which an intermembrane space nuclease,
endonuclease G (human ENDOG; yeast Nuc1), prevents mtDNA escape to the cytosol in
yeast"], and both its catalytic activity and its mitochondrial localization are
required [PMID:41638207 "Nuc1 nuclease activity and mitochondrial localization are
essential for preventing mtDNA escape"]; escape runs through mitophagy and the
vacuole. Separately, Nuc1 limits transfer of long mtDNA to the nucleus
[PMID:39227600 "nuclease limits insertion of cDNA and transfer of very long mtDNA"],
in a paper that frames the metazoan question explicitly [PMID:39227600
"mitochondrial DNA (mtDNA) or retrotransposon cDNA released to cytoplasm are degraded
by nucleases to prevent sterile inflammation"].

Whether human ENDOG does either job is untested. That is the gap worth an
OpenScientist run, and it is a mechanistic question rather than a disease-gene one.

### Dataset landscape (checked, not assumed)

- **No public ENDOG perturbation expression data.** A GEO query for ENDOG knockout
  or knockdown returns two datasets, both incidental text matches, and none of the
  mechanistic papers (PMID:29719607, PMID:33473107, PMID:37794041, PMID:39752519)
  has a GEO series indexed by PMID. So an "ENDOG-null interferon signature" cannot be
  read off public transcriptomes today.
- **NUMT catalog.** 1,637 NUMTs with mtDNA coordinates across 66,083 genomes
  [PMID:36198798 "More than 99% of individuals had at least one of 1,637 different
  NUMTs"], including the observation that [PMID:36198798 "NUMTs preferentially
  involved non-coding mitochondrial DNA, linking transcription and replication to
  their origin"]. The per-individual genotypes are UK Biobank and restricted, but the
  NUMT breakpoint coordinates are published, so breakpoint-versus-motif analysis is
  open.
- **mtDNA population variation.** gnomAD v3.1 mtDNA [PMID:35074858 "Our gnomAD v3.1
  release contains population frequencies for 10,850 unique mtDNA variants"] is open
  and queryable; it reports heteroplasmy at >=10% only, and explicitly treats NUMT
  misalignment as a false-positive source.
- **Sub-mitochondrial reference proteomes.** MitoCarta3.0 (PMID:33174596) carries
  sub-mitochondrial localization assignments, and APEX2 proximity-labeling proteomes
  exist for matrix and IMS; these are the resources that could settle the
  intermembrane-space-versus-matrix conflict without new wet-lab work.
- **MITOMAP** deletion tables returned HTTP 403 to automated access; a deletion
  breakpoint catalog would need another route.

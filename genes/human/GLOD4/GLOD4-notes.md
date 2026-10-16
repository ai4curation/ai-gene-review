# GLOD4 (Q9HC38, HGNC:14111; formerly C17orf25) review notes

## Why this gene was selected

GLOD4 is a glyoxalase-domain orphan: UniProt places it in the glyoxalase I family by sequence
similarity (ECO:0000305) but assigns no EC number and no catalytic residues, and until 2026 its
entire GOA molecular-function record was `GO:0045296 cadherin binding` from a single
proximity-labelling experiment. A 2026 PNAS paper assigns it a first real enzymatic activity,
and an unusual one.

## Reference verification

PMID:41628334 verified against PubMed: Wright S, Dang VC, Hussain S, et al. (22 authors),
"Selective peroxynitrite-mediated protein nitration catalyzed by glyoxalase domain containing
protein 4." Proc Natl Acad Sci USA 2026 Feb 2;123(6):e2515002123. doi:10.1073/pnas.2515002123.
PMC12890929. Full text cached.

PMID:25468996 verified: Guo Z, Neilson LJ, Zhong H, et al., "E-cadherin interactome complexity
and robustness resolved by quantitative proteomics." Sci Signal 2014;7(354):rs7.
PMID:34800366 verified: Morgenstern M et al., Cell Metab 2021;33(12):2464-2483 (MitoCoP).
PMID:23533145 verified: In-depth proteomic analyses of exosomes from expressed prostatic
secretions in urine, Proteomics 2013.

## The claim, and how strong it is

Headline:
[PMID:41628334 "Here, we showed that glyoxalase domain-containing protein 4 (GLOD4), a
previously uncharacterized protein, is an enzyme that catalyzes selective protein nitration."]
[PMID:41628334 "A primary in vivo target for GLOD4-mediated nitration is alpha-synuclein
(α-syn), which is central to the pathogenesis of Parkinson's disease (PD) and related
disorders."]

What is actually shown, layer by layer:

*Biochemistry.* Recombinant and RBC-purified GLOD4 nitrates an α-synuclein peptide and
full-length α-syn in the presence of peroxynitrite; MS localises the modification
[PMID:41628334 "confirmed that GLOD4 catalyzed the nitration of the tyrosine residues Y39 and
Y125 of α-syn"]. Kinetics follow Michaelis-Menten
[PMID:41628334 "The estimated catalytic efficiency kcat/Km was 1.6 × 107 M−1 s−1, indicating
that GLOD4 is an efficient enzyme for nitrating α-synuclein."] and stopped-flow shows GLOD4
consumes the cosubstrate [PMID:41628334 "The data indicated that GLOD4 accelerated the
decomposition of peroxynitrite"].

*Cosubstrate specificity (a real strength).* The paper rules out the obvious alternatives:
[PMID:41628334 "The data illustrate that GLOD4 selectively uses peroxynitrite as a cosubstrate,
and not nitric oxide or nitric oxide-derived oxidants, or H2O2 combined with nitrite, to nitrate
α-syn."] and [PMID:41628334 "Moreover, GLOD4 does not function as an oxidase or peroxidase."]

*Active site.* [PMID:41628334 "However, inductively coupled plasma-mass spectrometry (ICP-MS)
analysis revealed that Zn2+ was present in purified GLOD4"] and
[PMID:41628334 "Mutation of GLOD4 at the putative metal-binding residues H8A and E70A and its
active site C254A reduced or eliminated its ability to catalyze α-syn nitration."]
This is the single most important control: a structure-guided catalytic-residue mutant that
loses activity is what separates an enzyme from a protein that merely accelerates a chemical
reaction non-specifically.

*Substrate selectivity.* A 23,000-protein HuProt array gave a very short hit list
[PMID:41628334 "GLOD4 catalyzed the nitration of α-syn and β-syn, PPM1B and PQBP1."], and
γ-synuclein, which lacks the C-terminal tyrosines, was not nitrated. Selectivity is the core
argument of the paper, since spontaneous peroxynitrite chemistry is not selective.

*Cells and animals.* [PMID:41628334 "In the GLOD4-KO line, tyrosine nitration of α-syn was
reduced by 86% upon adding peroxynitrite under the same experimental conditions, indicating
that GLOD4 mediates α-syn nitration in cells."] and in mice
[PMID:41628334 "The GLOD4-KO mice showed a gene-dependent reduction in the basal levels of
nitrated α-syn in RBCs and in the striatum"], with the gene-dose dependence being the
persuasive part.

*Localization.* [PMID:41628334 "GLOD4 is present in both mitochondria and cytosol, with
relatively higher levels in the cytosol"] - which qualifies UniProt's mitochondrion-only
subcellular location, itself inferred (ECO:0000305) from a 2003 interaction paper.

## Limitations to state honestly

1. **One paper, one laboratory, commercial interest.** Almost all authors are at Nitrase
   Therapeutics, and the paper itself declares
   [PMID:41628334 "Patent application, US63/733,953, filed on GLOD4 activity."] That is not a
   reason to disbelieve the data, but it is a reason to record the claim as single-sourced and
   awaiting independent replication.
2. **The category is unusual.** "Enzymatically catalysed protein tyrosine nitration" is a new
   enzyme class; the authors are explicit that it is a proposal
   [PMID:41628334 "Thus, we propose that GLOD4 is a putative member of a discovered enzyme
   family, which we tentatively refer to as nitrases based on their ability to catalyze self- or
   targeted protein tyrosine nitration."] and hedge again in the discussion
   [PMID:41628334 "Here, we report that GLOD4 is potentially a member of a class of enzymes that
   use peroxynitrite to catalyze the tyrosine nitration of specific proteins."]
3. **Mechanism is not established.** The paper states that work to dissect the catalytic
   mechanism is ongoing and that it is not yet known whether zinc is the catalytic metal.
4. **No organismal phenotype.** [PMID:41628334 "We also observed that GLOD4-KO mice were viable,
   follow Mendelian genetics in terms of birth rates, and show no phenotypic defects through 18
   mo of age."] So the physiological importance of the activity is undetermined, even though the
   biochemical contribution to α-syn nitration is large.
5. **Two of the four substrates are in vitro only** (PPM1B, PQBP1), as the authors note.
6. **The glyoxalase assignment is untouched.** No glyoxalase/lactoylglutathione lyase activity
   has ever been demonstrated for GLOD4, and the paper reframes the family relationship
   structurally rather than functionally
   [PMID:41628334 "Although GLOD4 has no known sequence-based homologs, it is a member of a
   structurally related family of metalloenzymes known as the vicinal oxygen chelate (VOC)
   superfamily"]. The "glyoxalase domain" in the gene name remains a fold description, not an
   activity, and no EC number is assigned.

## The GO term problem

There is **no GO term for protein nitration at all** - not as a molecular function and not as a
biological process. Searching QuickGO for "nitration" returns nothing; the nearest existing
terms are wrong chemistry or wrong direction:

- `GO:0017014 protein nitrosylation` - addition of a nitric oxide group (S-nitrosylation of
  cysteine). Different atom count, different residue, different chemistry. The paper
  specifically excludes NO and NO-derived oxidants as GLOD4 cosubstrates.
- `GO:0072541 peroxynitrite reductase activity` and `GO:0062213 peroxynitrite isomerase
  activity` - these consume peroxynitrite but yield nitrite or nitrate, i.e. they are
  detoxification activities. GLOD4 also accelerates peroxynitrite decomposition, so there is a
  superficial resemblance, but the product is a nitrated protein, not a free anion. Using either
  would assert a detoxifying role, the opposite of what is described.
- `GO:0018212 peptidyl-tyrosine modification` is obsolete.

So the honest options were a wrong term or no term. Two `proposed_new_terms` are filed instead
(one MF, one BP), and the NEW annotations placed in the file are deliberately non-committal:
`GO:0140096 catalytic activity, acting on a protein` as an explicitly flagged placeholder that
is true but uninformative, plus `GO:0008270 zinc ion binding` and `GO:0005829 cytosol`, which
are specific and independently supported.

## Curation position taken

- `GO:0005739 mitochondrion` (IEA and HTP) -> **ACCEPT** for both. GLOD4 is in the MitoCoP
  high-confidence mitochondrial proteome and the 2026 paper's own fractionation finds it in
  mitochondria, though with more in cytosol.
- `GO:0045296 cadherin binding` (HDA) -> **MARK_AS_OVER_ANNOTATED**. The source is BioID
  proximity labelling of the E-cadherin cytoplasmic tail, which reported
  [PMID:25468996 "We used proximity biotinylation and quantitative proteomics to identify 561
  proteins in the vicinity of the cytoplasmic tail of E-cadherin."] Proximity within a labelling
  radius is not binding; a 561-protein list from an abundant-cytosolic-protein-rich compartment
  is the classic source of spurious `cadherin binding` annotations, and nothing else connects
  GLOD4 to adherens junctions.
- `GO:0070062 extracellular exosome` (HDA) -> **KEEP_AS_NON_CORE**. GLOD4 was genuinely detected
  in prostatic-secretion exosomes, but abundant cytosolic proteins are routine in exosome
  proteomes and this is not where the enzyme acts.
- **NEW** `GO:0140096 catalytic activity, acting on a protein` (IDA) - placeholder for the
  nitrase activity, flagged as such.
- **NEW** `GO:0008270 zinc ion binding` (IDA) - ICP-MS on purified protein plus loss of activity
  in the H8A/E70A metal-site mutants.
- **NEW** `GO:0005829 cytosol` (IDA) - subcellular fractionation of H4 cells.

## Open questions

- Is the activity reproducible outside Nitrase Therapeutics? This is the first thing an
  independent laboratory should check, ideally with the recombinant protein and the published
  active-site mutants.
- What is the catalytic mechanism, and is Zn2+ the catalytic metal or a structural one? The
  authors leave this open and list Mn, Ni and Fe as alternatives.
- Does GLOD4 have any glyoxalase-family activity? The fold says VOC superfamily; no metabolic
  substrate has ever been tested systematically.
- Why is a nitrase in mitochondria as well as cytosol, and are there mitochondrial substrates?
  The α-syn work is all cytosolic.
- GLOD4-KO mice are healthy to 18 months. What, then, is the physiological function of selective
  α-syn nitration, and does removing it change synuclein pathology rather than baseline biology?

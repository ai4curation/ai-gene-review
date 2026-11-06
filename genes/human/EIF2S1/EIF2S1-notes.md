# EIF2S1 (eIF2alpha, P05198) — curation notes

Curated for the [Integrated Stress Response project](../../../projects/INTEGRATED_STRESS_RESPONSE.md)
(issue #3951). EIF2S1 is also a listed candidate of the
[Stress Granules project](../../../projects/STRESS_GRANULES.md) (issue #3953).

No provider deep-research file was available in this environment (`just deep-research`
is not a recipe in the justfile and no provider API key is present), so these notes were
written from the cached UniProt record, the cached publications, and the GOA file under
review. Nothing here is named `-deep-research-*`.

## Identity and the EIF2A name collision

`EIF2S1` has the legacy alias `EIF2A`, which is **not** the gene `EIF2A`. UniProt carries
an explicit caution: [file:human/EIF2S1/EIF2S1-uniprot.txt "This gene should not be
confused with EIF2A, with which it shares the alias EIF2A."]. Any annotation sourced from
an older paper that writes "eIF2A" needs this check; none of the 102 GOA rows reviewed here
appeared to be mis-keyed on that basis.

Protein: 315 aa, 36.1 kDa [PMID:2948954 "Both rat and human eIF-2 alpha proteins comprise
315 amino acids (36.1 kDa) and differ by only three amino acids."]. S1/OB-fold domain at
residues 17-88 (`DOMAIN 17..88`, `InterPro; IPR044126; S1_IF2_alpha.`). PANTHER family
PTHR10602.

## Residue numbering: the paper's S51 is UniProt Ser52

The eIF2alpha literature almost universally writes the ISR phosphosite as **Ser51**, which
is the mature-protein numbering (initiator Met removed). UniProt P05198 numbers from Met1
and therefore calls the same residue **Ser-52**; position 51 of the displayed sequence is a
leucine. The Chan lab mitophagy paper uses the S51 convention throughout (`EIF2αS51A`,
`EIF2αS51D`), while UniProt's `MOD_RES 52` and `MUTAGEN 52` lines describe the same
experiments. Every residue statement in the review file is written as Ser52 of P05198 with
the paper's S51 noted, so the number is never ambiguous about which sequence it indexes.
This is a numbering convention, not a UniProt defect and not an isoform mismatch, so it is
recorded here rather than as a `source_defects` entry.

## Core biology

**The eIF2 heterotrimer.** [file:human/EIF2S1/EIF2S1-uniprot.txt "Eukaryotic translation
initiation factor 2 eIF2 is a heterotrimeric complex composed of an alpha (EIF2S1), a beta
(EIF2S2) and a gamma (EIF2S3) chain"]. Gamma is the GTPase core
[PMID:23063529 "Here, we show that a human X-chromosomal neurological disorder characterized
by intellectual disability and microcephaly is caused by a missense mutation in eIF2γ
(encoded by EIF2S3), the core subunit of the heterotrimeric eIF2 complex."]; assembly is
CDC123-dependent and alpha is the **last** subunit added
[PMID:35031321 "By binding to eIF2γ, eIF2α displaces Cdc123 and thereby completes the
assembly process." / "In addition, levels of eIF2α influence the rate of eIF2 assembly."].
So alpha is both a structural subunit and a rate-determining component of holo-eIF2
formation.

**Initiation.** [file:human/EIF2S1/EIF2S1-uniprot.txt "Member of the eIF2 complex that
functions in the early steps of protein synthesis by forming a ternary complex with GTP and
initiator tRNA"] and [... "This complex binds to a 40S ribosomal subunit, followed by mRNA
binding to form a 43S pre-initiation complex (43S PIC)"]. Added eIF2 stimulates translation
of capped, uncapped **and** IRES-driven mRNAs in a HeLa extract
[PMID:16289705 "eIF2 (eukaryotic translation initiation factor 2) and eIF2B augmented
translation of capped, uncapped and encephalomyocarditis virus-internal ribosome entry
site-promoted mRNAs."] — which is the experimental basis for the gene carrying *both*
`GO:0160296` (cap-dependent) and `GO:0160297` (IRES-mediated) initiation-factor activity by
IDA. The same paper's internal control (eIF4E stimulating only capped mRNA) shows the
cap-independence is real rather than a non-specific extract effect
[PMID:16289705 "eIF4E specifically stimulated capped mRNA translation"].

**The ISR switch.** This is the one function that is specific to the alpha subunit.
Phosphorylation of Ser52 (paper S51) by any of HRI/PKR/PERK/GCN2 converts eIF2 from an
eIF2B substrate into a competitive eIF2B inhibitor:
[PMID:38340717 "Phosphorylation of the α subunit of EIF2 by the ISR kinases causes EIF2 to
change from a substrate to a competitive inhibitor of EIF2B."],
[PMID:29599213 "Phosphorylation converts eIF2 from a substrate to a competitive inhibitor of
its dedicated guanine nucleotide exchange factor, eIF2B, thereby inhibiting translation."].
Structurally the two states are distinct binding modes on eIF2B, not a loss of affinity
[PMID:31048492 "The unphosphorylated and phosphorylated forms of eIF2 bind to eIF2B in
completely different manners: the nucleotide exchange-active and -inactive modes,
respectively."]. The output is global attenuation plus selective uORF-licensed translation
[file:human/EIF2S1/EIF2S1-uniprot.txt "This results in the global attenuation of 5'
cap-dependent protein synthesis and concomitant translation of ISR-specific mRNAs that
contain a short upstream open reading frame (uORF) in their 5' UTR, such as ATF4, ATF5,
DDIT3/CHOP and PPP1R15A/GADD34"].

Note the direction of the molecular event: it is phospho-eIF2 that **binds and inhibits**
eIF2B. The informative molecular function for the ISR arm is therefore an eIF2B-directed
binding/inhibition activity, which is why the review's second core function uses
`GO:0031369 translation initiation factor binding` rather than a bare `protein binding`.

**Return to baseline.** GADD34 (PPP1R15A) scaffolds PP1 onto eIF2alpha
[PMID:26095357 "The growth-arrest- and DNA-damage-induced transcript 34 (GADD34) bound to the
serine/threonine protein phosphatase 1 (PP1) is the necessary eIF2α phosphatase complex that
returns mammalian cells to normal protein synthesis following stress."],
[PMID:26095357 "The data highlight independent interactions of PP1 and eIF2α with GADD34,
demonstrating that GADD34 functions as a scaffold both in vitro and in cells."]. This is the
basis for rewriting the PPP1CA protein-binding row as `GO:0019903 protein phosphatase
binding`.

**Kinase docking.** eIF2alpha's N-terminal domain is the substrate-targeting module that
docks on the kinase C-lobe, and the poxvirus K3L pseudosubstrate mimics it
[PMID:9431994 "Homologous regions of the alpha subunit of eukaryotic translational initiation
factor 2 (eIF2alpha) and the vaccinia virus K3L gene product interact with the same domain
within the dsRNA-activated protein kinase (PKR)."],
[PMID:18971339 "Our results support the identification of the eIF2alpha-binding site on an
extensive face of the C-terminal lobe of the kinase domain, and they indicate that subtle
changes to the PKR kinase domain can drastically impact pseudosubstrate inhibition while
leaving substrate phosphorylation intact."]. This is the basis for rewriting the PKR/PERK
protein-binding rows as `GO:0019901 protein kinase binding`.

## The mitochondrial branch, and what it does and does not license

The HRI branch is the one that relays mitochondrial stress, via OMA1-cleaved DELE1
[PMID:32132707 "Here we show that HRI is the eIF2α kinase that is necessary and sufficient
for this relay."], [PMID:32132707 "Mitochondrial stress stimulates OMA1-dependent cleavage of
DELE1 and leads to the accumulation of DELE1 in the cytosol, where it interacts with HRI and
activates the eIF2α kinase activity of HRI."].

The 2024 Chan-lab paper then shows that p-eIF2 itself accumulates on mitochondria and that
this is the mitophagy trigger:

- fractionation: [PMID:38340717 "However, DFP treatment resulted in notable accumulation of
  p-EIF2α in the mitochondrial fraction, whereas Tg treatment resulted in p-EIF2α
  localization almost exclusively in the cytosolic fraction (Figure 4A)."]
- the ER-contamination control that `projects/ORGANELLES.md` asks for was done:
  [PMID:38340717 "Analysis of the subcellular fractions with an ER marker showed no evidence
  of ER enrichment of p-EIF2α upon DFP treatment (Figure S4C)."]
- outer-membrane marker colocalization: [PMID:38340717 "We observed clear colocalization of
  p-EIF2α with the mitochondrial OM marker TOM20 in DFP-treated samples as opposed to control
  or Tg-treated samples (Figure 4C)."]
- sufficiency by OM tethering of the phosphomimetic: [PMID:38340717 "Accompanying this
  mitochondrial localization, a substantial increase in mitophagy was measured in K562 cells
  expressing EIF2αS51D but not in cells expressing EIF2αWT or EIF2αS51A (Figure 5B)."],
  [PMID:38340717 "Taken together, these results indicate that phosphorylation and
  mitochondrial localization of EIF2α are necessary and sufficient to trigger mitophagy."]

Two consequences for the review:

1. **Sub-compartment.** Three independent lines (fractionation with an ER-marker control,
   TOM20 colocalization, and a Fis1-anchored OM tethering experiment that reconstitutes the
   function) agree on the mitochondrial **outer** membrane, and the cytosolic topology is
   forced — p-eIF2alpha is a cytosolic protein recruited to the organelle surface, not
   imported. Per `projects/ORGANELLES.md` this clears the bar for adding
   `GO:0005741 mitochondrial outer membrane` as a `NEW` IC row **beside** the retained
   `GO:0005739 mitochondrion` rows, not as a substitute for them.
2. **Mitophagy vs regulation of mitophagy.** The mechanism downstream of p-eIF2alpha's
   arrival on the surface is explicitly unresolved
   [PMID:38340717 "More experiments will be needed to understand the mechanism whereby p-EIF2
   on the mitochondrial surface results in recruitment or initiation of autophagosomes."], and
   the pathway is distinct from PINK1/PRKN
   [PMID:38340717 "The HRI mitophagy pathway operates in parallel with the mitophagy pathway
   controlled by the Parkinson's disease related genes PINK1 and PARKIN and is mechanistically
   distinct."]. eIF2alpha supplies the signal; it has not been shown to do any of the
   engulfment or receptor work. So `GO:0000423 mitophagy` is modified to
   `GO:1901526 positive regulation of mitophagy`, which is also what the sibling EIF2AK1 (HRI)
   review carries for the same pathway.

The same paper incidentally supports treating the `GO:0005634 nucleus` IEA row as an
over-annotation: the authors treat the nuclear p-eIF2alpha immunofluorescence signal as
something to be subtracted [PMID:38340717 "Before analyzing the co-localization between TOM20
and p-EIF2α, the nuclear signal for p-EIF2α was removed post-imaging using the DAPI
channel."], and UniProt's curated subcellular location lists only cytosol, stress granule and
mitochondrion.

## How the 102 GOA rows were handled

Counts and the full per-row reasoning are in `EIF2S1-ai-review.yaml`. The shape of the
review:

- **Core, accepted as-is**: `GO:0005850` eIF2 complex (5 rows), `GO:0005829` cytosol
  (17 rows), `GO:0033290` 48S PIC, `GO:0044207` ternary complex, `GO:0160296`/`GO:0160297`
  initiation-factor activities, `GO:0032057` negative regulation of translational initiation
  in response to stress, `GO:0036499` PERK-mediated UPR, `GO:0140468` HRI-mediated signaling,
  `GO:0043022` ribosome binding.
- **Correct but general, modified to a descendant the gene already carries**:
  `GO:0003676` -> `GO:0003723`; `GO:0003723` -> `GO:0003729` mRNA binding;
  `GO:0003743` -> `GO:0160296` + `GO:0160297`; `GO:0006413` -> `GO:0002183`
  (matching the sibling EIF2S3 review); `GO:0006446` -> `GO:0032057`;
  `GO:0034976` -> `GO:0036490` + `GO:0036499`; `GO:0005737` -> `GO:0005829`
  (also matching EIF2S3).
- **Bare `GO:0005515` (25 rows)**: per the repository protein-binding policy, rewritten to an
  informative MF where the cited paper supports one — `GO:0031369` for eIF2/eIF2B subunits
  (11 rows), `GO:0019901` for the PKR/PERK kinases (4 rows), `GO:0019903` for PPP1CA
  (1 row) — and removed as uninformative otherwise (9 rows: ABCF1 x2, DDX3X x2, TBL2, ACTN1,
  VAC14, PRMT7 x2). Removal does not say the interaction is false.
- **Over-annotations**: `GO:0016020` membrane (HDA membrane-proteome fraction),
  `GO:0070062` extracellular exosome (HDA), `GO:0005634` nucleus (Compara transfer),
  `GO:0097451` glial limiting end-foot (Compara transfer of a highly specific anatomical
  location to a ubiquitous housekeeping factor), `GO:1904373` response to kainic acid and
  `GO:1990737` response to manganese-induced ER stress (treatment-specific rat experiments
  transferred electronically).
- **Non-core but kept**: the stress-input terms (`GO:0034198`, `GO:0034599`, `GO:0034605`,
  `GO:0034644`), `GO:0010494`/`GO:0034063` stress granule terms, `GO:0045202` synapse, and
  the modified mitophagy row.

## Open questions carried into the review file

- What on the mitochondrial outer membrane reads p-eIF2alpha and converts it into
  autophagosome recruitment? Targeting p-eIF2alpha to peroxisomes did **not** induce
  pexophagy, so a mitochondria-specific co-factor is required.
- Is the Ser49 site (UniProt `MOD_RES 49`, "by HRI", `ECO:0000250|UniProtKB:P83268`) phosphorylated
  in human cells, and does it contribute to eIF2B inhibition independently of Ser52? The
  human evidence for Ser49 is by similarity only.
- Does mitochondrial p-eIF2 act on local translation of mitochondrially-targeted mRNAs in
  addition to signalling mitophagy? Raised as a possibility by the authors themselves.

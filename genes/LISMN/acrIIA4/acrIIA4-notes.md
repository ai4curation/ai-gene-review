# AcrIIA4 (A0A247D711, Listeria monocytogenes prophage) — curation notes

## Identity and record state

UniProt entry is **unreviewed (TrEMBL)**, 87 aa, `SubName: Full=Anti-CRISPR protein
AcrIIA4` from EMBL and `SubName: Full=Associated protein` from PDB 5XBL. Taxon is
assigned to *Listeria monocytogenes* (NCBITaxon:1639) rather than to a phage, because
the gene sits in a prophage integrated in the *L. monocytogenes* chromosome.

**The accession is the assayed protein.** Rauch et al. used `AcrIIA4- (AEO04689.1)` as
the reference sequence for their phylogenetic reconstruction
[PMID:28041849 "AcrIIA2- (AEO04363.1), AcrIIA3- (CBY03209.1) and AcrIIA4- (AEO04689.1) homologous protein sequences were acquired by BLASTp searches"].
NCBI `efetch` of AEO04689.1 (hypothetical protein LMOG_02993, *L. monocytogenes* J0161)
returns
`MNINDLIREIKNKDYTVKLSGTDSNSITQLIIRVNNDGNEYVISESENESIVEKFISAFKNGWNQEYEDEEEFYNDMQTITLKSELN`,
which is **100% identical over all 87 residues** to A0A247D711. The entry also carries
PDB 5XBL (AcrIIA4–SpyCas9–sgRNA, 3.05 Å) and 5XN4 (solution NMR), so the structural and
the genetic work are on the same sequence. Experimental evidence codes are therefore
appropriate on this accession, not similarity codes.

## Discovery and in vivo inhibition

AcrIIA4 was one of four type II-A Cas9 inhibitors found by searching *cas9*-bearing
genomes for a CRISPR spacer coexisting with its own target
[PMID:28041849 "This analysis led to the discovery of four unique type II-A CRISPR-Cas9 inhibitor proteins encoded by Listeria monocytogenes prophages."].
Two of the four, AcrIIA2 and AcrIIA4, also inhibit the heterologous *S. pyogenes* Cas9
[PMID:28041849 "Two of these inhibitors also blocked the widely used Streptococcus pyogenes Cas9 when assayed in Escherichia coli and human cells."],
and the authors attribute the breadth to a conserved target surface
[PMID:28041849 "Using the orthologous Spy Cas9, it is clear that AcrIIA2 and AcrIIA4 have broad specificity, given that Lmo Cas9 and Spy Cas9 only share 53% sequence identity. AcrIIA2 and AcrIIA4 likely target regions conserved between the two Cas9 proteins."].
Prophage carriage is common, so this is a widespread counter-defence and not a curiosity
[PMID:28041849 "More than half of L. monocytogenes strains with cas9 contain at least one prophage-encoded inhibitor, suggesting widespread CRISPR-Cas9 inactivation."].

## Mechanism: DNA mimicry at the PAM-recognition site, plus RuvC occlusion

The module (`modules/anti_crispr_suppression.yaml`, annoton `acriia4_dna_mimic`) assigns
AcrIIA4 to the "Type II Cas9 PAM-site occlusion and DNA mimicry" variant. **The
assignment holds, and is if anything understated: two surfaces are occluded, not one.**

Yang & Patel solved the AcrIIA4–SpyCas9–sgRNA crystal structure and found competitive
occupancy of *both* the PAM-reading surface and the RuvC pocket
[PMID:28602637 "AcrIIA4 preferentially targets critical residues essential for PAM duplex recognition, as well as blocks target DNA access to key catalytic residues lining the RuvC pocket"],
[PMID:28602637 "demonstrate that AcrIIA4 competitively occupies both PAM-interacting and non-target DNA strand cleavage catalytic pockets"].
The buried-area comparison is the quantitative statement of the competition
[PMID:28602637 "AcrIIA4 targets the concave surface formed by the Topo, CTD and RuvC domains in the SpyCas9-sgRNA binary complex and buries an area of 1,693 Å2 on ternary complex formation (Figure 4A). By contrast, positioning of the PAM duplex of dsDNA on the surface formed by Topo and CTD domains of the SpyCas9-sgRNA binary complex buries an area of 553 Å"],
and the β1–β2 loop reaches into the RuvC active site itself
[PMID:28602637 "the protruding β1–β2 loop of AcrIIA4 inserts into the active site of RuvC domain"].

Dong et al., independently, state the mimicry explicitly
[PMID:28448066 "AcrIIA4 inhibits SpyCas9 activity by structurally mimicking the PAM to occupy the PAM-interacting site in the PAM-interacting domain, thereby blocking recognition of double-stranded DNA substrates by SpyCas9. AcrIIA4 further inhibits the endonuclease activity of SpyCas9 by shielding its RuvC active site."]
(abstract only in cache; no PMC record).

The physical basis of the mimicry is an acidic surface patch, characterised by NMR
[PMID:29497118 "AcrIIA4 is an acidic protein (pI ~4.2), and the surface electrostatic potential indicates that negative charges are densely populated in the β3–α2 loop, the α2–α3 loop and the beginning of the α3 helix"],
[PMID:29497118 "It has been suggested that the negatively charged patches mimic the phosphate groups of nucleic acids that associate with the PAM interaction site of SpyCas9"].
The same paper notes convergence with the unrelated type I-F inhibitor AcrF2
[PMID:29497118 "which was also found in AcrF2 proteins inhibiting the subtype I-F effector complex"],
which is exactly the mechanism-not-family convergence the module is built around.

Binding is **guide-dependent**: the binding site on Cas9 only exists once sgRNA is loaded
[PMID:28448066 "Our data show that AcrIIA2 and AcrIIA4 interact with SpyCas9 in a sgRNA-dependent manner."],
[PMID:28448066 "Structural comparison reveals that formation of the AcrIIA4-binding site of SpyCas9 is induced by sgRNA binding."],
and Yang & Patel devote a results section to it
[PMID:28602637 "Selective Binding of AcrIIA4 to sgRNA-bound SpyCas9"]
— so AcrIIA4 engages a ribonucleoprotein, not apo Cas9.

Contrast with AcrIIC1, which also inhibits Cas9 but leaves DNA binding intact
[PMID:28844692 "Both of these mechanisms are different from that of the anti-CRISPR protein AcrIIA4, which acts as a DNA mimetic that prevents DNA binding by occupying t"]
(truncated in cache at this point) — the two mechanism classes in the module (part 1
recognition blockade vs part 2 nuclease neutralisation) are distinguished in the primary
literature itself.

## Ontology gap

There is no GO molecular-function term for mimicry-based competitive inhibition. QuickGO
searches for "molecular mimicry" return only `GO:0140489 molecular template activity` and
the generic regulator terms; nothing for a protein that imitates a nucleic acid to occupy
its binding site. `GO:0043021 ribonucleoprotein complex binding` is *true* of AcrIIA4
(binding requires sgRNA-loaded Cas9) but says nothing about mimicry, and
`GO:0140721 nuclease inhibitor activity` is true but flattens the mechanism to generic
inhibition. A new term `nucleic acid mimicry-based competitive inhibitor activity` is
proposed under `GO:0140678 molecular function inhibitor activity`; it would serve
AcrIIA4, AcrIIA2 (`genes/9CAUD/acrIIA2`) and AcrF2/gp30 (`genes/BPD31/orf30`) at minimum.

## GOA qualifier adjudication

GOA (CACAO) holds one row: `acts_upstream_of_or_within_positive_effect GO:0098672`, IDA,
PMID:28041849. The term is right. The **qualifier is not well chosen**: AcrIIA4 does not
act upstream of the suppression process, it *is* the executing step — it binds Cas9
directly and the binding is the suppression. `involved_in` is the better-supported
qualifier, and `acts_upstream_of_or_within_positive_effect` additionally reads as though
AcrIIA4 positively regulated something, which inverts the sense for a reader skimming the
GAF. Same issue on A0A2D0TCG3 (`genes/NEIME/acrIIC1`). Flagged in `review.reason`;
the annotation itself is accepted.

## Scope note

AcrIIA4 is heavily used as a Cas9 "off-switch" reagent in human cells. That is a
laboratory application, not a biological function of the prophage gene, and is excluded
from the review's `description` and from all annotations.

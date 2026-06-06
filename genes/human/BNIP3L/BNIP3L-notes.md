# BNIP3L (NIX) curation notes

UniProt: O60238 (BNI3L_HUMAN). Synonyms: BNIP3A, BNIP3H, NIX, B5, NIP3L, BNIP3alpha.
219 aa, single-pass tail-anchored membrane protein. C-terminal transmembrane domain (FT TRANSMEM 188..208),
BH3 motif (FT MOTIF 126..148), large N-terminal disordered region (1..101).

## Core function synthesis

BNIP3L/NIX is an outer-mitochondrial-membrane, tail-anchored, atypical BH3-containing member of the
BNIP3/NIP3 family. Its best-supported, conserved function is as a **selective autophagy (mitophagy)
receptor**: it is anchored in the mitochondrial outer membrane via its C-terminal TM domain with the
N-terminus facing the cytosol, where an LIR (LC3-interacting region) motif binds the Atg8-family proteins
LC3 and GABARAP/GABARAPL1/GABARAPL2, tethering mitochondria to the forming autophagosome. This drives
programmed clearance of mitochondria, most strikingly during terminal erythroid/reticulocyte maturation,
and also during developmentally programmed and stress-induced mitochondrial turnover.

[PMID:20200478 "Nix is a mitochondrial outer membrane protein that is required for mitochondrial clearance during erythrocyte maturation. Recently, it was reported that Nix is a mitochondrial receptor that can directly connect to one of the autophagic machinery components, the Atg8 homologs LC3 and GABARAP."]

The UniProt IntAct interaction table directly records NIX binding to the human Atg8 orthologs GABARAPL1
(Q9H0R8), GABARAPL2 (P60520) and yeast ATG8 (P38182, Xeno), consistent with the LIR-dependent receptor model
(see BNIP3L-uniprot.txt INTERACTION block).

Historically NIX/BNIP3L was first described as a pro-apoptotic BCL-2/NIP3-family protein, but this is
context-dependent and atypical: NIX and BNIP3 do not act through classical cytochrome-c/caspase apoptosis.

[PMID:9973195 "Overexpression of BNIP3alpha in transfected cells results in apoptosis and suppresses the antiapoptosis activity of E1B-19K and BCL-xL. Like BNIP3, BNIP3alpha seems to be predominantly localized in mitochondria."]

[PMID:21264228 "in contrast to other mitochondrial Bcl-2 family proteins, NIX and BNIP3 are not involved in the release of cytochrome c and the resulting caspase-dependent apoptosis, but rather related to necrosis through the regulation of mitochondrial permeability transition pore (MPTP)"]

Notably, the original "B5"/BNIP3L paper found it does NOT itself induce apoptosis but rather inhibits
Nip3(BNIP3)-induced apoptosis, and localized it to nuclear envelope, ER and mitochondria:

[PMID:10381623 "B5 binds strongly to Nip3 and itself, weakly to E1B19K, but not to Bcl-2 and localizes in nuclear envelope, endoplasmic reticulum and mitochondria... Unlike other E1B19K binding BH3 proteins so far characterized, B5 does not induce apoptosis, but inhibits apoptosis induced by Nip3."]

This explains why both positive and negative regulation of apoptosis annotations exist in GOA; the
apoptotic role is genuine but secondary/contextual and direction-dependent, and is best treated as
non-core relative to mitophagy.

## Hypoxia / autophagy (survival)

Under hypoxia, HIF induces BNIP3 and BNIP3L; together they promote (macro)autophagy as a survival
mechanism, via their atypical BH3 domains disrupting the Bcl-2-Beclin1 complex, WITHOUT inducing cell death.

[PMID:19273585 "the combined silencing of these two HIF targets suppresses hypoxia-mediated autophagy... the atypical BH3 domains of hypoxia-induced BNIP3/BNIP3L have been designed to induce autophagy by disrupting the Bcl-2-Beclin1 complex without inducing cell death. Hypoxia-induced autophagy via BNIP3 and BNIP3L is clearly a survival mechanism"]

Note: the GOA IGI annotations to "negative regulation of programmed cell death", "positive regulation of
macroautophagy" and "cellular response to hypoxia" all trace to PMID:19273585 and are well supported.

## Mitochondrial quality control via SPATA18/MIEAP (MALM)

NIX interacts (via its BH3 domain) with SPATA18/Mieap (via coiled-coil) at the mitochondrial outer
membrane, in a ROS-dependent manner, and is required for MALM (Mieap-induced accumulation of lysosome-like
organelles within mitochondria), a non-canonical mitochondrial protein degradation/quality-control process.

[PMID:21264228 "A mitochondrial outer membrane protein NIX interacted with Mieap in a ROS-dependent manner via the BH3 domain of NIX and the coiled-coil domain of Mieap. Deficiency of NIX also completely impaired MALM."]

This is the source of the GOA "mitochondrial protein catabolic process" (GO:0035694, IMP) and
"mitochondrial outer membrane" (GO:0005741, IMP) annotations.

## Viral hijacking of NIX-mediated mitophagy (defense response to virus)

Multiple viruses hijack NIX-mediated mitophagy. SARS-CoV-2 ORF10 binds NIX (and LC3B) to drive mitophagy
and degrade MAVS, suppressing innate immunity; KSHV vIRF-1 likewise activates NIX-mediated mitophagy.

[PMID:34845370 "ORF10 was translocated to mitochondria by interacting with the mitophagy receptor Nip3-like protein X (NIX) and induced mitophagy through its interaction with both NIX and LC3B... NIX-mediated mitophagy is responsible for the elimination of spontaneously aggregated MAVS."]

The GOA "defense response to virus" (GO:0051607, IDA, PMID:9973195) actually traces to the 1999 BNIP3alpha
paper, which is about apoptosis/anti-apoptosis-protein interaction, not antiviral defense per se; the
modern antiviral connection is via mitophagy/MAVS turnover (PMID:34845370). The original PMID:9973195 does
not provide direct "defense response to virus" evidence, so that annotation is weakly supported by its
cited reference.

## Localization

UniProt subcellular location: Nucleus envelope; Endoplasmic reticulum; Mitochondrion outer membrane;
Membrane (single-pass). Colocalizes with SPATA18 at the mitochondrion outer membrane.
[file:human/BNIP3L/BNIP3L-uniprot.txt "SUBCELLULAR LOCATION: Nucleus envelope. Endoplasmic reticulum. Mitochondrion outer membrane. Membrane"]

The mitochondrial outer membrane is the core functional location. ER localization is reported (and linked
to Ca2+ handling in the Mieap-paper introduction) but is secondary. Nuclear envelope/lamin binding derives
from the original B5/PMID:10381623 study; nucleus / nuclear speck / nuclear envelope annotations are
weakly supported, likely reflecting the disordered N-terminus and the tail-anchor insertion behaviour, and
are not the core functional compartment for the mitophagy receptor role.

## Protein binding annotations

Numerous GO:0005515 "protein binding" and GO:0042802 "identical protein binding" IPI annotations come from
high-throughput interactome papers (16189514, 19060904, 21516116, 25416956, 25910212, 27107012, 28514442,
31515488, 32296183, 33961781, 24981860) and specific studies. "protein binding" is uninformative and is
marked as over-annotated. "identical protein binding"/homodimerization is genuine and informative (NIX
self-associates; UniProt: "Self-associates", IntAct O60238-O60238 NbExp=11; PMID:10381623 reports it
"binds... itself"); homodimerization is retained.

- PMID:10381623: NIX(B5) binds itself and Nip3/BNIP3 -> homodimerization / heterodimerization with BNIP3.
- PMID:22645275: ATP13A2 interactome (α-synuclein) - generic.
- PMID:24316735: TR3/NR4A1 (Nup4A1) autophagic cell death - NIX listed; the UniProt IntAct table records O60238-NR4A1.
- PMID:34845370: SARS-CoV-2 ORF10 (defense/mitophagy, informative for antiviral mitophagy not generic binding).
- PMID:21264221, 21264228: Mieap/SPATA18 (mitochondrial QC).

## Key existing annotation classification summary

CORE (mitophagy receptor / selective autophagy of mitochondria):
- regulation of mitophagy (GO:1901524)
- mitochondrial outer membrane (GO:0005741) localization
- positive regulation of macroautophagy (GO:0016239)
- regulation of protein localization to mitochondrion (GO:1903747)

SECONDARY / NON-CORE:
- apoptosis (positive and negative regulation), mitochondrial fragmentation in apoptosis
- cellular response to hypoxia, negative regulation of programmed cell death
- mitochondrial protein catabolic process (MALM / Mieap)
- defense response to virus
- mitochondrial membrane potential / permeability
- ER, nucleus, nuclear envelope, nuclear speck localizations (secondary/weak)

OVER-ANNOTATED / UNINFORMATIVE:
- protein binding (GO:0005515) - all instances

## Proposed new term
NIX/BNIP3L's defining molecular activity (LIR-dependent Atg8/LC3 binding as a mitophagy receptor) is not
captured by any existing annotation. Candidate: GO:0098780 "response to mitochondrial depolarisation" or
more precisely the molecular function for selective autophagy receptor activity. The most appropriate
existing molecular-function term is GO:0140311 "protein sequestering activity"? No — the canonical term is
mitophagy receptor activity. Existing process term GO:0000423 "mitophagy" (in UniProt DR but not in GOA
seeded set) and GO:1905037 "autophagosome organization" are relevant. I propose adding the molecular
function for the cargo-receptor/Atg8-binding role.
</content>

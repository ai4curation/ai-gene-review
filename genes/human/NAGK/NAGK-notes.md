# NAGK (Q9UJ70) — review notes

Human N-acetyl-D-glucosamine kinase (GlcNAc kinase), HGNC:17174, gene ID 55577, chromosome 2.
344 aa; homodimer; sugar kinase / Hsp70 / actin (ASKHA) superfamily,
"eukaryotic-type N-acetylglucosamine kinase family"
[file:human/NAGK/NAGK-uniprot.txt "Belongs to the eukaryotic-type N-acetylglucosamine kinase"].

## Core molecular function: N-acetylglucosamine kinase (EC 2.7.1.59)

NAGK phosphorylates free N-acetyl-D-glucosamine (GlcNAc) using ATP to make
GlcNAc 6-phosphate + ADP + H+ (Rhea:RHEA:17417; EC 2.7.1.59). This is the salvage
entry point of amino-sugar metabolism: GlcNAc released by endogenous glycoconjugate
turnover (lysosomal degradation, O-GlcNAc removal) or from diet is recycled back into
the hexosamine / UDP-GlcNAc pool.

- UniProt FUNCTION: "Converts endogenous N-acetylglucosamine (GlcNAc), a major
  component of complex carbohydrates, from lysosomal degradation or nutritional sources
  into GlcNAc 6-phosphate" [file:human/NAGK/NAGK-uniprot.txt].
- Catalytic activity (verbatim): "N-acetyl-D-glucosamine + ATP = N-acetyl-D-glucosamine 6-phosphate + ADP + H(+)"; EC=2.7.1.59; Evidence ECO:0000269|PubMed:22692205 [file:human/NAGK/NAGK-uniprot.txt].
- First cloning/characterization: "N-Acetylglucosamine is produced by the endogenous degradation of glycoconjugates and by the degradation of dietary glycoconjugates by glycosidases. It enters the pathways of aminosugar metabolism by the action of N-acetylglucosamine kinase." [PMID:10824116 "It enters the \npathways of aminosugar metabolism by the action of N-acetylglucosamine kinase"]. Recombinant enzyme "displays N-acetylglucosamine kinase activity as well as N-acetylmannosamine kinase activity" and is ubiquitously expressed [PMID:10824116].
- Direct IDA of GlcNAc kinase activity by recombinant human enzyme in the Neu5Gc study [PMID:22692205]; also assigns EC 2.7.1.59 (ECO:0000269).
- Structure: X-ray structures (PDB 2CH5/2CH6) of human NAGK with GlcNAc and ADP/glucose; homodimer; substrate-binding and ATP-binding residues mapped (Weihofen et al. 2006, PMID:17010375). SUBUNIT "Homodimer." [file:human/NAGK/NAGK-uniprot.txt].

## ManNAc kinase side activity (EC 2.7.1.60)

NAGK also phosphorylates N-acetyl-D-mannosamine (ManNAc). In UniProt the ManNAc
kinase reaction is By-similarity (ECO:0000250|UniProtKB:Q9QZ08 mouse), but the
original murine/human cloning paper reported both activities biochemically
[PMID:10824116 "N-acetylglucosamine kinase activity as well as N-acetylmannosamine \nkinase activity"]. GO:0009384 "N-acylmannosamine kinase activity" is a reasonable
(if imprecise) MF; N-acetylmannosamine metabolic process GO:0006051 is the BP.
Note: ManNAc-6-P from GNE/MNK is the canonical route to sialic acid biosynthesis;
NAGK's ManNAc activity is a secondary/salvage capacity.

## Amino-sugar / hexosamine salvage BP

Campbell et al. (eLife 2021) show glutamine deprivation in pancreatic cancer cells
raises free GlcNAc and engages NAGK to salvage it into the UDP-GlcNAc pool:
"GlcNAc salvage via N-acetylglucosamine kinase (NAGK) is engaged to feed UDP-GlcNAc pools"
and "NAGK deletion from PDA cells impairs tumor growth in mice" [PMID:34844667].
"GlcNAc salvage feeds UDP-GlcNAc pools" [PMID:34844667]. The paper is annotated by
FlyBase as IMP for GO:0006046 (GlcNAc catabolic), GO:0006048 (UDP-GlcNAc biosynthetic)
and GO:0045127 (kinase activity). NAGK-6-P is the product feeding the hexosamine
biosynthesis pathway at the GlcNAc-6-P node (downstream of / parallel to GNPNAT1).
The paper itself notes salvage "has been little studied, and the proportion of
UDP-GlcNAc generated via the NAGK-dependent salvage pathway is unknown" [PMID:34844667].

## Neu5Gc / N-acetylneuraminate degradation (Reactome)

Reactome R-HSA-6803771: "dimeric GlcNAc kinase (NAGK) to phosphorylate
N-acetylglucosamine (GlcNAc) to GlcNAc-6-phosphate and N-glycolylglucosamine (GlcNGc)
to GlcNGc-6-P". Humans lack Neu5Gc synthesis (inactive CMAHP) but ingest it and must
degrade it; NAGK acts in this degradation branch [reactome R-HSA-6803771;
PMID:22692205 abstract]. This is why GO:0019262 "N-acetylneuraminate catabolic process"
is annotated (TAS to PMID:22692205). This is a real but relatively narrow, context-specific
role — the direct catalytic step is GlcNAc/GlcNGc phosphorylation.

## Moonlighting innate-immunity role: MDP phosphorylation → NOD2 (EC 2.7.1.-)

Stafford et al. (Nature 2022) identified NAGK in a forward genetic screen as essential
for MDP sensing. NAGK directly phosphorylates the muramyl dipeptide (MDP) MurNAc C6
hydroxyl to make 6-O-phospho-MDP, which is the actual NOD2 agonist:
- "NAGK functions upstream of NOD2 by directly" ... phosphorylating MurNAc of MDP [PMID:36002575].
- "constitutes an agonist for NOD2" (NAGK-phosphorylated, not unmodified, MDP) [PMID:36002575].
- In vitro: "we expressed recombinant human NAGK in E. coli and used it in an in vitro kinase assay with various substrates"; "NAGK readily phosphorylated MDP and the related molecule N-acetylmuramic acid" [PMID:36002575].
- Catalytic dependence: "a mutant NAGK(D107V) construct, which is predicted to disrupt enzyme activity13, did not rescue NOD2 signalling in NAGK-deficient cells" [PMID:36002575]; matches UniProt MUTAGEN D107V "Abolished ability to phosphorylate muramyl dipeptide."
- Knockout: "completely deficient in MDP sensing" [PMID:36002575].
This supports GO:0160047 muramyl dipeptide kinase activity (IDA), GO:0032495 response to
muramyl dipeptide (IDA), GO:0042742 defense response to bacterium (IDA), and
GO:0070434 positive regulation of NOD2 signaling pathway (IDA). UniProt captures this as
EC 2.7.1.- and additional AltName "Muramyl dipeptide kinase". This is a genuine, distinct
biological role but is a moonlighting/immunity function; the enzymatic step (sugar-6-OH
phosphorylation) is mechanistically the same kinase chemistry.

## Kinase-independent moonlighting: dynein-mediated dendrite/axon branching

Timalsina et al. (2023) report NAGK acts as a non-canonical structural/anchor protein
that, via interaction with SNRPN and the dynein light chain DYNLRB1, promotes
axodendritic branching through dynein-mediated microtubule transport
[PMID:37511433 "N-acetylglucosamine kinase (NAGK) has been identified as an anchor protein that \nfacilitates neurodevelopment with its non-canonical structural role"]. This is the basis
for the SNRPN (P63164) IntAct annotation. This role is developmental / neuron-specific and
non-core; the associated GO:0005515 IPI is a bare protein-binding capture.

## Localization

Cytosolic (TAS Reactome, GO:0005829). Also detected in urinary extracellular exosomes by
mass spec [PMID:19056867 "urinary exosomes"] — an HDA proteomics capture (GO:0070062),
non-core; exosome/secretome MS commonly detects abundant cytosolic enzymes.

## Protein-binding (IPI) annotations

GO:0005515 (protein binding) annotations come from large interactome / Y2H / MS screens:
PMID:16189514 (CCSB HI-1), PMID:21516116 (NGS interactome), PMID:25416956 (HI-II-14),
PMID:29892012, PMID:31515488, PMID:37511433 (SNRPN). These are uninformative bare
"protein binding" captures. Per policy, IPI protein-binding is not REMOVEd; mark as
over-annotated (KEEP context in notes). None of these interactors define NAGK's core
molecular function.

## Summary of core vs non-core

- CORE MF: N-acetylglucosamine kinase activity (GO:0045127); ATP binding (GO:0005524).
- CORE BP: N-acetylglucosamine metabolic process (GO:0006044) / GlcNAc catabolic
  (GO:0006046) / UDP-GlcNAc biosynthetic salvage (GO:0006048) — the hexosamine salvage role.
- CORE-ish MF: muramyl dipeptide kinase activity (GO:0160047) — same chemistry, immunity context.
- Non-core / context-specific: NOD2 signaling & bacterial defense (immunity moonlight);
  Neu5Gc degradation (narrow); ManNAc kinase (secondary); dynein/dendrite (kinase-independent);
  exosome localization (proteomics); all protein-binding IPI (uninformative).

## Isoforms

Two isoforms: Q9UJ70-1 (canonical, MANE) and Q9UJ70-2 (VSP_044586, N-terminal extension
from alternative splicing). No isoform-specific function established; annotations are on the
gene/canonical enzyme.

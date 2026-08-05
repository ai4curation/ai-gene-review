# GNPNAT1 (GNA1) review notes

UniProt: Q96EK6 (GNA1_HUMAN). HGNC:19980. Gene ID 64841. Chromosome 14. 184 aa.

## Identity and core enzymatic function

GNPNAT1 (synonym GNA1) is **glucosamine 6-phosphate N-acetyltransferase**, EC 2.3.1.4
[file:human/GNPNAT1/GNPNAT1-uniprot.txt "RecName: Full=Glucosamine 6-phosphate N-acetyltransferase" / "EC=2.3.1.4"].
It catalyzes the acetyl-CoA-dependent acetylation of D-glucosamine 6-phosphate to
N-acetyl-D-glucosamine 6-phosphate (GlcNAc-6-P), the **second committed step of the
hexosamine biosynthetic pathway (HBP)**:

> Reaction=D-glucosamine 6-phosphate + acetyl-CoA = N-acetyl-D-glucosamine 6-phosphate + CoA + H(+)
[file:human/GNPNAT1/GNPNAT1-uniprot.txt "Reaction=D-glucosamine 6-phosphate + acetyl-CoA = N-acetyl-D-"].

UniProt PATHWAY: "Nucleotide-sugar biosynthesis; UDP-N-acetyl-alpha-D-glucosamine
biosynthesis; N-acetyl-alpha-D-glucosamine 1-phosphate from alpha-D-glucosamine
6-phosphate (route I): step 1/2." So this is step 1 of a 2-step route within UDP-GlcNAc
biosynthesis (GNPNAT1 = HBP step 2 overall, after GFPT1/GFAT).

Belongs to the acetyltransferase family, GNA1 subfamily; contains a GNAT
(GCN5-related N-acetyltransferase) domain (residues 39-184)
[file:human/GNPNAT1/GNPNAT1-uniprot.txt "Belongs to the acetyltransferase family. GNA1 subfamily"].

## Structural / kinetic evidence (experimental, EXP)

- PMID:18601654 (Hurtado-Guerrero et al., Biochem J 2008; abstract-only in cache):
  crystal structures of human and A. fumigatus GNA1 with kinetic characterization.
  "GNA1 (D-glucosamine-6-phosphate N-acetyltransferase) catalyses the acetylation of
  GlcN-6P (glucosamine-6-phosphate) to GlcNAc-6P (N-acetylglucosamine-6-phosphate), a
  key intermediate in the UDP-GlcNAc biosynthetic pathway." UniProt records this as the
  EC 2.3.1.4 CATALYTIC ACTIVITY evidence and gives KM = 26 uM (acetyl-CoA), 97 uM
  (GlcN6P). Basis of GO:0004343 EXP annotation.
- PMID:18675810 (Wang et al., FEBS Lett 2008; abstract-only in cache): crystal
  structures of apo GNA1, GNA1-GlcN6P complex, and E156A mutant.
  "GNA1 catalyzes the formation of N-acetylglucosamine-6-phosphate (GlcNAc6P) from
  acetyl-CoA (AcCoA) and the acceptor substrate GlcN6P." Establishes acceptor-substrate
  binding and role of Glu156. Basis of the second GO:0004343 EXP annotation and of the
  GO:0042802 (identical protein binding) self-interaction annotation.

Both papers, plus UniProt SUBUNIT "Homodimer" [file:human/GNPNAT1/GNPNAT1-uniprot.txt
"SUBUNIT: Homodimer."], support that the active enzyme is a homodimer. This grounds the
GO:0042802 identical protein binding annotations (self-interaction, WITH/FROM Q96EK6).

## Subcellular location

UniProt SUBCELLULAR LOCATION: "Golgi apparatus membrane; Peripheral membrane protein.
Endosome membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}."
[file:human/GNPNAT1/GNPNAT1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane; Peripheral membrane"].
Note the endosome-membrane location is by similarity (ECO:0000250), not direct.
Reactome R-HSA-449734 places the catalytic reaction in the **cytosol**: "Cytosolic
GNPNAT1 catalyzes the reaction of glucosamine 6-phosphate and acetyl-CoA to form
N-acetyl-glucosamine 6-phosphate (GlcNAc6P) and CoA-SH." The HBP is a cytosolic pathway,
so cytosol/cytoplasm is the functionally central location; the Golgi/endosome membrane
associations are peripheral-membrane and (for endosome) by-similarity.

## Interactions (protein binding annotations)

UniProt INTERACTION lists FABP1 (P07148), self (Q96EK6, homodimer), and PSMB8
(P28062-2). The bare `protein binding` (GO:0005515) IPI annotations come from
high-throughput proteome-scale interactome maps:
- PMID:28514442 "Architecture of the human interactome defines protein communities and
  disease networks" (BioPlex-type AP-MS), WITH/FROM P07148 (FABP1).
- PMID:32296183 "A reference map of the human binary protein interactome" (HuRI Y2H),
  WITH/FROM P28062-2 (PSMB8).
- PMID:33961781 "Dual proteome-scale networks reveal cell-specific remodeling of the
  human interactome" (BioPlex 3.0 AP-MS), WITH/FROM P07148 (FABP1).
These are uninformative for molecular function (per curation policy, avoid bare protein
binding) and are best marked as over-annotated rather than removed (they are IPI/experimental).

The GO:0042802 identical protein binding IPIs (PMID:18675810 crystallography;
PMID:25416956 HuRI/interactome) reflect the biologically meaningful homodimer and are
informative in that context.

## Disease

UniProt DISEASE: "Rhizomelic dysplasia, Ain-Naz type (RHZDAN) [MIM:619598]: An autosomal
recessive skeletal dysplasia characterized by short stature, marked rhizomelic
shortening of the limbs, platyspondyly, hip dysplasia, and large hands and feet relative
to height." Variant E76K (VAR_086302). Reference PMID:32591345 (Ain et al., J Med Genet
2021). This is the first reported human disease from GNPNAT1 loss of function and is
consistent with HBP/UDP-GlcNAc deficiency (a CDG-like glycosylation disorder). PMID not
in existing_annotations (no GO annotation attached to it), so it is not a review target,
but supports the biological description.

## GO term id verification (QuickGO 2026-07)

- GO:0004343 glucosamine 6-phosphate N-acetyltransferase activity — MF, not obsolete ✓ (core MF)
- GO:0006048 UDP-N-acetylglucosamine biosynthetic process — BP, not obsolete ✓ (core BP)
- GO:0005829 cytosol — CC, not obsolete ✓ (core location)
- GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups — MF, not obsolete (parent/general)
- GO:0005737 cytoplasm — CC, not obsolete
- GO:0000139 Golgi membrane — CC, not obsolete
- GO:0010008 endosome membrane — CC, not obsolete

## Curation summary of actions

- GO:0004343 (MF): ACCEPT (both EXP; IBA; and IEA all correct core function).
- GO:0006048 (BP): ACCEPT (correct core biosynthetic process; matches UniPathway).
- GO:0005829 cytosol (TAS, Reactome): ACCEPT (functionally central HBP compartment).
- GO:0005737 cytoplasm (IEA/ARBA): KEEP_AS_NON_CORE (general parent of cytosol; correct but redundant/less specific).
- GO:0016747 (MF, IEA/InterPro): MARK_AS_OVER_ANNOTATED (general GNAT parent; GO:0004343 is the specific term).
- GO:0000139 Golgi membrane (IEA/SubCell): KEEP_AS_NON_CORE (peripheral membrane association; not the catalytic compartment).
- GO:0010008 endosome membrane (IEA/SubCell): KEEP_AS_NON_CORE (by-similarity peripheral association).
- GO:0005515 protein binding x3 (IPI, HT interactome): MARK_AS_OVER_ANNOTATED (uninformative bare binding; do not REMOVE — IPI/experimental).
- GO:0042802 identical protein binding x2 (IPI): KEEP_AS_NON_CORE (real homodimer, but supports MF rather than being a core function in its own right).

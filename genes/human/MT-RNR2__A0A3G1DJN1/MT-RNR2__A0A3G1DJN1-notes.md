# SHLP6 (A0A3G1DJN1) - curation notes

## Shared context: the MT-RNR2 sORF peptides

Humanin and SHLP1-6 are seven separate UniProt entries whose ORFs all lie inside
MT-RNR2, the mitochondrial 16S rRNA gene. UniProt files all seven under the host
symbol `MT-RNR2`, so this repo uses the `<HOST>__<ACC>` folder convention
(CLAUDE.md, "Alternative-ORF peptides"). The SHLPs were found by in silico search
of the humanin-containing region [PMID:27070352 "An in silico search revealed six
additional peptides in the same region of mtDNA as humanin; we named these
peptides small humanin-like peptides (SHLPs)"] - they share a genomic
neighbourhood with humanin, not sequence similarity.

The founding study detected five of the six by immunoblot in mouse tissues
[PMID:27070352 "Multiple mouse tissues expressed SHLPs 1-4 and 6 at varying
levels"] with organ-specific patterns [PMID:27070352 "Specifically, SHLP1 was
detected in the heart, kidney, and spleen; SHLP2 was detected in the liver,
kidney, and muscle; SHLP3 was detected in the brain and spleen; SHLP4 was
detected in the liver and prostate; and SHLP6 was detected in the liver and
kidney"], and could not raise an antibody against SHLP5 [PMID:27070352 "Despite
multiple attempts, we were unable to obtain a specific antibody against SHLP5"].
Phenotypes were assigned with synthetic peptides at 100 nM: SHLP2 and SHLP3 were
cytoprotective [PMID:27070352 "SHLP2 and SHLP3 enhanced cell viability (Fig. 2A)
and decreased apoptosis in both NIT-1 and 22Rv1 cells"], SHLP2 and SHLP4
proliferative [PMID:27070352 "SHLP2 and SHLP4 promoted cell proliferation in
NIT-1 beta-cells"], and SHLP6 pro-apoptotic [PMID:27070352 "SHLP6 significantly
increased apoptosis in both NIT-1 and 22Rv1 cells (Fig. 2B), having an effect
opposite of SHLP2 and SHLP3"]. SHLP1 had no assigned phenotype.

Two caveats apply to all seven entries. The peptides are read with the
cytoplasmic genetic code although the locus is mitochondrial, and no export route
for an mtDNA-encoded transcript or a matrix-made peptide has been demonstrated.
And the same mtDNA region exists in the nuclear genome as MT-RNR2-like (NUMT)
copies, so antibody-based detection cannot be assigned to the mitochondrial locus
with certainty. All but SHLP2 are UniProt PE4 (predicted).


## What is known about SHLP6 specifically

The only SHLP with an opposite-sign phenotype: [PMID:27070352 "SHLP6
significantly increased apoptosis in both NIT-1 and 22Rv1 cells (Fig. 2B), having
an effect opposite of SHLP2 and SHLP3"]. 20 residues, the shortest of the group.
Detected in mouse liver and kidney. No receptor, partner, structure or location;
no follow-up publication.

## Decisions

- Zero GOA rows, no NEW terms. A short synthetic peptide that kills two unrelated
  cell lines at 100 nM is as consistent with membrane perturbation as with
  receptor-mediated apoptosis, and the founding study includes no
  sequence-scrambled or membrane-integrity controls that would separate them.
  Proposing "positive regulation of apoptotic process" would assert a signalling
  activity the data do not establish.
- The experiments section asks for exactly those controls.

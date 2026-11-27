# SHLP2 (A0A3G1DIU6) - curation notes

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


## What is known about SHLP2 specifically

The only SHLP with mechanism. Three independent arms:

**Receptor ligand (ACKR3/CXCR7).** [PMID:37468558 "Through high-throughput
structural complementation screening, we discovered that SHLP2 binds to and
activates chemokine receptor 7 (CXCR7)"]; [PMID:37468558 "Out of the screened
GPCR candidates, SHLP2 showed the highest efficiency in recruiting beta-Arrestin
to the chemokine receptor CXCR7 (previously known as ACKR3)"]; direct binding
[PMID:37468558 "Additionally, the SHLP2 binds directly to CXCR7, as evidenced by
the detection of tagged CXCR7 through pulldown analysis"]; and a physiological
output [PMID:37468558 "These results strongly suggest that SHLP2 directly
activates POMC neurons while marginally inhibiting AgRP/NPY neurons"].

**Chaperone-like / misfolded-seed binding.** [PMID:28798389 "Seeded fluorescence
and co-sedimentation studies demonstrate MDPs block amyloid seeding and directly
bind misfolded, seeding-capable IAPP species"], with the conformer selectivity
controlled [PMID:28798389 "Furthermore, our electron paramagnetic resonance
spectroscopy and circular dichroism data indicate MDPs do not act by binding IAPP
monomers"].

**Mitochondrial inner membrane and complex I.** [PMID:38167865 "with a custom
antibody against full length SHLP2, SHLP2 is enriched in the mitochondria
fraction, but not the cytoplasmic fraction"]; [PMID:38167865 "These results
suggest the localization of SHLP2 is in the inner mitochondrial membrane"];
[PMID:38167865 "these associations align with our experimental data showing SHLP2
interaction with mitochondrial complex 1"]. Three orthogonal methods
(fractionation, Na2CO3 extraction, APEX2 topology), which is better localisation
evidence than most microproteins have.

Phenotypic context: AMD cell-model protection [PMID:30310092 "we examined the
biological consequences of treatment with exogenously-added SHLP2 in an in vitro
human transmitochondrial age-related macular degeneration (AMD) ARPE-19 cell
model"]. The m.2158T>C (K4R) Parkinson claim of PMID:38167865 is disputed by
PMID:38940474 and is not used for any annotation.

## Decisions

- All four GOA rows (extracellular region EXP+IEA, mitochondrial inner membrane
  EXP+IEA) ACCEPT.
- Three NEW terms, each passing the participation test with SHLP2 itself doing the
  step: GO:0048018 receptor ligand activity (binds and activates CXCR7),
  GO:0051787 misfolded protein binding (binds the misfolded IAPP conformer, not
  the monomer), GO:1905907 negative regulation of amyloid fibril formation (the
  process counterpart; comparator check passes - humanin carries GO:1905907 twice
  by IDA for the equivalent amyloid-beta result).
- Deliberately NOT proposed: the downstream cytoprotective phenotypes (apoptosis,
  ROS, OXPHOS subunit stabilisation, glucose handling, food intake), because for
  each of those the step is executed by something else and SHLP2's contribution is
  necessity, not participation. Also not proposed: a complex I assembly or
  enzyme-regulator term - proximity labelling places SHLP2 next to complex I but no
  effect on assembly or activity has been measured.
- GO:0051082 unfolded protein binding was obsoleted without a direct replacement,
  so GO:0051787 misfolded protein binding is used rather than inventing a holdase
  term; no holdase cycle was demonstrated, only seed binding.
- The secreted-versus-inner-membrane tension is the most interesting open question
  on this entry and is recorded as such rather than resolved.

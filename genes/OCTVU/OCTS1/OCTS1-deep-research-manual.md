# OCTS1 (S-crystallin 1) - Deep Research Summary

## Gene Identity

- **UniProt:** P27013 (Swiss-Prot, reviewed)
- **Gene symbol:** OCTS1
- **Organism:** *Octopus vulgaris* (Common octopus), NCBI Taxon:6645
- **Protein name:** S-crystallin 1
- **Length:** 214 amino acids, 25.3 kDa
- **Accession:** EMBL X65543 (mRNA)
- **Classification:** GST superfamily, S-crystallin family

## Structural Features

### Domain Architecture

OCTS1 has a bipartite domain structure characteristic of glutathione S-transferases:
- **GST N-terminal domain** (residues 2-79): Contains the thioredoxin-like fold with the glutathione (GSH) binding site (G-site)
- **GST C-terminal domain** (residues 81-214): All-helical domain containing the hydrophobic substrate binding site (H-site)

### Crystal Structure of Octopus S-crystallin (PDB: 5B7C)

Tan et al. (2016) solved the crystal structure of the Q108F mutant of an *O. vulgaris* S-crystallin (OctS4) in complex with GSH at 2.35 Angstrom resolution [PMID:27499004, "We determined the crystal structure of the S-crystallin Q108F mutant at 2.35 A resolution"]. Key structural findings:

- **Quaternary structure:** S-crystallin forms a homodimer via crystallographic 2-fold symmetry, burying approximately 1600 square Angstrom of surface area per monomer (vs 1300 square Angstrom for squid GST-sigma) [PMID:27499004]
- **GSH binding:** A GSH molecule sits in the active site between the N- and C-domains, with a disulfide bond between GSH thiol and Cys112 of S-crystallin [PMID:27499004]
- **Polar interaction network:** The glutamyl group of GSH interacts with Arg14, Gln64, Ser65, and Tyr97; the cysteinyl group with Met51; and the glycinyl group with His49 and Gly110 [PMID:27499004]
- **Closed conformation:** Compared to GST-sigma, S-crystallin has a more closed active center due to the 11-residue insertion between alpha4 and alpha5 helices (the "long loop"), which shields the active site and explains the failure of S-crystallin to bind immobilized glutathione in affinity chromatography [PMID:9929473]
- **Collapsed H-site pocket:** Key hydrophobic residues in the H-site of GST (Phe98, Val102, Phe106) are mutated to Leu100, Met104, Gln108 in S-crystallin, collapsing the pocket that normally binds electrophilic substrates [PMID:27499004]

### Homology Model

Before the crystal structure was available, Chuang et al. (1999) constructed a homology model based on squid sigma-class GST, revealing that the S-crystallin active center is more buried after dimerization, and that mutation of Asn99 (GST) to Asp101 (S-crystallin) alters the electrostatic environment at the active site [PMID:9929473].

## Primary Function

### Structural Lens Protein

S-crystallin 1 is a structural constituent of the cephalopod eye lens. It is one member of a large family of S-crystallins that collectively constitute the major soluble protein mass of the lens, contributing to lens transparency and refractive power [PMID:8587103, "S-crystallins are structural components of squids and octopi eye lens"].

### Residual GST Activity

OCTS1 retains only approximately 1/1000 of the GST enzymatic activity of authentic digestive gland GST when tested with the standard substrate 1-chloro-2,4-dinitrobenzene (CDNB) [UniProt, PMID:8827456]. The catalytic constant (kcat) for wild-type S-crystallin is 0.24 per second, which is approximately 1/700 of that of GST-sigma and approximately 1/6000 in terms of catalytic efficiency (kcat/Km,CDNB) [PMID:27499004]. The kinetic mechanism conforms to a steady-state random Bi-Bi mechanism similar to authentic GSTs, and Tyr7 interacts with bound GSH to lower the pKa of the sulfhydryl group (to 6.82-6.85), but the overall catalytic efficiency is drastically reduced [PMID:8827456].

### GSH Binding for Protein Stability

A key finding from Tan et al. (2016) is that S-crystallin preferentially binds GSH to enhance its own stability rather than for catalysis. GSH binding increases the melting temperature (Tm) of S-crystallin by 7 degrees Celsius and prevents denaturant-induced aggregation in a dose-dependent manner [PMID:27499004, "S-crystallin is stabilized by glutathione binding to prevent its aggregation; this contrasts with GST-sigma, which do not possess this protection"]. This is significant because GSH is abundant in animal lenses (2-10 mM) [PMID:27499004], and this binding may protect S-crystallin from the aggregation that causes cataracts.

## Biological Role

### Refractive Index Gradient in Cephalopod Lens

Cephalopod lenses have a graded refractive index that follows a parabolic relationship between lens radius and refractive index, allowing the spherical lens to avoid spherical aberration [PMID:28798124]. S-crystallins are differentially expressed in a radial gradient, with different family members present at different concentrations from the lens periphery to the center [PMID:17293312, "S-crystallins are differentially expressed in a radial gradient, suggesting a role in refractive index"].

Cai et al. (2017) demonstrated using small-angle X-ray scattering that S-crystallins form colloidal gels at all radial positions in the squid lens. The disordered loops protruding from the protein surface (including the "long loop" insertion between alpha4 and alpha5) serve as low-valence linkers for self-assembly into volumetric materials. Peripheral lens regions with low particle valence form stable gels at low density, while central regions with higher valence gel at higher densities [PMID:28798124, "patchy colloidal physics resulted from an evolutionary radiation of globular S-crystallin proteins"].

Recent ultrastructural studies using synchrotron X-ray scattering on squid lenses revealed that an extensive network of membrane-like structures forms a substantial component of both anterior and posterior lens segments, with the posterior segment possessing a noticeably higher refractive index gradient [PMID:39133170].

### Polymerization Properties

Chang et al. (2000) characterized the polymerization behavior of octopus lens S-crystallin, showing that it aggregates more easily than sigma-GST in the presence of denaturants. The proposed molecular model involves side-by-side associations of Lys-208 from one protomer with a complementary patch of aspartate residues (Asp-90, Asp-94, Asp-101, Asp-102, Asp-179, Asp-180) from another protomer, potentially forming a liquid crystal structure in the lens [PMID:10733985].

## S-Crystallin Gene Family

### Family Size and Diversity

The S-crystallin family is much larger than initially appreciated:
- **Squid *Loligo opalescens*:** At least 24 different S-crystallins, 46-99% identical at the amino acid level [PMID:8587103]
- **Squid *Ommastrephes sloani pacificus*:** At least 10 members [PMID:8587103]
- **Octopus *O. vulgaris*:** At least 4 characterized members (3 isoforms cloned by Chiou et al. 1995) plus the ancestral GST [PMID:7639695]

### Short-Loop vs Long-Loop S-Crystallins

S-crystallins divide into two functional groups:

1. **Short-loop S-crystallins** (SL11, LopS4, Cry9): Lack the central peptide insertion; expressed at lower levels in the lens; retain some GST activity; considered the earliest descendants from the ancestral GST gene [PMID:8587103, "SL11 and Lops4 have some enzymatic activity with the CDNB substrate"]

2. **Long-loop S-crystallins** (the majority, including abundant lens forms): Contain a variable-length inserted peptide between alpha4 and alpha5 helices; dominantly expressed in the lens; enzymatically inactive [PMID:8587103, "SL20-1 of O. pacificus and Lops12 of L. opalescens (which are encoded by abundant lens mRNAs) have no GST activity"]

OCTS1 is a long-loop S-crystallin with the central peptide insertion.

## Evolutionary Context

### Gene Recruitment (Enzyme Co-option)

S-crystallins represent a textbook example of "gene sharing" or enzyme co-option, where a housekeeping enzyme is recruited as a structural lens protein [PMID:8587103, PMID:7987197]. This parallels cases in vertebrates where alpha-crystallin is related to small heat-shock proteins, delta-crystallin to argininosuccinate lyase, and eta-crystallin to aldehyde dehydrogenase [PMID:7987197].

### Mechanisms of Activity Loss

Three mechanisms contributed to the evolutionary loss of GST activity in S-crystallins [PMID:8587103, PMID:27499004]:

1. **Gradual sequence drift:** Mutations at active site residues including the catalytically important Tyr7 and Trp38, and changes in the H-site residues (Phe98->Leu100, Val102->Met104, Phe106->Gln108) that collapse the electrophilic substrate binding pocket

2. **Insertion of the central peptide:** Exon shuffling introduced a loop between alpha4 and alpha5 helices that enhances GSH binding but interferes with electrophilic substrate access. The insertion alone reduced GST activity by 30-100-fold [PMID:8587103]

3. **Active site charge changes:** The mutation of Asn99 (GST) to Asp101 (S-crystallin) introduces a charge-charge interaction with Arg14 that diminishes the ability to stabilize the negatively charged Meisenheimer complex intermediate during catalysis [PMID:27499004]

### Evolutionary Trajectory Reconstruction

Tan et al. (2016) experimentally reconstructed the evolutionary trajectory by creating "GST-like" S-crystallin mutants. The quadruple mutant L100F/D101N/M104V/Q108F showed a 518-fold increase in catalytic efficiency and a switch in substrate-binding affinity (increased Km,GSH, decreased Km,CDNB), essentially producing a "reverse-evolved" S-crystallin with recovered GST function [PMID:27499004]. Conversely, a "S-crystallin-like" GST was created by the reciprocal quadruple mutation plus long-loop insertion, which showed a 120-fold reduction in catalytic activity [PMID:27499004].

### Evolutionary Driving Force

The authors propose that a tradeoff between enzyme activity and protein stability was the major driving force behind S-crystallin evolution: in the lens, it is advantageous for the protein to capture and retain GSH (for stability/anti-aggregation) while minimizing catalytic turnover that would release GSH as a product conjugate [PMID:27499004, "a tradeoff between enzyme activity and the stability of the lens protein might have been one of the major driving force behind lens evolution"].

### Positive Selection

Sweeney et al. (2007) showed that S-crystallins have been under positive selection, with selection appearing to result in stabilization of derived S-crystallins via mutations in the dimer interface and extended electrostatic fields, producing the glassy organization and stability required for low refractive index lens layers [PMID:17293312].

## Key References

1. **Tomarev SI, Chung S, Piatigorsky J (1995).** Glutathione S-transferase and S-crystallins of cephalopods: evolution from active enzyme to lens-refractive proteins. *J Mol Evol* 41:1048-56. [PMID:8587103] -- Definitive study on the S-crystallin family: 24 members in squid, activity loss mechanisms (sequence drift + exon shuffling), identification of short-loop crystallins as ancestral forms.

2. **Tan WH et al. (2016).** Structure of a Highly Active Cephalopod S-crystallin Mutant: New Molecular Evidence for Evolution from an Active Enzyme into Lens-Refractive Protein. *Sci Rep* 6:31176. [PMID:27499004] -- Crystal structure of S-crystallin-GSH complex (PDB: 5B7C), GSH-mediated stability, and experimental reconstruction of the evolutionary trajectory.

3. **Chiou SH et al. (1995).** Octopus S-crystallins with endogenous glutathione S-transferase (GST) activity: sequence comparison and evolutionary relationships with authentic GST enzymes. *Biochem J* 309:793-800. [PMID:7639695] -- Cloning and characterization of three octopus S-crystallin isoforms with low endogenous GST activity.

4. **Tang SS, Chang GG (1996).** Kinetic characterization of the endogenous glutathione transferase activity of octopus lens S-crystallin. *J Biochem* 119:1182-8. [PMID:8827456] -- Detailed kinetics of S-crystallin's residual GST activity.

5. **Chuang CC et al. (1999).** Homology modeling of cephalopod lens S-crystallin: a natural mutant of sigma-class glutathione transferase with diminished endogenous activity. *Biophys J* 76:679-90. [PMID:9929473] -- Structural basis for loss of GST activity from homology modeling.

6. **Chang HC, Lin TL, Chang GG (2000).** Molecular basis for the polymerization of octopus lens S-crystallin. *Biophys J* 78:2070-80. [PMID:10733985] -- Polymerization behavior and proposed liquid crystal model for lens organization.

7. **Cai J et al. (2017).** Eye patches: Protein assembly of index-gradient squid lenses. *Science* 357:564-569. [PMID:28798124] -- S-crystallin colloidal gel self-assembly produces the refractive index gradient.

8. **Sweeney AM et al. (2007).** Evolution of graded refractive index in squid lenses. *J R Soc Interface* 4:685-98. [PMID:17293312] -- Positive selection on S-crystallins and their role in the refractive index gradient.

9. **Regini JW et al. (2024).** Membrane structures and functional correlates in the bi-segmented eye lens of the cephalopod. *Biol Open* 13(9). [PMID:39133170] -- Ultrastructural analysis of cephalopod lens with refractive index gradient.

10. **Tang SS, Lin CC, Chang GG (1994).** Isolation and characterization of octopus hepatopancreatic glutathione S-transferase. Comparison of digestive gland enzyme with lens S-crystallin. *J Protein Chem* 13:609-18. [PMID:7702742] -- Comparison of authentic octopus GST with lens S-crystallin.

11. **Tomarev SI, Zinovieva RD, Piatigorsky J (1992).** Characterization of squid crystallin genes. Comparison with mammalian glutathione S-transferase genes. *J Biol Chem* 267:8604-12. [PMID:1373730] -- Gene structure of squid S-crystallins, exon-intron organization, promoter analysis.

12. **Lin CW, Chiou SH (1992).** Facile cloning and sequencing of S-crystallin genes from octopus lenses based on polymerase chain reaction. *Biochem Int* 27:173-8. [PMID:1627174] -- Original cloning of octopus S-crystallin cDNAs including OCTS1.

13. **Zinov'eva RD, Tomarev SI, Piatigorsky J (1994).** [The evolutionary kinship of the crystallins of cephalopods and vertebrates with heat-shock proteins and stress-induced proteins]. *Izv Akad Nauk Ser Biol* (4):566-76. [PMID:7987197] -- Review of convergent evolution between cephalopod and vertebrate crystallins.

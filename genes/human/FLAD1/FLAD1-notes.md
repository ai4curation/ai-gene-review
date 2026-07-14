# FLAD1 (Q8NFF5) — Gene Review Notes

## Identity and summary

FLAD1 encodes human FAD synthase (FMN adenylyltransferase; FMNAT; FADS; EC 2.7.7.2),
the enzyme that catalyzes the **final, committed step of FAD-cofactor biosynthesis**:
adenylylation of flavin mononucleotide (FMN) with ATP to yield flavin adenine
dinucleotide (FAD) plus diphosphate. FAD is the cofactor of hundreds of flavoenzymes
(respiratory chain Complex I/II, acyl-CoA dehydrogenases, MTHFR, dimethylglycine
dehydrogenase, monoamine oxidase, etc.). The reaction requires a divalent metal,
optimally Mg2+.

[file:human/FLAD1/FLAD1-uniprot.txt "FAD synthase catalyzes the adenylation of flavin mononucleotide (FMN) to form flavin adenine dinucleotide (FAD) coenzyme"]
[file:human/FLAD1/FLAD1-uniprot.txt "Reaction=FMN + ATP + H(+) = FAD + diphosphate"]
[PMID:16643857 "FAD synthetase (FADS) (EC 2.7.7.2) is a key enzyme in the metabolic pathway that converts riboflavin into the redox cofactor FAD"]
[PMID:16643857 "Both isoforms possessed FADS activity and had a strict requirement for MgCl(2)"]

The human enzyme is **bifunctional and multidomain**, distinguishing it from the
single-domain yeast Fad1p:
- **C-terminal PAPS-reductase domain (FADSy; ~residues 355-587)** = the FAD-forming
  catalytic (FMN adenylyltransferase) domain.
- **N-terminal molybdopterin-binding-resembling (MPTb) domain (with a KH domain)** =
  a **FAD hydrolase / FAD diphosphatase (FADHy)** activity (EC 3.6.1.18), and, at lower
  efficiency, an NADH diphosphatase / NADH pyrophosphatase activity (EC 3.6.1.22).

[file:human/FLAD1/FLAD1-uniprot.txt "This enzyme has two activities: FAD diphosphatase activity"]
[file:human/FLAD1/FLAD1-uniprot.txt "In the N-terminal section; belongs to the MoaB/Mog family"]
[file:human/FLAD1/FLAD1-uniprot.txt "In the C-terminal section; belongs to the PAPS reductase"]
[PMID:26277395 "The recombinant hFADS2 was able to hydrolyse added FAD in a Co(2+) and mersalyl dependent reaction"]
[PMID:38688286 "the combination of the N-terminal molybdopterin-binding and KH domains is the minimal essential substructure required for the hydrolysis of FAD and other ADP-containing dinucleotides"]

## Reactions (from UniProt CATALYTIC ACTIVITY)

- FAD synthase (forward): `FMN + ATP + H+ = FAD + diphosphate` (EC 2.7.7.2, RHEA:17237) — the physiological/biosynthetic direction.
- FAD diphosphatase / FAD hydrolase: `FAD + H2O = FMN + AMP + 2 H+` (EC 3.6.1.18, RHEA:13889).
- NADH diphosphatase / NADH pyrophosphatase: `NADH + H2O = reduced NMN + AMP + 2 H+` (EC 3.6.1.22, RHEA:48868).
- FAD synthase also runs the reverse pyrophosphorolytic reaction at a much lower rate.

[file:human/FLAD1/FLAD1-uniprot.txt "Reaction=FAD + H2O = FMN + AMP + 2 H(+)"]
[file:human/FLAD1/FLAD1-uniprot.txt "PATHWAY: Cofactor biosynthesis; FAD biosynthesis; FAD from FMN: step"]

Note the direction convention: GO:0003919 FMN adenylyltransferase activity is defined
`ATP + FMN = diphosphate + FAD` (the synthase direction), while GO:0047884 FAD
diphosphatase activity is `FAD + H2O = AMP + FMN` (the hydrolase direction). Both are
distinct, well-supported activities of this bifunctional protein.

## Cofactor / metal requirement

FAD synthase activity requires a divalent metal (Mg2+ optimal; Co2+ comparable; lower
with Mn/Ca/Zn). FAD diphosphatase activity instead requires Co2+ (Ni/Mn partial;
Mg/Ca/Cu cannot substitute) and is stimulated by K+.

[file:human/FLAD1/FLAD1-uniprot.txt "The FAD synthase activity requires a divalent metal"]
[file:human/FLAD1/FLAD1-uniprot.txt "Magnesium or cobalt supports the highest FAD synthase activity"]
[file:human/FLAD1/FLAD1-uniprot.txt "The FAD diphosphatase activity requires cobalt"]

## Kinetics (isoform 2; from UniProt)

KM(FMN) ~0.35-1.5 uM; KM(ATP) ~15 uM; kcat(FAD synthesis) ~0.69 s-1 (E. coli-purified).
kcat is low, consistent with FAD release being rate-limiting and with a "FAD chaperone"
delivery step.

[PMID:16643857 "exhibited a K(M) value for FMN of 1.5+/-0.3microM"]
[PMID:21951714 "FAD release may represent the rate-limiting step of the whole catalytic cycle"]

## FAD chaperone / delivery function

Beyond catalysis, hFADS2 physically interacts with client apo-flavoproteins and
directly transfers newly made FAD to them (a "FAD chaperone" role). Demonstrated for
the nuclear demethylase KDM1A/LSD1 and mitochondrial dimethylglycine dehydrogenase
(DMGDH).

[PMID:25954742 "hFADS is able to operate as a FAD \"chaperone.\""]
[PMID:25954742 "A direct transfer of the cofactor from hFADS2 to apo-dimethyl glycine dehydrogenase was also demonstrated"]
[file:human/FLAD1/FLAD1-uniprot.txt "Interacts with KDM1A; which promotes"]
[file:human/FLAD1/FLAD1-uniprot.txt "Interacts with DMGDH; which promotes DMGDH holoenzyme formation"]

## Subcellular localization (isoform-dependent)

- **Isoform 1** (587 aa, canonical; N-terminal cleavable mitochondrial transit peptide,
  residues 1-17) → **mitochondrial matrix**.
- **Isoform 2** (490 aa; lacks the first 97 aa) → **cytosol** (most abundant isoform).
- FADS is also found in the **nucleus**, consistent with a nuclear flavin-cofactor pool
  supplying LSD1/KDM1A.

[PMID:20060505 "hFADS1, but not hFADS2, localizes in mitochondria"]
[file:human/FLAD1/FLAD1-uniprot.txt "Isoform 1 and 2 are located in mitochondria and cytosol, respectively"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: Nucleus"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 1]: Mitochondrion matrix"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Cytoplasm, cytosol"]

## Structure

Crystal structure (PDB 8ROM/8RON) of full-length hFADS2 and its C-terminal PAPS domain
in complex with FAD. The enzyme forms a **stable C2-symmetric dimer**; packing of one
protomer's KH domain against the other's N-terminal domain creates the adenosine-specific
hydrolytic active site.

[PMID:38688286 "hFADS2 associates in a stable C2-symmetric dimer"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBUNIT: Dimer (PubMed:38688286)"]

## Disease

Biallelic FLAD1 variants cause **Lipid Storage Myopathy due to FAD Synthase Deficiency
(LSMFLAD; MIM:255100)**, presenting as combined respiratory-chain deficiency and multiple
acyl-CoA dehydrogenase deficiency (MADD-like). Some (frameshift, hypomorphic) cases are
riboflavin-responsive. (Primary reference PMID:27259049 not in local cache; disease
statement quoted from UniProt.)

[file:human/FLAD1/FLAD1-uniprot.txt "Lipid storage myopathy due to flavin adenine dinucleotide"]
[file:human/FLAD1/FLAD1-uniprot.txt "Some patients show significant improvement with riboflavin treatment"]

## Notes on annotation review

- Core MF is **GO:0003919 FMN adenylyltransferase activity** (= FAD synthase), the
  biosynthetic step; supported by a large body of EXP/IDA annotations.
- **GO:0047884 FAD diphosphatase activity** is a genuine, experimentally demonstrated
  second catalytic activity (MPTb/KH domain), so it is a real (secondary) core function,
  not an over-annotation. IDA support in PMID:26277395, PMID:31351152, PMID:38688286.
- **GO:0035529 NADH pyrophosphatase activity** is a lower-efficiency side activity of the
  same hydrolase site (EC 3.6.1.22, RHEA:48868); real but non-core (KEEP_AS_NON_CORE).
- **GO:0003824 catalytic activity** (IEA, InterPro) is an uninformative root — MARK_AS_OVER_ANNOTATED (better specific terms exist).
- The many **protein binding / identical protein binding IPI** annotations come from
  high-throughput interactome screens (HuRI, BioPlex, etc.). Bare GO:0005515 is
  uninformative → MARK_AS_OVER_ANNOTATED (per policy, never REMOVE an IPI). The
  identical protein binding (GO:0042802) reflects the physiological homodimer, so keep
  as non-core. The functionally meaningful interactions (KDM1A, DMGDH) are the
  apo-flavoprotein clients (PMID:25954742), captured as the FAD-chaperone role, not as
  bare "protein binding".
- Localization: cytosol (IDA, isoform 2), mitochondrial matrix (IDA, isoform 1), nucleus
  (IDA) are all experimentally supported. Mitochondrion (HTP) and mitochondrial-matrix
  IEA are consistent. Nucleus IEA/ISS and cytoplasm ARBA IEA are redundant with the IDA
  evidence.
</content>
</invoke>

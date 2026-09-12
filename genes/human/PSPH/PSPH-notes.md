# PSPH (P78330, SERB_HUMAN) — review notes

## Identity and overview

- UniProt **P78330** (SERB_HUMAN), gene symbol **PSPH** (HGNC:9577), 225 aa, human (NCBITaxon:9606) [file:human/PSPH/PSPH-uniprot.txt].
- Recommended name: **Phosphoserine phosphatase** (PSP/PSPase); EC **3.1.3.3** [file:human/PSPH/PSPH-uniprot.txt "RecName: Full=Phosphoserine phosphatase"].
- Belongs to the **HAD-like hydrolase superfamily, SerB family** [file:human/PSPH/PSPH-uniprot.txt "Belongs to the HAD-like hydrolase superfamily. SerB family."]. InterPro IPR004469 (PSP); CDD cd04309 (HAD_PSP_eu); PANTHER PTHR43344.

## Core molecular function — catalysis

PSPH catalyzes the **last, irreversible step of de novo L-serine biosynthesis (the phosphorylated pathway)**: the Mg2+-dependent hydrolysis of O-phospho-L-serine to L-serine + inorganic phosphate.

- FUNCTION: "Catalyzes the last irreversible step in the biosynthesis of L-serine from carbohydrates, the dephosphorylation of O-phospho-L-serine to L-serine" [file:human/PSPH/PSPH-uniprot.txt].
- CATALYTIC ACTIVITY: "O-phospho-L-serine + H2O = L-serine + phosphate" (Rhea:21208; EC 3.1.3.3) [file:human/PSPH/PSPH-uniprot.txt].
- PATHWAY: "Amino-acid biosynthesis; L-serine biosynthesis; L-serine from 3-phospho-D-glycerate: step 3/3" [file:human/PSPH/PSPH-uniprot.txt].
- Original enzymatic characterization of the recombinant human enzyme: "it catalyzed the Mg2(+)-dependent hydrolysis of L-phosphoserine and an exchange reaction between L-serine and L-phosphoserine ... the enzyme was phosphorylated upon incubation with L-[32P]phosphoserine, which indicates that the reaction mechanism proceeds via the formation of a phosphoryl-enzyme intermediate" [PMID:9188776 abstract].

**GO term for MF:** The precise current MF term used by GOA is **GO:0036424 "L-phosphoserine phosphatase activity"** (def: "Catalysis of the reaction: O-phospho-L-serine + H2O = L-serine + phosphate, on a free amino acid"). Note: the older, broader GO:0004647 "phosphoserine phosphatase activity" is now **obsolete in GO** (confirmed via OLS `go` slice), so GO:0036424 is the correct current term and is exactly what GOA uses. Used as the core catalytic MF.

## Mechanism / catalytic residues (HAD phosphoaspartate mechanism)

- Active site Asp20 is the nucleophile; a phosphoaspartyl (or glutamyl) enzyme intermediate forms [PMID:9188776 "an aspartyl- or a glutamyl-phosphate was formed"].
- UniProt annotates ACT_SITE 20 (Nucleophile) and ACT_SITE 22 (Proton donor); BINDING sites for Mg2+ (Asp20, Asp22, Asn179 [FT residues]), O-phospho-L-serine (Thr52/Ser53 region, 109-111, 158, 182), and product L-serine [file:human/PSPH/PSPH-uniprot.txt].
- Mutagenesis (PMID:12213811) confirms catalytic importance: E29Q "Loss of L-phosphoserine phosphatase activity"; R65A/K "Loss of ... activity"; T182S "Reduces ... by about 99%"; R202A "Reduces ... by about 99%" [file:human/PSPH/PSPH-uniprot.txt].

## Cofactor / metal — magnesium

- COFACTOR: "Name=Mg(2+) ... Binds 1 Mg(2+) ion per subunit" [file:human/PSPH/PSPH-uniprot.txt].
- Ca2+ inhibits the Mg2+-dependent enzyme: "a Ca(2+) ion inhibits the activity of HPSP, even in the presence of added Mg(2+) ... The bidentate character of Asp20 towards Ca(2+) hampers the nucleophilic attack" [PMID:15291819 abstract]. GO:0000287 magnesium ion binding is well supported (IDA, PMID:15291819).

## Quaternary structure — homodimer, and dimerization is functionally required

- SUBUNIT: "Homodimer" (PMID:12213811, PMID:12777757, PMID:15291819, PMID:31205021) [file:human/PSPH/PSPH-uniprot.txt].
- Crystallography: "HPSP is a dimeric enzyme responsible for the third and final step of the l-serine biosynthesis pathway" [PMID:12777757 abstract].
- **Dimerization is required for full activity** — a rare self-interaction-disrupting variant lowers catalytic activity: PSPH "exists as a dimer in solution and can aggregate when mutations that interfere with dimerization are introduced ... mutations that disrupt this dimerization may also reduce PSPH enzymatic activity"; the T152I variant "significantly reduced PSPH phosphatase activity to 59.2% ± 4.3% relative to WT" and disrupts "an interaction with itself" [PMID:31515488 full text]. This is the functional basis for the GO:0042803 (protein homodimerization) and GO:0042802 (identical protein binding) annotations: they capture the biologically meaningful self-association, not a generic sticky-protein artifact.
- The three GO:0042802 "identical protein binding" IPI annotations come from high-throughput interactome/variant-scanning studies:
  - PMID:25416956 (Rolland et al., proteome-scale binary interactome map) — Y2H self-interaction detection.
  - PMID:25502805 (Wei et al., Clone-seq / comparative interactome scanning) — PSPH not named in abstract/full text I read (paper is methods-focused on many genes); IntAct curated the self-interaction from it.
  - PMID:31515488 (Fragoza et al.) — explicitly characterizes PSPH self-interaction and its disruption by T152I (see quote above); the strongest of the three.

## Subcellular location

- SUBCELLULAR LOCATION: "Cytoplasm, cytosol" [file:human/PSPH/PSPH-uniprot.txt].
- The human brain enzyme is "a cytosolic enzyme ... purified 106 fold from human brain" [PMID:1965857 abstract]. (Note: the IDA cytosol annotation, GOA line, is assigned_by FlyBase but the source paper PMID:1965857 is the human-brain purification paper; cytosolic localization is consistent.)
- PMID:1965857 also shows the enzyme "could dephosphorylate both L and D enantiomers of the phosphoserine, but with different Km values"; L-serine is an uncompetitive inhibitor (feedback). This supports minor O-phospho-D-serine activity (UniProt: "May also act on O-phospho-D-serine (Probable)").

## Biological process — serine biosynthesis and downstream

- Core BP: **L-serine biosynthetic process (GO:0006564)**, IMP from PMID:14673469 (disease variants reduce activity and cause serine deficiency), plus IBA and IEA. Well supported.
- L-serine is a precursor for protein synthesis, other amino acids (e.g. glycine), nucleotide metabolism, glutathione, and phospholipids; it can be racemized to D-serine, an NMDA-receptor co-agonist neuromodulator [file:human/PSPH/PSPH-uniprot.txt "L-serine can then be used ... or can be racemized to D-serine, a neuromodulator"; PMID:12213811 "HPSP regulates the levels of glycine and d-serine, the putative co-agonists for the glycine site of the NMDA receptor in the brain"].
- GO:0006563 "L-serine metabolic process" (IDA, PMID:15291819) is a correct-but-more-general parent of the biosynthetic process; kept as non-core (redundant with GO:0006564).

## Disease

- **Phosphoserine phosphatase deficiency (PSPHD, MIM:614023)** — autosomal recessive serine-biosynthesis defect with pre/postnatal growth retardation, psychomotor/intellectual disability, and Williams-syndrome-like facial features; serine-responsive.
  - First case, with Williams-like features: "the phosphoserine phosphatase (EC 3.1.3.3.) activity in lymphoblasts and fibroblasts amounted to about 25% of normal values. Oral serine normalised the plasma and CSF levels" [PMID:9222972 abstract].
  - Causal mutations characterized on recombinant enzyme: D32N and M52T — "Met52Thr almost abolished the enzymatic activity, whereas the Asp32Asn mutation caused a 50% decrease in Vmax" [PMID:14673469 abstract].
  - Additional ID family with A35T variant [PMID:25080166; abstract is a Letter — full details not in cached abstract].

## Over-annotation / IEA-transfer flags

- **GO:0009612 response to mechanical stimulus**, **GO:0031667 response to nutrient levels**, **GO:0033574 response to testosterone** — all IEA (GO_REF:0000107, Ensembl Compara) transferred from a **rat** ortholog (UniProtKB:Q5M819 / ENSRNOP00000001228). These are physiological-context expression/regulation phenotypes of the rat gene, not molecular functions of human PSPH, and are not supported by any human data in this record. Marked as over-annotated (do not represent core function). Not removed (electronic transfer of a genuine experimental ortholog annotation), but flagged.

## Summary of core functions

1. **L-phosphoserine phosphatase activity (GO:0036424)** — Mg2+-dependent hydrolysis of O-phospho-L-serine to L-serine (+ Pi), the committed final step of L-serine biosynthesis.
2. **Magnesium ion binding (GO:0000287)** — essential catalytic cofactor (1 Mg2+/subunit).
3. **L-serine biosynthetic process (GO:0006564)** — the pathway role (step 3/3, 3-phospho-D-glycerate → L-serine).
4. **Protein homodimerization activity (GO:0042803)** — obligate homodimer; dimerization is required for full catalytic activity.

Localization: cytosol (GO:0005829).

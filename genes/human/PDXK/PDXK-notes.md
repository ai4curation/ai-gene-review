# PDXK (human) — pyridoxal kinase — review notes

UniProt: O00764 (PDXK_HUMAN). HGNC:8819. Gene on chromosome 21q22.3. 312 aa.
Family: pyridoxine kinase family; ribokinase-like superfamily fold.

## Core biology

PDXK is the salvage enzyme of vitamin B6 metabolism. It phosphorylates the three
dietary B6 vitamers — pyridoxal (PL), pyridoxine (PN) and pyridoxamine (PM) — at
their 5' hydroxyl using ATP, producing pyridoxal 5'-phosphate (PLP), pyridoxine
5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP) respectively. PLP is the
catalytically active form of vitamin B6 and the obligate cofactor for ~140
PLP-dependent enzymes (aminotransferases, decarboxylases, etc.).

- UniProt FUNCTION [file:human/PDXK/PDXK-uniprot.txt]: "Catalyzes the phosphorylation of the dietary vitamin B6 vitamers pyridoxal (PL), pyridoxine (PN) and pyridoxamine (PM) to form pyridoxal 5'-phosphate (PLP), pyridoxine 5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP)"; and "PLP is the active form of vitamin B6, and acts as a cofactor for over 140 different enzymatic reactions."
- EC 2.7.1.35 (pyridoxal kinase); Rhea:RHEA:10224 (PL + ATP = PLP + ADP + H+).
- Enzyme-level confirmation: [PMID:9099727 "Transient expression of the cDNA in human embryonic kidney cells confirmed that it encodes human pyridoxal kinase."]
- [PMID:10987144 "Pyridoxal kinase catalyses the phosphorylation of the vitamin B6."] and "Zn2+ is the most effective divalent cation in the phosphorylation of pyridoxal, and the human enzyme has maximum catalytic activity in the narrow pH range of 5.5-6.0."
- [PMID:17766369 "Pyridoxal kinase catalyzes the transfer of a phosphate group from ATP to the 5' alcohol of pyridoxine, pyridoxamine, and pyridoxal."] — establishes activity on all three vitamers.
- [PMID:19351586 "Pyridoxal kinase catalyzes the phosphorylation of pyridoxal (PL) to pyridoxal 5'-phosphate (PLP)."]

## Cofactor / metal and monovalent-cation requirements

- Divalent metal required. In vitro effectiveness: Zn2+ > Co2+ > Mn2+ > Mg2+ [file UniProt COFACTOR note]. Mg2+ is the physiological cofactor coordinating ATP in crystal structures.
- Mg2+ binding: [PMID:17766369] crystal structure "reveals Mg(2+) and Na(+) acting in tandem to anchor the ATP at the active site." (IDA GO:0000287 magnesium ion binding).
- Zn2+ binding: [PMID:10987144 "Zn2+ is the most effective divalent cation in the phosphorylation of pyridoxal"] (IDA GO:0008270 zinc ion binding).
- Monovalent cation activation: K+ and Na+ both activate; [PMID:9252787 "Among them, K+ is the most effective, improving both PK affinity for the substrates and maximal velocity. Na+ increases maximal velocity and PK affinity for ATP but decreases it for PL."]; [PMID:17766369 "hPLK affinity for ATP and PL is increased manyfold in the presence of K(+) when compared to Na(+); however, the maximal activity of the Na(+) form of the enzyme is more than double the activity in the presence of K(+). Other monovalent cations, Li(+), Cs(+), and Rb(+) do not show significant activity."]
  - Note: Li+, Na+, K+ binding are structural/regulatory features of the monovalent-cation site rather than the enzyme's core molecular function. Li+ is described as a "poor activator" [PMID:9252787]; the GO:0031403 lithium ion binding annotation is over-annotation of a physiologically minor cation.

## Structure / mechanism

- Homodimer: [file UniProt SUBUNIT: "Homodimer. {ECO:0000269|PubMed:17766369}."]. Note PMID:10987144 reports the recombinant MBP-fusion enzyme as a monomer that is still catalytically active ("The recombinant enzyme is a monomer endowed with catalytic activity, indicating that the native quaternary structure of pyridoxal kinase is not a prerequisite for catalytic function."). So dimerization is not strictly required for catalysis — supports KEEP_AS_NON_CORE for GO:0042803 homodimerization activity.
- Active-site residue Asp235 is the catalytic proton acceptor: [PMID:19351586 "A D235A variant shows 7-fold and 15-fold decreases in substrate affinity and activity, respectively."] and "These results document the role of Asp235 in PL kinase activity."
- Multiple crystal structures (2AJP, 2F7K, 2YXT/2YXU, 3FHX/3FHY, 3KEU, 4EN4/4EOH, 8WR2) with ATP/Mg2+/Na+/PLP.
- [PMID:16600635 "Pyridoxal kinase, a member of the ribokinase superfamily, catalyzes the ATP-dependent phosphorylation reaction of vitamin B6 and is an essential enzyme in the formation of pyridoxal-5'-phosphate"] — confirms ATP binding (IDA GO:0005524) and homodimeric crystal form.

## Subcellular location

- Cytosol is the authoritative location: [file UniProt SUBCELLULAR LOCATION: "Cytoplasm, cytosol {ECO:0000269|PubMed:9099727}."]. Supported by IBA, IEA (SubCell), and Reactome TAS annotations, and HDA proteomics (PMID:16780588 chr21 localization screen).
- Nucleus/nucleoplasm annotations (HDA PMID:21630459 sperm-nucleus proteome; IDA GO:0005654 nucleoplasm from HPA) are high-throughput / IF localizations. The sperm-nucleus proteome (PMID:21630459) is a bulk MS catalogue of 403 proteins; not indicative of a nuclear function for PDXK. Treat nuclear locations as non-core/over-annotation.
- Extracellular exosome (HDA PMID:19056867, urinary exosome proteome) and extracellular region / secretory-granule / specific-granule lumen (Reactome "Neutrophil degranulation" TAS) are bystander/secretome catalogue annotations; PDXK is a cytosolic enzyme with no signal peptide. Keep as non-core.

## Disease

- Biallelic PDXK mutations cause autosomal recessive axonal polyneuropathy with optic atrophy (HMSN6C, MIM:618511), responsive to PLP supplementation: [PMID:31187503 "We identified biallelic mutations in PDXK in 5 individuals from 2 unrelated families with primary axonal polyneuropathy and optic atrophy."] and "Low PDXK ATP binding resulted in decreased erythrocyte PDXK activity and low pyridoxal 5'-phosphate (PLP) concentrations." Variants R220Q and A228T decrease kinase activity [file UniProt VARIANT].
- This IMP evidence (PMID:31187503) supports both GO:0008478 (kinase activity, via patient-variant loss of activity) and GO:0009443 (PLP salvage, via low PLP phenotype).

## Annotation review summary

Core molecular function: GO:0008478 pyridoxal kinase activity (many IDA/EXP/IMP, plus IBA, IEA).
Core process: GO:0009443 pyridoxal 5'-phosphate salvage (IDA/IC/IMP/IBA). GO:0042816 vitamin B6 metabolic process is a correct but more general parent (KEEP_AS_NON_CORE / general).
Core supporting MF: GO:0005524 ATP binding, GO:0000287 magnesium ion binding, GO:0008270 zinc ion binding (all IDA).
Core location: GO:0005829 cytosol.

Non-core / over-annotation:
- GO:0030955 potassium ion / GO:0031402 sodium ion binding: real monovalent-cation activation site; regulatory, keep as non-core.
- GO:0031403 lithium ion binding: over-annotation (Li+ is a poor/non-physiological activator).
- GO:0030170 pyridoxal phosphate binding: PLP is the reaction product bound in product-complex crystal structures (3KEU etc.), not a cofactor role; over-annotation of a substrate/product-binding event.
- GO:0042803 protein homodimerization activity: real (homodimer) but not required for catalysis; keep as non-core.
- Nuclear (GO:0005634, GO:0005654), extracellular (GO:0005576, GO:0070062), granule lumen (GO:0034774, GO:0035580) locations: HDA/IF/Reactome secretome bystander annotations; non-core.

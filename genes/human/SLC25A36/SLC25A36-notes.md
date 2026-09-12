# SLC25A36 (PNC1 / PNC2) — gene review notes

## Identity
- UniProt: Q96CQ1 (S2536_HUMAN), 311 aa, "Solute carrier family 25 member 36" [file:human/SLC25A36/SLC25A36-uniprot.txt].
- Gene: HGNC:25554, GeneID 55186, chromosome 3 (GLC1C region).
- Also called PNC2 in the disease literature (the mitochondrial pyrimidine nucleotide carrier PNC1 was originally the yeast/related activity; human SLC25A36 is designated PNC2 by Shahroor et al.). UniProt title: "PNC2 (SLC25A36) deficiency" [PMID:34971397].
- Member of the mitochondrial carrier (SLC25 / TC 2.A.29) family: three Solcar repeats, six predicted transmembrane helices (TM 7-27, 41-57, 111-131, 180-200, 226-246, 291-311) [file:human/SLC25A36/SLC25A36-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family"].

## Core molecular function — mitochondrial pyrimidine nucleotide carrier
- UniProt FUNCTION: "Mitochondrial transporter that imports/exports pyrimidine nucleotides into and from mitochondria. Selectively transports cytosine, guanosine, inosine and uridine (deoxy)nucleoside mono-, di-, and triphosphates by antiport mechanism. Catalyzes uniport at much lower rate" [file:human/SLC25A36/SLC25A36-uniprot.txt].
- Biochemical characterization: recombinant SLC25A36 was overexpressed in bacteria and reconstituted in phospholipid vesicles. It transports "cytosine and uracil (deoxy)nucleoside mono-, di-, and triphosphates by uniport and antiport" [PMID:25320081]. It "also transported guanine but not adenine (deoxy)nucleotides" [PMID:25320081] — i.e. broad pyrimidine specificity plus guanine (a purine) but excluding adenine nucleotides.
- Kinetics (reconstituted, 25 °C): KM 0.21 mM CTP, 1.19 mM UTP, 0.23 mM GTP, 2.5 mM TTP; "CTP is the best substrate" [file:human/SLC25A36/SLC25A36-uniprot.txt].
- Inhibited by pyridoxal 5'-phosphate, 4,7-diphenyl-1,10-phenanthroline, tannic acid, and mercurials [file:human/SLC25A36/SLC25A36-uniprot.txt].
- UniProt encodes many Rhea CATALYTIC ACTIVITY entries as antiport half-reactions vs CTP (e.g. UTP(in)+CTP(out)=UTP(out)+CTP(in), RHEA:73531), consistent with a nucleotide antiporter; also a pure CTP(out)=CTP(in) uniport reaction (RHEA:73651) [file:human/SLC25A36/SLC25A36-uniprot.txt]. These are transporter "catalytic activities" (transport reactions), NOT enzymatic bond-making/breaking — SLC25A36 is a transporter, not a metabolic enzyme.
- **Primary core MF term: GO:0015218 pyrimidine nucleotide transmembrane transporter activity** (UniProt DR line assigns this IDA; GOA has it as IDA/IBA/IEA). Verified MF-branch in local go.db.
- Secondary/contributing MF: GO:0015216 purine nucleotide transmembrane transporter activity — supported by transport of guanine (deoxy)nucleotides but not adenine [PMID:25320081]. This is a genuine but non-core activity; the pyrimidine activity is the defining/best-supported one and the one GOA/UniProt annotate. Not adding as a separate core_functions MF (single primary MF used); noted here for completeness.

## Core biological process and localization
- Physiological role: "import/export pyrimidine nucleotides into and from mitochondria" providing precursors for de novo synthesis of mitochondrial DNA and RNA while exporting catabolites; the main physiological role "is to import/export pyrimidine nucleotides" and to "accomplish transport steps essential for mitochondrial DNA and RNA synthesis and breakdown" [PMID:25320081].
- BP term: GO:1990519 pyrimidine nucleotide import into mitochondrion (IDA from PMID:25320081; also IBA). Verified BP-branch.
- Localization: mitochondrion inner membrane. UniProt SUBCELLULAR LOCATION "Mitochondrion inner membrane {ECO:0000305|PubMed:25320081}; Multi-pass membrane protein" [file:human/SLC25A36/SLC25A36-uniprot.txt]. Targeting confirmed: "SLC25A33 and SLC25A36 were found to be targeted to mitochondria" [PMID:25320081]. GO:0005743 (mitochondrial inner membrane, CC) is the specific core location; GO:0005739 (mitochondrion) is the redundant organelle-level parent (IDA/HTP/IBA).
- Functional confirmation across species: expression of SLC25A36 rescued yeast RIM2 (mitochondrial pyrimidine nucleotide carrier) deletion phenotypes [PMID:25320081].

## Disease
- Biallelic loss-of-function causes Hyperinsulinemic hypoglycemia, familial, 8 (HHF8; MIM 620211) — hyperinsulinism/hyperammonemia (HI/HA)-like syndrome, protein-feeding-provoked hypoglycemia, persistent mild hyperammonemia, recurrent seizures [file:human/SLC25A36/SLC25A36-uniprot.txt; PMID:34576089; PMID:34971397; PMID:36695547]. Uridine treatment was reported in the first case [PMID:34576089]. These are disease/phenotype references, not GO-annotation sources in the current GOA.

## Tissue specificity
- "Widely expressed at moderate level. Expressed most strongly in pancreas" [file:human/SLC25A36/SLC25A36-uniprot.txt; PMID:17210862, PMID:34971397]. HPA: low tissue specificity.

## Annotation-by-annotation notes (GOA, 11 rows)
1. GO:0005739 mitochondrion, IBA, is_active_in (GO_REF:0000033) — correct organelle localization, redundant with inner-membrane; KEEP_AS_NON_CORE.
2. GO:1990519 pyrimidine nucleotide import into mitochondrion, IBA, involved_in — core BP, phylo-inferred; ACCEPT.
3. GO:0015218 pyrimidine nucleotide transmembrane transporter activity, IBA, enables — core MF, phylo-inferred; ACCEPT.
4. GO:0005743 mitochondrial inner membrane, IEA (SubCell), located_in — core location; ACCEPT.
5. GO:0006862 nucleotide transport, IEA (ARBA), involved_in — over-general parent of the specific pyrimidine import BP; MARK_AS_OVER_ANNOTATED.
6. GO:0015218 ... IEA (InterPro), enables — same core MF via InterPro; ACCEPT.
7. GO:0055085 transmembrane transport, IEA (InterPro), involved_in — very general parent; KEEP_AS_NON_CORE.
8. GO:1990519 ... IDA (PMID:25320081), involved_in — strongest experimental support for core BP; ACCEPT.
9. GO:0005739 mitochondrion, HTP (PMID:34800366), located_in — mito-proteome, redundant with inner-membrane; KEEP_AS_NON_CORE.
10. GO:0005739 mitochondrion, IDA (PMID:25320081), located_in — direct localization, redundant with inner-membrane; KEEP_AS_NON_CORE.
11. GO:0015218 ... IDA (PMID:25320081), enables — strongest experimental support for core MF; ACCEPT.

## References status
- PMID:25320081 (Di Noia 2014, J Biol Chem) — the defining biochemical paper. Cache is abstract-only (full_text_available: false) but the abstract is rich and directly supports MF/BP/localization. HIGH / VERIFIED.
- PMID:34800366 (Morgenstern 2021 mito-proteome) — bulk HTP localization support only. LOW / VERIFIED.
- Disease PMIDs (34576089, 34971397, 36695547) and identification/tissue PMID:17210862 are in UniProt but are not sources of current GOA GO annotations; not added to the review references list (no GO annotation to support). Documented here.

## Core function decision
- molecular_function: GO:0015218 pyrimidine nucleotide transmembrane transporter activity
- directly_involved_in: GO:1990519 pyrimidine nucleotide import into mitochondrion
- locations: GO:0005743 mitochondrial inner membrane
- NOT a catalytic/enzymatic MF — it is a transporter. Avoided "protein binding". Purine (guanine) nucleotide transport (GO:0015216) is a real secondary activity but pyrimidine transport is the core.

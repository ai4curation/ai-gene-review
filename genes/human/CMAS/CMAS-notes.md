# CMAS (human) — review notes

UniProt: Q8NFW8 (NEUA_HUMAN). Gene: CMAS. HGNC:18290. Chromosome 12.
Recommended name: **N-acylneuraminate cytidylyltransferase** (EC 2.7.7.43).
AltName: CMP-N-acetylneuraminic acid synthase (CMP-NeuNAc synthase).

## Core biology

CMAS is the enzyme that **activates free sialic acid** so it can be used for
glycoconjugate biosynthesis. It condenses **N-acetylneuraminate (Neu5Ac)** with
**CTP** to form the sugar-nucleotide donor **CMP-N-acetylneuraminate (CMP-Neu5Ac)**
plus diphosphate. CMP-Neu5Ac is the universal donor substrate used by
sialyltransferases (after CMP-Neu5Ac is transported into the Golgi by SLC35A1).

- FUNCTION (UniProt): "Catalyzes the activation of N-acetylneuraminic acid (NeuNAc) to cytidine 5'-monophosphate N-acetylneuraminic acid (CMP-NeuNAc), a substrate required for the addition of sialic acid. Has some activity toward NeuNAc, N-glycolylneuraminic acid (Neu5Gc) or 2-keto-3-deoxy-D-glycero-D-galacto-nononic acid (KDN)." [file:human/CMAS/CMAS-uniprot.txt]
- CATALYTIC ACTIVITY (UniProt): "an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate"; Rhea:RHEA:11344; EC=2.7.7.43; Evidence ECO:0000269|PubMed:11602804. [file:human/CMAS/CMAS-uniprot.txt]
- PATHWAY (UniProt): "Amino-sugar metabolism; N-acetylneuraminate metabolism." [file:human/CMAS/CMAS-uniprot.txt] (UniPathway UPA00628)
- Substrate promiscuity: acts on Neu5Ac, Neu5Gc and KDN — hence the recommended name is the general "N-acylneuraminate cytidylyltransferase", not just CMP-Neu5Ac synthase.

## Subcellular location — notably nuclear

Human CMAS is (at least partly) **nuclear**. This is unusual among the sialic-acid
biosynthetic enzymes (the others are cytosolic); CMP-Neu5Ac made in the nucleus is
then exported to the cytosol and imported into the Golgi.

- SUBCELLULAR LOCATION (UniProt): "Nucleus {ECO:0000269|PubMed:11602804}." [file:human/CMAS/CMAS-uniprot.txt] — experimental, from Lawrence et al. 2001.
- DOMAIN (UniProt): "The BC2 (basic cluster 2) motif is necessary and sufficient for the nuclear localization and contains the catalytic active site. The localization in the nucleus is however not required for the enzyme activity (By similarity)." [file:human/CMAS/CMAS-uniprot.txt] — i.e. nuclear localization and catalysis are separable; nuclear import is NOT needed for activity.
- SUBUNIT (UniProt): "Homotetramer; the active enzyme is formed by a dimer of dimers." [file:human/CMAS/CMAS-uniprot.txt]

Reactome R-HSA-4084982 concurs: "CMAS is ubiquitously expressed and localizes to the nucleus in mammalian cells. The active form of the enzyme is a homotetramer (a dimer of dimers) ... CMP-Neu5Ac is the donor substrate for sialyltransferases." [reactome:R-HSA-4084982]

## GO term id verification (OLS, 2026-07)

- GO:0008781 N-acylneuraminate cytidylyltransferase activity — MF; def "Catalysis of the reaction: CTP + N-acylneuraminate = diphosphate + CMP-N-acylneuraminate." Current, not obsolete. Core MF.
- GO:0006055 CMP-N-acetylneuraminate biosynthetic process — BP; current. Core BP (the actual product of the reaction).
- GO:0006054 N-acetylneuraminate metabolic process — BP; current. Parent/broader metabolic process (UniPathway IEA).
- GO:0005634 nucleus — CC; current. Experimental (Lawrence 2001) + HDA.
- GO:0005730 nucleolus — CC; current. HPA IDA (immunofluorescence).
- GO:0005654 nucleoplasm — CC; current. Reactome TAS.

## Annotation-by-annotation reasoning

1. GO:0008781 MF, IBA (GO_REF:0000033) — core catalytic function. ACCEPT. Directly supported by UniProt CATALYTIC ACTIVITY + EC 2.7.7.43 + phylogenetic (IBA) consensus across FB/MGI/ZFIN orthologs.
2. GO:0005634 nucleus, IEA (GO_REF:0000044, SubCell) — subcellular-location IEA that mirrors the experimental Nucleus location. ACCEPT (redundant with the HDA nucleus but correct).
3. GO:0008781 MF, IEA (GO_REF:0000120, RHEA/EC) — automated MF from the Rhea/EC mapping; identical to core function. ACCEPT.
4. GO:0006054 N-acetylneuraminate metabolic process, IEA (GO_REF:0000041, UniPathway) — correct but broad parent process. The reaction product is specifically CMP-Neu5Ac (GO:0006055), so this is a less-precise ancestor. KEEP_AS_NON_CORE (correct, but GO:0006055 is the precise core BP).
5. GO:0005730 nucleolus, IDA (GO_REF:0000052, HPA immunofluorescence) — HPA IF sub-nuclear localization. Consistent with the nuclear localization but nucleolar sub-compartment is not functionally established as where catalysis matters. KEEP_AS_NON_CORE.
6. GO:0006055 CMP-N-acetylneuraminate biosynthetic process, IMP (PMID:31121216) — Willems et al. 2019: CMAS KO cells have UNDETECTABLE CMP-sialic acid, directly demonstrating CMAS is required for CMP-Neu5Ac biosynthesis. This is the precise core BP. ACCEPT. (abstract-only cache; abstract explicitly states the CMAS-KO result.)
7. GO:0016020 membrane, HDA (PMID:19946888) — NK-cell membrane-proteome MS dataset. CMAS is a soluble nuclear/cytosolic enzyme with no TM domain; membrane capture is a proteomics artifact (paper itself notes ~60% of hits are not membrane proteins). Non-experimental for a specific function; over-annotation. MARK_AS_OVER_ANNOTATED (HDA, not IDA/IMP — do not REMOVE; flag as over-annotation).
8. GO:0005634 nucleus, HDA (PMID:21630459) — sperm-nucleus proteome MS. Corroborates nuclear localization (consistent with the experimental Lawrence 2001 nucleus). ACCEPT.
9. GO:0005654 nucleoplasm, TAS (Reactome:R-HSA-4084982) — Reactome states CMAS localizes to the nucleus; nucleoplasm is a reasonable sub-nuclear placement. Consistent with nuclear localization. KEEP_AS_NON_CORE.

## Publications reviewed (cache = abstract-only)

- PMID:31121216 (Willems 2019) full_text_available: false. Abstract supports GO:0006055 IMP: "CMP-sialic acid was ... undetectable in CMAS KO." RELEVANT/HIGH.
- PMID:19946888 (Ghosh 2010, NK membrane proteome) full_text_available: false. Large-scale MS; ~40% predicted membrane, remainder transient/artifactual. Supports only "membrane" HDA capture; LOW relevance to CMAS function.
- PMID:21630459 (de Mateo 2011, sperm nucleus proteome) full_text_available: false. Large-scale MS of sperm nuclei; supports nucleus HDA. MEDIUM (corroborative of nuclear localization).
- PMID:11602804 (Lawrence 2001) NOT in publications cache — this is the primary experimental reference for enzyme activity, tissue specificity, and Nucleus location (cited in UniProt with ECO:0000269). Its content is quoted here via the UniProt record (file: reference), not the paper directly.

## Core functions (synthesis)

- MF: GO:0008781 N-acylneuraminate cytidylyltransferase activity.
- BP: GO:0006055 CMP-N-acetylneuraminate biosynthetic process.
- Location: GO:0005634 nucleus (experimental; also detected nucleolus/nucleoplasm sub-compartments).

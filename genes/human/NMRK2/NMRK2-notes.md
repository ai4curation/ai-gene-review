# NMRK2 (Q9NPI5) review notes

## Identity

- HGNC symbol: **NMRK2** (HGNC:17871); synonyms **ITGB1BP3**, **NRK2**, **MIBP**.
- UniProt: Q9NPI5, `NRK2_HUMAN`, 230 aa, chromosome 19. RecName **Nicotinamide riboside kinase 2** with EC 2.7.1.22 and EC 2.7.1.173; AltNames **Integrin beta-1-binding protein 3**, **Muscle integrin-binding protein (MIBP)**, **Ribosylnicotinamide kinase 2** [file:human/NMRK2/NMRK2-uniprot.txt lines 6-17].
- Family: uridine kinase family, NRK subfamily; Rossmann-fold / P-loop NTPase (CDD NRK1, Pfam AAA_18) [file:human/NMRK2/NMRK2-uniprot.txt lines 173, 272-278].

## Two distinct roles

NMRK2 has two documented, historically independent lines of characterization that both map to real functions.

### 1. Nicotinamide riboside kinase (NAD+ salvage) — CORE catalytic function

- UniProt FUNCTION: "Catalyzes the phosphorylation of nicotinamide riboside (NR) and nicotinic acid riboside (NaR) to form nicotinamide mononucleotide (NMN) and nicotinic acid mononucleotide (NaMN)" [file:human/NMRK2/NMRK2-uniprot.txt lines 123-126].
- Two catalytic activities, both ECO:0000269|PubMed:17914902:
  - EC 2.7.1.22: beta-nicotinamide D-riboside + ATP = beta-nicotinamide D-ribonucleotide (NMN) + ADP + H+ (RHEA:14017) → **GO:0050262 ribosylnicotinamide kinase activity**.
  - EC 2.7.1.173: beta-D-ribosylnicotinate + ATP = nicotinate beta-D-ribonucleotide (NaMN) + ADP + H+ (RHEA:25568) → **GO:0061769 nicotinate riboside kinase activity**.
- Kinetics (PubMed:17914902): KM=0.19 mM NR (with ATP), KM=0.063 mM NaR (with ATP); also acts on the cancer drug tiazofurin (KM=0.11 mM) and weakly on uridine (KM=1.3 mM) [file:human/NMRK2/NMRK2-uniprot.txt lines 142-153].
- Bieganowski & Brenner 2004 established the NRK route: "Nicotinamide riboside kinases from yeast and humans essential for this pathway were identified and found to be highly specific for phosphorylation of nicotinamide riboside and the cancer drug tiazofurin" [PMID:15137942 abstract]. Human NRK2 is one of the two human NRK genes (NRK1 = NMRK1, NRK2 = NMRK2) [PMID:17914902 "specific kinase, encoded by the products of the yeast and human NRK1 genes or the human NRK2 gene"].
- Tempel et al. 2007 solved the Nrk1 structure, identified active-site residues "shown to be essential for human Nrk1 and Nrk2 activity in vivo" [PMID:17914902 abstract]. Mutagenesis of NMRK2 Asp35→Ala and Glu100→Ala both abolish activity [file:human/NMRK2/NMRK2-uniprot.txt lines 335-340].
- Pathway: NAD(+) biosynthesis (cofactor biosynthesis), NR/NaR salvage branch, cytosolic. UniPathway UPA00253; Reactome R-HSA-8869627 (NR→NMN) and R-HSA-8869607 (NaR→NAMN) [file:human/NMRK2/NMRK2-uniprot.txt lines 154-155, 249, 251]. Best BP terms: **GO:0034355 NAD+ biosynthetic process via the salvage pathway** (NR/NAR salvage; term text explicitly covers NR and NAR), and the broader **GO:0009435 NAD+ biosynthetic process**.
- Localization: cytosol/cytoplasm (Reactome TAS; IBA cytoplasm) [file:human/NMRK2/NMRK2-goa.tsv].

### 2. Muscle integrin beta-1-binding protein (MIBP) — genuine second (non-core NAD) role

- Originally cloned as **MIBP**, a muscle-specific beta1-integrin binding protein: "A novel muscle-specific beta 1 integrin binding protein (MIBP) that modulates myogenic differentiation" [file:human/NMRK2/NMRK2-uniprot.txt lines 30-31; PubMed:10613898].
- UniProt SUBUNIT: "Interacts with ITGB1 alone or when associated with alpha-7, but not with alpha-5" [file:human/NMRK2/NMRK2-uniprot.txt lines 156-158], citing PubMed:10613898 and PubMed:12941630 (MIBP interacts with alpha7beta1 integrin, regulates cell adhesion and laminin matrix deposition).
- Functional consequence: "Reduces laminin matrix deposition and cell adhesion to laminin, but not to fibronectin. Involved in the regulation of PXN [paxillin] at the protein level and of PXN tyrosine phosphorylation. May play a role in the regulation of terminal myogenesis." [file:human/NMRK2/NMRK2-uniprot.txt lines 125-129].
- Down-regulated during myoblast differentiation [file:human/NMRK2/NMRK2-uniprot.txt line 171].
- This maps to **GO:0005178 integrin binding** (MF). GOA does NOT currently carry a GO:0005178 annotation for NMRK2 — it is documented in UniProt but not in the GOA TSV. I keep integrin binding as a **second core function** justified by UniProt + two primary papers (10613898, 12941630), and flag it as a proposed new term / candidate GOA annotation. The integrin-binding role is treated as non-core relative to the primary NAD-salvage catalytic identity but is a real, experimentally supported function.

## Annotation-by-annotation reasoning

- **GO:0005737 cytoplasm (IBA)** — ACCEPT (KEEP_AS_NON_CORE location). Broad but consistent; cytosol is the more precise term.
- **GO:0050262 ribosylnicotinamide kinase activity** — appears 4x (IBA, IEA/ARBA, 2× EXP from PMID:15137942 & PMID:17914902). This is the CORE MF. ACCEPT the two EXP annotations; ACCEPT IBA; the ARBA IEA is redundant but correct (KEEP_AS_NON_CORE).
- **GO:0061769 nicotinate riboside kinase activity** — appears 4x (IBA, IEA/ARBA, 2× EXP). NMRK2 also phosphorylates nicotinic acid riboside (EC 2.7.1.173), experimentally shown in PubMed:17914902. ACCEPT (second catalytic activity).
- **GO:0005829 cytosol** — IEA(ARBA) + 2× TAS(Reactome). Correct cytosolic localization. ACCEPT.
- **GO:1901847 nicotinate metabolic process (IEA + TAS Reactome)** — correct but broad parent process; the salvage/NAD-biosynthesis terms are more informative. KEEP_AS_NON_CORE.
- **GO:0005515 protein binding (IPI, PMID:12809483, with UniProtKB:Q9Y561=LRP12)** — the interactor is LRP12/ST7 (yeast two-hybrid, cytoplasmic tail of LRP12 binds MIBP) [PMID:12809483 abstract]. Bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED (never REMOVE an IPI). The biologically meaningful binding is integrin binding (GO:0005178), captured in core_functions.
- **GO:0009435 NAD+ biosynthetic process (IEA, UniPathway)** — correct; core BP. ACCEPT.
- **GO:0005654 nucleoplasm (IDA, HPA GO_REF:0000052)** — HPA immunofluorescence. NMRK2 is a cytosolic metabolic enzyme; a nucleoplasm localization is unexpected and not supported by any primary literature (no NLS, disordered C-terminus only). Small proteins (26 kDa) can passively equilibrate into the nucleus, and HPA antibody-based IF can over-call nuclear signal. IDA experimental → do not REMOVE; MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE (isolated HPA IDA, no functional role in nucleus known).

## Reference adjudication

- PMID:15137942 (Bieganowski & Brenner, Cell 2004) — HIGH relevance, VERIFIED. Establishes human NRK genes (incl. NMRK2) and the Preiss-Handler-independent NR→NAD+ route. Abstract-only cache.
- PMID:17914902 (Tempel et al., PLoS Biol 2007) — HIGH, VERIFIED. Structures + kinetics; NMRK2 EC 2.7.1.22 / 2.7.1.173, active-site mutants. Full text available.
- PMID:12809483 (Battle et al., Biochemistry 2003) — the IPI source. VERIFIED as the record behind the IntAct MIBP–LRP12 interaction (paper is about ST7/LRP12 whose cytoplasmic tail binds MIBP). Relevance to NMRK2's core function is LOW (it is an interactor discovery, not a functional study of NMRK2). Correctly cited for the interaction, but supports only bare "protein binding".
- Reactome R-HSA-196807 (Nicotinate metabolism), R-HSA-8869607 (NMRK2 phosphorylates NAR→NAMN), R-HSA-8869627 (NMRK2 phosphorylates NR→NMN) — VERIFIED, describe the catalytic reactions and cytosolic localization.
- PubMed:10613898 (Li, Mayne & Wu, J Cell Biol 1999) and PubMed:12941630 (Li et al., Dev Biol 2003) — MIBP / integrin-binding papers cited in UniProt; not in GOA TSV, not cached, so cited via the UniProt record rather than directly.
</content>
</invoke>

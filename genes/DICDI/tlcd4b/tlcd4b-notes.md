# tlcd4b (DICDI) - Research Notes

## Gene Identity

- **UniProt**: Q550S9 (TLC4B_DICDI)
- **Gene**: tlcd4b (synonyms: tmem56b)
- **ORF**: DDB_G0277029
- **Organism**: Dictyostelium discoideum (social amoeba)
- **Product**: TLC domain-containing protein 4 B / Transmembrane protein 56 homolog B

## Domain Architecture

The protein contains a single TLC (TRAM/LAG1/CLN8) domain spanning residues 44-243 (PROSITE PS50922), within the broader TLC domain-containing family signature (IPR050846, residues 10-247). It has six predicted transmembrane helices and is a multi-pass integral membrane protein of 257 amino acids.

Relevant InterPro signatures:
- IPR006634: TRAM/LAG1/CLN8 homology domain (Pfam PF03798: TRAM_LAG1_CLN8)
- IPR050846: TLC domain-containing (family-level)
- PANTHER: PTHR13439 (CT120 protein family)

## TLC Domain Family - Literature Review

The TLC domain was originally identified as a shared module across three functionally diverse protein families: TRAM (translocating chain-associated membrane protein), LAG1/ceramide synthases, and CLN8 (mutated in neuronal ceroid lipofuscinosis). [PMID:12151215 Winter & Ponting 2002, "A family of membrane-associated proteins related to yeast Lag1p and mammalian TRAM has been identified. The family includes the protein product of CLN8, a gene mutated in progressive epilepsy with mental retardation."]

In humans, 16 genes encode TLC domain-containing proteins. Six of these are ceramide synthases (CerS1-6), which catalyze the N-acylation of sphinganine using fatty acyl-CoA substrates. Their acyl chain specificity is determined within a 150-residue region of the TLC domain [PMID:22144673 Tidhar et al. 2012, "a minimal region of 150 residues is sufficient for retaining CerS specificity"]. Three encode TRAM proteins involved in ER protein translocation; TRAMs also bind ceramide [PMID:34793833 Deng et al. 2021, "translocating chain-associated membrane protein 2 (TRAM2)...and TRAM1, a homolog of TRAM2, interacted with molecules derived from pac-C-Cer"].

Critically, a 2025 study demonstrated that the remaining TLCD family members (TLCD1, TLCD2, CLN8, etc.) are phospholipid-remodeling acyltransferases, not ceramidases or ceramide synthases [PMID:39970228 Sheokand et al. 2025, "poorly understood TRAM-LAG1-CLN8 domain (TLCD)-containing proteins are phospholipid remodeling enzymes"]. Specifically, TLCD1 is a lysophosphatidylethanolamine acyltransferase, and CLN8 is a lysophosphatidylglycerol acyltransferase catalyzing bis(monoacylglycero)phosphate biosynthesis.

In fission yeast (S. pombe), the CerS homolog Tlc4 was shown to function through non-catalytic activity in maintaining nuclear envelope integrity via Golgi translocation [PMID:37078207 Hirano et al. 2023, "Tlc4 possesses a TRAM/LAG1/CLN8 domain that is conserved in CerS proteins and functions through its non-catalytic activity"].

## TLCD4 Subfamily

TLCD4 (formerly TMEM56) belongs to the TLCD4 family within the broader TLC superfamily. The human TLCD4 paralog is predicted to be involved in lipid homeostasis, with localization to the ER and membranes. An important paralog is TLCD3A (a ceramide synthase). However, TLCD4 falls in the non-CerS branch of the TLC family -- it does NOT contain the Lag1p motif that defines ceramide synthases.

Given the 2025 findings (PMID:39970228) that non-CerS TLCD proteins are phospholipid acyltransferases, TLCD4 likely functions as a lysophospholipid acyltransferase involved in membrane phospholipid remodeling, rather than as a ceramidase or ceramide synthase.

## D. discoideum Sphingolipid Biology Context

D. discoideum produces phosphoinositol-containing sphingolipids with predominantly phytoceramide backbones, analogous to plants and fungi rather than mammals [PMID:39286488 Listian et al. 2024, "produces phosphoinositol-containing sphingolipids with predominantly phytoceramide backbones"]. An IPC synthase (IPCS1) was identified in D. discoideum that localizes to the Golgi and contractile vacuole. While sphingolipid metabolism is active in D. discoideum, there is no direct evidence linking tlcd4b specifically to ceramide metabolism.

## Genomic Context

The gene was identified through the D. discoideum genome sequencing projects [PMID:12097910 Gloeckner et al. 2002; PMID:15875012 Eichinger et al. 2005] and is located on chromosome 2. No experimental studies have been published specifically on D. discoideum tlcd4b.

## Key Conclusions

1. tlcd4b is an uncharacterized TLC domain protein in D. discoideum
2. Based on the most current understanding of the TLC family (PMID:39970228), non-CerS TLCD proteins are phospholipid acyltransferases, not ceramidases
3. The IBA annotation for lipid homeostasis (GO:0055088) is reasonable as a broad descriptor
4. The IBA annotation for ER localization (GO:0005783) is consistent with known TLCD localizations
5. The IEA annotation for membrane (GO:0016020) is correct but could be more specific (integral component of membrane)
6. No experimental molecular function has been established for this specific protein
7. The claim that TLCD4 proteins are ceramidases (as stated in the BioReason trace) is not supported by current literature

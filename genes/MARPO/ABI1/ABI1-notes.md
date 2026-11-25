# MpABI1 research and annotation notes

2026-10-25, Codex. Review and annotation-reviewer workflow, based on full primary text. D3W6X9 is a 568-residue ABI1 protein with the UniProt EMBL cross-reference GQ504039/ADB22517.1. The precise accession is the unit reviewed here.

## Identity caveat

[PMID:20097789, Evolutionarily conserved regulatory mechanisms of abscisic acid signaling in land plants: characterization of ABSCISIC ACID INSENSITIVE1-like type 2C protein phosphatase in the liverwort Marchantia polymorpha](https://pmc.ncbi.nlm.nih.gov/articles/PMC2832234/) explicitly states that cDNA was amplified using mRNA from male mature thalli and that the 568-residue clone is GQ504039. This source directly maps the cloned protein to D3W6X9. A proposed modern assignment to female ABI1A/MpVg00730 is therefore not asserted here. The historical clone source, modern locus, and sex-linked ABI1A/ABI1B names require sequence reconciliation. PMID:30442644 refers to interaction with MpABI1A, but the name alone does not resolve that accession ambiguity.

## Direct functional evidence

Full text of PMID:20097789 retrieved with `just fetch-pmid` through the supported HTML fallback. The original experiment purifies GST-MpABI1 from E. coli and measures phosphate release from radiolabeled myelin basic protein previously phosphorylated by a protein Ser/Thr kinase. It is a protein Ser/Thr phosphatase assay, not merely a pNPP small-molecule assay. EDTA abolishes activity. Mg2+ and Mn2+ activate the enzyme; Mn2+ works at lower concentrations, while Mg2+ supports maximal measured activity. Neither establishes the prevailing metal in vivo. G298D strongly reduces activity; N-terminal deletions do not markedly change catalytic activity. Wild-type protein, mutant proteins, and truncated constructs are distinguished.

The exact full-length MpABI1-GFP fusion accumulates mainly in nuclei of onion epidermal cells. This is direct localization evidence in a heterologous assay, not a demonstration of endogenous Marchantia nuclear localization. N-terminal deletion constructs distribute differently and their cytoplasmic signal should not be assigned to full-length protein.

Coexpression suppresses ABA-induced Em-GUS transcription in Marchantia cells. This supports direct negative regulation of ABA signaling by the phosphatase. Transgenic Physcomitrella stress/brood-cell phenotypes are heterologous and are not transferred as native Marchantia process annotations. The paper does not identify a physiological Marchantia SnRK2 substrate; no specific kinase-dephosphorylation claim is made.

## Decisions and research availability

All three original GOA rows reviewed: accept protein Ser/Thr phosphatase activity; refine both cation binding and metal ion binding to magnesium ion binding and manganese ion binding. One core catalytic function includes the evidenced negative signaling role and the explicitly qualified localization. Added two primary-supported annotations: nucleus (IDA, explicitly heterologous onion assay) and negative regulation of ABA signaling (IMP, Marchantia cell reporter assay). The enzyme performs the inhibitory signaling role; this is not substrate-necessity reasoning. QuickGO checks on 2026-10-25 show GO:0009788 on Arabidopsis ABI1/P49597 (including IMP PMID:16614222 and PMID:26443375) and ABI2/O04719 (IBA); HAB1/Q9CAJ0 has no exact match, so the role is not systematically excluded. Term definition and ancestry confirm negative regulation of signaling/ABA signaling. No redundant parent/child process is proposed. GO-CAM index has no D3W6X9 entry. Provider research was unavailable owing to established Falcon authentication/Perplexity quota failures in this session, so manual primary-source notes were used and no provider report was fabricated.

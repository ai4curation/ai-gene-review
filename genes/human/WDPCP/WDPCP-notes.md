# WDPCP: paired human–horse review notes

## Biological evidence

WDPCP is a CPLANE ciliary scaffold with an independent actin/septin/polarity role. Mouse microscopy and perturbation establish ciliary-base, cytoplasmic actin and focal-adhesion pools. Recombinant structural work demonstrates individual WDPCP phosphoinositide binding in its C-terminal tail. The full2016paper explicitly reports human WDPCP variants and relevant digit/tongue/palate phenotypes.

- [PMID:24302887: Wdpcp, a PCP protein required for ciliogenesis, regulates directional cell migration and cell polarity by direct modulation of the actin cytoskeleton.](https://pubmed.ncbi.nlm.nih.gov/24302887/) — full text cached.
- [PMID:27158779: The ciliopathy-associated CPLANE proteins direct basal body recruitment of intraflagellar transport machinery.](https://pubmed.ncbi.nlm.nih.gov/27158779/) — full text cached.
- [PMID:35427153: Structure of the ciliogenesis-associated CPLANE complex.](https://pubmed.ncbi.nlm.nih.gov/35427153/) — full text cached.

## Exact horse model

The horse N-terminal difference resembles the approximately35-residue human extension relative to mouse reported in the structure. The conserved scaffold supports broad ciliary/cytoskeletal predictions. A separate nine-residue deletion affects the lipid-binding tail; disorder does not imply that deletion is functionally irrelevant, and exact lipid affinity remains unresolved.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/WDPCP/WDPCP-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Distinguish transition-zone/base localization from the axonemal shaft. Test the tail deletion before transferring quantitative phosphoinositide affinity.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Sources: cached full texts of PMID:24302887 (mouse Wdpcp Cys40), PMID:27158779 (CPLANE, Xenopus/mouse/human genetics), PMID:35427153 (CPLANE cryo-EM and lipid binding), PMID:20671153 (Xenopus Fritz, the donor of the ISS rows), the UniProt record, PANTHER PTHR13667 PAINT/entries files, and the falcon deep-research file, which was used only to find sources.

### Identity
O95876 is the reviewed, canonical Swiss-Prot entry (isoform 1, 746 aa). It is not a fragment or an alternative gene model. UniProt cautions that Met-1 or Met-34 may be the initiator. That fits the structure paper: "Compared to mouse, the human Wdpcp has an N-terminal extension of ~35 residues that is not resolved in the map" [PMID:35427153]. Mouse Q8C456 is 722 aa, Xenopus Q32NR9 708 aa. The WD repeats (326-414) and the PIP-binding C-terminal tail (last ~60 residues) are both present.

### Evolutionary grounding
PANTHER puts human WDPCP, mouse Wdpcp (Q8C456), rat (B1WC10) and Xenopus (Q32NR9) in the same subfamily, PTHR13667:SF5. The four PAINT IBDs (cilium organization, nervous system development, axonemal basal plate, establishment of protein localization) sit at the bilaterian node PTN001007408, seeded from MGI and Xenopus (plus fly fritz for nervous system development). That justifies transferring the mouse and Xenopus experimental functions. The family review interpro/panther/PTHR13667/PTHR13667-review.yaml agrees with SF5 placement. It lists no mouse representative, but there is no disagreement.

### Changes vs previous review
- Axoneme (IEA, ISS): UNDECIDED → ACCEPT. The axonemal pool is shown directly in mouse IMCD3 ("Wdpcp is localized to the ciliary axoneme and in a ring-like structure at the base of the cilia in IMCD3 cells" [PMID:24302887]), in zebrafish pronephros, and in Xenopus ("sept7 and Fritz were localized along ciliary axonemes and in distinct foci near basal bodies" [PMID:20671153]).
- Intraciliary transport (NAS): ACCEPT → KEEP_AS_NON_CORE. CPLANE loads peripheral IFT-A at the basal body ("CPLANE acts by recruiting peripheral IFT-A proteins to the basal body for assembly onto the IFT-A core" [PMID:27158779]), but the IFT-A core still moves, and in the mouse "Ift88 distribution ... was unchanged" [PMID:24302887]. WDPCP acts upstream of the transport itself.
- Regulation of cilium assembly (NAS): ACCEPT → KEEP_AS_NON_CORE. WDPCP is assembly machinery; no regulatory role is shown.
- Plasma membrane (3 rows), apical plasma membrane: ACCEPT → KEEP_AS_NON_CORE. WDPCP is a peripheral cortical protein (Fritz-GFP at the cell cortex [PMID:20671153]); cell cortex is accepted as the informative location.
- NEW: ciliary transition zone (GO:0035869), the best-resolved ciliary compartment ("Wdpcp is localized to the transition zone" [PMID:24302887]).
- Phosphatidylinositol binding is kept as ACCEPT. The human C-terminal fragment (485-746) also binds PIP strips, and the BBS variant S708F increases binding [PMID:35427153]. Specificity is broad across monophosphates (PI3P > PI5P > PI4P), so the general term is as precise as the evidence allows.
- Developmental terms (nervous system/neural tube development, digit/tongue/palate morphogenesis, regulation of embryonic cell shape) stay KEEP_AS_NON_CORE. They are organismal outcomes, and the curator IMPs are not overruled.
- Added PMID:20671153 as the experimental basis of the Xenopus ISS rows. All earlier references are kept.
- Two core functions: (1) a CPLANE ciliary-base recruitment scaffold; (2) a cortical septin/actin PCP effector.

### Relative for the next review
Mouse Wdpcp (Q8C456, MGI:2144467) is a same-subfamily (SF5) ortholog and the PAINT seed. It is the best-characterized ortholog (Cys40 mutant, CPLANE structure with lipid mapping). There is no mouse review in the repo.

### Modules
No module covers CPLANE. modules/bbsome.yaml mentions WDPCP/BBS15 only to place it out of scope.

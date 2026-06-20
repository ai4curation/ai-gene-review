# UFC1 (Ubiquitin-fold modifier-conjugating enzyme 1) — research notes

UniProt: Q9Y3C8 (UFC1_HUMAN), 167 aa. HGNC:26941. Chromosome 1.

## Core identity / step in the cascade
UFC1 is the **E2 (conjugating) enzyme of the UFM1 (ufmylation) cascade**. UFM1 is a
ubiquitin-fold modifier conjugated to substrates via an E1→E2→E3 cascade analogous to
ubiquitylation. UFC1 accepts activated UFM1 from the E1 enzyme UBA5 and forms a thioester
intermediate at its catalytic Cys-116, then transfers UFM1 to substrate lysines with the
E3 ligase (UFL1/DDRGK1/CDK5RAP3).

- [PMID:15071506 "Activated Ufm1 is then transferred to its cognate E2-like enzyme, Ufc1, in a similar thioester linkage."] — founding paper identifying the UBA5–UFC1 E1/E2 pair.
- UniProt FUNCTION: "E2-like enzyme which specifically catalyzes the second step in ufmylation ... Accepts the ubiquitin-like modifier UFM1 from the E1 enzyme UBA5 and forms an intermediate with UFM1 via a thioester linkage."
- Active site Cys-116 (Glycyl thioester intermediate); C116S mutant forms a stable O-ester instead of thioester (UniProt MUTAGEN 116).

## Structural / mechanistic
- [PMID:38383789 "Stalled ribosomes at the endoplasmic reticulum (ER) are covalently modified with the ubiquitin-like protein UFM1 on the 60S ribosomal subunit protein RPL26 (also known as uL24)"] — UREL (UFL1–UFBP1/DDRGK1–CDK5RAP3) wraps around 60S; crystal structure of UFC1 in complex with UFL1/UFM1/DDRGK1 (PDB 8C0D). UFC1 residues Leu-32, Ile-40, Asp-50 mediate UFL1 binding / ribosome ufmylation.
- [PMID:36121123 "UFL1/UFBP1 utilizes a scaffold-type E3 ligase mechanism that activates the UFM1-conjugating E2 enzyme, UFC1, for aminolysis."] — non-canonical scaffold E3 activates UFC1; Lys-108 of UFC1 required (K108A abolishes ufmylation).
- UFC1 itself is ufmylated at Lys-122; deufmylated by UFSP1 (PMID:35926457).

## Biological roles of the modification (downstream of UFC1 catalysis)
- RPL26/uL24 on 60S is the principal UFMylation target [PMID:30626644 title "Ribosomal protein RPL26 is the principal target of UFMylation."].
- ER ribosome-associated quality control: [PMID:37036982 "UPS and RQC-dependent degradation of ER-APs strictly requires conjugation of the ubiquitin-like (Ubl) protein UFM1 to 60S ribosomal subunits at the RTJ."] — UFMylation modulates the ribosome–translocon junction to allow RQC of ER arrest peptides; release/recycling of stalled 60S from ER translocons.
- Reticulophagy / ER-phagy and response to ER stress: ufmylation pathway implicated (PMID:32160526, ER-phagy screen; PMID:23152784 transcriptional up-regulation of Ufm1 system under ER stress).
- Regulation of innate immune / interferon signaling: RIG-I signaling regulated by ufmylation (PMID:35394863); regulation of type II interferon production by ISS from mouse ortholog.

## Disease
- Biallelic UFC1 variants cause Neurodevelopmental disorder with spasticity and poor growth (NEDSG, MIM:618076); variants R23Q and T106I decrease thioester formation with UFM1 and decrease ufmylation [PMID:29868776]. Brain development (IMP) annotation derives from this.

## Interactions (IPI annotations in GOA)
Bona fide cascade partners: UBA5 (E1), UFL1 (E3), UFM1 (modifier). GOA IPI partners include
O94874 (UFL1), Q9GZZ9 (UBA5), P61960 (UFM1). Other IPI partners are largely high-throughput
(KIRREL3 Q8IZU9; various). Bare GO:0005515 protein binding is uninformative; the informative
MF is UFM1 conjugating enzyme activity.

## Localization
Acts in cytoplasm (IBA) but functions at the ER-bound/translocon-associated ribosome.
Extracellular exosome (HDA) and extracellular region annotations are proteomic-detection
contexts, not the site of function.

## Core function conclusion
Core MF: **GO:0061657 UFM1 conjugating enzyme activity** (E2), acting in **GO:0071569 protein
ufmylation** in the cytoplasm / at ER-bound ribosomes. GO:0071568 "UFM1 transferase activity"
is a near-synonymous parent reflecting the same activity.

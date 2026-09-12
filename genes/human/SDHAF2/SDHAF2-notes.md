# SDHAF2 (SDH5, PGL2, C11orf79) — Gene Review Notes

UniProt: Q9NX18 (SDHF2_HUMAN). 166 aa precursor; residues 1–29 mitochondrial transit
peptide, mature chain 30–166. HGNC:26034. Human, NCBITaxon:9606.

## Summary of function

SDHAF2 is a mitochondrial-matrix **assembly factor for succinate dehydrogenase
(respiratory Complex II / SDH)**. It is a soluble accessory protein, **not** a subunit
of the mature enzyme and **not** itself a succinate dehydrogenase. Its defining role is
in the **covalent flavinylation** of the flavoprotein subunit SDHA: SDHAF2 binds SDHA
and is required for/promotes the covalent attachment of the FAD cofactor to SDHA, a step
essential for SDH assembly and activity.

- UniProt FUNCTION [file:human/SDHAF2/SDHAF2-uniprot.txt]: "Plays an essential role in
  the assembly of succinate dehydrogenase (SDH)... Required for flavinylation (covalent
  attachment of FAD) of the flavoprotein subunit SDHA of the SDH catalytic dimer."
- UniProt SUBUNIT [file:human/SDHAF2/SDHAF2-uniprot.txt]: "Interacts with SDHA within the
  SDH catalytic dimer."
- UniProt SUBCELLULAR LOCATION [file:human/SDHAF2/SDHAF2-uniprot.txt]: "Mitochondrion
  matrix."
- UniProt keywords include **Chaperone**, Mitochondrion, Transit peptide.
- SIMILARITY: "Belongs to the SDHAF2 family"; HAMAP MF_03057; Pfam PF03937 (Sdh5);
  Gene3D "Flavinator of succinate dehydrogenase".

## Key primary references

- **PMID:19628817** (Hao et al., Science 2009) — the founding paper. Cached entry is
  **abstract-only** (`full_text_available: false`). Abstract states: "Both yeast and
  human Sdh5 interact with the catalytic subunit of the succinate dehydrogenase (SDH)
  complex... Sdh5 is required for SDH-dependent respiration and for Sdh1 flavination
  (incorporation of the flavin adenine dinucleotide cofactor)." Also reports germline
  loss-of-function mutations in human SDH5 segregating with hereditary paraganglioma.
  Basis for the IPI SDHA-interaction, IDA/EXP mitochondrion/matrix localization, and IMP
  protein-FAD linkage annotations. The G78R (Arg-78) PPGL2 variant "abolishes interaction
  with SDHA and flavination of SDHA" (UniProt VARIANT feature).

- **PMID:32887801** (Sharma et al., PNAS 2020) — X-ray structure of human SDHA–SDHAF2
  complex (PDB 6VAX). Cached entry is **abstract-only** (`full_text_available: false`).
  Abstract: "We report an X-ray structure of human SDHA and its dedicated assembly factor
  SDHAF2... a small molecule dicarboxylate... acts as an essential cofactor in this process
  and works in synergy with SDHAF2 to properly orient the flavin and capping domains of
  SDHA... adjusts the pKa of SDHAR451 so that covalent attachment of the flavin adenine
  dinucleotide (FAD) cofactor is supported." Basis for the IDA Complex II assembly
  annotation and confirms the direct SDHA interaction. Establishes SDHAF2 as a
  **chaperone/assembly factor** that orients SDHA domains rather than a catalyst — the
  covalent flavinylation is a largely autocatalytic reaction of SDHA that SDHAF2 (with the
  dicarboxylate) enables by structural remodeling.

- **PMID:23983127** (Liu et al., J Biol Chem 2013) — full text available. Reports a
  moonlighting/cytosolic role in a mouse/human lung-cancer context: loss of SDH5 initiates
  EMT via GSK-3β–β-catenin (Wnt) signaling; "The physical interaction between SDH5 and
  GSK-3β facilitates GSK-3β activation through Ser-9 dephosphorylation, which decreases
  nuclear β-catenin accumulation and transcriptional activity." Basis for the MGI IGI/IMP
  annotations to protein dephosphorylation (GO:0006470), negative regulation of EMT
  (GO:0010719), and negative regulation of canonical Wnt signaling (GO:0090090). These are
  a disease/cancer-context regulatory role, not the core mitochondrial assembly function;
  the mechanism (Ser-9 dephosphorylation of GSK-3β by SDH5) is indirect and SDHAF2 is not
  a phosphatase, so these are kept as non-core.

## Interactome / high-throughput references (protein binding IPIs)

- PMID:26496610 (Hein et al., Cell 2015), PMID:28514442 (Huttlin et al., Cell 2017),
  PMID:33961781 (Huttlin et al., Cell 2021, BioPlex 3.0), PMID:32296183 (Luck et al.,
  Nature 2020, HuRI Y2H): proteome-scale interaction surveys. WITH/FROM partners are SDHA
  (P31040) for most, and CYP4F2 (P78329)/SEC22A (Q96IW7) for PMID:32296183. These support
  GO:0005515 "protein binding" IPIs. Cached entries describe genome-scale methods and do
  not narrate SDHAF2 specifically; the SDHA interactions corroborate the well-established
  SDHAF2–SDHA binding, but "protein binding" (GO:0005515) is uninformative as an MF and is
  marked as over-annotated. The CYP4F2/SEC22A Y2H hits are isolated high-throughput binary
  pairs with no biological follow-up and are treated as over-annotations.

## Annotation review rationale (highlights)

- **Core molecular function**: SDHAF2 has no demonstrated catalytic activity of its own and
  does not bind FAD directly; it acts as a **protein-folding chaperone / assembly factor**
  (GO:0044183 "protein folding chaperone", MF; UniProt keyword "Chaperone") that binds SDHA
  and remodels/orients its domains to license autocatalytic covalent flavinylation.
- **Core biological process**: (1) covalent FAD attachment to SDHA —
  **GO:0018293 "protein-FAD linkage"** (the specific child of GO:0017013 "protein
  flavinylation"), and (2) **GO:0034553 "mitochondrial respiratory chain complex II
  assembly"**.
- Succinate-dehydrogenase / electron-transport catalytic terms
  (GO:0006121 "mitochondrial electron transport, succinate to ubiquinone",
  GO:0006099 "tricarboxylic acid cycle") are **over-annotations by IBA/IEA**: they describe
  the mature enzyme's activity, not the assembly factor. SDHAF2 is required *for* SDH
  activity but does not itself carry out succinate→ubiquinone electron transport or TCA-cycle
  chemistry. Marked as over-annotated / removed (IEA) as appropriate.

## Term id verifications (OLS, 2026)

- GO:0034553 = "mitochondrial respiratory chain complex II assembly" (BP). Verified.
- GO:0018293 = "protein-FAD linkage" (BP, child of GO:0017013 protein flavinylation). Verified.
- GO:0017013 = "protein flavinylation" (BP). Verified.
- GO:0044183 = "protein folding chaperone" — confirmed **molecular_function** namespace
  (OLS API). "Binding to a protein or a protein-containing complex to assist the protein
  folding process." Verified.
- GO:0050660 = "flavin adenine dinucleotide binding" (MF) — NOT used; no evidence SDHAF2
  binds FAD directly.
</content>

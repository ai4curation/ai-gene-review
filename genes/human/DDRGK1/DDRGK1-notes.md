# DDRGK1 / UFBP1 (DDRGK domain-containing protein 1) — research notes

UniProt: Q96HY6 (DDRGK_HUMAN), 314 aa. HGNC:16110. Chromosome 20. Synonyms: UFBP1, Dashurin, C20orf116.

## Role in the cascade
DDRGK1 is the **obligate cofactor / substrate-adaptor of the UFM1 E3 ligase**, a component of the
**UREL complex** (UFL1 + DDRGK1 + CDK5RAP3). It is a **single-pass ER membrane protein** (TM 1–28;
cytoplasmic 29–314) that tethers UREL to the ER membrane, restricting ufmylation to ER-docked ribosomes,
and stabilizes UFL1.
- UniProt: "Within the UREL complex, DDRGK1 tethers the complex to the endoplasmic reticulum membrane."
- Binds the E3 ligase UFL1 via its C-terminal region (region 216–314) → core MF GO:0044389 ubiquitin-like protein ligase binding.

## UFM1 reader
DDRGK1 has a **UFM1-interacting motif (UFIM, residues 195–209)** that specifically recognizes ufmylated
RPL26/uL24 → core MF **GO:0141185 UFM1-modified protein reader activity** [PMID:36121123, PMID:36543799,
PMID:37595036, PMID:38383785, PMID:38383789]. Reading ufmylated RPL26 stabilizes the 60S–UREL association
and drives release/recycling of the 60S subunit from the ER translocon.

## Substrate / PTM
DDRGK1 is itself ufmylated at **Lys-267** by UFL1; whether this is functional or collateral is unclear (UniProt).

## Other roles (downstream / non-core)
- ER stress / UPR: regulates ERN1/IRE1-alpha stability (UFM1-dependent), inhibiting the IRE1 UPR arm [PMID:28128204; PMID:32160526].
- Reticulophagy (CYB5R3 ufmylation) [PMID:36543799].
- NF-kappaB: modulates NFKBIA/IkappaB-alpha stability [PMID:23675531].
- Cartilage development via SOX9 stabilization; biallelic LoF → Shohat-type spondyloepimetaphyseal dysplasia (SEMDSH) [PMID:28263186].

## Localization
ER membrane (principal). HPA also reports ER, nucleolus; TAS cytoplasm (consistent with the large cytoplasmic domain).

## Core function conclusion
Core MFs: **GO:0044389 ubiquitin-like protein ligase binding** (UFL1 binding/adaptor) and
**GO:0141185 UFM1-modified protein reader activity** (UFIM). Site: ER membrane.

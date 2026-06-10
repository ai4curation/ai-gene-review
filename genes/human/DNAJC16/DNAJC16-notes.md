# DNAJC16 (ERdj8 / ERDJ8) research notes

## Identity
- UniProt Q9Y2G8, HGNC:29157, 782 aa precursor. DnaJ/HSP40 subfamily C member 16.
- AltName: ER-resident protein ERdj8 (Endoplasmic reticulum DNA J domain-containing protein 8).
- Architecture: N-terminal signal peptide (1-25), N-terminal J domain (29-93, cytoplasmic side),
  a thioredoxin (TRX) domain (119-247), single C-terminal TM helix (536-556; type IV membrane
  anchor); large cytoplasmic region 26-535. N-glycosylated. Two isoforms (isoform 2 lacks 1-312, so
  it lacks the J and TRX domains). [file:human/DNAJC16/DNAJC16-uniprot.txt]
- Pharos "Tdark"; PAN-GO 0 annotations; poorly characterized.

## Core function: ER membrane J-protein regulating autophagosome size
- Single functional study: PMID:32492081 (Yamamoto 2020, J Cell Biol): "ERdj8 governs the size of
  autophagosomes during the formation process." "ERdj8 localizes to a meshwork-like ER subdomain
  along with phosphatidylinositol synthase (PIS) and autophagy-related (Atg) proteins. ERdj8
  overexpression extended the size of the autophagosome through its DnaJ and TRX domains. ERdj8
  ablation resulted in a defect in engulfing larger targets." C. elegans orthologue dnj-8.
  [PMID:32492081]
- Mutagenesis: H57Q (J-domain HPD), C171A/C174A (TRX active-site cysteines) abolish the
  autophagosome-enlargement phenotype on overexpression — implicates both domains. [file:human/DNAJC16/DNAJC16-uniprot.txt]
- UniProt FUNCTION: "Plays an important role in regulating the size of autophagosomes during the
  formation process." [file:human/DNAJC16/DNAJC16-uniprot.txt]

## Localization
- ER membrane (IDA, PMID:32492081); single-pass type IV membrane protein. Also IEA SubCell.
  [file:human/DNAJC16/DNAJC16-uniprot.txt]

## GOA annotations (all 3 from PMID:32492081 / SubCell)
- GO:0005789 ER membrane IEA (SubCell) + IDA (PMID:32492081): ACCEPT, core localization.
- GO:0016243 regulation of autophagosome size IMP (PMID:32492081): ACCEPT, core BP.

## Curation
- Core function: ER membrane J-domain protein required for regulating autophagosome size; the
  precise molecular function (J-domain co-chaperone activity recruiting an ER Hsp70 such as
  BiP/HSPA5, and a redox/TRX activity) is not directly established — the readout is autophagosome
  size. No GOA MF term exists. Core captured via the BP GO:0016243 + ER membrane location. Do not
  over-claim a specific MF. The gene is otherwise poorly characterized.

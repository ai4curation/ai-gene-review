# DNAJC16 (ERdj8 / ERDJ8) research notes

## Identity
- UniProt Q9Y2G8, HGNC:29157, 782 aa precursor. DnaJ/HSP40 subfamily C member 16.
- AltName: ER-resident protein ERdj8 (Endoplasmic reticulum DNA J domain-containing protein 8).
- Architecture: N-terminal signal peptide (1-25), N-terminal J domain (29-93), a
  thioredoxin (TRX) domain (119-247), and a single C-terminal TM helix (536-556). UniProt
  predicts type IV topology with a cytoplasmic 26-535 region and an N-glycosylated
  C-terminal region, but Yamamoto et al. describe the J/TRX domains as ER-luminal (see
  topology note below). Two isoforms exist; isoform 2 lacks 1-312, so it lacks the J and
  TRX domains. [file:human/DNAJC16/DNAJC16-uniprot.txt; PMID:32492081]
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
- ER membrane (IDA, PMID:32492081; also IEA SubCell). ERdj8 is single-pass, but the
  orientation of its N-terminal J/TRX region remains unresolved.

## Topology remains unresolved

UniProt predicts a type IV orientation with residues 26-535, including the J and TRX
domains, on the cytoplasmic side of the ER membrane. The Yamamoto et al. primary study
instead describes ERdj8 as a type 1 membrane protein and states that "The DnaJ and TRX
domains of ERdj8 on the ER luminal side were important for the function of ERdj8 in the
regulation of autophagy" [PMID:32492081]. The cytoplasmic-topology model would make
BiP/HSPA5 an unlikely direct J-domain partner and would shift the HSP70 search toward
HSPA8/HSPA1A or other cytosolic partners, but that model should be treated as disputed
until a direct topology assay has mapped the J domain.

## GOA annotations (all 3 from PMID:32492081 / SubCell)
- GO:0005789 ER membrane IEA (SubCell) + IDA (PMID:32492081): ACCEPT, core localization.
- GO:0016243 regulation of autophagosome size IMP (PMID:32492081): ACCEPT, core BP.

## Curation
- Core function: ER membrane J-domain protein required for regulating autophagosome size; the
  precise molecular function (J-domain co-chaperone activity recruiting a topology-compatible
  HSP70, and a redox/TRX activity) is not directly established — the readout is autophagosome
  size. No GOA MF term exists. Core captured via the BP GO:0016243 + ER membrane location. Do not
  over-claim a specific MF or a BiP/HSPA5 exclusion until ERdj8's membrane topology is resolved.
  The gene is otherwise poorly characterized.

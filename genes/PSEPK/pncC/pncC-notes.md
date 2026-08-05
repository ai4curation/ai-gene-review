# pncC curation notes

## 2026-07-20

- Target identity: PP_1628 / UniProtKB Q88ME5, a 160-aa submitted NMN
  amidohydrolase with PncC-specific TIGR00199 and CinA C-terminal domains
  [UniProtKB:Q88ME5, "NCBIfam; TIGR00199; PncC_domain; 1."].
- Family function: bacterial PncC was established biochemically and genetically
  as NMN deamidase, routing NMN to NaMN and then through the Preiss-Handler
  pathway [PMID:21953451, "the predominant route, PNC IV, proceeds via NMN deamidation to NaMN, which is then converted to NAD by entering the Preiss-Handler pathway;"].
- Reaction grounding: NMN plus water yields NaMN and ammonium
  [RHEA:12400, nicotinamide-nucleotide amidase reaction].
- Evidence limit: Q88ME5 itself has not been assayed; GO:0019159 is accepted
  from coherent EC/domain/family evidence, not presented as direct experiment.
- OpenScientist correctly separated PncC NMN deamidation from PncA
  nicotinamidase chemistry and recovered the conserved family evidence. Its
  report also states that there is "No direct experimental characterization of
  the P. putida KT2440 protein" and that quantitative specificity has not been
  measured [file:PSEPK/pncC/pncC-deep-research-openscientist.md, "No direct
  experimental characterization of the P. putida KT2440 protein."]. Claims
  about NMN detoxification, cytoplasmic localization, and a target-level
  pyridine-nucleotide-cycle process are therefore retained as ortholog context
  rather than used for a NEW biological-process annotation.
- The report's 52.5% alignment identity and exact Ser27/Lys59 residue numbering
  are not used as curated evidence because the provider retained no alignment
  artifact from which those calculations can be reproduced.
- OpenScientist proposed PP_3298/Q88HQ5 as a second PncC. Direct UniProt review
  confirms a 167-aa TIGR00199/IPR008136/PF02464 protein but no EC, GO activity,
  PncC name, or experiment [UniProtKB:Q88HQ5, "SubName: Full=CinA domain protein"].
  It is included as a hole-filled, unresolved family paralog, not as a
  replacement for the better-annotated Q88ME5 or as a catalytic module member.
- PncA gap: exact searches of proteome UP000000556 found no `pncA`, EC 3.5.1.19,
  nicotinamidase name, IPR052347, NF008623, or PTHR11080 match. The ten broad
  PF00857 isochorismatase-fold proteins are not specific enough to nominate.
  Separate searches found no `nadV`, EC 2.4.2.12, or PTHR43816 match. PncC acts
  on NMN and must not be described as a replacement for either missing
  free-nicotinamide entry enzyme.

# Kcnj16 (rat) review notes

## Accession

- Task named A0A8I5ZPC6 (unreviewed TrEMBL). `just fetch-gene rat Kcnj16` resolved the
  Swiss-Prot entry P52191 (KCJ16_RAT), and the GOA file (19 rows) is keyed to P52191.
  A0A8I5ZPC6 (fetched from UniProt REST) carries the same gene: Name=Kcnj16, RGD:61824,
  GeneID 29719, 419 aa. P52191 also carries RGD:61824. Reviewed P52191.

## Key evidence

- Kir5.1 is non-functional alone and requires Kir4.1/Kir4.2
  [PMID:11306656 "The inwardly rectifying potassium channel Kir5.1 appears to form functional channels only by coexpression with either Kir4.1 or Kir4.2."]
  -> contributes_to GO:0005242. IBA row already has contributes_to; IEA (InterPro) and
  RGD ISO rows use enables -> WRONG_QUALIFIER source defects (CHECK).
- PMID:19665991 (full text read): Xenopus tropicalis orthologs mostly, but tandem
  XtKir4.1/ratKir5.1 constructs were recorded and behaved like rat Kir4.1/Kir5.1. So the
  RGD IDA potassium ion transport row does rest on rat Kir5.1 data (as heteromer).
- PMID:28931751 (abstract only): basolateral distal tubule localization; IDA accepted,
  consistent with UniProt and human ortholog.
- PMID:30605394 (full text): KO rats have metabolic acidosis and blunted CO2 chemoreflex;
  phenotypes -> KEEP_AS_NON_CORE for regulation of pH and response to CO2.

## Decisions

- GO:0006813 potassium ion transport (IEA, IDA) -> MODIFY to GO:0071805 potassium ion
  transmembrane transport (gene already has ISO row).
- GO:1990573 potassium ion import across plasma membrane (IBA) -> MODIFY to GO:0071805:
  net K+ flux through basolateral Kir4.1/Kir5.1 in the distal nephron is K+ recycling
  (exit) rather than import; direction is context dependent. GO:1990573 is_a GO:0071805
  (checked with OAK).
- GO:0016020 membrane (IEA/ISS/ISO) -> MODIFY to plasma membrane + basolateral plasma membrane.
- Plasma membrane and basolateral plasma membrane rows ACCEPT (plasma membrane kept
  because Kir5.1 also functions in non-polarized cells such as neurons).
- No NEW terms proposed.

# PTCD3 review notes

## Deep research

Automated deep research could not be generated: `just deep-research-falcon` failed
(Edison API 402 Payment Required; perplexity-lite fallback unavailable) and
`just deep-research-openai` failed with 401. The review uses cached literature and the
UniProt record directly.

## Literature used

- Davies et al. 2009 [PMID:19427859 "showed that it is a mitochondrial protein that associates with the small subunit of mitochondrial ribosomes"; "lowering PTCD3 in 143B osteosarcoma cells decreased mitochondrial protein synthesis"] (abstract only).
- Borna et al. 2019, COXPD51 [PMID:30607703 "PTCD3, a member of the pentatricopeptide repeat domain protein family, is a component of the small mitoribosomal subunit"; "Quantitative proteomic analysis revealed decreased levels of the small mitoribosomal subunits"].
- Aibara et al. 2020 human mitoribosome translation structures [PMID:32812867 "linker PPR protein mS39"].
- LRPPRC-SLIRP mitoribosome structure 2024 [PMID:39134711 "Here, the mRNA is handed to mS31–mS39, consistent with a translation initiation complex"].

## Curation decisions

- `ribosomal small subunit binding` (IDA/IBA/IEA) modified to `structural constituent of
  ribosome`: PTCD3 is now an established integral mitoribosomal protein (mS39), not a
  peripheral subunit-binding factor. The MRPS15 co-IP protein binding row from the same
  paper is modified to the same term; other protein binding rows (LNX2 Y2H, BioPlex,
  pestivirus Npro) removed.
- Mitochondrial inner membrane kept as non-core (whole-mitoribosome association).
- The mitochondrial matrix IDA (PMID:23275553) is accepted without a quote because the
  cached abstract does not mention PTCD3.

## Disease context (dismech)

dismech `Combined_Oxidative_Phosphorylation_Deficiency_51` used only as a literature lead.

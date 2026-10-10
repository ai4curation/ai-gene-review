# MRPS7 review notes

## Deep research

Automated deep research could not be generated: `just deep-research-falcon` failed
(Edison API 402 Payment Required; perplexity-lite fallback unavailable) and
`just deep-research-openai` failed with 401. The review uses the cached literature and
the UniProt record directly.

## Literature used

- Menezes et al. 2015, COXPD34 [PMID:25556185 "MRPS7 is a 12S ribosomal RNA-binding subunit of the small mitochondrial ribosomal subunit, and is required for the assembly of the small ribosomal subunit"]; rescue in patient fibroblasts [PMID:25556185 "Exogenous expression of wild-type MRPS7 in patient fibroblasts rescued complexes I and IV activities"].
- Amunts et al. 2015, human mitoribosome cryo-EM [PMID:25838379 "The head domain of the small subunit, particularly the messenger (mRNA) channel, is highly remodeled"] (abstract only).
- Greber and Ban 2016 review [PMID:27023846] (abstract only).

## Curation decisions

- Structural constituent of ribosome, rRNA binding, mitochondrial small ribosomal
  subunit and mitochondrial translation are the core annotations.
- mRNA binding (IBA) and generic RNA binding (HDA) kept as non-core: plausible/true but
  not the demonstrated function of the human protein.
- Mitochondrial inner membrane (Reactome TAS, NAS, ARBA) kept as non-core: reflects the
  peripheral membrane association of the whole mitoribosome; uS7m sits in the
  small-subunit head in the matrix.

## Disease context (dismech)

dismech `Combined_Oxidative_Phosphorylation_Deficiency_34` used only as a literature lead.

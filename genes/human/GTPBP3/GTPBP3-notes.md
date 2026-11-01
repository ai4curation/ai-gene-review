# GTPBP3 review notes

## Deep research

Automated deep research could not be generated for this review: `just deep-research-falcon`
failed (Edison API 402 Payment Required), the perplexity-lite fallback had no key, and
`just deep-research-openai` failed with 401. The review is built directly from the cached
primary literature listed below plus the UniProt record.

## Literature used

- Villarroya et al. 2008 [PMID:18852288 "We show that the two most abundant GTPBP3 isoforms exhibit moderate affinity for guanine nucleotides like their bacterial homologue, MnmE, although they hydrolyze GTP at a 100-fold lower rate"]
- Asano et al. 2018 [PMID:29390138 "we clearly showed that τm5U34 was absent from five mt-tRNAs in GTPBP3 KO cells"]; substrates are 5,10-CH2-THF and taurine, reconstituted with the GTPBP3-MTO1 complex.
- Peng et al. 2021 [PMID:33619562 "Here, we identified the mature form of hGTPBP3 and showed that hGTPBP3 is an active GTPase in vitro that is critical for tRNA modification in vivo"]; also describes the cytoplasmic splice isoform (UniProt isoform 4) [PMID:33619562 "Interestingly, hGTPBP3-Iso7 localizes in the cytoplasm but not mitochondria due to its distinct N-terminus"].
- Kopajtich et al. 2014, COXPD23 disease-gene paper [PMID:25434004 "Mutations in GTPBP3 are associated with a severe mitochondrial translation defect, consistent with the predicted function of the protein in catalyzing the formation of 5-taurinomethyluridine"].

## Curation decisions

- All 26 `protein binding` IPI rows come from binary Y2H interactome screens with
  partners unrelated to mitochondrial tRNA modification; removed as uninformative. The
  meaningful interaction (MTO1) is captured by GO:7770010 GTPBP3-MTO1 complex.
- `tRNA methylation` (IBA) marked over-annotated: the MnmE/MnmG reaction adds a
  taurinomethyl (methylene-taurine) group at C5 of U34, not a methyl group.
- `cytoplasm` IBA marked over-annotated (bacterial MnmE compartment); the EXP/IEA
  cytoplasm rows are kept as non-core because they reflect the minor isoform 4.

## Disease context (dismech)

dismech `Combined_Oxidative_Phosphorylation_Defect_Type_23` (COXPD23) is the corresponding
disease entry; it was used only as a lead for literature.

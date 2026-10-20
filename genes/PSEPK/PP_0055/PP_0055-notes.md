# PP_0055 (Q88RS4) notes

## Status of automated deep research

- 2026-10-19: `just deep-research PSEPK PP_0055 --provider falcon` failed ("All providers failed";
  falcon/Edison is returning an auth error for all users). Not retried; no `-deep-research-*.md`
  file was created. This review is grounded directly in UniProt, GOA, the RefSeq/PGAP record,
  genomic context (KEGG coordinates) and primary literature cached under `publications/`.

## Sequence and family

- 295 aa, unreviewed TrEMBL entry named only "Transcriptional regulator"
  [file:PSEPK/PP_0055/PP_0055-uniprot.txt "SubName: Full=Transcriptional regulator"].
- Canonical LysR-type transcriptional regulator (LTTR) architecture: N-terminal LysR HTH domain
  (PROSITE PS50931, residues 2-59, H-T-H motif 19-38) and a C-terminal LysR substrate-binding
  (periplasmic-binding-protein-like II) domain
  [file:PSEPK/PP_0055/PP_0055-uniprot.txt "DR   Pfam; PF00126; HTH_1; 1."]
  [file:PSEPK/PP_0055/PP_0055-uniprot.txt "DR   Pfam; PF03466; LysR_substrate; 1."].
- PANTHER PTHR30537 (HTH-type transcriptional regulator), subfamily SF3.
- RefSeq WP_010951464.1 is named "LysR family transcriptional regulator" by NCBI SPARCLE
  architecture 11426483, which supplies GO:0003677, GO:0003700 and GO:0006355
  [file:PSEPK/PP_0055/PP_0055-pgap-prediction-evidence/WP_010951464.1.gp].

## Genomic context (KEGG ppu, NC_002947)

| locus | strand/coords | product |
|---|---|---|
| PP_0053 | 61756..63024 (+) | sulfide:quinone oxidoreductase |
| PP_0054 | 62982..63839 (+) | membrane transporter (K07090) |
| **PP_0055** | complement(63828..64715) | LysR regulator (this gene) |
| PP_0056 | 64943..66595 (+) | GMC oxidoreductase, BetA-I / 3-hydroxypropionate dehydrogenase (hpdH) |
| PP_0057 | 66693..68312 (+) | MFS transporter |

PP_0055 is divergently transcribed from PP_0056 with a ~227 bp intergenic region (from KEGG
coordinates), the classic LTTR / target-operon arrangement.

## Identification as HpdR (3-hydroxypropionate-responsive activator of hpdH)

- Hanko et al. 2017 identified the P. putida KT2440 3-HP-inducible systems and their LTTRs
  [PMID:28496205 "we identify and characterise 3-HP-inducible promoters and their corresponding
  LysR-type transcriptional regulators from Pseudomonas putida KT2440"]. In P. denitrificans the
  3-HP catabolic operons each have a divergent LTTR
  [PMID:28496205 "In the opposite direction of each operon, a gene encoding a LTTR is located which
  was proposed to be required for 3-HP-inducible activation of gene transcription of its respective operon"].
- The KT2440 hpdR/hpdH intergenic region was ~233 bp
  [PMID:28496205 "the −233 bp long intergenic region was analysed for secondary structures"],
  matching the PP_0055/PP_0056 divergent gap (~227 bp by KEGG coordinates; small differences are
  expected from start-codon calls).
- hpdH is PP_0056 [PMID:41390427 "3-hpdh (PP_0056) is located in a separate operon and encodes a
  choline/3-hydroxypropionate dehydrogenase"], and PP_0056 is required for 3-HP degradation in a
  ΔmmsAB ΔPP_0488 background [PMID:41390427 "deletion of the third homolog, 3-hpdh (PP 0056), in this
  background generated the triple-deletion strain WT-ΔmmsΔ488Δ56, which completely lost the ability
  to degrade 3-HP for at least 144 h"].
- A review of P. putida expression systems states hpdR and hpdH form one divergent unit
  [PMID:34508142 "hpdH and its regulator hpdR in one operon"].
- Caveat: none of the cached papers prints the locus tag "PP_0055" for hpdR; the assignment is an
  inference from the shared divergent arrangement with PP_0056 (hpdH) and the intergenic length.
  It is strong (PP_0055 is the only gene divergent from PP_0056), but should be confirmed against
  the Hanko et al. supplementary sequences.

## Experimental function of HpdR (from PMID:28496205)

- PpHpdR/PhpdH is highly 3-HP-inducible in heterologous hosts
  ["PpHpdR/P hpdH are orthogonal and highly inducible by 3-HP in E. coli (12.3- and 23.3-fold,
  respectively) and Cupriavidus necator (51.5- and 516.6-fold, respectively)"].
- A conserved 40-nt promoter element is needed for HpdR-mediated activation
  ["a conserved 40-nucleotide sequence in the hpdH promoter, which plays a key role in HpdR-mediated
  transcription activation"].
- Direct DNA binding: ["we confirmed in vitro binding of HpdR to the native hpdH promoter region by EMSA"].
  Binding occurs without inducer, suggesting negative autoregulation (inferred, not tested)
  ["Protein-DNA complex formation occurs even under uninduced conditions likely indicating that HpdR
  is involved in negative autoregulation of hpdR transcription"].
- Effector range: 3-HP, and both enantiomers of 3-hydroxybutyrate
  ["show that it is also induced by both enantiomers of 3-hydroxybutyrate"]; levulinic acid also
  induces in KT2440 [PMID:34508142 "HpdR/PhpdH by 3HP or LA"].
- Phylogenetic grouping: ["Interestingly, HpdR belongs to group VI, which includes only a few
  LysR-type proteins."]
- PP_0056 (BetA-I) and PP_0057 are strongly induced on 1,4-butanediol vs glucose
  [PMID:32256468 "These include the GMC family oxidoreductase PP_0056 (BetA-I, along with its
  associated transporter PP_0057)"], consistent with a 3-hydroxyacid-responsive control of the
  PP_0056-0057 unit (4-hydroxybutyrate is a BDO oxidation intermediate), though HpdR's role there was
  not tested.

## Synthesis

PP_0055 = HpdR, an LTTR that binds the divergent hpdH (PP_0056) promoter and activates its
transcription in response to 3-HP (and 3-hydroxybutyrate / levulinate). Core MF: DNA-binding
transcription activator activity (GO:0001216); BP: positive regulation of DNA-templated
transcription (GO:0045893). No GO term exists for 3-HP catabolism or its regulation, so the
pathway context is recorded only in prose. Negative autoregulation is plausible but untested.

## Annotation decisions

- GO:0003677 DNA binding (IEA): TOO_GENERAL (entailed by GO:0043565 and GO:0001216).
- GO:0003700 DNA-binding TF activity (IEA): MODIFY -> GO:0001216.
- GO:0006351 DNA-templated transcription (IEA): MARK_AS_OVER_ANNOTATED (a TF regulates transcription;
  it is not part of the transcription process itself).
- GO:0006355 regulation of DNA-templated transcription (IEA): MODIFY -> GO:0045893.
- GO:0043565 sequence-specific DNA binding (IEA): ACCEPT (EMSA on the hpdH promoter).

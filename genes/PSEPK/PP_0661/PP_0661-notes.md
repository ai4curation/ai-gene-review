# PP_0661 (Q88Q37) notes

## Deep research status

`just deep-research PSEPK PP_0661 --provider falcon` failed twice on 2026-10-19 with
"Exception: Failed to authenticate" from the Edison API. Other reviews in the same batch
hit the same failure. No deep-research file exists for this gene. This review is based
on the UniProt record, GOA, InterPro and Pfam signatures, the RefSeq GenPept record, KEGG
genomic context, a small pairwise-alignment analysis (`PP_0661-bioinformatics/`), and
primary literature on the LysR family and on P. aeruginosa AmpR.

## Identity and domain architecture

- Unreviewed TrEMBL entry, 294 aa. The protein name comes from the 2002 genome submission:
  "SubName: Full=Transcriptional regulator AmpR {ECO:0000313|EMBL:AAN66286.1}"
  [file:PSEPK/PP_0661/PP_0661-uniprot.txt]. ECO:0000313 means submitter-imported and not
  vetted, so the name "AmpR" carries no evidential weight.
- Domains: an N-terminal LysR HTH, "FT   DOMAIN          7..64" with note "HTH lysR-type"
  (PROSITE PS50931), and an H-T-H motif at 24..43 (PROSITE-ProRule PRU00253). Signatures:
  "Pfam; PF00126; HTH_1; 1.", "Pfam; PF03466; LysR_substrate; 1.",
  "InterPro; IPR000847; LysR_HTH_N.", "InterPro; IPR005119; LysR_subst-bd." and
  "CDD; cd08432; PBP2_GcdR_TrpI_HvrB_AmpR_like; 1." [file:PSEPK/PP_0661/PP_0661-uniprot.txt].
- RefSeq WP_010951919.1 is named "LysR substrate-binding domain-containing protein". Its
  name evidence is "Evidence Accession :: NF015431.7" with "Source Identifier :: PF03466.26",
  and the CDD region is "PRK11139" with note "DNA-binding transcriptional activator GcvA;
  Provisional"
  [file:PSEPK/PP_0661/PP_0661-pgap-prediction-evidence/WP_010951919.1.gp].
- PANTHER PTHR30537 (HTH-TYPE TRANSCRIPTIONAL REGULATOR), subfamily SF79
  (TRANSCRIPTIONAL REGULATOR-RELATED). KEGG KO K03566 (GcvA-like).

## LysR family background

LysR-type regulators (LTTRs) have "an N-terminal DNA-binding helix-turn-helix motif and a
C-terminal co-inducer-binding domain" and "regulate a diverse set of genes, including those
involved in virulence, metabolism, quorum sensing and motility" [PMID:19047729]. So family
membership supports DNA-binding transcription factor activity and regulation of
transcription. It does not identify the target genes or the effector.

## Is it an AmpR?

- In AmpR systems, "The ampR gene is located adjacent to ampC and is divergently transcribed
  in C. freundii and E. cloacae, as well as in P. aeruginosa" [PMID:22479525]. P. aeruginosa
  AmpR "regulates the expression of a chromosomal β-lactamase AmpC" [PMID:22479525].
- In KT2440 the only class C beta-lactamase gene in KEGG (K01467) is PP_2876, about 2.5 Mb from
  PP_0661. Neither of its neighbours (PP_2875, PP_2877) is a LysR regulator
  [file:PSEPK/PP_0661/PP_0661-bioinformatics/RESULTS.md].
- Pairwise identity is 41.3% to P. aeruginosa AmpR (P24734) and 38.9% to E. coli GcvA
  (P0A9F6), so PP_0661 is not specifically closer to AmpR
  [file:PSEPK/PP_0661/PP_0661-bioinformatics/RESULTS.md].
- PP_0661 lies on the same strand as and adjacent to genes for sulfur amino acid and
  threonine metabolism: PP_0658 homocysteine S-methyltransferase, PP_0659 cystathionine
  gamma-synthase, PP_0660 S-methyl-L-methionine transporter and PP_0662 threonine synthase
  [file:PSEPK/PP_0661/PP_0661-bioinformatics/RESULTS.md].
- Conclusion: the "AmpR" name is a similarity-based submitter name from the shared
  GcdR/TrpI/HvrB/AmpR subgroup. Genomic context does not support it. The target genes are
  unknown; amino acid (methionine/threonine) metabolism is a hypothesis only.

## Literature search

Europe PMC returned no hits for "PP_0661", "PP0661" or "PP_RS03540" (searched 2026-10-19).
No experimental study of this protein was found. The KT2440 genome papers (PMID:12534463,
PMID:26913973) give only the sequence.

## Annotation decisions (summary)

- GO:0003700 DNA-binding transcription factor activity (IEA): ACCEPT, core.
- GO:0043565 sequence-specific DNA binding (IEA, TreeGrafter): ACCEPT. LTTR HTH domains bind
  specific operator sites.
- GO:0003677 DNA binding (IEA): TOO_GENERAL. It is entailed by GO:0043565, which is accepted.
- GO:0006355 regulation of DNA-templated transcription (IEA): ACCEPT. The direction of
  regulation is unknown, so no more specific term is warranted.
- GO:0006351 DNA-templated transcription (IEA): MARK_AS_OVER_ANNOTATED. A regulator does not
  carry out transcription, as in the PSEPK oxyR review.
- No NEW terms. Nothing supports a specific regulated process such as beta-lactam
  resistance or methionine biosynthesis.

## PGAP

PGAP names WP_010951919.1 from NF015431 (copy of PF03466), which has no GO terms, so PGAP
assigns no GO. The protein also matches NF012354 (copy of PF00126), which carries
GO:0003700 and GO:0006355, but PGAP keeps GO only from the naming model
[file:PSEPK/PP_0661/PP_0661-pgap-prediction-evidence/pgap_models.yaml]. Both terms are ones
this review accepts as core, so the empty PGAP GO set is a recall failure.

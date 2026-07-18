# BLVRB (Flavin reductase (NADPH) / Biliverdin reductase B) — review notes

UniProt: P30043 (BLVRB_HUMAN). HGNC:1063. 206 aa, cytosolic. Chromosome 19.
Source of most claims below: `file:human/BLVRB/BLVRB-uniprot.txt` and cached publications.

## Identity / nomenclature

- Recommended name in UniProt is **Flavin reductase (NADPH)** (Short=FR); EC=1.5.1.30.
  AltNames: **Biliverdin reductase B (BVR-B)**; **Biliverdin-IX beta-reductase** (EC=1.3.1.-);
  Green heme-binding protein (GHBP); NADPH-dependent diaphorase; NADPH-flavin reductase (FLR);
  S-nitroso-CoA-assisted nitrosyltransferase (SCAN), EC=2.6.99.-.
  [file:human/BLVRB/BLVRB-uniprot.txt "RecName: Full=Flavin reductase (NADPH)"; "AltName: Full=Biliverdin reductase B"]
- FR and BVR-B were shown to be the **same protein** [PMID:8687377, cited in UniProt RN[13] "Evidence that biliverdin-IX beta reductase and flavin reductase are identical."]

## Core enzymology

- Broad-specificity **NAD(P)H-dependent oxidoreductase**. UniProt FUNCTION:
  "Has a broad specificity oxidoreductase activity by catalyzing the NAD(P)H-dependent reduction of a
  variety of flavins, such as riboflavin, FAD or FMN, biliverdins, methemoglobin and PQQ (pyrroloquinoline quinone)"
  [file:human/BLVRB/BLVRB-uniprot.txt].
- **Biliverdin IXbeta -> bilirubin IXbeta** in fetal heme catabolism. UniProt: "Contributes to fetal heme
  catabolism by catalyzing reduction of biliverdin IXbeta into bilirubin IXbeta in the liver"; "Biliverdin IXbeta,
  which constitutes the major heme catabolite in the fetus is not present in adult"; "Does not reduce bilirubin IXalpha".
  Kinetics: KM=0.3 uM for biliverdin IX-beta [file:human/BLVRB/BLVRB-uniprot.txt].
- **Isomer specificity distinct from BLVRA**: BVR-B uses biliverdin IX-beta/-gamma/-delta but NOT IX-alpha;
  BVR-A (BLVRA) prefers IX-alpha [PMID:7929092 "Isozymes I and II used biliverdin-IX beta, -IX gamma, and -IX
  delta as substrates but not biliverdin-IX alpha, and isozymes III and IV preferred biliverdin-IX alpha"].
- **Flavin reductase kinetics**: reduces FMN, FAD, riboflavin with KM 52, 125, 53 uM respectively
  [PMID:10620517 "The enzyme was shown to catalyse the reduction of FMN, FAD and riboflavin, with K(m) values of
  52 microM, 125 microM and 53 microM, respectively."].
- **Ferric reductase** activity (NAD(P)H + FMN dependent) [PMID:10620517 "flavin reductase/biliverdin-IXbeta
  reductase has also been shown to exhibit ferric reductase activity"; UniProt "Can also reduce the complexed
  Fe(3+) iron to Fe(2+) in the presence of FMN and NADPH"].
- Single substrate-binding site; flavin and tetrapyrrole compete for the same site
  [PMID:11224564 "human BVR-B has a single substrate binding site, to which substrates and inhibitors bind
  primarily through hydrophobic interactions, explaining its broad specificity"; PMID:10620517 mesobiliverdin is
  a competitive inhibitor against FMN]. Monomer [PMID:11224564; UniProt SUBUNIT "Monomer."].
- Prefers NADPH over NADH (KM NADP 36 uM vs NADH 5.6 mM) [file:human/BLVRB/BLVRB-uniprot.txt kinetics].
- Catalytic mechanism: promiscuous; His-153 NOT required for catalysis (H153A/H153N retain activity)
  [PMID:18241201 "site-directed mutagenesis studies with both the H153A and the H153N mutant reveal that
  His(153) is not required for catalytic activity"].

## Localization

- **Cytosol / cytoplasm.** UniProt SUBCELLULAR LOCATION: "Cytoplasm" [file:human/BLVRB/BLVRB-uniprot.txt].
  [PMID:38056462 "BLVRB is mainly localized in the cytoplasm"]. HPA IDA cytosol (GO_REF:0000052).
  Detected in urinary exosomes in a large proteomics screen (non-specific; secreted/exosome contamination is
  common for abundant cytosolic proteins) [PMID:19056867].

## Physiological roles beyond fetal heme catabolism

- **Thrombopoiesis / megakaryocytopoiesis.** A loss-of-function redox mutation BLVRB(S111L) is causally
  associated with enhanced platelet production; BLVRB is a redox coupler whose defect causes ROS accumulation
  driving megakaryocyte lineage commitment [PMID:27207795 "identified a single loss-of-function mutation
  (BLVRB S111L) causally associated with clonal and nonclonal disorders of enhanced platelet production";
  "define the first physiologically relevant function of BLVRB ... governing terminal megakaryocytopoiesis"].
  This is an IMP for megakaryocyte differentiation (GO:0030219). BLVRB is a proposed thrombocytopenia drug target.
- **S-nitrosylation / insulin signaling (SCAN activity).** BLVRB acts as a SNO-CoA-assisted nitrosylase (SCAN):
  it transfers NO from SNO-CoA to target-protein cysteines (via BLVRB Cys-109/Cys-188 intermediates),
  S-nitrosylating INSR and IRS1, thereby **inhibiting insulin signaling** [PMID:38056462
  "uses SNO-CoA as its cofactor to S-nitrosylate multiple proteins"; "S-nitrosylation of INSR/IRS1 by SCAN
  reduces insulin signaling physiologically"]. Note: UniProt encodes this as EC=2.6.99.- (a transferase /
  nitrosyltransferase), and GO term GO:0035605 "peptidyl-cysteine S-nitrosylase activity" is the MF used.
  These are recent (2023) findings; a distinct enzymatic mode from the classical NADPH reductase.
- **Intermediary metabolism / stem-cell glutamine metabolism.** UniProt: "acts as a regulator of hematopoiesis,
  intermediary metabolism (glutaminolysis, glycolysis, TCA cycle and pentose phosphate pathway)"
  [file:human/BLVRB/BLVRB-uniprot.txt; PMID:29500232 (RN[23], FUNCTION)].

## Annotation-review reasoning summary

- Core MF: biliverdin reductase [NAD(P)H] activity (GO:0004074); riboflavin reductase (NADPH) activity
  (GO:0042602); FMN reductase (NADPH) activity (GO:0052873); FMN reductase (NADH) activity (GO:0052874).
  NADPH binding (GO:0070402) added as core (cofactor preference, structurally established).
  peptidyl-cysteine S-nitrosylase activity (GO:0035605) is a real second, recently-characterized MF (IDA,
  PMID:38056462) — kept as core but non-classical.
- Core BP: heme catabolic process (GO:0042167). Megakaryocyte differentiation (GO:0030219) is a real, IMP-backed
  downstream physiological role but not the enzyme's molecular core — KEEP_AS_NON_CORE. negative regulation of
  insulin receptor signaling pathway (GO:0046627) is IDA (PMID:38056462), a genuine but non-core/context role —
  KEEP_AS_NON_CORE.
- Location: cytosol/cytoplasm ACCEPT. extracellular exosome (GO:0070062, HDA, PMID:19056867) is a
  high-throughput proteomics detection typical of abundant cytosolic proteins — MARK_AS_OVER_ANNOTATED
  (do not treat as a functional site).
- Bare "protein binding" (GO:0005515, IPI, ANXA10) — MARK_AS_OVER_ANNOTATED (uninformative; policy: never REMOVE).
- IEA duplicates of experimentally-supported MF terms (riboflavin/FMN reductase, S-nitrosylase, neg reg insulin):
  the MF/BP is correct; where an experimental annotation to the same term exists, IEA is redundant but not wrong.
  ARBA IEAs (megakaryocyte diff, neg reg insulin, S-nitrosylase) transferred from mouse ortholog Q923D2 — the
  functions are corroborated experimentally in human, so KEEP (megakaryocyte/insulin as non-core) or ACCEPT
  (S-nitrosylase MF).
</content>

# CG4860 (Dmel\CG4860, FBgn0037999, UniProt Q9VGC2) — research notes

Research journal for the AI GO-annotation review of *Drosophila melanogaster* CG4860, a fatty
acid oxidation-family (acyl-CoA dehydrogenase) enzyme related to human ACADS/SCAD.

## Identity and sequence facts (from local UniProt record)

- UniProt: **Q9VGC2** (`Q9VGC2_DROME`), **Unreviewed (TrEMBL)**, 415 aa, 44,880 MW. Protein
  existence level `PE 3: Inferred from homology`.
- Names in the record are all electronic/rule-based:
  RecName `Short-chain specific acyl-CoA dehydrogenase, mitochondrial` and EC `1.3.8.1` come
  from **ARBA** (`{ECO:0000256|ARBA:...}`), AltName `Butyryl-CoA dehydrogenase` from ARBA.
  GN synonyms `ACAD11`, `ACADS` come only from `{ECO:0000313|EMBL:AAF54761.1}` (the genome
  submission), not from experiment.
- Gene: `Dmel\CG4860`, ORFName CG4860, FlyBase `FBgn0037999`, GeneID 41480, chromosome 3R.
- Family / domains (InterPro, Pfam, CDD): acyl-CoA dehydrogenase family. Three canonical ACAD
  domains present — N-terminal (PF02771, res 38–149), middle (PF02770, 154–248), C-terminal
  (PF00441, 260–408). CDD `cd01158; SCAD_SBCAD` (short-/branched-chain ACAD subfamily model).
  PANTHER `PTHR43884:SF12; ISOVALERYL-COA DEHYDROGENASE, MITOCHONDRIAL-RELATED`.
- Cofactor: FAD (flavoprotein), from ARBA/RuleBase.
- Pathway (ARBA): `Lipid metabolism; mitochondrial fatty acid beta-oxidation.`
- Catalytic activities listed (all ARBA-inferred, not curated from experiment on this protein):
  butanoyl-CoA (C4; RHEA:24004), pentanoyl-CoA (C5; RHEA:43456), hexanoyl-CoA (C6; RHEA:43464),
  each + oxidized ETF -> (2E)-enoyl-CoA + reduced ETF.
- Expression (Bgee, from record): `Expressed in adult Malpighian tubule (Drosophila) and 56
  other cell types or tissues.`
- **Important caveat**: every functional statement in the UniProt record carries an
  `ECO:0000256` (ARBA/RuleBase, automatic annotation) or `ECO:0000313` (imported) evidence code.
  There is **no experimental (`ECO:0000269`) characterization of Q9VGC2 itself** in the record.
  The FUNCTION text describing "short-chain specific ... acts specifically on acyl-CoAs with
  saturated 4 to 6 carbons long primary chains" is the generic ARBA rule text
  (`{ECO:0000256|ARBA:ARBA00045387}`), i.e. family boilerplate, not a measurement of CG4860.

## Two Drosophila ACADS-like genes: CG4860 vs Arc42 (CG4703)

Drosophila has (at least) two DIOPT-predicted orthologs of human ACADS: **Arc42** and **CG4860**.
The decisive fly-specific evidence comes from Geronazzo et al. 2025 (G3), who made CRISPR-Cas9
knockouts of putative FAO genes and read acylcarnitine profiles.

- Both predicted ACADS orthologs:
  [PMID:40519079 "Two different fly genes were predicted by DIOPT to be orthologs of human ACADS: Arc42 and CG4860"]
- CG4860 scored **lower** than Arc42:
  [PMID:40519079 "While CG4860 received a lower prediction score from the algorithm, they are both annotated on FlyBase as predicted orthologs of ACADS"]
  and [PMID:40519079 "Arc42 received a higher score, but both are annotated on FlyBase as orthologous to ACADS, so we were interested in observing both"]
- Human/mouse SCAD (ACADS) deficiency = elevated C4 (butyrylcarnitine):
  [PMID:40519079 "In human individuals with SCAD (short-chain acyl-CoA dehydrogenase) deficiency, the stereotypical acylcarnitine profile is dominated by elevated C4 (butyrylcarnitine)"]
- **Arc42** knockout mirrors ACADS loss (elevated C4); **CG4860 does not**:
  [PMID:40519079 "C4 was elevated in the homozygous Arc42 mutant flies, and this elevation was exacerbated in the starved condition, as expected"]
  [PMID:40519079 "In contrast, we did not observe an elevation of acylcarnitine C4 in the homozygous CG4860 mutant flies as compared to controls in either condition"]
- Instead, CG4860 knockout showed **lower** C4 and elevated C2 (acetylcarnitine):
  [PMID:40519079 "Instead, we observed a significantly lower concentration of C4, and a significant elevation of C2 (acteylcarnitine). This is the only genotype for which we observed an elevation in C2"]
- The authors' summary statement:
  [PMID:40519079 "the acylcarnitine profile for Arc42 loss of function mimics that of ACADS loss of function, while that of CG4860 does not"]
- Speculative interpretations of CG4860's actual role (explicitly hedged by the authors):
  [PMID:40519079 "Instead, we observe a significantly lower level of C4 in starved CG4860 knockout flies, which could indicate a role in SCAD synthesis. In addition, this is the only fly for which we observe a modest but significant elevation of C2, which could be related to a role in ketone utilization"]
- CRISPR allele: CG4860 carried a **1 bp deletion, predicted frameshift** (Table 4), and the
  KO was **viable** (acylcarnitine profiling was done on homozygous mutant adults, unlike the
  homozygous-lethal Etf-QO/CG7834). Table 4 records CG4860 phenotype as
  "Lower C4 acylcarnitine, elevated C2 acylcarnitine".

### Interpretation for annotation

The only *in vivo, fly-specific* functional test of CG4860 (Geronazzo et al. 2025) argues
**against** CG4860 being the enzyme responsible for short-chain (butyryl-CoA / C4) acyl-CoA
dehydrogenation in the fly — that role belongs to its paralog Arc42. CG4860 KO does not
accumulate C4; if anything C4 falls. So the ARBA-derived "**short-chain specific**" and
"**butyrate catabolic process**" annotations are over-specific for this particular paralog:
they are family/rule inferences that the direct experiment does not support (and partly
contradicts) for CG4860.

However, CG4860 is unambiguously a member of the **acyl-CoA dehydrogenase family** (domains,
CDD SCAD_SBCAD, FAD cofactor) and participates in **mitochondrial fatty acid beta-oxidation /
lipid catabolism**; its knockout perturbs the acylcarnitine (β-oxidation) pool. So the
general family-level MF (`acyl-CoA dehydrogenase activity`, oxidoreductase acting on CH-CH,
FAD binding), the mitochondrial localization, and the general fatty-acid β-oxidation process
remain reasonable. What is NOT supported is the confident restriction to the **short-chain /
butyryl-CoA (C4)** substrate class *for CG4860 specifically*.

This is consistent with the review task guidance: treat chain-length specificity cautiously;
mark over-specific chain-length claims as over-annotated where unsupported.

## Provenance of the existing GOA annotations (CG4860-goa.tsv)

- IBA (GO_REF:0000033, PANTHER PTN000097838 / PTN000856533) propagates short-chain ACAD
  activity (GO:0016937), mitochondrion (GO:0005739), FAO-using-ACAD (GO:0033539), and butyrate
  catabolic process (GO:0046359) from the ACADS/SCAD phylogenetic clade. These are family/clade
  inferences, not fly measurements.
- IEA: GO:0003995 (ARBA, GO_REF:0000120), GO:0016627 (InterPro), GO:0016937 (EC:1.3.8.1 ->
  GO_REF:0000003), GO:0050660 FAD binding (InterPro).
- ISS (GO_REF via FlyBase, WITH UniProtKB:Q709F0, cited PMID:22758915): GO:0003995 acyl-CoA
  dehydrogenase activity and GO:0006635 fatty acid beta-oxidation. Q709F0 is a peroxisomal-
  inventory-associated reference protein; the ISS is a homology transfer of the generic ACAD
  activity + β-oxidation, not a short-chain-specific claim. PMID:22758915 (Faust et al. 2012)
  is a Drosophila **peroxisomal proteome inventory** paper; its cached record is abstract-only
  (`full_text_available: false`) and the abstract does not mention CG4860 or SCAD specifically.

## Key conclusions for the review

1. `description`: SCAD-**like** / acyl-CoA-dehydrogenase-family mitochondrial flavoenzyme,
   predicted to act in fatty acid β-oxidation; **note substrate-specificity uncertainty** — the
   "short-chain specific / butyryl-CoA" designation is rule-based (ARBA/TrEMBL) and is not
   supported (and is partly contradicted) by the one in vivo fly knockout study, in which the
   paralog Arc42, not CG4860, reproduces short-chain (C4) ACADS deficiency.
2. Downgrade / flag the over-specific short-chain (GO:0016937) and butyrate catabolic
   (GO:0046359) annotations for CG4860; retain the general ACAD-family MF (GO:0003995),
   oxidoreductase (GO:0016627), FAD binding (GO:0050660), mitochondrion (GO:0005739), and
   general/ACAD-step fatty-acid β-oxidation (GO:0006635, GO:0033539) as reasonable.
3. Do NOT overrule the FlyBase ISS experimental-transfer annotations to the general terms
   (GO:0003995, GO:0006635) — those are the safe, family-level claims and are consistent with
   the KO perturbing the β-oxidation/acylcarnitine pool.

## References consulted
- UniProt Q9VGC2 (local record).
- PMID:40519079 — Geronazzo et al. 2025, G3, "Characterizing fatty acid oxidation genes in
  Drosophila." Full text available; directly assays CG4860. **Most important reference.**
- PMID:22758915 — Faust et al. 2012, Traffic, Drosophila peroxisomal proteome inventory.
  Abstract-only in cache; basis of the FlyBase ISS annotations (WITH Q709F0).
- Human ortholog review genes/human/ACADS/ACADS-ai-review.yaml for grounding.

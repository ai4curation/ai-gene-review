# EFM6 (YNL024C) — curation notes

UniProt: P53970 (EFM6_YEAST). SGD: S000004969. Systematic name YNL024C. 246 aa, 27.7 kDa.
Standard name EFM6 = "Elongation Factor Methyltransferase 6".

## Summary of identity / domain (from UniProt P53970 record, read inline)

- RecName: **Protein-lysine N-methyltransferase EFM6**; EC=2.1.1.- .
- SIMILARITY: "Belongs to the class I-like SAM-binding methyltransferase superfamily.
  METTL21 family. EFM6 subfamily." So EFM6 is a **seven-beta-strand (7BS) / Class I
  SAM-dependent methyltransferase**, specifically an MTase-Family-16 (MTF16 / Methyltransf_16)
  member. Pfam PF10294 (Methyltransf_16); InterPro IPR033684 (EFM6), IPR019410
  (Methyltransf_16), IPR029063 (SAM-dependent MTases superfamily). Gene3D 3.40.50.150.
  HAMAP MF_03198 (Methyltr_EFM6). PANTHER PTHR14614:SF152 "PROTEIN-LYSINE
  N-METHYLTRANSFERASE EFM6".
- **SAM-binding site present** (motif I and downstream elements): UniProt BINDING features
  for S-adenosyl-L-methionine at residues 51, 87-89, 115, 143, 169 (by similarity to human
  Q9H867 = METTL21A and HAMAP MF_03198). So the SAM-binding scaffold (motif I region and
  post-I) is intact → the protein is expected to be a competent SAM-dependent methyltransferase.
- SUBCELLULAR LOCATION: Cytoplasm (HAMAP + PubMed:14562095).
- Abundance: ~1760 molecules/cell in log-phase SD medium (PubMed:14562106).

## KNOWN (EFM6-specific experimental evidence)

The molecular function of EFM6 is firmly established — this gene is NOT functionally dark;
only its physiological/biological role is unknown.

- **EFM6 methylates eukaryotic elongation factor 1A (eEF1A; TEF1/TEF2) at Lys390.**
  [PMID:26115316 Jakobsson et al. 2015, "we here show that the YNL024C gene is required for
  methylation of eEF1A at Lys390, the only of these methylations for which the responsible
  MTase has not yet been identified"].
- Genetic dependence: [PMID:26115316, "Lys390 was found in a partially monomethylated state
  in wild-type yeast cells but was exclusively unmethylated in a ynl024cΔ strain"].
- Overexpression drives higher methylation: [PMID:26115316, "over-expression of Ynl024c
  caused a dramatic increase in Lys390 methylation, with trimethylation becoming the
  predominant state"]. Also [PMID:26115316, "when Ynl024c was overexpressed ... the di- and
  tri-methylated forms of Lys390 in eEF1A were the dominant species (>70% of total)"].
- Direct catalysis in vitro (crude extract, GTP-dependent): [PMID:26115316, "when GTP was
  present, a markedly stronger, Ynl024c-specific labelling was observed in the 50 kDa region
  of the ynl024cΔ yeast extract"] and [PMID:26115316, "Taken together, these results suggest
  that the Ynl024c protein is capable of directly methylating eEF1A ... but reflect KMT
  activity of Ynl024c on eEF1A"].
- High substrate specificity for eEF1A (does NOT methylate yeast Hsp70, unlike its closest
  human homolog METTL21A): [PMID:26115316, "the lysine in Ssa1/Ssb1/Ssb2 that correspond to
  the target site of human METTL21A in Hsp70 was exclusively found as unmethylated in cells
  overexpressing Ynl024c ... demonstrating that the enzyme is highly specific for eEF1A"] and
  [PMID:26115316, "yeast Hsp70 proteins are unmethylated ... consequently, that Ynl024c is
  likely not a functional orthologue of human METTL21A"].
- Domain/motif analysis (bioinformatics in the same paper): [PMID:26115316, "an alignment of
  Ynl024c with the human METTL21 proteins clearly demonstrates that Ynl024c harbours hallmark
  conserved motifs found in 7BS MTases, i. e. Motif I, Motif post I and Motif II ... Ynl024c
  possesses the characteristic DXXY ... motif"]. Predicted catalytic residues Asp170/Tyr173
  (DXXY), Trp143, Asp115 (post-I) [PMID:26115316].
- Cytoplasmic localization (global GFP study): [PMID:14562095 Huh et al. 2003] — HDA evidence
  in GOA; consistent with a translation-machinery-associated enzyme.
- Putative-MTase prediction (genome-wide bioinformatics, basis of ISS): [PMID:12872006 Katz,
  Dlakić, Clarke 2003, "automatic assignment of S-adenosylmethionine (AdoMet)-dependent
  methyltransferase functionality to genomic open reading frames"]; abstract-only.

## Separating EFM6 from the other EFM methyltransferases

eEF1A carries four methylated lysines, each installed by a distinct, dedicated enzyme
[PMID:26115316]:
- **Lys30** by **Efm1** (Yhl039w; a SET-domain enzyme, not 7BS) [PMID:26115316].
- **Lys79** by **Efm5** (YGR001C) [PMID:26115316].
- **Lys316** by **Efm4** / See1 (human ortholog METTL10) [PMID:26115316]. (The paper's
  abstract writes "Lys318" but the Results table and Discussion consistently write "Lys316";
  the Efm4/See1 site is the same eEF1A dimethylation regardless of the numbering slip.)
- **Lys390** by **Efm6** / Ynl024c (this gene) [PMID:26115316].

Other "Efm" enzymes act on eEF2, not eEF1A: Efm2 (YBR271W, eEF2 Lys613) and Efm3 (YJR129C,
eEF2 Lys509; human ortholog FAM86A/eEF2-KMT) [PMID:26115316]. Efm2 is EFM6's closest yeast
paralog (BLAST e=7e-7) but has a different substrate (eEF2). **Care must be taken NOT to
transfer eEF2 substrate or the other Lys sites to EFM6.** The Lys390-specific evidence is
uniquely attributed to YNL024C/EFM6.

Closest human homolog is METTL21A (HSPA-KMT; e=2e-17), but EFM6 is NOT its functional
ortholog (see Hsp70 result above). Lys390-equivalent (Lys392) in human/rabbit eEF1A is
unmethylated [PMID:26115316, "Lys392 was exclusively detected as unmethylated ... mammalian
METTL21 enzymes do not target this site"] — so the modification and, by extension, EFM6's
in-vivo role are not conserved to mammals.

## NOT known (genuine knowledge gaps)

- **Physiological/biological role of eEF1A-Lys390 methylation is unknown.** [PMID:26115316,
  "the precise function of Efm6-mediated eEF1A methylation does remain an enigma and further
  studies are required to reveal its role"]. No downstream biological process can be assigned
  → BP is legitimately ND.
- No growth/fitness phenotype tied to the methylation: [PMID:26115316, "simultaneous
  mutations of the four lysine methylation sites to arginine does not affect the proliferation
  rate of the resulting mutant yeast strain nor the enzymatic properties of the eEF1A protein
  in vitro"].
- The modification is low-occupancy (~20% mono in WT; a separate study ~5%) [PMID:26115316] —
  functional significance of such low stoichiometry is unclear.
- Recombinant soluble Efm6 could not be purified; direct activity shown only from crude
  extracts, so kinetics / a fully reconstituted single-protein assay are lacking
  [PMID:26115316, "We were unable to purify recombinant soluble Efm6 protein showing activity
  on eEF1A"].
- Whether EFM6 has additional substrates beyond eEF1A is untested (only Hsp70 excluded;
  eEF1A found via candidate approach).
- Regulation (whether Lys390 methylation responds to stimuli / cell state, possible demethylase)
  is speculative [PMID:26115316 Discussion].

## GO annotation review plan

7 GOA annotations:
1. GO:0008276 protein methyltransferase activity — IBA (GO_REF:0000033). Correct but general;
   EFM6 is specifically a protein-LYSINE N-MTase → MODIFY toward GO:0016279 as core; keep IBA
   framing. Actually the more specific GO:0016279 is already separately annotated (IEA), so
   ACCEPT this general IBA as a valid (if less specific) parent; core function captured by
   GO:0016279.
2. GO:0005737 cytoplasm — IEA (GO_REF:0000120, UniRule/SubCell). ACCEPT (redundant with HDA).
3. GO:0008757 SAM-dependent methyltransferase activity — IEA (ARBA). ACCEPT; general parent MF.
4. GO:0016279 protein-lysine N-methyltransferase activity — IEA (UniRule). ACCEPT — this is
   the correct specific MF, matching the experimental eEF1A-Lys390 result. CORE.
5. GO:0008757 SAM-dependent methyltransferase activity — ISS (PMID:12872006). ACCEPT; general
   parent, computational prediction consistent with experiment.
6. GO:0005737 cytoplasm — HDA (PMID:14562095). ACCEPT — experimental localization. CORE location.
7. GO:0008150 biological_process — ND (GO_REF:0000015). ACCEPT/KEEP — BP genuinely unknown
   (root ND); do not invent a BP. This IS the honest state given the enigmatic role.

Note: the strongest experimental MF evidence (PMID:26115316, IDA/IMP-grade eEF1A-Lys390) is
NOT itself in GOA as a separate row, but the IEA GO:0016279 term coincides with it. I will
cite PMID:26115316 in the review reasons and core_functions.

## Falcon deep-research (EFM6-deep-research-falcon.md) — corroboration + extra context

Falcon completed (1279 s, 11 citations) and is fully consistent with the primary paper. It
draws on PMID:26115316 plus a review I did not cache (Jakobsson, Małecki, Falnes 2018, RNA
Biology, "Regulation of eukaryotic elongation factor 1 alpha (eEF1A) by dynamic lysine
methylation", DOI:10.1080/15476286.2018.1440875). Extra context NOT added to the review YAML
(uncached review → no verifiable supporting_text; recorded here only, not as a GO claim):
- EFM6 expression reported to be upregulated by hypoxia → possible stress-responsive/regulatory
  role for Lys390 methylation (per the 2018 review). This strengthens the "regulated switch"
  hypothesis in the knowledge_gaps but is not itself GO-annotatable evidence for a BP.
- The "eEF1A code" framing: multiple dedicated KMTs install a combinatorial methylation pattern
  on eEF1A; methylation may also protect lysines from ubiquitin-mediated degradation (a role
  that would be preserved by K→R and thus masked in the quadruple-K→R mutant).
- Efm7 (EFM7) methylates eEF1A Lys3 (a fifth eEF1A KMT, post-dating the 2015 paper). So the
  full set of yeast eEF1A KMTs is Efm1 (Lys30, SET), Efm4/See1 (Lys316), Efm5 (Lys79),
  Efm6 (Lys390, this gene), Efm7 (Lys3). Care: keep EFM6 = Lys390 only.
- The alternate residue number "Lys395" seen in some reviews is a numbering variant of the same
  eEF1A site; the primary paper uses Lys390 (mature-protein numbering), which I follow.

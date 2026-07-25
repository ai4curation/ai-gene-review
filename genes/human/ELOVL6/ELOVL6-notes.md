# ELOVL6 (human) — review notes

UniProt: Q9H5J4 (ELOV6_HUMAN). Gene: ELOVL6 (HGNC:15829); synonyms FACE, LCE, hELO2, "Fatty acid elongase 2". 265 aa, 7 predicted TM helices, N-glycosylated at Asn2. HAMAP rule MF_03206 (VLCF_elongase_6). EC 2.3.1.199. Reference proteome UP000005640.

## Core biology (all grounded below)

ELOVL6 is a multipass ER-membrane condensing enzyme of the ELO family. It catalyzes the
first and rate-limiting step of the microsomal (long-chain) fatty-acid elongation cycle:
acyl-CoA + malonyl-CoA -> 3-oxoacyl-CoA + CO2 + CoA. The cycle is completed by KAR/HSD17B12
(reduction), HACD1-4 (dehydration) and TECR (second reduction), each a separate ER protein.

- Rate-limiting condensation step of the elongation cycle:
  [file:human/ELOVL6/ELOVL6-uniprot.txt "Catalyzes the first and rate-limiting reaction of the four"]
  and [PMID:25003994 "In the first, rate-limiting step, acyl-CoA is condensed with malonyl-CoA to form 3-ketoacyl-CoA"].
- Chain-length preference: elongates C12/C14/C16, highest toward C16:0; makes C18.
  [file:human/ELOVL6/ELOVL6-uniprot.txt "Condensing enzyme that elongates fatty acids with"] /
  [file:human/ELOVL6/ELOVL6-uniprot.txt "12, 14 and 16 carbons with higher activity toward C16:0 acyl-CoAs"].
  [PMID:25003994 "The FA elongase ELOVL6 is responsible for the conversion of C16-CoAs to C18-CoAs"].
- EC 2.3.1.199, Rhea RHEA:35315 (hexadecanoyl-CoA + malonyl-CoA -> 3-oxooctadecanoyl-CoA); also
  monounsaturated C16:1 -> C18:1 (RHEA:39675). Substrate profiling: [PMID:19575253] (Unifilter GF/C
  assay; ELOVL1,-3,-6 elongate saturated acyl-CoAs) and [PMID:20937905] (in vitro substrate
  specificities of all seven ELOVLs).

## Localization

ER membrane, multipass. [file:human/ELOVL6/ELOVL6-uniprot.txt "Endoplasmic reticulum membrane"];
EXP localization from [PMID:20937905]; IDA ER from same. HPA tissue-enhanced (liver); ubiquitous
tissue expression per UniProt.

## Enzyme complex / partners

The elongation-cycle enzymes act as a coordinated machinery. KAR (3-ketoacyl-CoA reductase,
= HSD17B12/second step) stimulates ELOVL6 ~3-fold independent of KAR catalysis (physical
interaction) and further in a catalysis-dependent manner [PMID:25003994
"Activity of purified ELOVL6 was enhanced by"; and see abstract "stimulated by the presence of
HSD17B12"]. UniProt ACTIVITY REGULATION:
[file:human/ELOVL6/ELOVL6-uniprot.txt "The reaction is stimulated by the presence of"] HSD17B12.
This underlies the GO:0009923 "fatty acid elongase complex" IDA (part_of) annotation.

Note on the two IPI "protein binding" annotations:
- PMID:32296183 (HuRI binary interactome; Luck et al. Nature 2020): Y2H binary hits HMOX1 (P09601),
  LCP2 (Q13094), RTP2 (Q5QGT7) — matches UniProt INTERACTION block. Large-scale, no ELOVL6-specific
  functional prose; treat as uninformative "protein binding".
- PMID:20937905 IPI WITH/FROM UniProtKB:Q96G23 (CERS6). This is from the ELOVL/CERS elongation-machinery
  study; still bare "protein binding" in GO terms.

## Metabolic physiology (mouse KO, human disease relevance)

ELOVL6 is a lipogenic, SREBP-regulated enzyme controlling the cellular C16/C18 ratio.
- Elovl6 KO mice: >=C18 FAs decreased, <=C16 increased; protects against high-fat-diet insulin
  resistance but causes pulmonary fibrosis [PMID:25003994 full text, Introduction].
- Stearate (C18:0) signalling: Drosophila dElovl6 (noa) loss reduces C18:0, is larval-lethal, and
  is rescued by human ELOVL6 [PMID:26214738 "the enzyme elongating C16 fatty acids to C18";
  "their lethality is rescued by human Elovl6"]. C18:0 regulates mitochondrial morphology/function
  via TFR1 stearoylation. This cross-species rescue/genetic-interaction is the IGI basis
  (WITH/FROM Drosophila Q9VV87) for the GO:0009922 and GO:0019367 IGI annotations.
- Brown adipose tissue: Elovl6 is necessary for BAT thermogenic capacity; converts C16 to C18 in BAT
  [PMID:26628376 "necessary for the thermogenic action of BAT"; "Elovl6 acts to convert C16 saturated
  and monounsaturated fatty acids to C18 fatty acids"]. Basis for the ISS/IEA
  "positive regulation of cold-induced thermogenesis" (GO:0120162) annotations, transferred from
  mouse Elovl6 (Q920L5).

## Annotation review reasoning (summary)

Core:
- MF GO:0009922 fatty acid elongase activity — ACCEPT (multiple EXP/IMP/IGI; EC 2.3.1.199).
- CC GO:0005789 ER membrane — ACCEPT (EXP + IBA); GO:0005783 ER IDA ACCEPT.
- CC GO:0009923 fatty acid elongase complex (part_of, IDA) — ACCEPT; ELOVL6 works with KAR/HSD17B12.
- BP GO:0019367 fatty acid elongation, saturated FA (IDA/IGI/IBA) — ACCEPT core; C16:0->C18:0.
- BP GO:0042759 long-chain fatty acid biosynthetic process (IDA) — ACCEPT (C18 is long-chain).

Non-core / broad but defensible (KEEP_AS_NON_CORE or ACCEPT):
- GO:0030497 fatty acid elongation (parent) — ACCEPT (accurate parent).
- GO:0034625 monounsaturated FA elongation — ACCEPT (C16:1->C18:1 documented in UniProt catalytic block).
- GO:0006633 fatty acid biosynthetic process; GO:0035338 long-chain fatty-acyl-CoA biosynthetic process
  (TAS Reactome + IEA) — ACCEPT as accurate higher-level process.
- GO:0120162 positive regulation of cold-induced thermogenesis — KEEP_AS_NON_CORE (downstream
  physiological role via C16->C18 in BAT; mouse-based ISS/IEA).

Over-annotations / broad:
- GO:0016020 membrane (IEA) — MARK_AS_OVER_ANNOTATED (uninformative parent of ER membrane).
- GO:0042761 very long-chain fatty acid biosynthetic process (IBA/IEA) — MARK_AS_OVER_ANNOTATED.
  ELOVL6 acts on C12-C16 substrates producing up to C18/C20; UniProt notes "to a lesser extent"
  contribution to VLCFA. C18 is long-chain, not VLCFA (>C20). ELOVL6 is not a principal VLCFA producer
  (that is ELOVL1/4/7); keep but flag as over-annotation rather than remove (IBA family-level transfer).
- GO:0034626 fatty acid elongation, polyunsaturated FA (IBA) — MARK_AS_OVER_ANNOTATED. PUFA elongation
  is the province of ELOVL2/ELOVL5; ELOVL6 preferentially elongates saturated/monounsaturated acyl-CoAs
  [PMID:19575253 abstract: ELOVL1/3/6 preferably elongate saturated, ELOVL2/5 the polyunsaturated].
- GO:0030148 sphingolipid biosynthetic process (IBA) — MARK_AS_OVER_ANNOTATED. Sphingolipid-destined
  saturated/monounsaturated VLCFAs are made mainly by ELOVL1/4; ELOVL6's C18 products are not the
  principal sphingolipid acyl chains. Family-level IBA transfer; keep, flag.
- GO:0006636 unsaturated fatty acid biosynthetic process (IEA UniRule) — KEEP_AS_NON_CORE; ELOVL6 does
  elongate monounsaturated C16:1->C18:1, so the term is partly supported but broad.

Uninformative:
- GO:0005515 protein binding x2 (IPI) — MARK_AS_OVER_ANNOTATED (bare "protein binding"; per policy do
  not REMOVE IPI). Real functional partner KAR/HSD17B12 captured by GO:0009923.

References that are TAS Reactome (R-HSA-548814, R-HSA-75876, R-HSA-1655835): titles left verbatim.
R-HSA-1655835 "Expression of ELOVL6" underpins the ER-membrane TAS location (weak; keep).

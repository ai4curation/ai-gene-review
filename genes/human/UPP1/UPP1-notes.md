# UPP1 (Uridine phosphorylase 1, Q16831) — review notes

## Identity and family
- Human gene `UPP1` (HGNC:12576), synonym `UP`; UniProt Q16831, 310 aa, EC 2.4.2.3
  [file:human/UPP1/UPP1-uniprot.txt "RecName: Full=Uridine phosphorylase 1"; "EC=2.4.2.3"].
- Belongs to the PNP/UDP phosphorylase family (nucleoside phosphorylase-I superfamily)
  [file:human/UPP1/UPP1-uniprot.txt "Belongs to the PNP/UDP phosphorylase family"].
- InterPro/PANTHER: Nucleoside_phosphorylase_d (IPR000845), Uridine_phosphorylase_euk
  (IPR010059), PANTHER PTHR43691:SF10 URIDINE PHOSPHORYLASE 1.

## Catalytic function
- Reversible phosphorolysis of uridine: `uridine + phosphate <=> alpha-D-ribose 1-phosphate + uracil`
  (RHEA:24388, EC 2.4.2.3), physiological direction left-to-right
  [file:human/UPP1/UPP1-uniprot.txt "Reaction=uridine + phosphate = alpha-D-ribose 1-phosphate + uracil"].
- Also acts on 2'-deoxyuridine: `2'-deoxyuridine + phosphate <=> 2-deoxy-alpha-D-ribose 1-phosphate + uracil`
  (RHEA:22824) [file:human/UPP1/UPP1-uniprot.txt "Reaction=2'-deoxyuridine + phosphate = 2-deoxy-alpha-D-ribose 1-"].
- Function summary: "Catalyzes the reversible phosphorylytic cleavage of uridine to uracil and
  ribose-1-phosphate which can then be utilized as carbon and energy sources or in the rescue of
  pyrimidine bases for nucleotide synthesis"
  [file:human/UPP1/UPP1-uniprot.txt "Catalyzes the reversible phosphorylytic cleavage of uridine"].
- Broad substrate specificity, can also accept deoxyuridine and analogues (Probable)
  [file:human/UPP1/UPP1-uniprot.txt "Shows broad substrate specificity and can"].
- Cloned and enzymatically characterized from human colorectal tumor line HCT116; recombinant enzyme
  in COS-7 cells showed "specific enzyme activity with uridine as the substrate; this activity was
  inhibited by the competitive inhibitor 2,2'-anhydro-5-ethyluridine"
  [PMID:7488099 "specific enzyme activity with uridine as the substrate"] (abstract-only cache;
  curated as IDA GO:0004850 / GO:0006218 by UniProt from the full text).

## Pathway context
- UniProt PATHWAY: "Pyrimidine metabolism; UMP biosynthesis via salvage pathway; uracil from uridine
  (phosphorylase route): step 1/1" (UniPathway UPA00574/UER00633)
  [file:human/UPP1/UPP1-uniprot.txt "UMP biosynthesis via salvage pathway"].
- Reactome places UPP1 in "Pyrimidine salvage" (R-HSA-73614) and "Pyrimidine catabolism"
  (R-HSA-73621); catalyzes the reversible reactions R-HSA-74372 / R-HSA-74376
  [reactome:R-HSA-74376 "Cytosolic uridine phosphorylase (isoforms UPP1 and UPP2) catalyzes the
  reversible reactions of uridine or deoxyuridine with orthophosphate to yield uracil"].
- Uracil liberated by UPP1 is further degraded by the reductive pyrimidine catabolic pathway
  (DPYD -> DPYS -> UPB1); the ribose-1-phosphate feeds the pentose pool. Uridine phosphorylase is
  "a ubiquitous enzyme involved in pyrimidine salvage and maintenance of uridine homeostasis"
  [PMID:19291308 "involved in pyrimidine salvage and maintenance of uridine homeostasis"].

## Quaternary structure (identical protein binding)
- Homodimer [file:human/UPP1/UPP1-uniprot.txt "Homodimer."].
- Crystallography confirms the human enzyme is dimeric (contrasting the hexameric microbial UPPs):
  [PMID:19291308 "is dimeric in contrast to the hexameric assembly present in microbial UPPs"];
  [PMID:20856879 "strictly dimeric complexes in eukaryotic organisms"]. The two annotations of
  GO:0042802 (identical protein binding, IPI, WITH UniProtKB:Q16831) capture this self-association.
- Structures: 3EUE, 3EUF (ligand-free / BAU-inhibited; 1.9 A) and 3NBQ (5-FU complex; 2.3 A).

## Localization
- Cytosolic enzyme (Reactome "Cytosolic uridine phosphorylase"; UniProt has no signal/TM features).
- GOA carries a nucleoplasm IDA (GO:0005654) from HPA (GO_REF:0000052). UPP1 has no known nuclear
  role; the physiologically supported and family-conserved location is the cytosol/cytoplasm. Treated
  as an over-annotation (HPA immunofluorescence localization), not removed (experimental IDA).

## Regulation / physiology
- Induced by vitamin D3 and inflammatory cytokines TNF, IL1, IFNG
  [file:human/UPP1/UPP1-uniprot.txt "By vitamin D3 and a mixture of inflammatory cytokines"].
- The GO:0042149 (cellular response to glucose starvation) annotation is IEA transferred from the rat
  ortholog (GO_REF:0000107, WITH ENSRNOP00000006765). Plausible but unverified in human; kept
  non-core.

## Pharmacology / disease relevance
- Activates fluoropyrimidine chemotherapeutics: 5-fluorouracil (5-FU) and its prodrug capecitabine;
  elevated tumor UPP levels contribute to drug selectivity. Specific inhibitors (e.g.
  5-benzylacyclouridine, BAU) raise endogenous uridine and protect normal tissue
  [PMID:19291308 "its role in the activation of pyrimidine nucleoside analogues used in chemotherapy,
  such as 5-fluorouracil (5-FU)"]. DrugBank: Fluorouracil, Capecitabine, 5-Benzylacyclouridine.

## Isoforms
- Isoform 2 ("Truncated", Q16831-2) diverges at residues 15-36 and is missing 37-310; annotated
  Inactive [file:human/UPP1/UPP1-uniprot.txt "[Isoform 2]: Inactive."].

## Curation decisions (summary)
- ACCEPT (core): GO:0004850 (MF, IBA+IEA+IDA), GO:0006218 (BP, IBA+IEA+IDA), GO:0005829 (CC,
  IBA+TASx2), GO:0005737 (CC, IEA), GO:0047847 (deoxyuridine phosphorylase, secondary catalytic
  activity documented by UniProt), GO:0044206 (UMP salvage, matches UniProt UniPathway pathway).
- MARK_AS_OVER_ANNOTATED: GO:0003824 (catalytic activity, root MF), GO:0016763 (pentosyltransferase,
  over-general parent), GO:0009116 (nucleoside metabolic process, over-general parent),
  GO:0006139 (nucleobase-containing compound metabolic process, over-general), GO:0005654
  (nucleoplasm IDA — experimental, not removed).
- REMOVE: GO:0009166 (nucleotide catabolic process, IEA) — UPP1 acts on the nucleoSIDE uridine, not
  on nucleoTIDES; wrong-branch electronic InterPro inference (correct process is pyrimidine nucleoside
  catabolism).
- KEEP_AS_NON_CORE: GO:0042149 (cellular response to glucose starvation, IEA from rat ortholog).
- ACCEPT (informative self-association, homodimer, structurally verified): GO:0042802 x2.
</content>
</invoke>

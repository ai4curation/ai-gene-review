# SLC7A2 (CAT-2) curation notes

UniProt: P52569 (CTR2_HUMAN). HGNC:11060. Chromosome 8p22. 658 aa, APC superfamily,
Cationic amino acid transporter (CAT) family, TC 2.A.3.3. 14 predicted TM helices.

## Core biology

SLC7A2 encodes cationic amino acid transporter 2 (CAT-2), a Na+-independent
facilitative transporter (permease) of the system y+ type for the cationic
(basic) L-amino acids L-arginine, L-lysine and L-ornithine (and the arginine
analogue L-homoarginine).

- UniProt FUNCTION: "Functions as a permease involved in the transport of the
  cationic amino acids (L-arginine, L-lysine, L-ornithine and L-homoarginine)"
  [file:human/SLC7A2/SLC7A2-uniprot.txt CC:FUNCTION].
- The transport mechanism is facilitated diffusion (uniport / equilibrative
  exchange), not a coupled symport or an obligate antiporter. UniProt records the
  reactions as equilibria with no co-transported ion, e.g.
  "Reaction=L-arginine(in) = L-arginine(out)"
  [file:human/SLC7A2/SLC7A2-uniprot.txt CC:CATALYTIC ACTIVITY]. Closs et al. show
  hCAT-2B has "transport properties consistent with y+" in Xenopus oocytes
  [PMID:9174363 "hCAT-1 and hCAT-2B demonstrated transport properties consistent with y+"].
- Substrate ChEBI IDs (verified against the UniProt CATALYTIC ACTIVITY Rhea
  cross-references): L-arginine CHEBI:32682, L-lysine CHEBI:32551,
  L-ornithine CHEBI:46911.

## Isoforms (functional, not location-specific)

Two major splice isoforms with distinct affinity (UniProt ALTERNATIVE PRODUCTS):
- Isoform 1 = CAT-2B / SLC7A2B (P52569-1, displayed). High affinity.
  KM = 0.32 mM for L-arginine [file:human/SLC7A2/SLC7A2-uniprot.txt].
- Isoform 2 = CAT-2A / SLC7A2A (P52569-2). Low affinity, high capacity.
  KM = 3.36 mM for L-arginine.
- Closs et al.: "hCAT-2A exhibited a 10-30-fold lower substrate affinity, a
  greater maximal velocity, and was much less sensitive to trans-stimulation at
  physiological substrate concentrations" [PMID:9174363]. CAT-2A is the
  liver/muscle form; CAT-2B is the inducible high-affinity form (immune cells).
- Both isoforms carry the same core MF (basic amino acid transmembrane transport)
  and the same substrate set; the GOA rows under review are not flagged as
  isoform-specific in GOA and the function is shared, so no `isoform:` field is
  applied to them. The affinity difference is the only isoform distinction and is
  recorded as kinetic parameters, not as separate GO functions.

## Not heteromeric

Unlike the SLC7 light chains (LAT1/LAT2/xCT etc.), CAT-2 is NOT one of the
heteromeric amino acid transporters: it functions on its own, without the
SLC3A2 (4F2hc) or SLC3A1 heavy chain. No in_complex / amino-acid-transport-complex
annotation should be modelled.

## Localization

Plasma membrane / cell membrane, multi-pass
[file:human/SLC7A2/SLC7A2-uniprot.txt CC:SUBCELLULAR LOCATION "Cell membrane"].
Confirmed by HPA immunofluorescence (GO_REF:0000052), by the Closs oocyte
expression (PMID:9174363), and by Yuan et al. who show "SLC7A2 protein was
exclusively accumulated on GSC membrane, as shown by immunofluorescence"
[PMID:37198486]. HPA also records a cell-junction localisation (IDA); this is a
peripheral plasma-membrane subdomain detail, not a distinct functional site.

## Physiological / disease roles (peripheral to core transport)

- Arginine supply to iNOS/NOS2 in macrophages. CAT-2B imports arginine that NOS2
  uses to make NO; UniProt notes "May play a role in classical or alternative
  activation of macrophages via its role in arginine transport (By similarity)"
  [file:human/SLC7A2/SLC7A2-uniprot.txt CC:FUNCTION]. This is substrate SUPPLY:
  the transporter imports the arginine, but NOS2 performs the NO-biosynthetic
  step and the activation signalling. By the participation test (CLAUDE.md), the
  transporter does not do any of the work of NO biosynthesis or of macrophage-
  activation regulation — it provides the substrate another enzyme consumes.
  Hence `regulation of macrophage activation` is over-annotation of the
  transporter (the regulatory work is done by NOS2 / downstream signalling), not
  a core or participatory function.
- Glioma stem cells (GSCs) upregulate SLC7A2 for lysine uptake: "GSCs upregulate
  SLC7A2 to increase lysine uptake and tumour growth"; SLC7A2 knockdown
  "dramatically reduced the intracellular levels of lysine" [PMID:37198486].
  This is direct functional (IMP/IDA) evidence that SLC7A2 imports L-lysine
  across the plasma membrane in human cells. The downstream histone
  crotonylation / tumour-immunity phenotype is executed by GCDH/CBP/ECHS1, not by
  the transporter.
- Blood-brain barrier: cationic-amino-acid (y+) transport operates at the BBB
  endothelium; the GOA NAS row cites a general BBB review (PMID:30280653) that
  does not itself name SLC7A2. Kept as a non-core tissue-context role.

## Action summary rationale

- Core MF: GO:0015174 basic amino acid transmembrane transporter activity
  (TAS from PMID:8954799), subsuming the ACCEPTed substrate-specific MF rows for
  L-arginine (GO:0061459), L-lysine (GO:0015189) and L-ornithine (GO:0000064).
- Generic MF rows (GO:0015171 amino acid transmembrane transporter activity,
  GO:0022857 transmembrane transporter activity) -> TOO_GENERAL (entailed by the
  specific MFs above).
- Core BP: substrate-specific transmembrane transport / import rows ACCEPTed;
  generic BP rows (GO:0006865, GO:0055085, GO:0089718) -> TOO_GENERAL.
- GO:0016020 membrane (IEA) -> MODIFY to GO:0005886 plasma membrane.
- GO:0043030 regulation of macrophage activation -> MARK_AS_OVER_ANNOTATED
  (arginine-supply trap; participation test fails).

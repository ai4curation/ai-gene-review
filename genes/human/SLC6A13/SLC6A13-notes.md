# SLC6A13 (GAT2 / GAT-2) curation notes

UniProt: Q9NSD5 (S6A13_HUMAN). HGNC:11046. Gene on chr12. 602 aa, 12 TM helices,
multi-pass membrane protein, SNF/SLC6 (TC 2.A.22) family, SLC6A13 subfamily.

## Core identity

SLC6A13 encodes GABA transporter 2 (GAT-2), one of four plasma-membrane GABA
transporters of the SLC6 (neurotransmitter:sodium symporter, NSS) family. It is a
secondary-active **Na+- and Cl--dependent symporter**: GABA uptake is coupled to
co-transport of 2 Na+ and 1 Cl- down their electrochemical gradients (symport, not
antiport, not uniport; monomeric carrier with no heavy chain / no heteromeric
complex).

- Function (experimental, human GAT-2): [PMID:17502375 "The transport was saturable and dependent on both Na(+) and Cl(-)"] and [PMID:17502375 "similar to rat GAT-2 and mouse GAT3 with high sensitivity"] toward GABA and beta-alanine.
- UniProt Rhea for the core reaction (CC:CATALYTIC ACTIVITY): 4-aminobutanoate(out) + chloride(out) + 2 Na(+)(out) = 4-aminobutanoate(in) + chloride(in) + 2 Na(+)(in); ChEBI GABA=CHEBI:59888, Na+=CHEBI:29101, Cl-=CHEBI:17996 (RHEA:70687). KM(GABA)=8.24 µM [PMID:17502375] / 26.2 µM [PMID:22932902].
- Structure/function: homology models on LeuT; Glu-48, Gly-51, Val-132 are key binding/transport residues (E48 mutations reduce uptake ~50-90%, G51A/G51L and V132I abolish GABA uptake) [PMID:22932902].
- GAT-2 is a "high selectivity/low affinity" transporter resistant to typical GABAergic inhibitors [PMID:22932902 "high selectivity/low affinity transporter that is resistant to inhibition by typical GABAergic inhibitors"].

## Substrate scope (broader than GAT1/GAT3 core)

GAT-2 carries, besides GABA, a range of small zwitterionic/β-amino substrates:
- **beta-alanine**: experimentally transported, Na+/Cl--coupled (UniProt Rhea RHEA:71247, CHEBI:57966) [PMID:17502375]; also a known inhibitor of GABA uptake.
- **taurine / hypotaurine**: by similarity to rodent ortholog (UniProt ECO:0000250|UniProtKB:P31649; taurine CHEBI:507393). Hence taurine:sodium symporter activity (GO:0005369) and taurine transmembrane transport (GO:0015734) are supported only by similarity → non-core.
- **guanidinoacetate (GAA)**: human GAT2 (and GAT3) directly transport GAA in heterologous cells; GAT2/GAT3 are the major astrocytic GAA uptake systems [PMID:29175673 "exhibited GAA transport, whereas CHO cells"; "play major roles in GAA uptake"]. Underlies the monocarboxylic-acid transporter/transport annotations (GO:0008028, GO:0015718). Genuine secondary physiological function (GAA homeostasis, creatine-pathway relevance) → KEEP_AS_NON_CORE.
- **5-aminolevulinic acid (ALA)**: GAT2 (with SLC6A6/TauT) mediates ALA uptake into cancer cells, driving ALA-induced protoporphyrin IX accumulation (relevant to photodynamic therapy) [PMID:24842606 "dependent on an increase in the uptake of"]. Underlies amino acid transmembrane transporter activity (GO:0015171) and amino acid import across plasma membrane (GO:0089718).

### Creatine is NOT a GAT2 substrate
Creatine transporter activity (GO:0005308) and creatine transmembrane transport
(GO:0015881) are ISS transfers from a rodent ortholog, but the dedicated creatine
transporter is SLC6A8/CRT. GAA (the creatine precursor), not creatine itself, is the
GAT2 substrate; in the GAA study creatine showed [PMID:29175673 "creatine, a substrate of creatine transporter (CRT)/Slc6a8"] had little inhibitory effect on GAT2-mediated GAA uptake. Treated as over-annotation.

## Localization

- **Plasma membrane** is the core location: direct evidence [PMID:22932902], IBA, IEA, ISS, Reactome TAS; UniProt "Cell membrane" (CC:SUBCELLULAR LOCATION). Mutant proteins also localize to the membrane in GAT-2 immunohistochemistry [PMID:22932902].
- **Basolateral cell membrane** by similarity to rodent ortholog (UniProt "Basolateral cell membrane", ECO:0000250|UniProtKB:P31649); relevant in kidney/liver epithelia. Accepted as a more specific, supported PM sub-location.
- **Mitochondrion** (GO:0005739, HPA IDA single immunofluorescence) conflicts with the robust plasma-membrane consensus for an SLC6 surface transporter → over-annotation (likely antibody/IF artifact).
- **Extracellular exosome** (GO:0070062, HDA urinary exosome proteomics) — standard membrane-protein detection in exosomes; real HDA but peripheral → non-core.
- **Presynapse** (GO:0098793, IEA inter-ontology inference from GABA reuptake) — GAT-2 is predominantly peripheral, not a major presynaptic reuptake transporter; the inference lacks direct localization support → over-annotation.

## Tissue / physiology

Expressed in liver, kidney, lung, testis, brain (leptomeninges) [UniProt "Expressed in brain, kidney, lung, liver and testis"; PMID:17502375 "GAT-2 mRNA is present in human"]. GAT-2 is "primarily expressed in the liver, kidney, and other peripheral tissues such as the testis, retina, and lungs" [PMID:22932902 "primarily expressed in the liver, kidney, and other peripheral tissues"]. Peripheral GABAergic homeostasis rather than synaptic reuptake is its principal role.

### Blood-brain barrier
GAT-2 is reported at the leptomeningeal/BBB interface; [PMID:22932902 "enriched at the BBB and might thus be a candidate transporter"] for translocation of 5-ALA through the BBB (from the authors' own mRNA data). The GOA "transport across blood-brain barrier" (GO:0150104) row is NAS and cites a general BBB review (PMID:30280653) that does not itself name SLC6A13; the better-supported source is PMID:22932902. The barrier/leptomeningeal role is plausible but peripheral to the core symport function → KEEP_AS_NON_CORE.

## IBA rows
GO:0005332 (MF), GO:0005886 (CC), GO:0006865 and GO:0035725 (BP) are PAINT/IBD
phylogenetic assertions for the SLC6 GABA-transporter clade. Q9NSD5 appears in its
own WITH/FROM for GO:0005332 and GO:0005886 — expected grounding (experimental
annotations on the target seeded the IBD), not circularity.

## Action summary rationale
- Core MF: GABA:sodium:chloride symporter activity (GO:0005332) — ACCEPT all rows.
- Core location: plasma membrane (GO:0005886) — ACCEPT; basolateral PM ACCEPT.
- Symporter-ancestor MF terms (GO:0005283 amino acid:sodium symporter, GO:0015370
  solute:sodium symporter, GO:0015185 GABA transmembrane transporter, GO:0015171
  amino acid transmembrane transporter) are strict is_a ancestors of GO:0005332 →
  TOO_GENERAL (verified via OLS).
- Process generality: neurotransmitter transport (GO:0006836) TOO_GENERAL vs GABA
  reuptake (GO:0051936); amino acid transport (GO:0006865) TOO_GENERAL vs amino acid
  import across PM (GO:0089718)/GABA import (GO:0051939) — is_a chains verified via OLS.
- Secondary substrates (taurine, GAA, ALA) → KEEP_AS_NON_CORE.
- Creatine, mitochondrion, presynapse → over-annotation.

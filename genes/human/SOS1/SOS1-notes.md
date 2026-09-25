# SOS1 (human, Q07889) curation notes

Journal for the GO annotation review of human SOS1 (Son of sevenless homolog 1),
HGNC:11187, gene ID 6654. Provenance for every assertion is given inline as
`[PMID:xxxx "verbatim supporting text"]` or from the UniProt record / deep-research file.

## Identity and architecture

- UniProt Q07889, 1333 aa, ~152 kDa multidomain guanine-nucleotide exchange factor (GEF).
  Domain order N→C (UniProt features + deep research): tandem histone folds → Dbl-homology
  (DH) domain (aa 200-390) → pleckstrin-homology (PH) domain (aa 444-548) → N-terminal
  Ras-GEF/REM domain (aa 597-741) → Ras-GEF/CDC25 catalytic domain (aa 780-1019) →
  disordered proline-rich C-terminal tail (aa ~1019-1333).
  [SOS1-deep-research-falcon.md "tandem histone folds → Dbl-homology (DH) domain → pleckstrin-homology (PH) domain → Ras exchanger motif (REM) → Cdc25 catalytic domain → proline-rich C-terminal tail"]
- PANTHER family PTHR23113 (GUANINE NUCLEOTIDE EXCHANGE FACTOR), subfamily PTHR23113:SF168
  (SON OF SEVENLESS HOMOLOG 1). Human paralog is SOS2. (UniProt DR lines)

## Core molecular function: RAS guanyl-nucleotide exchange factor (GO:0005085)

- The founding paper isolated hSos1 and showed its CDC25-related domain complements yeast
  CDC25 and stimulates nucleotide exchange on Ras.
  [PMID:8493579 "This hSos1 domain specifically stimulated guanine nucleotide exchange on mammalian Ras proteins in vitro"]
  and [PMID:8493579 "Thus hSos1 is a guanine nucleotide exchange factor for Ras."]
- GRB2 links receptor tyrosine kinases to SOS1: interaction is via the SOS1 C-terminus and
  the GRB2 SH3 domains.
  [PMID:8493579 "This interaction was mediated by the carboxyl-terminal domain of hSos1 and the Src homology 3 (SH3) domains of GRB2"]
- Mechanism: SOS1 does not synthesize/transfer GTP; the CDC25 helical hairpin engages Ras
  switch regions, disrupts nucleotide/Mg2+ binding, accelerates GDP release, and abundant
  cytosolic GTP then binds.
  [SOS1-deep-research-falcon.md "Its CDC25 helical hairpin disrupts Ras switch-region/nucleotide–Mg²⁺ interactions, accelerates GDP/Mg²⁺ release, and stabilizes nucleotide-free Ras; abundant cellular GTP then binds passively."]
- Substrates are the three canonical RAS isoforms (H-, N-, K-RAS).
  [SOS1-deep-research-falcon.md "SOS1 can activate the three principal vertebrate RAS isoforms—H-RAS, N-RAS and K-RAS"]
- Two Ras sites: catalytic (CDC25) and an allosteric REM–CDC25 site that binds Ras-GTP and
  gives positive feedback. Confirmed by MD/structure work.
  [PMID:38188543 "SOS1 facilitates the exchange of GDP to GTP thereby leading to activation of KRAS"]
  and [PMID:38188543 "The binding of GDP/GTP to KRAS at the REM/allosteric site of SOS1 regulates the activation of KRAS at CDC25/catalytic site by facilitating its exchange."]
- SOS1:RAS forms a defined complex targetable by small molecules and nanobodies.
  [PMID:25695162 "the discovery of three fragment binding sites on the Ras:SOS complex"]
  [PMID:39043660 "inhibit or facilitate the formation of the SOS1•RAS complex and modulate the nucleotide exchange rate on this pivotal GTPase in vitro as well as RAS signalling in cellulo"]

Decision: GO:0005085 (all evidence codes: EXP/IDA/IBA/IEA/TAS) = ACCEPT, this is the core MF.
The IBA (PANTHER:PTN000560991) sits on the RasGEF/CDC25 clade and is well grounded;
Q07889 correctly appears in its own WITH/FROM (experimental grounding on the target).

## GO:0005096 "GTPase activator activity" (TAS:ProtInc, PMID:9790532)

- GO:0005096 is the GAP term (stimulation of GTP hydrolysis). SOS1 is a GEF, not a GAP: it
  accelerates GDP release/nucleotide exchange, the opposite regulatory chemistry.
  This is a legacy ProtInc term-choice error.
  Decision: MODIFY → GO:0005085 guanyl-nucleotide exchange factor activity.

## Pathway position (RTK → GRB2 → SOS1 → RAS-GTP → RAF → MEK → ERK)

- SOS1 acts downstream of activated RTKs via GRB2 to load RAS with GTP.
  [SOS1-deep-research-falcon.md "activated receptor tyrosine kinase (RTK) → GRB2 → SOS1 → RAS-GTP → RAF → MEK → ERK"]
- EGF/insulin regulate distinct GRB2-SOS pools controlling Ras activation.
  [PMID:8663461 "Insulin and epidermal growth factor (EGF) stimulate a rapid but transient increase in the amount of GTP bound to Ras"]
- Decision: GO:0007173 (EGFR signaling), GO:0007265 (Ras protein signal transduction),
  GO:0007264 (small GTPase mediated signal transduction), GO:0051057 (pos reg of small
  GTPase signaling) = ACCEPT (core process / correct MF-linked processes).
- GO:0007165 "signal transduction" (NAS) is too general; a more specific term is present in
  the set. Decision: MODIFY → GO:0007265.

## RAC GEF / cytoskeletal role (secondary function)

- SOS1 DH-PH domain and an EPS8-ABI1(E3B1)-SOS1 complex link Ras signaling to Rac activation.
  Laminin/dystroglycan → Grb2-Sos1-Rac1-PAK1-JNK cascade.
  [PMID:16475793 "by way of Grb2-Sos1-Rac1-PAK1-JNK ultimately results in the phosphorylation of c-jun on Ser(65)"]
- p66Shc-Sos1 promotes Rac1 activation (PMID:16520382 title "Sos-mediated activation of rac1 by p66shc").
- The autonomous DH-domain Rho-GEF activity is contested; deep research flags it as
  context-dependent/less certain than the RAS-GEF assignment.
  [SOS1-deep-research-falcon.md "whether its DH domain is an autonomous physiological RAC-GEF is contested and less certain"]
- Decision: GO:0035022 (positive regulation of Rac protein signal transduction, IC) = ACCEPT
  as a genuine secondary function (RAC-directed exchange via DH-PH in complex).

## Localization

- Inactive SOS1 is cytosolic; catalysis occurs at the cytoplasmic face of the plasma membrane
  where lipid-anchored RAS resides.
  [SOS1-deep-research-falcon.md "SOS1 is primarily cytosolic when inactive but performs Ras exchange at the cytosolic face of the plasma membrane"]
- Decision: GO:0005737 cytoplasm (IDA), GO:0005829 cytosol (IEA + many Reactome TAS),
  GO:0005886 plasma membrane (IBA is_active_in + Reactome TAS) = ACCEPT.
- Neuronal/synaptic locations (GO:0043025 neuronal cell body, GO:0014069 postsynaptic
  density, GO:0098978 glutamatergic synapse; all IEA from rat ortholog) = KEEP_AS_NON_CORE
  (tissue-specific, not the general site of action).

## Molecular condensate scaffold (GO:0140693, IDA PMID:27056844)

- In reconstituted TCR signaling, pLAT-Grb2-Sos1 undergo phase separation into clusters that
  promote downstream signaling.
  [PMID:27056844 "Upon addition of Grb2 and Sos1, submicron-sized clusters formed within 1 minute and gradually grew in size"]
- Decision: ACCEPT (documented distinct MF; DisProt IDA).

## Adaptor / SH3-domain binding

- SOS1 proline-rich tail binds GRB2 SH3 domains (recruitment adaptor role).
  GO:0017124 SH3 domain binding (IEA) = ACCEPT (informative, mechanistically central).
- GO:0005154 EGFR binding (IEA rat ortholog): SOS1 co-precipitates with EGFR (IntAct
  Q07889;P00533); KEEP_AS_NON_CORE (real but non-core; recruitment is chiefly GRB2-mediated).
- GO:0019901 protein kinase binding (IEA mouse): SOS1 associates with kinases and is
  phosphorylated by ERK/RSK; generic but not GO:0005515; KEEP_AS_NON_CORE.

## GO:0005515 protein binding (many IPI rows)

- Per curation policy, generic `protein binding` (GO:0005515) carries no functional
  information. The functionally meaningful interactions are captured by specific terms:
  GRB2 (SH3 domain binding), EGFR (EGFR binding), RAS (GEF activity / GTPase complex).
- Decision: REMOVE all GO:0005515 rows as uninformative (removal does NOT assert the
  interactions are false; interactors include GRB2 P62993, HRAS P01112, EGFR P00533, NCK1
  P16333, CRK P46108, SHC1 P29353, PLCG1 P19174, PIK3R1 P27986, HCK P08631, etc.).
  Many are high-throughput interactome screens (PMID:28514442, 32296183, 33961781, 40205054,
  21988832, 34591642).

## GO:0006357 regulation of transcription by RNA Pol II (IDA PMID:23027131)

- PMID:23027131 is "Wnt4 inhibits cell motility induced by oncogenic Ras" — a study of
  Ras/Wnt4/miR-24 in transformed cells, not of SOS1 acting on RNA Pol II.
  [PMID:23027131 "we identified Wnt4 as an early target of Ras oncogenic signaling"]
- SOS1 is a cytoplasmic RasGEF; it performs no step of RNA Pol II transcription. Any
  transcriptional effect is indirect (Ras→MAPK→transcription factors).
- Decision: MARK_AS_OVER_ANNOTATED (indirect downstream effect; fails the participation test).

## GO:0046982 protein heterodimerization activity (IEA GO_REF:0000002, InterPro IPR009072)

- Mapped from the histone-fold InterPro signature. SOS1's histone folds are an intramolecular
  TANDEM pair (autoinhibitory regulatory module), not a heterodimerization interface with a
  partner protein. This InterPro2GO transfer is inappropriate for SOS1.
  [PMID:15507210 title "Structural analysis of autoinhibition in the Ras activator Son of sevenless"]
- Decision: REMOVE (demonstrably wrong IEA mapping for this protein).

## Downstream / pleiotropic processes (KEEP_AS_NON_CORE)

Real but context-specific or downstream of RAS activation, not SOS1's core function:
- GO:0008286 insulin receptor signaling; GO:0048009 IGF receptor signaling; GO:0048011 NTRK
  signaling; GO:0050853 BCR signaling; GO:0038095 FcεRI signaling; GO:0019221 cytokine
  signaling; GO:0007411 axon guidance; GO:0050900 leukocyte migration — SOS1 participates
  as the GRB2-recruited RasGEF node in each receptor pathway (Reactome/IEA). KEEP_AS_NON_CORE.
- GO:0042110 T cell activation (IDA PMID:7737275): CD28 binds GRB2/SOS.
  [PMID:7737275 "T cell antigen CD28 binds to the GRB-2/SOS complex, regulators of p21ras"] KEEP_AS_NON_CORE.
- GO:0042127 regulation of cell population proliferation (IDA PMID:9054499 oncogenic-Ras
  senescence; NAS PMID:38188543): downstream Ras-MAPK output. KEEP_AS_NON_CORE.
- GO:0002931 response to ischemia; GO:0042552 myelination; GO:0014044 Schwann cell
  development; GO:0045742 positive regulation of EGFR signaling (all IEA rat/mouse ortholog):
  developmental/pleiotropic. KEEP_AS_NON_CORE.

## GTPase complex (GO:1905360, part_of, IPI PMID:25695162 & PMID:39043660)

- SOS1 is a subunit of the RAS:SOS1 GTPase complex (ComplexPortal CPX-395/CPX-26660).
  [PMID:25695162 "the discovery of three fragment binding sites on the Ras:SOS complex"]
- Decision: ACCEPT.

## Disease (context, not core GO function)

- Germline gain-of-function SOS1 variants cause Noonan syndrome 4 (NS4) and, via a truncating
  gain-of-function, hereditary gingival fibromatosis type 1 (GINGF1). (UniProt DISEASE;
  PMID:17143282, PMID:17143285, PMID:11868160). RASopathy phenotypes are disease consequences
  of dysregulated RAS-MAPK signaling, not separate molecular functions — handled via
  KEEP_AS_NON_CORE where a matching process term exists, otherwise noted here only.

## Core functions (synthesis)

1. RAS guanyl-nucleotide exchange factor activity (GO:0005085) acting downstream of
   RTK/GRB2 in the Ras-ERK MAPK cascade (GO:0007265 / GO:0007173), at the plasma membrane.
2. RAC1 guanine-nucleotide exchange / positive regulation of Rac signaling (GO:0035022) via
   the DH-PH module in cytoskeletal/JNK signaling (secondary, context-dependent).
3. Adaptor / membrane-recruitment role: SH3-domain binding (GO:0017124) of GRB2, and
   molecular condensate scaffold activity (GO:0140693) in receptor signalosomes.

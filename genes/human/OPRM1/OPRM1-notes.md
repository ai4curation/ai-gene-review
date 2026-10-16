# OPRM1 (mu-type opioid receptor, MOR, P35372) — curation notes

## Deep research status (2026-10-15)

Automated deep research could not be generated for this review:

- `just deep-research-falcon human OPRM1 --fallback openai`: the Edison/Falcon
  auth endpoint returned `503 Service Unavailable` ("Failed to authenticate"),
  and the OpenAI fallback returned `401 invalid_api_key`. A second Falcon attempt
  failed the same way.
- `just deep-research human OPRM1 --provider perplexity`: provider not available
  in this environment (`Provider 'perplexity' not available. Available: openai,
  falcon, openscientist`).

No `-deep-research-*.md` file exists. The literature synthesis below was done
manually from the GOA-cited publications (cached by `just fetch-gene`) plus a
small set of additional key papers fetched with `just fetch-pmid` and checked
against their cached titles: PMID:8893006 (Oprm1 knockout), PMID:10617462
(beta-arrestin 2 knockout), PMID:22437502, PMID:26245379, PMID:29899455
(receptor structures) and PMID:27533032 (PZM21, G protein-biased agonist).

## Identity and family

- Class A (rhodopsin-like) GPCR; UniProt: "Belongs to the G protein-coupled
  receptor 1 family." InterPro: Mu_opioid_rcpt (IPR000105), Opioid_rcpt
  (IPR001418). Paralogs OPRD1, OPRK1, OPRL1.
- Many splice isoforms (18 named in UniProt), including 6TM MOR1K (isoform 12)
  and binding-incompetent SV1/SV2 (isoforms 16, 17).

## Molecular function: opioid receptor activity

- Human MOR was cloned and shown to bind opiates and opioid peptides in a
  G protein-sensitive way [PMID:7905839 "The expressed mu OR1 recognized tested
  opiate drugs and opioid peptides in a sodium- and GTP-sensitive fashion"].
- Mu-selective high-affinity binding [PMID:7891175 "Transient expression of this
  cDNA in COS-7 cells produced high-affinity binding sites to mu-selective
  agonists and antagonists"]; splice variants hMOR-1O/1X keep mu selectivity
  [PMID:12589820 "both variants showed high selectivity for mu opioids in binding
  assays"].
- Endogenous ligand beta-endorphin: the A118G (N40D) variant changes
  beta-endorphin binding and potency [PMID:9689128 "the A118G variant receptor
  binds beta-endorphin, an endogenous opioid that activates the mu opioid
  receptor, approximately three times more tightly than the most common allelic
  form of the receptor"].
- UniProt FUNCTION: "Receptor for endogenous opioids such as beta-endorphin and
  endomorphin" and "Receptor for natural and synthetic opioids including morphine,
  heroin, DAMGO, fentanyl, etorphine, buprenorphin and methadone"; enkephalins
  "By similarity".
- In vivo, MOR is the mandatory target of morphine [PMID:8893006 "a lack of mu
  receptors abolishes the analgesic effect of morphine, as well as
  place-preference activity and physical dependence"; "the mu-opioid-receptor
  gene product is the molecular target of morphine in vivo"].
- Structures (mouse receptor): antagonist-bound crystal [PMID:22437502],
  agonist + G protein mimetic nanobody [PMID:26245379], DAMGO-MOR-Gi cryo-EM
  [PMID:29899455 "mediated by μOR signalling through the adenylyl
  cyclase-inhibiting heterotrimeric G protein Gi"].

## Signaling (Gi/o arm)

- Adenylyl cyclase inhibition by human MOR in heterologous cells
  [PMID:14573758 "DAMGO inhibition of forskolin-stimulated adenylyl cyclase"]
  [PMID:19788913 "RanBPM had no effect on MOP-mediated inhibition of adenylyl
  cyclase"] [PMID:7957926 "Both receptors show similar ligand binding and coupling
  to cAMP in CHO-K1 cells"].
- G beta-gamma effectors: GIRK activation [PMID:7891175 "This receptor displays
  functional coupling to a recently cloned G-protein-activated K+ channel"];
  UniProt also lists inhibition of N- and L-type Ca channels, PLC, MAPK (mostly By
  similarity). MOR does not itself have channel activity; the ISS "voltage-gated
  calcium channel activity" row confuses an effector with the receptor.
- Canonical MOR1 couples to Gi/o, whereas the 6TM MOR1K isoform couples to Gs
  and is retained intracellularly [PMID:20525224 "unlike MOR1, which couples to
  the inhibitory Galphai/o complex, MOR1K couples to the stimulatory Galphas
  complex"].

## Regulation: GRK / beta-arrestin, desensitization, bias

- Kinase-modulated desensitization of human MOR [PMID:7891175 "The extent of
  desensitization was potentiated by both the multifunctional
  calcium/calmodulin-dependent protein kinase and protein kinase C"].
- beta-arrestin 2 limits morphine analgesia in vivo [PMID:10617462 "Functional
  deletion of the beta-arrestin 2 gene in mice resulted in remarkable
  potentiation and prolongation of the analgesic effect of morphine"].
- Biased ligands: [PMID:27533032 "PZM21-a potent Gi activator with exceptional
  selectivity for μOR and minimal β-arrestin-2 recruitment"]. Whether arrestin
  vs G protein signaling separates analgesia from respiratory depression is
  contested in later literature (not cached here); GO currently has no way to
  distinguish G protein-biased from arrestin-dependent MOR signaling.
- Interactors modulating trafficking: filamin A [PMID:14573758
  "agonist-induced receptor down-regulation and functional desensitization were
  virtually abolished in cells lacking filamin A"], RanBPM [PMID:19788913],
  WLS/GPR177 [PMID:20214800 "morphine treatment promotes formation of MOR/GPR177
  complexes. This in turn results in sequestration of GPR177 and inhibition of
  Wnt protein secretion."].

## Location

- Plasma membrane (multiple EXP papers; UniProt "Cell membrane"); neuronal
  axon, dendrite, perikaryon, endosome by similarity to guinea pig OPRM1 (P97266; the rodent ISS donor is guinea pig, while the GO_REF:0000107 IEA donor P42866 is mouse); "Is rapidly
  internalized after agonist binding".

## Annotation-review judgements (summary)

- GO:0004930 GPCR activity -> MODIFY to morphine receptor activity
  (GO:0038047) and beta-endorphin receptor activity (GO:0004979).
- Generic GPCR signaling / cyclic-nucleotide / ACh-pathway rows -> MODIFY to
  GO:0031635 adenylate cyclase-inhibiting opioid receptor signaling pathway
  (is_a GO:0007193 and GO:0038003, checked in OLS).
- voltage-gated calcium channel activity (ISS from rat P33535) and the derived
  IEA calcium ion transmembrane transport -> REMOVE (receptor inhibits channels;
  it is not a channel).
- 21 protein binding IPI rows -> REMOVE as uninformative (interactions not
  disputed).
- PMID:21039637 (human craving genetics, abstract-only): stress-induced craving
  result in the abstract is for CRH-BP, OPRM1 is associated with cue-induced
  craving; "regulation of cellular response to stress" left UNDECIDED.
- ER/Golgi TAS rows from PMID:9242668 (insect-cell overexpression, abstract
  only, abstract does not mention these compartments) left UNDECIDED.

## Review round 2 (PR #5042) additions

- PENK peptide (P01210-PRO_0000008243) IPI row: UniProt "P35372; PRO_0000008243
  [P01210]: PENK; NbExp=3"; MODIFY to GO:0004985 (endogenous opioid peptide
  ligand), not REMOVE.
- Mouse sources traced via QuickGO for P42866: GO:0050769 IMP
  [PMID:16682964 "implicating a role for receptor-receptor interactions in
  modulating neuritogenesis"]; GO:0098982 SynGO [PMID:31818459 "this release was
  attenuated by presynaptic mu opioid receptors (MORs) activation"].
- Ethanol: [PMID:10869404 "In no case did knockout mice show evidence of
  ethanol self-administration"].

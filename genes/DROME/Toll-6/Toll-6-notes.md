# Toll-6 (Q9VUN0, FBgn0036494) curation notes

## Literature search (2026-11-06)

No deep-research API keys were available, so no `-deep-research-<provider>.md` file
was generated. Searches run instead:

- PubMed `Toll-6 Drosophila` (23 hits: 42455660, 41656993, 40551010, 39704728,
  38838299, 38650964, 35732124, 35134382, 31477571, 30745142, 30361090, 28846707,
  28405401, 28373203, 27502486, 26150191, 25741726, 25363762, 23892553, 21158756,
  19602393, 12084571, 10973475). 38838299, 28405401, 19602393 concern the D42-GAL4
  driver inserted near toll-6 and are not about Toll-6 function; 12084571 is a
  silkworm Toll; 26150191 is a commentary.
- Newly cached with `just fetch-pmid`: 27502486, 35134382, 21158756, 15179511,
  35732124, 31477571, 40551010, 41656993, 38650964, 42455660, 12617819.
- FlyBase hand-written description (`Toll-6-deep-research-flybase.md`).

## Neurotrophin receptor (core)

- Toll-6 and Toll-7 are receptors for Drosophila neurotrophins DNT1 (Spz2, NT1) and
  DNT2 (Spz5) [PMID:23892553 "Here we show that Toll paralogs unrelated to the
  mammalian neurotrophin receptors function as neurotrophin receptors in fruit flies."].
- Binding: [PMID:23892553 "This indicates that DNT2 interacts with both Toll-6 and Toll-7."];
  binding is promiscuous [PMID:28373203 "Thus, binding of DNT1 and 2 to Toll-6 and -7 is promiscuous."].
- Loss of function: [PMID:23892553 "Altogether, our data show that Toll-6 and Toll-7 are
  required for locomotion, motor-axon targeting and neuronal survival."]
- Membrane localization: [PMID:23892553 "In Toll-6MIMICGFP, GFP is mostly cytoplasmic
  whereas Toll-6 is localised to the membrane"].
- Signalling: MyD88-dependent survival [PMID:28373203 "Collectively, these data show that
  Toll-6 and -7 signal via the canonical MyD88 pathway to promote neuronal survival in the
  CNS."]; DNT2 activates NF-kB through Toll-6 in S2 cells [PMID:28373203 "This shows that
  Toll-6 and -7 activate NF-κB signaling downstream of DNT2."]; Toll-6 can also induce
  apoptosis (pupae), independently of MyD88 via Wek/Sarm/JNK; dSarm does not bind Toll-6
  directly [PMID:28373203 "Thus, dSarm does not bind Toll-6 or -7, meaning that dSarm does not
  directly mediate the proapoptotic function of Toll-6."].
- Toll-6-dSARM-FoxO pathway in motoneurons, microtubule dynamics, axon transport and
  structural plasticity [PMID:27502486 "the Toll-6 receptor, the Toll/interleukin-1 receptor
  domain adaptor dSARM, and FoxO function in a linear pathway"].

## Synaptic plasticity

- NMJ: DNT2 from muscle acts on Kek-6 and Toll-6 in motoneurons [PMID:28846707 "Kek-6 and
  Toll-6 interact physically, and together regulate structural synaptic plasticity and
  homeostasis."]; "Toll-6 is required for active zone formation" (PMID:28846707).
- Dopaminergic circuit in adult brain [PMID:39704728 "Loss of function for DNT-2 or its
  receptors Toll-6 and kinase-less Trk-like kek-6 caused DAN and synapse loss, impaired
  dendrite growth and connectivity, decreased synaptic sites, and caused locomotion
  deficits."].
- Toll-receptor map underlying adult brain structural plasticity (PMID:32066523; Toll-2
  focus, cached but not cited in the review).

## Wiring (olfactory)

- [PMID:25741726 "Toll-6 and Toll-7, members of the Toll receptor family best known for
  functions in innate immunity and embryonic patterning, cell autonomously instruct the
  targeting of specific classes of PN dendrites and ORN axons, respectively"]. Toll-6 acts in
  PNs; it also non-autonomously affects VA1d ORN axon targeting. Cytoplasmic domain is
  dispensable [PMID:25741726 "Lastly, we found the cytoplasmic domains of Toll-6 and Toll-7 to
  be dispensable for their activities in PNs and ORNs, respectively, suggesting that these
  receptors signal through a non-canonical co-receptor mechanism."]. So this wiring role is
  a cell-surface recognition role, not neurotrophin signalling via TIR.
- ER proteins Meigo and Gp93 regulate Toll-6 localization in PNs for dendrite targeting
  (PMID:35134382, abstract only).

## Embryonic convergent extension

- Positional Toll code: [PMID:25363762 "These results demonstrate that Toll-2, Toll-6, and
  Toll-8 act in combination to regulate axis elongation."] and [PMID:25363762 "These results
  demonstrate that Toll-2, Toll-6, and Toll-8 promote cell intercalation during axis
  elongation."]. Toll-6 is one of three redundant stripe-expressed receptors; non-core.
- Long Tolls (Toll-2, -6, -7, -8) mediate interface surveillance in imaginal discs
  (PMID:41656993); striped LRR proteins and compartment boundaries (PMID:38650964). Not
  annotated.

## Other contexts (not annotated, peripheral)

- Glia: neuronal apoptosis processes Spz5, which activates a dSARM-mediated Toll-6 pathway
  in glia controlling Draper expression [PMID:30745142 "This cue activates a dSARM-mediated
  Toll-6 transcriptional pathway in glia, which controls the expression of the Draper
  engulfment receptor."].
- Tumour models: Toll-6 required for tumour cell migration/invasion via JNK (PMID:31477571);
  fat-body Spz5 acting via Toll-6/alpha-Spectrin/Hippo in cell competition (PMID:35732124,
  abstract only); adipose Spz5-Toll-6-Hh in tumour progression (PMID:40551010); Upd3/Spz5/
  Toll-6 in bitter taste neurons (PMID:42455660, abstract only). These are all Spz5-Toll-6
  signalling in different cell types; consistent with the receptor function, not separate
  molecular functions.
- Immunity: Toll-6 mutants are viable and have no AMP induction defect [PMID:21158756
  "Analysis of loss of function alleles of Toll-6, Toll-7 and Toll-8 showed that the single
  mutants were mostly viable with some leg defects."]; UniProt records normal AMP induction
  in Toll-6 mutants.

## PANTHER placement and the Slit-node IBAs

- UniProt DR PANTHER: PTHR24366:SF96 (HMM). PANTHER 19 tree: PTHR45836:SF8 "TOLL-LIKE
  RECEPTOR 6" inside the SLIT HOMOLOG family, hence IBAs from Slit nodes PTN002911633
  (Roundabout binding, heparin binding; Bilateria) and PTN002911625 (axon guidance; family
  root). `interpro/panther/PTHR45836/PTHR45836-review.yaml` already flags PTN002911633 as
  NEEDS_PRUNING for SF8 (Roundabout binding).
- Biological argument: Toll-6 is an LRR + TM + TIR receptor (UniProt: signal 1..14,
  TM 1058..1078, TIR 1111..1244) of the Toll-like receptor family; it has none of the Slit
  EGF repeats, laminin-G or C-terminal cystine-knot domains. Its closest paralogs are the
  long Tolls 18w/Toll-2, Toll-7, Toll-8 [PMID:21158756 "Overexpression of Toll and Toll-9
  suggested their functional similarities, while 18w, Toll-6, Toll-7 and Toll-8 often
  showed related phenotypes."]. Placement in the Slit clade is an LRR-driven tree artifact.
  Robo binding is a Slit ligand property; no study reports Toll-6/Robo interaction ->
  REMOVE. Heparin binding is untested for Toll-6; LRR ectodomains can bind heparin, so
  MARK_AS_OVER_ANNOTATED rather than REMOVE. Axon guidance is independently true for Toll-6
  (motor axon targeting, PMID:23892553; VA1d ORN axon targeting, PMID:25741726) so the IBA
  row is accepted on that evidence despite the wrong ancestral source.
- `just paint-losses DROME Toll-6`: no IRD/IKR on lineage (Q9VUN0 not a leaf of PTHR24366).

## Signal transduction IMP (PMID:31088910)

Full text cached; Toll-6 appears only in citations of McIlroy 2013 and of a Toll-1/TIR
chimera study. I could not find Toll-6 data in the cached text (possibly supplementary).
Row left UNDECIDED; the IEA row is modified to neurotrophin signaling pathway.

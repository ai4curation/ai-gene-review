# mstE (Q5B0S0, AN5860) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: MstE is the closest experimentally characterised relative of N. crassa GLT-1
(Q1K4S3); its findings will be used as a reference for transfer. This review does not
use any ProtNLM2 output.

### Setup and provenance

- `just fetch-gene EMENI mstE` failed to resolve the symbol (the TrEMBL entry carries
  only ORF name ANIA_05860); rerun with `--uniprot-id Q5B0S0` succeeded (15 GOA rows).
- Deep research failed: falcon returned "Failed to authenticate" and the
  perplexity-lite fallback returned HTTP 401 (insufficient quota). No deep-research file
  exists; the review relies on the literature below, read directly.
- The primary paper PMID:16418173 (Forment et al. 2006, JBC) is cached abstract-only.
  The JBC/Academia full-text routes returned 403. The AspGD IDA rows for mannose
  transporter activity and vacuole cannot be traced to text I can read, so they are
  left UNDECIDED rather than overruled.
- Additional cached full-text papers: PMID:24751997 (MstA/MstC, Forment 2014),
  PMID:24282591 (dos Reis 2013, HxtB-E), PMID:28361917 (HxtB signalling),
  PMID:28115989 (N. crassa GLT-1/HGT-1/-2), PMID:33509260 (RCO-3/COL-26).

### What is experimentally established for MstE in A. nidulans (PMID:16418173, abstract)

- Low-affinity glucose transporter active in germinating conidia on glucose
  ["The mstE gene encoding a low affinity glucose transporter active during the germination of Aspergillus nidulans conidia on glucose medium has been identified."].
- Deletion abolishes low-affinity glucose uptake kinetics, revealing a high-affinity
  system; no morphological phenotype
  ["Deletion of mstE has no morphological phenotype but results in the absence of low affinity glucose uptake kinetics, the latter being substituted by a high affinity system"].
- Expression in hyphae, induced by repressing carbon sources, CreA-dependent
  ["is dependent on the function of the transcriptional repressor CreA"].
- MstE-sGFP at the periphery of conidia and hyphae, consistent with plasma membrane
  ["fluorescence at the periphery of conidia and hyphae is consistent with MstE location in the plasma membrane"].
- Later work treats MstE as the reference low-affinity system
  [PMID:24751997 "Until very recently, the only A. nidulans monosaccharide uptake system to have been characterised biochemically, physiologically and genetically was that of the low-affinity glucose transporter encoded by mstE - genomic locus AN5860"];
  mstE is strongly repressed at low glucose [PMID:28361917 "Genes encoding the two transporters AtrA and MstE, presented the highest down-regulation"].

Not established for MstE: substrate range beyond glucose (the abstract reports none;
the mannose IDA presumably comes from full-text competition data I could not read, and
competition alone shows binding/inhibition, not transport), coupling mechanism (no CCCP
or proton-flux data for MstE in the abstract; the CCCP-sensitivity data in PMID:24282591
are for HxtB, HxtC and HxtE), vacuolar function.

### Evolutionary grounding (mstE-bioinformatics/RESULTS.md)

- PANTHER tree: MstE and GLT-1 meet at PTN002362094 (Pezizomycotina SPECIATION, root of
  SF92), so they are orthologs; SF92 has five leaves across Eurotiomycetes,
  Sordariomycetes, Leotiomycetes and Dothideomycetes.
- MstE descends from PTN000627328 (family root, 521 leaves), which carries three IBDs:
  membrane and carbohydrate transport (MstE is a seed of both) and carbohydrate:proton
  symporter activity (MstE is not a seed; seeds include its paralogs MstA and MstC).
  No IBD carries D-glucose transmembrane transporter activity, and the PTN001174948
  plasma-membrane IBD does not cover SF92.
- TM1 site: MstE has Ser67 (GLT-1 Val48) at the XylE Asp27 protonation position; the
  A. nidulans paralogs MstA/MstC/HxtE have Asp. Yeast HXT1 (facilitator) also has Asp,
  so the test is asymmetric and inconclusive for MstE energetics.
- Independent support for the ortholog relationship in the literature:
  [PMID:33509260 "whereas the A. nidulans MstE and N. crassa GLT1 ortholog CgHXT5 is a low-affinity glucose transporter"].
  GLT-1 itself is a low-affinity glucose transporter
  [PMID:28115989 "we assigned GLT-1 (Km = 18.42 ± 3.38 mM) and HGT-1/-2 (Km = 16.13 ± 0.95 and 98.97 ± 22.02 µM) to the low- and high-affinity glucose transport systems, respectively"].

### Decisions

- ACCEPT: D-glucose transmembrane transporter activity (IDA, IMP), D-glucose
  transmembrane transport (IMP), plasma membrane (IDA).
- MODIFY to the specific experimentally supported terms: membrane (IBA, IEA) -> plasma
  membrane; transmembrane transporter activity (IEA) -> D-glucose transmembrane
  transporter activity; transmembrane transport, carbohydrate transport,
  carbohydrate transmembrane transport -> D-glucose transmembrane transport.
- MARK_AS_OVER_ANNOTATED: carbohydrate:proton symporter activity (IBA). Mechanism
  not tested for MstE; root-level IBD spans facilitators and symporters; MstE not a
  seed; TM1 site non-acidic. Proton transmembrane transport (IEA, derived from it) gets
  the same action.
- UNDECIDED: mannose transmembrane transporter activity (IDA) and the derived mannose
  transmembrane transport (IEA); vacuole (IDA). Full text not accessible.

For transfer to GLT-1: only glucose transporter activity, glucose transmembrane
transport and plasma membrane localisation are experimentally established for MstE.
Low affinity is an MstE-specific kinetic observation (also measured independently for
GLT-1). CreA-dependent induction is regulatory context, not a transferable GO function.

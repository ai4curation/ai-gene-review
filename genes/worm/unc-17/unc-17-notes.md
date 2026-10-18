# unc-17 (P34711) — vesicular acetylcholine transporter — curation notes

## Identity

- UniProt P34711 (UNC17_CAEEL, reviewed), WormBase ZC416.8, 532 aa, MFS vesicular
  transporter family (IPR001958 ACh transporter; IPR011701/IPR020846 MFS). Orthologue of
  mammalian VAChT (SLC18A3) and paralogue of the vesicular monoamine transporter CAT-1
  within the SLC18 family. unc-17 lies in the cholinergic gene locus together with cha-1
  (ChAT), from which alternatively spliced transcripts arise.

## Literature

### Alfonso et al. 1993 (PMID:8342028, abstract only)

- "Mutations in the unc-17 gene of the nematode Caenorhabditis elegans produce deficits in
  neuromuscular function" [PMID:8342028].
- Identity and localization: "On the basis of sequence similarity to mammalian vesicular
  transporters of biogenic amines and of localization to synaptic vesicles of cholinergic
  neurons in C. elegans, unc-17 likely encodes the vesicular transporter of acetylcholine"
  [PMID:8342028].
- Essentiality: "Mutations that eliminated all unc-17 gene function were lethal, suggesting
  that the acetylcholine transporter is essential" [PMID:8342028]. UniProt adds that newly
  hatched null animals are small, coiled, do not grow or feed, barely move and die within
  days.

### Rand, Duerr & Frisby 2000 (PMID:11099459, review, abstract only)

- "Two of the four classes of vesicular transporters so far identified (VAChT and VGAT) were
  first described and cloned in C. elegans" [PMID:11099459].
- "The biochemical properties of the nematode transporters are surprisingly similar to their
  vertebrate counterparts, and they can be assayed under similar conditions using the same
  types of mammalian cells" [PMID:11099459] — i.e. worm VAChT behaves like vertebrate VAChT
  in transport assays.

### Lickteig et al. 2001 (PMID:11245684, abstract only)

- "UNC-4 is expressed in four classes (DA, VA, VC, and SAB) of cholinergic motor neurons"
  [PMID:11245684]; "Antibody staining reveals that five different vesicular proteins
  (UNC-17, choline acetyltransferase, Synaptotagmin, Synaptobrevin, and RAB-3) are
  substantially reduced in unc-4 and unc-37 mutants in these cells" [PMID:11245684]. UNC-17
  is used here as a synaptic vesicle marker in motor neuron processes — the basis of the NAS
  synaptic vesicle membrane and IDA synapse/neuron projection annotations.

### Steger et al. 2005 (PMID:15914662, abstract only)

- The paper is about the T-type calcium channel CCA-1 at the pharyngeal neuromuscular
  junction: "We show that CCA-1 plays a critical role at the pharyngeal neuromuscular
  junction, permitting the efficient initiation of action potentials in response to
  stimulation by the MC motor neuron" [PMID:15914662]; "Loss of cca-1 function decreases the
  chance that excitatory input from MC will successfully trigger an action potential, and
  reduces the ability of an animal to take in food" [PMID:15914662]. unc-17 is not named in
  the abstract; the curator's IMP/IGI rows for pharyngeal pumping and regulation of
  neurotransmitter secretion must come from unc-17 mutant experiments in the full text
  (unc-17 reduces cholinergic MC output onto pharyngeal muscle).

### Duerr et al. 2008 (PMID:18041778, abstract only)

- "The neurotransmitter acetylcholine (ACh) is specifically synthesized by the enzyme choline
  acetyltransferase (ChAT). Subsequently, it is loaded into synaptic vesicles by a specific
  vesicular acetylcholine transporter (VAChT)" [PMID:18041778].
- "VAChT is found in synaptic regions, whereas ChAT appears to exist in two forms in neurons"
  [PMID:18041778]; "All of the classes of putative excitatory motor neurons in the ventral
  nerve cord appear to be cholinergic" [PMID:18041778] — basis of the IDA organelle membrane,
  neuron projection and excitatory synapse rows.

### Nguyen et al. 1995 (PMID:7498734, abstract only)

- "We characterized 18 genes from Caenorhabditis elegans that, when mutated, confer recessive
  resistance to inhibitors of acetylcholinesterase" [PMID:7498734]; "Measurements of
  acetylcholine levels in these mutants suggest that some of the genes are involved in
  presynaptic functions" [PMID:7498734]. unc-17 is one of the classical Ric genes.

## Assessment

- Core: acetylcholine:proton antiport (GO:0005278) across the synaptic vesicle membrane,
  loading ACh into synaptic vesicles for cholinergic synaptic transmission (GO:0007271).
- Problem rows:
  - GO:0030121 AP-1 adaptor complex and GO:0030122 AP-2 adaptor complex (IBA, part_of).
    VAChT is a *cargo* recognised by clathrin adaptors through its C-terminal dileucine
    motif; it is not a subunit of the AP-1 or AP-2 heterotetramer (which comprises
    alpha/beta/mu/sigma adaptins). A cargo-adaptor interaction has been propagated as complex
    membership.
  - GO:0015311 monoamine:proton antiporter activity (IBA) comes from the SLC18 family node
    shared with the VMAT paralogues (CAT-1, human SLC18A1/2). UNC-17's physiological
    substrate is acetylcholine, which is not a monoamine; the ACh-specific antiporter term
    GO:0005278 is annotated separately, so this row is a paralog-level over-annotation.
  - GO:0005886 plasma membrane (NAS from PMID:8342028) conflicts with the same paper's
    synaptic vesicle localization.

## Deep research

- `unc-17-deep-research-falcon.md` confirms the identity and function ("UNC-17's primary
  biochemical function is to transport acetylcholine (ACh) from the neuronal cytosol into
  synaptic vesicles"). It makes no claim of AP-1/AP-2 complex membership and no claim of
  monoamine transport, consistent with the decisions taken on those two annotation rows.

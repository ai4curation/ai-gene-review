# Hard cases — pseudoenzymes & disputed-function human genes (batch 4)

The earlier cohorts used mostly well-behaved genes. This cohort ([`batch4-genes.txt`](../batch4-genes.txt);
[results](batch4/summary.md)) deliberately picks **human genes flagged as
hard-to-curate** in our own project docs (`HUMAN_GENES_RE_REVIEW.md`,
`UNIPROT_CAUTION_NOTE/`, `PSEUDOENZYMES.md`, `TOP_NOTS.md`, `TRANSCRIPTION_FACTORS/`):
pseudoenzymes, literature-contested activities, "was-X-actually-Y" reclassifications,
and family-label misdirection. It asks two questions the easy cohorts couldn't:
(a) does the **GO layer** assign the ancestral/dead/disputed activity? and (b) does
the **narrative** acknowledge the pseudoenzyme status or the controversy?

**Exact GO capture stays low (1/12).** The one hit is GAPDH `RNA binding`, a secondary core
term, so specific primary-function capture is **0/12**, as on the project page. Because Affinage
only emits `goslim_generic` bins, the informative scores are slim-level. The core-MF bin is
emitted for 10/12. The **top-supported** MF is a core bin for only 6/11 (CASP12 has no MF), the
lowest of any cohort. See [batch4/summary.md](batch4/summary.md). But the two-layer behaviour is
the real result.

## The narrative is genuinely pseudoenzyme- and reclassification-aware

Because Affinage reasons **from the literature** (not from domain/family labels), its
narrative repeatedly gets the hard call right — verbatim:

| Gene | Curation challenge | Narrative verdict (verbatim) |
|------|--------------------|------------------------------|
| ILK | pseudokinase (scaffold) | "Despite its kinase-like domain, ILK is a **bona fide pseudokinase**: recombinant ILK has **no detectable activity** toward GSK-3beta" |
| ROR1 | pseudokinase | "Although it adopts a kinase fold, ROR1 is a **pseudokinase devoid of intrinsic catalytic activity** and is instead transphosphorylated by partner kinases" |
| CPT1C | pseudo-transferase | "it retains **weak** carnitine palmitoyltransferase activity… catalytic efficiency **20–300 times lower** than CPT1A, and it localizes to the ER" |
| HDAC6 | *not* a histone deacetylase | "cytoplasmic class IIb deacetylase… deacetylating a broad set of **non-histone substrates**… alpha-tubulin" |
| PARK7 | glyoxalase **vs** deglycase controversy | "A reported nucleotide/protein **deglycase** activity is **reframed by rigorous kinetics as glyoxalase-like** with only a minor role in neuronal methylglyoxal defense" |

On **KEAP1**, InterPro2GO→BioReason assigned actin binding (from the BTB-Kelch fold). Affinage's
literature grounding avoids that error. Its terms by support are `molecular sensor activity`
(4), `catalytic activity, acting on a protein` (3), `ligase activity` (2), `molecular function
regulator activity` (2) and `molecular adaptor activity` (2). The two bins of our curated core
(ubiquitin-like ligase-substrate adaptor → adaptor; transcription regulator inhibitor →
regulator) are present but are not the top terms. The `acting on a protein` and `ligase` bins
are wrong for a non-catalytic substrate adaptor. So KEAP1 is "not actin", not a clean win.

## …but the GO layer is a lossy down-cast that can *contradict its own narrative*

The `mechanism_profile` does not inherit the narrative's nuance. The sharpest case:

- **ROR1** — narrative: *"pseudokinase devoid of intrinsic catalytic activity"*;
  GO layer: **`catalytic activity, acting on a protein`**. The two layers directly
  contradict each other.
- **CPT1C** — narrative: *"weak… 20–300× lower"*; the GO layer includes flat
  **`transferase activity`** (support 1; no hint of the pseudo/weak status). Our review
  REMOVEd transferase activity. Its curated core is palmitoyl-(protein) hydrolase activity,
  whose bin (`catalytic activity, acting on a protein`, support 1) Affinage also emits. Its
  top term is `molecular sensor activity` (2).

An earlier version of this table picked the favourable term for each gene rather than the
top-supported one, and so overstated how often the trap is avoided. Read by support count
(from [batch4/per-gene.json](batch4/per-gene.json)):

| Gene | Trap (ancestral/wrong activity) | Affinage MF terms, most-supported first (support) | Top term avoids trap? |
|------|--------------------------------|---------------------------------------------------|:--------:|
| ILK | protein kinase activity | molecular adaptor (4); cytoskeletal protein binding, ATP-dependent (2); regulator (1) | ✅ |
| RASA1 | GTPase activity | **catalytic activity, acting on a protein (5)**; regulator, transducer (3); lipid binding, adaptor (2) | ❌ (the correct GAP bin, regulator, is second) |
| PLD3 | phospholipase D activity | catalytic activity acting on RNA, hydrolase (5); acting on DNA, DNA binding (3); RNA binding (2); transferase (1) | partial (hydrolase/nuclease zone; DNA exonuclease bin is third) |
| KEAP1 | actin binding | **molecular sensor (4)**; acting on a protein (3); ligase, regulator, adaptor (2) | partial (no actin, but catalytic/ligase bins for a non-enzyme) |
| CASP12 | cysteine endopeptidase activity | *(empty — no MF grounded)* | ✅ by omission |
| ROR1 | (pseudo)kinase catalysis | transducer (3); **acting on a protein**, adaptor, virus receptor (2) | ✅ at top, ❌ in the list |
| CPT1C | carnitine transferase | molecular sensor (2); **transferase**, acting on a protein, regulator (1) | ✅ at top, ❌ in the list |

So literature grounding keeps the pseudo-activity off the **top** of the list more often than
not (ILK, ROR1, CPT1C, CASP12). It rarely keeps it off the list entirely: only ILK and CASP12
emit no catalytic bin at all.

## Controversy handling: mixed

- **PARK7** — the narrative *engages* the glyoxalase-vs-deglycase dispute and
  adjudicates it (deglycase "reframed… as glyoxalase-like"), matching our caution-note
  reading. Good.
- **UCHL1** — the narrative presents a confident deubiquitinase and **omits** the
  contested ubiquitin-**ligase** activity entirely. A curator's positive-vs-NOT pair
  records the dispute; the single "current model" flattens it.

So the "current model" format can represent a controversy when the literature has a
clear resolution (PARK7), but tends to **flatten** genuinely unresolved ones (UCHL1) —
it has no slot for "annotated both positively and NOT," which is exactly how GOA/our
reviews encode contested functions.

## Bottom line

On the hardest human genes, Affinage's **narrative** is impressively literature-faithful
— it names pseudokinases as catalytically dead, reclassifies HDAC6, and adjudicates
PARK7 — and beats domain-based tools on family-label misdirection (KEAP1). Its **GO
layer**, by contrast, is coarse. Exact capture is 1/12, and that one hit is a secondary term,
so specific capture is 0/12. At slim level the top-supported bin is right for 6/11. It often
lists the dead ancestral activity (ROR1, CPT1C), and in ROR1's case it **flatly contradicts the
very narrative it is derived from**. The gap between the two layers is widest exactly where
curation is hardest — reinforcing the project's core result: *judge Affinage by its
narrative, not its GO grounding, and even the narrative cannot encode a live dispute.*

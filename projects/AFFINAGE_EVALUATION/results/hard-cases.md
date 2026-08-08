# Hard cases — pseudoenzymes & disputed-function human genes (batch 4)

The earlier cohorts used mostly well-behaved genes. This cohort ([`batch4-genes.txt`](../batch4-genes.txt);
[results](batch4/summary.md)) deliberately picks **human genes flagged as
hard-to-curate** in our own project docs (`HUMAN_GENES_RE_REVIEW.md`,
`UNIPROT_CAUTION_NOTE/`, `PSEUDOENZYMES.md`, `TOP_NOTS.md`, `TRANSCRIPTION_FACTORS/`):
pseudoenzymes, literature-contested activities, "was-X-actually-Y" reclassifications,
and family-label misdirection. It asks two questions the easy cohorts couldn't:
(a) does the **GO layer** assign the ancestral/dead/disputed activity? and (b) does
the **narrative** acknowledge the pseudoenzyme status or the controversy?

**GO capture stays low (1/12).** But the two-layer behaviour is the real result.

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

This is markedly better than a domain-based tool: on **KEAP1**, InterPro2GO→BioReason
assigned actin binding (from the BTB-Kelch fold); Affinage's literature grounding
instead lands on `molecular adaptor`/`molecular sensor`/`ligase` — the correct
E3-adaptor/NRF2-sensor zone, **not** actin.

## …but the GO layer is a lossy down-cast that can *contradict its own narrative*

The `mechanism_profile` does not inherit the narrative's nuance. The sharpest case:

- **ROR1** — narrative: *"pseudokinase devoid of intrinsic catalytic activity"*;
  GO layer: **`catalytic activity, acting on a protein`**. The two layers directly
  contradict each other.
- **CPT1C** — narrative: *"weak… 20–300× lower"*; GO layer: flat **`transferase
  activity`** (no hint of the pseudo/weak status).

Where the *narrative itself* de-emphasises catalysis, the GO layer more often follows
and **avoids** the ancestral-activity trap — literature-grounding paying off:

| Gene | Trap (ancestral/wrong activity) | Affinage GO top terms | Avoided? |
|------|--------------------------------|-----------------------|:--------:|
| ILK | protein kinase activity | molecular adaptor, cytoskeletal protein binding | ✅ |
| RASA1 | GTPase activity | molecular function regulator activity | ✅ (it's a GAP) |
| PLD3 | phospholipase D activity | catalytic activity acting on DNA, DNA binding | ✅ (leans exonuclease) |
| KEAP1 | actin binding | molecular adaptor / sensor, ligase | ✅ |
| CASP12 | cysteine endopeptidase activity | *(empty — no MF grounded)* | ✅ by omission |
| ROR1 | (pseudo)kinase catalysis | **catalytic activity, acting on a protein** | ❌ |
| CPT1C | carnitine transferase | **transferase activity** | ❌ |

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
layer**, by contrast, is coarse (1/12 specific capture), sometimes assigns the dead
ancestral activity (ROR1, CPT1C), and in ROR1's case **flatly contradicts the very
narrative it is derived from**. The gap between the two layers is widest exactly where
curation is hardest — reinforcing the project's core result: *judge Affinage by its
narrative, not its GO grounding, and even the narrative cannot encode a live dispute.*

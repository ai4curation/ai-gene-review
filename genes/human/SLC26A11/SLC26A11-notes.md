# SLC26A11 (Q86WA9) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No prior review or notes existed for this gene; this is the first review. ProtNLM2
outputs were not consulted.

### Process

- `just fetch-gene human SLC26A11` created the UniProt, GOA (38 seeded rows) and stub files.
- `just deep-research-falcon human SLC26A11 --fallback perplexity-lite` FAILED: falcon timed
  out at 600 s and the perplexity-lite fallback also failed (recipe exit code 1). No
  deep-research file exists. The review is built from the primary literature cached in
  `publications/`, read directly.
- Cached and read: PMID:42509233 (full text), PMID:21716257 (full text), PMID:23733100 (full
  text), PMID:21593449 (abstract), PMID:25910210 (abstract), PMID:12626430 (abstract only),
  PMID:20957757 / PMID:19056867 (abstract only, large-scale proteomics), PMID:32296183
  (HuRI interactome).

### Evolutionary placement (checked before any transfer)

- PANTHER v19 tree (pantherdb treeinfo API, family PTHR11814) places Q86WA9 under subfamily
  SF55 "SODIUM-INDEPENDENT SULFATE ANION TRANSPORTER" (leaf node PTN002483409). The
  ancestor path includes PTN002483418 (family root: plasma membrane, transmembrane
  transporter activity, transmembrane transport IBDs), PTN000929279 (IBD: GO:0015116
  sulfate transmembrane transporter activity) and PTN000212046 (IBD: GO:1902358 sulfate
  transmembrane transport, seeded by Q86WA9 itself among others; and GO:1902476 chloride
  transmembrane transport, seeded by SLC26A9 human Q7LBE3 / rat RGD:69334).
- The negated PAINT node PTN000929309 (IRD NOT plasma membrane) is NOT on the Q86WA9 path,
  so the plasma membrane IBA is not contradicted by PAINT.
- Mouse Slc26a11 (Q80ZD3) sits in the same SF55 clade (PTN000212360/361 shared with human),
  a one-to-one ortholog; guinea pig G3C7W6 is a Swiss-Prot SLC26A11 ortholog. These are the
  donors for the ISS/IEA rows.
- PAINT curators did NOT propagate chloride:bicarbonate antiporter activity (mouse IDA,
  PMID:21716257) or chloride channel activity (mouse IDA, PMID:23733100) to an ancestral
  node. Treated as a deliberate decision: those functions are not inherited family-wide
  claims; whether they hold for SLC26A11 has to be decided on SLC26A11-specific data.

### What is experimentally established on the HUMAN protein

1. Proton-coupled sulfate transport with chloride as counter-substrate, in purified
   reconstituted SLC26A11ΔC proteoliposomes [PMID:42509233 "These results suggest that
   sulfate transport is obligatorily coupled to proton transport in the same direction."]
   [PMID:42509233 "In the most parsimonious model, SLC26A11 is an exchanger that couples the
   symport of one proton and one sulfate ion (net charge of −1) to the antiport of one
   chloride ion (net charge of −1)."] Electroneutral. Glu-320 (TM8, unique among human
   SLC26 members) controls pH-dependent sulfate affinity; E320Q abolishes transport.
2. Substrate range: thiosulfate, oxalate, selenate strongly compete; oxalate and selenate
   trans-stimulate sulfate efflux (so are likely transported); bicarbonate and phosphate
   have NO effect [PMID:42509233 "Molybdate, iodide, acetate and chloride inhibited transport
   to a lesser extent, whereas phosphate and bicarbonate had no effect on SLC26A11ΔC
   activity."]
3. Chloride-selective, channel-like conductance gated by the proton:sulfate transport
   cycle (Sf9 whole-cell patch clamp) [PMID:42509233 "Taken together, our findings suggest
   that SLC26A11 exhibits two distinct transport functions: electroneutral
   proton:sulfate/chloride exchange and chloride channel activity."]
4. Homodimeric cryo-EM structure (nanodiscs), domain-swapped STAS domains, inward-open.
5. Localization: lysosomal membrane (proteomics PMID:20957757 and cell imaging cited in
   PMID:42509233: "SLC26A11 exclusively localizes to lysosomes in various mammalian cell
   lines"). Plasma membrane only in heterologous overexpression (COS-7, Sf9;
   PMID:12626430; partial in Sf9 per PMID:42509233).
6. Older cell-based data: Na+-independent, DIDS-sensitive sulfate transport (PMID:12626430).

### Inferred, NOT directly shown in human

- Lysosomal sulfate export to the cytosol in cells: argued by the authors from in vitro
  properties plus lysosomal localization ("tailored to function as the elusive lysosomal
  sulfate exporter"); no knockout/lysosomal sulfate accumulation data in the paper. Not
  added as a NEW process annotation; raised as suggested question/experiment.
- Chloride/bicarbonate exchange: mouse COS-7 pHi data (PMID:21716257) positive; guinea pig
  oocytes negative (PMID:21593449); human proteoliposomes show no bicarbonate interaction.
  Treated as contested/over-annotated.
- Kidney intercalated-cell apical/basolateral localization and V-ATPase support (mouse
  only); Purkinje cell plasma membrane chloride channel (mouse); voltage-gated Cl− entry
  in cytotoxic neuronal swelling (rat neurons, PMID:25910210). Organismal/tissue roles not
  annotated as process participation.

### Ortholog context (for downstream transfer)

Bonobo A0A2R9CAF4 is ~99% identical; bonobo is not a PANTHER genome so SF55 placement is
by orthology. Transferable with high confidence: sulfate:proton symport coupled to chloride
antiport, chloride channel activity, lysosomal membrane localization (all human
experimental). Not transferable as established: chloride/bicarbonate exchange, kidney
apical/basolateral localization, tissue-level physiology.

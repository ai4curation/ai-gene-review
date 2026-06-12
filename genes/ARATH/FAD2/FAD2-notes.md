# FAD2 (Delta-12 / omega-6 oleate desaturase) — Arabidopsis thaliana — review notes

UniProt: P46313 · At3g12120 · EC 1.14.19.6 / 1.14.19.22 · Taxon 3702
Relevance: primary lever for seed-oil quality (oleic vs polyunsaturated content) — a
canonical DOE/BER oilseed engineering target (high-oleic oils for fuel/oleochemical use).

## Core function
- ER (microsomal) **omega-6 / Delta-12 fatty acid desaturase**: converts **oleic acid
  (18:1) -> linoleic acid (18:2)** by introducing a second double bond. Acts on fatty
  acids **esterified to phosphatidylcholine (PC)** (acyl-lipid desaturase), using
  **cytochrome b5** as electron donor; product 18:2 is further desaturated to 18:3 by
  FAD3. [UniProt P46313 FUNCTION; file:ARATH/FAD2/FAD2-deep-research-falcon.md;
  PMID:1730697; PMID:8685264]
- Membrane-bound desaturase: conserved histidine-box motifs, ~four transmembrane
  domains; no fused cytochrome b5 (uses separate electron-transfer partner).
  [file:ARATH/FAD2/FAD2-deep-research-falcon.md]
- PC is both the desaturation substrate and a major precursor for seed TAG assembly, so
  FAD2 directly shapes seed-oil fatty-acid composition. [PMID:14690501 context;
  file:ARATH/FAD2/FAD2-deep-research-falcon.md]

## Localization
- **Endoplasmic reticulum membrane**, experimentally confirmed (EXP PMID:14690501;
  in vivo FAD2-fluorescent fusion shows ER, no chloroplast/PM overlap).
- The GOA **nucleus (ISM, GO_REF:0000122 AtSubP)** annotation contradicts this and is a
  spurious sequence-model prediction -> REMOVE. (Same AtSubP artifact as FAE1's bogus
  chloroplast call.)

## Substrate-class nuance
- Two EXP annotations assign **GO:0102985 acyl-CoA (9+3)-desaturase activity**. FAD2 is
  canonically an **acyl-LIPID** (PC-bound) desaturase, not an acyl-CoA desaturase, so the
  acyl-lipid omega-6 desaturase term (GO:0050184) and omega-6 desaturase (GO:0045485) are
  the accurate core MFs. Per curation guidance I do not REMOVE the EXP acyl-CoA term but
  mark it KEEP_AS_NON_CORE and note the preferred acyl-lipid framing.

## Annotation review decisions
- GO:0050184 acyl-lipid omega-6 desaturase (cytochrome b5) (IEA+EXP) -> ACCEPT (core MF)
- GO:0045485 omega-6 fatty acid desaturase activity (IDA) -> ACCEPT (core MF)
- GO:0016717 oxidoreductase, paired donors, O2->2 H2O (IEA) -> ACCEPT (desaturase class)
- GO:0016491 oxidoreductase activity (IEA) -> ACCEPT (general)
- GO:0102985 acyl-CoA (9+3)-desaturase activity (IEA+EXP) -> KEEP_AS_NON_CORE (acyl-lipid
  is the accurate substrate class)
- GO:0006636 unsaturated fatty acid biosynthetic process (IEA) -> ACCEPT (core BP)
- GO:0006629 lipid metabolic process (IEA) -> ACCEPT (general)
- GO:0005789 endoplasmic reticulum membrane (IEA+EXP) -> ACCEPT (core location)
- GO:0005634 nucleus (ISM) -> REMOVE (spurious AtSubP prediction)

## DOE/BER relevance
FAD2 silencing/knockout raises oleic acid and lowers PUFA (e.g. Camelina 18:1 ~11.5% ->
~70%), improving oxidative stability for fuel/oleochemical feedstocks. Allohexaploid crops
(Camelina) need multi-homeolog targeting (gene-dosage model).

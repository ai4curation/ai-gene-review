# Wee1 (mouse, P47810) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Wee1 is reviewed as the experimentally characterised model-organism
member of PANTHER PTHR11042:SF72 (WEE1-LIKE PROTEIN KINASE), the same subfamily as
human WEE1 (P30291). WEE2/Wee1B (oocyte kinase) is a separate subfamily (SF75) and its
data are not used here. ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon mouse Wee1 --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and perplexity-lite returned HTTP 401
(insufficient_quota). No deep-research file exists. Literature was assembled by a
PubMed title search (Wee1 AND mouse/mice/murine) and cached with `just fetch-pmid`.

### Evolutionary grounding

- UniProt: P47810 is in PANTHER PTHR11042:SF72, InterPro IPR017164
  (Wee1-like protein kinase), PIRSF037281, CDD cd14138 PTKc_Wee1a; "Belongs to the
  protein kinase superfamily. Ser/Thr protein kinase family. WEE1 subfamily."
- PAINT (interpro/panther/PTHR11042/PTHR11042-paint.tsv):
  - PTN008510964, GO:0004713 protein tyrosine kinase activity, seeds FB wee1
    (FBgn0011737), human WEE1 P30291, and P47817 (Xenopus wee1); eukaryote-wide node.
  - PTN008510965, GO:0010972 negative regulation of G2/M transition, seed human
    P30291, taxon Euteleostomi (117571). Mouse Wee1 descends from this node.
  - PTN000113601 (deep family node) carries nucleus, cytoplasm and protein kinase
    activity; mouse Wee1 (MGI:103075) is itself one of the cytoplasm seeds (from the
    oocyte IHC IDA, PMID:15459478).
  - Curators did NOT propagate nuclear-envelope, nucleolus or "positive regulation of
    G2/M" from the WEE1 branch; treat as deliberate.

### Mouse experimental evidence (what is established in this species)

- Kinase activity, regulated by M-phase phosphorylation of the N-terminal domain
  (Honda 1995) [PMID:7551544 "In a cell cycle, the mouse wee1 kinase is phosphorylated
  at M-phase ... resulting in inactivation of the kinase activity"]. Abstract only; the
  abstract does not state the substrate assayed.
- Genetic: Wee1-/- embryos die before E3.5 and lack the IR-induced G2/M checkpoint;
  conditional deletion in MEFs causes premature mitotic entry with loss of CDK1 Tyr15
  phosphorylation, rescued by CDK1 inhibition (Tominaga 2006, full text)
  [PMID:16810330 "Our data revealed a significant reduction of Cdk1 phosphorylation at
  Tyr15 24 hours after 4-HT treatment"; "murine Wee1 controls mitotic entry and the G2/M
  cell cycle checkpoint through the regulation of Cdk1 activity"].
- Wee1 deficiency also increases APC/C activity and causes mitotic defects/genome
  instability; recombinant WEE1 had no effect on purified APC/C in vitro, so this is an
  indirect consequence (Vassilopoulos 2015, full text) [PMID:25088202 "addition of
  recombinant WEE1 had no effect on in vitro APC activity"]. Not used for annotation.
- 14-3-3 zeta binds the C-terminal half of mouse Wee1 (Y2H, in vitro, COS-1) [PMID:9016762].
- Neurons: Wee1 is a substrate of SadA/SadB (Brsk2/Brsk1); persistence of Wee1 in
  Sada-/-;Sadb-/- neurons disrupts polarity; Wee1 knockdown rescues [PMID:20026642].
  Abstract only. Microtubule-cytoskeleton organization (IMP) is not mentioned in the
  abstract -> UNDECIDED.
- Oocytes: Wee1 immunoreactivity in oocyte cytoplasm (PMID:15459478) and increased
  nuclear wee1 at meiotic competence (PMID:8886990). Caveat: these antibody studies
  predate the description of oocyte-specific Wee1B/Wee2; cross-reactivity cannot be
  excluded from the abstracts.

### Inferred from human WEE1 (same SF72 subfamily, PAINT node PTN008510965)

- Tyr15-specific (not Thr14) phosphorylation of cyclin B1-CDK1 [PMID:8428596], nuclear
  localization [PMID:8348613], CDK2 Tyr15 phosphorylation [PMID:7743995; Reactome
  R-MMU-1013867].

### Stale ISO rows

GO:0006998 nuclear envelope organization, GO:0007077 mitotic nuclear membrane
disassembly and GO:0010971 positive regulation of G2/M transition are ISO from
P30291, but the current human GOA file (genes/human/WEE1/WEE1-goa.tsv) no longer
carries any of these terms; the donor annotations have been withdrawn. GO:0010971 is
also sign-inverted relative to everything known about WEE1. REMOVE all three.

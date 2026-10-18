# hes4-a (Xenopus laevis, Q90Z12) — review notes

## 2026-10-05 — initial review (NEURAL_CREST_ORIGINS project, Tier 2)

### Identity and homeologs
- Q90Z12, HES4A_XENLA, 281 aa; Hairy2a / Xhairy2a. Xenbase XB-GENE-6256031 = **hes4.S**
  (UniProt DR line, chromosome 7S). Homeolog hes4-b = Q90VV1 = Hairy2b (hes4.L per the
  López 2022 nomenclature chapter summarised in the falcon deep research). X. tropicalis
  hes4 = Q6PBD4; human HES4 = Q9HCC6.
- Domains: bHLH with helix-interrupting proline in the basic region (N-box CACNAG binding),
  Orange domain, C-terminal WRPW Groucho/TLE-recruiting motif [file:XENLA/hes4-a/hes4-a-uniprot.txt
  "Transcriptional repressor. Binds DNA on N-box motifs"; "The C-terminal WRPW motif is a transcriptional repression"].
- **Homeolog problem (central to this gene).** Murato 2007 knocked down each alloallele
  separately: "Xhairy2a seems not to function in the neural crest, although both of them
  are required in the floor plate and the prechordal plate" and "Xhairy2b expression in
  the neural crest is much higher than Xhairy2a expression" [PMID:17724611]. UniProt
  CAUTION follows this: "that hes4-B/hairy2b but not hes4-A/hairy2a has a role in neural crest".
  Against this, Vega-López 2015 (hairy2a/2b resolved, abstract-only cache) reports that
  "hairy genes are required for the induction and migration of the neural crest" and
  "hairy genes have a functional equivalence between them" [PMID:25997789]; the falcon
  deep research (from full text) reports hairy2a ISH at the neural plate border from st.11
  and in prospective/migrating NC [file:XENLA/hes4-a/hes4-a-deep-research-falcon.md].
- Nichane 2008 a/b papers [PMID:18710660, PMID:18721802] and Nagatomo 2007 [PMID:17436284]
  say "Hairy2"/"Xhairy2" without suffix; UniProt/GOA attached the NC IMP rows from the
  Nichane papers to BOTH hes4-a and hes4-b. Glavic 2004 [PMID:14681193] says "Hairy2A",
  and that row is on hes4-a only. Murato's positive NC row is on hes4-b; its NOT row on
  hes4-a. So GOA currently asserts both `involved_in` and `NOT|involved_in` GO:0014029 for
  Q90Z12. Not "fixed" here: flagged for curators (UNDECIDED on the NOT row).

### Molecular activity
- Repressor: "Hairy2A acts as a repressor of Bmp4 transcription" [PMID:14681193];
  "hairy genes function as transcriptional repressors" [PMID:25997789] (falcon: bHLH-EnR
  fusion phenocopies wild type, bHLH-E1A activator fusion has the opposite effect).
- DNA binding: IDA row from Koyano-Nakagawa 2000 [PMID:10976052] (UniProt RP: "FUNCTION,
  DNA-BINDING, AND INTERACTION WITH HES6"); N-box specificity by similarity to Drosophila
  hairy (P14003).
- Partners: Hes6 (IPI, PMID:10976052; with A1L3K9, an unnamed Xenopus LOC protein — UniProt
  subunit line says the interaction "may inhibit the transcriptional repressor activity");
  Hey1 heterodimer and Id3 (Orange–HLH) by similarity; Id3 "physically interacts with
  Hairy2, negatively regulates Hairy2 activity" [PMID:18721802]. The id3-a review's
  Hairy2–Id3 IPI row has WITH UniProtKB:Q90VV1 (hes4-b), i.e. the interaction is
  recorded on the b homeolog.
- Non-DNA-binding mode: "Hairy2 transiently activates in a DNA-binding independent manner
  the expression of the Notch ligand Delta1"; "Hairy2 induces Delta1 through the
  transcription factor Stat3" [PMID:18710660]; Hairy2 facilitates Stat3–FGFR4 complex
  formation [PMID:19851287].
- Comparator for NEW GO:0001227 (QuickGO, 2026-10-05:
  `annotation/search?goId=GO:0001227&geneProductId=Q9HCC6,O14503,Q14469,Q9Y5J3,Q9UBP5,Q9C0J9,Q6IRB2`):
  human HES1 (ISS/IEA), HEY1 (IDA PMID:18239137), HEY2 (IDA PMID:10692439), BHLHE40/41 (IDA)
  carry GO:0001227. Human HES4 (Q9HCC6) does not. So the term is the family convention for
  this activity; hes4-a lacking it is a coverage gap, not a convention.

### Expression
- UniProt: neurula presumptive floor plate, anterior prechordal plate, anterior neural
  border; PSM stripes, pronephros; maternal + zygotic, lower zygotic than hes4-b
  [PMID:17724611 "Xhairy2a is a maternal factor having lower zygotic expression than Xhairy2b"].
- Glavic: "Xiro1, Notch and the Notch target gene Hairy2A are all expressed in the neural
  crest territory" [PMID:14681193].
- Nagatomo: "During gastrulation, Xhairy2 is localized at the presumptive neural crest
  prior to the expression of such neural crest markers as Slug and FoxD3" [PMID:17436284].

### Upstream inputs (not Hairy2 functions)
- Notch/Delta1 downstream of Xiro1 [PMID:14681193]; BMP, FGF, Wnt: "Hairy2 is regulated by
  BMP, FGF and Wnt and that it is only required downstream of BMP and FGF" [PMID:18721802];
  Stat3 activity levels control Hairy2 transcription [PMID:19851287]; floor plate: Delta1 →
  Notch → hairy2a [PMID:15689375].

### Gain / loss of function at the border
- LOF (unsuffixed Xhairy2 MO): represses NC markers, ectopic p27xic1, apoptosis of mitotic
  cells; "Xhairy2 functions in neural crest specification by maintaining cells in the
  mitotic and undifferentiated state" [PMID:17436284].
- GOF: "Hairy2 overexpression represses neural crest and upregulates neural border genes
  at early stages while it expands a subset of them in later embryos" [PMID:18721802];
  DNA-binding mutant "unable to promote cell survival and to upregulate the expression of
  early neural border genes" [PMID:18710660]. Glavic: Hairy2A represses Bmp4 "ensuring that
  levels of Bmp4 optimal for the specification of the neural plate border are attained"
  [PMID:14681193].
- Not sufficient alone in naive ectoderm (falcon on Vega-López 2015: hairy2a alone induced
  sox2 and weak snail1; with msx1 strong snail1).

### Network-layer placement
- Not an NC fate specifier: early overexpression *represses* NC markers and upregulates
  border genes; it acts upstream of / before slug and foxd3; its effect is to hold border
  cells in an undifferentiated, proliferating, surviving pre-crest state.
- Not a classical border specifier like Pax3/Zic1/Msx1 either (it does not by itself
  confer border identity; it is a Notch/BMP/FGF-responsive output that sets BMP levels and
  maintains border progenitors).
- Placement: **neural plate border maintenance / progenitor-maintenance factor**, working
  with Id3 (antagonist that is nevertheless required) and Stat3 (Hairy2 facilitates
  FGFR4–Stat3; Stat3 feeds back on Hairy2/Id3).
- GO consequence: keep `GO:0014029` neural crest formation, whose definition is the
  formation of the border *region* ("The formation of the specialized region of ectoderm
  between the neural ectoderm (neural plate) and non-neural ectoderm", QuickGO). This is
  exactly the level at which Hairy2 acts; do NOT narrow to `GO:0014036`/`GO:0014034`.
  Consistent with id3-a and myc-a under the pending project convention.

### Comparator checks (QuickGO, 2026-10-05)
- NC branch query: `annotation/downloadSearch?goId=GO:0014029&goUsage=descendants&goUsageRelationships=is_a,part_of`
  (1911 rows, all taxa). Hes/Her/Hey/Hairy family members carrying any NC-branch term:
  **only** Xenopus hes4-a (4 rows incl. the NOT), hes4-b (3 IMP) and X. tropicalis hes4
  Q6PBD4 (ISS from Q90VV1). No zebrafish her, no mouse/human HES/HEY row. All are at
  GO:0014029; none at GO:0014034/GO:0014036.
- Targeted: `annotation/search?goId=GO:0014029&goUsage=descendants&geneProductId=Q90VV1,Q90Z12,Q9HCC6,Q6PBD4,Q6IRB2`
  → 8 hits, as above (human HES4 and Xenopus hes1-a none).
- Interpretation: the absence elsewhere is a curation-coverage pattern (the crest Hairy
  literature is Xenopus-centred), not a convention against annotating Hes genes to NC.
  No NEW NC term proposed anyway (the existing rows suffice).
- Rodents: UniProt query `gene:hes4 AND (taxonomy_id:10090 OR taxonomy_id:10116)` returns
  no entries — Hes4 is absent from mouse/rat, so mouse genetics cannot test a Hes4 crest
  role (relevant to the IBA donor lists, which are dominated by MGI/RGD Hes1/5/7/Hey).

### hes4-b QuickGO (for homeolog comparison)
- Q90VV1 has 31 rows incl. GO:0014029 IMP ×3 (17724611, 18710660, 18721802), GO:0048642,
  extra repression IMPs (PMID:16316406, 16586347), protein heterodimerization IPI.

### Evolution / outgroups
- No cached or PubMed-findable data on amphioxus/lamprey hairy expression at the neural
  plate border (PubMed: "amphioxus hairy neural plate border expression neural crest
  evolution" → 0 hits; Yu 2008 amphioxus genome paper full text does not discuss hairy).
  Notch→Hes repression is pan-bilaterian, so the molecular activity is ancestral; the
  border/crest deployment cannot be dated from the evidence in hand. Left as a question.
- Within X. laevis: subfunctionalisation of the a/b alloalleles (Murato 2007) is itself an
  evolutionary case — hes4-a retained maternal and floor/prechordal plate expression,
  hes4-b took the high zygotic NC expression.

### Annotation decisions (summary)
- Repression / DNA binding / nucleus rows: ACCEPT; GO:0045892 IMPs → MODIFY to GO:0000122.
- NEW GO:0001227 (repressor activity).
- GO:0014029 positive IMP rows ×3: ACCEPT (broad level, homeolog-ambiguous evidence noted).
- GO:0014029 NOT row: UNDECIDED (conflicts with positive rows on the same protein and with
  Vega-López 2015; needs curator resolution).
- BMP signaling pathway IMP → MODIFY GO:0030514 negative regulation of BMP signaling pathway.
- Floor plate ×2, prechordal plate: ACCEPT (the best homeolog-resolved hes4-a functions).
- Lens, anti-apoptosis, A/P pattern IBA, neurogenesis IBA: KEEP_AS_NON_CORE.

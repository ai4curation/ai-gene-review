# AVT2 (YEL064C / P39981) review notes

Journal of the AI GO-annotation review for *S. cerevisiae* AVT2. Provenance is recorded inline
as `[PMID:xxxxx "verbatim text"]` or `[SGD/UniProt ...]`.

## Identity (verified)

- UniProt: **P39981** = `AVT2_YEAST`; systematic name **YEL064C**; SGD:S000000790.
  480 aa, 53.3 kDa. [UniProt P39981 record; SGD locus S000000790]
- Standard name **AVT2** = "Amino acid Vacuolar Transport 2". Protein name in UniProt:
  "Vacuolar amino acid transporter 2".
- Family (multiple concordant sources):
  - UniProt SIMILARITY: "Belongs to the amino acid/polyamine transporter 2 family." (ECO:0000305)
  - TCDB **2.A.18.6.20** = the Amino Acid/Auxin Permease (**AAAP**) family.
  - Pfam **PF01490** (Aa_trans); InterPro **IPR013057** (Amino acid transporter, transmembrane domain).
  - PANTHER **PTHR22950** "AMINO ACID TRANSPORTER", subfamily **PTHR22950:SF458**
    "SODIUM-COUPLED NEUTRAL AMINO ACID TRANSPORTER 11-RELATED" (i.e. SLC38/SNAT-like clan).
  - eggNOG KOG1305; OrthoDB 28208at2759.
  This is the SLC32/SLC36/SLC38 ("amino acid/auxin permease", AAAP) superfamily — the same
  clan Russnak et al. described as "related to the neuronal GABA-glycine vesicular transporters"
  (the vesicular inhibitory amino acid transporter VGAT/SLC32 is in this clan).
- **9 predicted TM helices** (UniProt FT TRANSMEM, ECO:0000255): 72-92, 95-115, 145-165,
  214-234, 263-283, 297-317, 338-358, 394-414, 447-467. N-terminal ~48 aa disordered/cytoplasmic
  (REGION 21-48 Disordered, polar-residue biased). So a bona fide polytopic integral membrane
  transporter fold.

NOTE on the "PQ-loop" descriptor in the task brief: the actual UniProt/InterPro/Pfam evidence
assigns AVT2 to the **Aa_trans (PF01490 / AAAP / SLC38-SNAT-like)** clan, NOT the PQ-loop
(SLC36-PAT/LamB / cystinosin, PF04193) family. I ground the review on the AAAP/Aa_trans
assignment that is actually in the record.

## The AVT family (AVT1-7) — what is known, and what is AVT2-specific

The founding paper is Russnak, Konczal & McIntire 2001, J Biol Chem
[PMID:11274162 "A family of yeast proteins mediating bidirectional vacuolar amino acid transport"].
`full_text_available: false` in our cache — **abstract only**. Abstract states:

- "Seven genes in Saccharomyces cerevisiae are predicted to code for membrane-spanning proteins
  (designated AVT1-7) that are related to the neuronal gamma-aminobutyric acid-glycine vesicular
  transporters." [PMID:11274162]
- "We have now demonstrated that **four** of these proteins mediate amino acid transport in
  vacuoles." [PMID:11274162]
- The four with demonstrated activity are named explicitly:
  - **AVT1** — vacuolar **uptake** of large neutral amino acids (Tyr, Gln, Asn, Ile, Leu);
    ATP-dependent, abolished by nigericin (pH-gradient driven). [PMID:11274162]
  - **AVT3, AVT4** — **efflux** of Tyr/large neutral amino acids from the vacuole (system-h-like).
    [PMID:11274162]
  - **AVT6** — **efflux** of aspartate and glutamate; ATP-dependent, nigericin-sensitive.
    [PMID:11274162]
- **AVT2, AVT5, AVT7 are NOT among the four** with demonstrated transport in that paper — i.e.
  no substrate or direction was demonstrated for AVT2. This is the AVT2-specific gap.

Secondary literature confirms AVT2 remained functionally uncharacterized:
- Regulation-of-amino-acid-transport review (Bianchi/Van Belle/... 2019, MMBR) and other
  reviews describe AVT2/AVT5 as members with **no observed transport activity**. (WebSearch of
  the MMBR review text: "No activity has been observed for two of the predicted family members,
  Avt2 and Avt5.") — I did not cite this verbatim in the YAML because I could not fetch the full
  MMBR text into the publications cache; recorded here as background only.

## GO annotations in GOA (9 total; from AVT2-goa.tsv / QuickGO)

MF:
- GO:0003674 molecular_function — **ND**, GO_REF:0000015 (SGD root placeholder)
- GO:0015179 L-amino acid transmembrane transporter activity — **IBA**, GO_REF:0000033
BP:
- GO:0003333 amino acid transmembrane transport — **IBA**, GO_REF:0000033
- GO:1902475 L-alpha-amino acid transmembrane transport — **IEA**, GO_REF:0000108 (inferred from
  the GO:0015179 MF via inter-ontology "logical inference" link)
- GO:0008150 biological_process — **ND**, GO_REF:0000015 (SGD root placeholder)
CC:
- GO:0005783 endoplasmic reticulum — **IDA**, **PMID:11274162** (SGD; direct assay)
- GO:0005783 endoplasmic reticulum — **IBA**, GO_REF:0000033 (GO_Central phylogenetic)
- GO:0016020 membrane — **IBA**, GO_REF:0000033
- GO:0005774 vacuolar membrane — **IEA**, GO_REF:0000044 (UniProtKB SubCell SL-0271)

### Localization: ER (IDA/SGD) vs vacuole membrane (UniProt SubCell / family expectation)

There is a genuine, notable discrepancy:
- **SGD IDA (GO:0005783 ER)** from PMID:11274162 — direct-assay localization to the ER.
  The abstract is about *vacuolar* transport of the family, but the SGD curator read the full
  text and assigned AVT2 specifically to the ER. Per project rules I do NOT overrule an
  experimental (IDA) curator call from the abstract-only cache → ACCEPT.
- **UniProt SubCell (GO:0005774 vacuole membrane, IEA)** — SL-0271, cites the same PMID:11274162
  as the source of "Vacuole membrane; Multi-pass membrane protein". So UniProt and SGD read the
  same paper differently (family-expected vacuole vs. observed ER). AVT family members are
  canonically tonoplast/vacuolar; AVT2 may localize to the ER (possibly ER-retained /
  not trafficked to the vacuole), which is itself a hint that AVT2 is atypical. This is a real
  knowledge gap (where does AVT2 actually act?).

## Domain-based reasoning for the molecular function

- The Aa_trans (PF01490 / AAAP / SLC38-SNAT-like) fold with 9 TM helices strongly supports a
  **generic amino acid transmembrane transporter** activity — this is domain-defensible.
- BUT no substrate and no direction (uptake vs efflux, and driving force) has been demonstrated
  for AVT2 specifically. Its paralogs split into uptake (AVT1) and efflux (AVT3/4/6) with
  different substrate classes, so paralogy does **not** pin AVT2's substrate/direction.
- Therefore: keep MF at the generic amino-acid-transporter level (GO:0015179 L-amino acid
  transmembrane transporter activity is a reasonable IBA-supported generic MF; a *specific*
  substrate/direction would be over-annotation).

## Review decisions (summary)

- GO:0015179 L-amino acid transmembrane transporter activity (IBA) — **ACCEPT** as the
  defensible generic MF (family fold; substrate unknown → do not specialize).
- GO:0003333 amino acid transmembrane transport (IBA) — **ACCEPT** generic BP.
- GO:1902475 L-alpha-amino acid transmembrane transport (IEA, inter-ontology) — **ACCEPT**
  (consistent, generic; auto-derived from the MF).
- GO:0005783 ER (IDA, PMID:11274162) — **ACCEPT** (direct experimental localization; core CC).
- GO:0005783 ER (IBA) — **KEEP_AS_NON_CORE** (phylogenetic duplicate of the IDA; the IDA is the
  authoritative one).
- GO:0016020 membrane (IBA) — **ACCEPT** (correct, generic; it is an integral membrane protein).
- GO:0005774 vacuolar membrane (IEA, SubCell) — **KEEP_AS_NON_CORE** (family-expected/UniProt
  location; conflicts with the ER IDA, so retained as plausible-but-not-core rather than removed —
  cannot overrule either the SubCell mapping or note the unresolved ER-vs-vacuole question).
- GO:0003674 molecular_function (ND) — **REMOVE** (root placeholder, now superseded by GO:0015179).
- GO:0008150 biological_process (ND) — **REMOVE** (root placeholder, superseded by GO:0003333).

## Knowledge gaps (primary deliverable — this is a dark gene)

1. **Transported substrate + direction unknown** for AVT2. Family fold ⇒ amino acid transporter,
   but no substrate/direction/driving-force demonstrated (unlike AVT1 uptake; AVT3/4/6 efflux).
2. **In-vivo localization unresolved**: IDA places it in the ER, but UniProt/family expectation is
   the vacuole membrane — is AVT2 an ER-resident, an ER-retained mis-folded/unassembled member, or
   a vacuolar transporter caught in transit?
3. **Physiological role / redundancy** with the AVT family: no dedicated phenotype; deletion is
   viable. Is AVT2 redundant with AVT1/3/4/5/6/7 or specialized/silent?
4. No demonstrated activity in the one biochemical survey that assayed the whole family
   (only 4/7 members scored positive; AVT2 was among the 3 negatives).
</content>
</invoke>

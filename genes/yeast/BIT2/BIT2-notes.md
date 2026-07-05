# BIT2 (YBR270C) curation notes

Journal-style working notes for the AI GO-annotation review of *Saccharomyces cerevisiae* BIT2.
Provenance is recorded inline as `[PMID:xxxx "verbatim supporting text"]` or `[source "..."]`.
BIT2-specific evidence is kept strictly separate from evidence about its paralog BIT61.

## Identity (from UniProt P38346 / SGD S000000474)

- UniProt: **P38346**, entry name `BIT2_YEAST`, 545 aa, 61.2 kDa.
- RecName: "Probable target of rapamycin complex 2 subunit BIT2" (Short: "TORC2 subunit BIT2");
  AltName "Binding partner of TOR2 protein 2".
- Systematic name: **YBR270C** (chromosome II); ORF name YBR1738; SGD:S000000474; GeneID 852573.
- Evidence at protein level (PE1). Reference proteome UP000002311.
- Sequence note: the protein is largely low-complexity; UniProt annotates two disordered regions
  (residues 1–24 and 78–166) with polar-residue compositional bias (MobiDB-lite). The globular
  portion is C-terminal (roughly residues ~170–545), which is where the Pfam HbrB match lies.

## Family / domain (inline domain analysis of the UniProt record)

- **Pfam PF08539 (HbrB)**, **InterPro IPR013745 (Bit61/PRR5)**, **PANTHER PTHR32428**
  ("TARGET OF RAPAMYCIN COMPLEX 2 SUBUNIT BIT61-RELATED"), subfamily **PTHR32428:SF2**.
- PANTHER family members (`interpro/panther/PTHR32428/PTHR32428-entries.csv`) place BIT2 in the
  same SF2 subfamily as:
  - *S. cerevisiae* **BIT61** (P47041) — the WGD paralog (also SF2);
  - *S. pombe* **bit61** (O74547) and SPAC6B12.03c (O14208);
  - and the mammalian/vertebrate orthologs are the **PRR5 / PRR5L** proteins (Proline-rich
    protein 5 / 5-like; SF3/SF4), i.e. **Protor-1 / Protor-2**, the accessory regulatory
    subunits of **mTORC2**.
  So the whole family is the fungal Bit61/Bit2 ↔ metazoan PRR5/Protor lineage of **TORC2/mTORC2
  accessory subunits**. This orthology is the strongest grounding for "TORC2 subunit".
- The HbrB/Bit61-PRR5 domain has no known catalytic activity; PRR5/Protor are described as
  accessory/regulatory (non-catalytic) subunits. There is no nucleotide-binding, kinase, or other
  enzymatic motif in the sequence. Consistent with an **accessory/scaffolding subunit**, not an
  enzyme. This underlies the MF-dark call below.

## KNOWN about BIT2 specifically (BIT2, not BIT61)

1. **BIT2 is a subunit of TORC2** (part of the TOR complex 2).
   - GOA: `GO:0031932 TORC2 complex`, **IDA**, PMID:15689497, assigned by SGD (part_of). This is the
     experimental anchor for complex membership.
   - The TORC2 subunit inventory in the cryo-EM paper explicitly names BIT2 as an alternative
     paralog subunit: [PMID:29170376 "TORC2 (mTORC2) is composed of Tor2 (mTOR), Lst8 (mLst8/GβL),
     Avo1 (hSin1), Avo2 (no ortholog), Avo3 (Rictor) and Bit61 or its paralog Bit2 (Protor1 or
     Protor2)."]. NOTE: TORC2 contains **Bit61 *or* Bit2** — the two paralogs are alternative,
     largely interchangeable accessory subunits of the same complex.
2. **BIT2 physically interacts with TORC2 components / effectors.**
   - UniProt SUBUNIT: "Interacts with the target of rapamycin complex 2 (TORC2) subunit TSC11 and
     the TORC2 effectors SLM1 and SLM2." {ECO:0000269|PubMed:11283351, ECO:0000269|PubMed:15689497}.
   - These are the physical-interaction data (Ito et al. 2001 genome-wide two-hybrid PMID:11283351;
     Fadri et al. 2005 PMID:15689497) that place BIT2 in the TORC2/Slm1-Slm2 interaction network.
   - CAUTION: PMID:15689497 is cached **abstract-only** (`full_text_available: false`); its abstract
     foregrounds **Slm1/Slm2 binding Avo2 and Bit61** [PMID:15689497 "Slm1 and Slm2 physically
     interact with Avo2 and Bit61, two components of the TORC2 signaling complex"]. The BIT2 IDA to
     TORC2 complex is attributed by the SGD curator to this paper, so the BIT2-specific data are in
     the full text / figures that I cannot see. Per project rules I do NOT remove or downgrade the
     experimental IDA on the basis that the abstract names the paralog.
3. **Non-essential; viable null.** *bit2Δ* is viable in S288C; high-throughput phenotyping reports
   decreased resistance to oxidative stress and to a farnesyltransferase inhibitor (SGD phenotype
   summary, high-throughput screens) [https://yeastgenome.org/locus/S000000474]. No strong,
   specific single-mutant growth phenotype is documented, consistent with paralog redundancy with
   BIT61.

## KNOWN about the paralog BIT61 (kept separate — do NOT attribute to BIT2)

- The **cryo-EM TORC2 structure was solved from TORC2 purified via Bit61-TAP in a *bit2Δ* strain**;
  the structural placement ("Finger2", the acute angle of the rhombohedron, contact with Avo3) is
  therefore for **Bit61, not BIT2**: [PMID:29170376 "TORC2 was prepared through pull-down of
  TAP-tagged Bit61 from yeast extracts lacking Bit2"] and [PMID:29170376 "despite the fact that we
  purified TORC2 via tagged Bit61 from cells lacking Bit2, the density for the Bit61 subunit is not
  well-defined, and beyond a general localization to Finger2, we cannot conclude more."]. I will NOT
  cite the Finger2/edge placement as BIT2 evidence — only the general "Bit61 or its paralog Bit2 is
  a TORC2 subunit" statement is BIT2-applicable.
- BIT61 (YJL058C, P47041) has its own SGD phenotypes (decreased competitive fitness on minimal/SC
  media, decreased resistance to acid pH, elevated chromosome loss) — these are BIT61, not BIT2.

## NOT known about BIT2 (the knowledge gaps)

1. **BIT2's specific molecular activity within TORC2 is undefined.** The Bit61/PRR5 (HbrB) domain
   has no catalytic activity; BIT2 is an accessory/regulatory subunit whose molecular contribution
   (does it modulate substrate selection? complex stability? localization? effector, e.g. Slm1/Slm2,
   engagement?) has not been demonstrated for BIT2 specifically. GOA already flags this: the SGD MF
   annotation is `GO:0003674 molecular_function` **ND** (no data).
2. **BIT2's non-redundant function vs BIT61 is unknown.** TORC2 contains "Bit61 or its paralog Bit2";
   whether the two paralogs are functionally distinct (differential expression, condition-specific
   incorporation, distinct effector bias) or fully redundant is not established. No *bit2Δ bit61Δ*
   double-mutant phenotype is annotated at SGD.
3. **No strong single-mutant loss-of-function phenotype** pins down a BIT2-specific biological role;
   the reported phenotypes are high-throughput sensitivities (oxidative stress; farnesyltransferase
   inhibitor), not a mechanistic assignment.

## GOA annotations to review (7 rows in BIT2-goa.tsv)

1. `GO:0007163 establishment or maintenance of cell polarity` — IBA (GO_REF:0000033), involved_in.
   Phylogenetic (IBA). TORC2/Slm-actin axis does regulate polarized growth/actin, so this is
   plausible at the family level but is a downstream/process-level inference, not BIT2-specific
   experimental data. → KEEP_AS_NON_CORE (family/process-level, not core BIT2 activity).
2. `GO:0019887 protein kinase regulator activity` — IBA (GO_REF:0000033), enables. IBA-projected MF.
   BIT2 as a TORC2 accessory subunit plausibly contributes to regulating the Tor2 kinase, but there
   is no BIT2 experimental MF; "regulator of the kinase" via being part of the complex is the family
   rationale. This is the least uninformative MF available. → KEEP_AS_NON_CORE (IBA family MF; not an
   independently demonstrated BIT2 activity; better captured as contributes_to at the complex level).
3. `GO:0031932 TORC2 complex` — IBA (GO_REF:0000033), part_of. → ACCEPT (redundant with the IDA row
   but phylogenetically well-supported; core).
4. `GO:0038203 TORC2 signaling` — IBA (GO_REF:0000033), involved_in. → ACCEPT/KEEP (core BP; TORC2
   membership implies participation in TORC2 signaling).
5. `GO:0031932 TORC2 complex` — **IDA**, PMID:15689497, part_of. → ACCEPT (experimental anchor;
   core). Defer to SGD curator; do not REMOVE despite abstract-only cache foregrounding Bit61.
6. `GO:0038203 TORC2 signaling` — **IC** (inferred from GO:0031932 complex membership),
   PMID:15689497, involved_in. → ACCEPT (IC directly from the experimental complex membership; core).
7. `GO:0003674 molecular_function` — **ND** (GO_REF:0000015), enables. Root MF, no data. → ACCEPT/KEEP
   (honestly reflects that BIT2's specific MF is undetermined — the MF-dark gap; this is the correct
   use of ND, not a defect).

## Core function synthesis

- **Core:** BIT2 is an accessory (non-catalytic) subunit of TORC2, the rapamycin-insensitive TOR
  complex 2 (Tor2, Lst8, Avo1, Avo2, Avo3/Tsc11, and Bit61-or-Bit2). It participates in TORC2
  signaling. Membership is experimental (IDA) and phylogenetically supported (IBA); orthology to
  metazoan PRR5/Protor (accessory mTORC2 subunits) corroborates an accessory/regulatory role.
- **MF:** best expressed as *contributes_to* a TORC2/kinase-regulatory activity rather than an
  independently enabled activity; BIT2's own biochemical activity is unknown (MF-dark).
- Because BIT2 is one of two interchangeable paralog subunits, its individual functional weight is
  intrinsically hard to pin down (redundancy with BIT61).

## Deep-research provider status

Automated deep research was attempted twice via `just deep-research-falcon yeast BIT2
--fallback perplexity-lite`. Both attempts failed: the falcon provider timed out/was killed
(exit 143/144) and the perplexity-lite fallback returned HTTP 401 (API quota exceeded). No
`-deep-research-{provider}.md` file was produced, and none was fabricated. This review is
therefore grounded directly in the UniProt record (P38346), the GOA TSV, the cached primary
literature (PMID:15689497, PMID:11283351, PMID:29170376), the PANTHER/InterPro family record
(PTHR32428 / IPR013745 / PF08539), and the SGD locus page — all cited with provenance above.

## References gathered / cached

- PMID:15689497 — Fadri et al. 2005, Mol Biol Cell (abstract-only cache). IDA anchor for TORC2
  complex membership; SLM1/SLM2 interaction. relevance HIGH.
- PMID:11283351 — Ito et al. 2001, PNAS (full text cached; genome-wide two-hybrid). Physical
  interaction data underlying the TSC11/SLM1/SLM2 interactions in UniProt SUBUNIT. relevance MEDIUM
  (systematic screen; BIT2 data in supplementary interaction tables, not discussed in body text).
- PMID:29170376 — Karuppasamy et al. 2017, Nat Commun (full text cached). Cryo-EM TORC2 structure.
  Establishes the "Bit61 or its paralog Bit2" subunit inventory (BIT2-applicable). CAUTION: all
  structural placement is for Bit61 (purified from *bit2Δ*), NOT BIT2. relevance MEDIUM.
- SGD locus page S000000474 — phenotype/paralog summary (viable null; oxidative-stress &
  farnesyltransferase-inhibitor sensitivities; WGD paralog BIT61).
- GO_REF:0000015 (ND policy), GO_REF:0000033 (phylogenetic IBA) — method references.

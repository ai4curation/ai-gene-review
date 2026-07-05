# SIA1 (YOR137C, Q12212) — curation notes

Journal / working notes for the AI GO-annotation review of *Saccharomyces cerevisiae* SIA1.

## Identity

- UniProt: **Q12212** (SIA1_YEAST); systematic name **YOR137C**; ORF YOR3329C; chromosome XV.
- SGD: S000005663.
- Length 622 aa; PE=2 (evidence at transcript level).
- Gene name origin: **SIA1 = "Suppressor of eIF5A 1"** — verified against the SGD backend record
  (`name_description: "Suppressor of eIF5A"`, cited to Valentini SR et al. 2002, PMID:11861547).
  NOTE: the task brief glossed the acronym as "Sphingoid long-chain base Influences ATPase"; this
  is NOT the SGD-authoritative expansion, and I found no source for the sphingoid gloss. I use the
  SGD name.
- SGD one-line description: "Protein of unassigned function; involved in activation of the Pma1p
  plasma membrane H+-ATPase by glucose; contains peptide signal for membrane localization."
- SGD curated GO summary: Molecular Function = Unknown; Biological Process = proton transmembrane
  transport; Cellular Component = Unknown. → genuinely a dark/understudied gene.

## KNOWN (evidence-supported)

1. **Required for glucose-triggered post-translational activation of the Pma1 plasma-membrane
   H+-ATPase.** [PMID:9450541 "Deletion of YOR137c does not affect the level of Pma1 at the plasma
   membrane, but disturbs the glucose-triggered Vmax increase of the enzyme."] The same abstract:
   "the YOR137c gene product is implicated in this activation" and "We propose that at least two
   independent mechanisms are involved in glucose activation of the H+-ATPase." This is the sole
   experimental functional characterisation (deletion phenotype, IMP-grade). It shows SIA1 is
   REQUIRED for the Vmax increase but does NOT show a direct molecular mechanism or a direct
   physical interaction with Pma1.

2. **Isolated genetically as a multicopy suppressor of a temperature-sensitive eIF5A (TIF51A)
   allele** — the basis of the gene name (Valentini et al. 2002, PMID:11861547). The abstract
   names PAB1, PKC1, WSC1, WSC2, WSC3 among six suppressors and connects eIF5A to the WSC/PKC1
   cell-wall-integrity signalling pathway; SIA1 is the sixth (unnamed in the abstract; full text
   not in cache). This links SIA1 genetically to PKC1/cell-integrity signalling, but the mechanism
   is unknown.

3. **Induced (up-regulated) by ethanol / short-term ethanol stress** (UniProt INDUCTION line,
   ECO:0000269|PubMed:11389906; Alexandre et al. 2001). This is expression regulation, not a
   molecular function.

4. **Contains an N-terminal signal peptide (residues 1–27, ECO:0000255)** and a metallophosphatase
   domain (see below); consistent with membrane/secretory-pathway localisation, matching the
   "peptide signal for membrane localization" phrasing in SGD. No experimentally verified
   subcellular localisation term is curated (CC = Unknown at SGD).

## Domain / bioinformatic reasoning (inline, from SIA1-uniprot.txt)

- Pfam **PF00149 Metallophos** (one copy); InterPro **IPR004843 (Calcineurin-like_PHP)** +
  **IPR029052 (Metallo-depent_PP-like)**; Gene3D **3.60.21.10**; SUPFAM **SSF56300 Metallo-dependent
  phosphatases**. → SIA1 has a calcineurin-like metallophosphoesterase (MPE) fold.
- PANTHER family **PTHR32440**, subfamily **SF0 "PHOSPHATASE DCR2-RELATED"**. Reviewed SF0 members
  (from PTHR32440-entries.csv): S. cerevisiae **DCR2** (Q05924, "Phosphatase DCR2"), the K. lactis
  SIA1 ortholog (Q6CPQ2), S. pombe SPCC1020.05, and several **Arabidopsis "probable INACTIVE purple
  acid phosphatase"** proteins (PAP14/16/28/29). The InterPro family text notes the family is in the
  "purple acid phosphatase family, although some are predicted to be inactive."
- Metallophosphatase catalytic signature (the conserved metal-coordinating blocks
  D-x-H…GD-x-x-D…GNH[D/E]…GH-x-H). Manual inspection of the SIA1 sequence finds candidate motifs:
  `QITDFHF` (~315, DxH), `VVITGDLLDS` (~350, GD..D), and `SCGHEHNNDCC` (~575, GH-x-H). So at least
  part of the metal-binding scaffold appears retained. HOWEVER: (a) no phosphatase substrate or
  catalytic activity has ever been demonstrated for SIA1 experimentally; (b) its nearest orthologs
  cluster with "inactive purple acid phosphatases"; (c) SGD lists Molecular Function = Unknown.
  → The molecular activity of SIA1 is UNRESOLVED. The IBA "phosphoprotein phosphatase activity" is
  a plausible family-level inference but is NOT experimentally supported for SIA1, and may reflect a
  degenerate / pseudophosphatase domain. I treat catalytic phosphatase activity as a knowledge gap,
  not an established function. (This is a family-level bioinformatic judgement, not a definitive
  claim of inactivity.)

## Existing GOA annotations (5) — review plan

| # | Term | Ev | Ref | Plan |
|---|------|----|-----|------|
| 1 | GO:0004721 phosphoprotein phosphatase activity | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE — family-level MPE inference; not experimentally shown; flag as gap |
| 2 | GO:0016787 hydrolase activity | IEA | GO_REF:0000002 (InterPro IPR004843) | KEEP_AS_NON_CORE — generic parent of the MPE-fold inference; uninformative but not wrong |
| 3 | GO:1902600 proton transmembrane transport | IMP | PMID:9450541 | MODIFY → regulation of proton transport (GO:0010155); SIA1 regulates, does not transport |
| 4 | GO:0003674 molecular_function (root, ND) | ND | GO_REF:0000015 | ACCEPT (ND placeholder; MF genuinely unknown) |
| 5 | GO:0005575 cellular_component (root, ND) | ND | GO_REF:0000015 | ACCEPT (ND placeholder; CC genuinely unknown) |

Rationale for #3 MODIFY (not REMOVE): PMID:9450541 is experimental (IMP) and I must not overrule
the SGD curator. But the *term* chosen (proton transmembrane transport, a transporter/BP for the
ion movement itself) attributes the transport activity to SIA1, whereas the paper shows SIA1 is
REQUIRED for the glucose-triggered Vmax increase of Pma1 — i.e. a *regulatory* role. MODIFY to
"regulation of proton transport" (GO:0010155) keeps the experimental support while stating the
biology more accurately. Keep the original as the essence-is-sound case.

## core_functions (planned)

SIA1 is best summarised as a positive regulator required for glucose-induced activation of the
Pma1 H+-ATPase; molecular mechanism unknown. I will use the BP "regulation of proton transport"
(GO:0010155) grounded in PMID:9450541, and NOT assert a catalytic MF given the gap.

## knowledge_gaps (the primary deliverable — dark gene)

1. **Molecular mechanism of Pma1 activation.** Does SIA1 act directly on Pma1 (as an activator /
   scaffold) or indirectly (e.g. via signalling, lipid environment)? PMID:9450541 shows a
   requirement, not a mechanism, and explicitly proposes "at least two independent mechanisms."
2. **Is SIA1 a catalytically active phosphatase or a pseudophosphatase?** The MPE/calcineurin-like
   fold and the IBA annotation suggest possible phosphatase activity, but no substrate/activity has
   been demonstrated and the closest orthologs are "inactive purple acid phosphatases." If active,
   its physiological substrate (Pma1? a Pma1 kinase/phosphatase relay?) is unknown.
3. **Direct physical partners.** BioGRID lists interactions but no validated Pma1 physical
   interaction is curated in UniProt (IntAct=1). Direct binding partners are unknown.
4. **Subcellular localisation.** Signal peptide predicts secretory-pathway/membrane entry, but no
   experimental localisation term is curated (SGD CC = Unknown). Where SIA1 acts relative to Pma1
   (plasma membrane vs. secretory compartments) is unresolved.
5. **Relationship to eIF5A / PKC1 cell-integrity signalling.** SIA1 was isolated as an eIF5A
   suppressor (PMID:11861547) linking it to WSC/PKC1 signalling; whether this is mechanistically
   related to its Pma1 role, or an independent activity, is unknown.
6. **Broader phenotype.** SGD large-scale phenotypes (altered chemical/UV resistance, abnormal
   vacuolar morphology, competitive-fitness changes) are unexplained at the molecular level.

## Files / provenance

- UniProt: genes/yeast/SIA1/SIA1-uniprot.txt
- GOA: genes/yeast/SIA1/SIA1-goa.tsv
- PANTHER: interpro/panther/PTHR32440/ (metadata + entries)
- Cached pubs: publications/PMID_9450541.md (abstract only), publications/PMID_11861547.md
  (abstract only). PMID:11389906 (ethanol induction) referenced by UniProt but not central to MF.
- Deep research: NOT AVAILABLE. Two `just deep-research-falcon yeast SIA1 --fallback
  perplexity-lite` runs both failed — the Falcon/Edison endpoint repeatedly disconnected
  (RemoteProtocolError / connection reset) and timed out at 600s, and the perplexity-lite
  fallback returned HTTP 401 "insufficient_quota". No `-deep-research-*.md` file was produced.
  Per project rules I did NOT hand-author a file named `-deep-research-{provider}.md`. The
  review is instead grounded in: UniProt Q12212 (domains/features), the GOA TSV, PANTHER
  PTHR32440 family data, the SGD locus record (name + curated summary + phenotypes, fetched
  from the SGD backend API), and the two cached primary papers PMID:9450541 and PMID:11861547.
</content>
</invoke>

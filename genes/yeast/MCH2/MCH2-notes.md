# MCH2 (YKL221W) research notes

UniProt: P36032 (MCH2_YEAST) · Systematic name: YKL221W · SGD: S000001704
Standard name: MCH2 (Monocarboxylate transporter Homologue 2)

## One-line summary

MCH2 is a **dark** *Saccharomyces cerevisiae* gene: a 473-aa polytopic membrane protein
of the Major Facilitator Superfamily (MFS), classified in the monocarboxylate porter
(MCT/TC 2.A.1.13) family by sequence homology, but with **no demonstrated transport
substrate, no measured transport activity, and no defined physiological role**. It is one
of five paralogous "monocarboxylate transporter homologues" (MCH1–MCH5) in budding yeast;
only Mch5p has an assigned substrate (riboflavin). MCH2's own substrate and direction are
unknown.

## What is KNOWN (with provenance)

### Sequence / domain architecture (high confidence)
- 473 aa, 52.3 kDa; predicted N-glycosylation site at Asn72.
  [UniProt:P36032 sequence & feature table]
- Belongs to the Major Facilitator Superfamily; UniProt SIMILARITY:
  "Belongs to the major facilitator superfamily. Monocarboxylate porter (TC 2.A.1.13)
  family." (ECO:0000305 — sequence-model inference, not experimental)
  [UniProt:P36032]
- InterPro: IPR011701 (MFS), IPR036259 (MFS_trans_sf), IPR050327 (Proton-linked_MCT).
  CDD cd17352 (MFS_MCT_SLC16). PANTHER PTHR11360 "Proton-linked Monocarboxylate
  Transporter", subfamily PTHR11360:SF315 "TRANSPORTER MCH2-RELATED". Pfam PF07690
  (MFS_1). TCDB 2.A.1.13.18. [UniProt:P36032 DR lines]
- The founding chromosome-XI sequencing paper described the ORF as having "the structure
  of membrane transporters" with similarity to a mammalian putative mevalonate transporter:
  [PMID:8091865 "The fourth one, part of which is similar to the mammalian putative
  transporter of mevalonate, has the structure of membrane transporters."]

### Membrane topology (experimental, moderate confidence for the specific residue map)
- UniProt annotates 12 transmembrane helices with cytoplasmic N- and C-termini
  (a canonical 12-TMS MFS fold). [UniProt:P36032 TRANSMEM/TOPO_DOM features]
- MCH2 was one of the 546 proteins in the global yeast membrane-proteome topology map;
  the C-terminus location was experimentally constrained by the glycosylation/growth
  reporter fusion assay. [PMID:16847258 — the study reporting experimentally constrained
  topology models for 546 S. cerevisiae membrane proteins]

### Localization
- UniProt: "Membrane; Multi-pass membrane protein." [UniProt:P36032]
- IBA (GO_Central) assigns plasma membrane (GO:0005886) by phylogenetic inference from
  the MCT/SLC16 tree. This is inference, not a direct MCH2 localization result.
- The functional study noted that at least some Mch proteins reside in intracellular
  membranes (a family-level statement, not MCH2-specific):
  [PMID:11536335 "intracellular localization studies indicated that at least some of the
  Mch proteins reside in intracellular membranes."]

### Function — the negative result (this is the load-bearing experimental finding)
- A quintuple deletion of all five MCH genes (mch1-5Δ) showed **no growth defect** on
  monocarboxylic acids as sole carbon sources, and monocarboxylate uptake/secretion rates
  were indistinguishable from wild type:
  [PMID:11536335 "A yeast mutant strain deleted for all five MCH genes exhibited no growth
  defects on monocarboxylic acids as the sole carbon and energy sources. Moreover, the
  uptake and secretion rates of monocarboxylic acids were indistinguishable from the
  wild-type strain."]
- Conclusion of that paper: the yeast Mch proteins do NOT transport monocarboxylates and
  "perform other functions than do their mammalian counterparts":
  [PMID:11536335 "It is concluded that the yeast monocarboxylate transporter-homologous
  proteins perform other functions than do their mammalian counterparts."]
- UniProt encodes this negative result directly:
  [UniProt:P36032 "FUNCTION: Probable transporter. Does not act in the transport of
  monocarboxylic acids across the plasma membrane."]
- The mch1-5Δ strain had strongly reduced biomass yields in aerobic glucose-limited
  chemostat cultures, which the authors interpreted as pointing to involvement of Mch
  transporters in mitochondrial metabolism — but pyruvate uptake into isolated mitochondria
  was NOT affected in mch1-5Δ, so no direct mitochondrial transport role was established:
  [PMID:11536335 "The mch1-5 mutant strain showed strongly reduced biomass yields in
  aerobic glucose-limited chemostat cultures, pointing to the involvement of Mch
  transporters in mitochondrial metabolism. ... However, pyruvate uptake into isolated
  mitochondria was not affected in the mch1-5 mutant strain."]
  NB: this is a phenotype of the *quintuple* mutant, not of mch2Δ alone; paralog redundancy
  is unresolved.

### Paralog context (family-level)
- Five MCH paralogs (MCH1–MCH5) were named for their similarity to mammalian MCTs.
  [PMID:11536335 "We have characterized the monocarboxylate permease family of
  Saccharomyces cerevisiae comprising five proteins."]
- Only Mch5p has a demonstrated substrate: it is a plasma-membrane **riboflavin (vitamin
  B2)** transporter (facilitated diffusion, Km ≈ 17 µM).
  [PMID:16204239 "characterize the protein as a plasma membrane transporter for
  riboflavin"]
- The riboflavin paper explicitly states the other MCH paralogs have unrelated functions:
  [PMID:16204239 "the other members of the MCH gene family appear to have unrelated
  functions."]
  => MCH2's substrate is NOT expected to be riboflavin, and remains unassigned.

## What is NOT known (the gap)

1. **Transported substrate** — undetermined. Ruled OUT: monocarboxylic acids (lactate,
   pyruvate, acetate). Not expected to be riboflavin (that is Mch5p; paralogs "unrelated").
2. **Transport direction / mechanism / driving force** — unknown (uniport / symport /
   antiport; proton-coupled vs facilitated). The UniProt "Symport" keyword and the IEA
   symporter-activity term come from family/keyword mapping, not from an MCH2 assay.
3. **Physiological role / biological process** — unknown. GOA carries ND for both MF and
   BP from SGD. No individual mch2Δ phenotype is established.
4. **Subcellular compartment of action** — the plasma-membrane IBA call is a phylogenetic
   inference; direct MCH2 localization (plasma membrane vs endomembrane) is not firmly
   established in the files available here.
5. **Paralog redundancy** — the only functional phenotype (reduced chemostat biomass) is
   from the mch1-5Δ quintuple mutant; whether MCH2 contributes, and whether the paralogs
   are redundant, is unresolved.

## Existing GOA annotations (7) and disposition (planned)

1. GO:0005886 plasma membrane — IBA (GO_REF:0000033) — KEEP_AS_NON_CORE (phylogenetic
   inference; MFS transporters are typically PM, but MCH2's own localization is not directly
   demonstrated; keep but do not treat as a solved core fact).
2. GO:0022857 transmembrane transporter activity — IBA (GO_REF:0000033) — ACCEPT
   (generic; well supported by 12-TMS MFS fold; the ONLY defensible MF given no substrate).
3. GO:0016020 membrane — IEA (GO_REF:0000044, SubCell) — ACCEPT (broad, correct).
4. GO:0022857 transmembrane transporter activity — IEA (GO_REF:0000002, InterPro) — ACCEPT
   (same generic MF, InterPro route; correct at this generality).
5. GO:0055085 transmembrane transport — IEA (GO_REF:0000002, InterPro) — ACCEPT
   (generic BP consistent with the fold; substrate/direction unknown so keep generic).
6. GO:0003674 molecular_function — ND (GO_REF:0000015, SGD) — REMOVE (superseded by the
   generic transmembrane transporter activity terms already present; ND root is now
   redundant and less informative).
7. GO:0008150 biological_process — ND (GO_REF:0000015, SGD) — REMOVE (superseded by the
   generic transmembrane transport BP term already present).

Note on the UniProt DR block: GO:0015293 symporter activity (IEA, UniProtKB-KW) appears in
the UniProt cross-references but is NOT in the QuickGO GOA TSV pulled here, so it is not one
of the seven review rows. The "Symport" keyword is a family-level inference; there is no
MCH2 symport assay.

## Sources consulted
- PMID:11536335 (Makuc et al. 2001, Yeast) — the functional/negative study. Abstract-only.
- PMID:16204239 (Reihl & Stolz 2005, JBC) — Mch5p riboflavin; family "unrelated functions".
  Abstract-only.
- PMID:16847258 (Kim et al. 2006, PNAS) — global topology map; MCH2 topology constrained.
  Full text (HTML).
- PMID:8091865 (Alexandraki & Tzermia 1994, Yeast) — original chromosome-XI sequencing;
  ORF has "structure of membrane transporters". Abstract-only.
- UniProt:P36032 — record with negative FUNCTION statement, MFS/MCT similarity, 12 TM.
- file:yeast/MCH2/MCH2-bioinformatics/RESULTS.md — local fold/TM/motif analysis (see file).

## Review completion (annotation dispositions, final)

All 7 GOA annotations reviewed (no monocarboxylate-specific term was actually present in GOA;
the two transporter-activity rows are already generic GO:0022857, which is the defensible level):

1. GO:0005886 plasma membrane (IBA) — KEEP_AS_NON_CORE (phylogenetic inference; PM not directly
   demonstrated for MCH2; family study places some Mch proteins in intracellular membranes;
   propagation_review: NO_FAILURE_NON_CORE / COMPARTMENT_OR_COMPLEX_MISMATCH).
2. GO:0022857 transmembrane transporter activity (IBA) — ACCEPT (generic MF; the only defensible
   MF given no substrate; explicitly NOT specialized to a monocarboxylate term — no TM1 Lys, no
   motif A, experimental negative).
3. GO:0016020 membrane (IEA/SubCell) — ACCEPT (correct; confirmed 12-TMS integral membrane protein).
4. GO:0022857 transmembrane transporter activity (IEA/InterPro) — ACCEPT (same generic MF, InterPro route).
5. GO:0055085 transmembrane transport (IEA/InterPro) — ACCEPT (generic BP; substrate/direction unknown).
6. GO:0003674 molecular_function (ND/SGD) — REMOVE (root placeholder superseded by GO:0022857).
7. GO:0008150 biological_process (ND/SGD) — REMOVE (root placeholder superseded by GO:0055085).

core_functions: single generic transmembrane transporter (GO:0022857) in membrane (GO:0016020);
substrate deliberately left open. knowledge_gaps: unknown substrate/direction/mechanism/biological
role (WHOLLY_DARK), substrate-level BP_DARK on the core function, and paralog-redundancy residual
sub-gap (mch1-5 quintuple-only phenotype). Validation clean: schema, references, terms all pass.


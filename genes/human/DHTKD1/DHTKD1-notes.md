# DHTKD1 review notes

## Deep research status
`just deep-research-falcon human Q96HY7 --alias DHTKD1` failed in this environment:
`scripts/deep_research_wrapper.py` uses `X | None` type-union syntax that raises
`TypeError: unsupported operand type(s) for |` under the interpreter available here
(recipe fails on line 218). The OLS MCP also errored (`No module named 'rich.traceback'`).
No `-deep-research-*.md` file was fabricated. Review is grounded in the UniProt record
(`DHTKD1-uniprot.txt`), the seeded GOA, and cached `publications/PMID_*.md`. GO term
labels/aspects/obsolescence were verified directly against the QuickGO REST API.

## Verified biology (from UniProt Q96HY7 + PMID:29191460)
- DHTKD1 = **2-oxoadipate dehydrogenase complex component E1 (E1a / OADH-E1)**, a
  thiamine-diphosphate (ThDP)-dependent enzyme; paralog of OGDH (E1o).
  [UniProt: "2-oxoadipate dehydrogenase (E1a) component of the 2-oxoadipate
  dehydrogenase complex (OADHC)"]
- Catalyzes the **irreversible oxidative decarboxylation of 2-oxoadipate (alpha-
  ketoadipate)** to a glutaryl intermediate that is transferred to the lipoyl group of
  the shared E2 (DLST); overall complex product is glutaryl-CoA + CO2. First / rate-
  limiting step of OADHC. RHEA:69576. [UniProt CATALYTIC ACTIVITY]
- Rate-limiting last step of **L-lysine, L-hydroxylysine and L-tryptophan catabolism**,
  whose common intermediate is 2-oxoadipate. [UniProt FUNCTION]
- Shares E2 (DLST) and E3 (DLD) with the TCA-cycle 2-oxoglutarate dehydrogenase complex;
  E1 component is complex-specific. Can decarboxylate 2-oxoglutarate in vitro but ~49x
  prefers 2-oxoadipate. [PMID:29191460 abstract]
- Functional unit is a **homodimer**; interacts with DLST. [UniProt SUBUNIT; PMID:32695416]
- Cofactor: **thiamine diphosphate**. [UniProt COFACTOR; PMID:32695416]
- Localization: **mitochondrion / mitochondrial matrix**. [UniProt SUBCELLULAR LOCATION,
  PMID:23141294; Reactome]
- Disease: **alpha-aminoadipic/alpha-ketoadipic aciduria (AAKAD)** (often asymptomatic)
  and **Charcot-Marie-Tooth disease axonal type 2Q (CMT2Q)**. [UniProt DISEASE]

## Annotation-by-annotation reasoning
- MF `GO:0160166` 2-oxoadipate dehydrogenase activity — IDA (PMID:29191460) + RHEA IEA:
  **ACCEPT** both; this is the core catalytic activity.
- MF `GO:0016624` (oxidoreductase, aldehyde/oxo donor, disulfide acceptor) IEA: parent of
  the full E1+E2+E3 disulfide-acceptor reaction; DHTKD1 alone does the ThDP decarboxylation
  and transfers to the E2 lipoyl group (not disulfide). This is a broad InterPro-family
  term that better describes the complex than E1a in isolation → MARK_AS_OVER_ANNOTATED
  (not wrong at family level, but imprecise for the E1 subunit; GO:0160166 is the precise term).
- MF `GO:0030976` thiamine pyrophosphate binding IEA: **ACCEPT** — ThDP is the cofactor
  (UniProt COFACTOR, crystal structure PMID:32633484/32695416).
- The three `GO:0005515 protein binding` IPIs are from high-throughput interactome
  screens (BioPlex, HuRI/binary Y2H, BioPlex-derived). Per policy: bare protein binding
  IPIs → MARK_AS_OVER_ANNOTATED (uninformative; the biologically meaningful partner is
  DLST/E2, captured by the complex-membership term).
- CC mitochondrion/matrix (several IEA/IDA/HTP/TAS): ACCEPT the experimental matrix ones;
  the generic `mitochondrion` calls are correct but less precise than mitochondrial matrix.
- CC `GO:0160167` oxoadipate dehydrogenase complex IDA (PMID:29191460): ACCEPT — core.
- BP `GO:0019477` L-lysine catabolic process IEA: ACCEPT (core pathway).
- BP `GO:0009063` amino acid catabolic process IEA: correct but generic parent →
  KEEP_AS_NON_CORE.
- BP `GO:0006091` generation of precursor metabolites and energy IMP (PMID:23141294):
  the paper shows DHTKD1 silencing impairs ATP/NAD(H); this is a downstream/indirect
  physiological readout, not the gene's direct process → MARK_AS_OVER_ANNOTATED.

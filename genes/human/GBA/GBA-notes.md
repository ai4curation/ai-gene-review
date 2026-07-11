# GBA (GBA1) review notes

UniProt: P04062 (GBA_HUMAN). HGNC: GBA / GBA1. Lysosomal acid glucosylceramidase
(glucocerebrosidase, GCase; EC 3.2.1.45).

Deep research: falcon provider is OUT OF CREDITS (HTTP 402) at time of review, so
no `-deep-research-falcon.md` file. Review grounded in the UniProt record
(`GBA-uniprot.txt`), the seeded GOA (`GBA-goa.tsv`), and cached
`publications/PMID_*.md` (all 25 cited PMIDs are cached).

## Core biology (verified)

- **Molecular function**: glucosylceramidase (GCase, EC 3.2.1.45). Hydrolyses
  glucosylceramide/GlcCer (beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine) + H2O
  -> ceramide (N-acylsphing-4-enine) + D-glucose. UniProt FUNCTION and CATALYTIC
  ACTIVITY (RHEA:13269). Also hydrolyses glucosylsphingosine.
- Also has, at lower activity / in vitro or under specific conditions:
  galactosylceramidase activity (EC 3.2.1.46, RHEA:14297; PMID:32144204, not
  cached but UniProt-supported), cholesteryl-beta-glucosidase / GlcChol hydrolysis
  (RHEA:11956), and **transglucosylation** transferring glucose from GlcCer to
  cholesterol to make cholesteryl-glucoside (PMID:24211208, PMID:26724485). The
  glucosyltransferase/transglucosylase activity is a side reaction of the same
  active site (retaining glycosidase double-displacement), not a canonical
  biosynthetic transferase.
- **Activator**: saposin C (from prosaposin/PSAP), synergistic with saposin A;
  requires negatively charged phospholipids (phosphatidylserine). Saposin C
  promotes membrane association of the enzyme (PMID:9201993, PMID:10781797).
- **Localization**: lysosome / lysosomal lumen; peripheral (lumenal-side) lysosomal
  membrane protein. Reaches lysosome by an M6P-independent route via its transport
  receptor LIMP-2/SCARB2, forming a complex in the ER that traffics through the
  Golgi/TGN to the lysosome (PMID:18022370, PMID:25202012, PMID:40159502).
- **Pathway**: penultimate step of glycosphingolipid (GSL) catabolism; also feeds
  the PKC-activated ceramide salvage pathway (PMID:19279011).
- **Disease**: deficiency -> Gaucher disease (commonest lysosomal storage disorder).
  GBA1 variants are the numerically greatest genetic risk factor for Parkinson
  disease / dementia with Lewy bodies (PMID:25456120, PMID:26388395, PMID:21700325).

## Annotation triage logic

CORE (accept, represent the gene's function):
- GO:0004348 glucosylceramidase activity (MF) — many IDA/IMP/IBA lines. This is the
  exact current GOA MF term. Use in core_functions.
- GO:0006680 glucosylceramide catabolic process (BP) — many IDA/IMP/IBA lines.
- lysosome / lysosomal lumen / lysosomal membrane (CC).

SECONDARY enzymatic activities (real but non-core / in-vitro side reactions):
- GO:0004336 galactosylceramidase activity — real but low; keep, IEA acceptable.
- GO:0050295 steryl-beta-glucosidase activity (IDA PMID:24211208, PMID:26724485;
  RHEA:11956) — real GlcChol hydrolysis; keep non-core.
- GO:0046527 glucosyltransferase activity (IDA, transglucosylation to cholesterol)
  — real side reaction; keep non-core (not canonical anabolic transferase).
- GO:0008422 beta-glucosidase activity — parent/broad; the bile-acid-glucosidase
  work (PMID:22659419) supports broad beta-glucosidase. Keep.
- GO:0009247 glycolipid biosynthetic process (IDA PMID:24211208, PMID:26724485) —
  refers to cholesterol glucosylation (GlcChol formation) via transglucosylation.
  Non-core; the enzyme is primarily catabolic. Keep as non-core.

DOWNSTREAM / INDIRECT physiology (mark over-annotated or non-core; these follow from
loss of the catabolic activity, not a distinct molecular action of GBA):
- inflammation / IL-6 / MAPK / TNF / termination of signal transduction
  (PMID:19279008) — ceramide-mediated signalling downstream effects in MCF-7 cells.
- autophagy / lysosome organization / TOR / macroautophagy / lysosomal protein
  catabolism (PMID:27378698, PMID:26388395, PMID:26392287) — consequences of GCase
  deficiency on the autophagy-lysosome pathway.
- cholesterol metabolic process — secondary; via GlcChol transglucosylation and
  lysosomal lipid handling.
- ceramide/sphingosine biosynthetic process (PMID:19279011) — the salvage pathway;
  ceramide IS a direct product of GlcCer hydrolysis, so ceramide "biosynthetic"
  here overlaps with catabolism of GlcCer. Keep as non-core.
- neuronal action potential / mitochondrion organization NOT / neuron projection
  development NOT (PMID:25456120) — PD-model phenotypes; the two NOT annotations are
  supported (normal mitochondria and normal neurite outgrowth in GBA-N370S neurons).

BINDING annotations:
- GO:0005515 protein binding IPIs (TCP1 PMID:21098288; PGRN/GRN PMID:27789271;
  LIMP-2 PMID:24162852) — bare protein binding, uninformative; MARK_AS_OVER_ANNOTATED.
- GO:0005124 scavenger receptor binding / GO:0005102 signaling receptor binding —
  these describe GBA binding to LIMP-2/SCARB2 (a scavenger-receptor family protein).
  The biologically meaningful partner is the LIMP-2 transporter; keep as non-core
  (they capture the LIMP-2 interaction, informative-ish but peripheral).

CC extras:
- ER / Golgi / trans-Golgi network (ISS/IEA from mouse) — transit compartments of
  the LIMP-2 route; keep non-core.
- extracellular exosome (HDA, prostatic secretion proteomics PMID:23533145) — mass-
  spec bystander; keep non-core.

Skin barrier / epidermis / hormone-response IEAs (from rat ortholog M0R3L8,
GO_REF:0000107): peripheral electronically-transferred physiology; keep non-core.

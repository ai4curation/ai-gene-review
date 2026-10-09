# crtY (P21687) — Pantoea ananatis lycopene beta-cyclase — review notes

## Identity
- UniProt P21687, CRTY_PANAN, 382 aa, EC 5.5.1.19, "Lycopene beta-cyclase" / "Lycopene cyclase".
- Organism Pantoea ananatis (historically Erwinia uredovora), NCBITaxon:553. The historical
  name "Erwinia uredovora" in the primary papers is the same organism as the UniProt entry
  [file:PANAN/crtY/crtY-uniprot.txt "Pantoea ananas (Erwinia uredovora)."].
- Deep research confirms correct identity: "The target is correctly identified as CrtY, the
  lycopene β-cyclase of Pantoea ananatis" and it is not a plant LCYB or fungal bifunctional
  cyclase [file:PANAN/crtY/crtY-deep-research-falcon.md].
- No PANTHER family is assigned to this protein in UniProt; the module records that CrtY is the
  Pantoea exemplar in UniProt "so no family id" (modules/carotene_backbone_biosynthesis.yaml).
- No FEBA fitness data exists for this organism.

## Function
- Catalyses the double cyclization of all-trans-lycopene to all-trans-beta-carotene, forming a
  beta-ionone ring at each psi-end, via the monocyclic intermediate gamma-carotene
  [file:PANAN/crtY/crtY-uniprot.txt "Catalyzes the double cyclization reaction which converts"
  / "lycopene to beta-carotene"]. UniProt records the sub-reactions
  all-trans-lycopene = gamma-carotene (RHEA:32219) and gamma-carotene = all-trans-beta-carotene
  (RHEA:32239), plus the generic RHEA:55620.
- Two-end cyclase: "The enzyme creates one β-ionone ring at each acyclic ψ-end of lycopene"
  [file:PANAN/crtY/crtY-deep-research-falcon.md].
- Pathway position: CrtE->CrtB->CrtI produces lycopene; CrtY cyclises it to beta-carotene;
  CrtZ hydroxylates to zeaxanthin; CrtX glycosylates. Deletion of crtY (ORF-C) causes lycopene
  accumulation: "Removing ORF-C caused lycopene accumulation, whereas constructs containing
  ORF-C produced β-carotene" [file:PANAN/crtY/crtY-deep-research-falcon.md; primary
  PMID:2254247, abstract-only cache].
- Misawa 1990 named the six-gene cluster: "Six open reading frames were found and designated
  the crtE, crtX, crtY, crtI, crtB, and crtZ genes" [PMID:2254247].

## Mechanism / cofactor (key to the oxidoreductase call)
- CrtY is an ISOMERASE (EC 5.5.1.19), not an oxygenase. It requires FAD as cofactor
  [file:PANAN/crtY/crtY-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692;"], catalytically active
  in the reduced state, but the carotenoid reaction is NON-REDOX.
- PMID:20178989 (abstract-only cache; full_text_available: false) title: "catalyzes an
  FADred-dependent non-redox reaction." Abstract: "We show that reduced FAD is the essential
  lycopene cyclase (CrtY) cofactor" and "a catalytic mechanism relying on cryptic (net)
  electron transfer can be refuted"; "Lycopene cyclase, thus, ranks among the novel class of
  non-redox flavoproteins."
- Activity is increased by NAD(P)H but NADPH is not incorporated and acts indirectly
  [file:PANAN/crtY/crtY-uniprot.txt "Activity is increased in the presence of NAD(P)H"].
- E199A mutant loses activity but still binds FAD [file:PANAN/crtY/crtY-uniprot.txt
  "E->A: Loss of activity. Still binds FAD."].
- Consequence for annotation: the InterPro2GO row GO:0016705 (oxidoreductase acting on paired
  donors, with incorporation or reduction of molecular oxygen) is biologically wrong — no O2 is
  incorporated and there is no net redox change ("no net oxidation or reduction of the
  carotenoid occurs" [file:PANAN/crtY/crtY-deep-research-falcon.md]). The FAD/NAD(P)-binding
  fold (IPR010108/Gene3D 3.50.50.60) is what misled InterPro2GO. REMOVE.

## Localization
- UniProt: "SUBCELLULAR LOCATION: Cell inner membrane" with ECO:0000269|PubMed:20178989;
  "Note=Membrane-bound." In a gram-negative bacterium the inner (cytoplasmic) membrane is the
  plasma membrane, so GO:0005886 plasma membrane is the correct CC term. The GOA EXP row cites
  PMID:20178989; the cached abstract is mechanism-only, but UniProt attributes the membrane
  location to that paper's full text, so the experimental call is retained (do not overrule the
  curator from an abstract-only cache).
- Deep research: functions "at the cytoplasmic-membrane interface" as a
  "membrane-associated/peripheral enzyme acting on a membrane-embedded substrate."

## Annotation decisions (5 GOA rows)
1. GO:0005886 plasma membrane, EXP, PMID:20178989 — ACCEPT (cell inner membrane = plasma membrane).
2. GO:0005886 plasma membrane, IEA, GO_REF:0000044 (SL-0037) — ACCEPT (SubCell mapping, concordant).
3. GO:0016117 carotenoid biosynthetic process, IEA, GO_REF:0000002 — ACCEPT (core process; CrtY catalyses a step).
4. GO:0016705 oxidoreductase..., IEA, GO_REF:0000002 (IPR010108) — REMOVE (enzyme is a non-redox isomerase; no O2 incorporation).
5. GO:0045436 lycopene beta cyclase activity, IEA, GO_REF:0000120 (IPR008461, RHEA:32219) — ACCEPT (defining MF, EC 5.5.1.19, experimentally established).

## NEW proposal
- GO:1901812 beta-carotene biosynthetic process. CrtY does the catalytic work of this process
  (it forms both beta rings, yielding beta-carotene), so participation is satisfied directly —
  this is not a substrate/necessity artefact. QuickGO confirms GO:1901812 is_a descendant of
  both GO:0016117 (already carried) and GO:0016120; it names the specific product process and
  adds real specificity over the generic carotenoid term. I do NOT also propose GO:0016120
  (it would be an ancestor of GO:1901812 — redundant). Comparator trap does not apply: the
  argument is direct catalysis of beta-carotene formation, not "other cyclases have it."

## Term verification (QuickGO, 2026-09-28)
- GO:0045436 lycopene beta cyclase activity — MF, not obsolete. Def matches (beta rings -> gamma/beta-carotene).
- GO:0016705 — MF, def: redox reaction, molecular oxygen reduced/incorporated. Contradicts non-redox isomerase.
- GO:1901812 beta-carotene biosynthetic process — BP, not obsolete; ancestors include GO:0016117 and GO:0016120.
- GO:0016117 carotenoid biosynthetic process — BP, not obsolete.
- GO:0016120 carotene biosynthetic process — BP, not obsolete (used only to check redundancy; not annotated).

## Provenance of identifiers
All GO ids from QuickGO or the GOA rows; Rhea ids (32219/32239/55620) and EC 5.5.1.19 from the
UniProt record; PMIDs from the cached publications. No identifiers taken from the deep-research
report.

## Publication cache + quote verification (2026-09-28, completion run)
- All four UniProt-cited PMIDs now cached, all abstract-only (full_text_available: false):
  PMID:2254247, PMID:8898919, PMID:11943208, PMID:20178989. GOA cites only PMID:20178989.
- PMID:20178989 abstract confirms the non-redox FADred mechanism verbatim: "We show that
  reduced FAD is the essential lycopene cyclase (CrtY) cofactor" and "Lycopene cyclase,
  thus, ranks among the novel class of non-redox flavoproteins". Localization is NOT in the
  abstract (mechanism-only); UniProt attributes "Cell inner membrane" to this paper's full
  text (ECO:0000269), so the EXP plasma-membrane row is retained per the do-not-overrule rule.
- PMID:11943208 abstract confirms NADPH is not incorporated/indirect: "No hydrogen is
  transferred from NADPH, which is therefore not involved directly in the cyclization
  reaction, but must play an indirect role, e.g. as an allosteric activator."
- PMID:8898919 abstract confirms alternative-substrate cyclization (neurosporene ->
  7,8-dihydro-beta-carotene via beta-zeacarotene; zeta-carotene -> tetrahydro-beta-carotene).
- PMID:2254247 abstract confirms the six-gene cluster naming and pathway order; its inline
  pathway diagram is garbled by extraction (do not quote that fragment).
- Deep-research verbatim strings usable as file: support (ASCII only): "no net oxidation or
  reduction of the carotenoid occurs"; "membrane-associated/peripheral enzyme acting on a
  membrane-embedded substrate"; "No experimentally solved three-dimensional structure of
  P21687 was identified in the retrieved literature."
- Note: UniProt DR block lists GO:0005737 cytoplasm (IEA:UniProtKB-ARBA), but this row is
  NOT in the GOA tsv, so it is not an existing_annotation to review.

## NEW proposal reconsidered against the CLAUDE.md redundancy rule
- GO:1901812 beta-carotene biosynthetic process is a descendant of GO:0016117 (already
  carried). The redundancy caution applies, but CrtY *directly catalyses* both beta-ring
  cyclizations that create beta-carotene (participation satisfied by catalysis, not by
  necessity/substrate), so the specific product-process term is more informative than the
  generic carotenoid term and is retained as NEW. GO:0016120 is NOT proposed (it would be an
  ancestor of GO:1901812 and is not even a descendant of GO:0016117 in the current ontology).

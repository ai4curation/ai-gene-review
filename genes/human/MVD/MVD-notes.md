# MVD (Diphosphomevalonate decarboxylase) — review notes

UniProtKB: P53602 (MVD1_HUMAN), gene MVD (synonym MPD). 400 aa, ~43 kDa subunit. HGNC:7529.

## Core function

MVD catalyses the final step of the mevalonate (MVA) pathway: the ATP-dependent
decarboxylation of (R)-5-diphosphomevalonate (mevalonate-5-diphosphate) to isopentenyl
diphosphate (IPP) + CO2 (+ ADP + Pi). EC 4.1.1.33; RHEA:23732.

- [file:human/MVD/MVD-uniprot.txt "Catalyzes the ATP dependent decarboxylation of (R)-5-diphosphomevalonate to form isopentenyl diphosphate (IPP)"]
- [PMID:18823933 "Mevalonate diphosphate decarboxyase (MDD1; EC 4.1.1.33) catalyzes the ATP dependent decarboxylation of mevalonate 5-diphosphate (MVAPP) to form isopentenyl 5-diphosphate"]
- Reaction (UniProt): (R)-5-diphosphomevalonate + ATP = isopentenyl diphosphate + ADP + CO2 + phosphate.

IPP is the fundamental C5 isoprenoid building block; this reaction feeds sterol
(cholesterol) and non-sterol isoprenoid biosynthesis (dolichol, ubiquinone, prenyl
groups for protein prenylation).
- [PMID:18823933 "The reaction is required for production of polyisoprenoids and sterols from acetyl-CoA."]

## Structure / family

- GHMP kinase superfamily member. [PMID:18823933 "MDD is a member of the GHMP kinase (galactokinase, homoserine kinase, mevalonate kinase, phosphomevalonate kinase) family of proteins."]
- Homodimer of ~43-kDa subunits. [PMID:8626466 "The recombinant human enzyme is a homodimer of 43-kDa subunits with a specific activity of 2.4 units/mg."] Also UniProt SUBUNIT: Homodimer.
- Crystal structure 3D4J (2.4 Å); R161 and N17 are active-site residues important for binding/orientation of mevalonate diphosphate. R161Q ~1000-fold loss of activity. [PMID:18823933 "R161Q exhibits a approximately 1000-fold diminution in specific activity"]
- ATP-binding (KW: ATP-binding; Nucleotide-binding). [file:human/MVD/MVD-uniprot.txt "F:ATP binding; IEA:UniProtKB-KW"]

## Localization

- Cytosolic. Earlier claims of peroxisomal targeting were refuted.
- [PMID:14972328 "We found a cytosolic localization for both endogenous human mevalonate pyrophosphate decarboxylase ... but no indication for a peroxisomal localization."]
- UniProt CAUTION: "Was originally thought to be located in the peroxisome (PubMed:11108725). However, was later shown to be cytosolic (PubMed:14972328)."
- GOA carries a NOT located_in peroxisome (IDA, PMID:14972328) — consistent.

## Disease

- Porokeratosis 7, multiple types (POROK7; MIM:614714), a disorder of faulty
  keratinization (cornoid lamella). MVD and MVK are the principal porokeratosis genes.
  Many POROK7 missense variants; R161Q abolishes decarboxylase activity.
  [PMID:26202976 — "Genomic variations of the mevalonate pathway in porokeratosis"]
  (variant paper; also UniProt DISEASE + VARIANT annotations)

## Notes on specific annotations

- Multiple EXP/IDA GO:0004163 annotations (PMID:18823933, 8626466, 9392419, 11792727,
  14680974) — core catalytic function, all ACCEPT (one as core, rest KEEP_AS_NON_CORE
  duplicates).
- GO:0008299 isoprenoid biosynthetic process — the enzyme's product IPP is the isoprenoid
  precursor; ACCEPT as a broader BP framing. GO:0019287 (isopentenyl diphosphate
  biosynthetic process, mevalonate pathway) is the precise BP — core.
- GO:0006695 cholesterol biosynthetic process (NAS/IEA UniPathway) — MVA pathway feeds
  cholesterol synthesis but MVD is upstream of the sterol branch point; the direct product
  is IPP, and IPP also feeds non-sterol isoprenoids. Cholesterol is a downstream
  consequence, not MVD's direct BP. KEEP_AS_NON_CORE (over-specific; the mevalonate/IPP
  BP is the accurate direct process).
- GO:0016831 carboxy-lyase activity (IEA, InterPro) — true but a broad parent of the
  specific GO:0004163; MODIFY toward the specific term (or accept as broader). Marked as
  over-annotated/parent; propose replacement GO:0004163.
- GO:0030544 Hsp70 protein binding (IPI, PMID:12646231) — mortalin (mot-2/GRP75, HSP70
  family) interaction from a Y2H screen; bare protein-binding-type MF, not the core
  catalytic function. Per policy, do NOT REMOVE an experimental IPI whose full text is
  unverified → MARK_AS_OVER_ANNOTATED.
- GO:0042803 protein homodimerization activity (IDA, PMID:8626466) — supported (homodimer),
  KEEP_AS_NON_CORE.
- GO:0008284 positive regulation of cell population proliferation (IMP, PMID:9270019) —
  the paper shows Fmev (an MVD inhibitor) blocks proliferation via loss of downstream
  prenylated Ras; this is an indirect pathway-level effect (mevalonate products drive
  proliferation), not a distinct MVD signalling function. KEEP_AS_NON_CORE.
- Localization terms: cytosol (GO:0005829) ACCEPT; cytoplasm (GO:0005737) ACCEPT as
  broader parent; NOT peroxisome ACCEPT (correct negation).

## Provenance

Deep research provider (falcon) was out of credits (HTTP 402) at review time; no
-deep-research-falcon.md generated. Review grounded in MVD-uniprot.txt, seeded GOA, and
cached publications/PMID_*.md (all 8 cited PMIDs present).

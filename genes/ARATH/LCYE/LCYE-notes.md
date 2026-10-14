# LCYE (LUT2, At5g57030, UniProt Q38932) — curation notes

Arabidopsis thaliana lycopene epsilon cyclase (chloroplastic). EC 5.5.1.18. Primary UniProt
gene name LUT2 (LUTEIN DEFICIENT 2). This journal records what each cached source actually
shows and the reasoning behind each annotation action.

## Identity / gestalt

LCYE is the plant lycopene epsilon-cyclase, one of the two lycopene cyclases at the central
branch point of plastid carotenoid biosynthesis. It forms a single epsilon ring at one psi-end
of all-trans-lycopene to give the monocyclic delta-carotene; a beta-cyclase (LCYB) then forms
a beta ring at the other end to give alpha-carotene, which is hydroxylated (LUT1/CYP97C1 on the
epsilon ring, LUT5/CYP97A3 and CHY1/CHY2 on the beta ring) to zeinoxanthin and then lutein.
Thus LCYE commits flux into the beta,epsilon (alpha-carotene/lutein) branch versus the beta,beta
(beta-carotene/zeaxanthin/violaxanthin/neoxanthin) branch. It is a nuclear-encoded,
plastid-targeted, membrane-associated flavoenzyme.

- UniProt EC and reaction [file:ARATH/LCYE/LCYE-uniprot.txt "EC=5.5.1.18"];
  [file:ARATH/LCYE/LCYE-uniprot.txt "a carotenoid psi-end derivative = a carotenoid epsilon-end"]
  (Rhea:RHEA:55616).
- Function statement [file:ARATH/LCYE/LCYE-uniprot.txt "epsilon-cyclization reaction which converts lycopene to delta-carotene"];
  [file:ARATH/LCYE/LCYE-uniprot.txt "Required for lutein biosynthesis (PubMed:9789087)."].
- Family [file:ARATH/LCYE/LCYE-uniprot.txt "Belongs to the lycopene cyclase family."]; PANTHER
  PTHR39757:SF3 (LYCOPENE EPSILON CYCLASE, CHLOROPLASTIC) per UniProt DR line and
  modules/carotene_backbone_biosynthesis.yaml.

## Cached publications (availability + what they show)

- PMID:8837512 (Cunningham 1996, "Functional analysis of the beta and epsilon lycopene cyclase
  enzymes of Arabidopsis"). full_text_available: FALSE (abstract only). Primary functional/
  catalytic paper: identified and expressed the beta and epsilon cyclase cDNAs; epsilon cyclase
  adds one ring giving delta-carotene, beta cyclase adds two giving beta-carotene, combined they
  give alpha-carotene. [PMID:8837512 "both enzymes use the linear, symmetrical"];
  [PMID:8837512 "forming the monocyclic delta-carotene (epsilon, psi-carotene)"];
  [PMID:8837512 "The cyclization of lycopene (psi, psi-carotene) is a key branch point"].
  UniProt cites this for FUNCTION and CATALYTIC ACTIVITY (ECO:0000269). GOA attributes the
  chloroplast TAS row to this PMID.

- PMID:8837513 (Pogson 1996, "Arabidopsis carotenoid mutants demonstrate that lutein is not
  essential"). full_text_available: FALSE (abstract only). Genetics paper defining lut1 and
  lut2. lut2 = disruption of epsilon-ring cyclization; cosegregates with the epsilon cyclase
  gene. [PMID:8837513 "phenotype is consistent with a disruption of epsilon ring cyclization."];
  [PMID:8837513 "locus cosegregates with the recently isolated epsilon cyclase gene"];
  [PMID:8837513 "lutein biosynthesis but not for the biosynthesis of beta, beta-carotenoids."];
  [PMID:8837513 "regulating lutein levels and the ratio of lutein to beta,beta-carotenoids."].
  GOA attributes the GO:0016117 IMP row and the GO:0045435 lycopene epsilon cyclase activity TAS
  row to this PMID. (The catalytic characterization itself is in Cunningham PMID:8837512/
  PMID:11226339, but the function is correct for the gene, so these are ACCEPTed and the curator
  deferred to.)

- PMID:9789087 (Pogson 1998, "Altered xanthophyll compositions..."). full_text_available: TRUE.
  lut2 eliminates lutein, replaced mainly by violaxanthin/antheraxanthin; lut2 confirmed as a
  disruption of lycopene epsilon-cyclase; both zeaxanthin and lutein contribute to NPQ.
  [PMID:9789087 "lutein is replaced mainly by a stoichiometric increase in violaxanthin"];
  [PMID:9789087 "The lut2 mutation eliminates lutein production and is"];
  [PMID:9789087 "both zeaxanthin and lutein contribute to nonphotochemical quenching"].
  UniProt cites this for FUNCTION (Required for lutein biosynthesis) and DISRUPTION PHENOTYPE.

- PMID:11226339 (Cunningham & Gantt 2001, "One ring or two?"). full_text_available: TRUE.
  Arabidopsis LCYe adds one epsilon-ring to lycopene giving delta-carotene; a single-residue
  molecular switch (Arabidopsis L448) determines mono- vs bi-epsilon-cyclase; L448H/L448R yield
  bi-epsilon-cyclase. [PMID:11226339 "adds one epsilon-ring to the symmetrical linear substrate lycopene"];
  [PMID:11226339 "A single amino acid was found to act as a molecular switch: lettuce"];
  [PMID:11226339 "complementary Arabidopsis LCYe mutant, L448H, added two epsilon-rings."].
  UniProt cites this for CATALYTIC ACTIVITY and the ALA-447/LEU-448 MUTAGENESIS features.

- PMID:16890225 (Fiore 2006, "Elucidation of the beta-carotene hydroxylation pathway").
  full_text_available: FALSE (abstract only). Constructed double/triple mutants in CHY1, CHY2,
  LUT1, LUT5 and LUT2 (lycopene epsilon-cyclase); chy1chy2lut2 leaves are ~80% beta-carotene.
  [PMID:16890225 "We\nconstructed double and triple mutant combinations in CHY1, CHY2, LUT1, LUT5 and\nLUT2 (lycopene epsilon-cyclase)."].
  GOA source of the GO:0016123 xanthophyll biosynthetic process IGI row (WITH/FROM
  AT4G25700 = CHY1/BCH1, AT5G52570 = CHY2/BCH2). Experimental genetic-interaction annotation;
  defer to curator.

## Ontology checks (QuickGO, 2026-09-28)

Verified is_a ancestry of GO:0045435 lycopene epsilon cyclase activity:
`['GO:0003824','GO:0045435','GO:0016860','GO:0003674','GO:0009975','GO:0016853']`.

- GO:0009975 cyclase activity IS a true parent of GO:0045435 -> correct but general -> MODIFY to
  GO:0045435.
- GO:0016860 intramolecular oxidoreductase activity IS a true parent of GO:0045435 (GO places
  the plant lycopene cyclases under intramolecular oxidoreductase / isomerase, not under
  intramolecular lyase) -> correct but general -> MODIFY to GO:0045435. (Do NOT REMOVE: despite
  the EC 5.5.1.18 lyase classification, the GO ontology genuinely nests the specific term here.)
- GO:0016705 (oxidoreductase, acting on paired donors, with incorporation or reduction of
  molecular oxygen) is NOT in the ancestor set of GO:0045435 -> genuinely wrong function. LCYE
  is a cyclase/isomerase (reaction: psi-end -> epsilon-end derivative, no O2 incorporation, no
  net redox). The InterPro2GO mapping from IPR010108 (shared FAD/NAD-binding fold of the
  lycopene cyclase family) to a monooxygenase activity is incorrect for this enzyme -> REMOVE
  per the brief (IEA InterPro2GO assigning an activity the protein does not have).
- GO:1901824 alpha-carotene biosynthetic process is a descendant of GO:0016117 (which LCYE
  already carries). LCYE genuinely forms the epsilon ring of alpha-carotene, but per the
  CLAUDE.md redundancy rule (do not propose a NEW term that is a descendant of one the gene
  already carries) I am NOT proposing it as NEW. Recorded as a suggested question instead.

## Annotation-by-annotation decisions

1. GO:0009507 chloroplast, ISM, GO_REF:0000122 — ACCEPT (location; transit peptide + plastid).
2. GO:0009507 chloroplast, TAS, PMID:8837512 — ACCEPT (location).
3. GO:0009975 cyclase activity, IEA, GO_REF:0000117 (ARBA) — MODIFY -> GO:0045435 (general parent).
4. GO:0016117 carotenoid biosynthetic process, IEA, GO_REF:0000002 (InterPro) — ACCEPT (core process).
5. GO:0016117 carotenoid biosynthetic process, IMP, PMID:8837513 — ACCEPT (experimental, core process).
6. GO:0016123 xanthophyll biosynthetic process, IBA, GO_REF:0000033 — ACCEPT (committed step to
   the beta,epsilon-xanthophyll lutein; considered PAINT judgment at PTN008674247).
7. GO:0016123 xanthophyll biosynthetic process, IGI, PMID:16890225 — ACCEPT (experimental
   genetic interaction with the ring hydroxylases; defer to curator).
8. GO:0016705 oxidoreductase, paired donors, O2 IEA, GO_REF:0000002 (InterPro) — REMOVE (wrong
   function; LCYE is a cyclase, not a monooxygenase; not an ancestor of GO:0045435).
9. GO:0016860 intramolecular oxidoreductase activity, IEA, GO_REF:0000117 (ARBA) — MODIFY ->
   GO:0045435 (true but general parent).
10. GO:0031969 chloroplast membrane, IEA, GO_REF:0000044 — ACCEPT (multi-pass membrane protein;
    two TRANSMEM helices).
11. GO:0045435 lycopene epsilon cyclase activity, TAS, PMID:8837513 — ACCEPT (core molecular function).

## NEW annotations

None proposed. The molecular function (lycopene epsilon cyclase activity), the direct processes
(carotenoid and xanthophyll biosynthetic process) and the locations (chloroplast, chloroplast
membrane) are already captured. alpha-carotene biosynthetic process (GO:1901824) would be a
descendant of an already-carried term and is deliberately not proposed.

## UNDECIDED

None. All PMIDs referenced are cached (two full-text, three abstract-only); the abstracts plus
UniProt curation are sufficient to adjudicate every row without overruling any experimental
annotation.

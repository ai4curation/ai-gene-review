# LCYB (LCY1 / LYC / SZL1, At3g10230, UniProt Q38933) — curation notes

Arabidopsis thaliana lycopene beta cyclase, chloroplastic. EC 5.5.1.19.

## Identity

- UniProt Q38933, LCYB_ARATH; gene names LCY1 / LCYB / LYC / SZL1; locus AT3G10230.
- Single-copy major lycopene beta-cyclase of Arabidopsis. Identity unambiguous
  (deep-research report confirms Q38933 = At3g10230, the one principal LCYB, and
  szl1 was genetically mapped to this structural gene).
- 501 aa precursor with an N-terminal chloroplast transit peptide (1..48), mature
  chain 49..501 [file:ARATH/LCYB/LCYB-uniprot.txt "TRANSIT         1..48"].
- Belongs to the lycopene cyclase family [file:ARATH/LCYB/LCYB-uniprot.txt
  "Belongs to the lycopene cyclase family"]. Domains: Lycopene_cyclase_b/e
  (IPR010108), FAD/NAD(P)-binding fold (IPR036188). Flavoprotein; NAD(+) binding
  site 85..113.

## Molecular function (well established)

- Catalyzes the double cyclization that converts all-trans-lycopene to beta-carotene
  (two beta-ionone rings) [file:ARATH/LCYB/LCYB-uniprot.txt "converts lycopene to
  beta-carotene and"]. UniProt catalytic activity: "a carotenoid psi-end derivative =
  a carotenoid beta-end derivative", Rhea:55620, EC 5.5.1.19
  [file:ARATH/LCYB/LCYB-uniprot.txt "Reaction=a carotenoid psi-end derivative = a
  carotenoid beta-end"; "EC=5.5.1.19"].
- Cunningham et al. 1996 (primary functional paper, cached abstract-only,
  full_text_available: false): the beta cyclase "introduces a ring at both ends of
  lycopene to form the bicyclic beta-carotene"; both beta and epsilon cyclases use
  the symmetrical lycopene as substrate; when combined with LCYE the two enzymes
  convert lycopene to alpha-carotene [PMID:8837512 "introduces a ring at both ends of
  lycopene to form the bicyclic"; "both enzymes use the linear, symmetrical";
  "cyclases convert lycopene to alpha-carotene"]. Lycopene cyclization "is a key
  branch point" of carotenoid biosynthesis [PMID:8837512 "is a key branch point"].
- Li et al. 2009 (szl1 = point mutation in LCYB, cached abstract-only): "szl1
  contains a point mutation in the lycopene beta-cyclase (LCYB) gene"; "LCYB appears
  to be the major lycopene beta-cyclase and is not involved in neoxanthin synthesis"
  [PMID:19549928]. The mutant enzyme (Gly451Glu, per UniProt MUTAGEN) is hypomorphic:
  szl1 npq1 has low violaxanthin, antheraxanthin, neoxanthin (beta,beta-xanthophylls)
  and accumulates more lutein and alpha-carotene, i.e. flux shifts toward the
  beta,epsilon branch [PMID:19549928 "have low levels of violaxanthin, antheraxanthin,
  and neoxanthin"; "they accumulate more lutein and alpha-carotene than the wild type"].
- Mechanistic note (deep research, ruizsola2012 / dellapenna2006): plant LCYB is a
  flavoprotein requiring reduced FAD, but ring formation has NO net redox change — FAD
  assists catalysis (carbocation stabilization), it is not consumed as an oxidant.
  This is why the enzyme is classified as an intramolecular lyase / isomerase
  (EC 5.5.1.19), NOT an oxidoreductase.

## Localization

- Nuclear-encoded chloroplast precursor; UniProt "SUBCELLULAR LOCATION: Plastid,
  chloroplast" [file:ARATH/LCYB/LCYB-uniprot.txt]. Membrane-associated within the
  plastid (deep research favors envelope-associated carotenoid machinery, but exact
  intraplastid topology is unresolved for Q38933). Chloroplast is well supported;
  no experimental mitochondrial localization exists.

## Pathway role

- First committed cyclization branch point after all-trans-lycopene. Two beta
  cyclizations -> gamma-carotene -> beta-carotene (beta,beta branch, feeding
  zeaxanthin/violaxanthin/neoxanthin xanthophylls). With LCYE it contributes the
  beta-ring of alpha-carotene (beta,epsilon branch, feeding lutein). UniProt pathways:
  "Carotenoid biosynthesis; beta-carotene biosynthesis." and beta-zeacarotene
  biosynthesis [file:ARATH/LCYB/LCYB-uniprot.txt].
- Salt/oxidative-stress tolerance (PMID:21471119): overexpression of AtLCY (and
  SeLCY) increases carotenoids and improves salt tolerance by reducing ROS
  [PMID:21471119 "improved salt tolerance by increasing synthesis of"]. This is a
  downstream, gain-of-function/pleiotropic consequence of increased carotenoid pools,
  not a distinct molecular activity — treat as non-core context, keep in
  description/notes rather than a process annotation.

## Annotation-by-annotation reasoning

The GOA rows fall into two groups by phylogenetic source. PANTHER's per-organism
classification places Q38933 in **PTHR43876:SF15**, a subfamily of a family named for
the **COQ6 mitochondrial ubiquinone monooxygenase** (module knowledge_gap records
this; UniProt instead cross-references PTHR39757:SF5). The FAD/NAD fold is shared with
COQ6, so PANTHER's HMM swept LCYB into the COQ6 clade. A set of GO_Central IBAs at
node **PTN000350182** (donors: yeast COQ6 SGD:S000003487, human COQ6 Q9Y2Z9, mouse
MGI:1924408, PomBase SPBC146.12, fly, worm) therefore propagated the ancestral COQ6
functions — mitochondrion, ubiquinone biosynthesis, oxidoreductase — onto LCYB. These
are functionally wrong for the diverged plant lycopene cyclase and are removed on
biological grounds (this is over-propagated IBA, not second-guessing an experimental
annotation).

A separate, correct set of IBAs sits at the lycopene-cyclase-specific nodes
**PTN001789482** (lycopene beta cyclase activity, donor AGI_LocusCode:AT3G10230 =
LCYB itself, expected/not circular) and **PTN001789479** (xanthophyll biosynthetic
process, donor plant LCYB K4C9E2). Those are accepted.

1. GO:0005739 mitochondrion (IBA, PTN000350182) — REMOVE. COQ6-clade propagation;
   LCYB is a chloroplast enzyme (compartment mismatch + functional divergence). No
   mitochondrial evidence.
2. GO:0006744 ubiquinone biosynthetic process (IBA, PTN000350182) — REMOVE. Ancestral
   COQ6 monooxygenase role; LCYB does not participate in ubiquinone biosynthesis
   (functional divergence).
3-5. GO:0009507 chloroplast (IEA SubCell / ISM AtSubP / TAS PMID:8837512) — ACCEPT all
   three. Correct organelle, consistent with transit peptide and UniProt.
6. GO:0009975 cyclase activity (IEA ARBA) — MODIFY -> GO:0045436. Verified true parent
   of GO:0045436 (QuickGO is_a ancestors of GO:0045436 include GO:0009975) but too
   general; specific term is experimentally supported.
7. GO:0016117 carotenoid biosynthetic process (IDA PMID:8837512) — ACCEPT. Core BP.
8. GO:0016117 carotenoid biosynthetic process (IEA InterPro IPR010108) — ACCEPT.
   IPR010108 = lycopene cyclase family; correct process.
9. GO:0016123 xanthophyll biosynthetic process (IBA PTN001789479) — KEEP_AS_NON_CORE.
   LCYB supplies the committed beta-ring precursor of beta,beta-xanthophylls; szl1
   reduces violaxanthin/antheraxanthin/neoxanthin, so participation is real but
   downstream of the core cyclase step.
10. GO:0016491 oxidoreductase activity (IBA, PTN000350182) — REMOVE. COQ6-clade
    propagation. QuickGO: GO:0016491 is NOT an is_a ancestor of GO:0045436 (lycopene
    cyclase sits under the isomerase branch via intramolecular oxidoreductase); LCYB
    is redox-neutral (no net redox change). Wrong branch, over-propagated.
11. GO:0016705 oxidoreductase acting on paired donors, incorporation/reduction of O2
    (IEA InterPro IPR010108) — REMOVE. Monooxygenase-type activity; LCYB does not
    incorporate or reduce molecular oxygen. Not an is_a ancestor of the real function.
12. GO:0016860 intramolecular oxidoreductase activity (IEA ARBA) — MODIFY ->
    GO:0045436. QuickGO confirms GO:0016860 IS a true is_a ancestor of GO:0045436
    (the isomerase branch), so it is correct but uninformatively broad; replace with
    the specific experimentally supported term.
13. GO:0045436 lycopene beta cyclase activity (IBA, PTN001789482, self in WITH/FROM) —
    ACCEPT. Core MF; self-appearance is the expected marker of experimental grounding.
14. GO:0045436 lycopene beta cyclase activity (IDA PMID:19549928) — ACCEPT. Core MF.
15. GO:0045436 lycopene beta cyclase activity (IDA PMID:8837512) — ACCEPT. Core MF.

NEW: GO:1901812 beta-carotene biosynthetic process. LCYB performs the two
beta-cyclizations that form beta-carotene from lycopene — it does the actual chemistry
(participation test passes; it is not merely a substrate/precursor supplier). Direct
support: Cunningham 1996 ("introduces a ring at both ends of lycopene to form the
bicyclic beta-carotene") and UniProt PATHWAY "Carotenoid biosynthesis; beta-carotene
biosynthesis." Comparator: beta-carotene biosynthesis is exactly what a lycopene
beta-cyclase does; this is the defining product term and is not currently annotated.
Verified: GO:1901812 exists, is a descendant of GO:0016117 (per brief).

## Action tally

ACCEPT 8; REMOVE 4; MODIFY 2; KEEP_AS_NON_CORE 1 (= 15 existing reviewed); plus NEW 1.
No UNDECIDED, no PENDING.
ACCEPT = 3x chloroplast, 2x carotenoid biosynthetic process, 3x lycopene beta cyclase activity.

## Evidence caveats

All three primary PMIDs (8837512, 19549928, 21471119) are cached abstract-only
(full_text_available: false). The IDA lycopene-beta-cyclase and carotenoid-biosynthesis
annotations rest on the full-text heterologous E. coli assays; the abstracts state the
beta-carotene-forming activity and the szl1/LCYB mapping directly, so ACCEPT is well
grounded without overruling curators.

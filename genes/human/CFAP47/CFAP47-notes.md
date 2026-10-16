# CFAP47 notes

## Deep research status

Automated deep research was attempted and failed, so no `CFAP47-deep-research-*.md`
file exists for this gene:

- `just deep-research human CFAP47 --provider falcon` failed with
  `Exception: Failed to authenticate` (Edison/Falcon JWT authentication error).
- `just deep-research human CFAP47 --provider perplexity` failed with
  `Provider 'perplexity' not available. Available: falcon, asta, openscientist`.

Notes below come from a manual PubMed search (`CFAP47[Title/Abstract]`, 18 hits,
2021-2026) and the cached publications. Every cited PMID was cached with
`just fetch-pmid` / `just fetch-gene-pmids`.

## Identity

- UniProt Q6ZTR5 (CFA47_HUMAN); X-linked (Xp21.1); very large (canonical isoform 5,
  3,187 aa); UniProt annotates a calponin-homology (CH) domain (1746-1869) and InterPro
  Ig-like folds; the mouse structure (PMID:40473901) resolves a chain of numbered ASH
  domains with the CH domain in the "CFAP47-ring". PANTHER PTHR45912. Highly expressed in testis and present in sperm.
- Disease: X-linked spermatogenic failure 3 (SPGFX3, MIM:301059).

## Structure: core of the central-apparatus bridge

- [PMID:40473901 "CFAP47, the core structural component of the bridge, binds C1 through
  its N-terminal domains, interacts with HYDIN via its central CFAP47-ring, and anchors to
  C2 through its C-terminal region."] (in situ cryo-ET of mouse sperm central apparatus,
  full text).
- Knockout: [PMID:40473901 "In the sperm of Cfap47-knockout (KO) mice, a hollow bridge
  region within the CA structure was observed, correlating with abnormal sperm motility
  and confirming the essential role of CFAP47 in CA function."]

## Human genetics

- MMAF: [PMID:33472045 "we conducted whole-exome sequencing (WES) and identified
  hemizygous missense variants in the X-linked CFAP47 in three unrelated Chinese
  individuals with MMAF."]; an Australian man with a whole-gene Xp21.1 deletion; a
  Cfap47-mutated mouse [PMID:33472045 "the adult males of which were sterile and presented
  with reduced sperm motility and abnormal flagellar morphology and movement."] Abstract
  only (PMC7895902 full text not retrievable through PubMed tools).
- Further MMAF/OAT families: PMID:37424856 (p.V472M; head, mitochondrial sheath and
  annulus defects; co-IP with SEPTIN4, CFAP65, CFAP69) and PMID:36571501 (abstract only;
  CFAP47 interacts with WDR87 in the midpiece).
- Airway: [PMID:37723893 "Two hemizygous missense variants of X-linked CFAP47 in two
  unrelated PCD individuals were identified."] Respiratory cilia were short and fewer but
  the 9+2 structure was intact; the PCD association rests on two patients.
- Kidney (weaker): [PMID:39698362 "CFAP47 was expressed in primary cilia of human kidney
  tubules"]; proposed X-linked PKD gene from three sporadic male patients.

## Localization by immunofluorescence

- Two IF studies place a CFAP47 signal at the sperm head-tail junction:
  GOA IDA from PMID:33472045 (head-tail coupling apparatus; abstract only) and
  [PMID:37723893 "Immunofluorescence analysis showed CFAP47 is located to junction of head
  and flagellum in sperm of control but absent in sperm of P1."]
- This contrasts with its structural position along the central apparatus of the whole
  axoneme (PMID:40473901). A neck pool or epitope accessibility could explain the IF.

## Annotation decisions (summary)

- sperm axoneme assembly (IBA, IMP) -> ACCEPT (structural core of CA bridge; KO hollow
  bridge).
- cilium assembly (IBA) -> TOO_GENERAL (entailed by sperm axoneme assembly).
- cilium (IBA) -> TOO_GENERAL, entailed by NEW axonemal central apparatus.
- NEW: axonemal central apparatus (GO:1990716). Comparator check: HYDIN (its bridge
  partner), SPAG16, SPAG17, CFAP65 and MYCBPAP carry GO:1990716 in human GOA.
- protein binding x3 (BioPlex UBB x2; CFAP65) -> REMOVE (uninformative).
- sperm head-tail coupling apparatus (IDA) -> KEEP_AS_NON_CORE.

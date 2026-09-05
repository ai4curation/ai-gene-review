# USH1C / harmonin (Q9Y6N9) — research notes

Reviewer journal for the annotation review (2026-09-04). Provenance is inline as
[PMID:NNN "quote"].

## Identity and architecture

- USH1C encodes harmonin, historically also called PDZ-73, AIE-75, NY-CO-38/37 and
  NY-REN-3. It was identified as the USH1C disease gene in 2000
  [PMID:10973247 "We identified this gene (USH1C), encoding a PDZ-domain-containing
  protein, harmonin, in a subtracted mouse cDNA library derived from inner ear
  sensory areas."].
- Alternative splicing yields isoform classes a, b and c; the long b isoforms add a
  second coiled-coil and a PST (proline/serine/threonine-rich) actin-binding region
  [PMID:10973247 "The inner ear Ush1c transcripts predicted several harmonin
  isoforms, some containing an additional coiled-coil domain and a proline- and
  serine-rich region."]. The b isoforms are hair-bundle enriched; retinal expression
  is dominated by harmonin-a1 (Nagel-Wolfrum 2023, via deep research; not cached).
- Harmonin is not an enzyme/transporter/channel; it is a multivalent PDZ scaffold.
  The N-domain (HHD) plus PDZ1 form a supramodule
  [PMID:20142502 "We demonstrate that the N-terminal domain and the first PDZ domain
  of harmonin are tethered by a small-domain C-terminal to PDZ1 to form a structural
  and functional supramodule responsible for binding to Sans."].

## Hair-cell function (core)

- USH1C loss in humans causes congenital profound deafness, vestibular dysfunction
  and progressive retinitis pigmentosa
  [PMID:10973247 "Usher syndrome type 1 (USH1) is an autosomal recessive sensory
  defect involving congenital profound sensorineural deafness, vestibular dysfunction
  and blindness (due to progressive retinitis pigmentosa)"]. Some alleles cause
  nonsyndromic deafness DFNB18 [PMID:10973247 "we propose that USH1C also underlies
  the DFNB18 form of isolated deafness"].
- In the mouse inner ear, expression is hair-cell specific
  [PMID:10973247 "We showed that, in the mouse inner ear, only the sensory hair
  cells express harmonin."].
- Harmonin belongs to BOTH hair-cell scaffolding complexes:
  1. The upper tip-link density (UTLD) of mature stereocilia, with MYO7A and
     SANS/USH1G, anchoring CDH23 at the upper tip-link insertion (tension-bearing).
     Deep research: "Harmonin-b is concentrated at the **upper tip-link density** of
     stereocilia... There it forms part of a CDH23–harmonin–SANS–MYO7A assembly that
     anchors mechanically loaded tip links to the actin core."
  2. The transient ankle-link/USH2 complex of developing bundles (USH2A, ADGRV1,
     whirlin, PDZD7). Deep research: "Harmonin PDZ1 recognizes C-terminal motifs in
     usherin/USH2A and ADGRV1, providing a physical bridge between USH1 and USH2
     networks." (Reiners 2005, PMID not cached here.)
- The harmonin–SANS complex is exceptionally stable and destabilized by USH1
  patient mutations [PMID:20142502 "the synergistic PDZ1/SAM and PDZ1/carboxyl PDZ
  binding-motif interactions, between harmonin and Sans, lock the two scaffold
  proteins into a highly stable complex" ... "Mutations in harmonin and Sans found
  in USH1 patients are shown to destabilize the complex formation of the two
  proteins."].

## Intestinal brush border function (core)

- Harmonin is the shared scaffold between the Usher complex and the enterocyte
  intermicrovillar adhesion complex (IMAC: CDHR2, CDHR5, USH1C, ANKS4B, MYO7B)
  [PMID:32209652 "Importantly, the USH1C scaffold is shared genetically between the
  IMAC and Usher complex, although different splice isoforms are utilized between
  these two complexes"].
- It binds protocadherin tails and promotes their tip targeting
  [PMID:24725409 "The cytoplasmic domains of microvillar protocadherins interact
  with the scaffolding protein, harmonin, and myosin-7b, which promote localization
  to microvillar tips."]; harmonin-null mice have severe brush border defects
  [PMID:24725409 "a mouse model of Usher syndrome lacking harmonin exhibits
  microvillar protocadherin mislocalization and severe defects in brush border
  morphology"]. This explains the enteropathy seen in some USH1C patients
  [PMID:32209652 "some patients with mutations in the scaffold USH1C also present
  with severe inflammatory enteropathy and nephropathy"].
- USH1C sits at the top of the IMAC assembly hierarchy
  [PMID:26812018 "However, a tripartite complex only forms if ANKS4B and MYO7B are
  first activated by USH1C."].
- Earlier support: brush border proteome + CACO-2 immunostaining
  [PMID:21330445 "All three probes produced striking punctate staining at the apical
  surface, representative of microvillar labeling"]; apical enrichment in intestinal
  epithelium was already seen in 1999
  [PMID:10209257 "a prominent apical staining pattern in cells of the small
  intestine"].
- Direct tip localization [PMID:32209652 "Confocal imaging of rat BBs stained for
  USH1C revealed marked enrichment of this scaffold at the distal tips of
  microvilli, the normal site of IMAC function"].

## Retina (genuine, secondary emphasis)

- USH1C patients develop retinitis pigmentosa (above). Harmonin protein detected in
  human rod outer segments, cone pedicles, Mueller glia endfeet/microvilli, and OLM
  junctions; harmonin-a1 is the dominant retinal transcript (Nagel-Wolfrum 2023 via
  deep research; not in cached publications).
- Spectrin betaV association along the photoreceptor trafficking route
  [PMID:23704327 "We showed that spectrin βV also associates with two USH1 proteins,
  sans (USH1G) and harmonin (USH1C)."].

## Curation judgments of note

- PMID:11398101 (PCDH15/USH1F paper) is cited for three USH1C IMP annotations
  (GO:0007605, GO:0050953, GO:0045494). Full text contains no USH1C data — USH1C
  appears once, in the intro list of cloned USH1 genes. The terms themselves are
  clearly correct for USH1C (patient phenotype per PMID:10973247), so the
  annotations were ACCEPTed with the citation flagged as MISCITED in
  reference_review, rather than removed.
- PMID:15219944 (AIE-75 overexpression induces G2/M arrest in SW480 cells):
  recommended REMOVE for GO:0000086 "G2/M transition of mitotic cell cycle". The
  assay is ectopic overexpression in a cancer line lacking endogenous harmonin, the
  phenotype is arrest (not participation in the transition), and no subsequent
  literature supports a physiological cell-cycle role.
- GO:0050885 "neuromuscular process controlling balance" (ARBA IEA): the balance
  defect is vestibular-sensory, not neuromuscular; proposed MODIFY to GO:0050957
  equilibrioception (already annotated IMP from PMID:10973247).
- Bare GO:0005515 protein binding lines: MODIFY to GO:0030674
  protein-macromolecule adaptor activity for the three mechanistically informative
  papers (PMID:20142502 SANS; PMID:24725409 CDHR2/CDHR5/MYO7B; PMID:26812018
  ANKS4B/MYO7B); MARK_AS_OVER_ANNOTATED for the high-throughput interactome /
  fragmentomics lines (PMID:25416956, 25502805, 27173435, 28514442, 29997244,
  31515488, 32814053, 33961781, 36115835) and the isolated Y2H partners
  (PMID:11311560 MCC2; PMID:16464467 DOCK4).
- GO:0005929 cilium (IBA): stereocilia are actin-based protrusions, not cilia; kept
  as NON_CORE on the strength of photoreceptor ciliary-region reports and the
  patient-fibroblast primary-cilium rescue (deep research).
- Isoform note: GOA carries no isoform-specific or negated (NOT) annotation lines
  for USH1C, although the biology is isoform-structured (b isoforms in hair
  bundles, a1 in retina; UniProt records complex-specific isoform usage between the
  Usher complex and the IMAC).

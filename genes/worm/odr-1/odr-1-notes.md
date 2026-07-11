# odr-1 (gcy-10) research notes — C. elegans

UniProt: **B1Q257** (GCY10_CAEEL). WormBase: WBGene00003848 / R01E6.1.
Gene symbol **odr-1** (Odorant response abnormal), synonym **gcy-10**.
EC 4.6.1.2 (guanylate cyclase). Reference proteome protein B1Q257.

## Identity / architecture (from UniProt B1Q257)

odr-1 encodes a **receptor-type (transmembrane) guanylyl cyclase**. Domain layout
(1067 aa, isoform b):
- Signal peptide 1–20; extracellular domain 21–438 (periplasmic-binding-protein-like
  ligand-binding fold, InterPro IPR028082 / SSF53822).
- Single-pass type I transmembrane helix 439–459.
- Cytoplasmic 460–1067, containing:
  - **Protein-kinase-like (KHD) domain 509–791** — annotated by UniProt as *predicted
    catalytically inactive*: "The protein kinase domain is predicted to be catalytically
    inactive." (ECO:0000255|PROSITE-ProRule:PRU00159). This is the canonical
    pseudokinase/kinase-homology domain of receptor guanylyl cyclases.
  - **Guanylate cyclase (catalytic) domain 859–989** (Pfam PF00211, PROSITE PS50125).
- N-glycosylation site (Asn411); glycoprotein.

Family: adenylyl cyclase class-4 / guanylyl cyclase family; PANTHER PTHR11920
(GUANYLYL CYCLASE), subfamily PTHR11920:SF355 (RECEPTOR-TYPE GUANYLATE CYCLASE
GCY-10-RELATED). C. elegans has ~27 receptor-type + 7 soluble GCs
[PMID:23874221 "27 receptor-type GCYs and 7 soluble GCYs are encoded by the C. elegans genome"].

Catalytic activity (UniProt, EC 4.6.1.2): GTP = 3',5'-cyclic GMP + diphosphate
(Rhea:RHEA:13665). The specific EC/cyclase activity for odr-1 is by-similarity
(ECO:0000250|UniProtKB:Q19187 = gcy-12); there is no direct in-vitro enzymology on
purified ODR-1.

## Subcellular location / expression

- **Cell membrane / cilium.** UniProt: "Cell membrane ... Single-pass type I membrane
  protein. Cell projection, cilium ... Localizes in cilium of sensory neurons"
  (ECO:0000269|PMID:10774726). GOA: non-motile cilium (GO:0097730, IDA, PMID:10774726,
  WormBase).
- **Tissue specificity:** "Expressed predominantly in AWC but also in AWB, ASI, ASJ and
  ASK sensory neurons and in I1 interneuron" (UniProt; PMID:10774726, PMID:9096403).
  PMID:20436480 corroborates AWB/ASJ/ASK expression: "two membrane-associated GCs
  (daf-11 and odr-1) are expressed in C. elegans photoreceptor cells, including ASJ, ASK
  and AWB".

## KNOWN functions (well supported)

### Molecular function: guanylate cyclase (cGMP synthesis)
- ODR-1 is a transmembrane guanylyl cyclase producing the second messenger cGMP. The
  cyclase identity is established by domain architecture and by the point mutant E904A
  in the cyclase domain: UniProt MUTAGEN 904 "E->A: Probable loss of cyclase activity.
  Loss of chemotaxis to some volatile odorants." (PMID:10774726). Note: activity is
  inferred (ISS/by-similarity), not measured on purified protein.
- Overexpression phenotype implicates cGMP overproduction:
  [PMID:10774726 "Olfactory discrimination is also disrupted by ODR-1 overexpression,
  probably by overproduction of the shared second messenger cGMP."]

### Biological process: olfaction / chemosensation (core)
- ODR-1 is essential for AWC-mediated olfaction and required for responses to all
  AWC-sensed odorants:
  [PMID:10774726 "We demonstrate that the transmembrane guanylyl cyclase ODR-1 is
  essential for responses to all AWC-sensed odorants. ODR-1 appears to be a shared
  signaling component downstream of odorant receptors."]
- odr-1 was originally isolated as an *odr* (odorant-response-abnormal) gene in the
  founding olfaction screen: [PMID:8348618 "Chemotaxis to subsets of volatile odorants
  is disrupted by mutations in the odr genes, which might be involved in odorant
  sensation or signal transduction."]. Mutagenesis G647D (in n1930): "loss of chemotaxis
  to volatile odorants" (UniProt, PMID:8348618).
- Acts in both attractive (AWC) and repulsive (AWB) odor pathways (UniProt FUNCTION,
  PMID:10774726, PMID:8348618): "Regulates chemotaxis responses toward volatile odorants
  in AWC sensory neurons and their avoidance in AWB sensory neurons."
- Role in odor discrimination and adaptation (overexpression disrupts both;
  PMID:10774726).

### Phototransduction (ASJ) — non-image light sensing
- [PMID:20436480 "odr-1(n1936) mutant worms also showed a severe reduction in the
  density of photocurrents ... These results demonstrate that membrane-associated GCs
  are required for phototransduction in ASJ."] Model: LITE-1 → Gi/o (goa-1/gpa-3) →
  membrane GCs (daf-11, odr-1) → cGMP → CNG channel (tax-2/tax-4). This is the same
  cGMP→TAX-2/TAX-4 architecture as chemosensation, redeployed for light.

### cGMP supply to EGL-4 (PKG) for bitter/quinine (nociceptive) sensitivity
- [PMID:23874221 "Loss-of-function mutations in the guanylyl cyclase genes odr-1,
  gcy-27, gcy-33 and gcy-34 resulted in behavioral hypersensitivity to dilute (1 mM)
  quinine"] and the model that these GCs "function in a non-cell-autonomous manner to
  provide cGMP to regulate EGL-4 function in ASH" (odr-1 is not expressed in ASH).
  odr-1(lof) quinine hypersensitivity was rescued by srb-6p::odr-1 but not osm-10p::odr-1
  [PMID:23874221 "The quinine hypersensitivity of odr-1(lof) animals was rescued by
  srb-6p::odr-1 expression (p<0.001), but not osm-10p::odr-1 expression (p>0.5)."].
  → supports GO:0050913 (sensory perception of bitter taste) and GO:0007635
  (chemosensory behavior).

### Maintenance of asymmetric str-2 (olfactory receptor) expression in AWC
- [PMID:10571181 "A cGMP signaling pathway that is used in olfaction maintains str-2
  expression after the initial decision has been made."] odr-1 provides the cGMP;
  UniProt FUNCTION: "Required to maintain the expression of putative olfactory receptor
  str-2 in AWC neurons in adults (PubMed:10571181)." → supports GO:0010628 (positive
  regulation of gene expression), qualifier involved_in (WormBase, PMID:10571181).

### AWB cilia membrane morphogenesis (developmental / non-cell-autonomous readout)
- In the Tubby paper, odr-1 is used as a "receptor guanylyl cyclase signaling mutant"
  whose reduced sensory signaling drives ciliary phenotypes:
  [PMID:31259686 "AWB cilia width is significantly increased in odr-1 receptor guanylyl
  cyclase signaling mutants"], [PMID:31259686 "we found that odr-1 mutants showed
  enrichment of a TUB-1 fusion protein in AWB cilia as compared to levels at the PCMC"],
  [PMID:31259686 "In odr-1 mutants, we observed significantly increased relative levels
  of GFP::PPK-1 in AWB cilia"]. This is the basis of the GOA IMP annotations
  GO:0097499 (protein localization to non-motile cilium) and GO:0050767 (regulation of
  neurogenesis) attributed to PMID:31259686. These are downstream/developmental
  consequences of loss of odr-1 sensory-signaling, not a distinct biochemical activity of
  ODR-1; they are best treated as non-core.

## Additional / peripheral GOA annotations reviewed

- **GO:0010628 positive regulation of gene expression, acts_upstream_of, IMP,
  PMID:18832350.** The cached abstract of PMID:18832350 is about EGL-4/KIN-29/PKA
  regulating chemoreceptor (CR) gene expression and does not name odr-1; full text
  unavailable. Consistent with odr-1 supplying cGMP upstream of EGL-4, but odr-1's
  specific role here cannot be verified from the abstract → treat cautiously
  (non-core / UNDECIDED-leaning; keep, defer to curator, flag reference).
- **GO:0040015 / GO:0040014 regulation of multicellular organism growth (body size),
  IGI, PMID:26434723.** The abstract of PMID:26434723 explicitly assigns body-size
  control to **gcy-12** ("gcy-12 ... provide cGMP to the EGL-4 ... only for limited tasks
  including body size regulation") and states EGL-4 partners with different GCs for
  different functions. odr-1 is not named in the abstract; the annotation is an IGI
  (WITH gcy-12 = Q19187 and G5EGF0). Body-size regulation is clearly peripheral to odr-1
  and, per the paper's own model, is a gcy-12 task → non-core; keep (do not REMOVE an
  experimental IGI on abstract-only grounds), mark non-core, flag reference relevance LOW.
- **GO:0001653 peptide receptor activity (IBA, GO_REF:0000033).** This is a phylogenetic
  (PANTHER) inference from natriuretic-peptide-receptor GCs (mammalian NPR-A/NPR-B,
  UniProtKB:P16066/P20594). C. elegans receptor GCs are orphan receptors with no
  demonstrated peptide ligand; odr-1's extracellular domain is explicitly NOT implicated
  in odorant detection [UniProt DOMAIN "The extracellular domain may not be directly
  implicated in the detection of volatile odorants."]. "peptide receptor activity" is an
  over-annotation for odr-1 (no known peptide ligand) → MARK_AS_OVER_ANNOTATED / non-core.
- **GO:0004672 protein kinase activity (IEA, InterPro)** — NOTE: present in the UniProt DR
  block but NOT in the GOA TSV/seeded review (so not in existing_annotations). UniProt
  explicitly states the kinase (KHD) domain is *predicted catalytically inactive*; a
  protein-kinase-activity annotation would be a pseudokinase over-annotation. Documented
  here for completeness / knowledge_gaps.
- **GO:0005524 ATP binding (IEA, InterPro:IPR000719).** From the kinase-homology domain.
  UniProt lists ATP-binding residues (515–523, 534). Plausible structural nucleotide
  binding but the domain is a pseudokinase; keep as non-core (weak, IEA).
- **GO:0009190 cyclic nucleotide biosynthetic process / GO:0035556 intracellular signal
  transduction (IEA, InterPro).** Generic parents of the specific, well-supported
  cGMP-biosynthesis / receptor-GC-signaling terms; keep as non-core (redundant with the
  specific experimental terms).

## NOT known / knowledge gaps (explicit)

1. **Activating ligand / stimulus for ODR-1 is unknown.** No peptide or small-molecule
   ligand has been identified for the extracellular domain, and UniProt states the
   extracellular domain "may not be directly implicated in the detection of volatile
   odorants" [PMID:10774726]. ODR-1 acts *downstream* of odorant receptors as a shared
   signaling component [PMID:10774726 "ODR-1 appears to be a shared signaling component
   downstream of odorant receptors."], so what activates/regulates its cyclase output in
   vivo (Ca2+, phosphorylation, GPCR/G-protein input, an orphan-receptor ligand) is
   undetermined.
2. **Direct catalytic activity of ODR-1 has never been measured biochemically.** The
   cyclase activity is inferred (ISS from gcy-12/Q19187 and mammalian NPRs) and from the
   E904A "probable loss of cyclase activity" phenotype [PMID:10774726]; purified-protein
   enzymology is lacking. Whether ODR-1 homodimerizes or must heterodimerize with another
   GC (e.g. daf-11) to form an active catalytic unit is unresolved.
3. **The kinase-homology domain: regulatory pseudokinase vs. active kinase.** UniProt
   predicts it catalytically inactive (PRU00159). Whether it has any residual catalytic
   activity, and its regulatory role, are untested. (In this sense odr-1 is a candidate
   pseudokinase-containing, possibly regulatory-cyclase protein.)
4. Cell-autonomous vs non-cell-autonomous scope: for quinine/EGL-4, ODR-1 acts
   non-cell-autonomously to supply cGMP to ASH [PMID:23874221]; the diffusible-signal
   mechanism is not defined.

## Core function synthesis (for core_functions)

1. **Molecular function:** guanylate cyclase activity (GO:0004383) producing cGMP from
   GTP — the catalytic identity of the protein. Location: ciliary membrane / plasma
   membrane of sensory neurons.
2. **cGMP biosynthetic process (GO:0006182) / receptor guanylyl cyclase signaling
   pathway (GO:0007168):** generation of the cGMP second messenger that gates the
   TAX-2/TAX-4 CNG channel.
3. **Sensory perception / olfaction (GO:0042048 olfactory behavior; sensory perception
   of smell):** the organismal role — required for AWC/AWB olfaction and odor
   discrimination.
4. Cellular location: **non-motile cilium (GO:0097730) / ciliary membrane** —
   experimentally localized (IDA, PMID:10774726).

Non-core (pleiotropic / downstream / genetic-tool readouts): phototransduction, bitter
taste/quinine (via EGL-4), body-size regulation (gcy-12-attributed), AWB cilia membrane
morphogenesis, str-2 maintenance, chemoreceptor-gene expression.

## Deep research

Falcon deep-research launched (`just deep-research-falcon worm odr-1 --fallback
perplexity-lite`). If it completes, its file is `odr-1-deep-research-*.md`. Review below
is grounded in primary cached literature (PMIDs above) and UniProt B1Q257, independent of
the deep-research summary.

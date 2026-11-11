# mpz-1 (C52A11.4; UniProt G5ECZ8) -- manual literature research

No deep-research provider was available for this review. This summary was
compiled by hand from the cached publications (`publications/PMID_*.md`) and a
PubMed search for "mpz-1 elegans" (six hits: PMID:16890216, PMID:20207731,
PMID:22363657, PMID:30417267, PMID:35247383, PMID:40472775). The PDZ
interactome screen PMID:21110867 was added from the GOA file.

## Identity and domain architecture

- MPZ-1 (Multiple PDZ domain protein 1) is a 2,422-residue (canonical isoform
  C52A11.4d) scaffold with ten PDZ domains (PROSITE PS50106, Pfam PF00595) and
  long disordered linkers (MobiDB-lite); no transmembrane segment, signal
  peptide or catalytic domain is annotated (`mpz-1-uniprot.txt`).
- PANTHER places it in PTHR19964 (multiple PDZ domain protein), subfamily
  SF92 "PATJ homolog"; CDD hits are to MUPP1/PATJ PDZ-domain models.
- It is described as closely related to the mammalian scaffold MUPP1
  [PMID:22363657 "MPZ-1 is closely related to the mammalian PDZ domain scaffold
  protein MUPP1"] and as a candidate PATJ ortholog [PMID:35247383 "We also
  identified MPZ-1 as a candidate ortholog of PATJ based on the physical
  interaction with MAGU-2 and sequence similarity with PATJ proteins."]. The
  N-terminal L27 domain of PATJ/MUPP1 is not evident in MPZ-1 (PMID:35247383).
- The locus is complex: "at least ten predicted splice variants and seven
  different promoter regions" [PMID:35247383].

## Expression and localization

- Expressed in ~60 neurons and in body wall and vulval muscles; in neurons
  GFP-tagged MPZ-1 is punctate and colocalizes with synaptobrevin
  [PMID:16890216 "In neurons, GFP-tagged MPZ-1 is punctate and colocalizes with
  the synaptic marker, synaptobrevin."].
- MPZ-1::tagRFP is strongest in nerve-ring axons, where it co-localizes with
  RHGF-2::GFP [PMID:22363657 "MPZ-1::tagRFP was most strongly localized to the
  axons of the nerve ring where RHGF-2::GFP was also highly distributed"].
- An endogenous GFP knock-in (mib188) labels nervous system, excretory canal
  and spermatheca but not most epithelia [PMID:35247383 "we did not observe
  expression in epithelial tissues, apart from the spermatheca and excretory
  canal"].
- MPZ-1::GFP in head neurons increases under hypoxia but not heat stress
  (PMID:40472775; expression-only observation in a PATJ stroke paper).

## Binding partners (PDZ-ligand interactions)

| Partner | Binding site on MPZ-1 | Assay | Reference |
|---|---|---|---|
| SER-1 (5-HT2-like serotonin GPCR), C-terminal ETFL | PDZ10 | GST pull-down, co-IP | PMID:16890216 |
| other GPCRs with acidic -3 residue | n.d. | binding | PMID:16890216 |
| RHGF-2 (RhoGEF, PLEKHG5/Tech homolog), C-terminal SDV | PDZ8 > PDZ9, 10 | Y2H, GST pull-down, co-IP, co-localization | PMID:22363657 |
| ARR-1 (arrestin), C-terminal PDZ ligand | n.d. in abstract | direct binding; complex with DAF-18/PTEN | PMID:20207731 |
| MGL-1 (mGluR) | n.d. | Y2H | PMID:30417267 |
| MAGU-2 (PALS1 ortholog) | full-length | MS pull-down, Y2H | PMID:35247383 |
| NRX-1 and others (eri-12, C39D10.7, R06F6.12) | PDZ9 | Y2H PDZ-array | PMID:21110867 |

RHGF-2 is a Rho guanine-nucleotide exchange factor, not a GTPase-activating
protein [PMID:22363657 "RHGF-2 GEF activity is specific to RHO-1, the C.
elegans RhoA homolog"].

## Functional (genetic) data

- Serotonin-stimulated egg laying: "mpz-1 RNAi reduces 5-HT stimulated
  egg-laying in wild type animals and in ser-1 mutants rescued by muscle
  expression of SER-1", but not when SER-1 lacks its PDZ ligand; PDZ10
  overexpression is dominant-negative [PMID:16890216]. Authors' conclusion:
  "the SER-1/MPZ-1 interaction facilitates SER-1 mediated signaling."
- Insulin/IGF (DAF-2) signalling and lifespan: ARR-1 positively regulates DAF-2
  signalling "via direct interaction with MPZ-1"; ARR-1 and MPZ-1 are "found in
  a complex with" DAF-18/PTEN [PMID:20207731]. Complex Portal CPX-3881
  ("arr-1-mpz-1-daf-18 complex") states that complex formation probably
  inhibits DAF-18 phosphatase activity (inferred by Complex Portal from the
  full text, which was not available in this session).
- mGluR signalling: mpz-1 deletion mutants respond largely normally to the
  mGluR agonist L-CCG-I in a pharyngeal assay [PMID:30417267], so MPZ-1 is not
  obligatory for MGL-1 signalling there.
- Crumbs complex: MPZ-1 binds MAGU-2/PALS1 but, given its restricted
  expression, is "not likely a core component of the C. elegans Crumbs complex"
  [PMID:35247383].

## Synthesis

MPZ-1 is a neuronal and muscle multi-PDZ scaffold of the MUPP1/PATJ family
that binds the C-terminal PDZ ligands of GPCRs (SER-1, MGL-1), a RhoGEF
(RHGF-2) and arrestin (ARR-1), and is found at synapses and in nerve-ring
axons. Functional evidence links it to facilitating SER-1 signalling in vulval
muscle and to positive regulation of DAF-2 insulin-like signalling via an
ARR-1/MPZ-1/DAF-18 complex. No enzymatic activity is expected.

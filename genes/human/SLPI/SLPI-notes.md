# SLPI (secretory leukocyte protease inhibitor) — curation notes

UniProt: P03973 (ANTIL / antileukoproteinase; synonyms HUSI-I, MPI, BLPI, WFDC4, WAP4).

## Deep research status

- **Update 2026-10-05:** the falcon job did complete late (report end time
  2026-10-05T01:25) and `SLPI-deep-research-falcon.md` now exists; see the
  reconciliation section at the end of this file. Original status note:
- `just deep-research-falcon human SLPI` was launched at the start of this review
  (no perplexity key available, so no fallback). At the time the review was written
  the falcon job had not yet returned (other concurrent falcon jobs in this session
  were hitting Edison API `429 Too Many Requests`). The review below is therefore
  based on the UniProt record, cached publications for GOA references, and
  additional primary papers retrieved via PubMed and cached with `just fetch-pmid`.

## Protein / structure

- 132 aa precursor; signal peptide 1-25; mature chain 26-132 (107 residues), two
  WAP (whey acidic protein / four-disulfide core) domains (UniProt features).
- Two homologous domains, 16 cysteines [PMID:3485543 "The molecule comprises two
  consecutive domains which are homologous to each other"].
- Crystal structure with chymotrypsin: boomerang shape; reactive-site loop of the
  second (C-terminal) domain carries the scissile Leu72-Met73 bond (mature numbering)
  [PMID:3366116 "The reactive site loop of the second domain has elastase and
  chymotrypsin binding properties."].
- Complex with HNE: 1/2SLPI (C-terminal domain) is sufficient to inhibit neutrophil
  elastase [PMID:18421166 "P1 Leu72i and six hydrogen bonds between the main chains
  in the primary contact region have sufficient ability to inhibit HNE and PPE"].

## Core molecular function: canonical (Laskowski-type) serine protease inhibitor

- Purified from parotid secretions; potent inhibitor of leukocyte elastase,
  cathepsin G and trypsin [PMID:3462719 "A potent inhibitor of human leukocyte
  elastase (EC 3.4.21.37) and cathepsin G (EC 3.4.21.20) and of human trypsin
  (EC 3.4.21.4) has been purified from human parotid secretions."].
- Physiological role: protection of mucosal tissue from neutrophil elastase
  [PMID:3462719 "suggesting a functional role for the protein in preventing
  elastase-mediated damage to oral and possibly other mucosal tissues"].
- UniProt: "Acid-stable proteinase inhibitor with strong affinities for trypsin,
  chymotrypsin, elastase, and cathepsin G".
- Elastase-specific inhibitor (elafin, PI3) is a WAP-family paralog; the 2039600
  paper compares ESI with MPI (=SLPI) isolated from sputum.

## Location

- Secreted into mucosal fluids: saliva/parotid secretion (3462719), seminal plasma
  and cervix (3485543), bronchial sputum (2039600), plasma and myeloid cells
  (24352879). Also found in neutrophil specific granules (Reactome R-HSA-6798749).
- Can enter monocytes and localise to cytoplasm and nucleus [PMID:16352738 "SLPI
  enters the cells, becoming rapidly localized to the cytoplasm and nucleus"].

## Anti-inflammatory / NF-kB

- Mouse: LPS-induced macrophage product that suppresses LPS-induced NF-kB
  activation [PMID:9039268 "Transfection of macrophages with SLPI suppressed
  LPS-induced activation of NF-kappa B and production of nitric oxide and TNF
  alpha."].
- Human monocytes: nuclear SLPI binds NF-kB consensus sites and competes with p65
  [PMID:16352738 "SLPI inhibition of NF-kappaB activation is mediated, in part, by
  competitive binding to the NF-kappaB consensus-binding site."]. This provides
  some (sequence-site-specific) support for DNA binding beyond the nonspecific
  charge-driven binding seen in E. coli (PMID:2467900).

## Antimicrobial

- Antibacterial against E. coli and S. aureus; N-terminal domain carries most of it
  [PMID:8890201 "ALP was shown to display marked in vitro antibacterial activity
  against Escherichia coli and Staphylococcus aureus."].
- Skin: antimicrobial against P. aeruginosa, S. aureus, S. epidermidis, C. albicans
  [PMID:9704025].
- Seminal plasma: SLPI identified in zones of clearance in gel overlay assays but its
  contribution is minor relative to semenogelin peptides [PMID:18714013 "the
  contribution of these (poly)peptides to the bactericidal activity was minor"].
- E. coli toxicity paper (PMID:2467900): intracellular high-level expression of the
  basic SLPI in E. coli is toxic because it binds mRNA/DNA via charge interactions;
  lysozyme behaves similarly — authors conclude this is a general problem of basic
  recombinant proteins. This is not good evidence for a physiological nucleic-acid
  binding function or host-mediated perturbation of the symbiont.

## Antiviral (HIV-1)

- Saliva factor inhibiting HIV-1 infection of monocytes; acts on host cell
  [PMID:7615818 "SLPI appears to target a host cell-associated molecule"].
- Blocks infection after virus binding, before reverse transcription; independent
  of antiprotease activity [PMID:9242546].
- PLSCR1 and PLSCR4 bind SLPI; SLPI disrupts PLSCR1-CD4 association
  [PMID:19333378]. GOA term "negative regulation of viral genome replication" is a
  poor fit: the block is at entry; better is GO:0046597 host-mediated suppression
  of symbiont invasion (formerly "negative regulation of viral entry into host
  cell").

## Wound healing / tissue protection

- Slpi-null mice: impaired cutaneous wound healing with increased inflammation and
  elastase activity [PMID:11017147].
- Mechanism: SLPI binds proepithelin (progranulin, GRN) and prevents elastase from
  converting it to epithelins [PMID:12526812 "SLPI and PEPI form complexes,
  preventing elastase from converting PEPI to EPIs."].

## Myelopoiesis

- Reduced SLPI in congenital neutropenia; SLPI knockdown in CD34+ progenitors
  impairs myeloid differentiation [PMID:24352879]. Likely indirect/pleiotropic.

## Interactome (HT Y2H)
- SLPI binds progranulin (GRN, P28799) protecting it from elastase [PMID:12526812].
- Phospholipid scramblases PLSCR1 (O15162) and PLSCR4 (Q9NRQ2) are SLPI receptors
  implicated in anti-HIV activity [PMID:19333378].
- Large set of binary Y2H hits (CALN1, CIB3, EFEMP1, FAM9B, HOXA1, LAT, MKRN3,
  NBL1, NTAQ1, PIH1D2, SGTA, SGTB, SMIM14, UBQLN1, UBQLN2) from systematic
  interactome maps [PMID:25416956, PMID:32296183]; these are generic, mostly
  functionally uninterpreted "protein binding" annotations.

## Reference caveats

- PMID:2467900: E. coli recombinant-expression artifact (charge-driven nucleic
  acid binding), not a physiological DNA/mRNA binding function. GOA uses it for
  DNA binding, mRNA binding and host-mediated perturbation of symbiont process.
- PMID:16352738 (not in GOA) is the better support for any sequence-specific
  nuclear DNA/NF-kB binding.

## Reconciliation with late falcon deep research (2026-10-05)

`SLPI-deep-research-falcon.md` arrived after the review was written and was read in full and
compared with the review and these notes.

- **No contradictions.** Its evidence-weighted conclusion - SLPI is chiefly a secreted
  C-terminal-WAP-domain serine protease inhibitor protecting mucosal extracellular environments
  from neutrophil elastase and cathepsin G, with context-dependent nuclear NF-kB-site competition
  and antimicrobial host defence - matches the review's core functions and actions.
- **Agrees with existing caveats:** it explicitly warns against annotating SLPI as an enzyme or as
  a direct PR3 or MMP-9 inhibitor (PR3 cleaves SLPI; no such GOA rows exist), and treats
  anti-HIV activity as variable/secondary, consistent with the review's handling of GO:0045071.
- **Additional material, not acted on:** Eisenberg et al. 1990 (JBC) Leu72 site-directed
  mutagenesis (reinforces the P1 Leu72 assignment already supported by PMID:3366116 and
  PMID:18421166); Weldon et al. 2009 NE cleavage of SLPI at Ser15-Ala16/Ala16-Glu17 in CF
  airways, removing LPS and NF-kB-site binding while retaining cathepsin G inhibition (a
  regulation-of-SLPI finding, not a new SLPI activity); Brown et al. 2024 Slpi-null x ENaC-Tg mouse
  airway phenotype (indirect); clinical registry entries. None of these was independently
  fetched, since none changes an annotation.
- Actions: added the falcon report to `references` (reference_review UNVERIFIED). No annotation
  actions changed; review status already COMPLETE.

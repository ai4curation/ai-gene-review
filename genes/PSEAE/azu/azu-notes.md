# azu (PA4922, P00282) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE P00282 --alias azu`; accession matches the worklist.
Reviewed (Swiss-Prot) entry. No deep-research provider; PubMed eutils and Europe PMC searches
failed during the session (HTTP 500/503). Literature from the cached papers and a web search
for the physiological role of azurin.

### Literature

- PMID:14758526 (Marks et al. 2004), abstract only: [PMID:14758526 "Pseudomonas aeruginosa
  azurin binds copper so tightly that it remains bound even upon polypeptide unfolding."];
  ITC and spectroscopy on WT and Met121Ala azurin and on model peptides give Cu(II), Cu(I)
  and Zn affinities; [PMID:14758526 "Copper can be substituted with zinc without change in
  protein structure"].
- PMID:19299503 (Sato et al. 2009), abstract only: loop-engineering of the Cu site;
  [PMID:19299503 "Cupredoxins function as redox shuttles and are required to be monomeric"];
  one loop mutant forms a strand-swapped dimer in the crystal.
- PMID:21352498 (Alagaratnam et al. 2011), abstract only: H117G variant, flash-photolysis
  reduction kinetics, crystal structure 3N2J. The abstract does not mention self-association.
- PMID:23911566 (Panzner et al. 2013), abstract only: Ag(I) binds apo-azurin at the copper
  site, the silver adduct is redox inert.
- PMID:31790504 (Han et al. 2019), full text: azurin is secreted by the H2-T6SS and binds the
  TonB-dependent receptor OprC for copper uptake [PMID:31790504 "Secreted Azu acquires
  extracellular Cu2+ and delivers its load via direct interaction with OprC"]; also found in
  cytoplasm and periplasm.
- Vijgenboom, Busch and Canters 1997 (Microbiology 143:2853-2863, DOI
  10.1099/00221287-143-9-2853; PMID not resolvable during this session, so not cited in the
  YAML): cytochrome c551, not azurin, is the functional electron donor in the nitrite
  reduction pathway in vivo; azu is induced in stationary phase (RpoS) and an azu mutant is
  more sensitive to H2O2 and paraquat (from the abstract via web search).
- UniProt P00282: signal peptide 1-20, Cu ligands (BINDING 66, 132, 137, 141), Swiss-Prot
  location periplasm; PANTHER PTHR38439 (auracyanin-B family).

### Annotation decisions

- GO:0005507 copper ion binding: IBA, IEA, IMP all ACCEPT (core).
- GO:0009055 electron transfer activity (IEA): ACCEPT (core; redox-shuttle cupredoxin).
- GO:0042597 periplasmic space (IEA): ACCEPT.
- GO:0005886 plasma membrane (IBA, PTN002212868): REMOVE, with a GO_CENTRAL defect (see below).
- GO:0008270 zinc ion binding (IMP): MARK_AS_OVER_ANNOTATED (Zn substitution in vitro).
- GO:0046914 transition metal ion binding (IDA, silver): TOO_GENERAL (copper ion binding accepted).
- GO:0042802 identical protein binding: PMID:19299503 MARK_AS_OVER_ANNOTATED (engineered
  loop mutant swap dimer); PMID:21352498 UNDECIDED (abstract does not show the basis).
- GO:0005515 protein binding (OprC, IPI): REMOVE per the protein-binding policy.
- Action counts: ACCEPT 5, REMOVE 2, MARK_AS_OVER_ANNOTATED 2, TOO_GENERAL 1, UNDECIDED 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002212874 | GO:0005507 copper ion binding | 2 | 6 (5 taxa) | GO:0005507, IMP, PMID:14758526 | SOUND | ITC and spectroscopy on WT and Met121Ala azurin measure copper affinities directly; the evidence is really direct binding (closer to IDA than IMP), but the term is right. | Chloroflexus auracyanin A (P27197; UniProt IDA PMID:1313011) | Yes |

Node PTN002212874 leaves: azurins of P. aeruginosa, Shewanella and Xanthomonas, Neisseria
Laz (NMB1533) and Chloroflexus auracyanins (P27197, Q8RMH6). All are type 1 blue copper
proteins, so the term suits the clade. No PSEUDOCAP defect (the evidence code is a minor
issue and the term is correct).

Not a PseudoCAP seed but checked: the plasma membrane IBA comes from PTN002212868, a
sole-seed IBD on auracyanin A (P27197, UniProt IDA PMID:1313011), a membrane-associated
cupredoxin of the monoderm Chloroflexus. Its 11 leaves include soluble periplasmic azurins
(P. aeruginosa azu, Shewanella azu, Xanthomonas az1), CopI and the lipid-anchored outer
membrane Laz of Neisseria. GO_CENTRAL defect recorded on the azurin IBA row (PROBABLE).

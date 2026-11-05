# PA4400 (Q9HW06) notes

## Identity: MutT, fused to a TenI-like domain

- TrEMBL, unreviewed, no gene name in UniProt. N-terminal Nudix hydrolase
  domain (1-128, Nudix box 38-59; NCBIfam TIGR00586 mutt; IPR003561
  Mutator_MutT) fused to a C-terminal thiamine-phosphate synthase-like TenI
  domain (PF02581 TMP-TENI; NCBIfam NF006530 PRK08999).
  [file:PSEAE/PA4400/PA4400-uniprot.txt "Mutator_MutT"]
- This is the mutT characterised by Oliver et al. 2002, whose abstract
  describes the same two-part architecture:
  [PMID:12445642 "the sequence of the P. aeruginosa mutT gene strongly suggested that the product of this gene has a bifunctional activity in P. aeruginosa, being the C-terminal part 40% identical to a consensus sequence of thiamine monophosphate synthases"]

## Literature

**Oliver, Sanchez and Blazquez 2002, PMID:12445642 (abstract only; no PMC).**
- Cloned PAO1 mutT, mutM and mutY complement the mutator phenotype of the
  corresponding E. coli mutants:
  [PMID:12445642 "The three genes, when cloned in a plasmid, were able to complement the high mutation frequency of the corresponding Escherichia coli deficient strains."]
  [PMID:12445642 "Our results also demonstrated that the N-terminal part of the protein is necessary and sufficient for the 8-oxodGTP hydrolase activity."]
- The abstract describes heterologous complementation of mutation frequency.
  Whether a direct 8-oxo-dGTPase assay was done cannot be seen. The "necessary
  and sufficient" statement may come from complementation with truncations.

Later work (not cached here) links P. aeruginosa GO-system defects (mutT,
mutY) to hypermutability in cystic fibrosis isolates; not needed for the
annotation calls.

## Comparator check for "DNA repair" on MutT

E. coli MutT (P08337) carries GO:0006281 DNA repair as EcoCyc EXP
(acts_upstream_of_or_within, PMID:7739614) and UniProt IC (PMID:10373420);
human NUDT1 carries DNA repair (IC) and DNA protection (GO:0042262). GO
practice is to annotate MutT-type 8-oxo-dGTPases, which prevent
incorporation of oxidised guanine, to DNA repair. The PseudoCAP term follows
that convention and is accepted.

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; P08337 annotations from QuickGO 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000755027 | GO:0006281 DNA repair | 2 | 27 (22 taxa) | GO:0006281, IDA, PMID:12445642 | SOUND | Complementation of the E. coli mutT mutator phenotype shows the antimutator (GO system) function; DNA repair is the GO convention for MutT. The evidence is heterologous complementation (IGI), not IDA: PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE (abstract states the method). Term suits the MutT clade. | E. coli MutT P08337 (EXP PMID:7739614, EcoCyc; IC PMID:10373420, UniProt) | Yes |

The other IBDs at this node (8-oxo-dGTP, 8-oxo-GTP pyrophosphatase; 8-oxo-dGDP,
8-oxo-GDP phosphatase) rest on P08337 only, with direct IDA data; PA4400 is
not a seed. No GO_CENTRAL defect.

## Review decisions

- ACCEPT: DNA repair (IBA, IDA with evidence-code defect, IEA);
  8-oxo-dGTP pyrophosphatase activity (IBA, IEA).
- KEEP_AS_NON_CORE: 8-oxo-GTP pyrophosphatase (IBA, IEA), 8-oxo-dGDP and
  8-oxo-GDP phosphatase (IBA). Shown for E. coli MutT; secondary to the
  dGTP-pool activity, not tested for PA4400.
- MODIFY: metal ion binding -> magnesium ion binding.
- TOO_GENERAL: hydrolase activity (IDA, IEA); GO:0035539 accepted.
- The TenI-like C-terminal domain has no GO row and no experimental data; a
  thiamine-related activity is not proposed.

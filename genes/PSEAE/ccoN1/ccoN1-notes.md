# ccoN1 (PA1554, Q9I3G3) review notes

## Review session 2026-11-12 (PseudoCAP tier 3, IMP-on-MF worklist)

Fetched with `just fetch-gene PSEAE ccoN1`. No deep-research provider file was generated.

Subunit I of the cbb3-1 oxidase. Evidence for the catalytic role, all from the UniProt record
and none of it ARBA-only: [file:PSEAE/ccoN1/ccoN1-uniprot.txt "Binds 1 copper ion per subunit,
denoted as copper B."], [file:PSEAE/ccoN1/ccoN1-uniprot.txt "Binds 2 heme groups per subunit,
denoted as high- and low-spin."] (both PIRSR), [file:PSEAE/ccoN1/ccoN1-uniprot.txt "PROSITE;
PS00077; COX1_CUB; 1."] and [file:PSEAE/ccoN1/ccoN1-uniprot.txt "NCBIfam; TIGR00780; ccoN; 1."].
475 residues, 12 transmembrane helices.

### Annotation decisions

- ACCEPT: GO:0004129 (IEA and IMP), GO:0005886, GO:0009060 (IBA and IEA), GO:0020037,
  GO:0022904, and GO:1902600 — the last accepted rather than kept non-core, because the proton
  channels of a heme-copper oxidase run through subunit I.
- MODIFY: GO:0006119 to GO:0019646 (the ccoP precedent); GO:0016020 to GO:0005886.
- NEW: GO:0005507 copper ion binding (IC). Copper B is curated on the record and the COX1_CUB
  site matches, yet only heme binding is annotated. The same gap applies to ccoN2.
- Three UniProt comments (CATALYTIC ACTIVITY, PATHWAY, SUBCELLULAR LOCATION) are ARBA-only on
  this record, so they are not cited as support; the validator flagged a first draft that did.
  The membrane and proton rows rest on the TRANSMEM features and the family assignment instead.

## Why this group was reviewed together

These six entries came off the tier-3 PseudoCAP worklist
(`projects/PSEUDOCAP/pseudocap_mf_worklist.yaml`), whose `shared_claims` block flags
`GO:0004129` / PMID:14763990 as one claim spread over six proteins. The two CcoP subunits of
the same operon pair were already reviewed, and the `ccoP1` review had already identified the
pattern: PseudoCAP entered the identical IMP row on 20190311 for all eight subunits of both
cbb3 operons, so a whole-operon deletion phenotype was transferred to each subunit.

The paper is abstract-only in our cache. What the abstract actually reports is isoform-level:
[PMID:14763990 "In highly aerated cultures, cbb3-1 abundance and expression were greater than
that of cbb3-2, and only loss of cbb3-1 influenced growth."] There is no ccoN-, ccoO- or
ccoQ-specific experiment described, so the per-subunit granularity of the GO rows is not
supported by what we can read.

None of the six seeds a PAINT IBD node (no `UniProtKB:<acc>` appears in any WITH/FROM of
`.cache/paint/IBD.gaf`), so unlike tiers 1 and 2 there is no node placement to argue with and
no `propagation_review` is needed. The IBA rows on ccoN1/ccoN2 are received, not seeded.

## The structural check

Both CcoO entries cross-reference PDB 8SMR and 8SNH. Queried against the RCSB API
(2026-11-12), both are 2.7 A cryo-EM models titled "cytochrome bc1-cbb3 supercomplex from
Pseudomonas aeruginosa", and their cbb3 chains map to:

| structure | catalytic CcoN | CcoO | CcoP | CcoQ |
|---|---|---|---|---|
| 8SMR | Q9HWP8 (PA4133) | Q9I3G4 (CcoO1) | Q9I3G5 (CcoP1) | absent |
| 8SNH | Q9HWP8 (PA4133) | Q9I3G4 (CcoO1) | Q9I3G2 (CcoP2) | absent |

Two things follow. The catalytic subunit modelled is the orphan CcoN paralogue PA4133, not
CcoN1 or CcoN2, which is why the ccoN reviews raise the isoform question rather than claiming
the structures as direct evidence for themselves. And no CcoQ chain is present in either model
— which is not proof that CcoQ is not a subunit, since a 61-residue single-helix chain is
easily lost on purification or left unmodelled, but it does mean no structural evidence places
it in the holoenzyme.

## How the eight subunits were differentiated

The corpus already treats `GO:0004129` on oxidase subunits along a gradient, and the human COX
reviews state the principle: the catalytic activity "resides in the mtDNA-encoded core
(binuclear centre of MT-CO1), not in the structural COX5A subunit". `SURF1`, an assembly
factor rather than a subunit, is the only one where the term is REMOVEd. Applying that here:

- **CcoN1, CcoN2** carry the catalytic machinery — curated PIRSR cofactors give one copper ion
  per subunit (copper B) and two hemes (high- and low-spin), and the chain matches PROSITE
  PS00077 COX1_CUB. Oxygen is reduced here, so `enables` is right and no qualifier defect is
  filed. This is the one place these reviews part company with the ccoP siblings.
- **CcoO1, CcoO2** (and CcoP) carry a heme and relay electrons, performing a step of the
  reaction without a catalytic site: ACCEPT the term, `contributes_to` in the core function,
  qualifier defect at PROBABLE.
- **CcoQ1, CcoQ2** carry no cofactor at all, are 61 residues with one transmembrane helix at
  protein existence 4 (Predicted), and are absent from both structures: MARK_AS_OVER_ANNOTATED,
  with the unknown recorded as a BIOLOGY knowledge gap. Not REMOVE, which would assert that
  CcoQ is not in the complex — the SURF1 case — and that has not been shown.

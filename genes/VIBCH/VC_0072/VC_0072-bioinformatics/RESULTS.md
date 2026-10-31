# VC_0072 (Q9KVR7) bioinformatics: GGDEF/EAL motif check and dashboard gene model

## Question

The dashboard call ("c-di-GMP-binding protein containing PAS, GGDEF, and EAL domains")
declines to name a catalytic activity. Are the GGDEF (diguanylate cyclase) and EAL
(c-di-GMP phosphodiesterase) catalytic motifs intact, is there a GGDEF I-site (RxxD), and
how does the 785-aa dashboard sequence relate to the 768-aa UniProt entry?

## Method

`analyze.py` (stdlib Python, regex motif search on the UniProt Q9KVR7 sequence within the
PROSITE domain boundaries GGDEF 368-501 and EAL 512-767; difflib comparison of the
dashboard sequence with UniProt). Run through BERIL:
`beril run --name vc0072-motifs` -> run `20261030T213409Z-vc0072-motifs`
(`projects/hackathon/runs/20261030T213409Z-vc0072-motifs/out/results.json`, copied here
as `results.json`). An earlier run `20261030T213353Z-vc0072-motifs` wrote nothing because
the output-directory variable was not expanded; it should be ignored.

Motif positions are given in UniProt Q9KVR7 numbering. Motif expectations follow the
canonical GGDEF (PleD/WspR) and EAL (RocR/YkuI/FimX) literature; no structural
alignment to a characterized enzyme was done.

## Results

### Dashboard vs UniProt gene model

- The dashboard sequence carries an 18-residue N-terminal segment `MKLKCAYFTTIKTIGLTL`
  before the residue that aligns with UniProt position 2 (E). UniProt Met1 therefore
  corresponds to dashboard Leu18, i.e. the N16961 gene model starts at an alternative
  (non-ATG, likely TTG/CTG) codon, and the dashboard (draft genome NZ_JAACMT010000013.1)
  gene caller chose an in-frame upstream start. Net length difference 17 aa (785 vs 768).
- Only two substitutions in the aligned region: dashboard V84 / UniProt A67 (inside the
  predicted TM helix) and dashboard E381 / UniProt D364 (just before the GGDEF domain).
  99.7% identity over 768 aligned residues.
- Neither difference touches any catalytic motif. Which start codon is used in vivo is
  unknown; both models keep the hydrophobic N-terminal region and the single TM helix
  (UniProt 57-79; DeepTMHMM on the dashboard sequence: TM 78-96, cytoplasmic 97-785).

### GGDEF domain (UniProt 368-501)

- A-site: **GGDEF at 417-421** (intact).
- Beta-1 metal-binding `D[LI]D`: **DLD at 376-378** (context `YLDLDQLK`).
- `HxxGD` (metal/GTP-binding loop): **HDAGD at 389-393** (context `TAGHDAGDGA`).
- I-site: the 9 residues preceding GGDEF are `PFKATLARM`; **no RxxD** in the canonical
  I-site position (RxxD-x5-GGDEF). The only RxxD in the domain (`RMID`, 465) is
  downstream of the GGDEF motif and not at the I-site position. This agrees with Roelofs
  et al. 2015 (PMID:26506097).
- Conclusion: the GGDEF domain has the canonical catalytic signature and could be an
  active diguanylate cyclase, but activity has not been measured.

### EAL domain (UniProt 512-767)

- `ExLxR` motif: **EVLVR at 548-552** (EVL variant of EAL; Glu and Arg retained).
- Asn of the N-loop region: **INLS at 606** (`SINLSGNS`).
- Glu of `ExxE`-type motif: **EITE at 639** (`CFEITETAAM`).
- Loop 6: **DDFGSG at 669-674** (`ALDDFGSGLSSF`; the conserved DDFGTG with T->S).
- Catalytic Lys: **KID at 690** (`VDIVKIDGIF`).
- Glu in `E[GF]VE`: **EFVE at 726** (`TVAEFVENQQ`).
- Conclusion: all EAL residues normally needed for Mg2+-dependent c-di-GMP hydrolysis are
  present; the domain is predicted to be catalytically competent. Activity has not been
  measured for VC0072.

## Interpretation

Both output domains retain canonical catalytic motifs, so VC0072 cannot be classed as a
degenerate (receptor-only) GGDEF-EAL protein on sequence grounds. Its experimentally shown
c-di-GMP binding (lysate DRaCALA, PMID:26506097) is most simply explained by substrate
binding at the intact EAL site. The protein is best described as a membrane-anchored
PAS-GGDEF-EAL c-di-GMP-metabolizing protein, probably a phosphodiesterase and possibly
bifunctional; which activity dominates in vivo is untested.

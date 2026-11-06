# ureB (P69996, H. pylori 26695) - curation notes

Deep research: the single attempted run (`just deep-research HELPY ureG --provider
perplexity`, 2026-10-23) failed because only the `falcon` and `openscientist` providers are
configured in this checkout. No `-deep-research-*.md` file was written. Notes below come from
the cached publications, the UniProt record and PubMed lookups.

## What UreB is

The catalytic subunit - the alpha/UreC equivalent - of the two-chain H. pylori urease
[PMID:22013070 "the ureA gene encodes the β and γ subunits as a fusion protein, and the ureB
gene encodes the α subunit"]. It carries the metallo-dependent hydrolase domain (UniProt
DOMAIN 131..569), ACT_SITE 322, the nickel-ligand BINDING features, and MOD_RES 219
(carbamylated lysine). Activation requires Lys219 carbamylation plus insertion of two nickel
ions [PMID:22013070 "Activation of apo-urease involves carboxylation of lysine 219 and
insertion of two nickel ions."].

Enzymology of the native enzyme: Km 0.3 mM, Vmax ~1100 umol urea/min/mg
[PMID:2188975 "The purified enzyme exhibited a Km of 0.3 +/- 0.1 mM and a Vmax of 1,100 +/-
200 mumols of urea hydrolyzed/min/mg of protein"]. Physiological point: urease is required
for gastric colonization [PMID:8039935 "H. pylori urease is essential for colonizing the nude
mouse stomach"].

## Decisions

- `GO:0009039` (IBA PTN001702453 + IEA) and `GO:0043419` (IBA + IEA): ACCEPT. UreB is inside
  the urease alpha-subunit clade and all active-site features are conserved.
- `GO:0016151 nickel cation binding`: ACCEPT - cofactor binding integral to catalysis
  (carbamylated Lys219 bridges the two nickels; UniProt PTM line with
  ECO:0000269|PubMed:11373617).
- `GO:0016787` and `GO:0016810`: TOO_GENERAL - ancestors of the accepted urease activity.
- Two bare `GO:0005515` rows (partner UreA): REMOVE per the protein-binding policy; the
  association is recorded as `GO:0035550` membership instead.
- `GO:0035550 urease complex` added as NEW (IDA, PMID:11373617) - UreA already carries it,
  UreB did not.

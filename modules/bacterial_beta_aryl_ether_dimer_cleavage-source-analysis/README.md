# Beta-aryl ether dimer cleavage audit

Run from the repository root:

```bash
uv run python modules/bacterial_beta_aryl_ether_dimer_cleavage-source-analysis/check_preservation.py
uv run python modules/bacterial_beta_aryl_ether_dimer_cleavage-source-analysis/check_routes.py
uv run python modules/bacterial_beta_aryl_ether_dimer_cleavage-source-analysis/check_module.py
```

Results and the seeding baseline are in
`analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/`.
The baseline captures the original annotation payloads and raw-source SHA256
hashes before curation. Three deleted SYK-6 accessions were recovered from
version-pinned UniSave records through the documented LigN source-analysis
wrapper; they are not presented as current UniProt entries.

The production Boolean compiler tests enzyme capacity with explicit inventories,
native implementations, complex assembly and supplied NAD+/GSH. It does not infer
these inputs from family membership, predict flux or growth, or infer native
expression. The separate native-extract case supplies the published negligible
LigO contribution as an external constraint. Both alpha substrate classes and
both beta classes are required for the complete SYK-6 route. LigG's weak
betaS-conjugate activity is not treated as a replacement for native LigQ.

F199 is an optional, independently assayed downstream MPHPV subroute. Its
first-step dehydrogenase assignments remain predictions. BaeAB requires one
subunit of each kind; trace isolated-subunit conversion is not sufficient.
BaeAB product epimer is unassigned, and NaGSTNu accepts both epimers. The
NaLigE/NaLigF1 conjugate configuration follows the documented class mechanism;
it is explicitly distinguished from direct absolute product assignment.
NaLigF2 is an isolated substituted-dimer comparator: its GβG substrate yields
vanillin and a substituted conjugate, and does not establish MPHPV turnover.
K-12 YghU disulfide reduction is separated from DH5alpha-derived GS-HPV assays
and heterologous F199 complementation. Neither comparator satisfies a native
complete GGE route.

The module checker uses the production semantic validator, scoped gene reviews
and PANTHER memberships read from the unedited raw records. PANTHER labels are
checked against the committed ontology. Literal evidence quotes are checked
against the cited local publication/source. Source-level scientific review
separately checked substrate identities, stereochemistry, experimental strain,
native versus recombinant evidence and current taxonomy. Automated checks alone
do not establish those biological interpretations.

Thirty function-conformance advisories remain because the exact oxidation,
aryl-ether substitution and reductive deglutathionylation activities have no
precise GO identifier established in this audit. Gene reviews use supported
proposed activities; the module retains exact free-text chemistry. Assigning a
halide-displacement or carbon-sulfur-elimination term would misstate the reaction.
Taxonomy JSON records are unedited UniProt API responses with URLs and hashes
in `taxonomy/provenance.yaml`. They supplement, rather than rewrite, raw gene
record taxon identifiers.

The module checker also requires all fifteen proposed-function uses to match the
three canonical definitions, parents and justifications. Gene-specific quotations
and stereochemical roles remain separate. Official UniParc cross-reference
responses and the reproducible lookup script are retained under LigN source
analysis; no active UniProtKB equivalent was returned for any of the three
archived exact sequences on 2026-11-03.

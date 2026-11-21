# PP_0075 curation notes

## Evidence boundary

PP_0075 (Q88RQ4) is a 521-aa multi-pass membrane protein annotated as a
choline-sulfate transporter. Its current architecture is SLC26A/SulP plus a
cytoplasmic STAS domain, not a canonical ABC permease/ATPase architecture
[`PP_0075-uniprot.txt`, "InterPro; IPR001902; SLC26A/SulP_fam.";
"InterPro; IPR002645; STAS_dom."].

The adjacent KT2440 `betC` locus was studied genetically. The paper describes
an adjacent putative ABC transporter, but the decisive phenotype is that a
`betC` mutant still accumulated intact choline-O-sulfate while failing to use
it as carbon or nitrogen. This establishes a role for BetC in utilization and
shows that uptake can occur independently of BetC; it does not directly assay
PP_0075 or establish PP_0075 as the sole choline-O-sulfate importer
[PMID:17116241, "This mutant still accumulated intact COS but failed to use
this compound as carbon or nitrogen source."].

## Curation position

- Retain the well-supported membrane location and generic transmembrane
  transport process.
- Treat choline-O-sulfate specificity as a pathway-level candidate assignment,
  not as an experimentally established gene-level function.
- Do not annotate PP_0075 as an ABC-transporter component.

## OpenScientist adjudication

The report correctly retrieves the SulP/SLC26-STAS architecture and the absence
of a direct transport assay. Its proposed sulfate cargo remains speculative.
Its assignment of intact choline-O-sulfate uptake to an unspecified ABC route
is also not established by the target or cached KT2440 evidence.

## 2026-11-02 completion (choline-O-sulfate module curation)

- GO:0016020 membrane changed from KEEP_AS_NON_CORE to MODIFY -> GO:0005886 plasma
  membrane: correct but general; nine Phobius helices plus SLC26A/SulP domain in a
  Gram-negative bacterium place the protein in the cytoplasmic (inner) membrane.
- Removed reliance on the ARBA-only SUBCELLULAR LOCATION line as support.
- Status set to COMPLETE.


## 2026-11-06 cross-taxon choline-sulfate audit

Retained all three original rows, including the inherited NEW generic transporter activity. Exact cargo/coupling and partnership with PP_0076 remain unresolved. Replaced an incorrect universal Gram-negative membrane argument with target architecture and added inferred plasma-membrane core location. SulP/STAS and adjacency are not direct COS-uptake evidence.

Reviewed the existing OpenScientist provider report and primary/cached sources; preserved the provider report and its PDF/HTML artifacts. A provider report is already present, so no replacement research run was needed. All machine annotation payloads and raw UniProt/GOA files are unchanged. No new annotation rows were added. Generic family labels and locus proximity do not establish COS transport, a BetD-BetE complex, or substrate promiscuity in unassayed homologs.

Normal force-fetches of PMID:17116241 and PMID:21369825 still returned abstract-only caches; their assay limitations remain explicit. PMID:9736747 also remains abstract-only in the cache after the root fetch. PMC methods were independently accessible at https://pmc.ncbi.nlm.nih.gov/articles/PMC21653/ and explicitly name 102F34R; direct HTML retrieval encountered a challenge, Europe PMC XML returned HTTP500, and NCBI BioC returned no result. No publication cache was hand-edited or invented. Existing abstract quotations remain used as such. Full-text PMID:29458126 and PMID:35503214 distinguish recombinant source strains and assay conditions.

Focused gene validation passed. Preservation is reproducibly checked by `.cache/module-audit-logs/choline-sulfate-20261106/check-existing-four.py`, against the frozen original baseline: 16 total rows, one inherited NEW, zero added rows, eight raw and twelve provider/artifact hashes unchanged. PSEPK/betC retains the advisory about not citing its low-quality provider in annotation support; primary and curated family evidence are used instead.

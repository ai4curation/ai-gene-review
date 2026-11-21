# betC curation notes

## Evidence boundary

KT2440 BetC (Q88RQ2; PP_0077) is assigned EC 3.1.6.6 and the exact
choline-sulfatase family signature [`betC-uniprot.txt`, "EC=3.1.6.6";
"InterPro; IPR017785; Choline-sulfatase."]. The KT2440 genetic study found
that a `betC` mutant accumulated intact choline-O-sulfate but could not use it
as carbon or nitrogen, supporting a central role in utilization rather than
uptake or osmoprotection [PMID:17116241, "This mutant still accumulated intact
COS but failed to use this compound as carbon or nitrogen source."].

Direct ortholog evidence comes from Sinorhizobium meliloti BetC (UniProt
O69787): the gene encodes a choline sulfatase converting choline-O-sulfate, and
more slowly phosphorylcholine, to choline [PMID:9736747, "a new gene (betC) was
identified as encoding a choline sulfatase catalyzing the conversion of
choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline."].

The same Sinorhizobium choline sulfatase was subsequently characterized as a
purified enzyme and by X-ray crystallography [PMID:29458126,
"Sinorhizobium meliloti choline sulfatase (SmCS) efficiently catalyzes the
hydrolysis of alkyl sulfate choline-O-sulfate"]. This provides a direct
structural and kinetic exemplar for the exact BetC family assignment.

PANTHER PTHR45953:SF1 is not used as an exact BetC selector because its official
label is `IDURONATE 2-SULFATASE` and its membership spans functionally distinct
sulfatases. InterPro IPR017785 and the characterized UniProt exemplar provide a
more defensible module selector.

## Curation position

- Accept exact choline-sulfatase activity as the core function.
- Retain sulfuric ester hydrolase activity as a valid but broad non-core parent.
- Retain cytoplasm only as non-core localization evidence.

## OpenScientist adjudication

The report correctly identifies Q88RQ2, the C52-A-P-S-R sulfatase motif, the
direct KT2440 `betC` phenotype, and the absence of purified target-protein
kinetics. Its claim that an adjacent ABC transporter imports choline-O-sulfate
is not adopted: PP_0075 has SLC26A/SulP-STAS architecture, no cognate local ABC
ATPase is established, and neither PP_0075 nor PP_0076 has a target-specific
transport assay.

## 2026-11-02 completion (choline-O-sulfate module curation)

- GO:0008484 sulfuric ester hydrolase activity changed from KEEP_AS_NON_CORE to
  MODIFY -> GO:0047753 (correct but general; consistent with S. meliloti ortholog
  O69787, reviewed in genes/RHIME/betC).
- Cytoplasm row now supported by the betC deletion phenotype (intact COS accumulates
  inside cells) and the choline-sulfatase InterPro signature.
- Status set to COMPLETE.


## 2026-11-06 cross-taxon choline-sulfate audit

Retained all three original row payloads. Cytoplasm now ACCEPT as inferred core location. KT2440 genetics plus specific family evidence support sulfatase activity, while isolated Q88RQ2 kinetics and phosphorylcholine physiology remain unestablished. Removed a provider absence-of-assay sentence as positive activity evidence. Sinorhizobium strain-specific genetics and recombinant assays are comparative, not target assays.

Reviewed the existing OpenScientist provider report and primary/cached sources; preserved the provider report and its PDF/HTML artifacts. A provider report is already present, so no replacement research run was needed. All machine annotation payloads and raw UniProt/GOA files are unchanged. No new annotation rows were added. Generic family labels and locus proximity do not establish COS transport, a BetD-BetE complex, or substrate promiscuity in unassayed homologs.

Normal force-fetches of PMID:17116241 and PMID:21369825 still returned abstract-only caches; their assay limitations remain explicit. PMID:9736747 also remains abstract-only in the cache after the root fetch. PMC methods were independently accessible at https://pmc.ncbi.nlm.nih.gov/articles/PMC21653/ and explicitly name 102F34R; direct HTML retrieval encountered a challenge, Europe PMC XML returned HTTP500, and NCBI BioC returned no result. No publication cache was hand-edited or invented. Existing abstract quotations remain used as such. Full-text PMID:29458126 and PMID:35503214 distinguish recombinant source strains and assay conditions.

Focused gene validation passed. Preservation is reproducibly checked by `.cache/module-audit-logs/choline-sulfate-20261106/check-existing-four.py`, against the frozen original baseline: 16 total rows, one inherited NEW, zero added rows, eight raw and twelve provider/artifact hashes unchanged. PSEPK/betC retains the advisory about not citing its low-quality provider in annotation support; primary and curated family evidence are used instead.


## PR6105 round1 evidence-scope reassessment (2026-11-06)

The existing TreeGrafter cytoplasm inference is plausible and is not contradicted. KT2440 provides stronger target physiology than the other BetC comparators: the betC mutant still accumulates intact COS while failing to use it as carbon or nitrogen source (PMID:17116241). This favors uptake before BetC-dependent hydrolysis, but the accessible abstract does not identify a compartment-resolving assay or locate the enzyme. Accumulation alone does not discriminate cytoplasmic enzyme activity from another cell compartment. Choline-sulfatase family membership supports the chemistry, not the side of the membrane where it occurs. With full experimental localization evidence unavailable, retain this original row as UNDECIDED and omit a core location; the supported molecular function is unchanged.

The cytoplasm row is retained as UNDECIDED, and no activity location is asserted in core_functions. Molecular-function verdicts, original annotation payloads, raw sources and genuine provider research remain unchanged. No publication cache was refreshed.

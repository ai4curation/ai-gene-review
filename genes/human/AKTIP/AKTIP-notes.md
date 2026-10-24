# AKTIP review notes


## 2026-09-20 full-gene IBA re-review

All 38 original annotations assessed; 37 remain after removing the author-added generic molecular-adaptor NEW now covered by evidence-backed MODIFY rows. All 34 actual source rows remain semantically intact. Three earlier NEW annotations remain with primary references replacing provider-only references.

No preexisting OpenScientist report was present. Falcon provides leads to PMID:26110528 (telomere replication) and PMID:34449766 (ESCRT/midbody); both primary full texts were fetched and read. AKTIP is a UEV lacking the catalytic cysteine, supporting rejection of direct E2 activity and retention of the preexisting negative ubiquitin-transferase assertion.

Loss of catalysis does not refute K63 ubiquitination participation. The cached GOA WITH/FROM field establishes PANTHER:PTN000630262 for both K63 ubiquitination and DNA damage tolerance. Extant donor count was not used. Existing propagation review was corrected to target the ancestral node and the actual unresolved noncatalytic function.

QuickGO GO:0006301 defines lesion bypass during DNA replication without removing the damage (https://www.ebi.ac.uk/QuickGO/term/GO:0006301). Telomere-fork progression and PCNA recruitment do not alone establish that specific process. Both DNA damage tolerance and K63 chain-assembly participation remain UNDECIDED pending root-owned focused adjudication.

PMID:14749367 reports a PDK1/AKT/GSK3/NF-ATc/Fas-ligand apoptosis mechanism in T lymphocytes; restored KEEP_AS_NON_CORE rather than treating later discoveries as refutation. PMID:36516775 describes a distinct ER-positive breast-cell CAND1/cullin context and does not establish K63 chains.

FHF assembly and cargo transport are supported by PMID:18799622, PMID:32073997 and PMID:34882091. Corresponding generic-binding rows now MODIFY to molecular adaptor activity. HOPS-associated trafficking is retained on the primary interaction/function evidence; the rationale no longer argues from the GOA relationship field.

Existing telomere-maintenance, midbody and cytokinesis NEW proposals now cite the exact primary experiments, demonstrate structural participation, and are independent of annotation-gap reasoning. No AKTIP/Q9H8T0 match was found in gocams/index.tsv. No new process assertion was introduced.

Verified the proximate IBA PANTHER nodes from cached WITH/FROM fields and revised structured propagation metadata to match final decisions; no relationship-field reasoning, donor-count argument, or invented topology reconstruction was used.


## 2026-09-21 focused report incorporation

Read the complete ready OpenScientist report and both HTML/PDF artifacts; independent source and phylogeny checks are recorded in [AKTIP-primary-source-checks.md](AKTIP-primary-source-checks.md) and [AKTIP-paint-lineage.json](AKTIP-paint-lineage.json). The two process rows are restored from UNDECIDED to KEEP_AS_NON_CORE on confirmed descent from PTN000630262, with no process-negative node on the target path. The report's UBE2V-only source-clade narrative is incorrect: the actual source IBD includes UBE2N orthologs, and human AKTIP is a descendant. Live v19 uses PTHR24068 where the newer local records use PTHR24067; persistent nodes connect them.

Intrinsic E2 activity stays REMOVE because Asp replaces the catalytic cysteine; this does not refute noncatalytic BP participation. Full PMID:36516775 Figure 3 confirms a CAND1/CUL2-linked ubiquitination context, but does not specify K63 linkage and expressly leaves the ligase-activity mechanism unvalidated. PMID:26110528 Figures 6–7 show replication support, not a defined lesion-bypass assay. The primary limits and remaining human mechanism questions are preserved rather than converted to loss claims. All 37 prior source objects (34 actual source rows plus three pre-existing NEWs) are unchanged; no NEW or duplicate provider run added.

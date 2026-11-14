# iscS curation notes

## Target selection

PP_0842/Q88PK8 is the relay-relevant IscS paralog. The module-level
OpenScientist analysis reports 72.5% identity to *E. coli* IscS, the
IscS-specific IPR010240 signature, and placement in the canonical
`iscS-iscU-iscA-hscB` locus; PP_2435 lacks that specific signature and locus
context. [file:projects/P_PUTIDA/deep-research/PSEPK__bacterial-mnma-trna-wobble-uridine-thiolation-sulfur-relay__ppu04122-deep-research-openscientist.md
"only PP_0842 carries the IscS-specific InterPro **IPR010240
(Cys_deSase_IscS)**"]

## Functional boundary

IscS is a multi-branch cysteine desulfurase, not a tRNA-specific enzyme. The
review therefore retains both tRNA wobble-uridine thiolation and [2Fe-2S]
cluster assembly as core processes, while the reusable MnmA module includes
only the Tus-relay branch. The cluster-binding annotation is valid but non-core:
the local feature table records a transient [2Fe-2S] ligand shared with IscU.
[file:PSEPK/iscS/iscS-uniprot.txt "ligand shared with IscU"]

The ordered relay assignment is transferred from the reconstituted *E. coli*
system, where IscS directly transfers persulfide sulfur to TusA; no direct
KT2440 reconstitution was identified. [PMID:16387657 "IscS transfers the
persulfide sulfur to TusA."]

## Isc cluster-assembly branch (wave43 curation)

- Q88PK8 is the KT2440 IscS-family PLP-dependent cysteine desulfurase. UniProt/HAMAP supports the catalytic assignment; direct KT2440 biochemistry was not found.
- Reconstituted *E. coli* ISC machinery shows IscS inserting persulfide into iron-bound IscU, followed by Fdx-dependent sulfide formation [PMID:39870763 "this process is initiated by iron binding to the scaffold protein IscU, which triggers persulfide insertion by the cysteine desulfurase IscS"].
- This ortholog evidence supports the conserved Isc role without implying that all IscS sulfur flux in KT2440 is restricted to Fe-S assembly.


## Isc comparative-evidence audit (2026-11-07)

IscS is the cytoplasmic pyridoxal-phosphate-dependent cysteine desulfurase of Pseudomonas putida KT2440. It converts L-cysteine to L-alanine while forming an enzyme-bound persulfide, which supplies sulfur to acceptors involved in iron-sulfur cluster assembly, tRNA thiolation and cofactor biosynthesis. IscU is its cluster-assembly scaffold partner; sulfur allocation among the different acceptor pathways is not restricted to the Isc locus.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-iscS.log`.

### Evidence and biological limits

- [PMID:16387657] IscS supplies persulfide sulfur to the Tus relay during reconstituted wobble-uridine thiolation. Quoted support: “IscS transfers the persulfide sulfur to TusA.”.
- [PMID:39870763] Reconstituted E. coli IscS inserts persulfide into an iron-loaded IscU scaffold; this supports the conserved sulfur-donor mechanism. Quoted support: “which triggers persulfide insertion by the cysteine desulfurase IscS”.

### Decisions

- GO:0005737 cytoplasm: ACCEPT. Curated HAMAP target localization and the soluble sulfur-transfer mechanism support the cytoplasm; this is conserved-function inference, not KT2440 fractionation.
- GO:0030170 pyridoxal phosphate binding: ACCEPT. The curated target cofactor statement assigns pyridoxal phosphate through HAMAP MF_00331, independently of an automatic label. Cofactor binding is integral to cysteine desulfuration.
- GO:0031071 cysteine desulfurase activity: ACCEPT. The target HAMAP function and catalytic reaction establish cysteine desulfurase activity by curated family inference; no purified KT2440 assay is implied.
- GO:0044571 [2Fe-2S] cluster assembly: ACCEPT. The target curated sulfur-delivery statement and E. coli reconstitution support this branch. PMID39870763 is a homolog experiment and does not determine target flux allocation or every intermediate in KT2440.
- GO:0051537 2 iron, 2 sulfur cluster binding: KEEP_AS_NON_CORE. The target HAMAP-derived binding feature describes a persulfide-associated ligand shared with IscU, not a constitutive redox cofactor on IscS. Retain this restricted intermediate-associated claim as non-core; its occupancy and lifetime have not been measured in KT2440.
- GO:0002143 tRNA wobble position uridine thiolation: NEW. The original TAS/module payload is preserved. Independent support is the curated target tRNA-modification branch and reconstitution of the IscS-Tus sulfur relay in PMID16387657. The latter is comparative evidence, not a KT2440 pathway-flux assay; IscS performs sulfur mobilization rather than merely serving as a consumed substrate.

Final shared-ligand source adjudication: GO0051537 is UNDECIDED, superseding the earlier KEEP_AS_NON_CORE discussion above. PMID36605734 identifies the structural precedent as Archaeoglobus fulgidus IscS-IscU(D35A), with a modified scaffold; “indicates that persulfide coordination of iron at the cluster site is possible.” The target HAMAP feature supports a plausible inference, but does not resolve native bacterial IscS cluster occupancy. No negative binding assay or universal absence is asserted.

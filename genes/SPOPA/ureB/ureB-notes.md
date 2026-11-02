# ureB (P41021, URE2_SPOPA) — Sporosarcina pasteurii urease beta subunit

## What the protein is

- Reviewed Swiss-Prot entry P41021, 126 aa, same ure operon as ureA and ureC
  [file:SPOPA/ureB/ureB-uniprot.txt "STRAIN=ATCC 11859 / DSM 33 / NCIB 8841 / NCTC 4822"].
- Beta chain of the three-chain urease: "Heterotrimer of UreA (gamma), UreB (beta) and
  UreC (alpha) subunits. Three heterotrimers associate to form the active enzyme"
  [file:SPOPA/ureB/ureB-uniprot.txt], with ECO:0000269 evidence from the S. pasteurii
  structures. 36 PDB cross-references; protein-existence level 1.
- Signatures: HAMAP MF_01954 Urease_beta, Pfam PF00699, NCBIfam TIGR00192,
  InterPro IPR002019 / IPR036461, PANTHER PTHR33569.
- No BINDING, MOD_RES or metal keyword on the entry; keywords are
  "3D-structure; Cytoplasm; Hydrolase." The nickel site is on the alpha subunit
  [file:SPOPA/ureC/ureC-uniprot.txt "Note=Binds 2 nickel ions per subunit."],
  as resolved crystallographically [PMID:10368287 "In the native enzyme, the coordination
  sphere of each of the two nickel ions is completed by a water molecule and a bridging
  hydroxide."].

## Review calls

- GO:0009039 urease activity: MARK_AS_OVER_ANNOTATED, for the same reason as ureA — the
  reaction belongs to the assembled enzyme and the beta chain contributes to it rather
  than possessing it (recorded as `contributes_to_molecular_function`).
- GO:0035550 urease complex: ACCEPT. This is the one subunit GOA gives the complex term
  to, via InterPro:IPR002019, and it is exactly right.
- GO:0005737 and GO:0043419: ACCEPT.
- Added as NEW: GO:0005198 structural molecule activity.
- Note the contrast with ureA: the beta-subunit InterPro entry does not carry a
  nickel-binding mapping, so no defect arises here, while the gamma-subunit entries do
  (see ureA-notes.md).

## CMMMech usage note (no edits made to CMMMech)

CMMMech's `functional_role` for this accession is "Beta subunit (UreB; EC 3.5.1.5) of the
heterotrimeric Sporosarcina pasteurii urease complex". As for ureA, the EC number
describes the complex rather than this chain. The caveats recorded in ureC-notes.md
(representative-only evidence in the MICP sources; the reaction occurs in the cytoplasm)
apply equally here.

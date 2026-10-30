# ureA (P41022, URE3_SPOPA) — Sporosarcina pasteurii urease gamma subunit

## What the protein is

- Reviewed Swiss-Prot entry P41022, 100 aa, same strain and same ure operon as ureB and
  ureC [file:SPOPA/ureA/ureA-uniprot.txt "STRAIN=ATCC 11859 / DSM 33 / NCIB 8841 / NCTC 4822"].
- Gamma chain of the three-chain urease: "Heterotrimer of UreA (gamma), UreB (beta) and
  UreC (alpha) subunits. Three heterotrimers associate to form the active enzyme"
  [file:SPOPA/ureA/ureA-uniprot.txt], with ECO:0000269 evidence from the S. pasteurii
  crystal structures (PubMed:9761912, 10368287, 10766443, 11713685, 15038715).
- Signatures: HAMAP MF_00739 Urease_gamma, Pfam PF00547, NCBIfam TIGR00193,
  InterPro IPR012010 / IPR002026 / IPR036463, PANTHER PTHR33569.
- The entry notes an N-terminal modification modelled in the PDB entries: "The N-terminal
  is probably N-(dihydroxymethyl)methionine, the hydrated form of N-formylmethionine"
  [file:SPOPA/ureA/ureA-uniprot.txt]. UniProt states it is not discussed in the published
  references, so nothing functional is read into it here.

## The nickel-binding annotation is wrong for this subunit

- P41022 has no BINDING feature, no MOD_RES and no Nickel keyword; its keyword line is
  "3D-structure; Cytoplasm; Formylation; Hydrolase."
- All the metal chemistry is on the alpha subunit: "Binds 2 nickel ions per subunit"
  with ligands His137, His139, carboxy-Lys220, His249, His275 and Asp363
  [file:SPOPA/ureC/ureC-uniprot.txt], consistent with the native structure
  [PMID:10368287 "In the native enzyme, the coordination sphere of each of the two nickel
  ions is completed by a water molecule and a bridging hydroxide."].
- The GO:0016151 row comes from interpro2go. Both source entries were checked against the
  InterPro API: IPR002026 (Urease, gamma/gamma-beta subunit) and IPR036463 (Urease, gamma
  subunit superfamily) each map to GO:0016151 nickel cation binding and GO:0043419 urea
  catabolic process. The GO:0043419 mappings are right; the GO:0016151 mappings propagate a nickel-binding
  claim to every urease gamma subunit and to the fused gamma-beta subunits. Recorded as
  two `source_defects` (resource InterPro, `requested_change: DELETE_VALUE`), and the row
  is REMOVEd.

## Review calls

- GO:0016151: REMOVE, with the interpro2go defects above.
- GO:0009039 urease activity: MARK_AS_OVER_ANNOTATED. The reaction belongs to the
  assembled enzyme; the gamma chain contributes to it (recorded as
  `contributes_to_molecular_function`) but cannot perform it.
- GO:0019627: TOO_GENERAL (true, but entailed by the accepted descendant GO:0043419).
- GO:0005737 and GO:0043419: ACCEPT.
- Added as NEW: GO:0035550 urease complex (part_of) and GO:0005198 structural molecule
  activity, following the treatment of the Pseudomonas putida gamma subunit in
  genes/PSEPK/ureA.

## CMMMech usage note (no edits made to CMMMech)

CMMMech grounds its MICP mechanisms to this accession with `functional_role` "Gamma
subunit (UreA; EC 3.5.1.5) of the heterotrimeric Sporosarcina pasteurii urease complex".
Attaching the EC number to the subunit is the same shorthand GOA uses and is harmless at
the record level, but this subunit is not catalytic and does not bind nickel; the
catalytic claim should be read as a property of the complex. The caveats recorded in
ureC-notes.md (representative-only evidence; cytoplasmic site of the reaction) apply
equally here.

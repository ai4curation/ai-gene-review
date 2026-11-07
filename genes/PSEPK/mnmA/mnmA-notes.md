# mnmA curation notes

## Functional assignment

PP_4014/Q88FR9 is the single KT2440 MnmA-family tRNA-specific
2-thiouridylase. The local record assigns EC 2.8.1.13, IPR004506, ATP-binding
features, and catalytic cysteines; the OpenScientist analysis additionally
reports conservation of the ATP-utilizing PP-loop and both catalytic cysteines.
[file:PSEPK/mnmA/mnmA-uniprot.txt "Catalyzes the 2-thiolation of uridine at the
wobble position"]

Structural work on *E. coli* MnmA directly establishes tRNA U34 recognition and
an adenylated RNA intermediate. [PMID:16871210 "The adenylated RNA intermediate
is trapped."] ATP binding is therefore added as a missing `NEW` annotation from
the local UniProt record, not proposed as a new ontology term because
GO:0005524 already exists.

The relay boundary ends at MnmA-mediated sulfur incorporation. MnmE/MnmG and
MnmC-dependent side-chain elaboration are downstream and are not assigned to
MnmA. The modified wobble base has a direct decoding role, but that system-level
effect is context rather than an additional MnmA molecular function.
[PMID:26791911 "We show that mnm(5)s(2)U forms an unusual pair with guanosine at
the wobble position"] The full *E. coli* IscS-TusA-TusBCD-TusE-MnmA pathway was
reconstituted, but no direct KT2440 reconstitution was identified.
[PMID:16387657 "Efficient 2-thiouridine formation in vitro was reconstituted
with recombinant TusA, a TusBCD complex, TusE, and previously identified IscS
and MnmA."]


## 2026-11-07 — complete source-aware review

All original rows and historical NEW proposals are retained in their original order and source payload. The review now distinguishes target-specific family/curated-site inference from E. coli experiments; no KT2440 assay is invented. The soluble location is inferred from the conserved reaction/complex context, not ARBA-only annotation. Broad true rows are refined where ontology ancestry supports it; covalent sulfur-carrier and sulfurtransferase terms are not treated as a false hierarchy.

ATP-dependent tRNA uridine34 C2 thiolation supported by conserved MnmA architecture; terminal persulfide versus Fe-S-mediated chemistry is unresolved in KT2440.

Evidence and exact source/access limits are in [the consultation](../../../analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/evidence.md). A reproducible frozen-sequence alignment independently checks conserved sites rather than quoting generated provider claims. Existing OpenScientist material is discovery provenance. A normal Falcon attempt for this gene failed HTTP403 authentication; the actual log is retained at `analysis/module_audits/bacterial_mnma_trna_thiolation/existing-review-consultation/falcon-mnmA.log`. No provider report was fabricated.

The earlier notes are preserved as historical text. Where they describe C5 modification as obligatorily downstream, assert a directly established KT2440 reaction or operon expression, or equate carrier with a catalytic GO descendant, this append and the current review supersede that wording. No NEW annotation was added to fill a core-coverage warning.

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

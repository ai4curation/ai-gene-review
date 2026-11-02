# PDX1 (P16451, YGR193C) notes

Module: `pyruvate_metabolism`, role = PDHX / E3-binding protein (structural adaptor). Not in any YeastCyc reaction (missing from PYRUVDEHYD-PWY gene list).

## Evidence journal
- Structural role [PMID:2007123 "protein X apparently plays a structural role in the PDH complex; i.e., it binds and positions E3 to the E2 core, and this specific binding is essential for a functional PDH complex"]
- pdx1 complex lacks E3 [PMID:2007123 "The PDH complex isolated from the mutant cells contained pyruvate dehydrogenase (E1 alpha + E1 beta) and dihydrolipoamide acetyltransferase (E2) but lacked protein X and dihydrolipoamide dehydrogenase (E3)"]
- Lipoyl domain dispensable [PMID:2007123 "This observation indicates that the lipoyl domain, and its covalently bound lipoyl moiety, is not essential for protein X function"]
- Stoichiometry [PMID:7947791 "The results showed that the E1-E2 subcomplex binds about 12 E3BP monomers attached to 12 E3 homodimers"]
- Matrix, lipoyl + PSBD domains only [UniProt:P16451]

## Decisions
- acyltransferase activity IEA REMOVE (no catalytic domain; non-catalytic subunit). acetyltransferase complex MODIFY to PDH complex.
- Structural molecule activity (IBA/IDA/IMP) ACCEPT; NEW GO:0030674 adaptor (as for human PDHX and the module).

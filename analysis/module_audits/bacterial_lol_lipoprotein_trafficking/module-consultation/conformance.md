# Manual resolution of intentionally unautomated function matches

`input-closure.json` freezes the 17 completed gene core-function records and six
released consultation manifests. All 153 released files were verified against
their manifests before module finalization. The assertions below are scientific
matches, not a claim that the validator parsed free-text chemistry.

| Module role | Reviewed representatives | Positive function support and limit |
|---|---|---|
| LolC subunit | ECOLI P0ADC3, PSEPK Q88KY5 | Core contribution to GO:0140306 in the defined LolCDE assembly. LolC recruitment/interface work is a positive coupled function; not autonomous complete release. Target E. coli architecture and recruitment evidence (PMID:30012603) ground the conserved KT2440 inference. |
| LolE subunit | ECOLI P75958, PSEPK Q88KY3 | Core contribution to GO:0140306 with cargo-anchor/peptide handling supported by structures (PMID:41557797). Complete release belongs to C1/E1/D2. |
| LolF subunit | ACIAD A0ACM8PZZ0 | Exact sequence bridge to the assayed ADP1 LolF supports homodimeric F2/D2 release (PMID:42736309). The gene remains named lolC; it does not imply a heterodimer with a second distinct LolE. |
| LolD ATPase | ECOLI P75957, PSEPK Q88KY4, ACIAD Q9EYM2 | GO:0016887 cores; paired ATPase units drive the corresponding complete extractor. ADP1 Q9EYM2 has verified PTHR42798:SF2 membership, not the E. coli PTHR24220 family. ATPase activity alone does not identify Lol release machinery. |
| LolA carrier | ECOLI P61316, PSEPK Q88FS9, ACIAD Q6F8G3, FLAJ1 A5FI22 | GO:0140598 cores. Evidence ranges from direct transfer/reconstitution to target localization plus specific architecture. The native FLAJ1 phenotype is not purified transfer kinetics. The family review leaves whole-SF1 substrate universality unresolved; only the named positive members and compatible partners support this role. |
| Classical LolB insertion | ECOLI P61320, PSEPK Q88PX4, ACIAD Q6F8J1 | Proposed insertion core functions and classical TIGR00548 identity. Direct E. coli transfer/incorporation grounds target-specific conserved-function inferences; no direct ADP1 terminal-insertion assay is claimed. No fitting GO MF identifier is invented. |
| Distant LolB insertion | FLAJ1 A5FL25 | The distinct PF14125/DUF4292 member has native UW101 localization/complementation support and an inferred insertion core (PMID:40050408). Structural resemblance and native trafficking do not constitute purified insertase kinetics. No PANTHER assignment is guessed. |
| Bifunctional carrier/inserter | CAUVC Q9A261 | Carrier GO:0140598 and proposed insertion cores refer to the same native protein, inferred from construct-bounded work (PMID:36716372). Strong heterologous complementation required an E. coli-compatible terminal replacement and a permissive Δlpp host. Native CB15 flux and a complete native extractor panel are unestablished. |

The 15 NO_FUNCTION_ID warnings concern coupled membrane subfunctions or insertion
chemistry intentionally represented without a false autonomous GO identifier.
The remaining family-function warning reflects a real unresolved universal
scope, not a missing positive named-member review. The Pfam prefix warning is a
validator-configuration limit: the frozen A5FL25 UniProt record explicitly names
Pfam PF14125 / DUF4292. Two ADP1 membership-index warnings are pending the parent's
incremental index refresh; exact official membership/sequence sources were
checked in the released ADP1 and family consultations.

The independent capacity consultation supplies the biological gates that the
production structural compiler does not encode. Conditional LolDE release and
LolAB bypass remain positive observations outside this canonical-profile model;
negative profile outcomes must not be described as biological impossibility.

# PDHA1 (P08559) review notes

Human PDHA1 = pyruvate dehydrogenase E1 component subunit alpha, somatic form, mitochondrial (UniProt RecName, ODPA_HUMAN). Gene HGNC:8806, X-linked. EC 1.2.4.1.

## Verified biology (grounding)

- **E1 alpha subunit of the mitochondrial pyruvate dehydrogenase complex (PDC).** Together with PDHB (E1beta) it forms the heterotetrameric (alpha2-beta2) E1 component. [UniProt SUBUNIT: "Heterotetramer of two PDHA1 and two PDHB subunits."]
- **Reaction / MF:** thiamine-pyrophosphate (TPP)-dependent oxidative decarboxylation of pyruvate followed by reductive acetylation of the E2 lipoyl group. EC=1.2.4.1; RHEA:19189. GO MF = GO:0004739 pyruvate dehydrogenase (acetyl-transferring) activity. [UniProt FUNCTION: "The E1 subunit catalyzes both the thiamine pyrophosphate (TPP)-dependent decarboxylation of pyruvate and the reductive acetylation of a lipoyl group..."]
- **Overall PDC:** pyruvate + CoA + NAD+ -> acetyl-CoA + CO2 + NADH; gateway linking glycolysis to the TCA cycle. [PMID:19081061 full text: "gate-keeper enzyme that strategically links glycolysis to the Krebs cycle and lipogenic pathways"; UniProt "links cytoplasmic glycolysis and the mitochondrial tricarboxylic acid (TCA) cycle".]
- **Cofactors:** thiamine diphosphate (ThDP/TPP) and Mg2+ (also K+ per Reactome). [UniProt COFACTOR; PMID:12651851 holo-structure with Mg2+ and TPP.]
- **Location:** mitochondrial matrix. [UniProt SUBCELLULAR LOCATION: "Mitochondrion matrix".]
- **Regulation:** activity inhibited by phosphorylation of E1alpha at Ser-232/Ser-293/Ser-300 (PDK isozymes; single-site phosphorylation is sufficient to inactivate) and reactivated by dephosphorylation (PDP1/2). [PMID:7782287 abstract "Phosphorylation of each site resulted in complete inactivation of the E1"; PMID:17474719; PMID:19081061; UniProt ACTIVITY REGULATION/PTM.]
- **Disease:** Pyruvate dehydrogenase E1-alpha deficiency (PDHAD, MIM:312170); X-linked; commonest cause of PDC deficiency (~up to 90%); primary lactic acidosis, Leigh syndrome, neurodevelopmental disease. [UniProt DISEASE; dismech KB Pyruvate_Dehydrogenase_Deficiency.yaml "Pyruvate dehydrogenase complex deficiency is in up to 90% caused by pathogenic variants in the X-linked PDHA1 gene."]

## Annotation decisions (summary)

Core catalytic + complex + location + process annotations (GO:0004739, GO:0045254, GO:0005759, GO:0006086) are well supported by structure/biochemistry (PMID:12651851, 17474719, 19081061, 7782287, 24534072, 19240034) and accepted; the strongest experimental MF annotation is EXP/IDA GO:0004739.

- GO:0016624 (IEA, InterPro) is the parent oxidoreductase class of the specific EC-mapped GO:0004739 -> MODIFY (too general; replace with GO:0004739).
- `protein binding` GO:0005515 IPIs: uninformative bare MF term (per curation policy). PMID:12651851 (interactor P11177=PDHB) is the genuine intra-E1 alpha-beta interaction from the crystal structure; PMID:29128334 (PDHB, IMMT), 7782287 (PDK1, Q15118), 29568061 (PDK1 Q15118) reflect real complex/regulator contacts; PMID:33961781/35156780/36012204 are large-scale interactome/CFTR proximity screens. All -> MARK_AS_OVER_ANNOTATED (keep, but not core; more informative terms are complex part_of / MF captured elsewhere). Not REMOVE (experimental IPIs).
- Nucleus GO:0005634 HDA from sperm-nucleus proteomics (PMID:21630459) -> MARK_AS_OVER_ANNOTATED (single high-throughput proteomic detection; not an established site of PDHA1 function; PDHA1 is matrix). Not REMOVE.
- mitochondrion (parent of matrix) IEA/ISS/HDA/HTP/NAS/TAS -> ACCEPT (correct but less specific than matrix) or KEEP_AS_NON_CORE where redundant with matrix.
- Reactome TAS mitochondrial matrix (multiple reaction IDs incl. CLPXP degradation reactions) -> ACCEPT location (matrix correct); the CLPXP reactions reflect PDHA1 as a matrix substrate, location still valid.
- GO:0032991 protein-containing complex (IEA, Ensembl Compara) -> MODIFY to the specific PDC complex GO:0045254 (already annotated).

DR (falcon) not available within the 8-min poll window; grounded in UniProt, GOA, cached publications, Reactome, and the dismech disorder KB.

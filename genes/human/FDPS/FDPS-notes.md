# FDPS (P14324, FPPS_HUMAN) — review notes

## Identity and core function

FDPS encodes **farnesyl pyrophosphate synthase** (farnesyl diphosphate synthase, FPPS; EC 2.5.1.10 and EC 2.5.1.1),
a cytosolic trans-prenyltransferase of the mevalonate/isoprenoid pathway.

- UniProt names the protein "Farnesyl pyrophosphate synthase" with two catalytic activities:
  EC 2.5.1.10 ((2E,6E)-farnesyl diphosphate synthase / geranyltranstransferase) and
  EC 2.5.1.1 (dimethylallyltranstransferase) [file:human/FDPS/FDPS-uniprot.txt "EC=2.5.1.10 {ECO:0000269|PubMed:16684881}" / "EC=2.5.1.1 {ECO:0000269|PubMed:16684881}"].
- FUNCTION: "Key enzyme in isoprenoid biosynthesis which catalyzes the formation of farnesyl diphosphate (FPP),
  a precursor for several classes of essential metabolites including sterols, dolichols, carotenoids, and ubiquinones.
  FPP also serves as substrate for protein farnesylation and geranylgeranylation. Catalyzes the sequential
  condensation of isopentenyl pyrophosphate with the allylic pyrophosphates, dimethylallyl pyrophosphate, and then
  with the resultant geranylpyrophosphate to the ultimate product farnesyl pyrophosphate."
  [file:human/FDPS/FDPS-uniprot.txt, CC FUNCTION block].
- Two catalytic-activity RHEA reactions in UniProt: IPP + DMAPP = GPP + diphosphate (RHEA:22408, EC 2.5.1.1);
  IPP + GPP = (2E,6E)-FPP + diphosphate (RHEA:19361, EC 2.5.1.10) [file:human/FDPS/FDPS-uniprot.txt].
- COFACTOR: Mg(2+); "Binds 2 Mg(2+) ions per subunit." [file:human/FDPS/FDPS-uniprot.txt, ECO:0000269|PubMed:19309137].
- PATHWAY: "Isoprenoid biosynthesis; farnesyl diphosphate biosynthesis; farnesyl diphosphate from geranyl diphosphate
  and isopentenyl diphosphate: step 1/1." and "Isoprenoid biosynthesis; geranyl diphosphate biosynthesis; geranyl
  diphosphate from dimethylallyl diphosphate and isopentenyl diphosphate: step 1/1." [file:human/FDPS/FDPS-uniprot.txt].
- SUBUNIT: "Homodimer." [file:human/FDPS/FDPS-uniprot.txt]. Consistent with the many "FDPS dimer" Reactome reactions.
- SUBCELLULAR LOCATION: "Cytoplasm." (only location recorded) [file:human/FDPS/FDPS-uniprot.txt].

## Experimental evidence for catalysis (EC 2.5.1.1 / 2.5.1.10)

[PMID:16684881 "The molecular mechanism of nitrogen-containing bisphosphonates as antiosteoporosis drugs"] —
abstract-only in cache (`full_text_available: false`). Establishes human FPPS as the bisphosphonate target and
states: "FPPS, a key branchpoint of the mevalonate pathway, catalyzes the successive condensation of isopentenyl
pyrophosphate with dimethylallyl pyrophosphate and geranyl pyrophosphate." High-resolution X-ray structures of the
human enzyme with risedronate and zoledronate; kinetics show inhibition competitive with GPP. UniProt cites this
PMID (ECO:0000269) for both catalytic activities. This is the basis for the EXP MF annotations (GO:0004161, GO:0004337).

## Bisphosphonate target (pharmacology)

Nitrogen-containing bisphosphonates (alendronate, risedronate, zoledronate, etc.) inhibit FPPS by binding the
allylic (DMAPP/GPP) substrate pocket and mimicking a carbocation intermediate [PMID:16684881, abstract]. Many bound
structures in the PDB (>90 entries) and DrugBank entries (Alendronic acid DB00630, Risedronic acid DB00884, Zoledronic
acid DB00399, etc.) [file:human/FDPS/FDPS-uniprot.txt, DR DrugBank lines]. Not a GO annotation per se but confirms
the enzyme identity/active site.

## Disease

POROK9 (porokeratosis 9, multiple types; MIM:616631): autosomal disorder of keratinization; variant R179Q reported
[file:human/FDPS/FDPS-uniprot.txt, DISEASE block; VARIANT 179 R->Q; ECO:0000269|PubMed:26202976]. Mevalonate-pathway
gene variants underlie porokeratosis. Not an existing GO annotation in the GOA set.

## Regulation / interactions

- ACTIVITY REGULATION: "Inactivated by interferon-induced RSAD2" (viperin); may disrupt lipid rafts, antiviral effect
  [file:human/FDPS/FDPS-uniprot.txt, ECO:0000269|PubMed:18005724].
- Interacts with HTLV-1 p13(II) (microbial infection) [file:human/FDPS/FDPS-uniprot.txt, PubMed:11773414].
- High-throughput IntAct binary interactions (ATXN1, ABHD16A, RNF19B, SSMEM1, SLC30A2) underlie the six
  GO:0005515 "protein binding" IPI annotations in GOA (PMID:16713569, PMID:32296183, PMID:32814053).

## RNA binding (moonlighting candidate)

[PMID:22658674 "Insights into RNA biology from an atlas of mammalian mRNA-binding proteins"] — abstract-only in cache.
Proteome-wide "interactome capture" in HeLa; "We identify 860 proteins that qualify as RBPs by biochemical and
statistical criteria," including many metabolic enzymes. FDPS was among captured proteins → HDA GO:0003723 RNA binding
annotation. No FDPS-specific RNA-dependent function known; kept as non-core.

## Curation decisions (summary)

Core molecular functions (EC 2.5.1.10 GO:0004337; EC 2.5.1.1 GO:0004161) supported by EXP (PMID:16684881), IBA, and
IEA — all ACCEPT. Core BP (farnesyl-PP biosynthesis GO:0045337; geranyl-PP biosynthesis GO:0033384; isoprenoid
biosynthesis GO:0008299) and location (cytosol GO:0005829; cytoplasm GO:0005737) — ACCEPT. Redundancy across evidence
types is not treated as over-annotation.

Over-annotations (MARK_AS_OVER_ANNOTATED): generic parent MF terms GO:0004659 prenyltransferase activity and
GO:0016765 (transferase, alkyl/aryl); the six bare GO:0005515 protein-binding IPIs; and GO:0005759 mitochondrial
matrix (IBA) — the human protein's only curated location is cytoplasm (UniProt), and the mitochondrial-matrix IBA
comes from a distinct PANTHER sub-branch (PTN000897621, fly/rat orthologs), not the human FPPS node (PTN000162949);
documented via propagation_review (PROPAGATION_BAD / COMPARTMENT_OR_COMPLEX_MISMATCH).

Non-core (KEEP_AS_NON_CORE): GO:0006695 cholesterol biosynthetic process (IEA + TAS PMID:2690933) — FDPS provides the
FPP precursor but the dedicated sterol reactions are downstream; GO:0003723 RNA binding (HDA) — high-throughput
moonlighting candidate.

No experimental (IDA/IMP/IPI/EXP) annotation was REMOVEd; no IEA was removed either (all were either correct core,
correct-but-general, or contributory).

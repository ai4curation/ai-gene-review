# COQ8B (ADCK4) review notes

UniProt: Q96D53 (COQ8B_HUMAN). Gene: COQ8B; synonym ADCK4 (AarF domain-containing kinase 4). HGNC:19041.
Taxon: Homo sapiens (NCBITaxon:9606). 544 aa; two isoforms (Q96D53-1 displayed, Q96D53-2 lacks 123-163).

## Identity and family
- RecName in UniProt: "Atypical kinase COQ8B, mitochondrial"; EC=2.7.-.- (ECO:0000269|PubMed:38425362) [file:human/COQ8B/COQ8B-uniprot.txt].
- Member of the protein kinase superfamily, ADCK protein kinase family (UbiB family of atypical/protein-kinase-like enzymes). SIMILARITY: "Belongs to the protein kinase superfamily. ADCK protein kinase family." [file:human/COQ8B/COQ8B-uniprot.txt].
- One of five human UbiB/ADCK members (ADCK1-5); ADCK4/COQ8B is the closest paralog of ADCK3/COQ8A. Both are co-orthologs of yeast Coq8p [PMID:27499294 "Based on phylogenetic analyses defining ADCK3 and ADCK4 as co-orthologs of yeast Coq8p ... we propose to rename ADCK3 and ADCK4 as COQ8A and COQ8B, respectively."].

## Molecular function — the atypical-kinase question
- Adopts an atypical protein kinase-like fold; the KxGQ motif (155-158) occludes the canonical substrate-binding pocket; nucleotide binding relieves this autoinhibition [file:human/COQ8B/COQ8B-uniprot.txt DOMAIN and ACTIVITY REGULATION blocks].
- ATP binding is supported: multiple ATP BINDING sites annotated (219, 237, 324-327, 372, 386; ECO:0000250 from COQ8A/Q8NI60); KW ATP-binding, Nucleotide-binding; GO:0005524 ATP binding IEA (UniProtKB-KW). Consistent with the nucleotide-gated mechanism.
- Direct in vitro demonstration that COQ8B phosphorylates the COQ metabolon enzyme COQ3 (protein-kinase activity), but is NOT a small-molecule/lipid kinase:
  - [PMID:38425362 "We therefore hypothesized that COQ8B could act as a COQ3 kinase"]
  - [PMID:38425362 "COQ3, but not COQ6, is phosphorylated by COQ8B at multiple sites"]
  - [PMID:38425362 "GC/MS analyses did not detect any phosphorylated CoQ intermediates, suggesting that the enzyme is not a small-molecule kinase"]
  - This is the basis for the UniProt EC=2.7.-.- (PubMed:38425362) and the GO:0004672 protein kinase activity IDA (PMID:38425362).
- The paralog/family-level work (COQ8A/yeast Coq8p) previously found NO canonical protein kinase activity in trans, and ATPase activity instead:
  - [PMID:27499294 "we demonstrate that it lacks canonical protein kinase activity in trans. Instead, COQ8 has ATPase activity and interacts with lipid CoQ intermediates"]
  - This underpins the NOT protein kinase activity / NOT protein phosphorylation annotations attributed to COQ8B via PMID:27499294, and the ATP hydrolysis activity (GO:0016887) ISS annotation.
- Interpretation: the field has moved from "no protein kinase activity (2016, in trans, COQ8A)" to a specific, ATP-dependent COQ3 protein-kinase activity for COQ8B (2024). Both the NOT (protein kinase, in trans, family-level) and the positive IDA (COQ3-specific, COQ8B) annotations are legitimately in GOA and are kept; they describe different assays. Represent MF conservatively as ATP binding + (atypical) protein kinase activity; do NOT assert a small-molecule/lipid kinase MF (explicitly refuted for COQ8B in PMID:38425362).
- UniProt FUNCTION hedges: "may act as a protein kinase that mediates phosphorylation of COQ3 (PubMed:38425362)"; a By-similarity lipid-kinase possibility is noted but "the small molecule kinase activity was not confirmed by another publication (PubMed:38425362)" [file:human/COQ8B/COQ8B-uniprot.txt].

## Biological process
- Required for coenzyme Q10 (ubiquinone) biosynthesis; stabilizes/regulates the COQ metabolon ("complex Q"/CoQ synthome).
  - [PMID:24270420 "Mutations in ADCK4 resulted in reduced CoQ10 levels and reduced mitochondrial respiratory enzyme activity in cells isolated from individuals with SRNS"]
  - PATHWAY: "Cofactor biosynthesis; ubiquinone biosynthesis." [file:human/COQ8B/COQ8B-uniprot.txt].
  - GO:0006744 ubiquinone biosynthetic process has IDA (PMID:38425362), IMP (PMID:27499294), IBA and IEA support — well supported, core BP.
- Required for podocyte migration [file:human/COQ8B/COQ8B-uniprot.txt "Required for podocyte migration (PubMed:24270420)."; PMID:24270420 "Knockdown of ADCK4 in podocytes resulted in decreased migration, which was reversed by CoQ10 addition."]. This is a downstream/tissue-level consequence of the CoQ role, not a distinct core molecular function.

## Localization
- Mitochondrion / mitochondrial (inner) membrane, matrix face; also reported at cytosol and plasma/cell membrane (single-pass membrane protein).
  - SUBCELLULAR LOCATION: "Mitochondrion membrane ...; Single-pass membrane protein. Cytoplasm, cytosol. Cell membrane." [file:human/COQ8B/COQ8B-uniprot.txt].
  - [PMID:24270420 "ADCK4 was expressed in glomerular podocytes and partially localized to podocyte mitochondria and foot processes"] — supports both mitochondrial and cell-membrane/foot-process localization.
  - GO:0005739 mitochondrion IDA (PMID:33988507, HPA GO_REF:0000052) and HTP (PMID:34800366); GO:0031966 mitochondrial membrane EXP (PMID:24270420, PMID:33988507). Core location = mitochondrial (inner) membrane. Cytosol (GO:0005829 IEA) and plasma membrane (GO:0005886 IEA/EXP) are supported by the record but are non-core/minor pools.

## Interactions
- Homodimer (via transmembrane region) [PMID:25216398, cited in UniProt SUBUNIT].
- Interacts with COQ6 and COQ7 [file:human/COQ8B/COQ8B-uniprot.txt "Interacts with COQ6 and COQ7 (PubMed:24270420)."].
- Interacts with the multi-subunit COQ enzyme complex (COQ3, COQ4, COQ5, COQ6, COQ7, COQ9) [PMID:27499296, cited in UniProt SUBUNIT].

## Disease
- Nephrotic syndrome 9 (NPHS9; MIM:615573) / primary CoQ10 deficiency-9 — steroid-resistant nephrotic syndrome (SRNS) with focal segmental glomerulosclerosis (FSGS); adolescence/adult onset in some cohorts.
  - [PMID:24270420 "we identified mutations in the aarF domain containing kinase 4 (ADCK4) gene in 15 individuals with SRNS from 8 unrelated families"]
  - [PMID:25967120] ADCK4-associated glomerulopathy causes adolescence-onset FSGS (cited in UniProt DISEASE/VARIANT blocks).
  - Some patients respond partially to CoQ10 supplementation [PMID:24270420 "a patient with SRNS with a homozygous ADCK4 frameshift mutation had partial remission following CoQ10 treatment"].

## Annotation-review decisions (summary)
- GO:0004672 protein kinase activity IDA (PMID:38425362): ACCEPT — direct COQ3 phosphorylation; core (atypical) MF.
- GO:0006744 ubiquinone biosynthetic process (IDA PMID:38425362; IMP PMID:27499294; IBA; IEA UniPathway): ACCEPT the experimental ones; core BP. Keep IEA/IBA as ACCEPT (redundant but correct).
- GO:0005524 ATP binding — not seeded as a separate existing annotation row in GOA TSV? It IS in the UniProt DR block (IEA KW) but not in the GOA TSV rows; added as core MF (supported by UniProt ATP-binding sites + nucleotide-gated mechanism). (See core_functions.)
- GO:0031966 mitochondrial membrane (EXP PMID:24270420, PMID:33988507; IEA): ACCEPT; core location.
- GO:0005739 mitochondrion (IDA PMID:33988507; HPA IDA; HTP PMID:34800366): ACCEPT (mitochondrial localization).
- GO:0005829 cytosol IEA (SubCell): KEEP_AS_NON_CORE — record-supported minor pool, not the core site of action.
- GO:0005886 plasma membrane (IEA SubCell; EXP PMID:24270420): KEEP_AS_NON_CORE — podocyte foot-process/cell-membrane pool; supported but non-core relative to mitochondrial CoQ role.
- GO:0008289 lipid binding ISS (FlyBase, from UniProtKB:P27697): KEEP_AS_NON_CORE — CoQ-intermediate/lipid interaction is real for the family, but this is an inferred binding property, not the core catalytic MF; keep, non-core. (Do NOT REMOVE — ISS w/ biological support.)
- GO:0016887 ATP hydrolysis activity ISS (FlyBase, from P27697): KEEP_AS_NON_CORE — ATPase activity demonstrated for COQ8A/Coq8p (PMID:27499294) and consistent with the atypical-kinase mechanism; keep as supporting/non-core MF (the physiologically relevant catalytic output for COQ8B is COQ3 phosphorylation).
- GO:0004672 protein kinase activity NOT|enables IDA (PMID:27499294): ACCEPT the negation as recorded — no canonical protein kinase activity in trans (family-level assay). Retained as a NOT annotation; not core.
- GO:0006468 protein phosphorylation NOT|involved_in IDA (PMID:27499294): ACCEPT the negation as recorded (no canonical trans phosphorylation of general substrates). Note tension with the specific COQ3 phosphorylation (PMID:38425362); the NOT refers to general/in-trans protein kinase behaviour.
- GO:0021692 cerebellar Purkinje cell layer morphogenesis IMP (PMID:27499294): MARK_AS_OVER_ANNOTATED — the Purkinje-cell phenotype in PMID:27499294 is the mouse *Coq8a* (COQ8A, ADCK3) knockout, not COQ8B; COQ8B disease is renal (SRNS/FSGS), not cerebellar. Experimental IMP so per policy NOT removed; flagged as mis-attributed to the paralog / over-annotation.

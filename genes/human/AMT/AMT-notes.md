# AMT (Aminomethyltransferase, mitochondrial) — review notes

UniProt: P48728 (GCST_HUMAN). Gene AMT / GCST. HGNC:473. EC 2.1.2.10.
403 aa precursor; residues 1-28 mitochondrial transit peptide; mature chain 29-403.
Belongs to the GcvT family. PANTHER PTHR43757:SF16 (AMINOMETHYLTRANSFERASE, MITOCHONDRIAL).

## Function (verified)

AMT is the **T-protein (aminomethyltransferase)** of the mitochondrial **glycine cleavage
system (GCS)**, a four-protein multienzyme complex: P-protein (GLDC), T-protein (AMT),
L-protein (DLD), and H-protein (GCSH). The GCS catalyses the reversible oxidative
decarboxylation/degradation of glycine.

AMT catalyses the **third step**: it acts on the aminomethyl (methylamine) moiety of glycine
that is carried, after decarboxylation, on the reduced lipoate arm of H-protein
(the aminomethyl-dihydrolipoyl-GCSH intermediate). AMT **releases ammonia (NH3)** and
**transfers the remaining one-carbon (methylene) unit to tetrahydrofolate (THF), forming
(6R)-5,10-methylenetetrahydrofolate (5,10-CH2-THF)**, leaving GCSH in its dihydrolipoyl
(reduced-lipoate) form, which is subsequently reoxidised by the L-protein (DLD).
This THF-dependent reaction couples glycine catabolism to one-carbon/folate metabolism.

Catalytic activity (UniProt/RHEA:16945; EC 2.1.2.10):
N6-[(R)-S8-aminomethyldihydrolipoyl]-L-lysyl-[protein] + (6S)-5,6,7,8-tetrahydrofolate
= N6-[(R)-dihydrolipoyl]-L-lysyl-[protein] + (6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + NH4(+)

[PMID:16051266 "T-protein, a component of the glycine cleavage system, catalyzes the formation of ammonia and 5,10-methylenetetrahydrofolate from the aminomethyl moiety of glycine attached to the lipoate cofactor of H-protein"]

Reactome R-HSA-5693977 ("AMT transfers NH2CH2 from GCSH:SAMDLL to THF") describes the same
reaction: AMT degrades the H-protein-bound aminomethyl moiety to ammonia + GCSH-reduced-lipoate,
with THF accepting the one-carbon unit to form 5,10-MTHF.

## Localisation (verified)

Mitochondrion / mitochondrial matrix. Nuclear-encoded, imported via an N-terminal transit
peptide (aa 1-28). Present in the high-confidence human mitochondrial proteome (MitoCoP,
PMID:34800366). UniProt: "SUBCELLULAR LOCATION: Mitochondrion".

## Structure (verified)

2.0 A crystal structure of human T-protein, free and bound to 5-CH3-THF (PDB 1WSR/1WSV;
PMID:16051266). Cloverleaf three-domain fold with a central folate-binding cavity; substrate
binding residues (UniProt BINDING 232, 261, 399). Disease residues cluster around the cavity.

## Disease (verified)

Deficiency of AMT causes **nonketotic hyperglycinemia (NKH) / glycine encephalopathy**
(Glycine encephalopathy 2, GCE2; MIM:620398), the second most common cause after GLDC
(P-protein). ~80% of NKH is GLDC (P-protein); the remainder are largely T-protein (AMT).
Many pathogenic missense variants (H42R, G47R, R94W, N145I, E211K, R222C, R265C, G269D,
D276H, R296C, R320H) reduce/abolish aminomethyltransferase activity.

[PMID:9600239 "Nonketotic hyperglycinemia (NKH) is caused by a mutation in the genes encoding the components of the glycine cleavage multi-enzyme system"]
[PMID:9600239 "T-protein activity was deficient in the liver specimen from one propositus"]

## Annotation review summary

- MF: GO:0004047 aminomethyltransferase activity — ACCEPT (multiple lines: EXP, IMP
  PMID:16051266; IBA; IEA EC/RHEA). This is the core molecular function.
- BP: GO:0019464 glycine decarboxylation via glycine cleavage system (IBA, IMP) and
  GO:0006546 glycine catabolic process (IEA, TAS) — ACCEPT. Core process.
- CC: GO:0005739 mitochondrion (IBA/IEA/IDA/HTP/IC/TAS) and GO:0005759 mitochondrial matrix
  (TAS) — ACCEPT. GO:0005960 glycine cleavage complex (IEA InterPro, part_of) — ACCEPT;
  T-protein is a constituent of the GCS complex.
- transaminase / aminotransferase keyword (GO:0008483) appears in UniProt DR line
  (IEA:UniProtKB-KW) from the "Aminotransferase" keyword but is NOT in the seeded GOA TSV,
  so it is not reviewed as an existing annotation. AMT is an aminomethyltransferase, not a
  classic PLP transaminase; the keyword-derived transaminase term would be an over-annotation
  if present.

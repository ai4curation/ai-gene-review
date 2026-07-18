# NANS (Q9NR45) — review notes

## Identity
- UniProt: Q9NR45, `SIAS_HUMAN`, 359 aa, gene symbol **NANS** (HGNC:19237), synonym **SAS**.
- RecName: **N-acetylneuraminate-9-phosphate synthase** (EC 2.5.1.57); AltName **3-deoxy-D-glycero-D-galacto-nononate 9-phosphate synthase** (EC 2.5.1.132); AltName **Sialic acid synthase / Sialic acid phosphate synthase**.
  - [file:human/NANS/NANS-uniprot.txt "RecName: Full=N-acetylneuraminate-9-phosphate synthase"]
  - [file:human/NANS/NANS-uniprot.txt "EC=2.5.1.57"] and [file:human/NANS/NANS-uniprot.txt "EC=2.5.1.132"]

## Core molecular function
NANS catalyzes the committed condensation step of de novo sialic acid (Neu5Ac) biosynthesis:
condensation of **phosphoenolpyruvate (PEP)** with **N-acetylmannosamine 6-phosphate (ManNAc-6-P)** to
form **N-acetylneuraminate 9-phosphate (Neu5Ac-9-P)**.
- UniProt FUNCTION: [file:human/NANS/NANS-uniprot.txt "Catalyzes the condensation of phosphoenolpyruvate (PEP) and"] / [file:human/NANS/NANS-uniprot.txt "acetylneuraminate-9-phosphate (Neu5Ac-9-P) (PubMed:10749855)."]
- It also condenses PEP with **D-mannose 6-phosphate (Man-6-P)** to make **KDN-9-P** (deaminoneuraminic acid 9-phosphate), but with much lower activity toward the non-acetyl product.
  - [file:human/NANS/NANS-uniprot.txt "catalyzes the condensation of PEP and D-mannose 6-phosphate (Man-6-P)"]
  - Primary characterization: [PMID:10749855 "In vitro the human enzyme uses N-acetylmannosamine 6-phosphate and mannose 6-phosphate as substrates to generate phosphorylated forms of Neu5Ac and KDN, respectively, but exhibits much higher activity toward the Neu5Ac phosphate product."]
- The enzyme complements a *neuB*-negative *E. coli* mutant (homolog of bacterial sialic acid synthase NeuB).
  - [PMID:10749855 "The gene partially restores sialic acid synthase activity in a neuB-negative mutant of E. coli"]

### Important CAUTION (do not over-annotate)
UniProt explicitly notes NANS does **NOT** have "sialic acid synthase activity" acting on the
non-phosphorylated substrates ManNAc / mannose (i.e. it is a *phosphate* synthase, not the
ManNAc→Neu5Ac reaction, EC of GO:0050462).
- [file:human/NANS/NANS-uniprot.txt "Does not exhibit sialic acid synthase activity, which"] / [file:human/NANS/NANS-uniprot.txt "acetylmannosamine (ManNAc) and mannose, respectively."]
- Therefore the correct MF term is **GO:0047444 N-acylneuraminate-9-phosphate synthase activity** (EC 2.5.1.57, reaction: PEP + ManNAc-6-P + H2O = Neu5Ac-9-P + phosphate), NOT **GO:0050462 N-acetylneuraminate synthase activity** (the ManNAc→Neu5Ac reaction). GO:0047444 def (go.db): "Catalysis of the reaction: H2O + phosphoenolpyruvate + N-acyl-D-mannosamine 6-phosphate = phosphate + N-acylneuraminate 9-phosphate." N-acyl generalizes over N-acetyl, and also accommodates the KDN-9-P (EC 2.5.1.132) side activity.

## Biological process
De novo sialic acid biosynthesis (5 steps: GNE → NANS → NANP → CMAS → …). NANS is the sialic-acid-synthase step.
- NANS KO in human cell lines reduces cell-surface sialylation and dramatically reduces CMP-sialic acid.
  - [PMID:31121216 "Sialylation of cell surface glycans was reduced by KO of GNE (UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase), NANS (sialic acid synthase) and CMAS (N-acylneuraminate cytidylyltransferase) genes"]
  - [PMID:31121216 "CMP-sialic acid was dramatically reduced in GNE and NANS KO cells and undetectable in CMAS KO."]
- Pathway context: [PMID:31121216 "Biosynthesis of CMP-sialic acid, the essential substrate, comprises five enzymatic steps, involving ManNAc and sialic acid and their phosphorylated forms as intermediates."]
- Core BP term: **GO:0046380 N-acetylneuraminate biosynthetic process** (direct product path). GO:0006054 (N-acetylneuraminate metabolic process) is the more general parent (metabolic ⊃ biosynthetic; confirmed via go.db entailed_edge: GO:0046380 is-a GO:0006054).
- CMP-N-acetylneuraminate biosynthetic process (GO:0006055): NANS acts upstream of the cytidylyltransferase (CMAS) step; its loss abolishes CMP-Neu5Ac, so involvement is defensible but is the *pathway product* rather than NANS's own catalytic step. Kept as non-core.

## Location
- Cytosolic enzyme. UniProt keyword set + Reactome place NANS in cytosol.
- **GO:0005829 cytosol** (Reactome TAS; ARBA IEA) — accept; consistent with a soluble cytosolic metabolic enzyme.
- **GO:0005737 cytoplasm** (NAS, PMID:10749855) — accept as non-core (less specific than cytosol).
- **GO:0005654 nucleoplasm** (IDA, HPA immunofluorescence, GO_REF:0000052) — over-annotation; NANS is a cytosolic sialic-acid-synthesis enzyme with no known nuclear role. HPA IF localizations frequently over-call nucleoplasm. Mark as over-annotated (IDA → keep in record, not REMOVE).
- **GO:0070062 extracellular exosome** (HDA, PMID:23533145) — high-throughput mass-spec detection in urinary prostatic-secretion exosomes; a common HTP contaminant/co-purification for abundant cytosolic enzymes. Not a functional location. Mark as over-annotated.

## Disease
- **NANS-CDG / Spondyloepimetaphyseal dysplasia, Genevieve type (SEMDG, MIM:610442)**: autosomal recessive, infantile-onset global developmental delay, intellectual disability, skeletal dysplasia, short stature.
  - [file:human/NANS/NANS-uniprot.txt "An autosomal recessive disorder characterized by global"] / [file:human/NANS/NANS-uniprot.txt "developmental delay with infantile onset, intellectual disability,"]
  - [file:human/NANS/NANS-uniprot.txt "Required for brain and skeletal development (PubMed:27213289)."]
- Biallelic loss-of-function/missense variants (e.g. p.His29Asn, p.Gly133Val, p.Arg151His, p.Tyr188His, p.Pro189Leu, p.Arg237Cys) documented in UniProt VARIANT lines (PubMed:27213289). Patients accumulate N-acetylmannosamine (upstream substrate).

## Structure / domains
- Two-domain architecture: N-terminal (β/α)8 TIM-barrel catalytic domain (Aldolase class I / NeuB Pfam PF03102) + C-terminal antifreeze-like (AFP-like) / SAF domain (Pfam PF08666), residues 294–353.
- NMR structure of the C-terminal AFP-like domain: PDB 1WVO (PMID:16597820, "Solution structure of the antifreeze-like domain of human sialic acid synthase").
- PANTHER: PTHR42966:SF1 "SIALIC ACID SYNTHASE".

## Annotation action summary (14 GOA rows)
| Term | Evidence | Action | Rationale |
|---|---|---|---|
| GO:0047444 MF | IBA (GO_REF:33) | ACCEPT | phylogenetic; correct core MF |
| GO:0006054 N-acetylneuraminate metabolic process | IEA (ARBA) | KEEP_AS_NON_CORE | general parent of core BP |
| GO:0016051 carbohydrate biosynthetic process | IEA (InterPro) | KEEP_AS_NON_CORE | high-level, correct but generic |
| GO:0047444 MF | IEA (ARBA/RHEA/EC:2.5.1.57) | ACCEPT | matches EC 2.5.1.57 |
| GO:0005829 cytosol (is_active_in) | IEA (ARBA) | ACCEPT | correct location |
| GO:0047444 MF | TAS (Reactome) | ACCEPT | correct core MF |
| GO:0005654 nucleoplasm | IDA (HPA) | MARK_AS_OVER_ANNOTATED | HPA IF over-call; no nuclear role (never REMOVE IDA) |
| GO:0006055 CMP-Neu5Ac biosynthetic process | IMP (PMID:31121216) | KEEP_AS_NON_CORE | downstream pathway product |
| GO:0046380 N-acetylneuraminate biosynthetic process | IMP (PMID:31121216) | ACCEPT | core BP |
| GO:0047444 MF | IDA (PMID:10749855) | ACCEPT | primary experimental characterization |
| GO:0006055 CMP-Neu5Ac biosynthetic process | NAS (PMID:10749855) | KEEP_AS_NON_CORE | author statement, pathway-level |
| GO:0070062 extracellular exosome | HDA (PMID:23533145) | MARK_AS_OVER_ANNOTATED | HTP MS co-purification (never REMOVE HDA) |
| GO:0005829 cytosol (located_in) | TAS (Reactome) | ACCEPT | correct location |
| GO:0005737 cytoplasm | NAS (PMID:10749855) | KEEP_AS_NON_CORE | less specific than cytosol |

## Core functions (for review)
- MF: **GO:0047444 N-acylneuraminate-9-phosphate synthase activity** (with inputs ManNAc-6-P + PEP → Neu5Ac-9-P).
- BP: **GO:0046380 N-acetylneuraminate biosynthetic process**.
- Location: **GO:0005829 cytosol**.
</content>
</invoke>

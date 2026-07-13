# ATP5F1D (P30049) review notes

## Identity and core biology
- ATP5F1D = ATP synthase F(1) complex subunit delta, mitochondrial (formerly ATP5D). HGNC:837.
- Delta (δ) subunit of the **F1 catalytic head / central stalk** of mitochondrial ATP synthase (Complex V, F1Fo-ATP synthase).
- The central stalk = subunits γ (ATP5F1C), δ (ATP5F1D), ε (ATP5F1E). It rotates inside the F1 α3β3 catalytic core and couples proton flow through Fo to ATP synthesis.
- **Non-catalytic / structural subunit.** The catalytic nucleotide-binding sites are on the alpha (ATP5F1A) and beta (ATP5F1B) subunits. The metazoan mitochondrial "delta" subunit is homologous to the **bacterial epsilon subunit** ("Belongs to the ATPase epsilon chain family" — UniProt). This is a rotor/central-stalk subunit, distinct from the bacterial delta (= mitochondrial OSCP/ATP5PO peripheral-stalk subunit).
- Localises to the **mitochondrial inner membrane** (GO:0005743) as part of the F1 sector projecting into the matrix.
- Disease: biallelic mutations cause Mitochondrial complex V (ATP synthase) deficiency, nuclear type 5 (MC5DN5; MIM:618120), AR.

## Key evidence
- [PMID:29478781 "important role in coupling proton translocation and ATP production."] — establishes ATP5F1D as ATP-synthesis-coupling subunit; patient fibroblasts "exhibited impaired assembly of F1FO ATP synthase and subsequent reduced complex V activity". Drosophila ATPsynδ knockdown lethal, rescued by WT human ATP5F1D but not by disease variants → basis for the GO:0009060 aerobic respiration (IMP) and GO:0033615 assembly (IMP) annotations. iPSC-cardiomyocytes showed "impaired maximal respiration".
- [PMID:29499186 "The central stalk of mitochondrial ATP synthase consists of subunits γ, δ, and ε, and along with the membraneous subunit c oligomer constitutes the rotor domain of the enzyme."] — shRNA knockdown of δ reduced assembled ATP synthase and ATP synthase function; "similar phenotype of γ, δ and ε subunit deficiencies suggest uniform requirement for assembled central stalk as driver of the c-oligomer attachment in the assembly process". Basis for GO:0005198 structural molecule activity (IDA) and GO:0033615 assembly (IDA).
- [PMID:37244256 "Structure of the human ATP synthase."] — cryo-EM structure identifies subunit delta in the F1/central stalk; basis for GO:0045259 complex membership (IDA) and understanding of the rotary mechanism.
- [PMID:12110673] — functionally active human F1Fo ATPase immunocaptured; complex V displayed oligomycin/IF1-sensitive ATP hydrolysis. Basis for older IDA complex-membership and rotary-mechanism (contributes_to) annotations.
- UniProt FUNCTION: "In vivo, can only synthesize ATP although its ATP hydrolase activity can be activated artificially in vitro" — core BP is ATP synthesis, not hydrolysis.

## Annotation strategy
- Core CC: GO:0045259 proton-transporting ATP synthase complex (current GOA term; ComplexPortal CPX-6151). Anatomical: GO:0005743 mitochondrial inner membrane.
- Core BP: GO:0042776 proton motive force-driven mitochondrial ATP synthesis / GO:0015986 proton motive force-driven ATP synthesis (accept both; 42776 is the mitochondrial-specific child).
- Core MF: GO:0005198 structural molecule activity (IDA, PMID:29499186) — the correct MF for a non-catalytic structural subunit. contributes_to GO:0046933 (rotational ATP synthase activity) is acceptable at the complex level.
- Over-annotations to flag:
  - GO:0005515 protein binding (IPI) x4 lines: keep as non-core / over-annotated (bare protein binding; most partners are non-mitochondrial high-throughput hits; ATP5F1E/P56381 is the one genuine complex partner). Not REMOVE (experimental IPI policy).
  - GO:0005524 ATP binding / GO:0043531 ADP binding (contributes_to, NAS from copper review PMID:12539966): delta does not bind nucleotides — those sites are on alpha/beta. NAS from a copper-nutrition review, not a structural determination. MARK_AS_OVER_ANNOTATED.
  - GO:0046688 response to copper ion (NAS, PMID:12539966): copper-deficiency review reports decreased delta-subunit protein as a downstream effect; not a direct function of ATP5F1D. MARK_AS_OVER_ANNOTATED.
  - GO:0005759 mitochondrial matrix (TAS Reactome) x4: the F1 head projects into the matrix, so defensible, but the curated anatomical location is inner membrane; keep as non-core.
  - GO:0005739 mitochondrion (several IEA/IDA/HTP/IC/NAS): correct but non-specific; accept broad, prefer inner membrane as specific.

## Interactor identities (IntAct IPI with/from)
- P56381 = ATP5F1E (epsilon) — genuine central-stalk complex partner.
- P54253 = ATXN1; P60410 = KRTAP10-8; Q99750 = MDFI; P0DPK4 = NOTCH2NLC; Q05519-2 = SRSF11; Q63HR2 = TNS2 — nuclear/cytoplasmic proteins, high-throughput Y2H/AP-MS; not established as biologically meaningful complex-V interactions.

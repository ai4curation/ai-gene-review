# A0A2U1PS28 (Artemisia annua, CTI12_AA119750) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Identity and gene model
- UniProt A0A2U1PS28 (TrEMBL, PE 3), 661 aa, ORF CTI12_AA119750. Complete gene model with all LepA
  domains and an N-terminal extension (~60 aa beyond E. coli LepA) with transit-peptide-like
  composition (no D/E, 22% S/T, 10 K/R in first 60 aa). Not a fragment or isoform
  [file:ARTAN/A0A2U1PS28/A0A2U1PS28-bioinformatics/RESULTS-rereview.md].
- UniProt names it "Translation factor GUF1 homolog, mitochondrial" via HAMAP MF_03137 (mitochondrial
  GUF1 rule, UniRule UR000376609). The Arabidopsis chloroplast ortholog Q9FNM5 is instead annotated
  through UniRule UR000376359 (chloroplastic rule; QuickGO query 2026-10-21). The mitochondrial name and
  mitochondrial GO rows on A0A2U1PS28 are a rule misassignment.

### Evolutionary placement
- PANTHER PTHR43512:SF4 "TRANSLATION FACTOR GUF1 HOMOLOG, CHLOROPLASTIC", the subfamily holding
  bacterial LepA (E. coli P60785) and plant cpLEPA (Arabidopsis Q9FNM5, At5g08650; rice B9F2U5).
  Mitochondrial GUF1 (yeast P46943, human Q8N442, Arabidopsis Q9FLE4) are SF7.
- Pairwise identity: 82.9% to Arabidopsis cpLEPA, 55.6% to E. coli LepA, 43-50% to the SF7
  mitochondrial GUF1s.
- PAINT (interpro/panther/PTHR43512/PTHR43512-paint.tsv): mitochondrion GO:0005739 is placed at the
  eukaryotic node PTN000563148 (yeast/trypanosome/worm seeds); the target did not inherit it. Ribosome
  binding and positive regulation of translation sit at PTN002460656 (seeds yeast Guf1 and E. coli
  LepA), which spans both subfamilies, so those two terms are legitimately inherited.

### Literature on the characterised ortholog (Arabidopsis cpLEPA)
- [PMID:23166764 "promotes the efficiency of chloroplast protein synthesis"]; cplepa-1 mutants pale,
  reduced chloroplast protein synthesis by in vivo labelling, altered polysome association.
- Fractionation: [PMID:23166764 "most of the cpLEPA protein was detected in the thylakoid fractions"];
  stroma:thylakoid ratio ~0.25; released by Na2CO3/urea, i.e. peripheral membrane protein. So the
  mitochondrial inner-membrane (matrix side) row maps to chloroplast thylakoid membrane, the matrix row
  to chloroplast stroma.
- Bacterial LepA mechanism (back-translocation, ribosome-dependent GTPase, C-terminal domain contact with
  A-site tRNA): PMID:25712150, PMID:27092003, PMID:27137929 (SF4 members, same subfamily).

### Changes from the previous review
- Description rewritten; removed unverified OpenScientist claims (k-mer ratios, five paralogs,
  distance values) that I could not reproduce.
- Mitochondrial inner membrane -> MODIFY to chloroplast thylakoid membrane (GO:0009535), not stroma.
- Mitochondrial matrix -> MODIFY to chloroplast stroma (GO:0009570).
- NEW translation row (previously ISS from yeast Guf1 paper, a SF7 protein) replaced by NEW plastid
  translation GO:0032544 grounded in the SF4 ortholog cpLEPA (PMID:23166764).
- Relative to review next: Arabidopsis cpLEPA Q9FNM5 (At5g08650); no review exists in genes/ARATH.
- Addendum: UniProt names Q9FNM5 via HAMAP MF_03138 (chloroplastic GUF1 rule), while A0A2U1PS28 carries
  HAMAP MF_03137 (mitochondrial rule), confirming the two plant orthologs were split between rules.

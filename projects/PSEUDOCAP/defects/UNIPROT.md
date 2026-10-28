# Source-record defects for UNIPROT

5 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I537
- **Subject:** UniProtKB:Q9I537
- **Change:** EC:2.3.2.3 → EC:2.3.2.11 (alanylphosphatidylglycerol synthase)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0920/PA0920-ai-review.yaml`

The ARBA-derived RecName "Phosphatidylglycerol lysyltransferase", EC 2.3.2.3 and the lysyl-tRNA CATALYTIC ACTIVITY on Q9I537 are wrong. PA0920 is the experimentally characterised alanyl-phosphatidylglycerol synthase (Klein et al. 2009; Hebecker et al. 2011, 2015), and the EC 2.3.2.3 mapping produces the incorrect GO:0050071 IEA. Name it alanyl-phosphatidylglycerol synthase (EC 2.3.2.11) and restrict the ARBA rule so it does not fire on A-PGS sequences.

> Consequently, the protein encoded by PA0920 was named A-PG synthase.
> — PMID:19087229

## 2. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P18275 enables GO:0043858 arginine:ornithine antiporter activity (EXP, PMID:2158926)
- **Field:** DB:Reference
- **Change:** check PMID:2158926 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

enables GO:0043858 (EXP) on P18275 ArcD cites Luthi et al. 1990, whose abstract only proposes the antiport from the arcD mutant phenotype. The activity was measured in PMID:1311296 (reconstituted proteoliposomes) and PMID:8449902, which UniProt's FUNCTION comment cites. Please check whether this row should cite PMID:1311296 (IDA) instead. The annotation is correct.

> it is proposed that arcD specifies an arginine: ornithine antiporter or a part thereof
> — PMID:2158926

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0008610 lipid biosynthetic process (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0008610 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

The IMP lipid biosynthetic process row on EstA (O33407) from PMID:17631636 is based on reduced rhamnolipid in an estA deletion mutant. The UniProt entry itself says the role of EstA is unclear, and EstA is a surface-exposed outer-membrane esterase, not a rhamnolipid synthase. Unless the full text shows EstA acting on a biosynthetic intermediate, please consider removing the row. It is the sole seed of the PAINT IBD at PTN005219546 (960 leaf IBAs).

## 4. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9K3C5 located_in GO:0009421 bacterial-type flagellum filament cap (IDA, PMID:9488388)
- **Field:** SUBUNIT
- **Change:** Homopentamer → Homohexamer
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fliD/fliD-ai-review.yaml`

The UniProt entry Q9K3C5 records "SUBUNIT: Homopentamer {ECO:0000250}", an inference by similarity. The oligomeric state of PAO1 FliD has since been determined experimentally and it is a hexamer: the FliD78-405 core crystallises as a six-pointed star hexamer (PDB 5FHY), the hexamer is confirmed in solution and by negative-stain EM class averaging, and the same study shows that capping-protein stoichiometry differs between species (Salmonella FliD is a pentamer). Please update the SUBUNIT line to a homohexamer with ECO:0000269|PubMed:27664419 and add PMID:27664419 to the entry.

> Thus, we confirmed that the hexameric assembly of FliD78–405 occurs not only in the crystalline environment but also in solution using negative stain EM class averaging (Tang et al.
> — PMID:27664419

## 5. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT73
- **Subject:** UniProtKB:Q9HT73
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

The EC 7.2.2.20 / RHEA:29795 transport reaction is carried out by the ZnuABC complex. ZnuC is the nucleotide-binding subunit and has no transmembrane segment, so it cannot translocate Zn(2+) on its own; the UniProt record itself states that the complex comprises two ZnuC, two ZnuB and one ZnuA. contributes_to GO:0015633 would be the accurate qualifier for the subunit, as is done for other ABC importer ATPases.

> The complex is composed of two ATP-binding proteins (ZnuC),
> — file:PSEAE/znuC/znuC-uniprot.txt

# KRT19 (Keratin, type I cytoskeletal 19; K19, CK19) - curation notes

UniProt: P08727; HGNC:6436; 400 aa; type I (acidic) keratin of the intermediate filament (IF) family.

## Deep research status

- `just deep-research-falcon human KRT19` was launched in parallel with `just fetch-gene-pmids`.
  Status recorded at the end of this file. Literature was gathered independently from the
  cached publications and PubMed (PubMed MCP), so the review does not depend on it.

## Structure

- Smallest keratin; uniquely lacks the C-terminal non-helical tail domain
  [PMID:2448790 "The DNA sequence encodes a protein of 44,098 Da, which is unique in that it lacks the terminal non-alpha-helical tail segment found in all other keratins"].
- Domain layout: head (1-79), IF rod (80-391) with coils 1A/1B/2 and linkers [file:human/KRT19/KRT19-uniprot.txt "This keratin differs from all other IF proteins in lacking the C-terminal tail domain."].
- Highly conserved with the bovine ortholog (89% identity), suggesting strong structural constraint
  [PMID:2448790 "The high degree of cross-species identity between bovine and human 40-kDa keratins suggests that there is strong evolutionary pressure to conserve the structure of this keratin."].

## Core molecular role: structural subunit of keratin IFs

- Obligate heteropolymer with type II keratins (mainly KRT8 in simple epithelia)
  [file:human/KRT19/KRT19-uniprot.txt "Forms intermediate filaments by heterodimerizing with the type II keratin KRT8, providing mechanical integrity to epithelial cells"];
  [file:human/KRT19/KRT19-uniprot.txt "Heterodimers composed of one type I and one type II keratins; forms parallel coiled-coil heterodimers"].
- High-throughput Y2H (HuRI, PMID:32296183; CCSB PMID:16189514, 25416956) recovers many type II keratins
  (KRT1-6, KRT8, KRT71-86 etc.) as binary partners - consistent with the promiscuous type I/type II
  rod-domain coiled-coil pairing. Non-keratin Y2H hits (ABI2, HGS, EXOC8, CARD9, etc.) are not
  biologically validated.

## Expression

- Simple and ductal epithelia, basal keratinocytes in hair follicle outer root sheath, and others
  [file:human/KRT19/KRT19-uniprot.txt "Expressed in a defined zone of basal keratinocytes in the deep outer root sheath of hair follicles."].
- Marker of germinative epidermal layers in fetal skin, declining with maturation
  [PMID:23377137 "keratin-19 expression gradually decreased with epidermal maturation through gestation"].
- Widely used marker of cholangiocytes / ductal plate hepatoblasts [PMID:19185580 "a transient sheet of CK19-expressing hepatoblasts that gives rise to mature bile ducts"]
  and of carcinomas / circulating tumour cells.
- Higher in ER-positive vs ER-negative breast cancer lines [PMID:10037815 "Sequence analysis identified four of these clones as cytokeratin 19, GATA-3, CD24 and glutathione-S-transferase mu-3."]
  - this is differential expression between lines, not a demonstrated response to estrogen.

## Striated muscle role (secondary, tissue-specific)

- K8/K19 concentrate at costameres; dystrophin's ABD binds K19 directly and specifically
  [PMID:16000376 "Studies in COS-7 cells and in vitro showed that Dys-ABD binds directly and specifically to K19."].
- K19-null mice: mild myopathy, costamere disruption, subsarcolemmal gap with mitochondria
  [PMID:17971417 "Our results suggest that keratin 19 in fast-twitch skeletal muscle helps organize costameres and links them to the contractile apparatus"].
- K19/desmin double-null comparisons [PMID:21209367 "Our previous results show that the tibialis anterior (TA) muscles of mice lacking keratin 19 (K19) lose costameres, accumulate mitochondria under the sarcolemma, and generate lower specific tension than controls."];
  passive mechanics [PMID:22287836 "Though fibers are more compliant in all mutant genotypes compared to wild-type"].

## Signalling-scaffold reports (cancer cell lines; non-core)

- K19 bridges tTG (TGM2) and Src in SKBR3 cells [PMID:20080707 "we identified the intermediate filament K19 as a tTG-binding partner"].
- K19 interacts with beta-catenin/RAC1 and modulates NUMB/NOTCH signalling in breast cancer cells
  [PMID:27345400 "we found that KRT19 interacts with β-catenin/RAC1 complex and enhances the nuclear translocation of β-catenin"].
  Context-dependent opposing effects in colon vs breast cancer [PMID:30650643].
- K19 interacts with cyclin D3 and supports MCF7 proliferation [PMID:31601969 "K19 interacts with cyclin D3, and a loss of K19 resulted in decreased protein stability of cyclin D3"].
- These are single-lab, cancer-cell findings; treated as non-core / not annotated as new GO terms.

## Annotation review decisions (summary)

- Core: structural constituent of cytoskeleton; keratin filament / IF cytoskeleton; IF organization.
- Muscle terms (costamere, sarcolemma, Z disc, structural constituent of muscle) kept as non-core.
- Epidermis-specific IBA (structural constituent of skin epidermis), epithelial cell differentiation,
  response to estrogen (IEP), DGC membership and apicolateral PM flagged as over-annotations.
- protein binding: REMOVE for uninformative non-keratin hits; MODIFY to protein heterodimerization
  activity (GO:0046982) for type II keratin partners; MODIFY to protein-macromolecule adaptor
  activity (GO:0030674) for the TGM2 bridging report.

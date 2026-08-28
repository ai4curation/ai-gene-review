# treSA curation notes

## Evidence audit

- Q88IT1 is the PP_2918 standalone TreS candidate. The fetched UniProt record
  is unreviewed (PE 4), assigns the submitted name `Trehalose synthase A`, EC
  5.4.99.16, and the TreS-specific InterPro family IPR012665.
  [file:PSEPK/treSA/treSA-uniprot.txt, "SubName: Full=Trehalose synthase A";
  "EC=5.4.99.16"; "DR   InterPro; IPR012665; Trehalose_synth."]
- Wang et al. cloned a `treS` gene from P. putida KT2440, expressed the enzyme,
  and measured conversion of maltose to trehalose by HPLC. The PubMed record is
  abstract-only and does not state the locus. [PMID:25204684, "The treS gene
  from Pseudomonas putida KT2440 was amplified and expressed in E. coli BL21
  (DE3)."; "High-pressure liquid chromatography results indicated that this
  enzyme had the ability to catalyze 59% maltose into trehalose, with about
  5.1% glucose as by-product."]
- A companion primary article reports the KT2440 cloning forward primer
  `GGATCCATGACCCAGCCCGACCCGTC`; after the BamHI site, it encodes
  `MTQPDPS`, exactly matching residues 1-7 of Q88IT1. This primer match favors
  PP_2918/Q88IT1 over the 1106-aa TreSB/PP_4059 fusion. [Wang et al., Journal
  of Pure and Applied Microbiology
  8(2):1687-1692 (2014), "The forward primer was designed as 5'-(GGATCCATGACCC
  AGCCCGACCCGTC)-3'"; "a recombinant protein about 76 kDa, was observed";
  https://microbiologyjournal.org/download/69686/]
- The molecular-mass reports conflict. The companion article reports an
  approximately 76-kDa recombinant product, close to Q88IT1's predicted 75.6
  kDa, but the cached PMID:25204684 abstract says 67 kDa. The latter matches
  neither Q88IT1 nor the approximately 125.6-kDa Q88FN0 fusion. This
  discrepancy is unresolved, so apparent mass is not treated as decisive locus
  evidence; the exact primer-encoded N terminus remains the stronger assignment
  evidence. [PMID:25204684, "The recombinant TreS showed a molecular mass of
  67 kDa."]

## Coverage limitation

The fresh OpenScientist jobs for treY, treZ, treSA, the generic module, and the
module + ppu00500 + PSEPK query all finished without producing reports. They
were not restarted, and no provider output was reconstructed. This review uses
the fetched records, the previously completed narrower TreY-TreZ report, and
the primary literature listed above.

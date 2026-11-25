# fabF (Escherichia coli K-12, P0AAI5) curation notes

## 2026-11-13

- FabF is 3-oxoacyl-ACP synthase II (KAS II). Its distinctive role is
  elongation of palmitoleoyl-ACP to cis-vaccenoyl-ACP
  [PMID:237914 "This finding suggests that synthetase II functions specifically in the elongation of palmitoleyl-ACP to form cis-vaccenyl-ACP."],
  which underlies temperature control of membrane composition
  [PMID:6988423 "Cvc- mutants of Escherichia coli are deficient in the synthesis of cis-vaccenic acid and in the temperature control of fatty acid synthesis."].
- The active-site nucleophile is Cys163
  [PMID:9482715 "The proposed nucleophile in the reaction, Cys163, is located at the bottom of a mainly hydrophobic pocket"].
- Response to cold (IMP) is kept as non-core: it is the physiological
  consequence of the cis-vaccenate step, not a separate activity.
- The bare protein-binding IPI row is removed under the protein-binding policy.
- Used as the optional C16:1-to-C18:1 extension exemplar in
  `modules/bacterial_unsaturated_fatty_acid_biosynthesis.yaml`; family
  placement PTHR11712:SF336, whose official label says MITOCHONDRIAL although
  most members are bacterial.

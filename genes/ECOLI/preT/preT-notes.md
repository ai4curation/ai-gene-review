# preT (P76440, b2146) notes

## 2026-10-23 review

Reviewed for the `pyrimidine_degradation` module, where PreT-PreA is the
biochemically characterized bacterial heteromeric dihydropyrimidine
dehydrogenase. Deep research could not be run in this session (no provider API
key); the review rests on the cached abstracts and the curated UniProt record.

- PreT-PreA is an NADH-dependent iron-sulfur flavoenzyme that converts uracil
  to 5,6-dihydrouracil in vivo [PMID:21169495 "dihydropyrimidine dehydrogenase is the first member of a novel NADH-dependent subclass of iron-sulfur flavoenzymes"].
- E. coli lacks the rest of the reductive pathway [PMID:21169495 "The reductive pyrimidine catabolic pathway is absent in Escherichia coli."],
  so the enzyme exemplifies the first-step activity but E. coli does not
  satisfy the whole module.
- Heterotetramer with FAD, FMN and about four [4Fe-4S] clusters per PreT-PreA
  dimer [PMID:34097066 "contained 0.81 FAD, 0.99 FMN, 14 acid-labile sulphur and 15 iron per PreT-PreA dimer"].
- PreT carries the FAD/NAD-binding domain (IPR023753), DPD domain II
  (IPR028261) and the NAD(+) binding site, so it is the NADH-oxidizing,
  electron-input subunit (orthologous role to PSEPK PydX).

Curation decisions: protein-binding IPI rows removed under policy (the partner
is PreA, captured by GO:0140690); iron-sulfur cluster binding refined to
GO:0051539; generic oxidoreductase and oxidoreductase-complex terms TOO_GENERAL.

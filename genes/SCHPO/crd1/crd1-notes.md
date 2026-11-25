# crd1 (O13899, SPAC22A12.08c) notes

Role: CMP-forming cardiolipin synthase (EC 2.7.8.41); module `cdp_dag_phospholipid_synthesis` part 8.
Fetch: correct accession O13899.

## Evidence
- Fusion protein: HAD-like mitochondrial hydrolase (N-terminal) + CL synthase (C-terminal) [PMID:29958934 "It is encoded by the ORF SPAC22A12.08c as a C terminal part of a tandem fusion protein together with a mitochondrial hydrolase of unknown function."]
- Essential in S. pombe [PMID:29958934 "Here we show that CL synthase is an essential protein in S. pombe."] (S. cerevisiae crd1 null is viable [PMID:9614098 "The cls1::TRP1 null mutant grew on both fermentable and non-fermentable carbon sources but more poorly on the latter."])
- Reciprocal complementation with S. cerevisiae CRD1 [PMID:29958934 "Expression of S. pombe CL synthase is able to complement deletion of the CRD1 gene of Saccharomyces cerevisiae"]
- Intron retention controls CLS production [PMID:29958934 "Functional CL synthase, however, is produced only from the minor SPAC22A12.08c derived mRNA that has intron IV retained."] — UniProt isoform O13899-1 (minor) carries CLS; O13899-2 (major) lacks it.
- UniProt oddity: the CL synthase CATALYTIC ACTIVITY block is labelled "[Mitochondrial hydrolase]" in O13899 [UniProt:O13899 "CATALYTIC ACTIVITY: [Mitochondrial hydrolase]:"]; it should belong to the CL synthase chain.

## Decisions
- MODIFY ISO `GO:0008808 cardiolipin synthase activity` -> GO:0043337: GO:0008808 is defined as the PLD-type PG + PG reaction.
- MODIFY `lipid biosynthetic process` -> `cardiolipin biosynthetic process`.
- `hydrolase activity` ISM (N-terminal HAD domain) kept non-core; `phospholipid homeostasis` IMP and `mitochondrial membrane organization` ISO non-core.
- Core: GO:0043337 / GO:0032049 / GO:0005743, same as S. cerevisiae CRD1 review.

# qkr58E-1 ProtNLM2 function-description review

## Original prediction

> Necessary for the splicing of pre-mRNA. Has a role in the recognition of the branch site (5'-UACUAAC-3'), the pyrimidine tract and the 3'-splice site at the 3'-end of introns

Original wording and all model/source metadata are retained in [qkr58E-1-protnlm-source.json](qkr58E-1-protnlm-source.json).

## Assessment

| Claim | Assessment | Evidence and limit |
|---|---|---|
| Participation in pre-mRNA splicing | CNN | FlyBase already assigns spliceosomal association and splicing from PMID:18981222; the protein has an intact KH RNA-binding domain. |
| Necessary for splicing | UNC | Recovery in B/C complexes supports participation but does not establish an absolute requirement; RNAi affects selected fl(2)d splice events (PMID:27919077), but that does not establish universal necessity for pre-mRNA splicing. |
| Recognition of the exact 5′-UACUAAC-3′ branch site, pyrimidine tract and 3′ splice site | UNC | The source paragraph comes from fungal BBP Q750X2. Conserved RNA-binding architecture does not establish that the fly protein recognizes all three elements or that its sequence preference matches this exact yeast motif. Direct RNA-binding specificity or crosslinking evidence is needed. |

The target is the native 396-residue PA product; shorter alternative products are separately listed in FlyBase. The complete original wording and source Q750X2 metadata remain above and in the raw JSON. [Primary fly spliceosome study](https://doi.org/10.1128/MCB.01415-08); [protein-trap localization study](https://doi.org/10.1242/dev.111310).

Direct follow-up evidence: [PMID:26294687](https://pubmed.ncbi.nlm.nih.gov/26294687/) identifies target-specific RNA associations and spliceosomal protein interactions; [PMID:27919077](https://www.nature.com/articles/nature20568), Extended Data Figure 10b, identifies qkr58E-1-dependent alternative splicing. These findings strengthen the positive regulatory interpretation while leaving exact motif recognition unresolved.

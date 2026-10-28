# arg7 (SPBC1773.14, UniProt P40369) notes

## Identity and naming
- PomBase arg7 = argininosuccinate lyase (ASL, EC 4.3.2.1), ortholog of S. cerevisiae ARG4 (P04076). [PMID:1868575 "The complete nucleotide sequence of the ARG7 gene, coding for argininosuccinate"]
- Naming trap: S. cerevisiae ARG7 is the ArgJ-family ornithine acetyltransferase (S. pombe aga1), unrelated to S. pombe arg7.
- Second S. pombe ASL paralog: arg41 (SPBC1539.03c, UniProt P50514, UniProt gene name "argx").

## Function
- [UniProt:P40369 "Reaction=2-(N(omega)-L-arginino)succinate = fumarate + L-arginine;"] evidence ECO:0000305 from PMID:1868575.
- PMID:1868575 (abstract only): gene sequenced, expressed in S. cerevisiae; C-terminal 66-aa deletion retains some activity [PMID:1868575 "Additionally, a deletion removing 66"]. PomBase IMP for ASL activity and arginine biosynthesis from this paper (presumably complementation of a S. cerevisiae arg4 mutant; full text not available).
- Deletion-library screen: arg7 deletion was NOT recovered as an arginine auxotroph, whereas arg41 deletion was [PMID:32896087 "arg7 is one of two argininosuccinate lyases (with deletion of the other one, arg41, showing arginine auxotrophy)"]. This suggests arg41 carries most in vivo ASL flux, or that arg7 is redundant; it conflicts with the classical naming of arg7 as an arginine-requiring locus — worth checking.

## Location
- Cytosol (ORFeome HDA, PMID:16823372; PAINT IBA). PomBase GO-CAM 6690711d00000916 has arg7 and arg41 both enabling GO:0004056 in cytosol, part of GO:0006526.

## Curation points
- Urea cycle rows (ARBA IEA, IC from ASL activity) reflect the vertebrate pathway name; S. pombe is not ureotelic, the ASL step belongs to arginine biosynthesis. MODIFY to GO:0006526 (as with yeast CAR1 urea cycle rows).
- catalytic activity (InterPro2GO) is uninformative -> MODIFY to GO:0004056.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 11 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

PMID:1868575 supports sequence/function by heterologous complementation and terminal-deletion effects. PMID:32896087 distinguishes the two native lyase paralogs: lack of an arg7 auxotrophy hit does not negate its demonstrated activity or establish zero native flux. Urea-cycle participation remains contextual.

Live GO:0000050 describes ornithine-to-arginine synthesis followed by arginine cleavage to urea and regenerated ornithine; it does not require ureotelic nitrogen excretion. PMID:20435771 directly measures S. pombe Car1/Car3 arginase-dependent urea production, and PMID:18849471 explicitly places OTC in the urea-cycle segment. Existing OTC/ASS/ASL rows are retained as non-core participation in this reaction topology, without asserting net full-cycle flux or universal simultaneous operation. The upstream acetylornithine-producing Arg1 is treated separately.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-SCHPO-arg7-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 8, KEEP_AS_NON_CORE 2, MODIFY 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

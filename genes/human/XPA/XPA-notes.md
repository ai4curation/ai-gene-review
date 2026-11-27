# XPA notes

## 2026-11-27

- Seeded XPA (UniProtKB:P23025) from the human GOA file with 82 GOA rows. `just fetch-gene human XPA` cached the UniProt and GOA records and seeded the review; `just fetch-gene-pmids human XPA` recovered the transient PubMed 429 misses from the first fetch, leaving all 22 GOA PMIDs cached.
- Fetched PANTHER family PTHR10142 and PAINT data. The reviewed InterPro member table has a single human member, XPA, in PTHR10142:SF0. `just paint-losses human XPA` reported no IRD or IKR on the human XPA lineage.
- The Falcon deep-research wrapper with `--fallback perplexity-lite` could not run because the host `deep-research-client` currently exposes only `claude_code`; no provider-authored `XPA-deep-research-*.md` file was generated. The review below is therefore a manual synthesis from the cached GOA publications, UniProt, Reactome records, and PAINT rows.

## Functional synthesis

XPA is a nuclear scaffold and verification factor for nucleotide-excision repair (NER). Its central zinc-containing domain binds damaged or kinked DNA structures rather than ordinary sequence motifs: Camenisch et al. showed that excision depends on XPA assembling on a sharply bent DNA substrate [PMID:16491090, "excision is crucially dependent on the assembly of XPA protein with a sharp bending angle in the DNA substrate"], and the earlier structural review notes preferential XPA binding to UV- or chemical carcinogen-damaged DNA [PMID:10946233].

Human XPA also organizes NER protein assembly. He et al. found that RPA and XPA bind damaged DNA cooperatively [PMID:7700386, "a complex of RPA and XPA showed a striking cooperativity in binding to DNA lesions"], Saijo et al. showed that the two RPA-contacting regions of XPA are both required for NER [PMID:21148310, "XPA interaction with both RPA32 and RPA70 is indispensable for NER reactions"], and ERCC1-domain binding recruits the ERCC1-XPF nuclease into the pre-incision complex [PMID:17720715; PMID:17948053].

The PAINT root node PTN000015717 has six IBD placements. The damaged-DNA binding, NER DNA-damage-recognition, NEF1 complex, and UV-damage excision rows match the human literature. The base-excision repair placement is seeded only from worm xpa-1 and does not transfer to human XPA's NER role. The precomposed "nucleotide-excision repair involved in interstrand cross-link repair" placement is seeded only from fission yeast rhp14; the review keeps the genus NER claim but drops the ICL context for human XPA until a direct conserved role is shown.

The protein-interaction block is intentionally one GOA row per interacting partner and original PMID. Most are bare GO:0005515 rows, including a mix of mechanistic NER partners and high-throughput HuRI/BioPlex/cell-map hits; all retain their original WITH/FROM value and are removed only under the project policy that bare protein binding is uninformative. The ERCC1-specific GO:0019904 row from PMID:17720715 is kept because it captures the central-domain interaction that recruits ERCC1-XPF.

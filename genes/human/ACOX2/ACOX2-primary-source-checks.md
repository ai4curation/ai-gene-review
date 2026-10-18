# ACOX2 primary-source and PAINT checks

All 40 source rows, their cited abstracts, UniProt catalytic entries and relevant Reactome summaries were reviewed. Full disputed experiments were checked separately from abstracts. No source annotation metadata or generated source file was edited.

## Primary experiments

PMID:29287774, Ferdinandusse et al., BBA Molecular Basis of Disease 1864 (2018), 952–958. Full author paper read through Methods 2.5–2.6, Results 3.1–3.4, Figure 2 and Discussion/Conclusion. [Author-hosted full text](https://www.researchgate.net/publication/322072163_A_novel_case_of_ACOX2_deficiency_leads_to_recognition_of_a_third_human_peroxisomal_acyl-CoA_oxidase).

Exact Results 3.2 excerpt: “ACOX2 and ACOX3 both showed some activity towards C10-CoA and C16-CoA”. Human coding sequences were expressed separately in a Saccharomyces cerevisiae fox1 deletion background; empty-background lysates lacked measurable acyl-CoA oxidase activity with the tested substrates. Activities were normalized to NH-tag expression and measured in at least triplicate by HPLC. Assay substrates were 100 micromolar C10-CoA, C16-CoA, pristanoyl-CoA and THC-CoA. This directly supports weak medium/long straight-chain oxidation; the study did not assay C24-CoA or C26-CoA. Normal VLCFA concentrations in deficient patient fibroblasts do not prove absence of a redundant activity. C27 steroid total carbon count is not a >22-carbon aliphatic fatty-acid tail.

PMID:27884763 full accepted manuscript read Methods, functional Results and Discussion: [repository PDF](https://repositorio.unican.es/xmlui/bitstream/handle/10902/34505/ACOX2DeficiencyInborn.pdf?sequence=3&isAllowed=y). Exact Methods excerpt: “the conversion of THCA into CA in HepG2 cells”. Wild-type and R225W ACOX2 were expressed in HepG2 cells; a 25R/25S THCA mixture was supplied for 48 hours and cholic-acid output measured by HPLC-MS. Wild type increased cholic-acid production and both proteins localized with the peroxisomal marker. This establishes pathway function but is not an isolated 24-hydroxylation assay. The authors report that supplemented homogenate turnover was too low for accurate enzymatic analysis.

Live QuickGO on 2026-09-20 defines GO:0033791 as 25R-THCA-CoA plus water/acceptor yielding a 24R,25R hydroxylated product. UniProt RHEA:46728 instead records 25S substrate oxidation with oxygen yielding a 24E enoyl product and hydrogen peroxide. The former review incorrectly treated those reactions as synonyms. The human experiment and rat donor require separate reaction-level adjudication; no assertion is made that every possible coupled hydroxylation is absent.

## Ancestry and localization

ACOX2-paint-lineage.json records the exact Q99424 target path recovered from live PTHR10909 treeinfo and node-column-matched IBD rows. Leaf PTN002474948 descends from PTN000097533 (fatty-acid binding, peroxisome/FAD/beta-oxidation), PTN000097706 (long-chain activity and VLCFA process), and PTN008508564 (24-hydroxylase assertion). The hydroxylase node includes experimental human Q99424 and rat RGD:628684; target inclusion is legitimate descendant grounding. The ISS donor is UniProtKB:O02767. These are actual nodes, not a donor-count argument. No target-path loss annotation was recovered.

Reactome R-HSA-9033235 and R-HSA-9033236 explicitly model cytosolic PEX5 cargo before matrix import. Retain that transient compartment as non-core alongside the established peroxisomal matrix. Reduced cytosolic stability in severe peroxisome-biogenesis deficiency does not mean that cytosolic precursor molecules do not exist.

## Adjudication

No target-specific prior OpenScientist report was found in the folder or global cache. The registered substrate-chain-length-binding-and-hydroxylase-chemistry request is gated under launcher session 45234; launcher existence does not establish remote submission. Full 29287774 assay details were read after loading that request and are a post-launch evidence lead. Pending questions are free fatty-acid binding versus CoA-ester recognition, VLCFA process scope, and exact hydroxylase reaction chemistry. Weak C10/C16 oxidation is resolved positively by primary evidence.

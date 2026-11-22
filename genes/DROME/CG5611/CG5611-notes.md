# CG5611 evidence notes

Q9VB17 is the 326-residue product of FBgn0039531. FlyBase identifies PA (AAF56726/NP_651574) and PC (AGB96396/NP_001263016) as identical products; both therefore correspond to this sequence. [FlyBase](https://flybase.org/reports/FBgn0039531), saved in CG5611-flybase.txt; exact frozen UniProt and ProtNLM records are preserved alongside the review.

The sequence record contains `DR   Pfam; PF00378; ECH_1; 1.` and InterPro IPR001753/IPR029045. These establish the crotonase-like family, but not an exact substrate or pathway. No narrow subfamily or experimentally characterized ortholog establishes the proposed fatty-acid-oxidation role in the evidence assembled here. The three ND root annotations are retained; no positive catalytic core is invented.

The Falcon report completed in 412.51 seconds. Its literature synthesis identifies a behavioral screening lead (Walkinshaw et al., DOI [10.1534/genetics.114.173575](https://doi.org/10.1534/genetics.114.173575)), not a biochemical characterization. That lead is not promoted to a memory annotation because the screen and activity confound require further examination. Its general crotonase-family discussion is useful context, not independent evidence that this particular protein oxidizes fatty acids. The absence of a direct assay alone would not defeat a justified close-family transfer; the present missing element is a diagnostic subfamily/ortholog link establishing the reaction.

The original function text is copied from the probable enoyl-CoA hydratase Q52995 of Ensifer meliloti, with source similarity score 113.5; the donor's own sentence is tentative and similarity-derived. The mitochondrial location suggestion has a separate donor, mouse ECHDC2 Q3TLP5 (score 95.8). Neither raw similarity score specifies coverage or targeting-sequence conservation. These donors identify hypothesis provenance, not validation. The exact original sentence and its UNC assessment are in the accompanying function review.

Validation advisories about absent positive core or uncited provider text reflect the unresolved biological assignment and use of underlying sources. They do not indicate unreviewed GOA rows.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Re-reviewed from the UniProt record, FlyBase report, Falcon deep research, PANTHER family
review (`interpro/panther/PTHR43802/PTHR43802-review.yaml`) and a new active-site check
(`CG5611-bioinformatics/RESULTS.md`, `active_site_check.py`). ProtNLM2 files were not opened.

Identity: Q9VB17 is the canonical full-length 326-aa product of FBgn0039531 (PA and PC
are identical). UniProt Q0IGX9 (IP11341p cDNA) has an identical sequence (same MD5), so it
is a duplicate entry, not an isoform or fragment. The benchmark accession is not a fragment.

Evolutionary placement: PANTHER PTHR43802:SF1. No human or mouse protein lies in PTHR43802.
The FlyBase/DIOPT human orthologs (ECHDC1, ECHDC2, ECH1, ECHDC3) are in other PANTHER
families (PTHR11941, PTHR43149, PTHR43602), so they are not valid function donors. Members of
SF1: fly paralog Srlp/CG5844 (Q9VG69, 54.9% identity over aligned columns), worm ech-3,
Arabidopsis ECHIA, zebrafish zgc:101569, and bacterial EchA12/13/14, BamA (6-OCH-CoA hydrolase)
and CamK (6-oxocamphor hydrolase, C-C cleavage, PMID:15138275). Function is heterogeneous
across the subfamily. Srlp has GO IDA mitochondrial matrix (PMID:26362788, APEX proteomics)
and IMP cellular response to hypoxia (PMID:18653470). Neither was transferred: there is no
PAINT/IBA node for this subfamily, and one paralog's proteomics hit does not establish
CG5611's location. I also could not check whether CG5611 itself appears in the APEX list,
because the cached text lacks the supplementary data.

Active site: in a pairwise alignment, CG5611 keeps the ECHS1 G141 (oxyanion hole) as G148 and
E144 as E151, but ECHS1 E164 corresponds to N171. UniProt reports no PROSITE ECH conserved-site
match (worm ech-3 gets GO:0003824 IEA only through IPR018376, which CG5611 lacks). This
argues against transferring enoyl-CoA hydratase activity.

Literature: the only gene-specific item is the Walkinshaw et al. 2015 RNAi memory screen
(PMID:25644700, now cached). The CG5611 table entry is not in the cached text, and the result
is a confounded behavioural phenotype, so it is not used for a process annotation.

Decisions: all three ND root annotations are ACCEPTed and now supported by the
literature-search statement and the active-site analysis rather than by the Pfam DR line.
No NEW annotations. core_functions are left empty on purpose (no MF can be justified).
The description was rewritten.

PANTHER family review: agrees on SF1 placement and on the UNRESOLVED scope for GO:0004300.
No disagreement.

Next relative: Srlp (CG5844, Q9VG69), the nearest relative in the same PANTHER subfamily that
has some experimental GO data. No review of it exists in the repo.

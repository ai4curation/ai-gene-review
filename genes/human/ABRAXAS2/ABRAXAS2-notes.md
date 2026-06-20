# ABRAXAS2 notes

## Review setup

- Ran `just fetch-gene human ABRAXAS2`, which created the UniProt, GOA, review stub, PANTHER family, Reactome, and cached publication files used here.
- Ran `just deep-research-falcon human ABRAXAS2 --fallback perplexity-lite`. Falcon produced `ABRAXAS2-deep-research-falcon.md` with 16 citations and artifacts, but the recipe exited through its timeout path after 600 seconds. The configured fallback then failed with a Perplexity quota/auth error. I treated the Falcon file as secondary synthesis and based curation decisions on the fetched primary literature, UniProt, GOA, Reactome, and PN projection files.

## Identity and complex context

- ABRAXAS2 is the same protein as ABRO1/FAM175B/KIAA0157 and is the ABRAXAS paralog in BRISC rather than the BRCA1-A scaffold. PMID:21282113 distinguishes the complexes: ABRO1 is mainly cytoplasmic and "the ABRO1 complex does not interact with BRCA1" [PMID:21282113 "Because it lacks the BRCA1-interacting motif, the ABRO1 complex does not interact with BRCA1."]. This is central for avoiding over-propagation from ABRAXAS1/BRCA1-A DNA-repair annotations.
- BRISC is a K63-linked deubiquitinating complex; ABRAXAS2 is a noncatalytic scaffold/adaptor rather than the catalytic JAMM subunit. PMID:20656690 supports ABRAXAS2/KIAA0157 as a cytosolic scaffold that activates BRCC36 [PMID:20656690 "KIAA0157 mainly localizes in cytosol and activates BRCC36 in the cytoplasm."].
- Structural work separates ABRAXAS/BRCA1-A DNA-repair targeting from ABRO1/BRISC immune signaling and SHMT2 regulation [PMID:31253574 "in BRCA1-A, BRCC36 is supported by ABRAXAS (Wang et al., 2007), whereas in BRISC, it is paired with ABRO1"].

## Proteostasis PN projection review

- The PN projection file contains two ABRAXAS2 projections. `GO:0070552 BRISC complex` is already exact in GOA and is the safe propagation target for the noncatalytic BRISC subgroup [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "ABRAXAS2 GO:0070552 BRISC complex already_in_goa_exact"].
- The same projection file proposes new broad `GO:0006281 DNA repair` from a context group containing ABRAXAS1, ABRAXAS2, BABAM2, GCNA, and POLH [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "ABRAXAS2 GO:0006281 DNA repair new_to_goa"]. I did not add this as a direct ABRAXAS2 annotation because the ABRAXAS2-specific literature supports BRISC scaffold, IFNAR1/NLRP3 signaling, spindle assembly, and p53-mediated damage-response signaling, not direct recruitment to DNA repair sites as in ABRAXAS1/BRCA1-A.
- The conservative replacement for the DNA-damage evidence is `GO:0043517 positive regulation of DNA damage response, signal transduction by p53 class mediator`, based on ABRO1 stabilizing p53 and supporting DNA-damage-induced p53 accumulation [PMID:25283148 "ABRO1 stabilizes p53 by facilitating the interaction of p53 with USP7."].

## Major supported functions

- BRISC scaffold/adaptor and K63-linked deubiquitination context: PMID:19214193 identifies BRISC as a K63-specific BRCC36-containing deubiquitinating complex [PMID:19214193 "the activity was intrinsic to PA700 and the Brcc36 isopeptidase complex (BRISC)"]. ABRAXAS2 supports the complex but should not be annotated as the catalytic DUB subunit.
- Type I interferon signaling is a strong process-level annotation. BRISC-SHMT targets K63-ubiquitinated IFNAR1 and limits receptor internalization/degradation [PMID:24075985 "SHMT directs BRISC activity at K63-Ub chains conjugated to the type 1 interferon (IFN) receptor chain 1 (IFNAR1)."]. The vitamin B6/PLP relationship is better represented as regulation of BRISC-SHMT2 assembly and interferon signaling, not as a direct broad response-to-vitamin-B6 function [PMID:31142841 "Mutations in BRISC that disrupt SHMT2 binding impair type I interferon signalling in response to inflammatory stimuli."].
- Mitotic spindle assembly is directly supported. BRISC localizes to spindle poles/K-fiber minus ends, binds microtubules, and deubiquitinates NUMA1 to promote bipolar spindle assembly [PMID:26195665 "BRISC is a microtubule (MT)-associated protein complex that predominantly localizes to the minus ends of K-fibers and spindle poles and directly binds to MTs"] [PMID:26195665 "promotes the assembly of functional bipolar spindle by deubiquitinating the essential spindle assembly factor nuclear mitotic apparatus (NuMA)."].
- Reactome places FAM175B/ABRO1 in BRISC-mediated NLRP3 deubiquitination, which supports BRISC innate immune context but does not require a new direct GO term beyond the current review scope [Reactome:R-HSA-5691439 "FAM175B (ABRO1), another BRISC subunit, binds directly to NLRP3 leading to FAM175B-dependent recruitment of the BRISC complex"].

## Annotation decisions to watch

- Generic `GO:0005515 protein binding` annotations from interactome or fragmentomics screens were removed as uninformative. More specific BRISC complex, K63-linked deubiquitination context, microtubule binding, and pathway terms capture the biology better.
- `GO:0031593 polyubiquitin modification-dependent protein binding` was marked over-annotated for ABRAXAS2 itself. The biology is related to BRISC K63-ubiquitin processing, but ABRAXAS2 is a noncatalytic scaffold/adaptor and the PMID:19261749 IDA instance supports BRCA1-A/ABRAXAS1 complex polyubiquitin binding rather than direct ABRAXAS2/BRISC binding [PMID:19261749 "four members of the BRCA1-A complex possess a polyubiquitin chain-binding capability"].
- `GO:0005856 cytoskeleton` was modified to microtubule/spindle-specific component terms because the direct evidence is centered on spindle poles, centrosomes, microtubule minus ends, and midbody.
- `GO:0000278 mitotic cell cycle` was modified to the more specific spindle assembly, kinetochore-microtubule attachment, and chromosome segregation terms supported by PMID:26195665.

# NFYA3 (At1g72830; HAP2C; NF-YA3) - manual literature synthesis

No deep-research provider was available in this session; this file is a manual synthesis
from cached publications and PubMed searches (query: `(NF-YA3 OR HAP2C OR At1g72830) AND Arabidopsis`,
20 hits, screened by title/abstract; Arabidopsis NF-YA3-specific primary papers read in full).

## Identity and domain architecture

- UniProt Q93ZH2 (NFYA3_ARATH, Swiss-Prot, 340 aa). Synonym HAP2C. Gene At1g72830 (TAIR AT1G72830, GeneID 843614).
- NFYA/HAP2 subunit family (PROSITE PS51152, Pfam PF02045 CBFB_NFYA, PANTHER PTHR12632). Subunit-association
  domain (SAD, residues 182-205) and NFYA/HAP2-type DNA-binding segment (212-237); N-terminal disordered region.
  [file:ARATH/NFYA3/NFYA3-uniprot.txt]
- UniProt function and subunit statements are by similarity (ECO:0000250); nuclear location is ECO:0000305.

## Biochemistry: CCAAT binding as part of NF-Y

- Calvenzani et al. 2012 tested recombinant Arabidopsis NF-Y subunits by EMSA on a CCAAT-box oligo (from the
  HSP70 promoter). AtNF-YA3 formed NF-Y-like shifted complexes both with mouse NF-YB/NF-YC and with an
  Arabidopsis NF-YB/NF-YC3 dimer: [PMID:22912760 "For AtNF-YAs, AtNF-YA2 and AtNF-YA4 were negative, whereas
  AtNF-YA3, AtNF-YA6, AtNF-YA8 and AtNF-YA9 were all capable of generating bands with mobilities similar to mouse NF-Y."]
  and [PMID:22912760 "Figure 5B shows that an NF-Y complex was obtained with AtNF-YA3, AtNF-YA6, AtNF-YA8 and AtNF-YA9."]
- So NF-YA3 is a canonical, DNA-binding-competent NF-YA subunit; binding requires the NF-YB/NF-YC histone-fold dimer.

## In planta function

- Fornari et al. 2013: NF-YA3 and its close paralog NF-YA8 are redundantly required for early embryogenesis.
  [PMID:24303077 "Plants from single nf-ya3 and nf-ya8 mutants are similar to wild-type plants, whereas nf-ya3 nf-ya8 double mutants are embryo lethal."]
  Double-mutant embryos arrest at globular stage, and DR5rev::GFP auxin response is lost; complementation with
  35S-driven CDS was partial. No direct target genes were identified; the authors speculate on PIN regulation.
  [PMID:24303077 "The NF-YA3 and NF-YA8 redundant subunits may form equivalent NF-Y complexes with NF-YB and NF-YC subunits [17], [62], which could directly or indirectly regulate the expression of PIN genes"]
- Leyva-Gonzalez et al. 2012: NF-YA3 is induced by nutrient stresses, most strongly under low N
  [PMID:23118940 "under low N NF-YA3 was the most responsive (19-fold induction at 14dag)"], is a miR169 target,
  and 35S:NF-YA3 (miR169-resistant) plants looked like WT, unlike NF-YA2/7/10 overexpressors
  [PMID:23118940 "P35S:NF-YA3 plants developed in a similar fashion to WT controls"]. Stress-tolerance and
  transcriptome conclusions in this paper are pooled across NF-YA members.
- Multinutrient root study (2026; PMID:42171007): nf-ya3 mutants showed altered root responses to combined N/Zn
  deficiency, and NF-YA3 sits in a suberin-enriched co-expression module
  [PMID:42171007 "nf‐ya3 displayed broad responses to N | Zn across all measured traits"]. Phenotypic/network evidence only.
- Edwards et al. 1998 (abstract only): three AtHAP2 cDNAs were cloned by complementation of yeast hap2 and are
  ubiquitously expressed [PMID:9662544 "Northern-blot analysis indicated ubiquitous expression for each AtHAP2 and AtHAP5 cDNA"].
  Whether HAP2c was among the complementing cDNAs cannot be verified from the abstract.

## Gaps

- No in vivo ChIP target, no subcellular localization experiment, no defined NF-YB/NF-YC partners in planta.
- Sign of regulation (activation vs repression) at natural targets unknown.

# FUN19 (YAL034C) — Curation notes

UniProt: P28003 · SGD: S000002134 · Systematic name: YAL034C · Standard name: FUN19 ("Function UNknown 19")
Organism: *Saccharomyces cerevisiae* S288C (NCBITaxon:559292)
Length: 413 aa; 47 kDa; non-essential.

This is a genuinely UNDERSTUDIED ("dark") gene. There is **no direct experimental
characterization of FUN19 molecular function**. The primary deliverable of this review is an
honest `knowledge_gaps` section plus a domain/orthology-grounded, carefully hedged
`description`/`core_functions`.

## Journal

### 2026-07-05 — Initial data gather

- `just fetch-gene yeast FUN19` succeeded. 11 GOA annotations, all **IBA/IEA/ND** — i.e. there
  is not a single experimental (IDA/IMP/IPI/IGI/IEP) GO annotation for this gene. Every
  informative term is phylogenetically or electronically propagated.
- PANTHER family for FUN19 is **PTHR12374 "TRANSCRIPTIONAL ADAPTOR 2 ADA2-RELATED"**, and FUN19
  falls in subfamily **SF21 "SWIRM DOMAIN-CONTAINING PROTEIN FUN19-RELATED"** — a subfamily
  DISTINCT from the true ADA2 orthologs.

## KNOWN (well-supported facts)

1. **Non-essential ORF originally of unknown function.** FUN19 was defined during the molecular
   analysis of chromosome I. [PMID:1583694 "FUN19 itself proved to be non-essential"] and, at the
   time, [PMID:1583694 "None of the four predicted products shows significant homologies to known
   proteins in the available databases."] The gene name literally encodes "Function UNknown."

2. **Contains a single SWIRM domain (residues 316–413).** UniProt FT DOMAIN 316..413 "SWIRM"
   (Pfam PF04433, PROSITE PS50934, InterPro IPR007526); the rest of the protein (1–315) is
   largely low-complexity/disordered (MobiDB-lite disordered REGIONs 35–55, 189–211, 249–271;
   COMPBIAS low-complexity 35–51, 200–211). RecName in UniProt: "SWIRM domain-containing protein
   FUN19".

3. **What SWIRM domains do (domain-level, general).** The SWIRM domain is a ~85-residue four-helix
   bundle with a helix-turn-helix motif found in chromatin-regulatory subunits — Swi3/Rsc8
   (SWI/SNF-family remodelers), Ada2 (SAGA/ADA HAT), and BHC110/LSD1 (KDM1A demethylase).
   [PMID:16461455 "The SWIRM domain is a module found in the Swi3 and Rsc8 subunits of
   SWI/SNF-family chromatin remodeling complexes, and the Ada2 and BHC110/LSD1 subunits of
   chromatin modification complexes."] It can bind DNA/nucleosomes and mediate complex assembly:
   [PMID:16461455 "the Swi3 SWIRM binds free DNA and mononucleosomes with high and comparable
   affinity"] and [PMID:16461455 "the Rsc8 and Swi3 SWIRM domains are essential for the proper
   assembly and in vivo functions of their respective complexes."] So the domain is a strong hint
   toward a chromatin-associated / nucleic-acid-binding role, but it is a *shared module* that by
   itself does not specify which complex or which activity.

4. **Phosphoprotein (large-scale MS).** Phosphorylated at Thr-194, Ser-207, Ser-211
   [PMID:18407956] and Ser-207 is a Cdk1 substrate site [PMID:19779198]. Evidence at protein
   level (UniProt PE 1) — i.e. the protein is expressed. These are proteome-scale, not
   function-specific.

5. **WGD paralog = YOR338W.** FUN19 and YOR338W (S000005865) are ohnologs from the whole-genome
   duplication; both are also SF21 "FUN19-related". YOR338W is likewise uncharacterized. (SGD)

6. **Heat-stress-induced expression; non-essential null with mild fitness/chemical-response
   phenotypes** (SGD phenotype summaries). No specific molecular process is implicated.

## Orthology / subfamily reasoning (basis for judging the IBA transfers)

PANTHER PTHR12374 splits into:
- **SF20 = TRANSCRIPTIONAL ADAPTER 2-ALPHA** — the bona fide ADA2 orthologs: *S. cerevisiae*
  ADA2 (Q02336, SGD:S000002856), human TADA2A (O75478), *S. pombe* ada2 (Q9P7J7), plant/fly ADA2.
  These are SAGA/ADA co-activator subunits with SWIRM + ZZ-type zinc finger + SANT/Myb domains.
- **SF21 = "SWIRM DOMAIN-CONTAINING PROTEIN FUN19-RELATED"** — FUN19 (P28003), its WGD paralog
  YOR338W (Q99326), and *S. pombe* **laf1 (O13719) / laf2 (O74443)**. These are shorter proteins
  carrying essentially only the SWIRM module (FUN19 = 413 aa but mostly disordered N-term; laf1
  272 aa; laf2 297 aa) — they LACK the ZZ finger and SANT/Myb domains that give ADA2 its SAGA
  coactivator identity.

Consequence for the GOA IBA transfers:
- Terms whose `with/from` cite **ADA2 (SGD:S000002856)** — "transcription coactivator activity"
  (GO:0003713), "chromatin binding" (GO:0003682), "chromatin remodeling" (GO:0006338, also cites
  ADA2), "regulation of transcription by RNA Pol II" (GO:0006357, cites ADA2) — are transfers from
  the *sibling ADA2 subfamily (SF20)*, NOT from within SF21. FUN19 lacks the ZZ/SANT domains that
  underlie ADA2's coactivator activity, so "transcription coactivator activity" in particular is
  a likely **over-propagation** across the subfamily boundary.
- The **"Rpd3L-Expanded complex" (GO:0070210)** IBA has `with/from` **PomBase laf1 / laf2**, i.e.
  it IS a within-SF21 transfer. laf1/laf2 have been reported as components of *S. pombe* SIN3/Rpd3-
  type (SIN3L) histone-deacetylase complexes (WebSearch, Two-assembly-modes / SIN3 HDAC
  literature). This makes an HDAC-complex association the most biologically defensible of the
  propagated terms for FUN19 — although still IBA, not experimental, and not verified in budding
  yeast. NOTE: the specific complex "Rpd3L-Expanded" is a fission-yeast complex name; whether
  *S. cerevisiae* FUN19 is part of Rpd3L is unverified (FUN19 is not among the established Rpd3L
  subunit set).

Net interpretation: FUN19 is best described as a SWIRM-domain protein of the ADA2/LSD1 chromatin
superfamily whose own molecular function is uncharacterized; the least-unreasonable inference is
a chromatin/nucleosome-associated role (possibly linked to a Rpd3/Sin3-type HDAC module via its
SF21 relatives), but the specific SAGA-type "transcription coactivator" identity of ADA2 should
NOT be transferred wholesale.

## NOT known (knowledge gaps — primary deliverable)

- **Molecular function**: unknown. No enzymatic activity; no demonstrated binding partner/substrate.
  Whether the SWIRM domain of FUN19 binds DNA/nucleosomes (as Swi3/Rsc8 SWIRM does) is untested.
- **Biological process**: unknown. No pathway assignment from direct evidence.
- **Cellular localization**: not experimentally established (nucleus is only an IBA inference from
  the ADA2/SWIRM family; no IDA/high-throughput GFP localization annotated in GOA here).
- **Complex membership**: unknown/unverified. IBA links to Rpd3L via *S. pombe* laf1/laf2, but
  FUN19 is not an established subunit of any purified *S. cerevisiae* chromatin complex.
- **Phenotype/role**: only mild, non-specific null phenotypes (competitive fitness, chemical
  sensitivities, heat-induced expression); redundancy with YOR338W paralog untested.

## Deep research status

Automated deep research was attempted but is unavailable for this review:
- `just deep-research-falcon yeast FUN19 --fallback perplexity-lite`: falcon timed out
  after 600s; the perplexity-lite fallback returned HTTP 401 (`insufficient_quota` — API
  quota exceeded). A subsequent clean falcon retry (`just deep-research-falcon yeast
  FUN19`) also hung on the network (0% CPU, ~2s CPU time over >12 min elapsed) and was
  terminated.

No `-deep-research-{provider}.md` file was produced, and none was fabricated. Per project
policy, the review is instead grounded in the UniProt record, the GOA annotations and their
`with/from` provenance, the PANTHER PTHR12374 family/subfamily data
(`interpro/panther/PTHR12374/`), and cached primary literature (PMID:1583694, PMID:16461455,
PMID:18407956, PMID:19779198), supplemented by targeted web/PubMed lookups recorded above.

## References to cite in review

- PMID:1583694 — chromosome I analysis; establishes FUN19 as non-essential, initially no homology.
- PMID:16461455 — SWIRM domain structure/function (domain-level basis for chromatin inference).
- PMID:18407956 — phosphoproteome (Thr194/Ser207/Ser211).
- PMID:19779198 — Cdk1 substrate phosphosites (Ser207).
- file: PANTHER PTHR12374 family/subfamily data (interpro/panther/PTHR12374) for subfamily reasoning.

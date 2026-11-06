# lipA (P60716) notes

Part of the RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 2 E. coli K-12.

## Literature sources

No deep-research file is available for this gene (falcon fails authentication and asta
returned nothing useful in Phase 1). These notes are built from cached publications
(`publications/PMID_*.md`; PMID:29051382 and PMID:24901788 are full text, the rest
abstract-only), the UniProt record and PubMed searches.

## Identity and family

- Lipoyl synthase, EC 2.8.1.8, 321 aa. Radical SAM superfamily, lipoyl synthase family
  (HAMAP MF_00206, TIGR00510 lipA, PTHR10949, Pfam PF04055 + PF16881 LIAS_N).
  [file:ECOLI/lipA/lipA-uniprot.txt "Belongs to the radical SAM superfamily. Lipoyl synthase family."]
- No E. coli LipA crystal structure; structures exist for other bacterial LipA orthologs (not cited here).

## Catalytic activity

- Inserts two sulfur atoms at C6 and C8 of an octanoyl chain amide-linked to the lipoyl-domain
  lysine; free octanoate is not a substrate.
  [file:ECOLI/lipA/lipA-uniprot.txt "Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes"]
- First in vitro activity: octanoyl-ACP + LipB + apo-PDC + SAM gave lipoylated PDC.
  [PMID:11106496 "When sodium dithionite-reduced LipA was incubated with octanoyl-ACP, LipB, apo-PDC, and S-adenosyl methionine (AdoMet), lipoylated PDC was formed."]
- Substrate is the octanoylated protein (E2 lipoyl domain, or H protein), so lipoate is
  assembled on the carrier. [PMID:14700636 "octanoyl domain and octanoyl-PDH were substrates for sulfur insertion in vitro"]
  [PMID:15157071 "the octanoylated derivative of the lipoyl-bearing subunit of the glycine cleavage system (H-protein) is also a substrate for LipA"]
- 2 SAM per lipoyl group; 5'-dA radical abstracts H from the octanoyl chain.
  [PMID:15157071 "our data indicate that 2 equiv of AdoMet are cleaved irreversibly in forming 1 equiv of [lipoyl]H-protein"]
- Both sulfurs come from the same LipA polypeptide.
  [PMID:15740115 "each lipoyl synthase polypeptide contributes both of the sulfur atoms to the intact cofactor"]
- Enzyme-substrate cross-link through a partly disassembled auxiliary cluster is a competent
  intermediate (Lanz et al. 2014; organism not stated in the cached text, Booker lab LipA work).
- Early genetics (Reed and Cronan 1993) misread LipA as acting on free octanoate; superseded.

## Clusters

- Two [4Fe-4S] clusters per polypeptide: radical SAM cluster in CX3CX2C (Cys94, Cys98, Cys101)
  and auxiliary cluster in CX4CX5C (Cys68, Cys73, Cys79).
  [PMID:15362861 "We report herein that LS from Escherichia coli can accommodate two [4Fe-4S] clusters per polypeptide and that this form of the enzyme is relevant to turnover."]
  Triple Cys-to-Ala variants of either motif are inactive.
- Earlier Mossbauer (Fontecave lab) saw one [4Fe-4S] per subunit, converting to [2Fe-2S] in air.
  [PMID:10747808 "under strict anaerobiosis, lipoate synthase can accommodate a (4Fe-4S) cluster per subunit"]
- Auxiliary cluster is degraded during turnover; NfuA (and IscU) re-installs it, making the
  enzyme catalytic. [PMID:29051382 "We found that the Escherichia coli iron-sulfur (Fe-S) cluster carrier protein NfuA efficiently reconstitutes the auxiliary cluster during LipA catalysis in a step that is not rate-limiting."]

## Quaternary structure

- Unresolved, and the literature has changed its mind. The early reports read a homodimer
  [PMID:10747808 "Biotin synthase and lipoate synthase are homodimers"], and the AdoMet and
  sulfur stoichiometries were taken the same way [PMID:15157071 "consistent with a model in
  which two LipA proteins are required to synthesize one lipoyl group"].
- Both sulfurs of one lipoyl group come from one polypeptide (PMID:15740115). This retires the
  inter-subunit sulfur-sharing rationale that made the 1:2 LipA:product stoichiometry look like
  evidence for an obligate dimer. It does *not* by itself exclude a homodimer whose subunits
  each run a complete reaction -- an inference these notes previously drew, wrongly.
- What is actually on the record: purification gives a monomer/dimer mixture (PMID:11106496);
  molecular-sieve chromatography puts LipA alone near its monomer mass [PMID:29051382 "LipA
  alone (dotted trace) elutes at 59.6 mL by MSC, exhibiting an experimentally calculated mass
  of 44.1 kDa (theoretical mass, 38.2 kDa)"] and resolves a 1:1 LipA-NfuA heterodimer; and
  UniProt declines to choose ("Monomer or homodimer."). So no *defined* homodimer is
  established, the earlier reports are superseded on this point, and GO:0042803 is treated as
  over-annotation on that basis. The oligomeric state under turnover is an open knowledge gap
  in the review, not a settled call.

## Interactions and localization

- LipA co-purifies with intact PDH and OGDH complexes (AceF, SucB rows), but not with the H
  protein. [PMID:21209092 "the intact pyruvate and 2-oxoglutarate dehydrogenase complexes specifically copurify with both LipB and LipA"]
- Cytosol: detected in the cytosolic fraction proteome (PMID:18304323). Soluble, no TM segment.

## Physiology

- lipA mutants cannot grow on glucose minimal medium without lipoate (PMID:29051382).
- Inhibited in vivo by 5'-deoxyadenosine accumulation in pfs mutants.
  [PMID:15911379 "Physiological experiments indicate that lipoic acid synthase, another SAM radical enzyme, is also inhibited by 5'-deoxyadenosine accumulation."]

## GO decisions (summary)

- Generic rows per the RADICAL_SAM treatment rule (GO:0003824 -> GO:0016992; GO:0051536 ->
  GO:0051539). GO:0016783 -> GO:0016992 (as in human LIAS).
- GO:0009107 is obsolete in QuickGO today (checked 2026-10-19: "obsolete lipoate biosynthetic
  process", replaced_by GO:0009249). Both rows MODIFY to GO:0009249, as in LIAS.
- Cytoplasm rows MODIFY to cytosol (GO:0005829), which the gene carries by IDA.
- NEW GO:1904047 (IC, from PMID:15157071 SAM stoichiometry and the HAMAP/Booker cluster
  description of SAM as an exchangeable ligand).
- Protein binding (AceF/SucB, NfuA) REMOVE.

## Review written (2026-10-31)

`lipA-ai-review.yaml` is complete: 19 rows (8 ACCEPT, 7 MODIFY, 2 REMOVE,
1 MARK_AS_OVER_ANNOTATED, 1 NEW), 3 core functions, `status: COMPLETE`. The
decisions are the ones sketched under "GO decisions" above, with two points
settled while writing:

- **GO:0042803 protein homodimerization** is `MARK_AS_OVER_ANNOTATED`, not
  REMOVE. The IDA observation is real — LipA purified "as a mixture of monomeric
  and dimeric species" (PMID:11106496) — so the term is not false; what
  overreaches is reading a functional homodimer into it, against UniProt's own
  "Monomer or homodimer", the single-polypeptide sulfur donation
  (PMID:15740115) and the 1:1 NfuA complex (PMID:29051382).
- **The cytoplasm rows MODIFY to cytosol.** GO:0005737 is not one of the five
  root organelle terms that `projects/ORGANELLES.md` exempts from refinement, so
  the ordinary "correct but general is MODIFY" rule applies, and GO:0005829 is
  carried by IDA.

Quoting note for whoever edits this file next: the `supporting_text` checker
strips square brackets as editorial, so
`"... 1 equiv of [lipoyl]H-protein"` fails even though it is verbatim in
PMID:15157071. `[4Fe-4S]` is exempt as scientific notation; `[lipoyl]` is not.
The quote is written in the sanctioned `...` form instead.

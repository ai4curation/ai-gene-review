# mei-9 (meiotic 9, CG3697, FBgn0002707; UniProt Q24087) review notes

## Sources and searches (2026-11-16)

- Inputs: `mei-9-uniprot.txt` (Swiss-Prot Q24087, XPF_DROME), `mei-9-goa.tsv` (36 rows),
  `mei-9-deep-research-flybase.md` (FlyBase hand-written description), and the cached GOA
  publications. No Falcon/Perplexity deep research was available for this batch.
- GOA fetch note: on 2026-11-16 QuickGO returned HTTP 500 whenever the request included
  `includeFields=taxonName` (an EBI taxonomy back-end error), so `just fetch-gene` wrote a
  header-only GOA file. The GOA file was regenerated with the project's own
  `ai_gene_review.etl.gene.fetch_goa_data`, dropping only that include and filling the
  taxon-name column from the returned taxon id (7227 = Drosophila melanogaster).
- PubMed queries run (E-utilities):
  - `(mei-9[tiab] OR mei9[tiab] OR MEI-9[tiab]) AND drosophila` (60 hits, titles scanned)
  - `(mus312[tiab] OR MEI-9[tiab] OR "mei-9"[tiab]) AND (crossover OR Holliday OR endonuclease) AND drosophila`
  - `drosophila AND (MEI-9 OR mei-9 OR XPF) AND (mitotic crossover OR mitotic recombination OR interstrand)`
  - `Enzlin JH[au] AND Scharer OD[au] AND active site` (XPF catalytic site background)
- Web search: Drosophila mei-9/Ercc1 and single-strand annealing or nonhomologous tail
  removal. No fly study testing mei-9 in SSA or somatic gene conversion was found.
- Extra papers cached for this review: PMID:15166153, PMID:22022278, PMID:25205745,
  PMID:17248870, PMID:11953324. PMID:11336992 (Vogel and Nivard 2001, mutagen response of
  mei-9 and mus201 germ cells) was read in abstract and not used.

## Identity and family

- MEI-9 is the Drosophila XPF/Rad1 ortholog [PMID:8647398 "We have analyzed the mei-9 gene
  at the molecular level and found that it encodes a homologue of the S. cerevisiae excision
  repair protein Rad1, the probable homologue of mammalian XPF/ERCC4."].
- PANTHER PTHR10150:SF0 (DNA repair endonuclease XPF); InterPro IPR006167 XPF,
  IPR047520 XPF_nuclease; CDD cd20078 XPF_nuclease_XPF_euk; NCBIfam TIGR00596 rad1.
  ERCC4 nuclease domain at residues 697-777 (UniProt FT DOMAIN).
- Quick sequence check (my own, `python` on the UniProt SQ block): the ERCC4 domain
  contains the GDY (Gly728-Asp729) and ERK (Glu739-Arg740-Lys741) segments of the XPF
  nuclease motif described for human XPF-ERCC1 [PMID:11953324 "seven of the residues of XPF
  involved in nuclease activity are absolutely conserved in the three protein families"].
  I did not map individual catalytic residues (the cached Enzlin and Scharer record is
  abstract-only), so this is only a presence check, not evidence of activity.
- The PAINT IBD node for every IBA row is PTN000015911, placed at Eukaryota (taxon:2759)
  in PTHR10150, a family containing only XPF orthologs. MEI-9 descends from it, and nothing
  in the family file marks a loss on the Drosophila branch.

## Partners and complexes

- ERCC1: interacts by yeast two-hybrid [PMID:10812334 "ERCC1(Dm) interacts strongly in a
  yeast two-hybrid assay with MEI-9, indicative of the presumed requirement for these
  polypeptides to dimerize to form the functional endonuclease."]. Ercc1 mutants have the
  same damage sensitivity as mei-9 mutants and lower MEI-9 levels [PMID:15944364 "We find that
  Ercc1 mutants are identical to mei-9 mutants in sensitivity to DNA-damaging agents, but have
  a less severe reduction in the number of meiotic crossovers. MEI-9 protein levels are reduced
  in Ercc1 mutants"].
- MUS312 (SLX4 ortholog) binds MEI-9 and is needed for the meiotic but not the repair
  function [PMID:12504024 "A missense mutation in mei-9 that disrupts the MEI-9-MUS312
  interaction abolishes the meiotic function of mei-9 but does not affect the DNA repair
  functions of mei-9."]. MEI-9 bridges ERCC1 and MUS312 in a three-hybrid assay
  [PMID:15944364 "This is the first evidence for all three proteins participating in a complex
  simultaneously."].
- HDM (hold'em) binds MEI-9 and ERCC1 [PMID:18957705 "We conclude that HDM, MEI-9, MUS312,
  and ERCC1 form a complex that resolves meiotic recombination intermediates into crossovers."].
- Fly NER partners exist: Xpac (P28518, XPA homolog) and Xpc/mus210 (Q24595), so the
  XPF-ERCC1-XPA composition in the GO:0000110 definition has fly counterparts. No fly study
  of a MEI-9-ERCC1-XPAC complex was found.
- No biochemistry on the fly enzyme: [PMID:19595722 "Although biochemical activities of
  MUS312–MEI-9–ERCC1 have not been reported"]; [PMID:22022278 "it has been proposed that
  MUS312–MEI-9–ERCC1 generates COs by resolving HJs [41], [42], but in vitro analysis of this
  enzyme has not been published."]. The catalytic-subunit designation rests on homology
  [PMID:15944364 "Drosophila MEI-9 is the catalytic subunit of a DNA structure-specific
  endonuclease required for nucleotide excision repair (NER)."].

## DNA repair

- NER: mei-9a cells are deficient in excision of UV pyrimidine dimers [PMID:826452 "is
  deficient in the excision of UV-induced pyrimidine dimers in both sexes"]. Larvae are
  hypersensitive to MMS, nitrogen mustard and 2-AAF (same paper).
- UV response in vivo: mei-9 larvae are UV-sensitive and epidermal re-expression rescues
  [PMID:21664581 "restoring Mei-9 expression in the epidermis alone (A58Gal4 driver) was
  sufficient to fully rescue the mortality (not shown) and melanization phenotypes"].
- ICL repair: [PMID:15166153 "Drosophila mei-9 is essential for several DNA repair and
  recombination pathways, including nucleotide excision repair (NER), interstrand crosslink
  repair, and meiotic recombination."]; [PMID:12504024 "Like XPF, MEI-9 functions in nucleotide
  excision repair and interstrand crosslink repair."]. MUS312 has a separate, MEI-9-independent
  ICL function [PMID:19595722 "Relative sensitivities of mutants to crosslinking agents
  indicate that MUS312 has a more crucial function and acts independently of MEI-9–ERCC1"].
  Whether the fly MEI-9 ICL step is NER-like (replication-independent) or an unhooking incision
  has not been tested; the IBA term is NER-involved-in-ICL-repair.
- DSB repair: [PMID:10908583 "The Drosophila homologue of Rad1, MEI-9, is involved in some DSB
  repair pathways (Baker et al. 1976)"]. No fly assay of mei-9 in somatic HR (gap repair,
  SDSA) or SSA tail removal was found.
- Mismatch repair: extracts of mei-9 mutants show reduced nick-dependent repair
  [PMID:9488459 "Nick-dependent repair was reduced in extracts of animals mutant for the mei-9
  gene."]. The in vivo basis for an MMR role (postmeiotic segregation in mei-9 females) was
  re-examined and attributed to crossover failure, not MMR [PMID:17339219 "suggesting that the
  underlying meiotic function for MEI-9 is in crossover formation rather than mismatch
  repair"].

## Mitotic recombination (IBA GO:0006312)

- Mitotic recombination is not reduced in mei-9 mutants: [PMID:17248870 "Mitotic recombination
  is at or above control levels in the presence of each of the recombination-defective meiotic
  mutants examined"]; instability in mei-9 is chiefly breakage [PMID:17248870 "that of mei-9
  alleles is primarily due to chromosome breakage and, to a lesser extent, to an elevated
  frequency of mitotic recombination"].
- Spontaneous mitotic crossovers in Fancm mutants do not need MEI-9 [PMID:25205745 "We made
  double mutants between Fancm and the genes encoding each of the catalytic subunits of the
  putative resolvases: Gen , mus81 , Slx1 , and mei-9 . There was no significant difference in
  crossover frequency in any of these double mutants relative to Fancm single mutants"]; they
  are made by MUS81 or SLX1 with MUS312.
- mei-9; mus309 (Blm) doubles are viable, unlike mus312 mus309 [PMID:22022278 "We found that
  mei-9; mus309 double mutants are viable, consistent with the previous finding that
  MEI-9–ERCC1 interacts with MUS312 in meiotic recombination, but not in somatic DNA repair
  [42]."].
- Verdict: the fly data argue against MEI-9 in mitotic crossing over; nonreciprocal mitotic
  events (gene conversion, SSA) are untested. MARK_AS_OVER_ANNOTATED.

## Meiotic recombination

- mei-9 females have strongly reduced crossovers and nondisjunction (Baker and Carpenter 1972,
  PMID:4625747; Yildiz 2002, PMID:12504024). Gene conversion frequency is not reduced
  [PMID:8647398 "mei-9 mutants suppress reciprocal exchange without suppressing the frequency of
  gene conversion"].
- Resolution model [PMID:17339219 "Our results support a model in which MEI-9 nicks Holliday
  junctions to generate crossovers during meiotic recombination, and, in the absence of MEI-9
  activity, the double Holliday junction intermediate instead undergoes dissolution to generate
  noncrossover products in which heteroduplex is unrepaired."].
- Checkpoint phenotypes in crossover mutants (delayed oocyte selection) are PCH2-dependent
  [PMID:18957704 "mutations in Drosophila genes required to process DSBs into crossovers delay
  two important steps in meiotic progression: a chromatin-remodeling process associated with DSB
  formation and the final steps of oocyte selection"]; this is a response to the defect, not a
  role of MEI-9 in oocyte fate.

## Verdicts on the non-duplicative IBA rows

| Term | Action | One-line reason |
|---|---|---|
| GO:0000110 NEF1 complex | ACCEPT | Definition names XPF-ERCC1-XPA; fly MEI-9 binds ERCC1, does NER, and fly Xpac exists |
| GO:0000724 DSB repair via HR | KEEP_AS_NON_CORE | Fly role is HR repair of meiotic DSBs (dHJ resolution); no somatic HR assay |
| GO:0003684 damaged DNA binding | MARK_AS_OVER_ANNOTATED | XPF-ERCC1 binds DNA structures; damage recognition is XPC/XPA; single human seed, no fly data |
| GO:0006312 mitotic recombination | MARK_AS_OVER_ANNOTATED | Two fly assays show mitotic crossovers do not need MEI-9 |
| GO:1901255 NER in ICL repair | ACCEPT | mei-9 essential for ICL repair and NER in flies |
| GO:1990599 3' overhang ssDNA endonuclease (contributes_to) | ACCEPT | Catalytic subunit of XPF-ERCC1; motif present; no fly biochemistry |

## Description sources

- FlyBase: both sentences traced (catalytic subunit with ERCC1 in NER: PMID:15944364;
  MUS312 interaction for crossovers: PMID:12504024, PMID:15944364). Verdict VERIFIED. It omits
  ICL repair and the HDM partner.
- UniProt FUNCTION: "required for the repair of mismatches within meiotic heteroduplex DNA" is
  outdated (PMID:17339219). Recorded as an OUTDATED_STATEMENT on the UniProt reference.

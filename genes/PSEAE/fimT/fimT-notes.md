# fimT (PA4549, UniProt Q9HVN0) review notes

No deep-research provider was available. These notes come from my own reading
of the cached publications, PubMed/Europe PMC searches, live QuickGO queries
(2026-11-03) and the UniProt entry.

## Identity

- `just fetch-gene PSEAE fimT` resolved to Q9HVN0 (Q9HVN0_PSEAE), PA4549,
  169 aa, unreviewed (TrEMBL), PE 3. The accession matches the one named in
  the task.
- UniProt recommended name "Type II secretion system protein H" and the
  inner-membrane location are ARBA predictions (ECO:0000256|ARBA), not
  curated statements.
- Family: InterPro IPR022346 T2SS_GspH, Pfam PF12019 GspH (domain 47-148),
  Pfam PF07963 N_methyl, NCBIfam TIGR02532 IV_pilin_GFxxxE, SUPFAM "Pili
  subunits" [file:PSEAE/fimT/fimT-uniprot.txt]. No PANTHER xref in the
  entry, so no PAINT node reaches it (QuickGO lists no IBA rows).
- No nuclease domain or catalytic motif of any kind; this is a small
  class III prepilin-like protein.
- P. aeruginosa has a separate T2SS GspH, XcpU (PA3100, Q00515; UniProt REST
  query), and the neighbouring paralogue FimU (PA4550, G3XCZ0).

## Literature

- Discovery: fimT and fimU lie between pilR and pilV and encode prepilin-like
  proteins. fimT mutants are wild type; FimT overexpression replaces FimU
  [PMID:8682785 "whereas the fimT and dada* mutants retained wild-type
  phenotypes"; "overexpression of the fimT gene was found to be able to
  functionally replace the lack of a fimU gene product, suggesting a subtle
  role in fimbrial biogenesis"]. Full text (PMC232641) could not be
  retrieved by the PubMed MCP; abstract only.
- The P. aeruginosa minor pilin papers from the Burrows lab study FimU,
  PilV, PilW, PilX and PilE; FimT is not among the minor pilins they assay
  [PMID:20338182 "including five conserved pilin-like proteins of unknown
  function (FimU, PilV, PilW, PilX, and PilE in Pseudomonas aeruginosa)"].
  The full-text caches of PMID:25389296, PMID:26359492 and PMID:29775484
  contain no mention of FimT (text search).
- FimT/FimU family includes the T2SS GspH [PMID:35246533 "FimT and FimU are
  minor type IV pilins that belong to the GspH/FimT family of proteins
  (Pfam: PF12019; InterPro: IPR022346), which also includes the type II
  secretion system (T2SS) pseudopilin GspH/XcpU."].
- DNA binding: purified P. aeruginosa FimT binds a 30 bp dsDNA in EMSA,
  whereas P. aeruginosa FimU does not [PMID:35246533 "We expressed and
  purified FimT and FimU from the human pathogen P. aeruginosa and the plant
  pathogen Xanthomonas campestris (both γ-Proteobacteria) and performed
  EMSAs to assess DNA binding in vitro"; "Interestingly, FimT from both
  species binds to DNA and the affinity appears to be within the same order
  of magnitude as L. pneumophila FimT."; "On the other hand, FimU does not
  interact with DNA"]. Full-length FimTPa did not restore transformation
  in a Legionella fimT mutant, but its C-terminal D-region grafted onto
  Legionella FimT did [PMID:35246533 "Intriguingly, the chimeric construct,
  appending the D-region of FimTPa to the rest of FimTLp, restored natural
  transformation to near wild-type levels"]. The binding is
  non-sequence-specific and electrostatic in the Legionella protein. PAO1 is
  not known to be naturally transformable, so the physiological role of FimT
  DNA binding in P. aeruginosa is unknown.

## The GO:0016888 row (PseudoCAP IDA, PMID:18174131)

Live QuickGO, 2026-11-03:

- `geneProductId=Q9HVN0`: 5 rows. GO:0016888 enables, IDA, PMID:18174131,
  PseudoCAP, 20190311 (no WITH/FROM). Also GO:0043683 IDA PMID:8682785
  PseudoCAP 20190311, and three InterPro/UniProt IEAs.
- `reference=PMID:18174131&assignedBy=PseudoCAP`: 4 rows, all 20190311:
  P22608 pilB GO:0016887; P24559 pilT GO:0016887; G3XCX3 pilU GO:0016888;
  Q9HVN0 fimT GO:0016888.

PMID:18174131 is Chiang et al. 2008, ATPase assays and NTPase-motif
mutagenesis of PilB, PilT and PilU [PMID:18174131 "Assay of purified
6xHis-tagged PilB, PilT and PilU from P. aeruginosa showed that all three
proteins have ATPase activities in vitro."]. Abstract only: no PMC copy
(PMID-to-PMCID conversion returns none), the publisher page returned 403, and
Europe PMC text-mined gene mentions are only ATPase/NTPase terms. I have not
read the full text.

Assessment:

1. GO:0016888 is wrong for FimT. CONFIRMED from primary data: the live
   QuickGO query shows the identical wrong id on the pilU row from the same
   paper and date, while pilB and pilT got the adjacent GO:0016887; the
   completed pilU review established that slip. FimT's sequence has no
   nuclease domain (GspH/N_methyl pilin only), and no paper reports nuclease
   activity for any FimT.
2. The paper probably has nothing on FimT, so repointing to GO:0016887 is
   not the fix. The abstract positively names PilB, PilT and PilU as the
   proteins purified and mutated and calls them motor proteins; FimT is a
   minor pilin, not an NTPase, so it cannot be one of the ATPases. The fimT
   row looks like a duplicate of the pilU row keyed onto the wrong gene
   product (the pilU row already exists, so the fimT copy should be deleted,
   not moved). Confidence PROBABLE: I read only the abstract, so I cannot
   exclude that the full text uses FimT somehow (e.g. as a control), but no
   reading of an NTPase paper would support a nuclease or ATPase function
   for a pilin.
3. Cause of the gene-product slip: unknown. PA4549 and PA0396 are not
   similar locus tags; pilB is PA4526, near PA4549 in the genome, but pilB's
   row from the paper is separate and correct.

Recorded as two PSEUDOCAP source defects on the row: WRONG_TERM (CONFIRMED,
requested_change CHECK, since the corrected term depends on point 2) and
WRONG_GENE_PRODUCT (PROBABLE, DELETE_ROW, the pilU row G3XCX3 being where the
assertion belongs).

## PseudoCAP IBA-seed assessment

fimT (PA4549, Q9HVN0) is not in `projects/PSEUDOCAP/iba_seed_worklist.yaml`:
none of its PseudoCAP rows seeds a PAINT IBD with PseudoCAP support. It also
receives no IBA (no PANTHER family assignment in UniProt; QuickGO returns no
GO_REF:0000033 rows), so there is no IBA to assess.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| none | - | - | - | GO:0016888, IDA, PMID:18174131 (PseudoCAP; seeds no IBD) | WRONG | Same off-by-one id as the pilU row from the same paper and date (live QuickGO); FimT is a pilin with no nuclease domain, and the ATPase paper's abstract concerns only PilB/PilT/PilU. Delete the row. |
| none | - | - | - | GO:0043683, IDA, PMID:8682785 (PseudoCAP; seeds no IBD) | SOUND (evidence code questionable) | FimT overexpression replaces FimU in fimbrial biogenesis; the abstract describes genetics (mutant, overexpression suppression), which fits IGI/IMP better than IDA. Abstract only, so no defect recorded. |

## Decisions summary

- ACCEPT: plasma membrane (IEA); type IV pilus assembly (IDA).
- REMOVE: type II protein secretion system complex and protein secretion by
  the type II secretion system (IEA, IPR022346): domain shared with
  T2SS GspH; XcpU is the Xcp GspH. Consistent with the fimU review.
- REMOVE: DNA endonuclease activity (IDA, PMID:18174131), with two PseudoCAP
  source defects.
- NEW: double-stranded DNA binding (GO:0003690), IDA, PMID:35246533 (EMSA of
  purified P. aeruginosa FimT with 30 bp dsDNA).

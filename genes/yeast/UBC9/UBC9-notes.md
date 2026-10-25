# UBC9 (YDL064W, P50623) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No earlier review of this gene existed, so this is the first review. It was requested because
UBC9 is the closest experimentally characterised relative of Neurospora NCU04302 (Q1K772). I
did not open or use any ProtNLM2 prediction files.

### Deep research

`just deep-research-falcon yeast UBC9 --fallback perplexity-lite` failed. Falcon gave
"Exception: Failed to authenticate", and the perplexity-lite fallback got HTTP 401 for
insufficient quota. No deep-research file was produced. This review rests on the cached
publications (all abstract-only), the UniProt record and the PANTHER/PAINT data.

### Evolutionary grounding

- The PANTHER geneinfo service (queried live by `UBC9-bioinformatics/subfamily_and_active_site.py`)
  places P50623 in PTHR24067:SF248. S. pombe hus5 P40984 and N. crassa Q1K772 are in the same
  subfamily. Human UBE2I P63279 is in the sister subfamily SF280.
- The PAINT node PTN000629675 carries IBD SUMO conjugating enzyme activity (GO:0061656),
  protein sumoylation (GO:0016925) and nucleus (GO:0005634). SGD:S000002222 (this gene) is a
  seed for the sumoylation and nucleus IBDs but not for GO:0061656. SGD curates this gene's
  activity as the parent term, SUMO transferase activity GO:0019789, so this omission
  follows from how SGD annotated the gene and is not a contrary judgement.
- Cys93 (the UniProt glycyl thioester active site) is conserved in all four proteins.

### Experimental findings in S. cerevisiae (abstract-level)

- Thioester with Smt3. "Ubc9p was found to form a thioester with Smt3p" [PMID:9341106]. No
  Ub~Ubc9p thioester could be detected. Ubc9p is needed for Smt3 attachment in vitro, "suggesting
  that it is the only such enzyme in S. cerevisiae" [PMID:9341106].
- In vivo requirement. "UBC9 ... is required for SMT3 conjugation in vivo" [PMID:9435231].
  Recombinant yeast Ubc9 forms SMT3 thioesters [PMID:9435231].
- Substrates. Septins (Cdc3) with the E3 Siz1/Ull1: the in vitro system needs E1, E2 (Ubc9) and
  ATP [PMID:11577116; PMID:11572779; PMID:11587849]. PCNA is "conjugated to SUMO by UBC9"
  [PMID:12226657].
- Auto-sumoylation and backside binding. Ubc9 is sumoylated at Lys153. Ubc9*SUMO acts as a
  cofactor for SUMO chain assembly through "noncovalent backside SUMO binding". The
  sumoylation-deficient mutant reduces meiotic SUMO conjugates and abolishes SC formation
  [PMID:23644018].
- Meiosis. Ubc9 localises to meiotic chromosomes, coinciding with SUMO. A non-null ubc9 allele
  impairs Zip1 polymerisation [PMID:16782016].
- Cell cycle. Repressing UBC9 arrests cells at G2/early M with a short spindle and stabilises
  Clb5 and Clb2 [PMID:7800043]. The 1995 paper read UBC9 as a ubiquitin E2 for cyclins. Later
  work showed that it is the SUMO E2 and forms no detectable Ub thioester [PMID:9341106]. The
  cell-cycle phenotypes therefore come downstream of the loss of sumoylation.

### Decisions

- GO:0019789 SUMO transferase activity (IDA/IMP/IEA): MODIFY to GO:0061656 SUMO conjugating
  enzyme activity. GO:0061656 is_a GO:0019789 (checked against the OLS hierarchy), and the
  evidence is the E2 thioester relay.
- GO:0000022 mitotic spindle elongation (IMP): MARK_AS_OVER_ANNOTATED. The short spindle is a
  feature of the G2/M arrest after depletion. It is not evidence that Ubc9 does any of the work
  of spindle elongation.
- Bare protein binding (4 rows, high-throughput Y2H/complexes with Smt3): REMOVE under the
  protein-binding policy. The Smt3 interaction is real and is covered by the E2 activity and the
  NEW SUMO binding row.
- NEW GO:0032183 SUMO binding (non-core), from the backside-binding finding [PMID:23644018].
- I did not add synaptonemal complex assembly as a NEW term. The data show necessity
  (sumoylation-deficient alleles), and the SC structural work is done by Zip1/Ecm11. Ubc9 acts
  on the process through its general catalytic role.

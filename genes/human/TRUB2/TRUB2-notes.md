# TRUB2 (human, O95900) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: TRUB2 is the experimentally characterised reference for a pigeon (COLLI/A0A2I0M3K7)
gene in the same PANTHER subfamily (PTHR13195:SF0). This review treats human TRUB2 in its own
right and does not use any ProtNLM2 output.

### Process notes
- `just fetch-gene human TRUB2` created the uniprot, GOA (29 rows) and stub files.
- `just deep-research-falcon human TRUB2 --fallback perplexity-lite` FAILED: Edison API
  "Failed to authenticate", then the perplexity-lite fallback timed out at 600 s. No deep-research
  file exists; the review is built from the cached primary literature below.
- Re-fetched full text (force) for PMID:33023933, PMID:31477916 and PMID:27974379; the previous
  cache entries were abstract-only. Abstracts were unchanged apart from trailing whitespace.

### Evolutionary grounding
- UniProt: PANTHER PTHR13195:SF0 (PSEUDOURIDYLATE SYNTHASE TRUB2, MITOCHONDRIAL), InterPro
  IPR039048 (Trub2), Pfam PF01509 (TruB_N), CDD cd02868 (PseudoU_synth_hTruB2_like); "Belongs to
  the pseudouridine synthase TruB family." Active-site nucleophile Asp98 is by similarity to
  TRUB1 (Q9Y606), ECO:0000250, not experimentally mutated in TRUB2.
- TRUB1 (nuclear) is a paralog in a different subfamily; its functions are not transferred here.
- PAINT (interpro/panther/PTHR13195/PTHR13195-paint.tsv): node PTN000324318 (taxon 33213,
  Bilateria) carries IBD for GO:0005759 mitochondrial matrix, GO:0009982 pseudouridine synthase
  activity, GO:0070131 positive regulation of mitochondrial translation and GO:1990481 mRNA
  pseudouridine synthesis, all seeded only by human TRUB2 (O95900). The PAINT curator did NOT
  place GO:0160148 tRNA pseudouridine(55) synthase activity or GO:0070902 mitochondrial tRNA
  pseudouridine synthesis on the node, although human TRUB2 carries both by IMP (PMID:33023933).
  For transfer purposes the tRNA-Psi55 terms should be treated as human-experimental only, not as
  PAINT-sanctioned inherited functions.

### Literature
- Antonicka et al. 2017 (PMID:27974379, full text): TRUB2 is in mitochondrial RNA granules, in a
  BioID module with RPUSD3, RPUSD4, FASTKD2, MTERFD1, WBSCR16 (RCC1L), NGRN.
  [PMID:27974379 "Using BioID, we reciprocally confirmed the specific interaction of TRUB2 with all these proteins"]
  siRNA depletion: [PMID:27974379 "was decreased to 76, 20, and 53% of control in cells in which TRUB2, RPUSD4, and RPUSD3 were depleted"];
  ATP8/ATP6 synthesis specifically reduced. Psi-seq: [PMID:27974379 "Depletion of both TRUB2 and RPUSD3 resulted in decreased pseudouridylation in the COXI"]
  BUT the authors argue [PMID:27974379 "three lines of evidence suggest that RPUSD3 is the major modifying enzyme for COXI and COXIII mRNA and that the effect of TRUB2 is secondary"],
  including that TRUB2 knockdown halves RPUSD3 mRNA. So direct TRUB2 catalysis on mt-mRNA in vivo is
  not established. A putative mt-tRNA position-55 site was seen but not verified.
- Mukhopadhyay et al. 2021 (PMID:33023933, full text): recombinant human TRUB2 (E. coli) has tRNA
  Psi55 synthase activity in vitro on tRNA transcripts (tRNATrp, tRNAAla), requiring U54-A58 and
  enhanced by m1A58; TRUB2 knockdown reduced Psi55 synthesis by mitochondrial extracts.
  [PMID:33023933 "We show here that all three human recombinant proteins, TRUB1, PUS10, and TRUB2, have Ψ55 synthase activities, but differ slightly in their tRNA structural requirements."]
  The in vivo mt-tRNA targets are only suggested: [PMID:33023933 "TRUB2 is present in the mitochondria and is suggested to produce Ψ55 in all four human mitochondrial tRNAs (out of 22 total) with this modification"].
  This is the strongest direct biochemical evidence for TRUB2 catalysis.
- Carlile et al. 2019 (PMID:31477916, full text): in vitro pseudouridylation of a human mRNA
  fragment pool by recombinant TRUB2 identified one site, in a cytosolic mRNA, which the authors
  think is probably not physiological.
  [PMID:31477916 "The modification of a cytosolic mRNA by TRUB2 was unexpected given the predominantly mitochondrial localization of this enzyme"]
  This supports mRNA-directed Psi synthase activity in vitro only.
- Arroyo et al. 2016 (PMID:27667664): CRISPR death screen for OXPHOS genes; TRUB2 in an
  NGRN-centred module required for 16S rRNA abundance and mitochondrial translation.
- Jourdain et al. 2017 (PMID:28082677): TRUB2 enriched in mitochondrial RNA granules (MRGs) by
  immunofluorescence; co-IP with MRG proteins.
- Morgenstern et al. 2021 (PMID:34800366): MitoCoP high-confidence mitochondrial proteome (HTP).
- Castello 2012 / Baltz 2012: mRNA interactome capture (HDA RNA binding).

### Synthesis
Experimentally established in human: mitochondrial matrix / RNA-granule localization; tRNA Psi55
synthase activity of the recombinant enzyme; contribution to mitochondrial-extract Psi55
activity; requirement for normal mitochondrial translation (especially ATP8/ATP6) and OXPHOS;
membership of the RPUSD3/RPUSD4/NGRN/RCC1L/FASTKD2 module. Weakly established: direct
pseudouridylation of mt-mRNAs (COX1/COX3), which may be secondary to RPUSD3. Inferred only:
active-site Asp98 (by similarity).

Annotation decisions: ACCEPT matrix, granule, pseudouridine synthase activity, tRNA Psi55
synthase activity, mitochondrial tRNA Psi synthesis; KEEP_AS_NON_CORE mRNA pseudouridine
synthesis (minor/secondary), positive regulation of mitochondrial translation (necessity
phenotype; PAINT-sanctioned but not a regulatory activity), and RNA binding; MODIFY the
general IEA process terms and the "mitochondrion" rows to the specific supported terms.

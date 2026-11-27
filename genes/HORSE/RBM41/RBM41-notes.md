# RBM41 (horse, A0A3Q2GZN1) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Cohort DONKEY40_HORSE_PARTNER (partner of donkey A0A9L0IK51, genes/EQUAS/RBM41, reviewed by another agent). No ProtNLM2 file or prediction-evidence folder was opened.

### Deep research
`just deep-research-falcon HORSE RBM41 --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite fallback HTTP 401 (insufficient quota). No deep-research file exists. The review rests on the one primary RBM41 paper, cached with full text: Norppa et al. 2024 (PMID:38499487).

### Identity of the benchmark accession
- A0A3Q2GZN1 is TrEMBL (PE 4), 437 aa, Ensembl ENSECAP00000026517.2, chromosome X. Human RBM41 canonical Q96IZ5-1 is 413 aa.
- Global alignment [file:HORSE/RBM41/RBM41-bioinformatics/RESULTS.md "Global alignment: 397/413 identical paired residues (96.13% identity)"]. Every human residue is paired. The one horse-only stretch is 175-198.
- That stretch is the exon peptide that defines human isoform 3 [file:HORSE/RBM41/RBM41-bioinformatics/RESULTS.md "Human isoform-3 inserted peptide (VSP_021346, after human Q174): AYHKKTSADKYMTSMKRKIKLGTK"]. Horse carries it at position 175. Human isoform 3 also loses the C-terminal RRM region (VSP_021347/VSP_021348). The horse model does not: it keeps the whole RRM and C terminus [file:HORSE/RBM41/RBM41-bioinformatics/RESULTS.md "78 of 79 human residues identical (79 paired)"].
- So the horse entry is a full-length alternative splice model: the human isoform 1 sequence plus the optional 24-aa exon. It is not a fragment, and nothing is missing. The extra exon sits in the N-terminal region, away from the RNA-binding RRM. The donkey model has the same insertion (donkey RESULTS.md, range 175-198).
- No reviewed (Swiss-Prot) horse RBM41 entry exists, so there is no separate horse canonical product to review.
- GN carries "Synonyms=MORC4" from a VGNC:20264 cross-reference. MORC4 is a different gene: an X-linked neighbour of RBM41 in mammals. This is a gene-model/xref artefact in the UniProt entry and says nothing about function.

### Family / phylogeny
- PANTHER PTHR16105 (RBM41/RNPC3 family). Horse is in SF2 "RNA-BINDING PROTEIN 41", with human Q96IZ5 and mouse Q8JZV4 (interpro/panther/PTHR16105/PTHR16105-entries.csv). The paralog U11/U12-65K (RNPC3; human Q96LT9, Arabidopsis SNRNP65) is in SF0.
- The IBA rows come from PTN000413238. Its donors are 65K orthologs: Arabidopsis AT1G09230, fly FBgn0265184, zebrafish rnpc3 and human Q96LT9. This node therefore sits above the RBM41/65K duplication. Norppa et al. show the duplication is ancient [PMID:38499487 "solidifies it as resulting from an ancient duplication and having been present in LECA"]. Functions common to both paralogs (binding the U12 3' stem-loop, membership of the minor spliceosome) can transfer from that node. Functions specific to 65K (U11-59K interaction, intron recognition in the U11/U12 di-snRNP) cannot, and PAINT did not propagate any such term.

### Experimental evidence on the SF2 ortholog (human RBM41), PMID:38499487 (full text)
- RNA binding: the RRM binds U12 and U6atac 3'-terminal stem-loops [PMID:38499487 "The two paralogous proteins have a similar shared dual RNA binding specificity in vitro, interacting with the same 3′-terminal stem-loops of U12 and U6atac snRNAs with approximately equal affinity"]. The EMSA construct is human residues 267-413, and horse is identical at 139 of its 147 residues (RESULTS.md).
- Complexes: [PMID:38499487 "Together these results suggest that RBM41 is present in the minor spliceosome post catalytic (P) and intron lariat spliceosome (ILS) complexes"]; [PMID:38499487 "RBM41 preferentially co-immunoprecipitated U12-type but not U2-type intron lariats"]. It is also present in the U12 mono-snRNP. The lariat association is a co-IP, so it does not show that RBM41 contacts intronic RNA directly.
- Localisation: [PMID:38499487 "Consistently, we found that endogenous RBM41 localizes to Cajal bodies, as shown by colocalization with coilin-GFP in HEK293 cells"].
- Process: KO HEK293 cells are viable, with weak changes to U12-type 3'ss choice [PMID:38499487 "Based on the weak, yet statistically significant effects of RBM41 knockout in human HEK293 cells specifically on 3′ss selection of U12-type introns"]. The model places RBM41 in the post-splicing steps and minor spliceosome disassembly.

### Decisions
- GO:0030626 U12 snRNA binding (IBA): ACCEPT. PAINT node, plus direct EMSA on the SF2 ortholog.
- GO:0005689 U12-type spliceosomal complex (IBA): ACCEPT. The stage evidence (P/ILS) is hedged and comes from one paper, so I do not refine it to post-spliceosomal subtypes.
- GO:0000398 mRNA splicing, via spliceosome (IBA): ACCEPT. RBM41 is a minor spliceosome component, and KO affects U12-type 3'ss selection.
- GO:0097157 pre-mRNA intronic binding (IBA): MARK_AS_OVER_ANNOTATED. The RRM binds snRNA. The intron-lariat association is indirect (co-IP), and the only donor is Arabidopsis 65K.
- GO:0003676 nucleic acid binding and GO:0003723 RNA binding (IEA): MODIFY to U12 snRNA binding plus U6atac snRNA binding.
- NEW GO:0030624 U6atac snRNA binding: EMSA on the human SF2 ortholog. The RRM is 78/79 identical in horse.
- NEW GO:0015030 Cajal body: localisation of the endogenous SF2 ortholog. The protein is RNA-binding dependent and cycles with the U12 mono-snRNP.

### Relative
- Human RBM41 (Q96IZ5), same PANTHER subfamily SF2. It is the only experimentally characterised member of SF2. There is no genes/human/RBM41 review in the repo, so it needs review.

## 2026-10-23 — PR #5309 review follow-up

The reviewer-proposed NEW rows transferred from PMID:38499487 are orthology-based, so evidence_type is
now ISS rather than IEA, consistent with the other NEW rows in this PR.

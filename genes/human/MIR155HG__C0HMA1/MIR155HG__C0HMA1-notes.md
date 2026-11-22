# miPEP155 / P155 (UniProt C0HMA1, gene symbol MIR155HG) — curation notes

Folder uses the repo's `<HOST>__<ACC>` convention for alternative-ORF peptides: the peptide
has its own UniProt entry (C0HMA1, P155_HUMAN) but UniProt files it under the host gene
symbol `MIR155HG` (HGNC:35460), the miR-155 host gene / BIC lncRNA. It must not be merged
with the host locus folder `genes/human/MIR155HG/`.

## What it is

- 17 aa peptide (`MEMALMVAQTRKGKSVV`), PE1 (evidence at protein level), no domains, no TM,
  1879 Da. UniProt feature `PRO_0000459474` covers residues 1..17 (the whole chain).
- Encoded by a 54-bp sense sORF ("ORF1") inside the human MIR155HG transcript, which is
  annotated as non-coding and is the primary transcript for miR-155
  [PMID:32671205 "ORFfinder was used to search for ORFs within human MIR155HG, and a 54–base pair (bp) small ORF was predicted to harbor coding potential among all the sense small ORFs"].
- Endogenous existence established three ways in the primary paper: CRISPR/Cas9 C-terminal
  EGFP knock-in at the ORF1 stop codon in HEK293T
  [PMID:32671205 "To determine whether the start codon of ORF1 is active, we introduced an enhanced green fluorescent protein (EGFP) tag (without its own start codon) into the C terminus of ORF1"],
  a peptide-specific antibody, and LC-MS of antibody immunoprecipitates
  [PMID:32671205 "To provide direct evidence of the existence of P155, we performed liquid chromatography–mass spectrometry (LC-MS) on cell-derived immune precipitates, which were generated using P155 antibodies."].
  Independently reproduced: the spliced pri-miR-155 transcript expresses miPEP155 in HeLa
  [PMID:33810468 "These results indicate that the spliced pri-miR-155 transcript is translatable and able to express miPEP155 in Hela cells."].

## Function (Niu et al. 2020, Sci Adv, PMID:32671205 — verified via PubMed/UniProt; journal is
Sci Adv, not Nat Commun)

- MIR155HG is induced in antigen-presenting cells in inflamed (psoriatic) dermis, not at
  steady state [PMID:32671205 "we found that MIR155HG was highly expressed by APCs in inflammation but not at steady state"].
- Target identification in **human** monocyte-derived DCs: biotin-P155 pull-down + silver
  stain + LC-MS + immunoblot identified a ~73 kDa partner as HSC70 (HSPA8)
  [PMID:32671205 "Using LC-MS and confirmative immunoblotting, we recognized this 73-kDa protein to be HSC70"];
  competition with free peptide established specificity. Also confirmed in human
  THP-1-derived DCs [PMID:32671205 "P155 is bound to HSC70 in THP-1–derived DCs treated with R848 (fig."].
- Binding is domain-selective (ATPase/NBD, not the SBD) and inhibits HSC70 ATPase activity
  [PMID:32671205 "P155 did not bind to the general peptide-binding region, namely, the SBD domain of HSC70, but selectively bound to the ATPase region of HSC70 and suppressed the ATPase activity of full-length HSC70, which is critical for the HSC70-mediated chaperon cycle of peptide transportation (30)."].
  ATPase assay used recombinant **human** HSPA8 protein plus synthetic peptide
  [PMID:32671205 "Moreover, P155 remarkably impaired the ATPase activity of full-length HSC70, which functionally supported P155’s binding specificity (Fig."].
- Downstream consequences were measured in **mouse** bone marrow-derived DCs: weakened
  HSC70–HSP90 and HSC70–LAMP2A co-IP, less OVA delivery to LAMP2A+ lysosomes, reduced
  MHC class II, reduced OT-II CD4+ T cell proliferation
  [PMID:32671205 "A weakened interplay between HSC70 and HSP90 as well as LAMP2A was detected in BMDCs cultured in the presence of P155 compared to BMDCs treated with Scr, which coincided with impaired lysosomal antigen trafficking observed in P155-treated BMDCs (Fig."],
  [PMID:32671205 "We found that P155 treatment remarkably decreased MHC class II expression in BMDCs stimulated with R848, supporting the proposed model that P155 modulates antigen presentation (Fig."].
- Therapeutic effect of exogenous synthetic peptide in two mouse models (MOG-EAE,
  imiquimod psoriasis-like skin inflammation)
  [PMID:32671205 "P155 treatment resulted in lower clinical scores of EAE compared to the Scr-treated controls, and P155 did not present general toxicity as indicated by untouched body weights (Fig."].

## Species caveat (important)

The peptide-coding sequence is **not** present in the mouse genome per the primary paper
[PMID:32671205 "Although the coding sequences of P155 were not found in the mouse genome, we noticed that murine and human HSC70 share 99.85% homology (fig. S3A), and both ATPase and SBD domains of HSC70 are exactly the same in human and mouse."].
Mouse BMDC and in vivo work therefore tests the **human** peptide acting on mouse HSC70,
which is essentially identical to human HSC70 in both domains. A second group describes the
peptide as "extremely well conserved in primates and partially conserved in mice"
[PMID:33810468 "The miPEP155 is extremely well conserved in primates and partially conserved in mice (Figure S2)."],
so conservation outside primates is contested. Practical consequence for GO: the molecular
interaction (HSPA8 binding, ATPase inhibition) is demonstrated with human proteins, while
the cell-biological outcome (antigen trafficking, MHC-II, T cell priming) rests mainly on
mouse cells treated with the human peptide. The UniProt/GOA IDA rows are defensible, but
all of them derive from **exogenously supplied synthetic peptide at 25 µM**, not from
loss of function of the endogenous peptide. No peptide-specific knockout or knockdown
(which is hard here: the ORF sits inside the miR-155 primary transcript) has been reported.

## What it does NOT do

Unlike plant miPEPs and human miPEP133, miPEP155 does not autoregulate its own host
pri-miRNA or the activity of miR-155
[PMID:33810468 "Thus, from our results we conclude that miPEP155 and miPEP497 do not regulate the levels of their own pri-miRNAs and consequently the activity of the processed miRNAs."];
instead it appears functionally antagonistic to miR-155
[PMID:33810468 "Our results are consistent with the idea that miPEP155 has an antagonistic role to miR-155."].
This is a useful negative result: no transcription-regulation GO terms should be inferred
for this peptide. A third paper reports that MIR155HG promotes NK-cell proliferation
"without reliance on its derived miR-155 and micropeptide P155" (PMID:40486832, Acta Pharm
Sin B 2025) — i.e. a host-RNA function explicitly separable from the peptide; not cached and
not used as support for any annotation here.

## Annotation decisions

- `GO:0030544 Hsp70 protein binding` (IPI, WITH UniProtKB:P11142) — ACCEPT. Informative MF,
  not bare `protein binding`; HSPA8 is the correct partner and the pull-down/LC-MS/PLA
  evidence is in human cells.
- `GO:0002605 negative regulation of dendritic cell antigen processing and presentation`
  (IDA) — ACCEPT, core. Direction and cell type are right; caveat recorded that readouts
  were in mouse BMDCs with exogenous human peptide.
- `GO:0005737 cytoplasm` / `GO:0005634 nucleus` (IDA, and the GO_REF:0000044 SubCell
  mappings SL-0086/SL-0191) — ACCEPT for cytoplasm (where HSC70 and the CMA/MHC-II
  trafficking machinery operate); nucleus kept but flagged as non-core, since it rests on
  immunofluorescence of FITC-synthetic peptide colocalising with antibody-detected
  endogenous peptide in HEK293T and no nuclear activity is known
  [PMID:32671205 "we first showed that fluorescein isothiocyanate (FITC)–labeled synthetic P155 efficiently entered HEK293T cells and colocalized with endogenous P155 in both cytoplasmic and nuclear compartments of the cells (fig. S1F)."].
  The two IEA rows are UniProt SubCell mappings of the same primary evidence — correct, and
  not circular in the sense CLAUDE.md reserves for IBA chains, but redundant with the IDA rows.
- NEW `GO:0042030 ATPase inhibitor activity` — proposed. Participation test is satisfied at
  the molecular level: the peptide itself binds the HSC70 nucleotide-binding domain and the
  measured ATP hydrolysis of recombinant human HSPA8 falls in its presence. This is the
  mechanistically informative MF, and it is what makes the BP term intelligible; the
  existing `Hsp70 protein binding` row records only the physical interaction.
- Not proposed: `GO:0002587 negative regulation of antigen processing and presentation of
  peptide antigen via MHC class II`. The MHC-II specificity is real but the GOA row
  GO:0002605 already captures the regulated process in the right cell type, and adding an
  overlapping sibling would be over-annotation on evidence from one paper. Raised as a
  suggested question instead.
- Not proposed: any `chaperone-mediated autophagy` term. The peptide inhibits a chaperone
  that performs that process; impairing someone else's machine is regulation of it, and the
  dedicated negative-regulation BP term already annotated covers the demonstrated outcome.

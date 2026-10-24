# OLFML2A: paired human–horse review notes

## Biological evidence

Photomedin-1/OLFML2A is distinct from photomedin-2/OLFML2B and OLFM2. Mouse recombinant experiments establish secretion, disulfide-linked oligomerization, and binding to sulfated glycosaminoglycans. Human podocyte imaging supports a relevant glomerular protein pool. Matrix binding does not by itself demonstrate matrix assembly or a defined signaling receptor.

- [PMID:15836428: Identification and characterization of photomedins: novel olfactomedin-domain-containing proteins with chondroitin sulphate-E-binding activity.](https://pubmed.ncbi.nlm.nih.gov/15836428/) — abstract cached; full-text availability must be checked separately.
- [PMID:18757743: Transcriptome-based systematic identification of extracellular matrix proteins.](https://pubmed.ncbi.nlm.nih.gov/18757743/) — abstract cached; full-text availability must be checked separately.
- [PMID:22913984: Neuronal proteins are novel components of podocyte major processes and their expression in glomerular crescents supports their role in crescent formation.](https://pubmed.ncbi.nlm.nih.gov/22913984/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The selected horse model lacks the human1–27 signal-peptide region and an internal segment. Its olfactomedin domain is strongly conserved, but normal secretory entry and maturation are unresolved. Consequently extracellular localization, binding and organization are UNC for this exact model despite a reasonable extracellular family default.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/OLFML2A/OLFML2A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Check horse transcript starts and test secretory targeting. Trace the extracellular-matrix screen at gene/assay level before making a specific matrix-organization claim. Cancer-expression/knockdown associations in the Edison report are leads, not a demonstrated receptor mechanism.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Identity
- Q68BL7 is the reviewed, canonical human OLFML2A entry (isoform 1, 652 aa; signal peptide 1-27, coiled coil 157-183, OLF domain 394-652). Isoforms 2 and 3 (VSP_029565-7) are alternative splice products of the same entry. The benchmark accession is therefore the canonical product, not a fragment or alternative gene model. (The truncated/leaderless gene model problem belongs to the horse entry A0A9L0SKW1, not this one.)
- PANTHER PTHR23192:SF29 (OLFACTOMEDIN-LIKE PROTEIN 2A), the same subfamily as mouse Olfml2a Q8BHP7 (checked in UniProt REST, 2026-10-20). Mouse Q8BHP7 is the experimentally characterized one-to-one ortholog; all human GO rows other than the IBAs derive from it.

### Evidence
- Mouse photomedin-1: secreted, disulfide-bonded dimer, O-glycosylated, cleaved mid-molecule after secretion; photomedins preferentially bind chondroitin sulfate E and heparin [PMID:15836428 "Among a panel of ECM components, including glycosaminoglycans, photomedins preferentially bound to chondroitin sulphate-E and heparin."]. Mouse UniProt attributes heparin/CS-E binding to Olfml2a with ECO:0000269 from this paper; human UniProt carries it by similarity ("Binds to heparin and chondroitin sulfate E."). Full text (PMC1180717) re-fetch attempted 2026-10-20: abstract only.
- Mouse GOA (QuickGO 2026-10-20): ECM binding IDA, identical protein binding IPI, ECM IDA (PMID:15836428, PMID:18757743), ECM organization acts_upstream_of_or_within IDA (PMID:18757743). The ECM-organization row was not transferred to human and the PANTHER family review rates it UNRESOLVED; not proposed.
- Podocyte major-process localization [PMID:22913984 "These proteins were expressed exclusively by podocytes, wherein they localized to major processes"].
- Cancer literature (AP-1/TNBC, AML prognosis; from the falcon report) is expression regulation/association, not molecular function.

### PAINT
- PTN000573635 is the bilaterian root of PTHR23192 (taxon:33213). It carries extracellular region (13 donors) and signal transduction (3 donors: Q99972 human myocilin, MGI:1202864, MGI:1860437). MGI:1202864 + Q99972 also seed the myocilin-only node PTN002754680 (Golgi, osteoblast differentiation), i.e. curators kept those myocilin terms off the root deliberately. Signal transduction for OLFML2A left UNDECIDED: formally inherited, no evidence of loss, but no OLFML2-subfamily support.

### Decisions
- Extracellular region (IBA/IEA/ISS): ACCEPT. ECM (IEA): ACCEPT. ECM binding (IEA): ACCEPT. Identical protein binding: KEEP_AS_NON_CORE.
- NEW: chondroitin sulfate binding (GO:0035374) and heparin binding (GO:0008201), ISS from the SF29 ortholog. These are not is_a descendants of GO:0050840 (OLS ancestors checked), so they are added alongside rather than as a MODIFY.
- Core function MF changed from ECM binding to chondroitin sulfate binding.

### Relative / family / modules
- Next relative: mouse Olfml2a (Q8BHP7), ortholog in SF29; no review in repo.
- interpro/panther/PTHR23192/PTHR23192-review.yaml places Q68BL7 in SF29, consistent with UniProt. No disagreement.
- No module under modules/ mentions OLFML2A/photomedin.

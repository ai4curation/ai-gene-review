---
title: "ProtNLM benchmark proteins without a PANTHER assignment"
autolink_gene_symbols: false
---

# Family curation beyond PANTHER coverage

**All 18 unassigned benchmark inputs have an individual family/domain assessment below.** Three have verified same-gene canonical context: **mcm-4, UBE2F and Spcs2**. Their exact short inputs remain unassigned; canonical functions must not replace the sequences ProtNLM actually received. Other proteins have informative domain assignments despite absent PANTHER coverage.

The most distinctive evolutionary lead is **Spo2**: its entire 133-residue sequence is exactly the C-terminus of 3131-residue Vps1302, while PomBase assigns the two records to different loci. This is a concrete relationship to investigate, not yet evidence of gene duplication, catalytic loss or annotation error.

| Exact input | Gene/context | Length | Current family assessment |
|---|---|---:|---|
| [Q9L243](https://www.uniprot.org/uniprotkb/Q9L243/entry) | STRCO/Q9L243 | 171 | HAD_SAK_2-domain candidate; substrate unresolved |
| [S0EDH7](https://www.uniprot.org/uniprotkb/S0EDH7/entry) | GIBF5/S0EDH7 | 342 | Kinase-like structural superfamily; catalytic class unresolved |
| [Q2U1U6](https://www.uniprot.org/uniprotkb/Q2U1U6/entry) | ASPOR/Q2U1U6 | 134 | Short chondroitin-lyase-like structural match; enzyme unresolved |
| [A0A061AL94](https://www.uniprot.org/uniprotkb/A0A061AL94/entry) | CAEEL/A0A061AL94 | 74 | Verified mcm-4 gene context; isolated MCM4 C-terminal sequence |
| [A2FPI7](https://www.uniprot.org/uniprotkb/A2FPI7/entry) | TRIV3/A2FPI7 | 129 | KilA-N/APSES DNA-binding domain family |
| [F7A4N8](https://www.uniprot.org/uniprotkb/F7A4N8/entry) | HORSE/CTDSP2 | 174 | Short CTDSP2 gene model; canonical phosphatase context insufficient |
| [Q8IPG8](https://www.uniprot.org/uniprotkb/Q8IPG8/entry) | DROME/CG31606 | 197 | Unclassified secreted fly protein; apolipoprotein placement unsupported |
| [A0A0B4LGP2](https://www.uniprot.org/uniprotkb/A0A0B4LGP2/entry) | CG45100 (DROME) | 38 | Hdac3 upstream-ORF microprotein; no deacetylase family inference |
| [M9NF85](https://www.uniprot.org/uniprotkb/M9NF85/entry) | CG32086 (DROME) | 475 | EFHB C-terminal EF-hand domain protein |
| [Q7KVQ7](https://www.uniprot.org/uniprotkb/Q7KVQ7/entry) | Tango5 (DROME) | 428 | VMP1-related membrane architecture without PANTHER coverage |
| [Q8MZA7](https://www.uniprot.org/uniprotkb/Q8MZA7/entry) | CG13494 (DROME) | 120 | Small membrane protein CG13494; family unresolved |
| [Q9VN74](https://www.uniprot.org/uniprotkb/Q9VN74/entry) | CG14662 (DROME) | 550 | LRR-related membrane protein CG14662; receptor mechanism unresolved |
| [C6Y4C2](https://www.uniprot.org/uniprotkb/C6Y4C2/entry) | spo2 (SCHPO) | 133 | Spo2 is a short VPS13 C-terminal-derived protein at a distinct annotated locus |
| [Q7S3T0](https://www.uniprot.org/uniprotkb/Q7S3T0/entry) | NEUCR/NCU04937 | 114 | Short coiled-coil protein; DNA-binding family unresolved |
| [V5ILC0](https://www.uniprot.org/uniprotkb/V5ILC0/entry) | NEUCR/NCU12035 | 232 | GNAT-domain acetyltransferase candidate; substrate unresolved |
| [F8WDQ9](https://www.uniprot.org/uniprotkb/F8WDQ9/entry) | UBE2F (human) | 101 | Verified UBE2F gene context; truncated alternative UBC product |
| [A0A140LHW5](https://www.uniprot.org/uniprotkb/A0A140LHW5/entry) | Spcs2 (mouse) | 74 | Verified Spcs2 gene context; short product lacks canonical membrane architecture |
| [Q18287](https://www.uniprot.org/uniprotkb/Q18287/entry) | C28G1.2 (worm) | 265 | Serpin-fold protein; inhibitory mechanism unresolved |

## Verified gene-context bridges

The shared MOD identifiers establish gene identity; sequence comparisons establish which part of the canonical protein the short product actually retains.

| Exact input | Same-gene reviewed reference | Shared MOD ID | Canonical PANTHER assignment | Observed sequence relationship |
|---|---|---|---|---|
| A0A061AL94 (74 aa) | [Q95XQ8](https://www.uniprot.org/uniprotkb/Q95XQ8/entry) (823 aa) | WBGene00003156 | PTHR11630, PTHR11630:SF66 | Exact residues 750–823 |
| F8WDQ9 (101 aa) | [Q969M7](https://www.uniprot.org/uniprotkb/Q969M7/entry) (185 aa) | HGNC:12480 | PTHR24067 | First 94 residues identical, followed by a distinct short tail |
| A0A140LHW5 (74 aa) | [Q9CYN2](https://www.uniprot.org/uniprotkb/Q9CYN2/entry) (226 aa) | MGI:1913874 | PTHR13085, PTHR13085:SF0 | First 66 residues identical, followed by a distinct short tail |

## Individual assessments

### STRCO/Q9L243 — Q9L243

Pfam PF18143 (HAD_SAK_2) supplies a domain-level relationship for this 171-residue Streptomyces protein. The current name 'Secreted protein' is explicitly ProtNLM-derived and does not independently validate secretion. Neither a specific 5-prime-nucleotidase reaction nor deoxyribonucleotide catabolism follows from the domain assignment.

**Next evidence:** Resolve full HAD-domain architecture and catalytic residues, compare the substrate-recognition region with experimentally characterized HAD_SAK_2 proteins, and test nucleotide versus non-nucleotide substrates.

**Evolutionary value:** Useful substrate-divergence candidate if a characterized HAD_SAK_2 clade can be established; not yet a defensible nucleotidase family.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q9L243/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASCO2678+AND+organism_id%3A100226&format=json&size=100).

### GIBF5/S0EDH7 — S0EDH7

InterPro IPR011009 identifies a kinase-like structural superfamily in the 342-residue Fusarium protein, but no specific protein-kinase family or catalytic-site assignment is present. The recommended kinase-domain name is ProtNLM-derived. A structural fold relationship alone does not establish ATP binding or protein phosphorylation.

**Next evidence:** Recover a structure-supported alignment spanning the nucleotide-binding and catalytic regions, distinguish active protein kinases from other kinase-like proteins, and establish the target gene model.

**Evolutionary value:** Potential divergent kinase or kinase-like nonenzyme case, provided catalytic competence is tested rather than presumed from the name.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/S0EDH7/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AFFUJ_06423+AND+organism_id%3A1279085&format=json&size=100).

### ASPOR/Q2U1U6 — Q2U1U6

The 134-residue Aspergillus sequence has only InterPro IPR008929, a chondroitin-lyase-like structural relationship. This does not establish a complete polysaccharide-degrading enzyme. Lyase chemistry and hydrolysis are different mechanisms, and neither is established by the short fold match.

**Next evidence:** Check transcript/gene-model completeness and whether the sequence covers a diagnostic catalytic domain; then compare the actual active-site architecture with characterized polysaccharide enzymes.

**Evolutionary value:** A useful fragment-versus-divergent-enzyme control, but too incomplete for confident substrate-family placement.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q2U1U6/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAO090138000091+AND+organism_id%3A510516&format=json&size=100).

### CAEEL/A0A061AL94 — A0A061AL94

The target has the WormBase gene identifier WBGene00003156 and Pfam PF21128 (WHD_MCM4). The reviewed full-length record Q95XQ8 shares that gene identifier and maps to PTHR11630:SF66. Direct sequence comparison shows the entire 74-residue target is exactly Q95XQ8 residues 750–823. This licenses MCM4 gene context, not ATPase/helicase activity, nuclear targeting or complex incorporation of the fragment itself.

**Next evidence:** Establish whether the short transcript produces a stable protein and whether its winged-helix region has independent interactions. Retain the short exact input when evaluating ProtNLM.

**Evolutionary value:** Strong domain-isolation control for propagation from full-length MCM4. The observed relationship is alternative gene-product structure, not evidence of evolutionary loss of helicase activity.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/A0A061AL94/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3Amcm-4+AND+organism_id%3A6239&format=json&size=100).

### TRIV3/A2FPI7 — A2FPI7

Pfam PF04383 and InterPro IPR017880/IPR018004 identify a KilA-N/APSES helix-turn-helix module; the domain spans residues 19–124 of a 129-residue protein. This is an informative domain-family assignment despite absent PANTHER coverage. It supports a broad DNA-binding inference without specifying a target sequence or regulatory program. The record lists two Trichomonas ORF identifiers, so locus provenance also needs attention.

**Next evidence:** Compare full KilA-N domains with characterized regulators and inspect genomic context for the two listed ORFs. Resolve DNA-recognition residues and regulatory partners before assigning a transcriptional role.

**Evolutionary value:** Interesting cross-lineage and mobile-element-associated DNA-binding module; investigate domain distribution without assuming horizontal transfer from domain presence alone.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/A2FPI7/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATVAG_233530+AND+organism_id%3A412133&format=json&size=100).

### HORSE/CTDSP2 — F7A4N8

The horse record names CTDSP2 and carries ENSECAG00000018788.4, but its 174-residue sequence has no diagnostic phosphatase or kinase domain assignment. The existing reproducible human–horse comparison reports a match to part of human CTDSP2 and loss/divergence across the catalytic region. The current horse gene search returned no longer same-gene record, so no verified horse canonical bridge is available.

**Next evidence:** Resolve the horse transcript and exon model against the genomic locus and an intact ortholog. A CTDSP2 gene-name assignment must not substitute for catalytic-domain evidence in the exact target.

**Evolutionary value:** Gene-model control for kinase-versus-phosphatase predictions; distinguish incomplete annotation from a real truncated isoform before interpreting functional divergence.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/F7A4N8/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTDSP2+AND+organism_id%3A9796&format=json&size=100).
Existing analysis: [RESULTS.md](https://github.com/ai4curation/ai-gene-review/blob/main/genes/HORSE/CTDSP2/CTDSP2-bioinformatics/RESULTS.md).

### DROME/CG31606 — Q8IPG8

CG31606 has a SignalP-derived signal peptide at residues 1–18 and a soluble mature sequence, supporting secretion as an inference. No recognized family domain is assigned. The retained analytical report shows asymmetric structural similarity to a mammalian apolipoprotein donor; that partial match does not establish apolipoprotein orthology, lipid binding or lipid transport.

**Next evidence:** Find well-supported insect orthologs and test whether a full-length structural relationship survives signal-peptide removal and low-complexity controls. Ligand or lipid assays are needed for the proposed cargo function.

**Evolutionary value:** Interesting lineage-restricted secreted-protein case and a control for overinterpreting partial structure matches across distant taxa.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q8IPG8/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACG31606+AND+organism_id%3A7227&format=json&size=100).
Existing analysis: [RESULTS.md](https://github.com/ai4curation/ai-gene-review/blob/main/genes/DROME/CG31606/CG31606-bioinformatics/RESULTS.md).

### CG45100 (DROME) — A0A0B4LGP2

The current UniProt gene name is Hdac3-5'utr, with aliases CG45100 and Dmel_Hdac3_uORF and FlyBase FBgn0266539. The protein is 38 residues and has a predicted transmembrane helix at 12–30. This is not the full-length histone deacetylase HDAC3; genomic association with its transcript must not transfer deacetylase activity to the microprotein.

**Next evidence:** Verify the uORF transcript/translation evidence and membrane insertion experimentally, then assess conservation of the small ORF independently from conservation of the downstream Hdac3 coding sequence.

**Evolutionary value:** High-interest de novo/uORF microprotein candidate. Conservation of the host gene is not conservation of the peptide.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/A0A0B4LGP2/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACG45100+AND+organism_id%3A7227&format=json&size=100).

### CG32086 (DROME) — M9NF85

CG32086 has Pfam PF25325/InterPro IPR057428 and a domain assigned at residues 399–469. Two additional records share FlyBase FBgn0052086, with lengths 491 and 245 residues, but none has a PANTHER assignment. This supplies an EFHB-related domain relationship without resolving calcium-binding stoichiometry, target pathway or equivalence of all isoforms.

**Next evidence:** Align the EF-hand liganding loops and complete N-terminal architecture across the three same-gene products and characterized EFHB relatives. Confirm whether each product retains a functional calcium-binding module.

**Evolutionary value:** Useful domain-retention and splice-product comparison for calcium sensing; ligand competence must be evaluated rather than inferred from an EF-hand label.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/M9NF85/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACG32086+AND+organism_id%3A7227&format=json&size=100).

### Tango5 (DROME) — Q7KVQ7

Tango5 has independently assigned KMS1 N-terminal and VMP1 C-terminal domains (PF28607/IPR063065 and PF27639/IPR059828) and multiple membrane helices. A second same-FlyBase-gene record Q9W2S1 is longer (530 versus 428 residues) and also lacks PANTHER. This domain architecture supports a VMP1-related comparison; the ARBA-derived scramblase reactions in the record are not independent confirmation of the target reaction.

**Next evidence:** Compare the two FlyBase-matched protein models with experimentally characterized VMP1 proteins, check missing sequence/topology, and trace lipid-scrambling evidence to reconstituted assays and its conserved structural determinants.

**Evolutionary value:** Strong membrane-lipid biology candidate: analyze family-specific architecture and paralog specialization while controlling for alternative input models.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q7KVQ7/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATango5+AND+organism_id%3A7227&format=json&size=100).

### CG13494 (DROME) — Q8MZA7

The 120-residue target carries a predicted helix at residues 37–61 and no recognized InterPro/Pfam family. Another 120-residue record Q7KVM4 shares FlyBase FBgn0034671 but likewise has no PANTHER match. Membrane insertion does not establish a transport pore, receptor or particular organelle.

**Next evidence:** Compare same-gene records and conserved fly orthologs, assess topology and signal-anchor orientation, and seek interaction/localization evidence before assigning a specific membrane function.

**Evolutionary value:** Useful small membrane-protein conservation case; distinguish genuine lineage restriction from weak profile sensitivity for short proteins.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q8MZA7/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACG13494+AND+organism_id%3A7227&format=json&size=100).

### CG14662 (DROME) — Q9VN74

The 550-residue target carries InterPro IPR032675 (LRR structural superfamily) and predicted helices at residues 29–50 and 421–447. Q8T4D5 is a same-FlyBase-gene 550-residue record with no PANTHER match. LRR-mediated interaction is a reasonable architectural hypothesis, but ligand identity, receptor function and signaling mechanism are not established.

**Next evidence:** Resolve whether the N-terminal hydrophobic segment is a signal peptide or retained membrane helix, compare extracellular LRR organization with insect homologs, and investigate binding partners.

**Evolutionary value:** Interesting LRR architecture and receptor/scaffold diversification case; avoid assigning a named receptor family solely from repeats.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q9VN74/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACG14662+AND+organism_id%3A7227&format=json&size=100).

### spo2 (SCHPO) — C6Y4C2

Reviewed UniProt evidence places Spo2 in meiotic spindle-pole-body modification and forespore-membrane initiation. Its record states that its sequence is identical to the C-terminus of Vps13b. Direct comparison confirms all 133 residues equal Vps1302 O42926 residues 2999–3131. However, PomBase assigns distinct loci: spo2 SPBC16C6.14 and vps1302 SPBC16C6.02c. O42926 has PTHR16166:SF93, but this is a domain-relationship lead, not a same-gene canonical bridge and not proof of full VPS13 lipid-transfer activity in Spo2.

**Next evidence:** Inspect the overlapping genomic and transcript models, translation initiation, and primary Spo2 constructs to distinguish a separately expressed C-terminal product from gene-model overlap or misassigned products. Examine whether the terminal module mediates the experimentally observed Spo13/Spo15 interactions.

**Evolutionary value:** Highest-priority nontrivial case here: potential reuse of a VPS13 terminal module for sporulation. Do not infer duplication, evolutionary truncation or misannotation until locus and protein-expression evidence resolves the origin.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/C6Y4C2/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3Aspo2+AND+organism_id%3A284812&format=json&size=100).

The primary study reports: “Spo2 is a 15-kDa nonconserved protein.” It experimentally distinguishes Spo2 recruitment and interactions at the meiotic spindle pole body. Its description of Spo2 as nonconserved makes the exact VPS13-terminal relationship worth revisiting with current locus and transcript evidence. [Nakase et al., PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/). The full-length comparison record is [Vps1302 O42926](https://www.uniprot.org/uniprotkb/O42926/entry); its PomBase identifier is SPBC16C6.02c, versus SPBC16C6.14 for Spo2.

### NEUCR/NCU04937 — Q7S3T0

NCU04937 is 114 residues, with N-terminal disorder and a predicted coiled coil at 52–104. No diagnostic DNA-binding domain or protein family is assigned. A weak human THAP11 prediction donor does not establish a THAP DNA-binding fold, particularly where low-complexity and coiled-coil sequence can drive similarity.

**Next evidence:** Use composition-aware searches and structure comparisons to distinguish a conserved interaction helix from a genuine DNA-binding module. Seek fungal orthologs and direct localization/binding evidence.

**Evolutionary value:** A useful false-homology control for coiled-coil and low-complexity proteins; the current evidence does not justify a THAP family.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q7S3T0/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ANCU04937+AND+organism_id%3A367110&format=json&size=100).

### NEUCR/NCU12035 — V5ILC0

NCU12035 has an N-acetyltransferase domain spanning 3–184 of its 232 residues, with Pfam PF00583 and InterPro IPR000182/IPR016181. This provides a broad GNAT-fold assignment. It does not distinguish protein/histone, small-molecule or other acceptors and does not establish nuclear localization.

**Next evidence:** Compare the GNAT substrate-recognition regions and genomic context with experimentally characterized fungal enzymes. Verify acetyl-CoA utilization and acceptor specificity before assigning a narrow reaction or a chromatin function.

**Evolutionary value:** Good metabolic diversification candidate if a substrate-specific clade can be established; broad GNAT membership is too heterogeneous for a family-wide substrate prediction.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/V5ILC0/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ANCU12035+AND+organism_id%3A367110&format=json&size=100).

### UBE2F (human) — F8WDQ9

The 101-residue target and reviewed UBE2F Q969M7 share HGNC:12480 and ENSG00000184182.20. Q969M7 maps to PTHR24067 and is an experimentally supported NEDD8 E2, not a generic ubiquitin-only conjugase. The target shares the first 94 residues with the 185-residue canonical protein, followed by a distinct short tail; it therefore lacks the intact canonical UBC domain. The canonical active-site feature is at residue 116, outside the retained common prefix. A record caution also flags missing conserved residues. Canonical catalytic activity must not be transferred to this exact alternative product.

**Next evidence:** Validate the alternative transcript, translation and folding, and determine whether the short UBC fragment has any regulatory interaction or is an incomplete/nonproductive product. Retain NEDD8-versus-ubiquitin specificity in the full-length comparison.

**Evolutionary value:** Excellent isoform/truncation and modifier-specificity control. Do not describe an alternatively encoded short product as an evolved pseudoenzyme without independent evidence.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/F8WDQ9/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AUBE2F+AND+organism_id%3A9606&format=json&size=100).

The biochemical study establishes UBE2F as a NEDD8-conjugating enzyme and distinguishes its cullin specificity from UBE2M. That result concerns an intact enzyme, not the 101-residue benchmark product. [PMID:19250909](https://pubmed.ncbi.nlm.nih.gov/19250909/); [PMID:23300442](https://pubmed.ncbi.nlm.nih.gov/23300442/).

### Spcs2 (mouse) — A0A140LHW5

The 74-residue target and reviewed Spcs2 Q9CYN2 share MGI:1913874 and ENSMUSG00000035227.8. Q9CYN2 is 226 residues and maps to PTHR13085:SF0. The first 66 residues match exactly, followed by a distinct target tail; the canonical membrane helices at 87–107 and 112–132 are outside this shared region. The target is annotated as disordered throughout. SPCS2 is an accessory signal-peptidase-complex subunit, so even the intact canonical protein should not be conflated with the catalytic SEC11 subunit.

**Next evidence:** Check the short transcript/protein's expression and interactions; distinguish absent membrane incorporation from any retained N-terminal binding function. Use full-length SPCS2 only as same-gene family context.

**Evolutionary value:** Strong short-isoform versus complex-subunit function control; distinguish accessory-subunit participation from protease catalysis.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/A0A140LHW5/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASpcs2+AND+organism_id%3A10090&format=json&size=100).

### C28G1.2 (worm) — Q18287

The worm protein has Pfam PF00079 and three serpin-domain/superfamily assignments, but its 265-residue sequence has only a local serpin-domain feature at residues 96–199. The same-gene search recovered no alternative canonical record. Serpin folds occur in inhibitory and noninhibitory proteins, and domain membership does not establish a protease target or a functional reactive-center-loop mechanism.

**Next evidence:** Establish whether the complete serpin fold and reactive-center-loop insertion machinery are present; compare structure and loop sequence against characterized inhibitory and noninhibitory serpins, then test protease trapping rather than simple binding.

**Evolutionary value:** High-interest inhibitory-versus-noninhibitory serpin comparison once fold completeness and reactive-center-loop architecture are resolved; avoid equating missing PANTHER coverage with pseudoenzyme status.

Sources: [current UniProt record](https://www.uniprot.org/uniprotkb/Q18287/entry), [same-gene search](https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AC28G1.2+AND+organism_id%3A6239&format=json&size=100).

## Evidence and reproducibility

The [machine-readable results](unassigned-results.json) preserve all 18 assessments, explicit shared gene identifiers, additional same-gene records, domain assignments, sequence hashes and the three permitted gene-context bridges. The [additional source responses](unmapped-sources.jsonl.gz) contain full UniProt search results and primary-publication abstracts retrieved on 2026-09-10. Starting target records are frozen in [uniprot-records.jsonl.gz](uniprot-records.jsonl.gz), with successful replacements in [uniprot-retries.jsonl.gz](uniprot-retries.jsonl.gz).

Run `UV_NO_SYNC=1 uv run python projects/PROTNLM_EVALUATION/family-curation/unassigned-checks.py` to recompute the identifier and sequence relationships. These comparisons use current UniProt sequences. Identity to every prediction-time input sequence is a separate check. No new full-family alignment or phylogenetic reconstruction is claimed, and gene-name searches do not establish that distant homologs are absent.

PANTHER coverage is a database observation, not a verdict on biological function. In particular, a domain-level relationship can be informative without a PANTHER match, and a short same-gene record can fail to match a family whose intact canonical protein is well characterized.

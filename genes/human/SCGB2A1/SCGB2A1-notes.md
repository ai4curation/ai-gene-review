# SCGB2A1 (O75556) curation notes

## Identity
- Mammaglobin-B; synonyms lipophilin C (LIPHC), lacryglobin, mammaglobin-2 (MGB2), UGB3, secretoglobin family 2A member 1.
- 95 aa precursor; signal peptide 1-18 (protein-sequenced), mature chain 19-95 [file:human/SCGB2A1/SCGB2A1-uniprot.txt "SIGNAL 1..18" / "CHAIN 19..95"]. N-glycosylated at Asn68.
- Secreted; secretoglobin family, lipophilin subfamily [file:human/SCGB2A1/SCGB2A1-uniprot.txt "Belongs to the secretoglobin family. Lipophilin subfamily."].
- Homologous to mammaglobin-A (SCGB2A2) and to the C3 component of rat prostatein ("estramustine-binding protein") [PMID:9720917 "homologous to the rat prostatein C3 component and to human mammaglobin"].

## Subunit / molecular function
- Forms a covalent-style head-to-head heterodimer with lipophilin A / secretoglobin 1D1 (SCGB1D1, UniProt O95968), the "lipophilin AC" complex isolated from human tears [PMID:9720917 "We identified a novel heterodimeric protein, lipophilin AC, in human tears"; file:human/SCGB2A1/SCGB2A1-uniprot.txt "Heterodimer of a lipophilin A and a lipophilin C (mammaglobin B) monomer associated head to head"]. This is the basis for MODIFY of the bare GO:0005515 (IPI with O95968) to GO:0046982 protein heterodimerization activity.
- Putative small-hydrophobic-ligand/steroid binding: "May bind androgens and other steroids, may also bind estramustine" [file:human/SCGB2A1/SCGB2A1-uniprot.txt "May bind androgens and other steroids, may also bind estramustine"]; the secretoglobin/prostatein family are "typically steroid-regulated and steroid-binding molecules" [PMID:9720917 "steroid-regulated and steroid-binding molecules"]. This is a family-level inference ("May"), not experimentally demonstrated for SCGB2A1, so it is noted but not asserted as a NEW ligand-binding annotation.

## Expression / localization
- Secreted into tears (tear proteome), ocular glands, and respiratory/nasopharyngeal secretions; also prostate, breast, uterus, ovary, testis, salivary gland, thymus, trachea, kidney [file:human/SCGB2A1/SCGB2A1-uniprot.txt "steroid responsive tissues (prostate, testis, uterus, breast and ovary)"]. Expression in all ocular glands and eyelid/conjunctival epithelium [PMID:16395610 "expression of SCGB 2A1 in all ocular glands"]. HPA: group enriched (cervix, epididymis). All localization evidence (IDA tears/ocular, HDA tear proteomics) supports the Secreted extracellular compartment.

## Androgen annotations (GO:0030521) — over-annotation call
- SCGB2A1 is a transcriptional TARGET under androgen control: it is induced >20-fold by DHT in androgen-responsive LNCaP prostate cells via an Sp-family binding site in its promoter [PMID:16020486 "SCGB 2A1 is under androgen control in the androgen-responsive prostatic cell line LNCaP and can be induced more than 20-fold by dihydrotestosterone"]. Its ocular expression tracks androgen-receptor-positive tissues [PMID:16395610 "Androgen-dependent expression of SCGB 2A1 has been observed in"].
- Being a downstream, androgen-INDUCED gene is not the same as the secreted protein participating in ("involved_in") the androgen receptor signaling pathway (GO:0030521 is nuclear-receptor signal transduction ending in transcriptional regulation; SCGB2A1 does none of that signal transduction — it is an output). Both the IDA (PMID:16020486) and the IBA rows assert involved_in GO:0030521, which over-annotates the relationship. -> MARK_AS_OVER_ANNOTATED (both, consistently). There is no clean "cellular response to androgen" GO term (GO:0071393 is progesterone; GO:0071394 is testosterone-specific, whereas the inducer here is DHT), so no MODIFY replacement is asserted.

## Deep research (OpenScientist)
- An OpenScientist deep-research report (SCGB2A1-deep-research-openscientist.md) was present and used as LEADS only. It corroborates the lipophilin AC heterodimer with SCGB1D1, hydrophobic-ligand (steroid) binding by homology to rat prostatein/uteroglobin, and reports that androgen regulation is indirect/Sp1-Sp3-mediated with the AR recruited but "does not bind DNA directly" [file:human/SCGB2A1/SCGB2A1-deep-research-openscientist.md "the androgen receptor is recruited but does not bind DNA directly"] — reinforcing that SCGB2A1 is a downstream target, not a signaling component. Claims verified against primary papers (PMID:9720917, PMID:16020486, PMID:16395610); not used as sole evidence.

## Annotation decisions (summary)
- GO:0005515 protein binding (IPI, with SCGB1D1/O95968): MODIFY -> GO:0046982 protein heterodimerization activity (lipophilin AC heterodimer with lipophilin A).
- GO:0005576 extracellular region (IBA/IDA x3/HDA x2/IEA): ACCEPT — core; secreted protein, multiple direct and proteomic lines of evidence.
- GO:0030521 androgen receptor signaling pathway (IDA + IBA): MARK_AS_OVER_ANNOTATED (see above).

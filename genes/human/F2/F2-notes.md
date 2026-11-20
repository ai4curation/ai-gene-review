# F2 (P00734) — curation notes

Deep-research providers are unavailable in this environment; research is from the cached
publications, the UniProt record and PubMed.

## Protein

Prothrombin: signal 1-24, propeptide 25-43, chain 44-622, with Gla and two kringle
domains and a chymotrypsin-like protease domain; alpha-thrombin is the disulfide-linked
light (315-363) and heavy (364-622) chain heterodimer.
[file:human/F2/F2-uniprot.txt "SUBCELLULAR LOCATION: Secreted, extracellular space."]
[file:human/F2/F2-uniprot.txt "Expressed by the liver and secreted in plasma."]

Localization conclusion: **extracellular / secreted plasma protein**. It is not a
membrane protein. The ER-lumen and Golgi-lumen rows are secretory transit compartments
(kept as non-core); the six Reactome `plasma membrane` rows were modified to
`GO:0009897 external side of plasma membrane`, which is where thrombin engages PARs,
GPIb-alpha and thrombomodulin, and which the gene already carries by IDA
(colocalizes_with).

## Function

[file:human/F2/F2-uniprot.txt "Thrombin, which cleaves bonds after Arg and Lys, converts fibrinogen to fibrin and activates factors V, VII, VIII, XIII, and, in complex with thrombomodulin, protein C."]
[PMID:10761923 "Thrombomodulin, a transmembrane thrombin receptor with six contiguous epidermal growth factor-like domains (TME1-6), profoundly alters the substrate specificity of thrombin from pro- to anticoagulant by activating protein C."]
[PMID:1672265 "A peptide mimicking the new amino terminus created by cleavage at R41 was a potent agonist for both thrombin receptor activation and platelet activation."]
[PMID:12855810 "defined two sites in GpIbalpha that bind to exosite II and exosite I of two distinct alpha-thrombin molecules"]
[PMID:20421939 "C-terminal peptides of thrombin ... constitute a novel class of host defense peptides"]

## Notable review decisions

- `GO:0070053 thrombospondin receptor activity` (IDA, PMID:2435757, assigned by BHF-UCL)
  was REMOVEd with a `source_defects` entry. The paper isolates an 88-kDa platelet
  membrane glycoprotein (the OKM5 antigen, CD36/GPIV) as the thrombospondin binding site;
  thrombin appears only as the platelet agonist, and a secreted protease cannot be a
  membrane receptor.
  [PMID:2435757 "We have identified and isolated an 88-kd membrane glycoprotein present in platelets, endothelial cells, monocytes, and a variety of human tumor cell lines that is the membrane binding site for TSP."]
- `GO:0008083 growth factor activity` and `GO:0048018 receptor ligand activity` were
  marked as over-annotations: thrombin activates PARs by cleaving them, the tethered
  ligand being the receptor's own N-terminus.
- Ten bare protein-binding rows (serpins, staphylocoagulase, alpha-1-microglobulin, APP,
  PAI-1, LRP1) were removed under the protein-binding policy; the informative LRP1 and
  GPIb-alpha interactions are retained as `signaling receptor binding`.
- Both `positive regulation of blood coagulation` and `negative regulation of blood
  coagulation` are accepted, because the switch is made by thrombomodulin binding; the
  parent `regulation of blood coagulation` is therefore TOO_GENERAL.
- Antimicrobial and immunomodulatory rows from PMID:20421939 are kept as non-core because
  they describe released C-terminal peptides rather than the coagulation protease.

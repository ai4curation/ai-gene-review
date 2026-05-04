# Hsp90aa1 curation notes

Deep research status: `just deep-research-falcon mouse Hsp90aa1 --timeout 1800 --fallback perplexity-lite` completed on 2026-05-03 and created `Hsp90aa1-deep-research-falcon.md`. Earlier short-timeout Falcon attempts failed before the required long run was used.

Core evidence: Hsp90aa1 is the inducible cytosolic/nuclear Hsp90-alpha ATP-dependent protein-folding chaperone. UniProt describes it as a "Molecular chaperone that promotes the maturation, structural maintenance and proper regulation of specific target proteins" and links this cycle to ATPase activity.

Falcon synthesis: The Falcon report supports the same core function: Hsp90aa1 encodes cytosolic HSP90-alpha, a dimeric ATP-dependent molecular chaperone with an N-terminal ATP-binding domain, middle client-regulatory domain, and C-terminal dimerization/co-chaperone interaction domain. It emphasizes co-chaperone-regulated maturation and stabilization of selected signaling clients rather than generic protein binding [file:mouse/Hsp90aa1/Hsp90aa1-deep-research-falcon.md "Hsp90aa1 encodes HSP90α, a highly abundant ATP-dependent molecular chaperone that functions as a dimer"; file:mouse/Hsp90aa1/Hsp90aa1-deep-research-falcon.md "ATP binding and hydrolysis drive a conformational cycle through open/closed and nucleotide-bound states that orchestrate client loading, activation/maturation, and release"].

Falcon non-core context: The Falcon report also supports several context-specific annotations as non-core rather than core: extracellular HSP90-alpha in wound repair/migration programs, male germline phenotypes with spermatogenesis/piRNA effects, and HIF-1alpha client stabilization in testis [file:mouse/Hsp90aa1/Hsp90aa1-deep-research-falcon.md "Hsp90α is a cytosolic Hsp90 isoform"; file:mouse/Hsp90aa1/Hsp90aa1-deep-research-falcon.md "Keratinocytes can massively release eHSP90α into the wound bed"; file:mouse/Hsp90aa1/Hsp90aa1-deep-research-falcon.md "Hsp90aa1-null males are sterile"].

ATPase evidence: UniProt lists catalytic activity "ATP + H2O = ADP + phosphate + H(+)" and notes that the Hsp90 cycle is linked to ATP binding and ATP hydrolysis. Tsc1/Aha1 experiments show cochaperone control of Hsp90 ATPase activity [PMID:29127155].

Client-folding evidence: Tsc1 is described as "a new co-chaperone for Hsp90 that inhibits its ATPase activity" and the paper concludes that Tsc1 facilitates "Hsp90-mediated folding of kinase and non-kinase clients" [PMID:29127155].

PhLP2A evidence: The PhLP2A study reports that "PhLP2A interacts directly with Hsp90" and that "PhLP2A forms complexes with Hsp90 which are mainly localized in the cytoplasm" [PMID:27496612]. This supports cytoplasmic chaperone-complex annotations.

Neuronal evidence: The neuronal-polarization study used Hsp90 inhibition and reports that "Hsp90 inhibition at different developmental stages disturbs neuronal polarity formation or axonal elongation" [PMID:24286867]. These annotations are context-specific and non-core because the evidence is inhibitor-based and not Hsp90aa1-isoform-specific.

Extracellular evidence: The Hectd1 study states that Hectd1 is a ubiquitin ligase substrate regulator for Hsp90 and that "Extracellular Hsp90 enhances migration of multiple cell types" [PMID:22431752]. Secreted or membrane-associated Hsp90 annotations should therefore be kept as non-core or marked over-annotated when the GO term implies a structural ECM location.

Nitric oxide evidence: The iNOS paper states that NO synthesis from iNOS "can be profoundly modulated by heat shock protein 90 (hsp90) through protein-protein interaction" and that Hsp90 increases iNOS activity [PMID:12855682]. This supports nitric-oxide-synthase regulator annotations as non-core client regulation.

Curation rule: GO:0051082 unfolded protein binding is not the best term for Hsp90; GO:0140662 ATP-dependent protein folding chaperone captures the ATP-driven Hsp90 foldase mechanism. GO:0005515 protein binding is too generic for Hsp90 client or cochaperone interactions.

Nucleotide specificity rule: Hsp90aa1 is an ATP-binding ATPase; GOA terms for UTP binding, CTP binding, GTP binding, and dATP binding are not supported as core Hsp90aa1 nucleotide-binding functions and should be removed unless direct gene-specific evidence is available.

Core location rule: Cytosol/cytoplasm and nucleus are core Hsp90aa1 locations. Plasma membrane, cell surface, extracellular, neuronal growth cone, myelin, sperm, and mitochondrial annotations can be context-specific but should not be treated as the core location of cytosolic Hsp90-alpha.

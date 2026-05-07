    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P16310
    gene: Ghr
    organism: Rattus norvegicus (Rat)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The N-terminal extracellular region contains IPR015152 (Growth hormone/erythropoietin receptor, ligand binding, residues 46–131), which is the canonical cytokine-binding module of class I hematopoietin receptors. This segment is embedded within immunoglobulin-like and fibronectin type III folds: IPR013783 (Immunoglobulin-like fold, residues 50–149) and IPR003961 (Fibronectin type III, residues 149–250), with the corresponding superfamily annotations IPR036116 (Fibronectin type III superfamily, residues 50–148 and 149–252) and IPR013783 (Immunoglobulin-like fold, residues 150–250). This extracellular module arrangement is characteristic of ligand-gated receptors that capture a specific peptide hormone at the cell surface. Immediately downstream, IPR003528 (Long hematopoietin receptor, single chain, conserved site, residues 171–249) marks the conserved signature of long-chain cytokine receptors, which include the WSXWS-related motif and the proline-rich Box1/Box2 regions that organize intracellular kinase docking. The ectodomain also includes IPR025871 (Growth hormone-binding protein, residues 317–616), indicating that a proteolytically released soluble ectodomain (GHRP) circulates and binds growth hormone with high affinity. Together with the stated topology (single-pass type I membrane protein), this architecture causes ligand-dependent receptor dimerization/rotation at the plasma membrane and positions a cytoplasmic tail to recruit tyrosine kinases and SH2-containing effectors.

From this domain layout, the molecular function follows. The ligand-binding cytokine receptor module confers growth hormone receptor activity (GO:0004903). The conserved cytoplasmic tail motifs in long hematopoietin receptors create phosphotyrosine docking sites for SH2 domains, establishing SH2 domain binding (GO:0042169). The same tail recruits non-receptor protein tyrosine kinases, consistent with protein kinase binding (GO:0019901), and engages regulatory phosphatases that tune signaling amplitude, consistent with protein phosphatase binding (GO:0019903). The presence of a cleavable ectodomain and the membrane-anchored form together explain how signaling is initiated by hormone-induced conformational changes that juxtapose cytoplasmic Box1/Box2 motifs to bind and activate associated kinases.

These molecular activities drive specific biological processes. Ligand-induced activation of the receptor’s associated tyrosine kinase triggers peptidyl-tyrosine phosphorylation (GO:0018108) on the receptor and STATs, initiating the growth hormone receptor signaling pathway via JAK-STAT (GO:0060397) and its positive regulation (GO:0060357). Phosphorylated STATs translocate to the nucleus to modulate transcription, while parallel recruitment of SHC/GRB2-SOS elicits activation of protein kinase activity (GO:0032147) and positive regulation of MAP kinase activity (GO:0043406). These signaling axes underlie organismal and tissue-level outcomes: positive regulation of cell differentiation (GO:0045597), cartilage development involved in endochondral bone morphogenesis (GO:0060351), and broader anatomical structure morphogenesis (GO:0009887). Because growth hormone integrates endocrine cues, the receptor participates in hormone-mediated signaling (GO:0009755) and cellular responses to growth hormone (GO:0071378), insulin (GO:0032869), interleukin-1 (GO:0071347), morphine (GO:0071316), and glucocorticoid (GO:0051384), reflecting crosstalk with metabolic and inflammatory pathways. Neurotrophic outputs of GH/IGF signaling contribute to negative regulation of neuron death (GO:1901215). System-level modulation of metabolism and behavior aligns with response to food (GO:0032094) and response to gravity (GO:0009629), consistent with GH’s role in fluid balance and posture reflexes. The receptor’s signaling also intersects with vascular and renal physiology, explaining its involvement in regulating renal sodium excretion and blood pressure.

The cellular component is dictated by the architecture and processing. The single-pass type I configuration places the full-length receptor at the plasma membrane (GO:0005886), where ligand binding occurs. Proteolytic shedding yields the secreted growth hormone-binding protein in the extracellular space (GO:0005615), which buffers hormone availability and shapes signaling gradients. Activated complexes form cytoplasmic signaling hubs (GO:0005737) that culminate in nuclear signaling (GO:0005634) via STAT translocation. Expression in neurons situates the receptor in the neuronal cell body (GO:0043025), and GH/IGF signaling can influence mitochondrial function (GO:0005739), consistent with observed associations with oxidative metabolism.

Mechanistically, hormone binding to the extracellular cytokine receptor module stabilizes an active dimer that reorients the cytoplasmic tails, enabling the conserved site (IPR003528) to bind and activate associated tyrosine kinases. The receptor then undergoes peptidyl-tyrosine phosphorylation, creating SH2 docking sites for STAT5A/STAT5B, which are phosphorylated and translocate to the nucleus to drive transcriptional programs for growth, differentiation, and metabolic adaptation. Parallel recruitment of SHC/GRB2-SOS activates MAPK, while phosphatases and SOCS proteins (e.g., SOCS2) bind to attenuate signaling. The secreted ectodomain (GHRP) modulates hormone bioavailability and receptor occupancy, shaping the amplitude and duration of signaling.

These inferences suggest specific interaction partners. The cytoplasmic tail’s kinase-docking motifs predict association with tyrosine-protein kinase JAK2 as the primary activator, with possible context-dependent engagement of JAK3. The SH2 docking sites recruit STAT5A and STAT5B. Negative feedback arises via SOCS2 binding. The ligand is somatotropin (growth hormone), and downstream endocrine coupling predicts functional interaction with insulin-like growth factor I. Crosstalk with prolactin and prolactin-6A1 is plausible through shared JAK/STAT machinery and overlapping transcriptional programs. Generic “tyrosine-protein kinase” entries reflect additional non-receptor kinases that can transiently bind during signaling bursts.

    ## Functional Summary

    A single-pass cell-surface cytokine receptor that binds growth hormone through an extracellular ligand-binding module and, upon ligand-induced dimerization, activates an associated tyrosine kinase to drive tyrosine phosphorylation and STAT-mediated transcription. This signaling promotes growth, differentiation, and metabolic adaptation, with parallel engagement of MAP kinase pathways and crosstalk with insulin, inflammatory, and stress-responsive hormones. The receptor signals from the plasma membrane with transient cytoplasmic complexes and nuclear translocation of activated transcription factors, while a proteolytically released soluble ectodomain circulates as a high-affinity growth hormone-binding protein that modulates hormone availability and signaling range. Its activity contributes to renal sodium excretion and blood pressure control and extends to neuronal and mitochondrial contexts where it supports cell survival and metabolic tuning.

    ## UniProt Summary

    Receptor for pituitary gland growth hormone involved in regulating postnatal body growth. On ligand binding, couples to, and activates the JAK2/STAT5 pathway (By similarity). Involved in regulating renal sodium excretion and blood pressure.

    ## InterPro Domains

        - IPR015152: Growth hormone/erythropoietin receptor, ligand binding (domain) [46-131]
    - IPR013783: Immunoglobulin-like fold (homologous_superfamily) [50-149]
    - IPR036116: Fibronectin type III superfamily (homologous_superfamily) [50-148]
    - IPR003961: Fibronectin type III (domain) [149-250]
    - IPR036116: Fibronectin type III superfamily (homologous_superfamily) [149-252]
    - IPR013783: Immunoglobulin-like fold (homologous_superfamily) [150-250]
    - IPR003961: Fibronectin type III (domain) [151-254]
    - IPR003528: Long hematopoietin receptor, single chain, conserved site (conserved_site) [171-249]
    - IPR025871: Growth hormone-binding protein (domain) [317-616]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


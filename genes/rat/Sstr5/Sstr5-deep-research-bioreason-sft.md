    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P30938
    gene: Sstr5
    organism: Rattus norvegicus (Rat)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. Multiple overlapping family and domain signatures define a class A (rhodopsin-like) G protein–coupled receptor (GPCR) with somatostatin receptor 5 (SSTR5) specificity. Short N-terminal motifs IPR001184 (Somatostatin receptor 5 family, residues 3–16 and 33–47) and broader family marks IPR000586 (Somatostatin receptor family, residues 36–48) indicate an extracellular N-terminus tailored for peptide binding. The core seven-transmembrane (7TM) region is captured by IPR017452 (GPCR, rhodopsin-like, 7TM domain, residues 54–304), with flanking family annotations IPR000276 (G protein-coupled receptor, rhodopsin-like family, residues 39–63, 48–319, 54–304, 72–93, 117–139, 123–139, 153–174, 201–224, 246–270, 286–312) that collectively specify the canonical class A GPCR fold and its intracellular coupling surfaces. Within this 7TM scaffold, SSTR-specific family signatures recur at key helices: IPR000586 (Somatostatin receptor family, residues 91–99, 111–120, 225–234, 235–248, 268–276, 306–318) and SSTR5-specific marks IPR001184 (Somatostatin receptor 5 family, residues 226–240, 272–288, 326–340). These motifs map to intracellular loops and the C-terminal tail that determine coupling to Gi/o proteins and receptor regulation. The ensemble of overlapping family entries (including IPR000276 and IPR000586) across the 7TM region establishes a peptide-activated GPCR that preferentially engages Gi/o.

This architecture causes somatostatin receptor activity (GO:0004994) by binding somatostatin peptides at the extracellular N-terminus and transmembrane pocket, then transmitting the signal through the 7TM core to intracellular loops that recruit heterotrimeric G proteins. The SSTR5-specific signatures imply high-affinity recognition of somatostatin-14 and -28, consistent with the observed preference.

Gi/o engagement by this receptor inhibits adenylate cyclase, lowering cAMP and dampening PKA signaling. This places the protein squarely in the adenylate cyclase-inhibiting G protein–coupled receptor signaling pathway (GO:0007193). Through cAMP/PKA and downstream effectors (e.g., CREB, CRTC/TORC transcriptional regulators), SSTR5 signaling modulates transcriptional programs that intersect with stress hormone pathways; such cAMP-dependent control provides a mechanistic route by which SSTR signaling shapes the cellular response to glucocorticoid stimulus (GO:0071385), for example by tuning glucocorticoid receptor–dependent gene expression.

The 7TM domain and multi-pass topology dictate residence in the plasma membrane (GO:0005886), where ligand access and G protein coupling occur. Internalization motifs and scaffold interactions commonly drive ligand-induced endocytosis and recycling, explaining a cytoplasmic (GO:0005737) pool associated with trafficking and signaling complexes. The subcellular description of a cell membrane, multi-pass protein aligns with this GPCR life cycle.

Mechanistically, somatostatin-14 binding stabilizes an active 7TM conformation that exposes intracellular interfaces for Gi/o. Gαi/o inhibits adenylate cyclase, while Gβγ can engage ion channels and kinases, collectively suppressing cAMP and modulating neuronal excitability and endocrine secretion. The receptor likely forms transient complexes with Gi α subunits (G(i) α-1 and α-2) and may hetero-oligomerize with other somatostatin receptors to fine-tune ligand affinity and signaling bias. Crosstalk with appetite-regulatory systems (appetite-regulating hormone; C-flanking peptide of NPY) is expected at the level of shared neuronal circuits and convergent control of cAMP/PKA and CREB-dependent transcription, providing a route to coordinate feeding behavior and stress-axis outputs.

    ## Functional Summary

    A seven-transmembrane, cell-surface receptor in rat that binds somatostatin peptides with a strong preference for the 14–residue form and transduces the signal through inhibitory G proteins to suppress adenylate cyclase and reduce cAMP. This signaling dampens PKA-dependent transcriptional programs and intersects with stress hormone pathways, shaping cellular responses to glucocorticoids. The receptor resides at the plasma membrane and cycles through cytoplasmic trafficking pools, where it assembles with Gi proteins and likely coordinates with other neuropeptidergic systems to regulate excitability, secretion, and endocrine tone.

    ## UniProt Summary

    Receptor for somatostatin with a high affinity binding for somatostatin-14 and-28.

    ## InterPro Domains

        - IPR001184: Somatostatin receptor 5 (family) [3-16]
    - IPR001184: Somatostatin receptor 5 (family) [33-47]
    - IPR000586: Somatostatin receptor family (family) [36-48]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [39-63]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [48-319]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [54-304]
    - IPR017452: GPCR, rhodopsin-like, 7TM (domain) [54-304]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [72-93]
    - IPR000586: Somatostatin receptor family (family) [91-99]
    - IPR000586: Somatostatin receptor family (family) [111-120]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [117-139]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [123-139]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [153-174]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [201-224]
    - IPR000586: Somatostatin receptor family (family) [225-234]
    - IPR001184: Somatostatin receptor 5 (family) [226-240]
    - IPR000586: Somatostatin receptor family (family) [235-248]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [246-270]
    - IPR000586: Somatostatin receptor family (family) [268-276]
    - IPR001184: Somatostatin receptor 5 (family) [272-288]
    - IPR000276: G protein-coupled receptor, rhodopsin-like (family) [286-312]
    - IPR000586: Somatostatin receptor family (family) [306-318]
    - IPR001184: Somatostatin receptor 5 (family) [326-340]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


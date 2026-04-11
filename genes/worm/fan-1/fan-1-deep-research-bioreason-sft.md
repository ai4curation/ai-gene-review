    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: P90740
    gene: fan-1
    organism: Caenorhabditis elegans
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. An N-terminal IPR006642 Rad18, zinc finger UBZ4-type domain occupies residues 35–62. UBZ4 zinc fingers recognize ubiquitin adducts on proteins or DNA, which equips the protein to dock onto monoubiquitinated chromatin factors at sites of DNA damage. The core of the protein is defined by two family-level signatures—IPR033315 Fanconi-associated nuclease 1-like (residues 115–860) and IPR049132 Fanconi-associated nuclease 1-like, eukaryotes (residues 214–856)—which together specify a eukaryotic FAN1-type nuclease scaffold. Within this scaffold, a discrete IPR049125 winged-helix domain (residues 245–305) provides a DNA-binding module that can grip duplex DNA and position the scissile strand. A central IPR049126 TPR domain (residues 457–609) forms a solenoid of tetratricopeptide repeats that mediates protein–protein interactions, enabling assembly with repair factors. The C-terminus contains the catalytic core: IPR014883 VRR-NUC domain (residues 742–858, also annotated as 743–857) is a metal-dependent nuclease fold characteristic of FAN1/VRR-NUC enzymes, and it overlaps with IPR011856 tRNA endonuclease-like domain superfamily (residues 794–865), indicating an RNase H/EndA-like endonuclease topology adapted here for DNA phosphodiester hydrolysis. The ordered layout—ubiquitin-binding UBZ4 at the N-terminus, DNA-binding winged helix, scaffolding TPR, and a C-terminal VRR-NUC nuclease—creates a recruitment-and-cleavage machine specialized for DNA repair.

This architecture causes specific molecular functions. The VRR-NUC/tRNA endonuclease-like core confers endonuclease activity on DNA, while the winged-helix domain positions duplex DNA for incision. The UBZ4 zinc finger binds ubiquitin, targeting the enzyme to ubiquitinated chromatin, and the TPR array mediates protein binding to assemble a repair complex. These features together support protein binding (GO:0005515) as a general capability and strongly imply DNA binding and endonuclease activity as direct molecular functions executed by the catalytic core.

From these molecular activities, the biological process follows. A ubiquitin-guided, DNA-bound nuclease that assembles via TPR modules is suited to DNA repair (GO:0006281), specifically the processing of DNA interstrand cross-links. The UBZ4 domain would capture monoubiquitinated FANCD2 at stalled replication forks; the winged-helix and VRR-NUC core then incise the DNA to unhook the cross-link. The family-level FAN1-like signatures indicate the incision occurs near the cross-link and extends to create entry points for downstream nucleases and translesion synthesis, a hallmark of the Fanconi pathway.

The cellular component is dictated by the need to access chromosomal DNA and assemble with nuclear repair factors. The presence of DNA-binding and ubiquitin-targeting modules that act on chromatin implies a nuclear residence, consistent with the nucleus (GO:0005634).

This mechanistic model predicts specific interaction partners and roles. The UBZ4 domain should bind monoubiquitinated FANCD2, recruiting the nuclease to the Fanconi focus. The TPR region likely scaffolds additional Fanconi and cross-link repair components: FANCI (via its HD2-associated region), ERCC4-family nucleases (XPF homologs) that extend incisions after the initial FAN1-mediated cut, and SLX1 as an alternative structure-specific endonuclease. Coordination with the ERCC (XPF) homolog and ERCC4-domain proteins would enable dual incisions flanking the cross-link. PMS family members (Fanconi-associated helicase-like factors) could couple incision to DNA unwinding, while the Werner syndrome helicase (WRN) may expand the repair at stalled forks. DNA polymerase kappa, a translesion polymerase, would fill gaps after unhooking. A DNA mis-repair domain-containing factor likely functions as an adaptor or quality-control component that senses aberrant intermediates and stabilizes the repair assembly. Altogether, ubiquitin-guided recruitment, DNA binding, and a VRR-NUC catalytic core drive targeted endonucleolytic incisions that initiate cross-link repair within the nuclear compartment.

    ## Functional Summary

    A nuclear DNA cross-link repair nuclease in Caenorhabditis elegans that is recruited to ubiquitin-marked damage sites, binds and positions duplex DNA, and uses a metal-dependent nuclease core to incise DNA near interstrand cross-links. Through a TPR-based scaffold, it assembles with Fanconi and excision-repair factors to unhook the cross-link and hand off intermediates for unwinding and gap filling, thereby restoring genome integrity during replication stress.

    ## UniProt Summary

    Nuclease required for the repair of DNA interstrand cross-links (ICL) in response to DNA damage.

    ## InterPro Domains

        - IPR006642: Rad18, zinc finger UBZ4-type (domain) [35-62]
    - IPR033315: Fanconi-associated nuclease 1-like (family) [115-860]
    - IPR049132: Fanconi-associated nuclease 1-like, eukaryotes (family) [214-856]
    - IPR049125: Fanconi-associated nuclease 1-like, winged-helix domain (domain) [245-305]
    - IPR049126: Fanconi-associated nuclease 1-like, TPR domain (domain) [457-609]
    - IPR014883: VRR-NUC domain (domain) [742-858]
    - IPR014883: VRR-NUC domain (domain) [743-857]
    - IPR011856: tRNA endonuclease-like domain superfamily (homologous_superfamily) [794-865]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


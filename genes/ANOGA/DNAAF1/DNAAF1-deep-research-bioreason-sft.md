    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q7PK92
    gene: DNAAF1
    organism: Anopheles gambiae (African malaria mosquito)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The N-terminus (residues 1–103) is covered by IPR032675 (Leucine-rich repeat domain superfamily), with embedded LRR repeats IPR001611 at 43–64 and 65–86, and a more specific IPR025875 (Leucine rich repeat 4) at 65–102. Immediately downstream, the LRR superfamily signature recurs (IPR032675, residues 104–204) and includes an additional LRR unit IPR001611 at 111–132. This tandem arrangement of LRR units creates a curved solenoid surface optimized for high-affinity, sequence-specific protein docking rather than catalysis. Encompassing nearly the entire polypeptide (residues 1–875) is IPR050576 (Ciliary and flagellar integrity-associated protein family), which ties this LRR scaffold to the biogenesis and maintenance of motile cilia/flagella. The ordered layout—an N-terminal LRR docking platform embedded within a cilia/flagella integrity family scaffold—causes the protein to function as a cytoplasmic adaptor that binds multi-subunit assemblies and positions them at the ciliary base.

This LRR-driven docking explains the molecular function as protein-containing complex binding (GO:0044877). LRR solenoids are classical interaction modules, and the breadth of the ciliary integrity family signature indicates the complexes are likely large, transport- or assembly-related machines (e.g., intraflagellar transport particles, motors, or signaling modules).

From this binding activity, several biological processes follow. The ciliary integrity family context predicts a role in organizing and delivering cargoes to the cilium/flagellum. Such cargo can include signaling receptors and organelles. The protein’s ability to assemble and position complexes at the ciliary base provides a mechanism to regulate Hedgehog/Smoothened signaling, aligning with negative regulation of smoothened signaling pathway (GO:0008590). By controlling the availability and localization of Smoothened and associated components, the scaffold can dampen pathway activation.

The same adaptor logic extends to MAPK signaling. A cytoplasmic LRR scaffold can sequester or spatially segregate RAF–MEK–ERK components, thereby causing negative regulation of ERK1 and ERK2 cascade (GO:0070373). This negative control can arise from competitive binding that limits complex assembly or from relocalization away from activating platforms.

The LRR scaffold can also tune calcium-mediated signaling (GO:0050848) by docking calcium channels, pumps, or calcium-sensitive enzymes at defined cytoplasmic locales, thereby modulating local Ca2+ microdomains that feed back on MAPK and ciliary functions. In neurons, the same spatial organization supports axo-dendritic transport (GO:0008088) by linking cargoes to microtubule-based motors and adaptors, ensuring directional trafficking of receptors and organelles into dendrites and axons. Because spatial control of signaling and transport often impinges on transcriptional outputs, the scaffold’s regulation of these pathways can culminate in positive regulation of gene expression (GO:0010628), for example by stabilizing transcriptional co-regulators or by modulating signaling axes that enhance gene expression programs.

The cellular component is cytoplasm (GO:0005737), consistent with a soluble adaptor that assembles complexes in the cytosol and at cytoplasmic faces of organelles such as the basal body/ciliary base. The absence of transmembrane domains and the presence of extensive LRRs further support a cytoplasmic scaffold role rather than a membrane-embedded or nuclear role.

Mechanistically, I propose that the N-terminal LRR array nucleates binding of multi-protein assemblies—such as intraflagellar transport particles, kinesin/dynein motors, and signaling complexes—while the broader ciliary integrity family scaffold stabilizes these interactions long enough to direct cargo to the ciliary base or neuronal processes. By selectively recruiting or excluding components of the Smoothened and RAF–MEK–ERK modules, and by positioning calcium-handling proteins, the protein tunes pathway amplitude and timing. In neurons, coupling to microtubule motors and dendritic trafficking adaptors extends this spatial control to axo-dendritic transport, ultimately influencing gene expression through signaling-dependent transcriptional programs.

    ## Functional Summary

    A cytoplasmic leucine‑rich repeat scaffold that assembles and positions large protein complexes to control signaling and transport. Its N‑terminal repeat array provides a high‑affinity docking surface that captures transport and signaling modules, while the extended scaffold stabilizes these assemblies to direct them toward the ciliary base and neuronal processes. Through spatial sequestration and delivery of components, it dampens Smoothened‑dependent Hedgehog signaling, restrains ERK1/2 activation, modulates calcium‑dependent signaling microdomains, and supports axo‑dendritic cargo trafficking. These coordinated actions can ultimately enhance gene expression programs downstream of the tuned signaling outputs.

    ## UniProt Summary

    Negatively regulates the Hedgehog (Hh) signaling pathway, possibly by regulating the activity of smoothened ( smo ).

    ## InterPro Domains

        - IPR032675: Leucine-rich repeat domain superfamily (homologous_superfamily) [1-103]
    - IPR050576: Ciliary and flagellar integrity-associated protein (family) [1-875]
    - IPR001611: Leucine-rich repeat (repeat) [43-64]
    - IPR001611: Leucine-rich repeat (repeat) [65-86]
    - IPR025875: Leucine rich repeat 4 (repeat) [65-102]
    - IPR001611: Leucine-rich repeat (repeat) [87-108]
    - IPR032675: Leucine-rich repeat domain superfamily (homologous_superfamily) [104-204]
    - IPR001611: Leucine-rich repeat (repeat) [111-132]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q6TNU4
    gene: fen1
    organism: Danio rerio (Zebrafish)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The polypeptide is dominated by XPG/Rad2 nuclease signatures: IPR006084 (XPG/Rad2 endonuclease family, residues 1–357) and the more specific IPR023426 (Flap endonuclease 1 family, residues 1–345) define the enzyme class and substrate preference. The N-terminus contains IPR006085 (XPG, N-terminal domain, residues 1–107), which houses catalytic and metal-binding residues for the nuclease core. Multiple overlapping XPG/Rad2 family motifs punctuate this region and the adjacent IPR006086 (XPG-I domain, residues 146–218; also detected as residues 149–233), forming the paired N and I subdomains that clamp DNA and position the scissile phosphate. These include IPR019974 (XPG conserved site, residues 79–93) and additional conserved motifs at residues 149–163 and 166–186, which together create the acidic residues that coordinate divalent metal ions and the helix-hairpin-helix elements that stabilize the DNA backbone. The catalytic core is further supported by IPR029060 (PIN-like domain superfamily, residues 2–233), a nuclease fold that contributes the metal-chelating geometry, and by IPR008918 (Helix-hairpin-helix motif, class 2, residues 220–253), which provides non-sequence-specific DNA binding and bends the duplex near the junction. The C-terminal region is captured by IPR036279 (5'-3' exonuclease, C-terminal domain superfamily, residues 218–351), a regulatory and DNA-binding module that recognizes 5'-flap architecture and stimulates catalysis. Together, these domains assemble the canonical Rad2/XPG-like nuclease that incises 5'-flaps at single-strand/double-strand junctions and also supports 5'→3' exonucleolytic degradation on nicked or gapped duplex DNA.

This domain architecture causes a precise molecular function: GO:0017108 5'-flap endonuclease activity. The XPG-N/I composite active site, reinforced by the HhH motif, binds a 5'-flap and introduces a single endonucleolytic cut 5' to the branch, leaving a ligatable nick. The C-terminal superfamily domain enhances recognition and positioning of the flap stem, while the PIN-like fold coordinates catalytic metal ions to hydrolyze the phosphodiester bond. The same structural features enable processive 5'→3' exonucleolysis on nicked or gapped duplexes, consistent with a distributive-to-processive switch depending on DNA context and partner binding.

From this chemistry, the biological processes follow. During lagging-strand DNA replication, displacement synthesis by DNA polymerase generates 5'-flaps on downstream Okazaki fragments; this nuclease resolves those flaps to enable ligation, placing it in DNA replication and specifically Okazaki fragment processing. In base-excision repair, long-patch BER creates 5'-flaps after gap filling; the enzyme trims these flaps to complete repair, aligning with base-excision repair and long-patch BER. Its ability to incise at ssDNA–dsDNA junctions and to degrade 5'-protrusions also supports DNA recombination and the processing of recombination intermediates. The same incision and resection activities contribute to double-strand break repair, including homologous recombination and nonhomologous end joining interfaces that require flap and overhang management. In metazoan tissues, such genome-maintenance activities are essential for proliferative and differentiating cells; thus, defects manifest in organogenesis, including retina development in the camera-type eye, where precise DNA repair and replication are required for photoreceptor and retinal pigment epithelium maturation.

The cellular component is dictated by the need to access chromosomal DNA and replication factories. The presence of nuclear-targeted DNA repair and replication roles, together with the regulatory C-terminal domain that engages replication clamps, places the enzyme in the GO:0005634 nucleus. The architecture lacks transmembrane segments or secretion signals, reinforcing a soluble nuclear localization.

Mechanistically, the enzyme likely operates within multi-protein assemblies. The C-terminal domain and HhH-mediated DNA engagement allow it to be clamped by the sliding clamp PCNA, which increases processivity and coordinates handoff to DNA ligase. DNA polymerase delta and its regulatory subunits generate the 5'-flaps that this nuclease removes; DNA polymerase beta participates in long-patch BER where the same flap-removal step is required. Helicase/nuclease Dna2 and the RecQ helicase WRN create or extend DNA flaps and suppress toxic recombination intermediates; the nuclease can then trim or process these structures. AP endonuclease (DNA-(apurinic or apyrimidinic site) lyase) generates entry points for repair synthesis that culminate in flap formation, which this enzyme resolves. In double-strand break contexts, coordination with XRCC1-like scaffolds and double-strand break repair proteins organizes repair tracts where flap processing is needed. Altogether, the domain architecture and partner repertoire support a model in which the enzyme is a nuclear 5'-flap endonuclease and 5'→3' exonuclease that acts at replication forks, BER patches, and recombination/DSB sites to maintain genome integrity and enable proper tissue development, including the retina.

    ## Functional Summary

    A nuclear nuclease that removes 5′ flaps and degrades 5′ ends to resolve replication and repair intermediates. During lagging-strand synthesis it cleaves displaced DNA on Okazaki fragments, and in long-patch base-excision repair it trims flap structures created after gap filling. Its incision at single- to double-strand junctions and exonucleolytic processing of nicked or gapped duplexes support recombination and double-strand break repair. By coordinating with sliding clamps, polymerases, helicases, and ligases, it ensures accurate maturation of DNA ends, a role that underpins genome stability and contributes to proper development of tissues such as the retina.

    ## UniProt Summary

    Key enzyme involved in DNA replication and repair. Has 5'-flap endonuclease activity during DNA replication of the lagging strand: tracks along the 5'-end of a flap structure emerging from the displacement synthesis of the downstream Okazaki fragment and cleaves the flap structure at the junction with the leading strand (By similarity). Has a 5'--> 3'-exonuclease activity on nicked or gapped double-stranded DNA (By similarity). Also involved in the repair of DNA double-strand breaks by non-homologous end joining (NHEJ) and homologous recombination (By similarity). Has endonuclease activity towards double-stranded DNA with a single-strand gap, introducing a cut near the junction between the single- and double-stranded sections (By similarity). Has exonuclease activity on nicked or gapped double-stranded DNA (By similarity).

    ## InterPro Domains

        - IPR006084: XPG/Rad2 endonuclease (family) [1-357]
    - IPR006085: XPG, N-terminal (domain) [1-107]
    - IPR023426: Flap endonuclease 1 (family) [1-345]
    - IPR029060: PIN-like domain superfamily (homologous_superfamily) [2-233]
    - IPR006084: XPG/Rad2 endonuclease (family) [28-42]
    - IPR019974: XPG conserved site (conserved_site) [79-93]
    - IPR006084: XPG/Rad2 endonuclease (family) [81-100]
    - IPR006084: XPG/Rad2 endonuclease (family) [145-162]
    - IPR006086: XPG-I domain (domain) [146-218]
    - IPR006086: XPG-I domain (domain) [149-233]
    - IPR019974: XPG conserved site (conserved_site) [149-163]
    - IPR006084: XPG/Rad2 endonuclease (family) [166-186]
    - IPR036279: 5'-3' exonuclease, C-terminal domain superfamily (homologous_superfamily) [218-351]
    - IPR008918: Helix-hairpin-helix motif, class 2 (conserved_site) [220-253]
    - IPR006084: XPG/Rad2 endonuclease (family) [223-238]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


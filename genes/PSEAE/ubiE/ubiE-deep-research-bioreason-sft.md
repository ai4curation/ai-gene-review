    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q9HUC0
    gene: ubiE
    organism: Pseudomonas aeruginosa (strain ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1)
    ---

    ## Thinking Trace

    I begin with the InterPro architecture. The core of the protein is defined by IPR004033 (UbiE/COQ5 methyltransferase family) spanning residues 21–255, with three overlapping entries across 21–255/25–255/30–255, indicating a canonical UbiE/COQ5 fold. This family assignment is embedded within IPR029063 (S-adenosyl-L-methionine-dependent methyltransferase superfamily, residues 18–253 and 36–256), which denotes a Rossmann-like class I SAM-dependent methyltransferase scaffold. Two conserved sites punctuate this core: IPR023576 at residues 41–56 and residues 163–177. These motifs typically organize the SAM-binding pocket and the catalytic environment that stabilizes the transition state for electrophilic methyl transfer to a carbon center. The ordered layout—superfamily Rossmann-like SAM-MTase scaffold with UbiE/COQ5 family determinants and two conserved catalytic/ligand-binding sites—causes a methyltransferase chemistry that uses S-adenosyl-L-methionine (SAM) to methylate a quinone ring at a defined carbon.

From this architecture, the molecular function resolves to a SAM-dependent quinone C-methylation. The UbiE/COQ5 family is specialized for methylating prenylated quinones at the C-3 position of demethylated intermediates. The presence of the UbiE/COQ5 family signatures together with the conserved sites that coordinate SAM and the quinone substrate supports the specific activity formalized as GO:0008924 3-demethylubiquinone methyltransferase activity. The same catalytic logic applies to demethylmenaquinone substrates in some bacteria, because the reaction is a carbon–carbon bond-forming methylation of a quinone headgroup; thus the enzyme can act on 3-demethylmenaquinone as well as 3-demethylubiquinone.

This chemistry feeds directly into quinone biosynthesis. By installing the C-3 methyl group, the enzyme completes the headgroup maturation of demethylmenaquinone, advancing it toward functional menaquinone. This places the protein in the biological process GO:0009234 menaquinone biosynthetic process. In organisms that use both ubiquinone and menaquinone pathways, UbiE/COQ5-like enzymes often exhibit substrate breadth governed by active-site determinants encoded in the family core; here, the UbiE/COQ5 family signatures and conserved sites are consistent with catalysis on demethylmenaquinone as part of the menaquinone branch.

The cellular context follows from the pathway organization. Quinone biosynthesis in Pseudomonas aeruginosa proceeds at the cytoplasmic face of the inner (plasma) membrane, where hydrophobic prenylated intermediates partition. UbiE/COQ5-like enzymes typically assemble into multi-enzyme metabolons with other quinone biosynthetic proteins to channel hydrophobic intermediates. This supports a residence within a GO:0032991 protein-containing complex. Given the membrane-proximal nature of the substrates and the need for efficient handoff among pathway enzymes, the most plausible physical setting is at the bacterial plasma membrane, where the enzyme associates peripherally with the membrane-resident biosynthetic machinery.

Mechanistically, the enzyme binds SAM in the Rossmann-like pocket formed by the class I methyltransferase superfamily scaffold (IPR029063) and positions 3-demethylmenaquinone (or 3-demethylubiquinone) in a hydrophobic channel shaped by the UbiE/COQ5 family core (IPR004033). The conserved sites at residues 41–56 and 163–177 stabilize the transition state for electrophilic substitution at C-3 of the quinone headgroup, transferring the methyl from SAM to yield the methylated quinone and S-adenosyl-L-homocysteine. Within a membrane-associated quinone biosynthetic complex, it likely receives the demethylated quinone from upstream methyltransferases and passes the product to downstream tailoring or modification steps.

This model predicts specific interaction partners. Association with 4-hydroxybenzoate-octaprenyl transferase positions the enzyme downstream of prenylation, while proximity to 3-demethylubiquinone 3-methyltransferase and Ubiquinone biosynthetic protein UbiB would organize a quinone-biosynthesis metabolon at the membrane. Contacts with NAD(P)H quinone oxidoreductase and probable NAD(P)H dehydrogenases could couple redox poise to quinone maturation, while the Trp repressor binding protein WrbA may buffer reactive oxygen species generated during quinone processing. The presence of a hypothetical protein partner suggests accessory scaffolds or adaptors that stabilize the complex. Together, these interactions would create a membrane-proximal assembly that channels hydrophobic intermediates and coordinates methylation with the rest of the quinone pathway.

    ## Functional Summary

    A SAM-dependent C-methyltransferase in Pseudomonas aeruginosa that installs the C-3 methyl group on demethylated menaquinone (and related demethylated quinone intermediates), thereby advancing menaquinone headgroup maturation within a membrane-associated quinone-biosynthesis assembly. The enzyme uses a Rossmann-like class I methyltransferase core to bind S-adenosyl-L-methionine and a UbiE/COQ5-specific pocket to position the quinone ring for electrophilic methyl transfer, likely operating at the cytoplasmic face of the inner membrane as part of a multi-enzyme complex that channels hydrophobic intermediates between pathway steps.

    ## UniProt Summary

    Menaquinone biosynthesis.

    ## InterPro Domains

        - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [18-253]
    - IPR004033: UbiE/COQ5 methyltransferase (family) [21-255]
    - IPR004033: UbiE/COQ5 methyltransferase (family) [25-255]
    - IPR004033: UbiE/COQ5 methyltransferase (family) [30-255]
    - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [36-256]
    - IPR023576: UbiE/COQ5 methyltransferase, conserved site (conserved_site) [41-56]
    - IPR023576: UbiE/COQ5 methyltransferase, conserved site (conserved_site) [163-177]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


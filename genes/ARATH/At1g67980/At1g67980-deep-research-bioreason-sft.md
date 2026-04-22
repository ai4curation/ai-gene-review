    ---
    provider: bioreason-pro
    model: SFT
    source: huggingface.co/datasets/wanglab/protein_catalogue
    date: '2026-04-04'
    uniprot_id: Q9C9W3
    gene: At1g67980
    organism: Arabidopsis thaliana (Mouse-ear cress)
    ---

    ## Thinking Trace

    The architecture begins with two overlapping superfamily signatures, IPR029063 (S-adenosyl-L-methionine-dependent methyltransferase superfamily, residues 1–232) and IPR029063 (S-adenosyl-L-methionine-dependent methyltransferase superfamily, residues 12–230), which together define a Rossmann-like Class I SAM-dependent methyltransferase core. Nested within these are two family-level assignments, IPR002935 (Class I-like SAM-dependent O-methyltransferase, residues 9–231) and IPR002935 (Class I-like SAM-dependent O-methyltransferase, residues 21–231), specifying a small-molecule O-methyltransferase that uses S-adenosyl-L-methionine (SAM) as methyl donor. Critically, IPR050362 (Cation-dependent O-methyltransferase, residues 8–231) adds a mechanistic constraint: catalysis requires a divalent cation, typically Mg2+ or Mn2+, which coordinates the catechol/phenolate moieties and orients the hydroxyl group for nucleophilic attack on the SAM methyl group. The compact, single-domain layout from the N-terminus through the C-terminus indicates a soluble enzyme optimized for rapid SAM binding and phenolic substrate recognition rather than for multi-domain regulation.

This domain ensemble causes a specific molecular function: a SAM-dependent O-methyltransferase that binds a divalent metal to activate phenolic hydroxyls. The cation-dependent family signature explains GO:0046872 metal ion binding, as the active site uses Mg2+/Mn2+ to stabilize the deprotonated 3-hydroxyl of the aromatic ring. The Class I O-methyltransferase fold and the cation-dependent specialization together account for GO:0047554 caffeoyl-CoA O-methyltransferase activity, in which the enzyme transfers a methyl group from SAM to the 3-hydroxyl of caffeoyl-CoA to form feruloyl-CoA. The same chemistry extends to 5-hydroxyferuloyl-CoA to yield 4-coumaroyl-CoA, consistent with a catechol-recognition pocket that positions either the 3-OH of a caffeoyl-CoA-type substrate or the 5-OH of a feruloyl-CoA-type substrate for methyl transfer.

By producing feruloyl-CoA and 4-coumaroyl-CoA, the enzyme feeds the phenylpropanoid biosynthetic network, committing carbon flow toward lignin precursors, coumarins, and other phenolics. This places the protein squarely in GO:0009699 phenylpropanoid biosynthetic process. The single soluble Class I methyltransferase domain lacks transmembrane segments or targeting peptides, favoring a cytosolic location where phenylpropanoid enzymes assemble into dynamic metabolons. This supports GO:0005829 cytosol as the cellular component.

Mechanistically, the enzyme binds SAM in the Class I Rossmann-like pocket and coordinates a divalent cation that bridges the CoA-linked phenolic substrate, lowering the pKa of the target hydroxyl and aligning it for SN2 transfer. The reaction proceeds with S-adenosyl-L-homocysteine (SAH) formation, and catalytic turnover likely couples to local SAM regeneration and SAH clearance. In a cytosolic phenylpropanoid metabolon, the enzyme would receive substrates from 4-coumarate–CoA ligases (4CL1–4) that activate 4-coumarate to its CoA thioester, and from shikimate O-hydroxycinnamoyltransferase (HCT) that can channel p-coumaroyl shikimate/p-coumaroyl malate to CoA pools. Downstream, cinnamoyl-CoA reductases (CCR1/2) can draw off feruloyl-CoA toward monolignol biosynthesis, while chalcone synthase (CHS) and an HXXXD-type acyl-transferase may compete for or remodel phenylpropanoid CoA esters. Spermidine hydroxycinnamoyl transferase suggests side-branching to amide/peptide conjugates. These partners plausibly form transient, substrate-channeling assemblies that increase flux efficiency and minimize diffusion of reactive phenylpropanoid intermediates in the cytosol.

    ## Functional Summary

    A cytosolic, cation-dependent O-methyltransferase that uses S-adenosyl-L-methionine to methylate phenolic hydroxyls on CoA-activated hydroxycinnamates, converting caffeoyl-CoA to feruloyl-CoA and 5-hydroxyferuloyl-CoA to 4-coumaroyl-CoA. By installing this methyl group, it commits intermediates toward lignin-related and other phenylpropanoid branches. A divalent metal ion coordinates the phenolate and orients the substrate for SN2 methyl transfer, and the enzyme likely operates within a cytosolic metabolon that channels CoA esters between activating, transfer, and reductive steps to optimize flux and minimize intermediate loss.

    ## UniProt Summary

    Catalyzes the O-methylation of caffeoyl-CoA to feruloyl-CoA. Methylates also 5-hydroxyferuloyl-CoA to 4-coumaroyl-CoA.

    ## InterPro Domains

        - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [1-232]
    - IPR050362: Cation-dependent O-methyltransferase (family) [8-231]
    - IPR002935: Class I-like SAM-dependent O-methyltransferase (family) [9-231]
    - IPR029063: S-adenosyl-L-methionine-dependent methyltransferase superfamily (homologous_superfamily) [12-230]
    - IPR002935: Class I-like SAM-dependent O-methyltransferase (family) [21-231]

    ## GO Term Predictions

    ### Molecular Function


    ### Biological Process


    ### Cellular Component


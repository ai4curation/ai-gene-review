---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:45:30.497090'
end_time: '2026-10-25T23:59:14.323647'
duration_seconds: 823.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: GPC3
  gene_symbol: GPC3
  uniprot_accession: A0A9L0J2B1
  protein_description: 'RecName: Full=Glypican-3 {ECO:0000256|ARBA:ARBA00014712};'
  gene_info: Name=GPC3 {ECO:0000313|Ensembl:ENSEASP00005043430.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the glypican family.
  protein_domains: Glypican. (IPR001863); Glypican_CS. (IPR019803); Glypican (PF01153)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 67
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0J2B1
- **Protein Description:** RecName: Full=Glypican-3 {ECO:0000256|ARBA:ARBA00014712};
- **Gene Information:** Name=GPC3 {ECO:0000313|Ensembl:ENSEASP00005043430.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the glypican family.
- **Key Domains:** Glypican. (IPR001863); Glypican_CS. (IPR019803); Glypican (PF01153)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPC3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPC3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPC3** (gene ID: GPC3, UniProt: A0A9L0J2B1) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Glypican-3 (GPC3) of the Donkey, *Equus asinus* (UniProt A0A9L0J2B1): Function, Localization and Signaling Roles

## 1. Introduction and Summary

Glypican-3 (GPC3) is a cell-surface heparan sulfate proteoglycan. Its core protein is held on the outer face of the plasma membrane by a glycosylphosphatidylinositol (GPI) anchor. It belongs to the glypican family, which has six members in mammals (GPC1–GPC6) and homologs throughout the Eumetazoa [filmus-2008-glypicans-abstract].

The donkey entry A0A9L0J2B1 is an unreviewed TrEMBL record. Its gene model was computationally predicted by Ensembl (gene ENSEASG00005018489, transcript ENSEAST00005057340) from the chromosome-level Dezhou donkey reference genome [wang-2020-donkey-genome-abstract]. The gene lies on chromosome X and spans about 410 kb (`notes/ensembl_gene_model.txt`). That matches human GPC3, an X-linked gene at Xq26 that spans more than 500 kb [pilia-1996-sgbs-abstract]. UniProt annotates the donkey protein only by homology: as a "cell surface proteoglycan" localized to the cell membrane via a GPI anchor on the extracellular side, carrying the Pfam Glypican domain (PF01153) and the PROSITE glypican signature.

The symbol GPC3 is unambiguous for this entry. The protein name, family assignment (PANTHER PTHR10822:SF4, "Glypican-3") and domain content all agree, and no different gene sharing the symbol was found. However, the literature on the equid protein is essentially absent. Two PubMed searches for glypican-3 or GPC3 combined with horse, equine, donkey or *Equus* returned no records (`PLAN.md`). This report therefore infers donkey GPC3 function by orthology from the well-studied human and mouse proteins, and the sequence comparison strongly supports that inference. A0A9L0J2B1 (565 aa) is 92.6% identical to human GPC3 (P51654, 580 aa) across 555 aligned positions (`notes/alignment_donkey_vs_human.txt`). Its residues 45–565 are identical to residues 60–580 of the canonical-length donkey model A0A9L0JGR2, and A0A9L0JGR2 is 96.2% identical to human GPC3 over its full length (`notes/isoform_comparison.txt`).

The same comparison raises a caveat that runs through the rest of the report. A0A9L0J2B1 begins with a distinct 44-residue N-terminus (MSFQFAPGGC…WKGTPNKG). This replaces the first 59 residues of the canonical protein, which contain the signal peptide (human residues 1–24), Cys35 and the Wnt-binding residue Phe41. Ensembl places the first exon of this transcript about 15 kb downstream of the canonical first exon. It sits in the large intron upstream of the first coding exon it shares with the canonical model, which starts at X:79,350,965. It is one of six protein-coding transcript models annotated for the donkey gene, which encode proteins of 526 to 611 residues (`notes/ensembl_gene_model.txt`). A0A9L0J2B1 is therefore an alternative-first-exon isoform model. Whether it is supported by transcript evidence, and whether it can enter the secretory pathway, is unknown.

In summary, by orthology donkey GPC3 is a GPI-anchored, heparan-sulfate-bearing co-receptor and modulator of morphogen signaling at the cell surface. It is neither an enzyme nor a transporter. Its best-characterized molecular role is negative regulation of Hedgehog. The core protein binds Hedgehog and competes with the receptor Patched [capurro-2008-hedgehog-abstract], and binding triggers LRP1-mediated endocytosis and degradation of the complex [capurro-2012-lrp1-abstract]. GPC3 also stimulates canonical Wnt/β-catenin signaling by binding Wnts and Frizzled receptors and promoting Wnt–Frizzled signaling complexes [capurro-2005-wnt-hcc-abstract][capurro-2014-frizzled-abstract][li-2019-crd-wnt-abstract], and it modulates BMP and FGF responses during organogenesis [grisaru-2001-renal-abstract][paine-saunders-2000-bmp4-abstract]. In mammals, loss of GPC3 causes developmental overgrowth: Simpson-Golabi-Behmel syndrome (SGBS) in humans and a closely similar phenotype in mice [pilia-1996-sgbs-abstract][cano-gauci-1999-knockout-abstract].

## 2. Molecular Architecture, Processing and Conservation in the Donkey Protein

Glypicans share a common plan. A conserved N-terminal globular core of about 45 kDa is followed by a stalk that carries the heparan sulfate (HS) attachment sites and ends in the GPI anchor [kim-2011-dlp-structure-abstract]. The crystal structure of the Drosophila glypican Dally-like core showed an elongated, entirely α-helical fold unlike any previously known structure [kim-2011-dlp-structure-abstract]. The 2.5-Å structure of human GPC1, the first structure of a vertebrate glypican, resolved the complete disulfide arrangement of the 14 conserved cysteines in this helical domain [svensson-2012-gpc1-structure-abstract]. It also showed that the helical domain itself steers which sugar is added to the stalk: without it, the stalk receives almost only chondroitin sulfate rather than heparan sulfate [svensson-2012-gpc1-structure-abstract].

Phylogenetically, glypicans fall into two subfamilies, GPC1/2/4/6 and GPC3/5, which share only about 25% identity. GPC3 belongs to the same branch as Drosophila Dally [filmus-2008-glypicans-fulltext], and Dally was among the first glypicans shown genetically to control morphogen signaling: it is required for normal cellular responses to the BMP homolog Decapentaplegic [jackson-1997-dally-abstract].

GPC3 is processed by a furin-like proprotein convertase at the paired-basic motif R355-QYR358. Cleavage produces an N-terminal α subunit and a C-terminal β subunit, which stay joined by disulfide bonds and remain GPI-anchored. A second cleavage can later separate the protein from its anchor and release it [de-cat-2003-processing-abstract][de-cat-2003-processing-fulltext]. Glypicans can also be released by Notum, a secreted lipase that acts extracellularly to cleave the GPI anchor of several mammalian glypicans [traister-2008-notum-abstract].

These features map almost perfectly onto the donkey sequence (`notes/residue_mapping.txt`). In A0A9L0J2B1 numbering:

- The convertase motif is R340-QYR343.
- The HS attachment serines are Ser480 and Ser494, corresponding to human Ser495 and Ser509.
- The predicted GPI ω-site is Asn539, corresponding to human Asn554.
- The protein ends in the expected hydrophobic GPI-signal stretch (…LTSLAIYVVCFFFLVH).
- The N-glycosylation sites corresponding to human Asn124 and Asn241 are present as Asn109 and Asn226.
- The total of 18 cysteines matches human GPC3.
- Trp281 is conserved. It corresponds to human Trp296, a residue conserved in all known glypicans. The SGBS missense mutation W296R gives a poorly processed protein that fails to increase cell-surface heparan sulfate, so it is a loss-of-function allele [veugelers-2000-sgbs-abstract].

The donkey protein therefore keeps all the processing, glycosaminoglycan-attachment and membrane-anchoring signals known to matter for GPC3 function. Its only notable departure is the alternative N-terminus described in the Introduction.

## 3. Subcellular Localization and Trafficking

GPC3 works at the outer leaflet of the plasma membrane, where it is tethered by its GPI anchor [filmus-2008-glypicans-abstract][cano-gauci-1999-knockout-abstract]. It is not static there, and its position changes its function.

A soluble pool forms through shedding. Glypicans are constitutively released from cultured cells, and GPC3 can be separated from its anchor by a second proteolytic event after convertase processing [de-cat-2003-processing-fulltext]. Notum releases it by cleaving the GPI anchor in the extracellular space, and in a cell system where GPC3 promotes Wnt signaling, Notum acts as a negative regulator of that signaling [traister-2008-notum-abstract]. Shed GPC3 is functionally distinct from the anchored form. A recombinant GPC3 lacking its GPI-anchoring domain blocked Wnt signaling and inhibited hepatocellular carcinoma growth in vitro and in xenografts, so membrane attachment is needed for GPC3 to stimulate Wnt, while soluble GPC3 acts as a competitive ligand trap [zittermann-2010-soluble-abstract]. In human hepatocellular carcinoma, circulating GPC3 is detectable in serum [capurro-2003-marker-abstract].

Ligand binding also moves GPC3 into the endocytic pathway. Wnt binding triggers endocytosis of a Wnt–Frizzled–GPC3 complex [capurro-2014-frizzled-abstract]. Hedgehog binding drives internalization and lysosomal degradation of the Hedgehog–GPC3 complex [capurro-2008-hedgehog-abstract]. That internalization depends on the low-density-lipoprotein receptor-related protein 1 (LRP1), which binds GPC3 through its HS chains and moves it out of lipid-raft membrane domains [capurro-2012-lrp1-abstract]. Endosomes and lysosomes are therefore part of the protein's working itinerary, not just its route to disposal.

Not every reported activity needs membrane attachment. An anchor-less GPC3 still induced apoptosis in a DPP4-expressing liver cell line [davoodi-2007-dpp4-abstract].

For the A0A9L0J2B1 variant specifically, plasma-membrane localization depends on whether its unusual N-terminus can act as a signal peptide, which has not been tested. The canonical-length donkey model A0A9L0JGR2 keeps the canonical signal sequence almost unchanged (MAGTVHTACLVVAMLLSLDCPG…), so canonical localization is expected for that protein.

## 4. Role in Hedgehog Signaling: a Competitive Decoy at the Reception Step

The strongest mechanistic explanation of GPC3's role as a growth suppressor involves Hedgehog. Capurro and colleagues found that Gpc3-null mouse embryos have increased Hedgehog signaling and that GPC3 inhibits Hedgehog activity in cultured embryonic fibroblasts [capurro-2008-hedgehog-abstract]. GPC3 binds Hedgehog with high affinity but does not bind Patched. It competes with Patched for Hedgehog and induces Hedgehog endocytosis and degradation, and the HS chains are not needed for the Hedgehog interaction [capurro-2008-hedgehog-abstract].

The internalization step was traced to LRP1. LRP1 mediates the Hedgehog-induced endocytosis of the GPC3–Hedgehog complex, binding GPC3 through its HS chains, and this endocytosis is required for GPC3 to inhibit Hedgehog [capurro-2012-lrp1-abstract]. The two parts of the proteoglycan therefore divide the work. The core protein captures the ligand, while the glycosaminoglycan chains engage the endocytic receptor that removes the complex from the surface. The authors concluded that the overgrowth seen in SGBS comes at least partly from hyperactive Hedgehog signaling [capurro-2008-hedgehog-abstract][filmus-2008-body-size-abstract]. Later reviews place this regulation at the level of signal reception [filmus-2014-hedgehog-review-abstract].

Convertase cleavage is essential for Hedgehog inhibition. A convertase-resistant GPC3 mutant failed to inhibit Hedgehog and instead stimulated signaling by increasing Hedgehog binding to Patched. This reversal came from unusually highly sulfated HS chains on the mutant, which bound both Hedgehog and Patched, while the mutant core protein had lost its ability to bind Hedgehog [capurro-2015-convertase-hh-abstract]. Cleavage therefore acts as a structural switch that sets both the ligand-binding shape of the core and the sulfation pattern of the attached HS.

Work on liver regeneration extended the model to Indian Hedgehog. GPC3 binding to Indian Hedgehog falls at the peak of hepatocyte proliferation, while the Hedgehog effector Gli1 rises [bhave-2013-cd81-abstract]. Heart development provides a contrasting case. Gpc3-deficient mouse embryos show reduced, not increased, Sonic Hedgehog expression and signaling in the heart, asymmetrically between cardiomyocytes and perivascular cells. They also show delayed formation of the coronary plexus, excessive coronary arteries, coronary artery fistulas and congenital heart malformations. The authors attributed this to GPC3 acting as a co-receptor for FGF9, which acts upstream of Sonic Hedgehog in the heart [ng-2009-coronary-abstract]. So the net effect of GPC3 on Hedgehog output depends on the tissue.

The structural basis of Hedgehog recognition is still unresolved. The purified core of Dally-like, from the other glypican subfamily, did not bind Hedgehog appreciably, although a surface patch on it was needed for Hedgehog responsiveness [kim-2011-dlp-structure-abstract]. Because the donkey protein keeps the convertase site, the HS-attachment serines and a helical core nearly identical to human GPC3, the same competitive, LRP1-dependent inhibition of Hedgehog is expected in equids. The extent to which the alternative N-terminus of A0A9L0J2B1 affects Hedgehog binding is unknown.

## 5. Role in Wnt Signaling: Co-receptor for Canonical and Non-canonical Pathways

GPC3 can raise or lower Wnt signaling depending on cell type, and several partly overlapping mechanisms have been described.

In hepatocellular carcinoma (HCC) cells, GPC3 promotes growth in vitro and in vivo by increasing autocrine and paracrine canonical Wnt signaling. It forms complexes with Wnts and raises the amount of Wnt bound at the cell surface [capurro-2005-wnt-hcc-abstract]. Two results were unexpected. The non-glycanated core protein can still bind Wnt, and the glycosaminoglycan chains are not needed for the growth effect [capurro-2005-wnt-hcc-abstract]. Nor is convertase processing required in these cells [capurro-2005-convertase-wnt-abstract].

Later work showed that GPC3 does more than concentrate ligand. GPC3 binds Frizzled receptors directly through its HS chains, which promotes formation of Wnt–Frizzled signaling complexes, and Wnt binding then triggers co-endocytosis of the ternary complex [capurro-2014-frizzled-abstract]. The related GPC6 also binds Wnt at the membrane but inhibits canonical signaling, which shows that ligand binding alone cannot explain stimulation [capurro-2014-frizzled-abstract]. An antibody approach supported an HS contribution: HS20, an antibody that recognizes the HS chains of GPC3, disrupted Wnt3a–GPC3 binding and blocked β-catenin signaling and xenograft growth [gao-2014-hs-antibody-abstract].

Li and colleagues described a second Wnt-binding site in the protein core. Using a structural model, they identified a Frizzled-like cysteine-rich domain in the N-terminal lobe of GPC3. It contains a hydrophobic groove formed by Phe41 and nearby residues, which binds the middle region of Wnt3a between its lipid "thumb" and "index finger" [li-2019-crd-wnt-abstract]. Mutating residues in this groove, especially F41, W260, Y264 and M269, greatly reduced Wnt3a binding [li-2019-crd-wnt-fulltext]. An F41E mutant reduced β-catenin activation and HCC xenograft growth. The core-protein site appeared to matter most when Frizzled was scarce [li-2019-crd-wnt-abstract]. The same group later noted that the therapeutic antibody HN3 recognizes this conformational epitope [kolluri-2019-gpc3-liver-review-fulltext].

This finding bears directly on the donkey A0A9L0J2B1 model, because its alternative N-terminus lacks the segment containing Phe41. The other groove residues are conserved as Trp245, Tyr249 and Met254 (human W260, Y264 and M269), and so are the C-terminal-lobe residues tested in that study (`notes/residue_mapping.txt`). If this variant is a real protein, it could have reduced core-mediated Wnt binding while keeping HS-mediated Frizzled engagement. The canonical donkey GPC3 (A0A9L0JGR2) has the complete groove. This prediction rests on sequence inference alone.

Outside the liver, GPC3 can act as a selective switch between Wnt pathways. In Gpc3-null mice, non-canonical Wnt/JNK signaling was reduced and canonical Wnt/β-catenin signaling was increased. In mesothelioma cells, GPC3 enhanced the response to Wnt5a, and neither GPC3–Wnt5a complex formation nor this stimulation required HS [song-2005-wnt-loss-abstract]. The same study argued against the long-standing idea that GPC3 controls growth through IGF signaling [song-2005-wnt-loss-abstract]. That idea traced back to early ligand-blotting evidence of IGF2 binding [pilia-1996-sgbs-abstract], and the normal IGF-II levels in Gpc3-null mice had already weakened it [cano-gauci-1999-knockout-abstract].

During gastrulation, Wnt5a binds only processed GPC3. Only a cleavable GPC3 rescued epiboly and convergent-extension movements in zebrafish morphants, and in vitro effects on Wnt signaling needed both the core protein and HS [de-cat-2003-processing-abstract]. Taken together, the Wnt literature shows that GPC3's dependence on cleavage and on HS varies with cell type and pathway [capurro-2005-convertase-wnt-abstract][filmus-2008-glypicans-abstract]. Reviews of liver cancer also connect GPC3 to the Hippo–YAP pathway. GPC3 knockdown reduced HCC cell proliferation, and YAP rescued the resulting apoptosis, but the review describes the mechanism of this crosstalk as undetermined [kolluri-2019-gpc3-liver-review-fulltext].

## 6. BMP, FGF and Other Interactions; Developmental Roles

GPC3 also tunes signaling by the TGF-β/BMP superfamily and by FGFs, a role that goes back to its fly ortholog [jackson-1997-dally-abstract]. In embryonic mouse kidney explants, loss of GPC3 had three effects on ureteric bud branching:

- it removed the inhibitory effect of BMP2;
- it turned BMP7 from an inhibitor into a stimulator;
- it strengthened the stimulatory effect of KGF (FGF7).

Comparable differences appeared in collecting-duct cell lines, pointing to a direct, cell-autonomous effect on how these cells respond to growth factors [grisaru-2001-renal-abstract]. Genetically, Gpc3-deficient mice that also carry only one copy of Bmp4 show highly penetrant postaxial polydactyly and rib malformations, linking GPC3 to BMP4 in limb and skeletal patterning [paine-saunders-2000-bmp4-abstract]. In the heart, GPC3 has been proposed as a co-receptor for FGF9 upstream of Sonic Hedgehog during coronary vascular development [ng-2009-coronary-abstract]. Across the family, glypicans can stimulate or inhibit Wnt, Hedgehog, FGF and BMP signaling depending on context, and depend on their HS chains only in part [filmus-2008-glypicans-abstract].

Several less established protein partners have been reported. GPC3 binds the tetraspanin CD81, which reduces CD81 binding to the transcriptional repressor Hhex. Hhex can then enter the nucleus, which the authors propose restrains hepatocyte proliferation [bhave-2013-cd81-abstract]. GPC3 was also isolated as a binding partner of CD26/DPP4, whose dipeptidyl peptidase activity it inhibited. Recombinant GPC3 reduced proliferation and induced apoptosis in DPP4-expressing cells [davoodi-2007-dpp4-abstract]. Each finding comes from a single group and should be treated as provisional.

At the organism level, these activities add up to a growth-restraining role during development. Gpc3-null mice show the following [cano-gauci-1999-knockout-abstract]:

- developmental overgrowth and perinatal lethality;
- cystic and dysplastic kidneys, caused by over-proliferation of the ureteric bud and collecting system;
- abnormal lung development;
- in some animals, mandibular hypoplasia.

Their kidneys show increased proliferation in cortical collecting ducts and a 16-fold rise in apoptosis in medullary collecting ducts [grisaru-2001-renal-abstract]. They also have a high incidence of ventricular septal defects, common atrioventricular canal, double-outlet right ventricle and coronary artery fistulas [ng-2009-coronary-abstract].

In humans, translocations, deletions and point mutations in GPC3 cause SGBS, an X-linked overgrowth syndrome with visceral and skeletal anomalies [pilia-1996-sgbs-abstract][veugelers-2000-sgbs-abstract]. GPC3 is expressed mainly in embryonic mesodermal tissues [pilia-1996-sgbs-abstract]. In adult liver it is an oncofetal marker, absent from normal hepatocytes but re-expressed in most hepatocellular carcinomas [capurro-2003-marker-abstract], which has made it a target for antibody-based cancer therapies [li-2018-glypicans-cancer-abstract][gao-2014-hs-antibody-abstract].

None of these phenotypes has been studied in equids. A similar developmental role is likely, since the gene is X-linked in both lineages and the protein is about 96% conserved.

## 7. Synthesis: Functional Annotation of Donkey GPC3

Taken together, the evidence supports annotating donkey GPC3 by orthology as an extracellular, GPI-anchored heparan sulfate proteoglycan of the plasma membrane. It works as a non-enzymatic co-receptor and ligand-sequestering modulator of developmental morphogens. It has no catalytic activity and transports no substrate. Its function comes from binding signaling proteins and controlling how they reach, or are kept from, their receptors.

The best-supported activity is negative regulation of Hedgehog signaling. The convertase-processed core protein binds Hedgehog ligands, including Sonic and Indian Hedgehog, and competes with Patched. The HS chains then recruit LRP1 to internalize the complex for lysosomal degradation [capurro-2008-hedgehog-abstract][capurro-2012-lrp1-abstract][capurro-2015-convertase-hh-abstract][bhave-2013-cd81-abstract].

Comparably strong is positive regulation of canonical Wnt signaling. GPC3 binds Wnt ligands such as Wnt3a through a hydrophobic groove in the core protein and binds Frizzled receptors through its HS chains, promoting Wnt–Frizzled complexes and their internalization. This stimulation needs membrane anchoring and is opposed by Notum-mediated shedding [capurro-2005-wnt-hcc-abstract][capurro-2014-frizzled-abstract][li-2019-crd-wnt-abstract][gao-2014-hs-antibody-abstract][traister-2008-notum-abstract][zittermann-2010-soluble-abstract].

Two further activities are context-dependent. GPC3 regulates non-canonical Wnt5a/JNK signaling and the cell movements of gastrulation [song-2005-wnt-loss-abstract][de-cat-2003-processing-abstract]. It also modulates BMP2/4/7, FGF7 and FGF9 responses during kidney branching, limb and skeletal patterning, and coronary vascular development [grisaru-2001-renal-abstract][paine-saunders-2000-bmp4-abstract][ng-2009-coronary-abstract]. Together these activities account for its physiological role in limiting body and organ growth [cano-gauci-1999-knockout-abstract][filmus-2008-body-size-abstract].

In Gene Ontology terms, appropriate inferred annotations are:

- **Location:** plasma membrane, the anchored component of the external side of the plasma membrane, and cell surface; extracellular space for the shed form.
- **Activity:** binding of Hedgehog family proteins, of Wnt proteins and of Frizzled receptors.
- **Process:** negative regulation of the smoothened (Hedgehog) signaling pathway, positive regulation of the canonical Wnt signaling pathway, regulation of the BMP signaling pathway, and negative regulation of organ growth.

All of these should carry orthology-based (ISS or IBA) evidence, because none has been shown directly for the donkey protein. A0A9L0J2B1 deserves extra caution, since its N-terminus lacks the canonical signal peptide and the Phe41-containing Wnt-binding region. The canonical-length donkey entry A0A9L0JGR2 is the better reference protein for transferring annotations.

## 8. Open Questions

The first and most specific question is whether the alternative first exon behind A0A9L0J2B1 is real. It lies about 15 kb downstream of the canonical first exon of the donkey gene. Equine short-read and long-read RNA sequencing, together with comparison against horse and other perissodactyl genomes, would show whether its 44-residue N-terminus is a genuine product or an artifact of automated gene prediction. If it is real, it would be worth testing whether the protein is secreted and GPI-anchored without a canonical signal peptide. Assays of Wnt3a binding would then show whether losing the Phe41 groove reduces core-mediated Wnt binding while sparing HS-mediated Frizzled engagement.

A second gap is that no expression data or phenotypes are available for any equid. Fetal-tissue expression atlases, such as those produced by the equine FAANG effort, would test whether the embryonic mesodermal and hepatic expression seen in human and mouse is conserved. Because GPC3 is X-linked and controls body size in mammals, variants near the gene could also be examined for associations with body-size variation among donkey and horse breeds, or with equine liver neoplasia.

Several mechanistic questions remain open even in the best-studied species. GPC3 has no experimental atomic structure, and the Wnt-binding groove is defined by a homology model [li-2019-crd-wnt-abstract]. How the cleaved core recognizes Hedgehog is also unknown, especially since the core of Dally-like does not bind Hedgehog [kim-2011-dlp-structure-abstract]. The proposed link between convertase cleavage, HS sulfation and the switch between Hedgehog inhibition and stimulation [capurro-2015-convertase-hh-abstract] would benefit from independent replication, as would the opposite effects of GPC3 loss on Hedgehog output in the heart and in the embryo as a whole [ng-2009-coronary-abstract][capurro-2008-hedgehog-abstract].

Finally, several reported links need independent biochemical confirmation and a clearer mechanism. These are the interactions with CD81/Hhex and DPP4 [bhave-2013-cd81-abstract][davoodi-2007-dpp4-abstract], and the connection to YAP signaling [kolluri-2019-gpc3-liver-review-fulltext].

## 9. References

Citation keys map to files in `citations/` (`<key>-abstract.md`, `<key>-summary.md`, and, where available, `<key>-fulltext.txt`).

* **de-cat-2003-processing** — De Cat B; Muyldermans SY; Coomans C et al. Processing by proprotein convertases is required for glypican-3 modulation of cell survival, Wnt signaling, and gastrulation movements. *J Cell Biol 2003;163(3):625-35*. PMID: 14610063. DOI: 10.1083/jcb.200302152. PMCID: PMC2173654. https://pubmed.ncbi.nlm.nih.gov/14610063/
* **capurro-2005-wnt-hcc** — Capurro MI; Xiang YY; Lobe C et al. Glypican-3 promotes the growth of hepatocellular carcinoma by stimulating canonical Wnt signaling. *Cancer Res 2005;65(14):6245-54*. PMID: 16024626. DOI: 10.1158/0008-5472.CAN-04-4244. https://pubmed.ncbi.nlm.nih.gov/16024626/
* **capurro-2005-convertase-wnt** — Capurro MI; Shi W; Sandal S et al. Processing by convertases is not required for glypican-3-induced stimulation of hepatocellular carcinoma growth. *J Biol Chem 2005;280(50):41201-6*. PMID: 16227623. DOI: 10.1074/jbc.M507004200. https://pubmed.ncbi.nlm.nih.gov/16227623/
* **capurro-2014-frizzled** — Capurro M; Martin T; Shi W et al. Glypican-3 binds to Frizzled and plays a direct role in the stimulation of canonical Wnt signaling. *J Cell Sci 2014;127(Pt 7):1565-75*. PMID: 24496449. DOI: 10.1242/jcs.140871. https://pubmed.ncbi.nlm.nih.gov/24496449/
* **davoodi-2007-dpp4** — Davoodi J; Kelly J; Gendron NH et al. The Simpson-Golabi-Behmel syndrome causative glypican-3, binds to and inhibits the dipeptidyl peptidase activity of CD26. *Proteomics 2007;7(13):2300-10*. PMID: 17549790. DOI: 10.1002/pmic.200600654. https://pubmed.ncbi.nlm.nih.gov/17549790/
* **capurro-2015-convertase-hh** — Capurro M; Shi W; Izumikawa T et al. Processing by convertases is required for glypican-3-induced inhibition of Hedgehog signaling. *J Biol Chem 2015;290(12):7576-85*. PMID: 25653284. DOI: 10.1074/jbc.M114.612705. PMCID: PMC4367263. https://pubmed.ncbi.nlm.nih.gov/25653284/
* **pilia-1996-sgbs** — Pilia G; Hughes-Benzie RM; MacKenzie A et al. Mutations in GPC3, a glypican gene, cause the Simpson-Golabi-Behmel overgrowth syndrome. *Nat Genet 1996;12(3):241-7*. PMID: 8589713. DOI: 10.1038/ng0396-241. https://pubmed.ncbi.nlm.nih.gov/8589713/
* **capurro-2003-marker** — Capurro M; Wanless IR; Sherman M et al. Glypican-3: a novel serum and histochemical marker for hepatocellular carcinoma. *Gastroenterology 2003;125(1):89-97*. PMID: 12851874. DOI: 10.1016/s0016-5085(03)00689-9. https://pubmed.ncbi.nlm.nih.gov/12851874/
* **veugelers-2000-sgbs** — Veugelers M; Cat BD; Muyldermans SY et al. Mutational analysis of the GPC3/GPC4 glypican gene cluster on Xq26 in patients with Simpson-Golabi-Behmel syndrome: identification of loss-of-function mutations in the GPC3 gene. *Hum Mol Genet 2000;9(9):1321-8*. PMID: 10814714. DOI: 10.1093/hmg/9.9.1321. https://pubmed.ncbi.nlm.nih.gov/10814714/
* **cano-gauci-1999-knockout** — Cano-Gauci DF; Song HH; Yang H et al. Glypican-3-deficient mice exhibit developmental overgrowth and some of the abnormalities typical of Simpson-Golabi-Behmel syndrome. *J Cell Biol 1999;146(1):255-64*. PMID: 10402475. DOI: 10.1083/jcb.146.1.255. PMCID: PMC2199732. https://pubmed.ncbi.nlm.nih.gov/10402475/
* **capurro-2008-hedgehog** — Capurro MI; Xu P; Shi W et al. Glypican-3 inhibits Hedgehog signaling during development by competing with patched for Hedgehog binding. *Dev Cell 2008;14(5):700-11*. PMID: 18477453. DOI: 10.1016/j.devcel.2008.03.006. https://pubmed.ncbi.nlm.nih.gov/18477453/
* **kim-2011-dlp-structure** — Kim MS; Saunders AM; Hamaoka BY et al. Structure of the protein core of the glypican Dally-like and localization of a region important for hedgehog signaling. *Proc Natl Acad Sci U S A 2011;108(32):13112-7*. PMID: 21828006. DOI: 10.1073/pnas.1109877108. PMCID: PMC3156181. https://pubmed.ncbi.nlm.nih.gov/21828006/
* **grisaru-2001-renal** — Grisaru S; Cano-Gauci D; Tee J et al. Glypican-3 modulates BMP- and FGF-mediated effects during renal branching morphogenesis. *Dev Biol 2001;231(1):31-46*. PMID: 11180950. DOI: 10.1006/dbio.2000.0127. https://pubmed.ncbi.nlm.nih.gov/11180950/
* **paine-saunders-2000-bmp4** — Paine-Saunders S; Viviano BL; Zupicich J et al. glypican-3 controls cellular responses to Bmp4 in limb patterning and skeletal development. *Dev Biol 2000;225(1):179-87*. PMID: 10964473. DOI: 10.1006/dbio.2000.9831. https://pubmed.ncbi.nlm.nih.gov/10964473/
* **filmus-2008-glypicans** — Filmus J; Capurro M; Rast J. Glypicans. *Genome Biol 2008;9(5):224*. PMID: 18505598. DOI: 10.1186/gb-2008-9-5-224. PMCID: PMC2441458. https://pubmed.ncbi.nlm.nih.gov/18505598/
* **filmus-2014-hedgehog-review** — Filmus J; Capurro M. The role of glypicans in Hedgehog signaling. *Matrix Biol 2014;35:248-52*. PMID: 24412155. DOI: 10.1016/j.matbio.2013.12.007. https://pubmed.ncbi.nlm.nih.gov/24412155/
* **filmus-2008-body-size** — Filmus J; Capurro M. The role of glypican-3 in the regulation of body size and cancer. *Cell Cycle 2008;7(18):2787-90*. PMID: 18787398. DOI: 10.4161/cc.7.18.6672. https://pubmed.ncbi.nlm.nih.gov/18787398/
* **li-2019-crd-wnt** — Li N; Wei L; Liu X et al. A Frizzled-Like Cysteine-Rich Domain in Glypican-3 Mediates Wnt Binding and Regulates Hepatocellular Carcinoma Tumor Growth in Mice. *Hepatology 2019;70(4):1231-1245*. PMID: 30963603. DOI: 10.1002/hep.30646. PMCID: PMC6783318. https://pubmed.ncbi.nlm.nih.gov/30963603/
* **bhave-2013-cd81** — Bhave VS; Mars W; Donthamsetty S et al. Regulation of liver growth by glypican 3, CD81, hedgehog, and Hhex. *Am J Pathol 2013;183(1):153-9*. PMID: 23665349. DOI: 10.1016/j.ajpath.2013.03.013. PMCID: PMC3702736. https://pubmed.ncbi.nlm.nih.gov/23665349/
* **song-2005-wnt-loss** — Song HH; Shi W; Xiang YY et al. The loss of glypican-3 induces alterations in Wnt signaling. *J Biol Chem 2005;280(3):2116-25*. PMID: 15537637. DOI: 10.1074/jbc.M410090200. https://pubmed.ncbi.nlm.nih.gov/15537637/
* **svensson-2012-gpc1-structure** — Svensson G; Awad W; Håkansson M et al. Crystal structure of N-glycosylated human glypican-1 core protein: structure of two loops evolutionarily conserved in vertebrate glypican-1. *J Biol Chem 2012;287(17):14040-51*. PMID: 22351761. DOI: 10.1074/jbc.M111.322487. PMCID: PMC3340175. https://pubmed.ncbi.nlm.nih.gov/22351761/
* **gao-2014-hs-antibody** — Gao W; Kim H; Feng M et al. Inactivation of Wnt signaling by a human antibody that recognizes the heparan sulfate chains of glypican-3 for liver cancer therapy. *Hepatology 2014;60(2):576-87*. PMID: 24492943. DOI: 10.1002/hep.26996. PMCID: PMC4083010. https://pubmed.ncbi.nlm.nih.gov/24492943/
* **li-2018-glypicans-cancer** — Li N; Gao W; Zhang YF et al. Glypicans as Cancer Therapeutic Targets. *Trends Cancer 2018;4(11):741-754*. PMID: 30352677. DOI: 10.1016/j.trecan.2018.09.004. PMCID: PMC6209326. https://pubmed.ncbi.nlm.nih.gov/30352677/
* **wang-2020-donkey-genome** — Wang C; Li H; Guo Y et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun 2020;11(1):6014*. PMID: 33293529. DOI: 10.1038/s41467-020-19813-7. PMCID: PMC7723042. https://pubmed.ncbi.nlm.nih.gov/33293529/
* **capurro-2012-lrp1** — Capurro MI; Shi W; Filmus J. LRP1 mediates Hedgehog-induced endocytosis of the GPC3-Hedgehog complex. *J Cell Sci 2012;125(Pt 14):3380-9*. PMID: 22467855. DOI: 10.1242/jcs.098889. PMCID: PMC3843007. https://pubmed.ncbi.nlm.nih.gov/22467855/
* **kolluri-2019-gpc3-liver-review** — Kolluri A; Ho M. The Role of Glypican-3 in Regulating Wnt, YAP, and Hedgehog in Liver Cancer. *Front Oncol 2019;9:708*. PMID: 31428581. DOI: 10.3389/fonc.2019.00708. PMCID: PMC6688162. https://pubmed.ncbi.nlm.nih.gov/31428581/
* **zittermann-2010-soluble** — Zittermann SI; Capurro MI; Shi W et al. Soluble glypican 3 inhibits the growth of hepatocellular carcinoma in vitro and in vivo. *Int J Cancer 2010;126(6):1291-301*. PMID: 19816934. DOI: 10.1002/ijc.24941. https://pubmed.ncbi.nlm.nih.gov/19816934/
* **ng-2009-coronary** — Ng A; Wong M; Viviano B et al. Loss of glypican-3 function causes growth factor-dependent defects in cardiac and coronary vascular development. *Dev Biol 2009;335(1):208-15*. PMID: 19733558. DOI: 10.1016/j.ydbio.2009.08.029. PMCID: PMC2763964. https://pubmed.ncbi.nlm.nih.gov/19733558/
* **traister-2008-notum** — Traister A; Shi W; Filmus J. Mammalian Notum induces the release of glypicans and other GPI-anchored proteins from the cell surface. *Biochem J 2008;410(3):503-11*. PMID: 17967162. DOI: 10.1042/BJ20070511. https://pubmed.ncbi.nlm.nih.gov/17967162/
* **jackson-1997-dally** — Jackson SM; Nakato H; Sugiura M et al. dally, a Drosophila glypican, controls cellular responses to the TGF-beta-related morphogen, Dpp. *Development 1997;124(20):4113-20*. PMID: 9374407. DOI: 10.1242/dev.124.20.4113. https://pubmed.ncbi.nlm.nih.gov/9374407/
* **UniProt A0A9L0J2B1** — UniProtKB/TrEMBL entry, Glypican-3, *Equus asinus*. https://rest.uniprot.org/uniprotkb/A0A9L0J2B1.txt (local sequence: notes/A0A9L0J2B1.fasta)
* **UniProt A0A9L0JGR2** — UniProtKB/TrEMBL entry, Glypican-3 (canonical-length model), *Equus asinus*. https://rest.uniprot.org/uniprotkb/A0A9L0JGR2.fasta
* **UniProt P51654** — UniProtKB/Swiss-Prot entry, Glypican-3, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/P51654.txt (local copy: notes/P51654_human.txt)
* **Ensembl ENSEASG00005018489** — Ensembl gene model for donkey GPC3, queried via https://rest.ensembl.org/lookup/id/ENSEASG00005018489 (local output: notes/ensembl_gene_model.txt)


## Citations

1. bhave-2013-cd81-abstract.md
2. bhave-2013-cd81-summary.md
3. cano-gauci-1999-knockout-abstract.md
4. cano-gauci-1999-knockout-fulltext.txt
5. cano-gauci-1999-knockout-summary.md
6. capurro-2003-marker-abstract.md
7. capurro-2003-marker-summary.md
8. capurro-2005-convertase-wnt-abstract.md
9. capurro-2005-convertase-wnt-summary.md
10. capurro-2005-wnt-hcc-abstract.md
11. capurro-2005-wnt-hcc-summary.md
12. capurro-2008-hedgehog-abstract.md
13. capurro-2008-hedgehog-summary.md
14. capurro-2012-lrp1-abstract.md
15. capurro-2012-lrp1-summary.md
16. capurro-2014-frizzled-abstract.md
17. capurro-2014-frizzled-summary.md
18. capurro-2015-convertase-hh-abstract.md
19. capurro-2015-convertase-hh-summary.md
20. davoodi-2007-dpp4-abstract.md
21. davoodi-2007-dpp4-summary.md
22. de-cat-2003-processing-abstract.md
23. de-cat-2003-processing-fulltext.txt
24. de-cat-2003-processing-summary.md
25. filmus-2008-body-size-abstract.md
26. filmus-2008-body-size-summary.md
27. filmus-2008-glypicans-abstract.md
28. filmus-2008-glypicans-fulltext.txt
29. filmus-2008-glypicans-summary.md
30. filmus-2014-hedgehog-review-abstract.md
31. filmus-2014-hedgehog-review-summary.md
32. gao-2014-hs-antibody-abstract.md
33. gao-2014-hs-antibody-fulltext.txt
34. gao-2014-hs-antibody-summary.md
35. grisaru-2001-renal-abstract.md
36. grisaru-2001-renal-summary.md
37. jackson-1997-dally-abstract.md
38. jackson-1997-dally-summary.md
39. kim-2011-dlp-structure-abstract.md
40. kim-2011-dlp-structure-summary.md
41. kolluri-2019-gpc3-liver-review-abstract.md
42. kolluri-2019-gpc3-liver-review-fulltext.txt
43. kolluri-2019-gpc3-liver-review-summary.md
44. li-2018-glypicans-cancer-abstract.md
45. li-2018-glypicans-cancer-summary.md
46. li-2019-crd-wnt-abstract.md
47. li-2019-crd-wnt-fulltext.txt
48. li-2019-crd-wnt-summary.md
49. ng-2009-coronary-abstract.md
50. ng-2009-coronary-summary.md
51. paine-saunders-2000-bmp4-abstract.md
52. paine-saunders-2000-bmp4-summary.md
53. pilia-1996-sgbs-abstract.md
54. pilia-1996-sgbs-summary.md
55. song-2005-wnt-loss-abstract.md
56. song-2005-wnt-loss-summary.md
57. svensson-2012-gpc1-structure-abstract.md
58. svensson-2012-gpc1-structure-summary.md
59. traister-2008-notum-abstract.md
60. traister-2008-notum-summary.md
61. veugelers-2000-sgbs-abstract.md
62. veugelers-2000-sgbs-summary.md
63. wang-2020-donkey-genome-abstract.md
64. wang-2020-donkey-genome-fulltext.txt
65. wang-2020-donkey-genome-summary.md
66. zittermann-2010-soluble-abstract.md
67. zittermann-2010-soluble-summary.md
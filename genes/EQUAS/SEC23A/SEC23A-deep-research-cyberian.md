---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:59:01.947949'
end_time: '2026-10-26T01:13:19.381710'
duration_seconds: 857.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: SEC23A
  gene_symbol: SEC23A
  uniprot_accession: A0A9L0IQB9
  protein_description: 'RecName: Full=Protein transport protein SEC23 {ECO:0000256|RuleBase:RU365030};'
  gene_info: Name=SEC23A {ECO:0000313|Ensembl:ENSEASP00005039976.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the SEC23/SEC24 family. SEC23 subfamily.
  protein_domains: ADF-H/Gelsolin-like_dom_sf. (IPR029006); Beta-sandwich_Sec23_24.
    (IPR012990); Gelsolin-like_dom. (IPR007123); Gelsolin-like_dom_sf. (IPR036180);
    Sec23. (IPR037364)
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
citation_count: 111
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IQB9
- **Protein Description:** RecName: Full=Protein transport protein SEC23 {ECO:0000256|RuleBase:RU365030};
- **Gene Information:** Name=SEC23A {ECO:0000313|Ensembl:ENSEASP00005039976.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the SEC23/SEC24 family. SEC23 subfamily.
- **Key Domains:** ADF-H/Gelsolin-like_dom_sf. (IPR029006); Beta-sandwich_Sec23_24. (IPR012990); Gelsolin-like_dom. (IPR007123); Gelsolin-like_dom_sf. (IPR036180); Sec23. (IPR037364)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SEC23A" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SEC23A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SEC23A** (gene ID: SEC23A, UniProt: A0A9L0IQB9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SEC23A (Protein transport protein SEC23A) in the donkey, *Equus asinus* (UniProt A0A9L0IQB9): Functional Annotation Review

## 1. Introduction and Summary

The donkey protein A0A9L0IQB9 is SEC23A, an inner-coat subunit of the coat protein complex II (COPII). It is a 739-residue product of the *SEC23A* gene on donkey chromosome 2, predicted from the donkey reference genome assembly [uniprot-A0A9L0IQB9-entry; wang-2020-donkey-genomes-abstract]. No experimental study of SEC23A in donkeys or any other equid could be found, and searches for donkey or equine SEC23A returned nothing. Every functional statement below is therefore transferred by orthology from human SEC23A (UniProt Q15436), mouse and zebrafish Sec23a, and yeast Sec23p.

That transfer is well supported. A pairwise alignment run for this report found 734 of the 765 residues of human SEC23A identical in the donkey protein (95.9%), with a single 26-residue gap. Every catalytic, metal-binding, disease-associated and regulatory residue examined is conserved (Section 2) [uniprot-A0A9L0IQB9-summary; uniprot-Q15436-human-SEC23A-entry]. The gene symbol, the protein name, the family assignment (SEC23/SEC24 family, SEC23 subfamily; PANTHER PTHR11141:SF7 "SEC23A") and the domain composition all agree. No unrelated gene shares the symbol, so the identification is not ambiguous [uniprot-A0A9L0IQB9-entry].

SEC23A's primary molecular function is as the **GTPase-activating protein (GAP) for the small GTPase SAR1**. It speeds up GTP hydrolysis by inserting an arginine side chain, the "arginine finger", into SAR1's active site [yoshihisa-1993-sar1-gap-abstract; bi-2002-prebudding-complex-abstract]. It is not a metabolic enzyme with a small-molecule substrate: the only bond it helps cleave is the γ-phosphate bond of GTP bound to SAR1.

SEC23A is also a scaffold. It forms an obligate heterodimer with one of four SEC24 cargo-adaptor paralogs, and the membrane-bound SAR1·GTP–SEC23–SEC24 "pre-budding complex" forms the inner layer of the COPII coat [bi-2002-prebudding-complex-abstract; peotter-2019-copii-review-fulltext]. Within this coat SEC23A has several jobs. It binds activated SAR1 and so anchors the inner coat to the membrane. It recruits the outer coat, SEC13–SEC31, whose disordered proline-rich region in turn speeds up SEC23's GAP activity [bi-2007-sec31-gap-abstract; antonny-2001-copii-dynamics-abstract; stancheva-2020-copii-multivalent-abstract]. It docks the procollagen-export receptor TANGO1/cTAGE5 and the exit-site organiser SEC16 [saito-2009-tango1-abstract; ma-2016-tango1-sec23-abstract; bhattacharyya-2007-sec16-homologues-abstract]. After budding, it stays on the carrier and serves as the binding site for the dynactin motor adaptor, the TRAPP tethering complex and the kinase CK1δ, which together move the carrier and give ER-to-Golgi traffic its direction [watson-2005-copii-dynactin-abstract; cai-2007-trapp-sec23-abstract; lord-2011-trapp-hrr25-sec23-fulltext].

SEC23A acts on the cytosolic face of the endoplasmic reticulum (ER), at ER exit sites (the transitional ER) and on the COPII-coated vesicles and tubules that bud from them, and a soluble pool sits in the cytosol [paccaud-1996-human-sec23-abstract]. In vertebrates, loss of SEC23A mainly impairs secretion of collagens and other extracellular-matrix proteins. Examples are the zebrafish *crusher* mutant, cranio-lenticulo-sutural dysplasia (CLSD) in humans, and mid-gestation lethality with collagen secretion failure in mice [lang-2006-crusher-sec23a-abstract; boyadjiev-2006-clsd-sec23a-abstract; zhu-2015-sec23a-mouse-abstract].

## 2. Identity, Domain Architecture and Evolutionary Conservation of the Donkey Protein

UniProt holds A0A9L0IQB9 as an unreviewed TrEMBL entry with protein-existence level 3 (inferred from homology). Its function, subcellular-location and GO annotations are all electronic, propagated by the SEC23 family rule RU365030 and by InterPro and TreeGrafter [uniprot-A0A9L0IQB9-entry]. The predicted domains follow the standard Sec23/Sec24 order: an N-terminal Sec23/Sec24-type zinc finger (residues 58–98), a trunk domain with a von Willebrand factor A-like fold (126–390), a β-sandwich domain (401–504), an α-helical domain (553–590) and a C-terminal gelsolin-like domain (606–692).

These match the InterPro signatures named in the request: IPR007123, IPR036180 and IPR029006 (gelsolin-like), IPR012990 (β-sandwich) and IPR037364 (Sec23) [uniprot-A0A9L0IQB9-entry].

To test orthology directly, the donkey sequence was aligned for this report against human SEC23A (Q15436), human SEC23B (Q15437) and *Saccharomyces cerevisiae* Sec23p (P15303). The alignment was a global BLOSUM62 alignment in Biopython, and the sequences are stored in `citations/sequences-donkey-human-SEC23AB.fasta`. The donkey protein shares 734 of 765 residues with human SEC23A (95.9% identity), 632 of 767 with human SEC23B (82.4%) and 367 of 768 with yeast Sec23p (47.8%).

This places A0A9L0IQB9 in the SEC23A orthology group rather than with SEC23B. The figures match the 85% identity between the two human paralogs, and the 48% identity of each to yeast Sec23p, reported when the human genes were cloned [paccaud-1996-human-sec23-abstract].

Residues 1–553 of the donkey protein align without gaps to human SEC23A. Within this region the four zinc-coordinating cysteines (C61, C66, C85 and C88), whose roles are seen in human SEC23A crystal structures, are conserved [uniprot-Q15436-human-SEC23A-entry]. So are phenylalanine 382, whose substitution by leucine causes recessive CLSD [boyadjiev-2006-clsd-sec23a-abstract], and S207, S312 and T405, which the autophagy kinase ULK1 phosphorylates in human cells [gan-2017-ulk1-sec23a-abstract].

After human residue 553 the donkey protein lacks 26 residues (human 554–579, CQKFGEYHKDDPSSFRFSETFSLYPQ) inside the helical domain, so its later residues are numbered 26 lower than the human ones. Allowing for that offset, the conservation continues. Human M702, site of the M702V CLSD variant, corresponds to donkey M676. The four TANGO1-binding residues of the human gelsolin-like domain (F628, Y672, Y678 and F681) correspond to donkey F602, Y646, Y652 and F655. Human R716, which aligns with the yeast Sec23p arginine finger R722, corresponds to donkey R690.

The TANGO1-binding residues are those whose mutation weakens binding to TANGO1 (MIA3) [uniprot-Q15436-human-SEC23A-entry; ma-2016-tango1-sec23-abstract]. The arginine finger is the residue that inserts into the SAR1 active site in the yeast crystal structure [bi-2002-prebudding-complex-abstract]. These residue correspondences come from the alignment in this report, not from experiments on the donkey protein.

The equivalent human arginine is now clinically relevant. In 2026 a de novo heterozygous SEC23A p.Arg716Cys variant was reported in a girl with short stature, developmental delay and spondyloepiphyseal-type skeletal dysplasia. The authors placed it within the autosomal-dominant CLSD spectrum and raised a dominant-negative effect on Sec23 multimers as one possible mechanism [yagasaki-2026-sec23a-r716c-fulltext]. That report contains no biochemical assay, so whether R716C removes GAP activity is untested. Its position at the catalytic arginine makes this a clear hypothesis (see Open Questions).

UniProt also contains donkey SEC23A predictions of 765 and 771 residues (A0A9L0JMP6 and A0A8C4LKL1). A0A9L0IQB9 is therefore probably an alternative splice model that skips an exon in the helical domain, not the main protein product. Whether that isoform is made in donkey tissues has not been tested [uniprot-A0A9L0IQB9-summary].

## 3. Molecular Function: SEC23A as the GTPase-Activating Protein for SAR1

The first defined biochemical activity of Sec23 was as a GAP. Yoshihisa, Barlowe and Schekman showed that yeast Sec23p, alone or within the Sec23p complex, increases GTP hydrolysis by Sar1p 10- to 15-fold. It has no effect on the Golgi-associated GTPases Ypt1p and ARF. Sec23p purified from two temperature-sensitive *sec23* strains had heat-sensitive GAP activity, which ties the activity to vesicle budding in vivo. Because Sec23p resembles no known GAP in sequence, the authors proposed it as a new GAP class [yoshihisa-1993-sar1-gap-abstract].

Reconstitution showed that Sar1p, the Sec23p complex and the Sec13p complex are enough to make 60–65 nm ER-derived vesicles with a 10-nm coat, which was named COPII. Budding also worked with the non-hydrolysable analogue GMP-PNP, but those vesicles kept their coat and could not fuse with the Golgi. GTP hydrolysis, triggered by Sec23, is therefore needed to release the coat and make vesicles fusion-competent, not to form the bud [barlowe-1994-copii-abstract].

The crystal structure of the yeast Sec23/24–Sar1·GppNHp complex showed how Sec23 does this. Sec23 and Sar1 form one continuous surface, and Sec23 inserts an arginine side chain into the Sar1 nucleotide-binding pocket [bi-2002-prebudding-complex-abstract]. As reviewed later, Sec23's helical domain recognises Sar1 switch I and the GTP-bound state, its trunk domain contacts switch II, and its gelsolin-like domain supplies the catalytic arginine *in trans* [peotter-2019-copii-review-fulltext].

The outer coat adjusts this activity. In a real-time liposome assay, Sec23/24 and Sec13/31 bound Sar1·GTP-loaded membranes within about one second. Sec13/31 then raised Sec23/24 GAP activity roughly ten-fold, so a complete cycle of assembly and disassembly lasted only seconds. Experiments with the phosphate analogue BeFx suggested that Sec23/24 supplies residues that take part directly in hydrolysis [antonny-2001-copii-dynamics-abstract]. Bi and colleagues traced the boost to a 40-residue Sec31 "active fragment". It lies across a combined Sec23–Sar1 surface and adds residues that meet those of Sec23 at the Sar1 active site [bi-2007-sec31-gap-abstract]. Later cryo-electron tomography of the complete coat confirmed this contact, mediated by conserved tryptophan–asparagine (WN) residues of Sec31 [hutchings-2021-complete-copii-coat-fulltext].

The reaction SEC23A drives is therefore GTP + H₂O → GDP + Pi on SAR1 (SAR1A or SAR1B in mammals). SEC23A is the activating protein and SAR1 is the enzyme. The F382L CLSD mutant behaves differently depending on which SAR1 paralog is present, indicating that SAR1A and SAR1B are not interchangeable partners in the SEC23A-driven cycle [yoshihisa-1993-sar1-gap-abstract; fromme-2007-clsd-coat-assembly-abstract].

## 4. Structural Role in the COPII Coat, Cargo Selection and Carrier Morphogenesis

Besides its catalytic role, SEC23A is a structural component of the coat. The Sec23/24 heterodimer forms a 15-nm bow-tie whose membrane-facing surface is concave and positively charged, which suits the curvature and acidic phospholipid content of COPII membranes [bi-2002-prebudding-complex-abstract].

Cargo is selected mainly by the SEC24 partner, which has several independent cargo-binding sites [miller-2003-sec24-cargo-abstract]. The four human SEC24 paralogs read different sorting signals (IxM, LxxLE and DxE) [mancias-2008-cargo-discrimination-abstract]. Because mammalian SEC23 paralogs pair with any of the four SEC24s [peotter-2019-copii-review-fulltext], SEC23A takes part in exporting the full range of SEC24-selected cargo. The SEC23 subunit can also help recognise cargo directly. The ER–Golgi SNARE Sec22 is read as a folded "conformational epitope" that binds at the Sec23/24 interface. Only unassembled Sec22 exposes this epitope, so the coat packages free SNAREs and not SNARE complexes [mancias-2007-sec22-signal-abstract]. Cargo-specific adaptors can also bind SEC23/SEC24. For example, the ER membrane protein TMEM39A binds both the phosphoinositide phosphatase SAC1 and SEC23/SEC24 to speed SAC1 export, which in turn controls PI4P distribution and autophagy [miao-2020-tmem39a-autophagy-abstract].

SEC23 is the main docking platform for the outer coat. The SEC31 proline-rich region binds a SEC23 surface spanning the gelsolin-like, trunk and β-barrel domains and extends over SAR1 switch II [peotter-2019-copii-review-fulltext]. Biochemistry and cryo-electron tomography show this contact is built from several distinct, mutually reinforcing interfaces: the GAP-accelerating active fragment at the SAR1–SEC23 junction, triple-proline (PPP) motifs bound to the tip of the SEC23 gelsolin-like domain, and a charge-based interaction whose structure is not yet known.

Because the binding is spread across these multiple weak interfaces, coat assembly can be cooperative yet reversible [stancheva-2020-copii-multivalent-abstract; hutchings-2021-complete-copii-coat-fulltext].

At 4.9 Å resolution, subtomogram averaging of membrane-bound inner coat shows SAR1–SEC23–SEC24 arranged in an ordered lattice. SEC13–SEC31 bridges neighbouring inner-coat units, and the lattice drives parallel insertion of SAR1 amphipathic helices, producing tubular curvature [hutchings-2018-copii-subtomogram-abstract]. Lateral packing in the inner coat depends mostly on homotypic SEC23–SEC23 contacts [peotter-2019-copii-review-fulltext], and a flexible SEC23 loop becomes ordered at these lattice interfaces [hutchings-2021-complete-copii-coat-fulltext]. Structure-guided mutagenesis of the complete coat showed that the inner coat alone can remodel membranes, with organising input from the outer coat. This challenges the older view that membrane curvature comes mainly from the outer cage [hutchings-2021-complete-copii-coat-abstract].

The CLSD substitution F382L shows how these steps are linked in cells. The mutant protein recruits SEC13–SEC31 poorly and fails to support vesicle formation in vitro. Patient fibroblasts accumulate uncoated, cargo-filled tubules at ER exit sites. This indicates that the SAR1–SEC23–SEC24 pre-budding complex can form tubules, while the outer coat is needed for fission [fromme-2007-clsd-coat-assembly-abstract]. Structurally, F382 corresponds to yeast Sec23 Phe380, which lines the groove that holds the Sec31 active fragment [bi-2007-sec31-gap-abstract].

**Large cargo: procollagen and TANGO1.** Procollagens are too large for standard 60–90 nm vesicles. TANGO1 (MIA3) is an exit-site transmembrane protein whose luminal SH3 domain binds collagen VII and whose cytoplasmic proline-rich domain binds SEC23/24. TANGO1 itself does not enter the carrier [saito-2009-tango1-abstract]. SEC23 recognises short PPP motifs that repeat along the proline-rich domains of TANGO1 and cTAGE5, so a single receptor can gather many inner-coat units into a close-packed array. Because SEC31 PPP motifs compete for the same SEC23 site, coat growth is expected to push TANGO1 back to the base of an expanding tubule [ma-2016-tango1-sec23-abstract]. Human SEC23A gelsolin-domain mutations (F628A/F681A and Y672K/Y678A) weaken TANGO1 binding, and all four residues are conserved in the donkey protein [uniprot-Q15436-human-SEC23A-entry]. Regulators such as SEC16 and TANGO1 compete with SEC31 for the inner coat, which offers one way to adjust coat lifetime to cargo size [stancheva-2020-copii-multivalent-fulltext].

The second CLSD allele, M702V, lies at the SEC31 interface. It does not disrupt general COPII budding, vesicle size or packaging of standard cargo, but it traps procollagen in the ER. In the presence of SEC13–SEC31, M702V SEC23A stimulates SAR1B GTPase activity more than wild-type SEC23A does, so the coat leaves the membrane too early. This supports the idea that procollagen needs the coat to stay on the membrane longer than small cargo do [kim-2012-sec23-sec31-procollagen-abstract; boyadjiev-2011-clsd-collagen-abstract].

## 5. Subcellular Localization

SEC23A is a peripheral membrane protein on the cytoplasmic face of the ER and of COPII carriers. Immuno-electron microscopy placed human SEC23A on the ribosome-free transitional ER (ER exit sites) and associated vesicles, and gel filtration placed the cytosolic pool in a complex of about 350 kDa, consistent with the SEC23/24 heterodimer [paccaud-1996-human-sec23-abstract]. SEC23A is recruited to membranes by SAR1·GTP, which the ER-resident exchange factor SEC12 activates at exit sites [peotter-2019-copii-review-fulltext].

Several proteins focus SEC23A at exit sites. The large mammalian Sec16 homologue (SEC16A, originally "Sec16L") localises to the transitional ER. Like yeast Sec16, it has a conserved C-terminal domain that binds Sec23, and it is needed for ER export and for normal exit-site organisation [bhattacharyya-2007-sec16-homologues-abstract]. The SEC23-interacting protein p125A/SEC23IP binds SEC23A and, through a separate domain, the C-terminus of SEC31A. Most cytosolic p125A exists in a preassembled complex with SEC13–SEC31A, so it physically links the inner and outer coats [ong-2010-p125a-sec13-sec31-abstract]. Its O-GlcNAc modification changes during transport and is needed to recruit SEC31A to exit sites [hirata-2026-sec23ip-oglcnac-abstract]. SEC23IP also recruits the lipid-transfer protein VPS13B to the junction between exit sites and the Golgi, where it supports tubular ERGIC carriers and timely procollagen export [du-2024-sec23ip-vps13b-abstract].

SEC23 also stays with carriers after budding. In live mammalian cells most exit sites, marked by YFP–SEC23A, lie close to microtubules. Sec23 binds the cargo-binding C-terminal domain of the dynactin subunit p150Glued directly, which links ER export to microtubule-based movement towards the Golgi [watson-2005-copii-dynactin-fulltext]. In a yeast transport assay, ER-derived vesicles kept their coat until they reached the Golgi [lord-2011-trapp-hrr25-sec23-fulltext]. Part of the SEC23 pool therefore acts at the ER–Golgi interface: in mammals, the ER-Golgi intermediate compartment (ERGIC) and the cis-Golgi.

For the donkey protein, UniProt's rule-based annotations (COPII vesicle membrane, ER membrane, cytosol; GO terms "COPII vesicle coat" and "endoplasmic reticulum exit site") agree with this experimentally supported picture from human cells [uniprot-A0A9L0IQB9-entry; uniprot-Q15436-human-SEC23A-entry].

## 6. Partners and Regulation: Tethering, Phosphorylation and Transcriptional Control

**Tethering and direction of traffic.** SEC23 binds a series of partners over the life of a carrier. After budding, the TRAPP I tethering complex binds Sec23 through its Bet3 subunit in both yeast and mammalian cells. This targets TRAPP to COPII vesicles so they can tether to each other or to the Golgi [cai-2007-trapp-sec23-abstract]. Next, the Golgi-associated kinase Hrr25p (orthologous to mammalian CK1δ) phosphorylates the Sec23/Sec24 complex. Phosphorylation is needed for fusion, and removal of the phosphate is needed for new rounds of budding. This ordered series of contacts (SAR1, then TRAPP, then the kinase) gives ER-to-Golgi traffic its direction and prevents carriers from fusing back with the ER. The authors report that the sequence is conserved in mammalian cells [lord-2011-trapp-hrr25-sec23-fulltext].

**Phosphorylation by ULK1.** When autophagy is induced, ULK1 phosphorylates human SEC23A at S207, S312 and T405; S207 most closely reproduces the effects of ULK1. Phosphorylation weakens the SEC23A–SEC31A interaction, causes exit sites to clump and slows ER-to-Golgi transport, which links nutrient stress to secretory output [gan-2017-ulk1-sec23a-abstract; gan-2017-ulk1-sec23a-fulltext]. All three sites are conserved in the donkey protein. A 2026 review summarises a wider set of COPII modifications (phosphorylation, O-GlcNAcylation and ubiquitination) that reshape exit sites in response to physiological signals [hirata-2026-eres-ptm-review-abstract].

**Transcriptional control by BBF2H7/CREB3L2.** *Sec23a* is a direct target of BBF2H7 (CREB3L2), an ER-stress-activated bZIP transcription factor that binds a CRE-like element in the *Sec23a* promoter. *Bbf2h7*⁻/⁻ mice develop severe chondrodysplasia, with type II collagen and COMP trapped in expanded ER. Restoring Sec23a in mutant chondrocytes fully restores matrix secretion [saito-2009-bbf2h7-sec23a-abstract]. In dermal fibroblasts, IGF-I induces BBF2H7 and SEC23A, and this pathway is needed for procollagen to move from the ER to the Golgi [ishikura-2012-bbf2h7-sec23a-abstract]. Cells therefore raise SEC23A levels when they need more secretory capacity.

**Post-transcriptional control (cancer models).** In breast-cancer models, miR-200 microRNAs were reported to target *Sec23a* mRNA directly. This lowered secretion of metastasis-suppressing proteins such as IGFBP4 and TINAGL1 and favoured metastatic colonisation [korpal-2011-mir200-sec23a-abstract]. An Editorial Expression of Concern was issued for that article in 2026 [korpal-2026-expression-of-concern-abstract], so these findings should be treated with caution. A separate melanoma study proposed that SEC23A-dependent secretion of S100A8 activates autophagy and restrains metastatic colonisation [sun-2020-s100a8-sec23a-abstract]. These cell-line studies are correlative and peripheral to SEC23A's core function. They are mentioned only because they show that SEC23A levels can limit how much of particular proteins a cell secretes.

## 7. Physiological Roles, Paralog Relationships and Disease

Loss of SEC23A in vertebrates consistently impairs secretion of collagen-rich extracellular matrix. In zebrafish, the *crusher* mutant carries a *sec23a* nonsense allele (L402X). Its chondrocytes accumulate type II collagen and other matrix proteins in distended ER, causing craniofacial cartilage malformation, kinked pectoral fins and short body length. *sec23b* is also needed in chondrocytes, while knocking down COPI does not produce this phenotype [lang-2006-crusher-sec23a-abstract].

In humans, homozygous SEC23A F382L causes autosomal-recessive CLSD: late-closing fontanels, sutural cataracts, facial dysmorphism and skeletal defects. Patient fibroblasts show dilated ER and mislocalised SEC31, and morpholino knockdown of *sec23a* in zebrafish produces a similar phenotype [boyadjiev-2006-clsd-sec23a-abstract]. A second family carries a heterozygous M702V allele, with severe collagen-secretion defects and probably an additional genetic contributor [boyadjiev-2011-clsd-collagen-abstract]. The recently reported de novo R716C variant extends the SEC23A disorders to dominant presentations [yagasaki-2026-sec23a-r716c-fulltext].

In mice, *Sec23a*-null embryos die in mid-gestation, with an open neural tube in the midbrain and defective extraembryonic membranes. Several collagen types fail to be secreted while fibronectin is unaffected, and the unfolded protein response is strongly induced in collagen-producing cells. SEC23B-deficient embryos show no collagen defect [zhu-2015-sec23a-mouse-abstract].

A 2026 review groups SEC23A with SEC16B and SEC24D as COPII genes whose mutation causes skeletal disease through defective collagen secretion [hirata-2026-eres-ptm-review-fulltext]. A broader review frames such disorders as diseases of reduced secretion arising at exit sites [robinson-2024-er-exit-review-abstract].

The two vertebrate SEC23 paralogs are linked to different diseases. SEC23B mutations cause congenital dyserythropoietic anaemia type II [schwarz-2009-sec23b-cda2-abstract], whereas SEC23A mutations mainly affect the skeleton. This first suggested that the two proteins have different functions. Khoriaty and colleagues tested this directly. They found that human SEC23A and SEC23B have indistinguishable intracellular interactomes and that both human and mouse paralogs complement yeast *sec23*. A *sec23a* transgene rescued *sec23b*-deficient zebrafish, and *Sec23a* coding sequence placed into the mouse *Sec23b* locus fully rescued the lethal pancreatic phenotype of SEC23B deficiency. They concluded that the two proteins are biochemically equivalent and that the different phenotypes reflect where each gene is expressed [khoriaty-2018-sec23-paralogs-abstract]. The mouse knockout data partly qualify this. Each paralog is upregulated when the other is lost, and reducing the remaining copy makes embryonic death earlier, which the authors interpret as overlapping but distinct cargo spectra in vivo [zhu-2015-sec23a-mouse-abstract]. A reconciling view is that SEC23A dominates in collagen-secreting cells because of its expression level, not because of any unique biochemical activity.

**Implications for the donkey.** No phenotypic data exist for donkey SEC23A. Its near-identity to human SEC23A predicts the same role in exporting collagen and other secretory cargo from the ER in connective tissue, cartilage and bone. This is an inference, not an observation.

## 8. Open Questions

The central gap is that no experiment has examined SEC23A in *Equus asinus* or any other equid. Every functional statement in this report is transferred from human, rodent, zebrafish and yeast orthologs. The transfer is strongly supported by sequence conservation, but it remains an inference.

**The 26-residue isoform.** The most immediate follow-up is to find out whether the A0A9L0IQB9 transcript is expressed at all. Donkey RNA-seq data, such as the resources produced by the donkey genome project [wang-2020-donkey-genomes-abstract], could show whether this exon-skipping model is real, in which tissues it appears, and whether it is a genuine splice isoform or a gene-model artefact. If the isoform exists, its activity is unknown. The missing segment lies in the helical domain, which recognises SAR1 switch I [peotter-2019-copii-review-fulltext]. Testing its SAR1 binding, GAP activity and SEC31 recruitment in vitro would show whether the deletion matters functionally. The same question applies to the corresponding human and horse isoforms.

**Molecular mechanism.** Biochemical study of the R716C variant would test whether loss of the arginine finger explains dominant CLSD, for example through a GAP-dead SEC23A that stalls coats or blocks uncoating [yagasaki-2026-sec23a-r716c-fulltext; bi-2002-prebudding-complex-abstract]. The GAP stimulation SEC23A provides towards SAR1A versus SAR1B, and how SEC31, SEC16, TANGO1 and SEC23IP tune it, still needs quantitative measurement [fromme-2007-clsd-coat-assembly-abstract; kim-2012-sec23-sec31-procollagen-abstract; stancheva-2020-copii-multivalent-abstract]. The structure of the charge-based SEC31–SEC23 interface is unresolved [hutchings-2021-complete-copii-coat-fulltext]. How phosphorylation by ULK1 and CK1δ, together with other modifications, sets coat lifetime in mammalian cells has not been fully mapped [gan-2017-ulk1-sec23a-abstract; lord-2011-trapp-hrr25-sec23-fulltext; hirata-2026-eres-ptm-review-abstract].

**Paralog roles.** It is still unresolved whether SEC23A and SEC23B are fully interchangeable or prefer certain cargo in particular cell types [khoriaty-2018-sec23-paralogs-abstract; zhu-2015-sec23a-mouse-abstract]. Measuring how much of each paralog equid tissues make would help predict which tissues depend most on SEC23A.

**Equine relevance.** Equine skeletal and connective-tissue disorders involving collagen secretion are a natural setting for candidate-gene studies of *SEC23A*. No SEC23A variant has been linked to an equid phenotype in the literature examined here. Finally, the miR-200–SEC23A findings in cancer need independent confirmation, given the 2026 expression of concern [korpal-2026-expression-of-concern-abstract].

## 9. References

* **antonny-2001-copii-dynamics**: Antonny B, Madden D, Hamamoto S, Orci L, Schekman R. (2001). Dynamics of the COPII coat with GTP and stable analogues. *Nature cell biology* 3:531-537. PMID: 11389436; DOI: [10.1038/35078500](https://doi.org/10.1038/35078500)
* **barlowe-1994-copii**: Barlowe C, Orci L, Yeung T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman R. (1994). COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. *Cell* 77:895-907. PMID: 8004676; DOI: [10.1016/0092-8674(94)90138-4](https://doi.org/10.1016/0092-8674(94)90138-4)
* **bhattacharyya-2007-sec16-homologues**: Bhattacharyya D, Glick BS. (2007). Two mammalian Sec16 homologues have nonredundant functions in endoplasmic reticulum (ER) export and transitional ER organization. *Molecular biology of the cell* 18:839-849. PMID: 17192411; DOI: [10.1091/mbc.e06-08-0707](https://doi.org/10.1091/mbc.e06-08-0707)
* **bi-2002-prebudding-complex**: Bi X, Corpina RA, Goldberg J. (2002). Structure of the Sec23/24-Sar1 pre-budding complex of the COPII vesicle coat. *Nature* 419:271-277. PMID: 12239560; DOI: [10.1038/nature01040](https://doi.org/10.1038/nature01040)
* **bi-2007-sec31-gap**: Bi X, Mancias JD, Goldberg J. (2007). Insights into COPII coat nucleation from the structure of Sec23.Sar1 complexed with the active fragment of Sec31. *Developmental cell* 13:635-645. PMID: 17981133; PMCID: PMC2686382; DOI: [10.1016/j.devcel.2007.10.006](https://doi.org/10.1016/j.devcel.2007.10.006)
* **boyadjiev-2006-clsd-sec23a**: Boyadjiev SA, Fromme JC, Ben J, Chong SS, Nauta C, Hur DJ, Zhang G, Hamamoto S, Schekman R, Ravazzola M, Orci L, Eyaid W. (2006). Cranio-lenticulo-sutural dysplasia is caused by a SEC23A mutation leading to abnormal endoplasmic-reticulum-to-Golgi trafficking. *Nature genetics* 38:1192-1197. PMID: 16980979; DOI: [10.1038/ng1876](https://doi.org/10.1038/ng1876)
* **boyadjiev-2011-clsd-collagen**: Boyadjiev SA, Kim SD, Hata A, Haldeman-Englert C, Zackai EH, Naydenov C, Hamamoto S, Schekman RW, Kim J. (2011). Cranio-lenticulo-sutural dysplasia associated with defects in collagen secretion. *Clinical genetics* 80:169-176. PMID: 21039434; PMCID: PMC4143380; DOI: [10.1111/j.1399-0004.2010.01550.x](https://doi.org/10.1111/j.1399-0004.2010.01550.x)
* **cai-2007-trapp-sec23**: Cai H, Yu S, Menon S, Cai Y, Lazarova D, Fu C, Reinisch K, Hay JC, Ferro-Novick S. (2007). TRAPPI tethers COPII vesicles by binding the coat subunit Sec23. *Nature* 445:941-944. PMID: 17287728; DOI: [10.1038/nature05527](https://doi.org/10.1038/nature05527)
* **du-2024-sec23ip-vps13b**: Du Y, Fan X, Song C, Chang W, Xiong J, Deng L, Ji WK. (2024). Sec23IP recruits VPS13B/COH1 to ER exit site-Golgi interface for tubular ERGIC formation. *The Journal of cell biology* 223:e202402083. PMID: 39352497; PMCID: PMC11457499; DOI: [10.1083/jcb.202402083](https://doi.org/10.1083/jcb.202402083)
* **fromme-2007-clsd-coat-assembly**: Fromme JC, Ravazzola M, Hamamoto S, Al-Balwi M, Eyaid W, Boyadjiev SA, Cosson P, Schekman R, Orci L. (2007). The genetic basis of a craniofacial disease provides insight into COPII coat assembly. *Developmental cell* 13:623-634. PMID: 17981132; PMCID: PMC2262049; DOI: [10.1016/j.devcel.2007.10.005](https://doi.org/10.1016/j.devcel.2007.10.005)
* **gan-2017-ulk1-sec23a**: Gan W, Zhang C, Siu KY, Satoh A, Tanner JA, Yu S. (2017). ULK1 phosphorylates Sec23A and mediates autophagy-induced inhibition of ER-to-Golgi traffic. *BMC cell biology* 18:22. PMID: 28486929; PMCID: PMC5424413; DOI: [10.1186/s12860-017-0138-8](https://doi.org/10.1186/s12860-017-0138-8)
* **hirata-2026-eres-ptm-review**: Hirata T, Boyce M. (2026). Remaking an exit: dynamic regulation of ER exit sites by post-translational modifications. *Trends in cell biology* 36:861-872. PMID: 42660790; PMCID: PMC13544067; DOI: [10.1016/j.tcb.2026.08.003](https://doi.org/10.1016/j.tcb.2026.08.003)
* **hirata-2026-sec23ip-oglcnac**: Hirata T, Nguyen Q, Liu C, Boyce M. (2026). Dynamic O-GlcNAcylation of Sec23-interacting protein regulates COPII function. *The Journal of biological chemistry* 302:113356. PMID: 42486260; PMCID: PMC13499130; DOI: [10.1016/j.jbc.2026.113356](https://doi.org/10.1016/j.jbc.2026.113356)
* **hutchings-2018-copii-subtomogram**: Hutchings J, Stancheva V, Miller EA, Zanetti G. (2018). Subtomogram averaging of COPII assemblies reveals how coat organization dictates membrane shape. *Nature communications* 9:4154. PMID: 30297805; PMCID: PMC6175875; DOI: [10.1038/s41467-018-06577-4](https://doi.org/10.1038/s41467-018-06577-4)
* **hutchings-2021-complete-copii-coat**: Hutchings J, Stancheva VG, Brown NR, Cheung ACM, Miller EA, Zanetti G. (2021). Structure of the complete, membrane-assembled COPII coat reveals a complex interaction network. *Nature communications* 12:2034. PMID: 33795673; PMCID: PMC8016994; DOI: [10.1038/s41467-021-22110-6](https://doi.org/10.1038/s41467-021-22110-6)
* **ishikura-2012-bbf2h7-sec23a**: Ishikura-Kinoshita S, Saeki H, Tsuji-Naito K. (2012). BBF2H7-mediated Sec23A pathway is required for endoplasmic reticulum-to-Golgi trafficking in dermal fibroblasts to promote collagen synthesis. *The Journal of investigative dermatology* 132:2010-2018. PMID: 22495181; DOI: [10.1038/jid.2012.103](https://doi.org/10.1038/jid.2012.103)
* **khoriaty-2018-sec23-paralogs**: Khoriaty R, Hesketh GG, Bernard A, Weyand AC, Mellacheruvu D, Zhu G, Hoenerhoff MJ, McGee B, Everett L, Adams EJ, Zhang B, Saunders TL, Nesvizhskii AI, Klionsky DJ, Shavit JA, Gingras AC, Ginsburg D. (2018). Functions of the COPII gene paralogs SEC23A and SEC23B are interchangeable in vivo. *Proceedings of the National Academy of Sciences of the United States of America* 115:E7748-E7757. PMID: 30065114; PMCID: PMC6099849; DOI: [10.1073/pnas.1805784115](https://doi.org/10.1073/pnas.1805784115)
* **kim-2012-sec23-sec31-procollagen**: Kim SD, Pahuja KB, Ravazzola M, Yoon J, Boyadjiev SA, Hammamoto S, Schekman R, Orci L, Kim J. (2012). The [corrected] SEC23-SEC31 [corrected] interface plays critical role for export of procollagen from the endoplasmic reticulum. *The Journal of biological chemistry* 287:10134-10144. PMID: 22298774; PMCID: PMC3323018; DOI: [10.1074/jbc.m111.283382](https://doi.org/10.1074/jbc.m111.283382)
* **korpal-2011-mir200-sec23a**: Korpal M, Ell BJ, Buffa FM, Ibrahim T, Blanco MA, Celià-Terrassa T, Mercatali L, Khan Z, Goodarzi H, Hua Y, Wei Y, Hu G, Garcia BA, Ragoussis J, Amadori D, Harris AL, Kang Y. (2011). Direct targeting of Sec23a by miR-200s influences cancer cell secretome and promotes metastatic colonization. *Nature medicine* 17:1101-1108. PMID: 21822286; PMCID: PMC3169707; DOI: [10.1038/nm.2401](https://doi.org/10.1038/nm.2401)
* **korpal-2026-expression-of-concern**: Korpal M, Ell BJ, Buffa FM, Ibrahim T, Blanco MA, Celià-Terrassa T, Mercatali L, Khan Z, Goodarzi H, Hua Y, Wei Y, Hu G, Garcia BA, Ragoussis J, Amadori D, Harris AL, Kang Y. (2026). Editorial Expression of Concern: Direct targeting of Sec23a by miR-200s influences cancer cell secretome and promotes metastatic colonization. *Nature medicine* 32:768. PMID: 41639381; DOI: [10.1038/s41591-026-04242-8](https://doi.org/10.1038/s41591-026-04242-8)
* **lang-2006-crusher-sec23a**: Lang MR, Lapierre LA, Frotscher M, Goldenring JR, Knapik EW. (2006). Secretory COPII coat component Sec23a is essential for craniofacial chondrocyte maturation. *Nature genetics* 38:1198-1203. PMID: 16980978; DOI: [10.1038/ng1880](https://doi.org/10.1038/ng1880)
* **lord-2011-trapp-hrr25-sec23**: Lord C, Bhandari D, Menon S, Ghassemian M, Nycz D, Hay J, Ghosh P, Ferro-Novick S. (2011). Sequential interactions with Sec23 control the direction of vesicle traffic. *Nature* 473:181-186. PMID: 21532587; PMCID: PMC3093450; DOI: [10.1038/nature09969](https://doi.org/10.1038/nature09969)
* **ma-2016-tango1-sec23**: Ma W, Goldberg J. (2016). TANGO1/cTAGE5 receptor as a polyvalent template for assembly of large COPII coats. *Proceedings of the National Academy of Sciences of the United States of America* 113:10061-10066. PMID: 27551091; PMCID: PMC5018777; DOI: [10.1073/pnas.1605916113](https://doi.org/10.1073/pnas.1605916113)
* **mancias-2007-sec22-signal**: Mancias JD, Goldberg J. (2007). The transport signal on Sec22 for packaging into COPII-coated vesicles is a conformational epitope. *Molecular cell* 26:403-414. PMID: 17499046; DOI: [10.1016/j.molcel.2007.03.017](https://doi.org/10.1016/j.molcel.2007.03.017)
* **mancias-2008-cargo-discrimination**: Mancias JD, Goldberg J. (2008). Structural basis of cargo membrane protein discrimination by the human COPII coat machinery. *The EMBO journal* 27:2918-2928. PMID: 18843296; PMCID: PMC2580787; DOI: [10.1038/emboj.2008.208](https://doi.org/10.1038/emboj.2008.208)
* **miao-2020-tmem39a-autophagy**: Miao G, Zhang Y, Chen D, Zhang H. (2020). The ER-Localized Transmembrane Protein TMEM39A/SUSR2 Regulates Autophagy by Controlling the Trafficking of the PtdIns(4)P Phosphatase SAC1. *Molecular cell* 77:618-632.e5. PMID: 31806350; DOI: [10.1016/j.molcel.2019.10.035](https://doi.org/10.1016/j.molcel.2019.10.035)
* **miller-2003-sec24-cargo**: Miller EA, Beilharz TH, Malkus PN, Lee MC, Hamamoto S, Orci L, Schekman R. (2003). Multiple cargo binding sites on the COPII subunit Sec24p ensure capture of diverse membrane proteins into transport vesicles. *Cell* 114:497-509. PMID: 12941277; DOI: [10.1016/s0092-8674(03)00609-3](https://doi.org/10.1016/s0092-8674(03)00609-3)
* **ong-2010-p125a-sec13-sec31**: Ong YS, Tang BL, Loo LS, Hong W. (2010). p125A exists as part of the mammalian Sec13/Sec31 COPII subcomplex to facilitate ER-Golgi transport. *The Journal of cell biology* 190:331-345. PMID: 20679433; PMCID: PMC2922642; DOI: [10.1083/jcb.201003005](https://doi.org/10.1083/jcb.201003005)
* **paccaud-1996-human-sec23**: Paccaud JP, Reith W, Carpentier JL, Ravazzola M, Amherdt M, Schekman R, Orci L. (1996). Cloning and functional characterization of mammalian homologues of the COPII component Sec23. *Molecular biology of the cell* 7:1535-1546. PMID: 8898360; PMCID: PMC276004; DOI: [10.1091/mbc.7.10.1535](https://doi.org/10.1091/mbc.7.10.1535)
* **peotter-2019-copii-review**: Peotter J, Kasberg W, Pustova I, Audhya A. (2019). COPII-mediated trafficking at the ER/ERGIC interface. *Traffic (Copenhagen, Denmark)* 20:491-503. PMID: 31059169; PMCID: PMC6640837; DOI: [10.1111/tra.12654](https://doi.org/10.1111/tra.12654)
* **robinson-2024-er-exit-review**: Robinson CM, Duggan A, Forrester A. (2024). ER exit in physiology and disease. *Frontiers in molecular biosciences* 11:1352970. PMID: 38314136; PMCID: PMC10835805; DOI: [10.3389/fmolb.2024.1352970](https://doi.org/10.3389/fmolb.2024.1352970)
* **saito-2009-bbf2h7-sec23a**: Saito A, Hino S, Murakami T, Kanemoto S, Kondo S, Saitoh M, Nishimura R, Yoneda T, Furuichi T, Ikegawa S, Ikawa M, Okabe M, Imaizumi K. (2009). Regulation of endoplasmic reticulum stress response by a BBF2H7-mediated Sec23a pathway is essential for chondrogenesis. *Nature cell biology* 11:1197-1204. PMID: 19767744; DOI: [10.1038/ncb1962](https://doi.org/10.1038/ncb1962)
* **saito-2009-tango1**: Saito K, Chen M, Bard F, Chen S, Zhou H, Woodley D, Polischuk R, Schekman R, Malhotra V. (2009). TANGO1 facilitates cargo loading at endoplasmic reticulum exit sites. *Cell* 136:891-902. PMID: 19269366; DOI: [10.1016/j.cell.2008.12.025](https://doi.org/10.1016/j.cell.2008.12.025)
* **schwarz-2009-sec23b-cda2**: Schwarz K, Iolascon A, Verissimo F, Trede NS, Horsley W, Chen W, Paw BH, Hopfner KP, Holzmann K, Russo R, Esposito MR, Spano D, De Falco L, Heinrich K, Joggerst B, Rojewski MT, Perrotta S, Denecke J, Pannicke U, Delaunay J, Pepperkok R, Heimpel H. (2009). Mutations affecting the secretory COPII coat component SEC23B cause congenital dyserythropoietic anemia type II. *Nature genetics* 41:936-940. PMID: 19561605; DOI: [10.1038/ng.405](https://doi.org/10.1038/ng.405)
* **stancheva-2020-copii-multivalent**: Stancheva VG, Li XH, Hutchings J, Gomez-Navarro N, Santhanam B, Babu MM, Zanetti G, Miller EA. (2020). Combinatorial multivalent interactions drive cooperative assembly of the COPII coat. *The Journal of cell biology* 219:e202007135. PMID: 32997735; PMCID: PMC7594496; DOI: [10.1083/jcb.202007135](https://doi.org/10.1083/jcb.202007135)
* **sun-2020-s100a8-sec23a**: Sun Z, Zeng B, Liu D, Zhao Q, Wang J, Rosie Xing H. (2020). S100A8 transported by SEC23A inhibits metastatic colonization via autocrine activation of autophagy. *Cell death & disease* 11:650. PMID: 32811814; PMCID: PMC7435177; DOI: [10.1038/s41419-020-02835-w](https://doi.org/10.1038/s41419-020-02835-w)
* **wang-2020-donkey-genomes**: Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, Wang J, Fang X, Zhao Z, Wang S, Zhang Y, Liu Q, Jiang Q, Wang X, Guo Y, Yang C, Wang Y, Tian F, Zhuang G, Fan Y, Gao Q, Li Y, Ju Z, Li J, Li R, Hou M, Yang G, Liu G, Liu W, Guo J, Pan S, Fan G, Zhang W, Zhang R, Yu J, Zhang X, Yin Q, Ji C, Jin Y, Yue G, Liu M, Xu J, Liu S, Jordana J, Noce A, Amills M, Wu DD, Li S, Zhou X, Zhong J. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: [10.1038/s41467-020-19813-7](https://doi.org/10.1038/s41467-020-19813-7)
* **watson-2005-copii-dynactin**: Watson P, Forster R, Palmer KJ, Pepperkok R, Stephens DJ. (2005). Coupling of ER exit to microtubules through direct interaction of COPII with dynactin. *Nature cell biology* 7:48-55. PMID: 15580264; PMCID: PMC1592520; DOI: [10.1038/ncb1206](https://doi.org/10.1038/ncb1206)
* **yagasaki-2026-sec23a-r716c**: Yagasaki H, Narusawa H, Watanabe D, Nagata M, Yonei A, Asano Y, Aoyagi K, Inukai T. (2026). Skeletal dysplasia and growth disorder with &lt;i&gt;SEC23A&lt;/i&gt; p.Arg716Cys variant-related cranio-lenticulo-sutural dysplasia. *Clinical pediatric endocrinology : case reports and clinical investigations : official journal of the Japanese Society for Pediatric Endocrinology* 35:286-290. PMID: 42441357; PMCID: PMC13337293; DOI: [10.1297/cpe.2025-0109](https://doi.org/10.1297/cpe.2025-0109)
* **yoshihisa-1993-sar1-gap**: Yoshihisa T, Barlowe C, Schekman R. (1993). Requirement for a GTPase-activating protein in vesicle budding from the endoplasmic reticulum. *Science (New York, N.Y.)* 259:1466-1468. PMID: 8451644; DOI: [10.1126/science.8451644](https://doi.org/10.1126/science.8451644)
* **zhu-2015-sec23a-mouse**: Zhu M, Tao J, Vasievich MP, Wei W, Zhu G, Khoriaty RN, Zhang B. (2015). Neural tube opening and abnormal extraembryonic membrane development in SEC23A deficient mice. *Scientific reports* 5:15471. PMID: 26494538; PMCID: PMC4616029; DOI: [10.1038/srep15471](https://doi.org/10.1038/srep15471)
* **uniprot-A0A9L0IQB9**: UniProtKB/TrEMBL entry A0A9L0IQB9_EQUAS, Protein transport protein SEC23 (SEC23A), *Equus asinus*, entry version 13 (10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A9L0IQB9.txt (local copy: citations/uniprot-A0A9L0IQB9-entry.txt; researcher's alignment analysis: citations/uniprot-A0A9L0IQB9-summary.md)
* **uniprot-Q15436-human-SEC23A**: UniProtKB/Swiss-Prot entry Q15436 (SC23A_HUMAN), Protein transport protein Sec23A, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q15436.txt (local copy: citations/uniprot-Q15436-human-SEC23A-entry.txt)


## Citations

1. antonny-2001-copii-dynamics-abstract.md
2. antonny-2001-copii-dynamics-summary.md
3. barlowe-1994-copii-abstract.md
4. barlowe-1994-copii-summary.md
5. bhattacharyya-2007-sec16-homologues-abstract.md
6. bhattacharyya-2007-sec16-homologues-summary.md
7. bi-2002-prebudding-complex-abstract.md
8. bi-2002-prebudding-complex-summary.md
9. bi-2007-sec31-gap-abstract.md
10. bi-2007-sec31-gap-summary.md
11. boyadjiev-2006-clsd-sec23a-abstract.md
12. boyadjiev-2006-clsd-sec23a-summary.md
13. boyadjiev-2011-clsd-collagen-abstract.md
14. boyadjiev-2011-clsd-collagen-fulltext.txt
15. boyadjiev-2011-clsd-collagen-summary.md
16. cai-2007-trapp-sec23-abstract.md
17. cai-2007-trapp-sec23-summary.md
18. chen-2021-fam20c-s1p-abstract.md
19. chen-2021-fam20c-s1p-summary.md
20. du-2024-sec23ip-vps13b-abstract.md
21. du-2024-sec23ip-vps13b-fulltext.txt
22. du-2024-sec23ip-vps13b-summary.md
23. fromme-2007-clsd-coat-assembly-abstract.md
24. fromme-2007-clsd-coat-assembly-summary.md
25. gan-2017-ulk1-sec23a-abstract.md
26. gan-2017-ulk1-sec23a-fulltext.txt
27. gan-2017-ulk1-sec23a-summary.md
28. gomez-navarro-2016-cop-vesicles-abstract.md
29. gomez-navarro-2016-cop-vesicles-summary.md
30. hirata-2026-eres-ptm-review-abstract.md
31. hirata-2026-eres-ptm-review-fulltext.txt
32. hirata-2026-eres-ptm-review-summary.md
33. hirata-2026-sec23ip-oglcnac-abstract.md
34. hirata-2026-sec23ip-oglcnac-fulltext.txt
35. hirata-2026-sec23ip-oglcnac-summary.md
36. hutchings-2018-copii-subtomogram-abstract.md
37. hutchings-2018-copii-subtomogram-fulltext.txt
38. hutchings-2018-copii-subtomogram-summary.md
39. hutchings-2021-complete-copii-coat-abstract.md
40. hutchings-2021-complete-copii-coat-fulltext.txt
41. hutchings-2021-complete-copii-coat-summary.md
42. ishikura-2012-bbf2h7-sec23a-abstract.md
43. ishikura-2012-bbf2h7-sec23a-summary.md
44. khoriaty-2018-sec23-paralogs-abstract.md
45. khoriaty-2018-sec23-paralogs-summary.md
46. kim-2012-sec23-sec31-procollagen-abstract.md
47. kim-2012-sec23-sec31-procollagen-summary.md
48. korpal-2011-mir200-sec23a-abstract.md
49. korpal-2011-mir200-sec23a-fulltext.txt
50. korpal-2011-mir200-sec23a-summary.md
51. korpal-2026-expression-of-concern-abstract.md
52. korpal-2026-expression-of-concern-summary.md
53. lang-2006-crusher-sec23a-abstract.md
54. lang-2006-crusher-sec23a-summary.md
55. lord-2011-trapp-hrr25-sec23-abstract.md
56. lord-2011-trapp-hrr25-sec23-fulltext.txt
57. lord-2011-trapp-hrr25-sec23-summary.md
58. ma-2016-tango1-sec23-abstract.md
59. ma-2016-tango1-sec23-summary.md
60. mancias-2007-sec22-signal-abstract.md
61. mancias-2007-sec22-signal-summary.md
62. mancias-2008-cargo-discrimination-abstract.md
63. mancias-2008-cargo-discrimination-summary.md
64. metadata.json
65. miao-2020-tmem39a-autophagy-abstract.md
66. miao-2020-tmem39a-autophagy-summary.md
67. miller-2003-sec24-cargo-abstract.md
68. miller-2003-sec24-cargo-summary.md
69. ong-2010-p125a-sec13-sec31-abstract.md
70. ong-2010-p125a-sec13-sec31-fulltext.txt
71. ong-2010-p125a-sec13-sec31-summary.md
72. paccaud-1996-human-sec23-abstract.md
73. paccaud-1996-human-sec23-summary.md
74. peotter-2019-copii-review-abstract.md
75. peotter-2019-copii-review-fulltext.txt
76. peotter-2019-copii-review-summary.md
77. pmid-slug-list-round2.tsv
78. pmid-slug-list.tsv
79. references.md
80. robinson-2024-er-exit-review-abstract.md
81. robinson-2024-er-exit-review-fulltext.txt
82. robinson-2024-er-exit-review-summary.md
83. saito-2009-bbf2h7-sec23a-abstract.md
84. saito-2009-bbf2h7-sec23a-summary.md
85. saito-2009-tango1-abstract.md
86. saito-2009-tango1-summary.md
87. schwarz-2009-sec23b-cda2-abstract.md
88. schwarz-2009-sec23b-cda2-summary.md
89. sequences-donkey-human-SEC23AB.fasta
90. stancheva-2020-copii-multivalent-abstract.md
91. stancheva-2020-copii-multivalent-fulltext.txt
92. stancheva-2020-copii-multivalent-summary.md
93. sun-2020-s100a8-sec23a-abstract.md
94. sun-2020-s100a8-sec23a-fulltext.txt
95. sun-2020-s100a8-sec23a-summary.md
96. uniprot-A0A9L0IQB9-entry.txt
97. uniprot-A0A9L0IQB9-summary.md
98. uniprot-Q15436-human-SEC23A-entry.txt
99. wang-2020-donkey-genomes-abstract.md
100. wang-2020-donkey-genomes-summary.md
101. watson-2005-copii-dynactin-abstract.md
102. watson-2005-copii-dynactin-fulltext.txt
103. watson-2005-copii-dynactin-summary.md
104. yagasaki-2026-sec23a-r716c-abstract.md
105. yagasaki-2026-sec23a-r716c-fulltext.txt
106. yagasaki-2026-sec23a-r716c-summary.md
107. yoshihisa-1993-sar1-gap-abstract.md
108. yoshihisa-1993-sar1-gap-summary.md
109. zhu-2015-sec23a-mouse-abstract.md
110. zhu-2015-sec23a-mouse-fulltext.txt
111. zhu-2015-sec23a-mouse-summary.md
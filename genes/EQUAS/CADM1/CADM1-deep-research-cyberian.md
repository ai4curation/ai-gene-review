---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:16:25.580295'
end_time: '2026-10-25T23:28:23.765268'
duration_seconds: 718.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: CADM1
  gene_symbol: CADM1
  uniprot_accession: A0A9L0IX39
  protein_description: 'RecName: Full=Cell adhesion molecule 1 {ECO:0000256|ARBA:ARBA00068781};
    AltName: Full=Synaptic cell adhesion molecule {ECO:0000256|ARBA:ARBA00080773};'
  gene_info: Name=CADM1 {ECO:0000313|Ensembl:ENSEASP00005045449.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the nectin family.
  protein_domains: CD80_C2-set. (IPR013162); Ig-like_dom. (IPR007110); Ig-like_dom_sf.
    (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599)
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
citation_count: 76
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IX39
- **Protein Description:** RecName: Full=Cell adhesion molecule 1 {ECO:0000256|ARBA:ARBA00068781}; AltName: Full=Synaptic cell adhesion molecule {ECO:0000256|ARBA:ARBA00080773};
- **Gene Information:** Name=CADM1 {ECO:0000313|Ensembl:ENSEASP00005045449.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the nectin family.
- **Key Domains:** CD80_C2-set. (IPR013162); Ig-like_dom. (IPR007110); Ig-like_dom_sf. (IPR036179); Ig-like_fold. (IPR013783); Ig_sub. (IPR003599)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CADM1" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CADM1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CADM1** (gene ID: CADM1, UniProt: A0A9L0IX39) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CADM1 (Cell adhesion molecule 1; SynCAM1/TSLC1/Necl-2) in the donkey, *Equus asinus* — UniProt A0A9L0IX39

## Introduction and summary

UniProt entry A0A9L0IX39 is an unreviewed (TrEMBL) protein from the donkey (*Equus asinus*, taxon 9793). It is named "Cell adhesion molecule 1" (alternative name "Synaptic cell adhesion molecule"), comes from the gene model CADM1 (Ensembl ENSEASG00005006655, donkey chromosome 20), and is placed in the nectin family. Its gene models derive from the chromosome-level donkey reference genome [wang-2020-donkey-genomes-abstract]. I found no experimental study of the donkey protein's biochemistry. The one donkey-specific study detected CADM1 by immunohistochemistry in donkey testis [gewaily-2020-cadm1-testes-farm-animals-abstract]. Closely related horse studies show that CADM1 marks equine dendritic-cell subsets [ziegler-2016-equine-pdc-abstract; baillou-2026-equine-dc-scrnaseq-fulltext]. The functional description below therefore rests mostly on orthologs: human CADM1 (TSLC1/IGSF4/Necl-2), mouse and rat Cadm1 (SynCAM1/RA175/SgIGSF).

The identity check is clear. The gene symbol, the protein name, the nectin-family classification and the domain set (one Ig V-set and two Ig C2/I-set domains, a single transmembrane helix) all match the well-studied vertebrate CADM1. I aligned A0A9L0IX39 with human CADM1 (Q9BY67; `notes/donkey_vs_human_CADM1.aln`). The extracellular region is about 99% identical, with only a few conservative substitutions. The literature under the symbol CADM1 does not appear to be split across unrelated genes. The aliases TSLC1, SynCAM1, Necl-2, IGSF4, RA175 and SgIGSF all refer to the same protein [shingai-2003-necl2-epithelial-abstract; biederer-2006-syncam-bioinformatic-abstract].

In summary, CADM1 is a single-pass type I transmembrane glycoprotein of the immunoglobulin superfamily. It does not catalyse any reaction or transport any substrate. Its main role is as a Ca²⁺-independent cell–cell adhesion receptor and signalling scaffold. The extracellular V-type Ig domain mediates homophilic binding in cis and in trans. It also mediates heterophilic binding to CADM3 (Necl-1), CADM2 (SynCAM2), nectin-3 and the lymphocyte receptor CRTAM [masuda-2002-tslc1-homophilic-abstract; shingai-2003-necl2-epithelial-abstract; fogel-2007-syncam-heterophilic-abstract; boles-2005-crtam-necl2-abstract; zhang-2013-crtam-necl2-structure-abstract]. In the canonical isoform, the short cytoplasmic tail carries two motifs that connect adhesion to the cell interior. A juxtamembrane 4.1/FERM-binding motif binds protein 4.1B/DAL-1 (EPB41L3) and the Rac-GEF Farp1. A C-terminal PDZ-binding motif (EYFI) binds MAGUK scaffolds such as MPP3 and Pals2 [yageta-2002-tslc1-dal1-abstract; cheadle-2012-farp1-fulltext; fukuhara-2003-tslc1-mpp3-abstract; shingai-2003-necl2-epithelial-abstract]. Through these interactions the same molecular activity serves several tissue-level functions. In the brain CADM1 is a synaptogenic trans-synaptic adhesion molecule [biederer-2002-syncam-abstract; robbins-2010-syncam1-synapse-number-fulltext]. In epithelia it is a lateral junction molecule whose loss contributes to cancer, which is why it was first named a tumour suppressor [kuramochi-2001-tslc1-abstract; mao-2003-tslc1-cytoplasmic-abstract]. In the testis it forms the junction that holds developing spermatids to Sertoli cells [vanderweyden-2006-tslc1-infertility-abstract; fujita-2006-ra175-spermatogenesis-abstract]. In mast cells it mediates both mast cell–nerve and mast cell–mast cell adhesion [furuno-2005-sgigsf-mast-nerve-abstract; moiseeva-2012-cadm1-mast-isoforms-fulltext]. Finally, on dendritic cells and tumour cells it is the ligand recognised by the lymphocyte receptor CRTAM [galibert-2005-necl2-crtam-abstract; boles-2005-crtam-necl2-abstract].

The specific donkey isoform described by A0A9L0IX39 has an important caveat, discussed in detail below. It lacks the O-glycosylated extracellular stalk, and it ends in a divergent 11-residue C-terminus (…RHKG**LFSLTSSPRIK**). That tail keeps only the first part of the FERM-binding motif and lacks the PDZ-binding motif. In the Ensembl gene model this C-terminus comes from an alternative terminal exon located about 6 kb downstream of the canonical last exon. If this transcript is expressed, it would encode an adhesion-competent ectodomain with a reduced capacity for cytoplasmic signalling.

## Gene identity, domain architecture and isoform structure of the donkey protein

A0A9L0IX39 is a 390-residue precursor. SignalP predicts a long signal peptide (residues 1–47), and Phobius places one helical transmembrane segment at residues 350–375. PROSITE identifies three Ig-like domains (residues 43–142, 147–241 and 246–320). InterPro assigns them to the V-set (IPR013106), the CD80-like C2-set (IPR013162) and the generic Ig families. The Conserved Domain Database assigns the first two domains to the Necl-2-specific families IgV_1_Necl-2 and IgI_2_Necl-2. The PANTHER subfamily is PTHR45889:SF2 (CELL ADHESION MOLECULE 1). These are all automated annotations taken from the UniProt record. They agree with the architecture described for the whole vertebrate SynCAM/CADM family: three extracellular Ig-like domains of the V, C1 and I-set subclasses, a single transmembrane region and a short cytosolic tail with conserved protein-interaction motifs [biederer-2006-syncam-bioinformatic-abstract].

My own sequence analysis supports both orthology and function. The six cysteines that form the three intradomain disulfides in human CADM1 (Cys64–Cys124, Cys166–Cys220 and Cys267–Cys313; the first is seen in crystal structure PDB 4H5S) are conserved in donkey at positions 67/127, 169/223 and 270/316. The donkey positions are shifted by +3 because the donkey signal peptide has three extra alanines. N-glycosylation sequons (N-X-S/T) occur at donkey residues 70, 104, 116, 168, 307 and 311. These correspond to human Asn67, Asn101, Asn113, Asn165, Asn304 and Asn308. The first two are equivalent to the Ig1 glycosylation sites that flank the adhesive interface. In the mouse protein, N-glycans at those two sites, including their sialic acids, strengthen SynCAM1 adhesion and are required for synapse induction [fogel-2010-syncam-glycosylation-abstract].

There are two isoform-level differences from human CADM1 isoform 1. First, the donkey protein lacks the threonine/proline-rich, O-glycosylation-rich stalk between the third Ig domain and the transmembrane segment (human residues ~333–360). Diverse SynCAM1 isoforms are generated by alternative splicing in exactly this region [biederer-2006-syncam-bioinformatic-abstract]. In human mast cells, the predominant isoform is SP4 (exons 7/8/11), which lacks the stalk exons. SP4 promotes homotypic adhesion more strongly than the stalk-containing SP1 isoform [moiseeva-2012-cadm1-mast-isoforms-fulltext]. So the stalk-less ectodomain of A0A9L0IX39 represents a known, adhesion-competent splice form.

Second, the cytoplasmic sequence after the transmembrane segment reads RYFARHKG and then diverges to LFSLTSSPRIK-COOH. In human CADM1 the FERM/4.1-binding motif spans residues 398–410 (YFARHKGTYFTHE), and the PDZ-interacting motif spans residues 432–442 and ends in EYFI [mao-2003-tslc1-cytoplasmic-abstract]. The donkey product keeps only the membrane-proximal half of the FERM-binding motif and has no PDZ-binding motif. The other seven donkey CADM1 entries in UniProt (A0A9L0IJE9, A0A8C4LBJ1, A0A9L0IKY6, A0A9L0JLU5, A0A9L0JM59, A0A8C4PJC1 and A0A8C4LG30) show that the donkey gene encodes the canonical tail as well. Five of them end in …KGTYFTHEAKGADDAADADTAIINAEGGQNNSEEKKEYFI, identical to the human tail, and A0A9L0IKY6 combines the same stalk-less ectodomain with the full canonical tail (`notes/donkey_cadm1_isoforms_ctermini.txt`). To find where the divergent tail comes from, I compared the exon structures of the donkey CADM1 transcripts in Ensembl (`notes/ensembl_cadm1_exon_comparison.txt`). The transcript that encodes A0A9L0IX39 (CADM1-207, ENSEAST00005076104) shares its first eight coding exons with CADM1-205 (ENSEAST00005057483), which encodes A0A9L0IKY6. Both skip the three stalk exons that are present in the canonical 12-exon transcript CADM1-204. The two transcripts differ only in their final exon. CADM1-205 ends with the canonical last exon (chromosome 20: 36,100,859–36,101,978), which encodes TYFTHE…EYFI. CADM1-207 instead splices from the transmembrane/juxtamembrane exon to a separate 1,039-nt exon about 6 kb further downstream (36,107,771–36,108,809). The first codons of that exon encode LFSLTSSPRIK and then a stop. So A0A9L0IX39 is the product of a predicted alternative terminal exon, not of intron read-through. I could not find transcript-level evidence (for example ESTs or long-read support) for this exon in donkey, and no equivalent human isoform with this C-terminus is described in UniProt. It is therefore at best a minor product, and it may be a prediction artefact. It is not the main donkey CADM1 product. For annotation, the core CADM1 functions should be attributed to the gene. Tail-dependent interactions should be stated with caution for this particular isoform.

## Molecular function: Ca²⁺-independent homophilic and heterophilic adhesion

The best-supported molecular activity of CADM1 is cell–cell adhesion through binding of Ig domains. When human TSLC1 is expressed in MDCK epithelial cells it is an N-linked glycoprotein of about 75 kDa. It forms cis homodimers within the plasma membrane, accumulates at cell–cell boundaries and on the lateral membranes of polarized cells, and causes cells to aggregate whether or not Ca²⁺ and Mg²⁺ are present. This is direct evidence for Ca²⁺-independent homophilic trans adhesion [masuda-2002-tslc1-homophilic-abstract]. Shingai and colleagues independently characterized rat Necl-2. It showed Ca²⁺-independent homophilic adhesion, and also Ca²⁺-independent heterophilic adhesion with Necl-1 (CADM3/SynCAM3) and with nectin-3 [shingai-2003-necl2-epithelial-abstract]. In neurons, SynCAM1 forms homophilic complexes but preferentially pairs with SynCAM2 (CADM2) to form an asymmetric heterophilic trans-synaptic complex, and glycosylation modulates this interaction [fogel-2007-syncam-heterophilic-abstract]. Nectins and Necls generally use homophilic and heterophilic engagement as tools for communication between cells. Necls, including Necl-2, have a broader range of cellular functions than nectins, which are mainly adhesion molecules [takai-2008-nectins-review-abstract].

Structural work has defined the binding mode. The crystal structure of the Necl-2 V-domain bound to the CRTAM V-domain shows that Necl-2 occupies the interface CRTAM would use to homodimerize. A "double lock-and-key" set of residues makes heterophilic binding compete with CRTAM homodimerization, and probably with Necl-2 homodimerization as well [zhang-2013-crtam-necl2-structure-abstract]. This agrees with the finding that the heterotypic CRTAM–Necl2 interaction has higher affinity than the homotypic Necl2 interaction [arase-2005-crtam-necl2-abstract]. Beyond trans binding, CADM1 also assembles laterally in the same membrane. SynCAM1 self-associates in cis through its membrane-proximal Ig2 and Ig3 domains. These cis oligomers have greater adhesive capacity, drive clustering of SynCAM1 at new axo-dendritic contacts, and are needed for its synaptogenic activity [fogel-2011-syncam1-lateral-assembly-abstract]. Two cis partners outside the family show that the ectodomain also regulates other receptors in the same membrane. In cancer cells, the ectodomain of Necl-2 binds ErbB3 and damps ErbB3/ErbB2 signalling [kawano-2009-necl2-erbb3-abstract]. In epithelial cells, it binds integrin β4 and stabilizes integrin α6β4 in hemidesmosomes [mizutani-2011-necl2-integrin-abstract]. All of these are extracellular interactions, so the stalk-less ectodomain of A0A9L0IX39, which keeps all three Ig domains intact, should retain them. For a GO-style description, the molecular function is protein homodimerization and cell adhesion molecule binding (homophilic and heterophilic), with the V-type Ig domain as the binding module. No enzymatic or transport activity has been described.

## Cytoplasmic partners and signalling pathways

The canonical CADM1 tail links extracellular adhesion to the cortical cytoskeleton and to scaffolding complexes. Its juxtamembrane 4.1/FERM-binding motif binds DAL-1 (protein 4.1B, EPB41L3) directly. Through DAL-1, TSLC1 associates with actin filaments at cell–cell contact sites, and the complex depends on an intact actin cytoskeleton. The two proteins also move together into newly forming membrane ruffles [yageta-2002-tslc1-dal1-abstract]. The C-terminal PDZ-binding motif binds the MAGUK MPP3, a human homologue of the *Drosophila* tumour suppressor Discs large, and the two proteins colocalize at cell–cell attachment sites [fukuhara-2003-tslc1-mpp3-abstract]. Necl-2 also binds another MAGUK, Pals2, but unlike the nectins it does not bind afadin. This suggests that CADM1 helps position other transmembrane proteins through MAGUK–Lin-7 complexes [shingai-2003-necl2-epithelial-abstract]. Both motifs matter for function. Deleting the FERM-binding motif, the PDZ-binding motif or the whole cytoplasmic domain abolished the tumour-suppressor activity of TSLC1 in A549 xenografts [mao-2003-tslc1-cytoplasmic-abstract]. The PDZ- and FERM-binding motifs are highly conserved across all four SynCAMs [biederer-2006-syncam-bioinformatic-abstract].

Later work has identified several signalling outputs that run through the two tail motifs. In MDCK cells, engaging CADM1 in trans with a recombinant CADM1 ectodomain triggers cell spreading that depends on phosphoinositide 3-kinase (PI3K), and partly on its effectors Akt and Rac1. MPP3 and Dlg link the CADM1 tail to the p85 regulatory subunit of PI3K at the cell periphery. The resulting pathway runs from trans-homophilic adhesion through the PDZ motif and a MAGUK complex to PI3K and actin remodelling [murakami-2014-cadm1-pi3k-fulltext]. The PDZ-binding motif also binds the PDZ domain of Tiam1, a Rac-specific guanine-nucleotide exchange factor. In adult T-cell leukaemia cells, which express CADM1 ectopically, this interaction activates Rac and drives lamellipodia formation [masuda-2010-cadm1-tiam1-abstract]. The tail additionally binds the tyrosine phosphatase PTPN13. PTPN13 is needed for Necl-2 to suppress ErbB3 phosphorylation and downstream Rac/Akt activation, so in this case the ectodomain selects the receptor and the tail delivers the inhibitory enzyme [kawano-2009-necl2-erbb3-abstract]. In neurons, protein 4.1B bound to the juxtamembrane motif recruits NMDA-type glutamate receptors to SynCAM1 adhesion sites, and 4.1N may similarly recruit AMPA receptors [hoy-2009-syncam1-4.1b-nmda-fulltext]. This gives a direct route from adhesion to the assembly of a postsynaptic receptor field. SynCAM1 also binds focal adhesion kinase, which takes part in SynCAM1-dependent shaping of growth cones [stagi-2010-syncam1-growth-cones-abstract].

At synapses, the best-defined downstream pathway runs through Farp1 (FERM, RhoGEF and pleckstrin domain protein 1). A proteomic comparison of synaptic membranes from SynCAM1-knockout and wild-type mice found Farp1 strongly reduced in the knockouts. The Farp1 FERM domain binds the SynCAM1 tail, and this binding requires the SynCAM1 FERM-binding motif. Downstream of SynCAM1 clustering, Farp1 activates the small GTPase Rac1 in dendritic spines and promotes F-actin assembly. SynCAM1 needs Farp1 to increase spine number, and Farp1 also triggers a retrograde signal that regulates the composition of the presynaptic active zone [cheadle-2012-farp1-fulltext]. The resulting pathway is: trans-synaptic CADM1 adhesion → clustering of the CADM1 tail → Farp1 recruitment through the FERM motif → Rac1 activation → actin remodelling and spine/synapse maturation. A0A9L0IX39 has a truncated FERM motif (RYFARHKG, then a divergent sequence). Farp1 binding to the SynCAM1 tail was lost when part of this motif was deleted [cheadle-2012-farp1-fulltext], so this donkey isoform may bind Farp1 and 4.1 proteins poorly. This is an untested prediction. The PDZ-dependent outputs (MPP3/Dlg–PI3K, Tiam1–Rac and Pals2) need the C-terminal motif, which A0A9L0IX39 lacks entirely. Whether the remaining RYFARHKG stretch is enough for 4.1B and the 4.1B-dependent recruitment of NMDA receptors is unknown.

## Subcellular localization

CADM1 is a plasma-membrane protein with a type I topology: the N-terminus is extracellular, there is one transmembrane helix and the C-terminus is cytoplasmic. In polarized epithelial cells it lies along the lateral membrane [masuda-2002-tslc1-homophilic-abstract]. In mouse gallbladder epithelium it localizes specifically to the basolateral plasma membrane, but not to tight junctions, adherens junctions or desmosomes [shingai-2003-necl2-epithelial-abstract]. In migrating or spreading cells it accumulates at sites of cell–cell attachment and in membrane ruffles together with DAL-1 [yageta-2002-tslc1-dal1-abstract].

In neurons, SynCAM1 sits at both excitatory and inhibitory synapses and in pre- and postsynaptic membranes, where it forms trans-synaptic complexes across the synaptic cleft [fogel-2007-syncam-heterophilic-abstract; biederer-2002-syncam-abstract]. Before synapses form, SynCAM1 is already in axonal growth cones, and it rapidly forms stable adhesive clusters where growth cones contact target neurites [stagi-2010-syncam1-growth-cones-abstract]. Later in development its partner Farp1 is postsynaptic [cheadle-2012-farp1-fulltext].

In the testis, Cadm1/RA175 is found at the cell junctions of spermatocytes and of elongating and elongated spermatids. In elongated spermatids it is restricted to the tail side [fujita-2006-ra175-spermatogenesis-abstract].

In donkey testis, immunohistochemistry detected CADM1 in spermatogonia, early spermatocytes and elongated spermatids, but not in Sertoli or interstitial cells [gewaily-2020-cadm1-testes-farm-animals-abstract]. This is the only direct localization evidence for the donkey protein.

At points of contact between mast cells and neurites, CADM1 becomes concentrated in both cells [furuno-2005-sgigsf-mast-nerve-abstract]. In epithelial cells, CADM1 is concentrated at cell–cell contact sites together with MPP3 and Dlg [murakami-2014-cadm1-pi3k-fulltext].

The UniProt cellular-component annotations for A0A9L0IX39 (cell membrane, synapse, neuron projection) are inferred electronically, but they agree with these ortholog data.

## Biological roles: synapse formation, spermatogenesis, mast cells and the immune system

**Synapse assembly and plasticity.** SynCAM was first defined as a brain-expressed homophilic adhesion molecule that drives synapse assembly. Expressing its isolated cytoplasmic tail in neurons blocked synapse assembly. Expressing full-length SynCAM in non-neuronal cells induced cocultured hippocampal neurons to form functional presynaptic terminals onto them, and adding glutamate receptors reconstituted glutamatergic transmission [biederer-2002-syncam-abstract]. In mice, overexpressing SynCAM1 increased the number of excitatory synapses and maintained the newly induced synapses. Knocking it out reduced excitatory synapses, changed long-term depression and, unexpectedly, improved spatial learning [robbins-2010-syncam1-synapse-number-fulltext]. In the prefrontal cortex, SynCAM1 sets synapse number together with LRRTM1. Losing both proteins lowered spine density more than the sum of the single knockouts and disrupted network activity and social and cognitive behaviour [dearce-2023-lrrtm1-syncam1-abstract]. Outside synapses, SynCAMs also take part in axon guidance and myelination [frei-2014-syncam-review-abstract].

**Spermatogenesis.** Two independent knockout lines showed that Cadm1 is essential for male fertility. In Tslc1-null males, spermatogenesis stopped at the spermatid stage: apoptotic spermatids were shed into the lumen, and the few spermatozoa were immature and rarely motile [vanderweyden-2006-tslc1-infertility-abstract]. Ra175-null males showed oligo-astheno-teratozoospermia. Their elongating spermatids could not mature or move to the adluminal surface and were eventually phagocytosed by Sertoli cells. This indicates that the CADM1-based junction holds elongating spermatids inside Sertoli cell invaginations [fujita-2006-ra175-spermatogenesis-abstract]. In donkey, CADM1 is expressed in spermatogonia, early spermatocytes and elongated spermatids [gewaily-2020-cadm1-testes-farm-animals-abstract]. This matches the mouse pattern of expression in early and late germ cells [vanderweyden-2006-tslc1-infertility-abstract] and suggests the role is conserved in the donkey.

**Mast cells and nerve–immune contacts.** Mast cells use CADM1 to attach to neurites, and this adhesion makes nerve-to-mast-cell Ca²⁺ signalling more efficient [furuno-2005-sgigsf-mast-nerve-abstract]. In human mast cells, CADM1 is the only receptor for homotypic aggregation. Knocking it down lowers survival, with reduced Mcl-1 and Kit and increased caspase-3/7 activity. The stalk-less SP4 isoform is the most adhesive [moiseeva-2012-cadm1-mast-isoforms-fulltext].

**Immune recognition via CRTAM.** CADM1 is the ligand of CRTAM, a receptor that appears on activated NK cells and CD8⁺ T cells [arase-2005-crtam-necl2-abstract; galibert-2005-necl2-crtam-abstract]. CRTAM–CADM1 engagement promotes NK cytotoxicity and CD8⁺ T-cell IFN-γ production, and NK cells reject CADM1-expressing tumours in vivo [boles-2005-crtam-necl2-abstract]. CADM1 marks the cDC1 dendritic-cell subset (human BDCA3⁺ and mouse CD8α⁺ cells). On antigen-presenting cells it regulates IL-22 production by CD8⁺ T cells [galibert-2005-necl2-crtam-abstract]. The same marker works in equids. In horse blood, DC subsets are separated by CADM1 and MHC-II, with pDC being CADM1-negative [ziegler-2016-equine-pdc-abstract]. Single-cell transcriptomics confirms high CADM1 expression in equine cDC1 [baillou-2026-equine-dc-scrnaseq-fulltext].

**Tumour suppression.** TSLC1/CADM1 was cloned as a tumour suppressor at 11q23.2 in non-small-cell lung cancer. It is silenced by promoter hypermethylation in lung, liver and pancreatic cancers, and restoring it suppresses tumorigenicity [kuramochi-2001-tslc1-abstract]. Its activity depends on the cytoplasmic 4.1- and PDZ-binding motifs [mao-2003-tslc1-cytoplasmic-abstract]. It suppresses metastasis together with DAL-1 [yageta-2002-tslc1-dal1-abstract]. These broad oncological effects are best explained by CADM1's main role in organising cell–cell adhesion and adhesion-linked cytoskeletal signalling. A second mechanism is that it presents a ligand to cytotoxic lymphocytes [boles-2005-crtam-necl2-abstract].

## Evidence assessment and implications for annotating A0A9L0IX39

The evidence for this donkey protein is layered. Direct donkey evidence is limited to one immunohistochemistry study in testis [gewaily-2020-cadm1-testes-farm-animals-abstract]. Closely related equid evidence (horse dendritic cells) supports conserved expression in immune cells [ziegler-2016-equine-pdc-abstract; baillou-2026-equine-dc-scrnaseq-fulltext]. Everything else is transferred from orthologs, but the ortholog evidence is strong and of several independent kinds. It includes direct binding and cell-aggregation assays [masuda-2002-tslc1-homophilic-abstract; shingai-2003-necl2-epithelial-abstract], crystal structures [zhang-2013-crtam-necl2-structure-abstract; fogel-2010-syncam-glycosylation-abstract], interaction motifs mapped by deletion [yageta-2002-tslc1-dal1-abstract; fukuhara-2003-tslc1-mpp3-abstract; cheadle-2012-farp1-fulltext], and several knockout mouse lines [robbins-2010-syncam1-synapse-number-fulltext; vanderweyden-2006-tslc1-infertility-abstract; fujita-2006-ra175-spermatogenesis-abstract].

The ectodomain is about 99% identical to human CADM1, the key cysteines and functional N-glycosylation sites are conserved, and the gene is assigned to the CADM1 PANTHER subfamily. Together these justify transferring the extracellular functions with high confidence: homophilic adhesion, heterophilic binding to CADM2/CADM3/nectin-3/CRTAM, plasma-membrane and synaptic localization, and roles in synapse organization, spermatid adhesion and immune recognition.

The cytoplasmic interactions with 4.1B/DAL-1, Farp1, MPP2/MPP3, Pals2, Tiam1 and PTPN13 need more care. UniProt's ARBA-derived subunit annotation transfers several of them to A0A9L0IX39, but this isoform lacks the PDZ-binding motif needed for MAGUK and Tiam1 binding [fukuhara-2003-tslc1-mpp3-abstract; masuda-2010-cadm1-tiam1-abstract]. It also has only a partial FERM-binding motif, encoded by the alternative terminal exon described above. For this isoform these interactions are therefore doubtful. They would hold for the canonical donkey isoforms that carry the full tail (e.g. A0A9L0IKY6, A0A9L0IJE9).

For Gene Ontology annotation, the safest terms are those that depend only on the ectodomain or are properties of the whole gene. For molecular function, these are homophilic cell–cell adhesion (GO:0007156, already annotated by TreeGrafter), heterophilic cell–cell adhesion, protein homodimerization activity, and signaling receptor binding (GO:0005102), the last reflecting CADM1's role as the CRTAM ligand. For cellular component, plasma membrane (GO:0005886) and synapse (GO:0045202) are appropriate. For biological process, synapse assembly or positive regulation of synapse assembly, and spermatid development, are appropriate. Terms that depend on the tail, such as PDZ-domain binding or positive regulation of PI3K signalling, should be attached to the canonical donkey isoforms rather than to this isoform specifically.

## Open Questions

Several questions remain open. The first is whether the A0A9L0IX39 transcript is real. This analysis shows that it uses a predicted alternative terminal exon about 6 kb downstream of the canonical last exon. The next step would be to look for RNA-seq split reads or long-read (Iso-Seq) support for the splice junction from the transmembrane exon to this downstream exon in donkey tissues, and to check whether the exon is conserved in horse and other mammals. Resources such as the donkey genome assemblies would be the starting point [wang-2020-donkey-genomes-abstract]. If the isoform is real, it would be an adhesion-competent protein whose tail cannot signal through the PDZ motif. It could act in a dominant-negative way, much as expressing the isolated tail or tail-truncated constructs perturbs synapse assembly and tumour suppression [biederer-2002-syncam-abstract; mao-2003-tslc1-cytoplasmic-abstract].

A second question is how the different donkey CADM1 isoforms are distributed across tissues. No equid data exist on the relative use of stalk-containing and stalk-less forms in brain, testis, lung or mast cells. Isoform choice matters: in human mast cells the stalk-less SP4 isoform dominates and is the most adhesive [moiseeva-2012-cadm1-mast-isoforms-fulltext], and the stalk region sits next to the Ig2–Ig3 interface that mediates cis assembly [fogel-2011-syncam1-lateral-assembly-abstract].

A third question concerns germ cells. CADM1 expression in donkey testis (spermatogonia, early spermatocytes and elongated spermatids) differs from that in bull and camel [gewaily-2020-cadm1-testes-farm-animals-abstract]. It is not known whether this reflects real species differences in how germ cells use CADM1, or differences in antibodies and isoforms detected. CADM1 has not been studied in relation to the sterility of horse × donkey hybrids, although the spermatid-arrest phenotype of the knockout mice makes it a plausible candidate to examine [vanderweyden-2006-tslc1-infertility-abstract; fujita-2006-ra175-spermatogenesis-abstract].

A fourth question is whether the CRTAM–CADM1 axis works in equids. Horse cDC1 express high levels of CADM1 [baillou-2026-equine-dc-scrnaseq-fulltext]. However, no study has tested whether equine CRTAM binds equine CADM1, or whether the pair regulates equid NK and CD8⁺ T-cell responses as it does in mice and humans [boles-2005-crtam-necl2-abstract; galibert-2005-necl2-crtam-abstract]. The CRTAM-contact residues defined in the human complex structure [zhang-2013-crtam-necl2-structure-abstract] lie in the V domain, which is essentially identical in donkey, so conserved binding is expected but not demonstrated.

Finally, it is unknown whether glycosylation is conserved. The donkey Ig1 sequons at Asn70 and Asn104 match the sites that strengthen adhesion in rodents [fogel-2010-syncam-glycosylation-abstract]. Mass-spectrometric glycoproteomics of donkey or horse brain would show whether the same N-glycans and sialylation are present. Comparing these would help explain how CADM1 adhesion is tuned in different tissues.

## References

- **arase-2005-crtam-necl2** — Arase N, Takeuchi A, Unno M, Hirano S, Yokosuka T, Arase H et al. (2005). Heterotypic interaction of CRTAM with Necl2 induces cell adhesion on activated NK cells and CD8+ T cells. International immunology 17:1227-37. PMID:16091383; DOI:10.1093/intimm/dxh299. https://pubmed.ncbi.nlm.nih.gov/16091383/ ; https://doi.org/10.1093/intimm/dxh299
- **baillou-2026-equine-dc-scrnaseq** — Baillou A, Botos M, Oberhaensli S, Cvitas I, Jonsdottir S, Ziegler A et al. (2026). Dendritic-cell diversity in equine blood revealed by single-cell transcriptomics. Discovery immunology 5:kyag012. PMID:42453898; PMCID:PMC13367329; DOI:10.1093/discim/kyag012. https://pubmed.ncbi.nlm.nih.gov/42453898/ ; https://doi.org/10.1093/discim/kyag012
- **biederer-2002-syncam** — Biederer T, Sara Y, Mozhayeva M, Atasoy D, Liu X, Kavalali ET et al. (2002). SynCAM, a synaptic adhesion molecule that drives synapse assembly. Science (New York, N.Y.) 297:1525-31. PMID:12202822; DOI:10.1126/science.1072356. https://pubmed.ncbi.nlm.nih.gov/12202822/ ; https://doi.org/10.1126/science.1072356
- **biederer-2006-syncam-bioinformatic** — Biederer T (2006). Bioinformatic characterization of the SynCAM family of immunoglobulin-like domain-containing adhesion molecules. Genomics 87:139-50. PMID:16311015; DOI:10.1016/j.ygeno.2005.08.017. https://pubmed.ncbi.nlm.nih.gov/16311015/ ; https://doi.org/10.1016/j.ygeno.2005.08.017
- **boles-2005-crtam-necl2** — Boles KS, Barchet W, Diacovo T, Cella M, Colonna M (2005). The tumor suppressor TSLC1/NECL-2 triggers NK-cell and CD8+ T-cell responses through the cell-surface receptor CRTAM. Blood 106:779-86. PMID:15811952; DOI:10.1182/blood-2005-02-0817. https://pubmed.ncbi.nlm.nih.gov/15811952/ ; https://doi.org/10.1182/blood-2005-02-0817
- **cheadle-2012-farp1** — Cheadle L, Biederer T (2012). The novel synaptogenic protein Farp1 links postsynaptic cytoskeletal dynamics and transsynaptic organization. The Journal of cell biology 199:985-1001. PMID:23209303; PMCID:PMC3518221; DOI:10.1083/jcb.201205041. https://pubmed.ncbi.nlm.nih.gov/23209303/ ; https://doi.org/10.1083/jcb.201205041
- **dearce-2023-lrrtm1-syncam1** — de Arce KP, Ribic A, Chowdhury D, Watters K, Thompson GJ, Sanganahalli BG et al. (2023). Concerted roles of LRRTM1 and SynCAM 1 in organizing prefrontal cortex synapses and cognitive functions. Nature communications 14:459. PMID:36709330; PMCID:PMC9884278; DOI:10.1038/s41467-023-36042-w. https://pubmed.ncbi.nlm.nih.gov/36709330/ ; https://doi.org/10.1038/s41467-023-36042-w
- **fogel-2007-syncam-heterophilic** — Fogel AI, Akins MR, Krupp AJ, Stagi M, Stein V, Biederer T (2007). SynCAMs organize synapses through heterophilic adhesion. The Journal of neuroscience : the official journal of the Society for Neuroscience 27:12516-30. PMID:18003830; PMCID:PMC6673342; DOI:10.1523/JNEUROSCI.2739-07.2007. https://pubmed.ncbi.nlm.nih.gov/18003830/ ; https://doi.org/10.1523/JNEUROSCI.2739-07.2007
- **fogel-2010-syncam-glycosylation** — Fogel AI, Li Y, Giza J, Wang Q, Lam TT, Modis Y et al. (2010). N-glycosylation at the SynCAM (synaptic cell adhesion molecule) immunoglobulin interface modulates synaptic adhesion. The Journal of biological chemistry 285:34864-74. PMID:20739279; PMCID:PMC2966101; DOI:10.1074/jbc.M110.120865. https://pubmed.ncbi.nlm.nih.gov/20739279/ ; https://doi.org/10.1074/jbc.M110.120865
- **fogel-2011-syncam1-lateral-assembly** — Fogel AI, Stagi M, Perez de Arce K, Biederer T (2011). Lateral assembly of the immunoglobulin protein SynCAM 1 controls its adhesive function and instructs synapse formation. The EMBO journal 30:4728-38. PMID:21926970; PMCID:PMC3243608; DOI:10.1038/emboj.2011.336. https://pubmed.ncbi.nlm.nih.gov/21926970/ ; https://doi.org/10.1038/emboj.2011.336
- **frei-2014-syncam-review** — Frei JA, Stoeckli ET (2014). SynCAMs extend their functions beyond the synapse. The European journal of neuroscience 39:1752-60. PMID:24628990; DOI:10.1111/ejn.12544. https://pubmed.ncbi.nlm.nih.gov/24628990/ ; https://doi.org/10.1111/ejn.12544
- **fujita-2006-ra175-spermatogenesis** — Fujita E, Kouroku Y, Ozeki S, Tanabe Y, Toyama Y, Maekawa M et al. (2006). Oligo-astheno-teratozoospermia in mice lacking RA175/TSLC1/SynCAM/IGSF4A, a cell adhesion molecule in the immunoglobulin superfamily. Molecular and cellular biology 26:718-26. PMID:16382161; PMCID:PMC1346906; DOI:10.1128/MCB.26.2.718-726.2006. https://pubmed.ncbi.nlm.nih.gov/16382161/ ; https://doi.org/10.1128/MCB.26.2.718-726.2006
- **fukuhara-2003-tslc1-mpp3** — Fukuhara H, Masuda M, Yageta M, Fukami T, Kuramochi M, Maruyama T et al. (2003). Association of a lung tumor suppressor TSLC1 with MPP3, a human homologue of Drosophila tumor suppressor Dlg. Oncogene 22:6160-5. PMID:13679854; DOI:10.1038/sj.onc.1206744. https://pubmed.ncbi.nlm.nih.gov/13679854/ ; https://doi.org/10.1038/sj.onc.1206744
- **furuno-2005-sgigsf-mast-nerve** — Furuno T, Ito A, Koma Y, Watabe K, Yokozaki H, Bienenstock J et al. (2005). The spermatogenic Ig superfamily/synaptic cell adhesion molecule mast-cell adhesion molecule promotes interaction with nerves. Journal of immunology (Baltimore, Md. : 1950) 174:6934-42. PMID:15905536; DOI:10.4049/jimmunol.174.11.6934. https://pubmed.ncbi.nlm.nih.gov/15905536/ ; https://doi.org/10.4049/jimmunol.174.11.6934
- **galibert-2005-necl2-crtam** — Galibert L, Diemer GS, Liu Z, Johnson RS, Smith JL, Walzer T et al. (2005). Nectin-like protein 2 defines a subset of T-cell zone dendritic cells and is a ligand for class-I-restricted T-cell-associated molecule. The Journal of biological chemistry 280:21955-64. PMID:15781451; DOI:10.1074/jbc.M502095200. https://pubmed.ncbi.nlm.nih.gov/15781451/ ; https://doi.org/10.1074/jbc.M502095200
- **gewaily-2020-cadm1-testes-farm-animals** — Gewaily MS, Kassab M, Farrag FA, Almadaly EA, Atta MS, Abd-Elmaksoud A et al. (2020). Comparative expression of cell adhesion molecule1 (CADM1) in the testes of experimental mice and some farm animals. Acta histochemica 122:151456. PMID:31635798; DOI:10.1016/j.acthis.2019.151456. https://pubmed.ncbi.nlm.nih.gov/31635798/ ; https://doi.org/10.1016/j.acthis.2019.151456
- **hoy-2009-syncam1-4.1b-nmda** — Hoy JL, Constable JR, Vicini S, Fu Z, Washbourne P (2009). SynCAM1 recruits NMDA receptors via protein 4.1B. Molecular and cellular neurosciences 42:466-83. PMID:19796685; PMCID:PMC2784006; DOI:10.1016/j.mcn.2009.09.010. https://pubmed.ncbi.nlm.nih.gov/19796685/ ; https://doi.org/10.1016/j.mcn.2009.09.010
- **kawano-2009-necl2-erbb3** — Kawano S, Ikeda W, Kishimoto M, Ogita H, Takai Y (2009). Silencing of ErbB3/ErbB2 signaling by immunoglobulin-like Necl-2. The Journal of biological chemistry 284:23793-805. PMID:19561085; PMCID:PMC2749152; DOI:10.1074/jbc.M109.025155. https://pubmed.ncbi.nlm.nih.gov/19561085/ ; https://doi.org/10.1074/jbc.M109.025155
- **kuramochi-2001-tslc1** — Kuramochi M, Fukuhara H, Nobukuni T, Kanbe T, Maruyama T, Ghosh HP et al. (2001). TSLC1 is a tumor-suppressor gene in human non-small-cell lung cancer. Nature genetics 27:427-30. PMID:11279526; DOI:10.1038/86934. https://pubmed.ncbi.nlm.nih.gov/11279526/ ; https://doi.org/10.1038/86934
- **mao-2003-tslc1-cytoplasmic** — Mao X, Seidlitz E, Ghosh K, Murakami Y, Ghosh HP (2003). The cytoplasmic domain is critical to the tumor suppressor activity of TSLC1 in non-small cell lung cancer. Cancer research 63:7979-85. PMID:14633730. https://pubmed.ncbi.nlm.nih.gov/14633730/
- **masuda-2002-tslc1-homophilic** — Masuda M, Yageta M, Fukuhara H, Kuramochi M, Maruyama T, Nomoto A et al. (2002). The tumor suppressor protein TSLC1 is involved in cell-cell adhesion. The Journal of biological chemistry 277:31014-9. PMID:12050160; DOI:10.1074/jbc.M203620200. https://pubmed.ncbi.nlm.nih.gov/12050160/ ; https://doi.org/10.1074/jbc.M203620200
- **masuda-2010-cadm1-tiam1** — Masuda M, Maruyama T, Ohta T, Ito A, Hayashi T, Tsukasaki K et al. (2010). CADM1 interacts with Tiam1 and promotes invasive phenotype of human T-cell leukemia virus type I-transformed cells and adult T-cell leukemia cells. The Journal of biological chemistry 285:15511-15522. PMID:20215110; PMCID:PMC2865322; DOI:10.1074/jbc.M109.076653. https://pubmed.ncbi.nlm.nih.gov/20215110/ ; https://doi.org/10.1074/jbc.M109.076653
- **mizutani-2011-necl2-integrin** — Mizutani K, Kawano S, Minami A, Waseda M, Ikeda W, Takai Y (2011). Interaction of nectin-like molecule 2 with integrin alpha6beta4 and inhibition of disassembly of integrin alpha6beta4 from hemidesmosomes. The Journal of biological chemistry 286:36667-76. PMID:21880726; PMCID:PMC3196104; DOI:10.1074/jbc.M110.200535. https://pubmed.ncbi.nlm.nih.gov/21880726/ ; https://doi.org/10.1074/jbc.M110.200535
- **moiseeva-2012-cadm1-mast-isoforms** — Moiseeva EP, Leyland ML, Bradding P (2012). CADM1 isoforms differentially regulate human mast cell survival and homotypic adhesion. Cellular and molecular life sciences : CMLS 69:2751-64. PMID:22438059; PMCID:PMC3400039; DOI:10.1007/s00018-012-0948-y. https://pubmed.ncbi.nlm.nih.gov/22438059/ ; https://doi.org/10.1007/s00018-012-0948-y
- **murakami-2014-cadm1-pi3k** — Murakami S, Sakurai-Yageta M, Maruyama T, Murakami Y (2014). Trans-homophilic interaction of CADM1 activates PI3K by forming a complex with MAGuK-family proteins MPP3 and Dlg. PloS one 9:e82894. PMID:24503895; PMCID:PMC3913574; DOI:10.1371/journal.pone.0082894. https://pubmed.ncbi.nlm.nih.gov/24503895/ ; https://doi.org/10.1371/journal.pone.0082894
- **robbins-2010-syncam1-synapse-number** — Robbins EM, Krupp AJ, Perez de Arce K, Ghosh AK, Fogel AI, Boucard A et al. (2010). SynCAM 1 adhesion dynamically regulates synapse number and impacts plasticity and learning. Neuron 68:894-906. PMID:21145003; PMCID:PMC3026433; DOI:10.1016/j.neuron.2010.11.003. https://pubmed.ncbi.nlm.nih.gov/21145003/ ; https://doi.org/10.1016/j.neuron.2010.11.003
- **shingai-2003-necl2-epithelial** — Shingai T, Ikeda W, Kakunaga S, Morimoto K, Takekuni K, Itoh S et al. (2003). Implications of nectin-like molecule-2/IGSF4/RA175/SgIGSF/TSLC1/SynCAM1 in cell-cell adhesion and transmembrane protein localization in epithelial cells. The Journal of biological chemistry 278:35421-7. PMID:12826663; DOI:10.1074/jbc.M305387200. https://pubmed.ncbi.nlm.nih.gov/12826663/ ; https://doi.org/10.1074/jbc.M305387200
- **stagi-2010-syncam1-growth-cones** — Stagi M, Fogel AI, Biederer T (2010). SynCAM 1 participates in axo-dendritic contact assembly and shapes neuronal growth cones. Proceedings of the National Academy of Sciences of the United States of America 107:7568-73. PMID:20368431; PMCID:PMC2867738; DOI:10.1073/pnas.0911798107. https://pubmed.ncbi.nlm.nih.gov/20368431/ ; https://doi.org/10.1073/pnas.0911798107
- **takai-2008-nectins-review** — Takai Y, Miyoshi J, Ikeda W, Ogita H (2008). Nectins and nectin-like molecules: roles in contact inhibition of cell movement and proliferation. Nature reviews. Molecular cell biology 9:603-15. PMID:18648374; DOI:10.1038/nrm2457. https://pubmed.ncbi.nlm.nih.gov/18648374/ ; https://doi.org/10.1038/nrm2457
- **vanderweyden-2006-tslc1-infertility** — van der Weyden L, Arends MJ, Chausiaux OE, Ellis PJ, Lange UC, Surani MA et al. (2006). Loss of TSLC1 causes male infertility due to a defect at the spermatid stage of spermatogenesis. Molecular and cellular biology 26:3595-609. PMID:16611999; PMCID:PMC1447413; DOI:10.1128/MCB.26.9.3595-3609.2006. https://pubmed.ncbi.nlm.nih.gov/16611999/ ; https://doi.org/10.1128/MCB.26.9.3595-3609.2006
- **wang-2020-donkey-genomes** — Wang C, Li H, Guo Y, Huang J, Sun Y, Min J et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. Nature communications 11:6014. PMID:33293529; PMCID:PMC7723042; DOI:10.1038/s41467-020-19813-7. https://pubmed.ncbi.nlm.nih.gov/33293529/ ; https://doi.org/10.1038/s41467-020-19813-7
- **yageta-2002-tslc1-dal1** — Yageta M, Kuramochi M, Masuda M, Fukami T, Fukuhara H, Maruyama T et al. (2002). Direct association of TSLC1 and DAL-1, two distinct tumor suppressor proteins in lung cancer. Cancer research 62:5129-33. PMID:12234973. https://pubmed.ncbi.nlm.nih.gov/12234973/
- **zhang-2013-crtam-necl2-structure** — Zhang S, Lu G, Qi J, Li Y, Zhang Z, Zhang B et al. (2013). Competition of cell adhesion and immune recognition: insights into the interaction between CRTAM and nectin-like 2. Structure (London, England : 1993) 21:1430-9. PMID:23871486; DOI:10.1016/j.str.2013.06.006. https://pubmed.ncbi.nlm.nih.gov/23871486/ ; https://doi.org/10.1016/j.str.2013.06.006
- **ziegler-2016-equine-pdc** — Ziegler A, Marti E, Summerfield A, Baumann A (2016). Identification and characterization of equine blood plasmacytoid dendritic cells. Developmental and comparative immunology 65:352-357. PMID:27524460; DOI:10.1016/j.dci.2016.08.005. https://pubmed.ncbi.nlm.nih.gov/27524460/ ; https://doi.org/10.1016/j.dci.2016.08.005
- **UniProt A0A9L0IX39** — UniProtKB/TrEMBL entry A0A9L0IX39_EQUAS (Cell adhesion molecule 1, *Equus asinus*), entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0IX39.txt
- **UniProt Q9BY67** — UniProtKB/Swiss-Prot entry CADM1_HUMAN, used for alignment and human residue numbering. https://rest.uniprot.org/uniprotkb/Q9BY67.txt
- **Ensembl ENSEASG00005006655** — Ensembl donkey CADM1 gene (assembly ASM1607732v2), transcripts and exon coordinates retrieved via the Ensembl REST API. https://rest.ensembl.org/lookup/id/ENSEASG00005006655?expand=1


## Citations

1. arase-2005-crtam-necl2-abstract.md
2. arase-2005-crtam-necl2-summary.md
3. baillou-2026-equine-dc-scrnaseq-abstract.md
4. baillou-2026-equine-dc-scrnaseq-fulltext.txt
5. baillou-2026-equine-dc-scrnaseq-summary.md
6. biederer-2002-syncam-abstract.md
7. biederer-2002-syncam-summary.md
8. biederer-2006-syncam-bioinformatic-abstract.md
9. biederer-2006-syncam-bioinformatic-summary.md
10. boles-2005-crtam-necl2-abstract.md
11. boles-2005-crtam-necl2-summary.md
12. cheadle-2012-farp1-abstract.md
13. cheadle-2012-farp1-fulltext.txt
14. cheadle-2012-farp1-summary.md
15. dearce-2023-lrrtm1-syncam1-abstract.md
16. dearce-2023-lrrtm1-syncam1-fulltext.txt
17. dearce-2023-lrrtm1-syncam1-summary.md
18. fogel-2007-syncam-heterophilic-abstract.md
19. fogel-2007-syncam-heterophilic-summary.md
20. fogel-2010-syncam-glycosylation-abstract.md
21. fogel-2010-syncam-glycosylation-summary.md
22. fogel-2011-syncam1-lateral-assembly-abstract.md
23. fogel-2011-syncam1-lateral-assembly-summary.md
24. frei-2014-syncam-review-abstract.md
25. frei-2014-syncam-review-summary.md
26. fujita-2006-ra175-spermatogenesis-abstract.md
27. fujita-2006-ra175-spermatogenesis-summary.md
28. fukuhara-2003-tslc1-mpp3-abstract.md
29. fukuhara-2003-tslc1-mpp3-summary.md
30. furuno-2005-sgigsf-mast-nerve-abstract.md
31. furuno-2005-sgigsf-mast-nerve-summary.md
32. galibert-2005-necl2-crtam-abstract.md
33. galibert-2005-necl2-crtam-summary.md
34. gewaily-2020-cadm1-testes-farm-animals-abstract.md
35. gewaily-2020-cadm1-testes-farm-animals-summary.md
36. hoy-2009-syncam1-4.1b-nmda-abstract.md
37. hoy-2009-syncam1-4.1b-nmda-fulltext.txt
38. hoy-2009-syncam1-4.1b-nmda-summary.md
39. kawano-2009-necl2-erbb3-abstract.md
40. kawano-2009-necl2-erbb3-summary.md
41. kuramochi-2001-tslc1-abstract.md
42. kuramochi-2001-tslc1-summary.md
43. mao-2003-tslc1-cytoplasmic-abstract.md
44. mao-2003-tslc1-cytoplasmic-summary.md
45. masuda-2002-tslc1-homophilic-abstract.md
46. masuda-2002-tslc1-homophilic-summary.md
47. masuda-2010-cadm1-tiam1-abstract.md
48. masuda-2010-cadm1-tiam1-summary.md
49. mizutani-2011-necl2-integrin-abstract.md
50. mizutani-2011-necl2-integrin-summary.md
51. moiseeva-2012-cadm1-mast-isoforms-abstract.md
52. moiseeva-2012-cadm1-mast-isoforms-fulltext.txt
53. moiseeva-2012-cadm1-mast-isoforms-summary.md
54. murakami-2014-cadm1-pi3k-abstract.md
55. murakami-2014-cadm1-pi3k-fulltext.txt
56. murakami-2014-cadm1-pi3k-summary.md
57. robbins-2010-syncam1-synapse-number-abstract.md
58. robbins-2010-syncam1-synapse-number-fulltext.txt
59. robbins-2010-syncam1-synapse-number-summary.md
60. shingai-2003-necl2-epithelial-abstract.md
61. shingai-2003-necl2-epithelial-summary.md
62. stagi-2010-syncam1-growth-cones-abstract.md
63. stagi-2010-syncam1-growth-cones-summary.md
64. takai-2008-nectins-review-abstract.md
65. takai-2008-nectins-review-summary.md
66. vanderweyden-2006-tslc1-infertility-abstract.md
67. vanderweyden-2006-tslc1-infertility-summary.md
68. wang-2020-donkey-genomes-abstract.md
69. wang-2020-donkey-genomes-fulltext.txt
70. wang-2020-donkey-genomes-summary.md
71. yageta-2002-tslc1-dal1-abstract.md
72. yageta-2002-tslc1-dal1-summary.md
73. zhang-2013-crtam-necl2-structure-abstract.md
74. zhang-2013-crtam-necl2-structure-summary.md
75. ziegler-2016-equine-pdc-abstract.md
76. ziegler-2016-equine-pdc-summary.md
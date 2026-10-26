---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:23:51.108525'
end_time: '2026-10-26T00:32:45.201067'
duration_seconds: 534.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: ORC5
  gene_symbol: ORC5
  uniprot_accession: A0A9L0JAR4
  protein_description: 'RecName: Full=Origin recognition complex subunit 5 {ECO:0000256|ARBA:ARBA00069657};'
  gene_info: Name=ORC5 {ECO:0000313|Ensembl:ENSEASP00005050401.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the ORC5 family.
  protein_domains: AAA_16. (IPR041664); ORC5. (IPR020796); ORC5_C. (IPR047088); ORC5_lid.
    (IPR048866); P-loop_NTPase. (IPR027417)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 86
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JAR4
- **Protein Description:** RecName: Full=Origin recognition complex subunit 5 {ECO:0000256|ARBA:ARBA00069657};
- **Gene Information:** Name=ORC5 {ECO:0000313|Ensembl:ENSEASP00005050401.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the ORC5 family.
- **Key Domains:** AAA_16. (IPR041664); ORC5. (IPR020796); ORC5_C. (IPR047088); ORC5_lid. (IPR048866); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ORC5" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ORC5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ORC5** (gene ID: ORC5, UniProt: A0A9L0JAR4) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ORC5 (Origin Recognition Complex Subunit 5) in the Donkey, *Equus asinus* (UniProt A0A9L0JAR4)

## 1. Introduction and Summary

The protein encoded by donkey *ORC5* (UniProt A0A9L0JAR4; Ensembl gene ENSEASG00005017348, donkey chromosome 1) is the fifth subunit of the origin recognition complex (ORC), the six-subunit initiator of eukaryotic chromosomal DNA replication [uniprot-A0A9L0JAR4]. The gene model comes from the chromosome-level donkey reference genome [wang-2020-donkey-genomes], and the entry is unreviewed; all of its functional annotation (ORC membership, DNA replication origin binding, DNA replication initiation, nuclear localization) is electronically transferred by family-level rules rather than from experiments on donkey material [uniprot-A0A9L0JAR4]. No experimental study of ORC5 in the donkey, or in equids generally, was found. The identity check required by the brief is nevertheless clear-cut. The gene symbol, protein name, family assignment (ORC5 family; PANTHER PTHR12705) and domain architecture (an AAA+ P-loop NTPase module, the ORC5 lid and the ORC5 C-terminal winged-helix region) all agree with one another and with the well-studied ORC5 proteins of human, *Drosophila* and yeast. My own pairwise comparison shows that the 440-residue donkey protein is 95.7% identical to human ORC5 (O43913) over residues 1–420, and nearly all functional residues identified in structural studies are conserved. The one exception is the ORC4·ORC5 tether position (human Arg104), which is cysteine in the donkey model [uniprot-A0A9L0JAR4; uniprot-O43913-human-ORC5; tocilj-2017-human-orc-active-form]. Comparison with horse gene models suggests that the donkey entry's unusual C-terminus represents an alternative, equid-specific isoform [uniprot-ORC5-horse-mouse-cow]. Inferring function by orthology from the mammalian, insect and fungal literature is therefore justified, and the rest of this report does so.

On that basis, donkey ORC5 should be understood as a non-catalytic, ATP-binding AAA+ subunit of the ORC ring. ORC is a two-tiered, notched ring in which the AAA+ domains of Orc1–Orc5 are arranged in the order Orc1–Orc4–Orc5–Orc3–Orc2, capped by a collar of winged-helix domains [bleichert-2015-orc-crystal-structure]. ORC5 occupies a central position in this ring. Its Walker A motif binds ATP at the ORC4·ORC5 interface, and it donates an arginine finger into the neighbouring ORC4 nucleotide site. Because its Walker B and sensor motifs are degenerate, ORC5 binds ATP but does not hydrolyse it [bleichert-2015-orc-crystal-structure]. The main biochemical role of this ATP binding is architectural: in human cells and in yeast, ATP bound to ORC5 (and ORC4) is required for the ORC subunits to assemble and to stay stable [siddiqui-2007-atp-dependent-assembly; takahashi-2004-orc5-walkerA; makise-2007-orc5-walkerA-degradation]. Within the assembled complex, ORC5 helps encircle and bend origin DNA and contacts the MCM2–7 helicase during its loading. ORC5 thereby contributes to the "licensing" of replication origins in G1 phase by loading the MCM2–7 double hexamer [li-2018-orc-dna-structure; yuan-2017-occm-structure; schmidt-2020-metazoan-orc-dna]. In human cells ORC5 is also multi-mono-ubiquitylated on chromatin in S phase by the E3 ligase OBI1, and this modification promotes origin firing [coulombe-2019-obi1]. ORC5 has further been linked to chromatin opening and heterochromatin organization [giri-2016-orc5-chromatin-decondensation; prasanth-2010-orc-hp1-heterochromatin]. The protein acts in the nucleus, on chromatin at replication origins [uniprot-O43913-human-ORC5; ohta-2003-orc1-cycle].

## 2. Gene Identity, Sequence Conservation and Evolution

ORC5 was first identified in budding yeast as the gene for the fifth-largest ORC subunit. The temperature-sensitive *orc5-1* allele arrested the cell cycle, raised plasmid loss in a way that extra origins could suppress, and impaired silencing. Even then, the sequence was noted to contain a potential ATP-binding site that might mediate ATP-dependent origin binding by ORC [loo-1995-orc-silencing]. Vertebrate orthologues were cloned soon afterwards. Human ORC5 (originally ORC5L) maps to 7q22.1 and is about 35% identical to *Drosophila* Orc5 and about 20% identical to the yeast proteins [ishiai-1997-orc5-homologues; quintana-1998-orc5l]. Xenopus Orc5 co-purified as a 48-kDa subunit of egg-extract ORC [tugal-1998-orc4-orc5-related]. Sequence comparison showed that Orc1, Orc4 and Orc5 are related to one another and to the helicase loader Cdc6 [tugal-1998-orc4-orc5-related], which places ORC5 in the initiator clade of AAA+ ATPases that also includes bacterial DnaA [clarey-2006-orc-dnaa-core; bleichert-2017-replication-initiation-review].

The donkey protein carries the domain signatures expected of this lineage: AAA_16 (PF13191), ORC5_lid (PF21639) and ORC5_C (PF14630), within a P-loop NTPase fold (Gene3D 3.40.50.300) [uniprot-A0A9L0JAR4]. Aligning it with human ORC5 gives 402 identical positions out of 420 over the shared N-terminal 420 residues. The Walker A motif (GHTASGKT, with the catalytic lysine at K43) is identical, as are the ORC5 residues that contact ORC2 in the human cryo-EM structure (D132, E134, A135, N136) [cheng-2020-human-orc-assembly] and the DNA-proximal β-hairpin histidine H398 [jaremko-2020-human-orc-cryoem]. The two proteins differ only in their extreme C-termini. Donkey ORC5 ends in a 20-residue segment (…RGPPKTCLQTHKNRLTMSSH) in place of the human 15-residue tail (…RTVNFDIIKYLYDFL), so the donkey protein is 440 rather than 435 residues long [uniprot-A0A9L0JAR4; uniprot-O43913-human-ORC5]. The donkey model is not the human ORC5T splice variant: that variant diverges much earlier, from residue 294 onward, and it binds ORC4 but cannot bind ORC2 [quintana-1998-orc5l; uniprot-O43913-human-ORC5]. The donkey tail most likely reflects a different terminal exon or a gene-model artefact. Whether it changes function is unknown (see Open Questions).

A comparison with the predicted ORC5 proteins of the domestic horse (*Equus caballus*) helps explain where this tail comes from. UniProt holds eleven horse ORC5 gene-model products. Several of them, for example A0A3Q2KSP7 (437 residues) and F6V340, end in the conserved mammalian tail (…RAIARTVNFDIIKYLYDFL) that is also present in mouse ORC5 (Q9WUV0) and in cattle models [uniprot-ORC5-horse-mouse-cow]. One horse model, A0A3Q2IA91 (479 residues), ends in exactly the same 20 residues as the donkey protein (…RGPPKTCLQTHKNRLTMSSH) [uniprot-ORC5-horse-mouse-cow]. The donkey tail therefore probably comes from an alternative terminal exon used in equids, and A0A9L0JAR4 most likely represents an alternative isoform, not the canonical one; the donkey genome very probably also encodes a canonical-tail isoform that the current annotation has not captured. This is my inference from the predicted sequences and has not been confirmed with transcript data. The same comparison flags one internal substitution. Human ORC5 Arg104 acts as the "tether" residue of the ORC4·ORC5 ATP site, where it forms a salt bridge with ORC4 Glu113 [tocilj-2017-human-orc-active-form]. The donkey protein has cysteine at this position, all horse models and human have arginine, and mouse has glutamine [uniprot-ORC5-horse-mouse-cow; uniprot-O43913-human-ORC5]. Because the residue is not invariant among mammals, the substitution may be tolerated. It could also be a sequencing or assembly error specific to the donkey, and it should be checked before anyone draws conclusions about the donkey ORC4·ORC5 interface.

## 3. Structural Organization: ORC5 as an ATP-Binding but Non-Catalytic AAA+ Subunit

The 3.5 Å crystal structure of *Drosophila* ORC first showed how ORC5 is built into the complex [bleichert-2015-orc-crystal-structure]. Each of Orc1–Orc5 contributes an AAA+ module to a lower tier and a winged-helix (WH) domain to an upper collar. WH domains and AAA+ modules of neighbouring subunits are swapped, so each subunit's WH domain packs against its neighbour's AAA+ domain. Of all the AAA+ interfaces in ORC, the Orc4·Orc5 interface looks most like those of canonical AAA+ ATPases. There the two subunits form a bipartite nucleotide-binding site, and Orc5 supplies a conserved arginine finger (Arg144 in *Drosophila*) to the Orc4 active site. Orc5 itself has a canonical Walker A motif in most eukaryotes but lacks a canonical Walker B motif and a sensor II residue, and its partner Orc3 provides no arginine finger. These features fit biochemical data showing that Orc5 binds ATP but does not hydrolyse it. ATPγS density was seen in the nucleotide-binding clefts of Orc1, Orc4 and Orc5 [bleichert-2015-orc-crystal-structure]. In contrast to the tight Orc4·Orc5 interface, the Orc5·Orc3 interface is relatively open. This breaks the clean helical symmetry of a DnaA-type filament and gives ORC a "cracked ring" shape reminiscent of clamp loaders [bleichert-2015-orc-crystal-structure]. Earlier electron microscopy had already shown that ORC changes conformation depending on nucleotide, and that the position of Orc5 defines the DnaA-like helical core of the complex [clarey-2006-orc-dnaa-core].

The crystal structure of the human ORC1/4/5 "motor module", fitted into a cryo-EM map of ORC1–5, shows the mammalian nucleotide sites in detail [tocilj-2017-human-orc-active-form]. ORC1, ORC4 and ORC5 have the same three-domain organization: a RecA fold, an α-helical lid and a winged-helix domain. Together they form a lobe arranged like the subunits of DNA polymerase clamp-loader complexes, while ORC2 and ORC3 form a second lobe. ORC as a whole is a double-layered, shallow corkscrew, and CDC6 fits into the gap between ORC1 and ORC2 to complete the ring [tocilj-2017-human-orc-active-form]. Nucleotide was bound in the ORC5 pocket, recognized by hydrogen bonds from ORC5 Arg226 and Tyr182 and a main-chain carbonyl. However, no neighbouring subunit supplies the arginine finger or the tether that would be needed to complete an ATP hydrolysis site at ORC5 [tocilj-2017-human-orc-active-form]. ORC5 instead contributes catalytic elements to the site it shares with ORC4: ORC5 Arg143 is the arginine finger ("piston") of the ORC4·ORC5 interface, and ORC5 Arg104 is its tether [tocilj-2017-human-orc-active-form]. Mutagenesis confirms that ORC5 is not the catalytic subunit. In the human ORC1–5 complex, a mutation of the ORC5 Walker B aspartate (D125) reduced ATPase activity only slightly, whereas a mutation of the ORC1 Walker B motif (D620A) abolished it [tocilj-2017-human-orc-active-form]. The donkey protein keeps every one of these ORC5 residues (Y182, R226, R143, D125, and Pro139 at the position where ORC1 has a catalytically important tyrosine) except R104, which is discussed in Section 2 [uniprot-A0A9L0JAR4; tocilj-2017-human-orc-active-form].

Cryo-EM structures of human ORC confirm this arrangement in mammals. They show nucleotide sites sandwiched between the ORC1·4, ORC4·5 and ORC5·3 AAA+ interfaces. ORC1·4 and ORC4·5 are canonical ATPase sites, whereas at the more flexible ORC5·3 interface ORC3 does not appear to help coordinate ATP [jaremko-2020-human-orc-cryoem]. The ORC4·ORC5 contact is the second-largest subunit interface in human ORC, burying about 2,700 Å² [jaremko-2020-human-orc-cryoem]. In the ORC2–5 sub-complex, which lacks ORC1, the winged-helix domain of ORC2 blocks the central DNA-binding channel; ORC2 contacts ORC5 directly through hydrogen bonds to ORC5 Asp132 and Glu134 [cheng-2020-human-orc-assembly]. Among ORC1–5, only ORC1, ORC4 and ORC5 contain functional AAA+ nucleotide-binding domains; ORC2 and ORC3 retain only RecA-like subdomains [cheng-2020-human-orc-assembly]. Cheng and colleagues also found that each lid subdomain, including the ORC5 lid, moves with the RecA domain of its neighbour rather than with its own. This coupling means that ORC5 links conformational changes across the ring [cheng-2020-human-orc-assembly]. Jaremko and colleagues identified a hinge at the ORC5·ORC3 interface that lets the ORC2·3 module (together with the ORC5 WH domain) rotate by about 22° away from the "ORC1·4·5 motor module". They propose that this twisting and pinching motion opens the ring so that DNA can enter [jaremko-2020-human-orc-cryoem]. The *Drosophila* structures likewise suggest that flexibility at the Orc3/Orc5 interface helps DNA enter ORC's channel by transiently widening the gap between Orc1 and Orc2 [schmidt-2020-metazoan-orc-dna].

## 4. Biochemical Function: ATP Binding Drives ORC Assembly and Stability

ORC5 has no known catalytic activity. Its key molecular property is nucleotide binding, and the clearest experimental evidence for what this binding does comes from mutating the Walker A motif. In budding yeast, the *orc5-A* allele (Walker A K43E) made cells temperature-sensitive and caused them to accumulate with nearly 2C DNA content. At the restrictive temperature all ORC subunits gradually disappeared. Overproducing Orc4, but not other subunits, specifically rescued the defect, whereas Orc4 overproduction did not rescue *orc5-1* (L331P), whose mutation lies outside the ATP-binding motif [takahashi-2004-orc5-walkerA]. A follow-up study showed that in *orc5-A* cells ORC is destroyed by the proteasome, and that blocking the proteasome restores cell-cycle progression. Orc5 interacts preferentially with Orc4, through the N-terminal region of Orc5 and the C-terminal region of Orc4, and the Walker A mutation weakens this interaction [makise-2007-orc5-walkerA-degradation]. The authors concluded that ATP binding to Orc5 is needed for its efficient interaction with Orc4 and thus for ORC stability [makise-2007-orc5-walkerA-degradation].

Studies of the human complex reached the same conclusion. Recombinant human ORC assembles in vitro only when ATP can bind. Mutating the ATP-binding sites of ORC4 or ORC5 impairs assembly, whereas ATP binding by ORC1 is not required [siddiqui-2007-atp-dependent-assembly]. This fits the observation that human ORC2–5 forms a stable core: the C-terminal region of ORC3 is needed to bring ORC4 and ORC5 into it, while ORC1 and ORC6 associate only labilely [dhar-2001-human-orc-architecture]. Structural work notes that the ORC4·5 and ORC5·3 interfaces stay intact while the ORC1·4 site opens and closes, and suggests that this stability may follow from their inability to hydrolyse ATP [jaremko-2020-human-orc-cryoem]. Taken together, the evidence suggests a division of labour within the ring. ORC1, partnered with ORC4, is the ATPase whose hydrolysis cycle drives helicase loading. ORC5 uses bound ATP as a structural cofactor that holds the ORC4·ORC5 module together [siddiqui-2007-atp-dependent-assembly; bleichert-2015-orc-crystal-structure; jaremko-2020-human-orc-cryoem].

## 5. Role in Replication Origin Recognition and MCM2–7 Helicase Loading

ORC binds replication origins and, together with CDC6 and CDT1, loads the MCM2–7 helicase as an inactive double hexamer around DNA in G1 phase. This is the licensing step, and the loaded helicase is activated in S phase [bell-2016-chromosome-duplication-yeast; bleichert-2017-replication-initiation-review]. ORC5 contributes to several distinct steps in this pathway.

The first step is DNA engagement. In the 3 Å structure of yeast ORC bound to origin DNA, ORC encircles the duplex and bends it at the ACS and B1 elements. Basic-patch motifs from Orc2 and Orc5 insert into the major and minor grooves of the B1 element, where they contact bases and bend the DNA [li-2018-orc-dna-structure]. Yeast Orc5 also carries a β-hairpin loop with several positively charged residues that reach into the DNA major groove. Human ORC5 has a corresponding β-hairpin, with H398 lying close to DNA in a structure of ORC bound to endogenous DNA [jaremko-2020-human-orc-cryoem]. In metazoans, however, ORC1 and ORC4 provide the main DNA-binding site. *Drosophila* Orc5 contacts the DNA backbone in an unusual way, through basic side chains on helix H2 of its WH fold. A triple mutation of those residues (K341A/K344A/R345A) lowers ORC's affinity for DNA only two- to three-fold, and the Orc5 initiation-specific motif does not touch the duplex [schmidt-2020-metazoan-orc-dna]. *Drosophila* Orc5 also lacks a yeast-specific loop insertion in its WH domain, which may partly explain why metazoan ORC bends DNA less and depends less on DNA sequence than budding-yeast ORC does [schmidt-2020-metazoan-orc-dna]. Budding yeast is unusual in having sequence-specific origins, a feature that co-evolved with ORC-dependent silencing [hu-2020-origin-specification-evolution]. Donkey ORC5, like other mammalian ORC5 proteins, is therefore expected to help hold DNA in the ring and remodel it, rather than to read a specific origin sequence [schmidt-2020-metazoan-orc-dna; jaremko-2020-human-orc-cryoem].

The second step is the helicase-loading intermediate. In the 3.9 Å structure of the yeast ORC–Cdc6–Cdt1–Mcm2-7 (OCCM) complex on DNA, nucleotide was bound at the Orc4–Orc5 and Orc5–Orc3 interfaces. Orc1, Orc4, Orc5 and Cdc6, the subunits that bind ATP, form a right-handed spiral around the DNA, much as the AAA+ subunits of RFC clamp loaders do [yuan-2017-occm-structure]. ORC5 also contacts MCM2–7 directly. The Orc5 AAA-lid touches the Mcm6 WH domain, which is itself reached by the Cdt1 C-terminal domain, and the Orc5 WH domain binds the Mcm2 AAA+ fold. Orc1, Orc4 and Orc5 thus form a tight interface with Mcm4, Mcm6 and Mcm2 [yuan-2017-occm-structure]. These findings agree with the earlier conclusion, drawn from the *Drosophila* crystal structure, that ORC engages MCM2–7 through its winged-helix face [bleichert-2015-orc-crystal-structure; bell-2016-chromosome-duplication-yeast]. Single-molecule fluorescence experiments with yeast proteins show that the double hexamer is built by loading one Mcm2–7 complex after another. Each loading event involves its own Cdc6 and Cdt1 molecules, but a single ORC molecule directs the loading of both helicases in a double hexamer [ticau-2015-single-molecule-licensing]. Because ORC5 is a stable, ATP-bound part of the ORC ring, it is presumably present throughout both loading events, but no study has yet resolved ORC5's specific contribution to the second one. Recent side-by-side comparisons of yeast and human ORC structures conclude that the two species use broadly shared licensing strategies that differ in detail [tye-2023-orc-review].

Genetic data support a requirement for ORC5 in replication across eukaryotes. Yeast *orc5* mutants arrest the cell cycle and lose plasmids in an origin-dependent manner [loo-1995-orc-silencing]. A fission yeast *orc5* allele is defective in replication initiation, and execution-point analysis showed that ORC acts before metaphase to prepare the next cycle's initiation [kato-2008-spombe-orc5]. *Drosophila Orc5* mutants die as late larvae, with fewer S-phase cells, metaphase arrest and abnormally condensed chromosomes [pflumm-2001-orc-mutants-metaphase]. In human cells, overexpressing an ORC3 fragment that disrupts the ORC2–5 core blocks cells in G1 [dhar-2001-human-orc-architecture]. An important caveat comes from engineered human cancer cell lines. HCT116 cells survive a mutation of the ORC5 start codon that leaves ORC5 undetectable; any product initiated from an internal methionine would lack about 80% of the AAA+ domain, including the Walker A motif. These cells load MCM2–7 onto chromatin normally and fire a normal number of origins. Cells lacking both ORC5 and ORC2 are also viable, even though ORC1, ORC3 and ORC4 are destabilized [shibata-2020-orc5-orc2-absent]. The same group earlier showed that ORC1- or ORC2-null cells become dependent on CDC6 [shibata-2016-orc-dispensable]. These results show that some transformed human cells can license origins with a crippled ORC, or by an ORC-independent route. They do not overturn the canonical role of ORC5 established by biochemistry and by genetics in model organisms, but they show that how strictly ORC5 is required can depend on cellular context [shibata-2020-orc5-orc2-absent; shibata-2016-orc-dispensable].

## 6. Subcellular Localization and Cell-Cycle Dynamics

ORC5 works in the nucleus and on chromatin. The human orthologue is annotated, on experimental evidence, to the nucleus and to chromosomes [uniprot-O43913-human-ORC5], and the donkey entry carries an electronically inferred nuclear localization [uniprot-A0A9L0JAR4]. When human ORC5 was first characterized, most of it was found in an insoluble nuclear fraction, whereas ORC1, ORC2 and ORC4 extracted more readily [quintana-1998-orc5l]. Across the human cell cycle, ORC2–5 is present at nearly constant levels as a complex. When ORC1 accumulates in G1, it recruits ORC2–5 to nuclease-insoluble nuclear structures, and this recruitment is needed for MCM loading. ORC1 is then degraded in S phase [ohta-2003-orc1-cycle]. Human ORC is assembled and disassembled with each cell cycle, coming apart as cells move through S phase [siddiqui-2007-atp-dependent-assembly]. This cycle is consistent with the ORC5-dependent stability of the ORC2–5 core described above. Chromatin-bound ORC5 is also the form targeted by OBI1 ubiquitylation in S phase (Section 7) [coulombe-2019-obi1]. At the tissue level, human ORC5 transcripts are abundant in proliferative tissues such as testis and colon mucosa, and also in spleen, ovary and prostate [quintana-1998-orc5l].

## 7. Regulation and Non-Canonical Roles

**Ubiquitin signalling in origin firing.** A proteomic survey of the human pre-replicative complex identified OBI1 (C13orf7/RNF219), an ORC-associated E3 ubiquitin ligase. OBI1 attaches single ubiquitins at multiple sites (multi-mono-ubiquitylation) on a subset of chromatin-bound ORC3 and ORC5 during S phase [coulombe-2019-obi1]. Silencing OBI1, or expressing ORC3/ORC5 mutants that cannot be ubiquitylated (lysine-less versions), reduces formation of the CMG helicase and origin firing without affecting pre-RC assembly. The ORC5 ubiquitylation therefore acts after licensing and helps decide which licensed origins fire [coulombe-2019-obi1]. The Xenopus OBI1 homologue can also ubiquitylate human ORC5, which suggests the pathway is conserved among vertebrates [coulombe-2019-obi1]. It is therefore likely, though not tested, to operate in equids.

**Chromatin opening.** When human ORC5 is tethered to a chromatin locus, it causes large-scale chromatin decondensation, mainly in G1. Other ORC subunits do not have this effect. ORC5 associates with the histone acetyltransferase GCN5 (KAT2A), which strengthens the effect, and loss of ORC5 lowers histone H3 acetylation at origins [giri-2016-orc5-chromatin-decondensation]. The authors propose that ORC5 opens local chromatin so that the pre-RC can assemble [giri-2016-orc5-chromatin-decondensation].

**Heterochromatin, silencing and cohesion.** Human ORC subunits associate with HP1α/β heterochromatic foci. Depleting ORC5 (like depleting ORC1) caused HP1α to be distributed abnormally, specifically at pericentric heterochromatin around nucleoli [prasanth-2010-orc-hp1-heterochromatin]. In budding yeast, *ORC5* alleles separate the replication and HMR silencing functions, and the two classes of allele complement each other [dillin-1997-orc5-silencing]. In fission yeast, an *orc5* allele weakens sister-chromatid cohesion by impairing loading of the cohesin subunit Rad21 [kato-2008-spombe-orc5]. These functions vary between lineages, and the yeast silencing role in particular co-evolved with sequence-specific origins [hu-2020-origin-specification-evolution]. Their relevance to mammals, and hence to the donkey, should be treated as provisional.

**Disease associations in humans.** Unlike *ORC1*, *ORC4* and *ORC6*, *ORC5* has not been reported among the genes mutated in Meier-Gorlin syndrome, a primordial dwarfism caused by defects in origin licensing; that syndrome involves mutations in *ORC1*, *ORC4*, *ORC6*, *CDC6* and *CDT1* [shen-2013-orc-human-diseases]. Human *ORC5* lies in the 7q22 region that is often deleted in uterine leiomyomas, acute myeloid leukaemia and myelodysplastic syndromes [quintana-1998-orc5l]. However, sequencing of the remaining *ORC5* allele in AML or MDS patients with such deletions found no mutations [shen-2013-orc-human-diseases]. These links therefore remain associations based on chromosomal location, with no shown causal role for ORC5.

## 8. Conclusions

The evidence is consistent, and it supports annotating donkey ORC5 (A0A9L0JAR4) as a nuclear, chromatin-associated structural subunit of the origin recognition complex. ORC5's molecular function is ATP binding without hydrolysis, through a conserved Walker A motif, at the ORC4·ORC5 interface, where it also supplies an arginine finger to the ORC4 site [bleichert-2015-orc-crystal-structure]. This ATP binding is needed to assemble and stabilize the ORC ring [siddiqui-2007-atp-dependent-assembly; takahashi-2004-orc5-walkerA; makise-2007-orc5-walkerA-degradation]. In the biological process of DNA replication initiation, ORC5 helps encircle and remodel origin DNA and contacts MCM2–7 during double-hexamer loading [li-2018-orc-dna-structure; yuan-2017-occm-structure; schmidt-2020-metazoan-orc-dna]. A hinge at the ORC5·ORC3 interface probably allows DNA to enter the ring [jaremko-2020-human-orc-cryoem]. ORC5 is also a target of OBI1-dependent ubiquitylation that promotes origin firing [coulombe-2019-obi1]. Appropriate GO-style annotations by orthology would be the nuclear origin recognition complex (cellular component), ATP binding and DNA replication origin binding (molecular function, as part of the complex), and DNA replication initiation and pre-replicative complex assembly (biological process). There is currently no direct experimental evidence for any of this in the donkey; all annotations rest on strong sequence conservation (about 96% identity to human ORC5) and on experiments in human, *Drosophila* and yeast systems.

## Open Questions

Several questions remain open. The first concerns the donkey protein itself. Its 20-residue C-terminal segment differs from the conserved mammalian C-terminus, and it should be checked against donkey RNA-seq and against horse (*Equus caballus*) ORC5. That comparison would show whether the segment is a real equid-specific exon, an alternative isoform or an error in the gene model, and whether it affects the ORC5 winged-helix region that contacts DNA and MCM2–7 [uniprot-A0A9L0JAR4; schmidt-2020-metazoan-orc-dna]. The horse gene models suggest that equids use two alternative ORC5 C-termini, one conserved and one equid-specific; donkey transcriptome data could confirm whether a canonical-tail isoform is expressed, and in which tissues [uniprot-ORC5-horse-mouse-cow]. The Cys104 residue of the donkey model, at a position where human ORC5 has the tether arginine of the ORC4·ORC5 site, should be confirmed by resequencing [tocilj-2017-human-orc-active-form]. The equid locus could also be searched for an ORC5T-like alternative transcript, which in humans produces an ORC5 that binds ORC4 but not ORC2 [quintana-1998-orc5l].

The other questions are mechanistic and apply to mammals generally. It is not known how ATP binding at the ORC4·ORC5 site is coupled to the ORC1 ATPase cycle during MCM loading, or whether nucleotide exchange at ORC5 ever happens in vivo, given that ORC5 cannot hydrolyse ATP [bleichert-2015-orc-crystal-structure; jaremko-2020-human-orc-cryoem]. The ORC5 lysines ubiquitylated by OBI1 have not been identified, nor is it known how ubiquitylated ORC5 promotes CMG formation [coulombe-2019-obi1]. Some cancer cells survive without detectable ORC5; whether untransformed or primary cells can do so remains open, as does the identity of the ORC-independent licensing route [shibata-2020-orc5-orc2-absent; shibata-2016-orc-dispensable]. The chromatin-opening activity of ORC5 depends on GCN5 [giri-2016-orc5-chromatin-decondensation], but whether it determines where origins are positioned in mammalian genomes has not been tested. Finally, a structure of mammalian ORC within an OCCM or MCM double-hexamer loading intermediate would show whether the ORC5 lid and WH contacts with MCM2 and MCM6 seen in yeast are conserved [yuan-2017-occm-structure].

## References

- **[bell-2016-chromosome-duplication-yeast]** Bell SP, Labib K (2016). Chromosome Duplication in Saccharomyces cerevisiae. *Genetics* 203:1027-67. PMID: 27384026; PMCID: PMC4937469; DOI: 10.1534/genetics.115.186452 (https://doi.org/10.1534/genetics.115.186452); https://pubmed.ncbi.nlm.nih.gov/27384026/
- **[bleichert-2015-orc-crystal-structure]** Bleichert F, Botchan MR, Berger JM (2015). Crystal structure of the eukaryotic origin recognition complex. *Nature* 519:321-6. PMID: 25762138; PMCID: PMC4368505; DOI: 10.1038/nature14239 (https://doi.org/10.1038/nature14239); https://pubmed.ncbi.nlm.nih.gov/25762138/
- **[bleichert-2017-replication-initiation-review]** Bleichert F, Botchan MR, Berger JM (2017). Mechanisms for initiating cellular DNA replication. *Science (New York, N.Y.)* 355. PMID: 28209641; DOI: 10.1126/science.aah6317 (https://doi.org/10.1126/science.aah6317); https://pubmed.ncbi.nlm.nih.gov/28209641/
- **[cheng-2020-human-orc-assembly]** Cheng J, Li N, Wang X, Hu J, Zhai Y, Gao N (2020). Structural insight into the assembly and conformational activation of human origin recognition complex. *Cell discovery* 6:88. PMID: 33298899; PMCID: PMC7684300; DOI: 10.1038/s41421-020-00232-3 (https://doi.org/10.1038/s41421-020-00232-3); https://pubmed.ncbi.nlm.nih.gov/33298899/
- **[clarey-2006-orc-dnaa-core]** Clarey MG, Erzberger JP, Grob P, Leschziner AE, Berger JM, Nogales E et al. (2006). Nucleotide-dependent conformational changes in the DnaA-like core of the origin recognition complex. *Nature structural & molecular biology* 13:684-90. PMID: 16829958; DOI: 10.1038/nsmb1121 (https://doi.org/10.1038/nsmb1121); https://pubmed.ncbi.nlm.nih.gov/16829958/
- **[coulombe-2019-obi1]** Coulombe P, Nassar J, Peiffer I, Stanojcic S, Sterkers Y, Delamarre A et al. (2019). The ORC ubiquitin ligase OBI1 promotes DNA replication origin firing. *Nature communications* 10:2426. PMID: 31160578; PMCID: PMC6547688; DOI: 10.1038/s41467-019-10321-x (https://doi.org/10.1038/s41467-019-10321-x); https://pubmed.ncbi.nlm.nih.gov/31160578/
- **[dhar-2001-human-orc-architecture]** Dhar SK, Delmolino L, Dutta A (2001). Architecture of the human origin recognition complex. *The Journal of biological chemistry* 276:29067-71. PMID: 11395502; DOI: 10.1074/jbc.M103078200 (https://doi.org/10.1074/jbc.M103078200); https://pubmed.ncbi.nlm.nih.gov/11395502/
- **[dillin-1997-orc5-silencing]** Dillin A, Rine J (1997). Separable functions of ORC5 in replication initiation and silencing in Saccharomyces cerevisiae. *Genetics* 147:1053-62. PMID: 9383052; PMCID: PMC1208233; DOI: 10.1093/genetics/147.3.1053 (https://doi.org/10.1093/genetics/147.3.1053); https://pubmed.ncbi.nlm.nih.gov/9383052/
- **[giri-2016-orc5-chromatin-decondensation]** Giri S, Chakraborty A, Sathyan KM, Prasanth KV, Prasanth SG (2016). Orc5 induces large-scale chromatin decondensation in a GCN5-dependent manner. *Journal of cell science* 129:417-29. PMID: 26644179; PMCID: PMC4732289; DOI: 10.1242/jcs.178889 (https://doi.org/10.1242/jcs.178889); https://pubmed.ncbi.nlm.nih.gov/26644179/
- **[hu-2020-origin-specification-evolution]** Hu Y, Tareen A, Sheu YJ, Ireland WT, Speck C, Li H et al. (2020). Evolution of DNA replication origin specification and gene silencing mechanisms. *Nature communications* 11:5175. PMID: 33056978; PMCID: PMC7560902; DOI: 10.1038/s41467-020-18964-x (https://doi.org/10.1038/s41467-020-18964-x); https://pubmed.ncbi.nlm.nih.gov/33056978/
- **[ishiai-1997-orc5-homologues]** Ishiai M, Dean FB, Okumura K, Abe M, Moon KY, Amin AA et al. (1997). Isolation of human and fission yeast homologues of the budding yeast origin recognition complex subunit ORC5: human homologue (ORC5L) maps to 7q22. *Genomics* 46:294-8. PMID: 9417919; DOI: 10.1006/geno.1997.5003 (https://doi.org/10.1006/geno.1997.5003); https://pubmed.ncbi.nlm.nih.gov/9417919/
- **[jaremko-2020-human-orc-cryoem]** Jaremko MJ, On KF, Thomas DR, Stillman B, Joshua-Tor L (2020). The dynamic nature of the human origin recognition complex revealed through five cryoEM structures. *eLife* 9. PMID: 32808929; PMCID: PMC7467728; DOI: 10.7554/eLife.58622 (https://doi.org/10.7554/eLife.58622); https://pubmed.ncbi.nlm.nih.gov/32808929/
- **[kato-2008-spombe-orc5]** Kato H, Matsunaga F, Miyazaki S, Yin L, D'Urso G, Tanaka K et al. (2008). Schizosaccharomyces pombe Orc5 plays multiple roles in the maintenance of genome stability throughout the cell cycle. *Cell cycle (Georgetown, Tex.)* 7:1085-96. PMID: 18414064; https://pubmed.ncbi.nlm.nih.gov/18414064/
- **[li-2018-orc-dna-structure]** Li N, Lam WH, Zhai Y, Cheng J, Cheng E, Zhao Y et al. (2018). Structure of the origin recognition complex bound to DNA replication origin. *Nature* 559:217-222. PMID: 29973722; DOI: 10.1038/s41586-018-0293-x (https://doi.org/10.1038/s41586-018-0293-x); https://pubmed.ncbi.nlm.nih.gov/29973722/
- **[loo-1995-orc-silencing]** Loo S, Fox CA, Rine J, Kobayashi R, Stillman B, Bell S (1995). The origin recognition complex in silencing, cell cycle progression, and DNA replication. *Molecular biology of the cell* 6:741-56. PMID: 7579692; PMCID: PMC301233; DOI: 10.1091/mbc.6.6.741 (https://doi.org/10.1091/mbc.6.6.741); https://pubmed.ncbi.nlm.nih.gov/7579692/
- **[makise-2007-orc5-walkerA-degradation]** Makise M, Takahashi N, Matsuda K, Yamairi F, Suzuki K, Tsuchiya T et al. (2007). Mechanism for the degradation of origin recognition complex containing Orc5p with a defective Walker A motif and its suppression by over-production of Orc4p in yeast cells. *The Biochemical journal* 402:397-403. PMID: 17107343; PMCID: PMC1798425; DOI: 10.1042/BJ20060841 (https://doi.org/10.1042/BJ20060841); https://pubmed.ncbi.nlm.nih.gov/17107343/
- **[ohta-2003-orc1-cycle]** Ohta S, Tatsumi Y, Fujita M, Tsurimoto T, Obuse C (2003). The ORC1 cycle in human cells: II. Dynamic changes in the human ORC complex during the cell cycle. *The Journal of biological chemistry* 278:41535-40. PMID: 12909626; DOI: 10.1074/jbc.M307535200 (https://doi.org/10.1074/jbc.M307535200); https://pubmed.ncbi.nlm.nih.gov/12909626/
- **[pflumm-2001-orc-mutants-metaphase]** Pflumm MF, Botchan MR (2001). Orc mutants arrest in metaphase with abnormally condensed chromosomes. *Development (Cambridge, England)* 128:1697-707. PMID: 11290306; DOI: 10.1242/dev.128.9.1697 (https://doi.org/10.1242/dev.128.9.1697); https://pubmed.ncbi.nlm.nih.gov/11290306/
- **[prasanth-2010-orc-hp1-heterochromatin]** Prasanth SG, Shen Z, Prasanth KV, Stillman B (2010). Human origin recognition complex is essential for HP1 binding to chromatin and heterochromatin organization. *Proceedings of the National Academy of Sciences of the United States of America* 107:15093-8. PMID: 20689044; PMCID: PMC2930523; DOI: 10.1073/pnas.1009945107 (https://doi.org/10.1073/pnas.1009945107); https://pubmed.ncbi.nlm.nih.gov/20689044/
- **[quintana-1998-orc5l]** Quintana DG, Thome KC, Hou ZH, Ligon AH, Morton CC, Dutta A (1998). ORC5L, a new member of the human origin recognition complex, is deleted in uterine leiomyomas and malignant myeloid diseases. *The Journal of biological chemistry* 273:27137-45. PMID: 9765232; DOI: 10.1074/jbc.273.42.27137 (https://doi.org/10.1074/jbc.273.42.27137); https://pubmed.ncbi.nlm.nih.gov/9765232/
- **[schmidt-2020-metazoan-orc-dna]** Schmidt JM, Bleichert F (2020). Structural mechanism for replication origin binding and remodeling by a metazoan origin recognition complex and its co-loader Cdc6. *Nature communications* 11:4263. PMID: 32848132; PMCID: PMC7450096; DOI: 10.1038/s41467-020-18067-7 (https://doi.org/10.1038/s41467-020-18067-7); https://pubmed.ncbi.nlm.nih.gov/32848132/
- **[shen-2013-orc-human-diseases]** Shen Z (2013). The origin recognition complex in human diseases. *Bioscience reports* 33. PMID: 23662735; PMCID: PMC3679595; DOI: 10.1042/BSR20130036 (https://doi.org/10.1042/BSR20130036); https://pubmed.ncbi.nlm.nih.gov/23662735/
- **[shibata-2016-orc-dispensable]** Shibata E, Kiran M, Shibata Y, Singh S, Kiran S, Dutta A (2016). Two subunits of human ORC are dispensable for DNA replication and proliferation. *eLife* 5. PMID: 27906128; PMCID: PMC5245961; DOI: 10.7554/eLife.19084 (https://doi.org/10.7554/eLife.19084); https://pubmed.ncbi.nlm.nih.gov/27906128/
- **[shibata-2020-orc5-orc2-absent]** Shibata E, Dutta A (2020). A human cancer cell line initiates DNA replication normally in the absence of ORC5 and ORC2 proteins. *The Journal of biological chemistry* 295:16949-16959. PMID: 32989049; PMCID: PMC7863895; DOI: 10.1074/jbc.RA120.015450 (https://doi.org/10.1074/jbc.RA120.015450); https://pubmed.ncbi.nlm.nih.gov/32989049/
- **[siddiqui-2007-atp-dependent-assembly]** Siddiqui K, Stillman B (2007). ATP-dependent assembly of the human origin recognition complex. *The Journal of biological chemistry* 282:32370-83. PMID: 17716973; DOI: 10.1074/jbc.M705905200 (https://doi.org/10.1074/jbc.M705905200); https://pubmed.ncbi.nlm.nih.gov/17716973/
- **[takahashi-2004-orc5-walkerA]** Takahashi N, Yamaguchi Y, Yamairi F, Makise M, Takenaka H, Tsuchiya T et al. (2004). Analysis on origin recognition complex containing Orc5p with defective Walker A motif. *The Journal of biological chemistry* 279:8469-77. PMID: 14625297; DOI: 10.1074/jbc.M305531200 (https://doi.org/10.1074/jbc.M305531200); https://pubmed.ncbi.nlm.nih.gov/14625297/
- **[ticau-2015-single-molecule-licensing]** Ticau S, Friedman LJ, Ivica NA, Gelles J, Bell SP (2015). Single-molecule studies of origin licensing reveal mechanisms ensuring bidirectional helicase loading. *Cell* 161:513-525. PMID: 25892223; PMCID: PMC4445235; DOI: 10.1016/j.cell.2015.03.012 (https://doi.org/10.1016/j.cell.2015.03.012); https://pubmed.ncbi.nlm.nih.gov/25892223/
- **[tocilj-2017-human-orc-active-form]** Tocilj A, On KF, Yuan Z, Sun J, Elkayam E, Li H et al. (2017). Structure of the active form of human origin recognition complex and its ATPase motor module. *eLife* 6. PMID: 28112645; PMCID: PMC5291709; DOI: 10.7554/eLife.20818 (https://doi.org/10.7554/eLife.20818); https://pubmed.ncbi.nlm.nih.gov/28112645/
- **[tugal-1998-orc4-orc5-related]** Tugal T, Zou-Yang XH, Gavin K, Pappin D, Canas B, Kobayashi R et al. (1998). The Orc4p and Orc5p subunits of the Xenopus and human origin recognition complex are related to Orc1p and Cdc6p. *The Journal of biological chemistry* 273:32421-9. PMID: 9829972; DOI: 10.1074/jbc.273.49.32421 (https://doi.org/10.1074/jbc.273.49.32421); https://pubmed.ncbi.nlm.nih.gov/9829972/
- **[tye-2023-orc-review]** Tye BK, Zhai Y (2023). The Origin Recognition Complex: From Origin Selection to Replication Licensing in Yeast and Humans. *Biology* 13. PMID: 38248444; PMCID: PMC10813338; DOI: 10.3390/biology13010013 (https://doi.org/10.3390/biology13010013); https://pubmed.ncbi.nlm.nih.gov/38248444/
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, Huang J, Sun Y, Min J et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7); https://pubmed.ncbi.nlm.nih.gov/33293529/
- **[yuan-2017-occm-structure]** Yuan Z, Riera A, Bai L, Sun J, Nandi S, Spanos C et al. (2017). Structural basis of Mcm2-7 replicative helicase loading by ORC-Cdc6 and Cdt1. *Nature structural & molecular biology* 24:316-324. PMID: 28191893; PMCID: PMC5503505; DOI: 10.1038/nsmb.3372 (https://doi.org/10.1038/nsmb.3372); https://pubmed.ncbi.nlm.nih.gov/28191893/
- **[uniprot-A0A9L0JAR4]** UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0JAR4 (ORC5, *Equus asinus*), entry version 15. https://rest.uniprot.org/uniprotkb/A0A9L0JAR4.txt
- **[uniprot-O43913-human-ORC5]** UniProt Consortium. UniProtKB/Swiss-Prot entry O43913 (ORC5_HUMAN). https://rest.uniprot.org/uniprotkb/O43913.txt
- **[uniprot-ORC5-horse-mouse-cow]** UniProt Consortium. UniProtKB search for ORC5 in *Equus caballus*, *Mus musculus* and *Bos taurus* (entries incl. A0A3Q2KSP7, A0A3Q2IA91, F6V340, Q9WUV0). https://rest.uniprot.org/uniprotkb/search?query=gene_exact:ORC5+AND+(organism_id:9796+OR+organism_id:10090+OR+organism_id:9913)&format=fasta


## Citations

1. _metadata.json
2. bell-2016-chromosome-duplication-yeast-abstract.md
3. bell-2016-chromosome-duplication-yeast-fulltext.txt
4. bell-2016-chromosome-duplication-yeast-summary.md
5. bleichert-2015-orc-crystal-structure-abstract.md
6. bleichert-2015-orc-crystal-structure-fulltext.txt
7. bleichert-2015-orc-crystal-structure-summary.md
8. bleichert-2017-replication-initiation-review-abstract.md
9. bleichert-2017-replication-initiation-review-summary.md
10. cheng-2020-human-orc-assembly-abstract.md
11. cheng-2020-human-orc-assembly-fulltext.txt
12. cheng-2020-human-orc-assembly-summary.md
13. clarey-2006-orc-dnaa-core-abstract.md
14. clarey-2006-orc-dnaa-core-summary.md
15. coulombe-2019-obi1-abstract.md
16. coulombe-2019-obi1-fulltext.txt
17. coulombe-2019-obi1-summary.md
18. dhar-2001-human-orc-architecture-abstract.md
19. dhar-2001-human-orc-architecture-summary.md
20. dillin-1997-orc5-silencing-abstract.md
21. dillin-1997-orc5-silencing-summary.md
22. giri-2016-orc5-chromatin-decondensation-abstract.md
23. giri-2016-orc5-chromatin-decondensation-summary.md
24. hu-2020-origin-specification-evolution-abstract.md
25. hu-2020-origin-specification-evolution-fulltext.txt
26. hu-2020-origin-specification-evolution-summary.md
27. ishiai-1997-orc5-homologues-abstract.md
28. ishiai-1997-orc5-homologues-summary.md
29. jaremko-2020-human-orc-cryoem-abstract.md
30. jaremko-2020-human-orc-cryoem-fulltext.txt
31. jaremko-2020-human-orc-cryoem-summary.md
32. kato-2008-spombe-orc5-abstract.md
33. kato-2008-spombe-orc5-summary.md
34. li-2018-orc-dna-structure-abstract.md
35. li-2018-orc-dna-structure-summary.md
36. loo-1995-orc-silencing-abstract.md
37. loo-1995-orc-silencing-summary.md
38. makise-2007-orc5-walkerA-degradation-abstract.md
39. makise-2007-orc5-walkerA-degradation-summary.md
40. ohta-2003-orc1-cycle-abstract.md
41. ohta-2003-orc1-cycle-summary.md
42. pflumm-2001-orc-mutants-metaphase-abstract.md
43. pflumm-2001-orc-mutants-metaphase-summary.md
44. prasanth-2010-orc-hp1-heterochromatin-abstract.md
45. prasanth-2010-orc-hp1-heterochromatin-summary.md
46. quintana-1998-orc5l-abstract.md
47. quintana-1998-orc5l-summary.md
48. schmidt-2020-metazoan-orc-dna-abstract.md
49. schmidt-2020-metazoan-orc-dna-fulltext.txt
50. schmidt-2020-metazoan-orc-dna-summary.md
51. shen-2013-orc-human-diseases-abstract.md
52. shen-2013-orc-human-diseases-fulltext.txt
53. shen-2013-orc-human-diseases-summary.md
54. shibata-2016-orc-dispensable-abstract.md
55. shibata-2016-orc-dispensable-fulltext.txt
56. shibata-2016-orc-dispensable-summary.md
57. shibata-2020-orc5-orc2-absent-abstract.md
58. shibata-2020-orc5-orc2-absent-summary.md
59. siddiqui-2007-atp-dependent-assembly-abstract.md
60. siddiqui-2007-atp-dependent-assembly-summary.md
61. takahashi-2004-orc5-walkerA-abstract.md
62. takahashi-2004-orc5-walkerA-summary.md
63. ticau-2015-single-molecule-licensing-abstract.md
64. ticau-2015-single-molecule-licensing-summary.md
65. tocilj-2017-human-orc-active-form-abstract.md
66. tocilj-2017-human-orc-active-form-fulltext.txt
67. tocilj-2017-human-orc-active-form-summary.md
68. tugal-1998-orc4-orc5-related-abstract.md
69. tugal-1998-orc4-orc5-related-summary.md
70. tye-2023-orc-review-abstract.md
71. tye-2023-orc-review-fulltext.txt
72. tye-2023-orc-review-summary.md
73. uniprot-A0A9L0JAR4-entry.txt
74. uniprot-A0A9L0JAR4-sequence.fasta
75. uniprot-A0A9L0JAR4-summary.md
76. uniprot-O43913-human-ORC5-entry.txt
77. uniprot-O43913-human-ORC5-summary.md
78. uniprot-O43913-sequence.fasta
79. uniprot-ORC5-horse-mouse-cow-sequences.fasta
80. uniprot-ORC5-horse-mouse-cow-summary.md
81. wang-2020-donkey-genomes-abstract.md
82. wang-2020-donkey-genomes-fulltext.txt
83. wang-2020-donkey-genomes-summary.md
84. yuan-2017-occm-structure-abstract.md
85. yuan-2017-occm-structure-fulltext.txt
86. yuan-2017-occm-structure-summary.md
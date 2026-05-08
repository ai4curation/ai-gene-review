# secF (PSEAE) -- Research Notes

## Gene Overview

secF encodes the protein translocase subunit SecF (UniProt Q9HXI2) in Pseudomonas aeruginosa PAO1 (ordered locus PA3820). SecF is a multi-pass inner membrane protein that is part of the SecDF accessory complex of the general secretory (Sec) pathway. It enhances protein translocation across the cytoplasmic membrane by harnessing the proton motive force (PMF).

## Key Literature Findings

### Genomic context

The secF gene was identified as part of the P. aeruginosa PAO1 complete genome sequence [PMID:10984043 "Complete genome sequence of Pseudomonas aeruginosa PAO1, an opportunistic pathogen"]. It is encoded at locus PA3820.

### SecDF structure and function (landmark studies in E. coli and T. thermophilus)

The crystal structure of SecDF from Thermus thermophilus was determined at 3.3 A resolution, revealing a pseudo-symmetrical 12-helix transmembrane domain belonging to the RND superfamily and two major periplasmic domains (P1 and P4) [PMID:21562494 "Structure and function of a membrane component SecDF that enhances protein export", "we determined the crystal structure of Thermus thermophilus SecDF at 3.3 A resolution, revealing a pseudo-symmetrical, 12-helix transmembrane domain belonging to the RND superfamily and two major periplasmic domains, P1 and P4"]. This study showed that SecDF functions as a membrane-integrated chaperone powered by PMF: "we propose that SecDF functions as a membrane-integrated chaperone, powered by proton motive force, to achieve ATP-independent protein translocation" [PMID:21562494].

Critically, Tsukazaki et al. (2011) identified an ATP-independent step of translocation requiring both SecDF and PMF, with conserved Asp and Arg residues at the SecD/SecF transmembrane interface playing essential roles in proton and preprotein movement: "Electrophysiological analyses revealed that SecDF conducts protons in a manner dependent on pH and the presence of an unfolded protein, with conserved Asp and Arg residues at the transmembrane interface between SecD and SecF playing essential roles in the movements of protons and preproteins" [PMID:21562494].

### SecDF as a PMF-driven translocation motor

A review by Tsukazaki (2018) summarized the structural basis for SecDF function: "SecDF is proposed to undergo repeated conformational transitions to pull out the precursor protein from the SecYEG channel into the periplasm. Once SecDF captures the precursor protein on the periplasmic surface, SecDF can complete protein translocation even if SecA function is inactivated by ATP depletion, implying that SecDF is a protein-translocation motor that works independent of SecA" [PMID:29718185 "Structure-based working model of SecDF, a proton-driven bacterial protein translocation factor"].

### I-form crystal structures and proton tunnel

Furukawa et al. (2017) reported I-form structures of SecDF at 2.6-2.8 A resolution, revealing that "SecDF in I form can generate a tunnel that penetrates the transmembrane region and functions as a proton pathway regulated by a conserved Asp residue" [PMID:28467902 "Tunnel Formation Inferred from the I-Form Structures of the Proton-Driven Protein Secretion Motor SecDF"].

### Holo-translocon (HTL) complex

The SecDF-YajC subcomplex associates with SecYEG and YidC to form the holo-translocon (HTL). Schulze et al. (2014) showed that the HTL differs from SecYEG alone: "It is more effective in cotranslational insertion of membrane proteins and the posttranslational secretion of a beta-barreled outer-membrane protein driven by SecA and ATP becomes much more dependent on the proton-motive force" [PMID:24550475 "Membrane protein insertion and proton-motive-force-dependent secretion through the bacterial holo-translocon SecYEG-SecDF-YajC-YidC"].

### Inter-membrane communication via SecDF

Alvira et al. (2020) demonstrated that SecDF's periplasmic domains connect the inner membrane Sec machinery to the outer membrane BAM complex: "the proton-motive force (PMF) across the inner-membrane acts at distinct stages of protein secretion: (1) SecA-driven translocation through SecYEG and (2) communication of conformational changes via SecDF across the periplasm to BAM" [PMID:33146611 "Inter-membrane association of the Sec and BAM translocons for bacterial outer-membrane biogenesis"].

### SecD operon characterization in E. coli

Pogliano and Beckwith (1994) characterized the secD operon in E. coli, establishing that it contains yajC, secD, and secF: "in addition to secD and secF, it contains the upstream gene yajC" and that "there are fewer than 30 SecD and SecF molecules per cell" [PMID:7507921 "Genetic and molecular characterization of the Escherichia coli secD operon and its products"].

### SecD-SecF interaction in P. aeruginosa

Navare et al. (2015) used in vivo chemical cross-linking mass spectrometry to directly demonstrate SecD-SecF interaction in P. aeruginosa cells: "Structures of three membrane proteins, namely, SecD-SecF, OprF, and OprI are predicted using in vivo cross-linked sites" [PMID:25800553 "Probing the protein interaction network of Pseudomonas aeruginosa cells by chemical cross-linking mass spectrometry"]. This is one of the few studies providing direct physical evidence for the SecD-SecF complex in P. aeruginosa specifically.

## Annotation Analysis

### MF annotation concern: protein-transporting ATPase activity (GO:0015450)

The InterPro2GO mapping (GO_REF:0000002) assigns GO:0015450 (protein-transporting ATPase activity) to SecF. This is problematic because SecF itself is NOT an ATPase. The ATPase activity in the Sec pathway belongs to SecA. SecF/SecDF instead uses the proton motive force for its translocation-enhancing function. A more appropriate MF term would be GO:0009977 (proton motive force dependent protein transmembrane transporter activity), as SecDF conducts protons coupled to polypeptide translocation.

### BP annotations

The process annotations (protein transport, protein targeting, protein transport by the Sec complex, intracellular protein transmembrane transport) are all broadly correct. GO:0043952 (protein transport by the Sec complex) is the most specific and informative.

### CC annotations

Plasma membrane (GO:0005886) is correct -- SecF is an integral inner membrane protein. However, the more specific complex term GO:0031522 (cell envelope Sec protein transport complex) would also be appropriate.

## SecF is NOT an ATPase -- it is a PMF-coupled accessory component

This is the key distinction for annotation: SecF (as part of SecDF) does not hydrolyze ATP. It uses the proton motive force to drive conformational changes that pull preproteins through the SecYEG channel. The ATPase activity in the Sec translocase belongs to SecA. SecF contributes to the overall translocase complex activity but does not independently enable protein-transporting ATPase activity.

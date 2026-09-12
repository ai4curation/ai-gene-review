# AGPS (alkylglycerone phosphate synthase) — review notes

UniProt: O00116 (ADAS_HUMAN). Gene: AGPS (a.k.a. AAG5, "aging-associated gene 5").
658 aa precursor; peroxisomal. EC 2.5.1.26.

## Core biology (from local UniProt O00116 and cited primary literature)

- **Enzyme / reaction.** AGPS is alkyldihydroxyacetonephosphate synthase (alkyl-DHAP synthase / alkylglycerone-phosphate synthase). It catalyzes the committed **ether-bond-forming** step of ether-lipid (plasmalogen) biosynthesis: it exchanges the **acyl group of acyl-dihydroxyacetone phosphate (acyl-DHAP) for a long-chain fatty alcohol**, yielding **alkyl-DHAP** (the first O-alkyl ether intermediate) plus the released fatty acid.
  - UniProt FUNCTION: "Catalyzes the exchange of the acyl chain in acyl-dihydroxyacetonephosphate (acyl-DHAP) for a long chain fatty alcohol, yielding the first ether linked intermediate, i.e. alkyl-dihydroxyacetonephosphate (alkyl-DHAP), in the pathway of ether lipid biosynthesis" [file:human/AGPS/AGPS-uniprot.txt].
  - Reaction (Rhea:36171): "a long chain fatty alcohol + a 1-acylglycerone 3-phosphate = a 1-O-alkylglycerone 3-phosphate + a long-chain fatty acid + H(+)"; EC=2.5.1.26 [file:human/AGPS/AGPS-uniprot.txt].
  - [PMID:8399344 "the second enzyme involved in ether phospholipid biosynthesis from dihydroxyacetone phosphate and responsible for glycero-ether bond formation, has been purified from guinea-pig liver."] — original purification (guinea-pig liver ortholog); 65 kDa band, 13,000-fold purification. EC assigned in UniProt with ECO:0000269|PubMed:8399344.
  - [PMID:9553082] — human AGPS characterization; R419H patient mutation abolishes activity ("providing further proof that this substitution is responsible for the inactivity of the enzyme and the phenotype"). Enzyme activity is inhibited by the arginine-modifying agent phenylglyoxal and protected by saturating substrate palmitoyl-DHAP.

- **Cofactor.** FAD-dependent flavoprotein; belongs to the "FAD-binding oxidoreductase/transferase type 4 family" [file:human/AGPS/AGPS-uniprot.txt]. UniProt COFACTOR: Name=FAD (ISS from mouse ortholog P97275). Four FAD-binding regions annotated (residues 234-240, 303-309, 316-319, 368-374). KW: FAD; Flavoprotein.

- **Localization / import.** Peroxisomal enzyme. UniProt SUBCELLULAR LOCATION: "Peroxisome membrane" and "Peroxisome" (ISS from mouse P97275). Imported into peroxisome via a **PTS2** signal in a cleavable N-terminal presequence (TRANSIT 1..58), PEX7-dependent.
  - [PMID:9553082 "Alkyl-dihydroxyacetonephosphate synthase, a peroxisomal enzyme playing a key role in the biosynthesis of ether phospholipids, contains the peroxisomal targeting signal type 2 in a N-terminal cleavable presequence."] Reduced levels in Zellweger/RCDP fibroblasts (defective import → cytoplasmic instability); NALD PTS1-import-deficient patient retains precursor form intraperoxisomally ("in line with an intraperoxisomal localization").
  - [PMID:10415121 "a peroxisomal enzyme involved in the biosynthesis of ether phospholipids, is synthesized with a cleavable N-terminal presequence containing the peroxisomal targeting signal type 2."] The precursor is imported into purified peroxisomes and processed by a cysteine protease (matches Reactome "TYSND1 cleaves peroxisomal proteins"); processing does not change activity. GO CC peroxisome IDA supported here.

- **Quaternary structure / partners.** Homodimer (UniProt SUBUNIT, ISS from P97275). Works together with GNPAT (DHAPAT), which produces acyl-DHAP; GNPAT and AGPS are thought to form a complex on the inner peroxisomal membrane surface. UniProt lists a curated interaction with GORASP1 (Q9BQQ3, GRASP65) with NbExp=7.

- **Disease.** Biallelic AGPS loss-of-function causes **rhizomelic chondrodysplasia punctata type 3 (RCDP3; MIM:600121)** — rhizomelic limb shortening, chondrodysplasia punctata, cataract, severe intellectual disability. Characterized RCDP3 variants: R419H (loss of activity), T309I, L469P, R182Q, E471K, T568M [file:human/AGPS/AGPS-uniprot.txt; PMID:9553082; PMID:11152660; PMID:21990100].

- **Pathway.** UniProt PATHWAY: "Glycerolipid metabolism; ether lipid biosynthesis" (UniPathway UPA00781). Reactome: R-HSA-75896 Plasmalogen biosynthesis.

## GOA annotation review summary (33 annotations)

- **Core molecular function** — GO:0008609 alkylglycerone-phosphate synthase activity: present as IDA (PMID:8399344, PMID:9553082, PMID:10415121), IBA, and IEA. ACCEPT the experimental/IBA; ACCEPT the redundant IEA (own core function, not over-annotation).
- **FAD binding** (GO:0071949 ISS/IEA; GO:0050660 flavin adenine dinucleotide binding IEA): correct cofactor; ACCEPT ISS, KEEP redundant IEA. GO:0050660 is a valid synonym-branch term (parent of GO:0071949) — ACCEPT.
- **catalytic activity** GO:0003824 (IEA, InterPro): correct but uninformative parent of the specific MF → MARK_AS_OVER_ANNOTATED (generic root-ish IEA superseded by GO:0008609).
- **protein binding** GO:0005515 (three IPI, all vs GORASP1/Q9BQQ3, high-throughput Y2H interactome maps PMID:25416956/31515488/32296183): uninformative bare "protein binding"; MARK_AS_OVER_ANNOTATED (policy: never REMOVE an IPI protein-binding). The GORASP1 interaction is real per UniProt INTERACTION record but its biological meaning for AGPS is unclear.
- **Biological process** — GO:0008611 ether lipid biosynthetic process (ISS, IEA): core BP, ACCEPT. GO:0008610 lipid biosynthetic process (IBA, IEA InterPro, and IDA PMID:9553082 acts_upstream_of_or_within): correct but general parent of GO:0008611; the IDA/IBA reflect real data → KEEP but the plain "lipid biosynthetic process" is less informative than ether lipid biosynthesis → MARK_AS_OVER_ANNOTATED for the generic IEA, KEEP_AS_NON_CORE / MODIFY toward GO:0008611 for the experimental ones. Chose: IBA GO:0008610 → MODIFY to GO:0008611; IEA GO:0008610 → MARK_AS_OVER_ANNOTATED; IDA GO:0008610 (acts_upstream_of_or_within, PMID:9553082) → MODIFY to GO:0008611 (paper is about ether phospholipid biosynthesis specifically).
- **Cellular component** — peroxisome GO:0005777 (IDA PMID:10415121, IDA PMID:9553082, IDA HPA GO_REF:0000052, IBA, ISS, IEA), peroxisomal matrix GO:0005782 (Reactome TAS x3), peroxisomal membrane GO:0005778 (ISS, IEA, HDA PMID:21525035): all correct peroxisomal localization. ACCEPT experimental/IBA/matrix; KEEP redundant IEA. Peroxisomal matrix is the best (most specific, mature-enzyme) location; membrane association reflects the GNPAT/AGPS complex on the inner membrane surface.
- **cytosol** GO:0005829 (Reactome TAS R-HSA-9033232, R-HSA-9033514): reflects the transient PTS2/PEX7 cytosolic import stage before peroxisomal import, not the functional steady-state location → KEEP_AS_NON_CORE.
- **membrane** GO:0016020 (HDA PMID:19946888, NK-cell membrane proteome): generic; over-annotation from a proteomic membrane prep → MARK_AS_OVER_ANNOTATED.
- **mitochondrion** GO:0005739 (HDA PMID:20833797, muscle mitochondrial phosphoproteome): AGPS is peroxisomal; this is a common contaminant in mitochondrial fraction proteomics (co-purifying peroxisomes). Experimental HDA so not REMOVE → MARK_AS_OVER_ANNOTATED.

## Core functions chosen

1. MF GO:0008609 alkylglycerone-phosphate synthase activity (directly_involved_in GO:0008611 ether lipid biosynthetic process; location GO:0005782 peroxisomal matrix).
2. MF GO:0071949 FAD binding (cofactor required for catalysis).
</content>
</invoke>

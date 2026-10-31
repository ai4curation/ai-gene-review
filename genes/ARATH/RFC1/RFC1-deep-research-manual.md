# RFC1 (At5g22010, UniProt Q9C587) - manual literature synthesis

No deep-research provider was available for this session. This file is a manual synthesis
of the cached publications (publications/PMID_*.md) and a PubMed search
(`Arabidopsis "replication factor C" RFC1 OR AtRFC1 OR At5g22010`, 9 hits).

## Identity and domain architecture

- RFC1 is the large (A) subunit of the heteropentameric replication factor C clamp loader
  (UniProt Q9C587, 956 aa; TAIR AT5G22010; GeneID 832261). UniProt: "Belongs to the activator 1
  large subunit family."
- Domains (UniProt/InterPro): N-terminal disordered region, BRCT domain (202-292; PS50172),
  AAA+ ATPase module with Walker A ATP-binding motif (FT BINDING 399..406, ECO:0000255),
  RFC lid (IPR047854) and the RFC1 C-terminal region (IPR013725; PF08519).
- [PMID:29971074 "AtRFC1 and OsRFC1 contain eight boxes I–VIII, while AtRFC2/3/4/5 and OsRFC2/3/4/5 contain seven boxes II-VIII."]

## Complex membership and localization

- BiFC in tobacco: [PMID:29971074 "AtRFC1 can interact with AtRFC2/3/4/5 in the presence of the other subunits, while OsRFC1 can directly bind OsRFC2/3/4/5."]
  and proposed arrangement [PMID:29971074 "In Arabidopsis, the arrangement of the subunits within the circular RFC complex was AtRFC5-AtRFC4-AtRFC3/2-AtRFC2/3-AtRFC1 (Figure 8C)."]
- Nuclear localization, two independent studies:
  [PMID:20639449 "GFP fluorescence was mainly detected in the nucleus in a transient assay of an epidermal leaf cell or in the root of T2 transgenic lines carrying RFC1-GFP"];
  [PMID:29971074 "AtRFC1 was only localized in the nucleus of the root tip cells (Figure 3N)."]
- Meiotic chromosomes (abstract only): [PMID:22974522 "Immunolocalization revealed that the AtRFC1 protein localized to the chromosomes during zygotene and pachytene in wild-type but were absent in the spo11-1 mutant."]

## Essential role / DNA replication

- Null alleles are lethal: [PMID:23144629 "Indeed, rfc1-3−/+ plants produce about 51% (178/349) defective seeds and no homozygous progeny (n = 385), suggesting that seeds homozygous for rfc1-3 were lethal."]
- Embryogenesis (abstract only, Chinese journal): [PMID:17556804 "These mutations caused defects in embryogenesis and led to embryo and seed abortion."]
- rfc1-1 plants are small due to fewer cells (PMID:20639449), consistent with reduced
  proliferation; this is a pleiotropic consequence of a replication defect.

## DNA repair and genome stability (somatic)

- [PMID:20639449 "As shown in Figures 3A and 3B , rfc1-1 ros1-1 and rfc1-1 were more sensitive to MMS than the C24 wild type or ros1-1 in both postgermination growth (the first test) and in seedling growth (the second test)."]
- [PMID:20639449 "These results indicate that DNA repair-related genes were spontaneously induced by rfc1-1 mutation."]
- Somatic homologous recombination strongly elevated in rfc1-1 (PMID:20639449); ABA suppresses
  this (PMID:24053948, abstract only).
- Telomeres shorter and telomerase expression reduced in rfc1 (PMID:20639449; correlative).

## Transcriptional gene silencing

- rfc1-1 was isolated as a ros1 suppressor releasing 35S-NPTII silencing and TSI, without DNA
  methylation change; DNA-damaging agents mimic this, so the effect may be partly indirect:
  [PMID:20639449 "These results suggest that treatment with DNA-damaging agents is able to directly release the TGS of 35S-NPTII in ros1-1 ."]
  and the rfc1 mutation [PMID:20639449 "reduced the levels of heterochromatin marker H3K9me2 in ros1 , and increased the expression of TSI"].

## Meiotic recombination

- PMID:23144629 (full text): partial-loss rfc1-2 has normal vegetative growth but reduced
  fertility, multivalents, fragmentation; epistasis places RFC1 after RAD51 in the SPO11-1
  pathway and in the MSH4/PTD interference-sensitive (class I) CO pathway; residual COs depend
  on MUS81 and lack interference.
  [PMID:23144629 "Therefore, these results support the hypothesis that RFC1 acts after RAD51 to promote recombination."]
  [PMID:23144629 "Our analyses demonstrate that the rfc1−/− plants form multivalents and are defective in CO formation via the interference-sensitive pathway (Type I), supporting the idea that lagging strand synthesis is probably important for dHJ formation."]
  Meiosis-specific RNAi (DMC1 promoter) reproduced the phenotype, arguing for a direct meiotic role.
- PMID:22974522 (abstract only): rfc1-2 chromosome fragmentation SPO11-1-dependent; "AtRFC1 is
  required for DNA double-strand break repair during meiotic homologous recombination".

## Points not verified

- UniProt FUNCTION lists "hypersensitive response (HR)" among RFC1 roles, citing PMID:17556804,
  20639449, 22974522 and 23144629. I could not find HR (the plant defence response) discussed in the
  cached texts of 20639449 or 23144629, nor in the two available abstracts; it may come from the
  full text of PMID:17556804 (not available) or be an expansion of "HR" = homologous recombination.
  Not asserted as an error; flagged as a question.
- No biochemical data (ATPase, clamp loading, DNA binding) exist for the Arabidopsis protein;
  molecular function is inferred from the conserved RFC1 family (yeast Rfc1, human RFC1/p140).

# RDR2 (At4g11130, UniProt O82504) - manual literature synthesis

No deep-research provider was available for this session; this summary was compiled manually from
the cached publications in `publications/` and the UniProt record. Every statement carries its source.

## Identity
- RNA-DEPENDENT RNA POLYMERASE 2, 1133 aa, Arabidopsis thaliana, TAIR AT4G11130, GeneID 826714;
  "Belongs to the RdRP family" (UniProt), InterPro IPR007855 RDRP.

## Biochemical activity
- Recombinant full-length RDR2 (baculovirus/insect cells) synthesizes RNA on RNA templates:
  [PMID:34903670 "RDR2 can transcribe free RNA but not RNA fully hybridized to template strand DNA"].
- Initiates 1-2 nt internal to the template 3' end and can use the RNA strand of an RNA/DNA hybrid only
  when ~9 nt of the 3' end are unpaired [PMID:34903670 "Our present study shows that RDR2 can only engage
  the RNA of an RNA/DNA hybrid if ∼9 nt (or more) of the RNA’s 3′ end is unpaired from the DNA"].
- Catalytic centre is a double-psi beta-barrel with an Asp triad (DLDGD 830-834) structurally homologous
  to multisubunit DNA-dependent RNA polymerases [PMID:34903670 "The three highly conserved aspartates
  (Asp triad) required for phosphodiester bond catalysis are located within a loop of DPBB2"].
- N-terminal RRM (aa 1-100) binds ssRNA by EMSA [PMID:34903670 "Electrophoretic mobility shift assays
  (EMSA) demonstrated that TF-RDR2-RRM exhibits ssRNA binding that is substantially impaired in
  TF-RDR2-RRMmut, consistent with RNA binding activity"].
- In planta-purified RDR2 associates with Pol IV and requires it (or an associated factor) for activity
  [PMID:23142082 "We conclude that RDR2 requires association with Pol IV, or a Pol IV-associated factor,
  for activity in vitro."]. Note the apparent tension with the recombinant activity above: free RDR2
  transcribes ssRNA, while RDR2 purified from nrpd1 plants did not transcribe the bipartite template
  that requires Pol IV coupling.
- Cryo-EM of the Pol IV-RDR2 holoenzyme shows an interpolymerase channel through which the backtracked
  Pol IV transcript is handed to RDR2 as template for dsRNA synthesis [PMID:34941388, abstract only:
  "Pol IV and RDR2 form a complex with their active sites connected by an interpolymerase channel"].

## Biological role
- Required for essentially all 24-nt heterochromatic siRNAs [PMID:15024409 "One RDR protein (RDR2) was
  required for all endogenous siRNAs analyzed"]; rdr2 loses non-CG methylation and H3K9me at AtSN1 and
  derepresses it [PMID:15024409].
- Background description of pathway role: [PMID:22772985 "RDR2 is responsible for the production of dsRNA
  precursors from single-stranded RNA transcripts, which are produced by RNA polymerase IV (Pol IV) and
  which correspond to the silenced genes or elements"]. That paper is about IBM1 controlling RDR2 and DCL3
  gene expression (H3K9/non-CG hypermethylation of the RDR2 locus in ibm1), i.e. regulation of RDR2, not
  RDR2 function.
- Required for reception of long-distance mRNA silencing in grafted shoots [PMID:17785412].
- rdr2 mutants are more susceptible to the necrotrophic fungus Plectosphaerella cucumerina
  [PMID:22242006].
- RDR2 transcript level is not changed by salicylic acid, unlike RDR1 [PMID:15024409].

## Localization
- Nucleolus (RNA processing centre, with DCL3, AGO4, NRPE1 and siRNAs) [PMID:16839878]; nucleolar signal
  plus nucleoplasmic puncta [PMID:22302148]; nucleus [PMID:26119694, abstract only].

## Interactions
- Pol IV (NRPD1) [PMID:23142082; PMID:34941388]; JMJ24 [PMID:26119694, abstract only].

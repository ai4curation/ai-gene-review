# MEF2C (human, Q06413) curation notes

Automated deep research was unavailable for this session (falcon 402, OpenAI 401). No `-deep-research-<provider>.md`
file was created. These notes come from the cached publications, the UniProt entry and PubMed abstracts fetched with
`just fetch-pmid`.

## Molecular function
- MADS-box/MEF2 transcription factor. It binds A/T-rich MEF2 sites as a dimer and transactivates [PMID:8455629 "The products of this gene have DNA-binding and trans-activating activities indistinguishable from those of the previously reported MEF2 factors"]; [PMID:9858528 "Members of the MEF2 family of transcription factors bind as homo- and heterodimers to the MEF2 site"].
- Partner DNA-binding TFs bind it through the DNA-binding domain:
  - MyoD/myogenin [PMID:8548800 "This cooperativity required direct interactions between the DNA-binding domains of MEF2 and the myogenic bHLH factors"]
  - HAND1 [PMID:16043483 "HAND1 is recruited to the promoter via physical interaction with MEF2 proteins"]
  - HAND2 [PMID:15486975 "dHAND and MEF2C synergistically activated expression of the atrial naturetic peptide gene (ANP) in transfected HeLa cells"]
  - TBX5 [PMID:19204083 "they physically associate through their DNA-binding domains to form a complex on the MYH6 promoter"]
  - NKX2-5 [PMID:19035347 "Co-immunoprecipitation and mammalian two-hybrid experiments revealed a direct molecular interaction between Nkx2.5 and Mef2c"]
  - SOX10 [PMID:21610032 "SOX10 and MEF2C physically interact and function cooperatively to activate the Mef2c gene in a feed-forward transcriptional circuit"]
- Repression by class II HDACs [PMID:10983972 "These HDACs do not interact directly with MyoD, yet they suppress its myogenic activity through association with MEF2"].
- Coactivators: MAML1 [PMID:16510869]; p300, recruited after skMLCK phosphorylates T80 [PMID:21556048 "MEFT80A was deficient in recruitment of p300 to skeletal but not cardiac muscle promoters"].
- Activated by p38 [PMID:9069290 "LPS increases the transactivation activity of MEF2C through p38-catalysed phosphorylation"]. MEF2C is the kinase's substrate, not a component of the MAPK cascade.

## Heart
- Mef2c-null mice [PMID:9162005 "In mice homozygous for a null mutation of MEF2C, the heart tube did not undergo looping morphogenesis, the future right ventricle did not form, and a subset of cardiac muscle genes was not expressed"].
- Second heart field: direct ISL1/GATA target [PMID:15253934 "establish Mef2c as the first direct transcriptional target of ISL1 in the anterior heart field"].
- Positive loop with NKX2-5 [PMID:9857019 "These findings indicate the presence of a positive regulatory network between Nkx2-5 and MEF2C"]. In double mutants the ventricular defect reflects differentiation, not proliferation [PMID:19035347 "ventricular hypoplasia is the result of defective ventricular cell differentiation"].
- The linear heart tube still forms in nulls, so primary heart field specification is marked as an over-annotation.

## Other tissues (pleiotropic, kept as non-core)
- Bone/cartilage [PMID:17336904 "controls bone development by activating the gene program for chondrocyte hypertrophy"].
- Neurons:
  - synapse number [PMID:18599438 "MEF2C limits excessive synapse formation during activity-dependent refinement of synaptic connectivity"]
  - cortical neuron differentiation [PMID:18599437]
  - human haploinsufficiency syndrome [PMID:19592390]
- B cells [PMID:18438409 "loss of Mef2c caused defects in B cell proliferation and survival after BCR stimulation"].
- Megakaryocytes/platelets [PMID:19211936].
- Melanocytes/neural crest [PMID:21610032].

## Review decisions (summary)
- Core:
  - GO:0000981 Pol II DbTF activity
  - GO:0045944 positive regulation of transcription by Pol II
  - Heart and cardiac muscle cell differentiation terms: GO:0007507, GO:0055012, GO:2000727
  - Skeletal myoblast differentiation
  - GO:0061629 partner-TF binding
  - GO:0042826 HDAC binding
- Generic protein binding rows were changed to HDAC, coactivator, partner-TF, kinase, HAT or E3-ligase binding where the partner is informative. MEK5 and CACNA1C rows were removed.
- Postsynapse IEA was removed, because MEF2C is a nuclear TF.
- Over-annotations: MAPK cascade, EPSP and NMDA/AMPA pathway terms, response to ischemia/xenobiotic/TSA, muscle cell fate determination, primary heart field specification, and negative regulation of ossification (a SOST reporter-assay inference that contradicts in vivo pro-ossification data).
- Kidney, sinoatrial valve, macrophage apoptosis and shear stress ISS terms are UNDECIDED, because their sources could not be checked.

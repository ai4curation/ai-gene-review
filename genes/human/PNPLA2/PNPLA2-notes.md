# PNPLA2 (ATGL) review notes

UniProt Q96AD5 (PLPL2_HUMAN), HGNC:30802. The literature synthesis below was done manually
from the cached publications and the UniProt record while falcon deep research was running
(the client reported a timeout, but `PNPLA2-deep-research-falcon.md` was written afterwards).
The falcon report agrees with this review: lipid-droplet TAG hydrolysis is the primary
function, ABHD5 co-activates and G0S2 inhibits ATGL, and PLA2, transacylase and PEDF-R
activities are context-specific; it also reports negligible retinyl-ester hydrolysis by ATGL,
consistent with keeping the retinyl esterase annotations as non-core.

## Core biology

- PNPLA2/ATGL (adipose triglyceride lipase, desnutrin, iPLA2-zeta, TTS-2.2, PEDF-R) is a
  patatin-domain serine hydrolase that catalyzes the first, rate-limiting step of
  intracellular triacylglycerol (TAG) hydrolysis on cytoplasmic lipid droplets, producing
  diacylglycerol (DAG) plus a fatty acid
  [PMID:15550674 "a second enzyme, adipose triglyceride lipase (ATGL), catalyzes the initial step in triglyceride hydrolysis"].
- High substrate specificity for TAG; associated with lipid droplets
  [PMID:15550674 "It exhibits high substrate specificity for triacylglycerol and is associated with lipid droplets."].
- The purified human enzyme has TAG lipase and acylglycerol transacylase activity
  [PMID:15364929 "we demonstrate that each possesses abundant TAG lipase activity"].
  Lipase activity requires the active-site serine
  [PMID:16150821 "All four proteins show lipase activity in vitro, which is dependent on the presence of the active site serine for Adiponutrin, Desnutrin/ATGL, and GS2."].
- Efficient activity requires the co-activator ABHD5/CGI-58 (the Chanarin-Dorfman gene)
  [PMID:16679289 "CGI-58 interacts with ATGL, stimulating its TG hydrolase activity up to 20-fold."].
- ATGL drives lipid droplet turnover in non-adipocytes
  [PMID:16239926 "Overexpression of wild-type ATGL causes a marked decrease in LD size, whereas a catalytically inactive mutant retains the ability to localize to LDs, but is unable to decrease their size."].
- ATGL protein levels are controlled by ubiquitination/proteasomal degradation (LDAH,
  PEX2), which is regulation OF ATGL rather than a function of ATGL
  [PMID:28578400 "LDAH enhances polyubiquitination and proteasomal degradation of adipose triglyceride lipase (ATGL), a rate limiting enzyme of TAG hydrolysis."].

## Secondary / in vitro activities

- Acylglycerol transacylase (mono-olein / diolein acceptors) in vitro [PMID:15364929].
- Retinyl ester hydrolysis and transfer of FA from TAG to retinol in keratinocyte-oriented
  comparative study [PMID:17603008 "Only hGS2 and hTTS-2.2 transfer fatty acid from triglyceride to retinol, hydrolyze retinylesters, and generate 1,3-diacylglycerol from triglycerides."].
- Phospholipase A2 activity stimulated by PEDF binding (PEDF-R model in retina)
  [PMID:17032652 "PEDF binding stimulates the enzymatic phospholipase A(2) activity of PEDF-R."].
  The plasma-membrane receptor model has not been integrated with the lipid-droplet
  lipase function; treated as non-core.
- FAHFA biosynthesis by transacylation (mouse and human adipose)
  [PMID:35676490 "recombinant ATGL uses a transacylation reaction that esterifies an HFA with a FA from triglyceride (TG) or diglyceride to produce FAHFAs"].
  Not proposed as a new annotation here (no GOA row; candidate for future curation).

## Disease

- Biallelic PNPLA2 variants cause neutral lipid storage disease with myopathy (NLSDM)
  [PMID:17187067 "a neutral lipid storage disease subgroup characterized by mild myopathy, absence of ichthyosis and mutations in both alleles of adipose triglyceride lipase (PNPLA2, also known as ATGL)"].
  This is consistent with loss of TAG hydrolase activity on lipid droplets
  (dismech `Neutral_Lipid_Storage_Myopathy`: GO:0004806 + GO:0019433 DECREASED, lipid droplet).

## Annotation decisions (summary)

- Core: triacylglycerol lipase activity (GO:0004806), triglyceride catabolic process
  (GO:0019433), lipid droplet (GO:0005811), lipid droplet disassembly (GO:1905691).
- Removed: lipoprotein lipase activity (Reactome DAG-hydrolysis reaction mis-mapped;
  ATGL acts on intracellular droplets, not lipoproteins), ER lumen (Reactome FAM20C
  substrate list; ATGL is cytosolic/droplet-associated), bare protein binding.
- General IEA parents (hydrolase activity, lipid (catabolic) metabolic process) and the
  InterPro-derived "positive regulation of triglyceride catabolic process" modified to the
  direct catalytic terms.

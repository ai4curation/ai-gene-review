# PCCB (human) — gene review notes

UniProtKB:P05166 — Propionyl-CoA carboxylase beta chain, mitochondrial. HGNC:8654. 539 aa precursor.

## Core biology (well established)

PCCB is the **beta (carboxyltransferase) subunit** of the mitochondrial **propionyl-CoA carboxylase (PCC)** holoenzyme, a biotin-dependent carboxylase (EC 6.4.1.3). The holoenzyme is an **alpha6-beta6 dodecamer** (~750 kDa) built around a central beta6 hexamer core, with the six PCCA (alpha) subunits arranged as monomers decorating the ends.
- [PMID:20725044 "The holoenzyme of PCC is an alpha(6)beta(6) dodecamer, with a molecular mass of 750 kDa. The alpha-subunit contains the biotin carboxylase (BC) and biotin carboxyl carrier protein (BCCP) domains, whereas the beta-subunit supplies the carboxyltransferase (CT) activity."]
- [PMID:29033250 "PCC is 750 kDa heterododecamer composed of 6 propionyl-CoA carboxylase, alpha (PCCA...) and 6 propionyl-CoA carboxylase, beta subunits (PCCB...)."]

**Catalysis / division of labor:** The alpha subunit (PCCA) catalyzes the ATP-dependent carboxylation of biotin (on its BCCP domain); the **beta subunit (PCCB) then transfers the carboxyl group from carboxybiotin to propionyl-CoA**, producing (S)-/D-methylmalonyl-CoA. The CT active site is at the interface of a beta-subunit dimer.
- UniProt FUNCTION: "the alpha subunit catalyzes the ATP-dependent carboxylation of the biotin ... while the beta subunit then transfers the carboxyl group from carboxylated biotin to propionyl-CoA".
- [PMID:20725044 "The active site of CT is located at the interface of its dimer"] and "after which the carboxyl group is transferred from biotin to the alpha-carbon of propionyl-CoA" [PMID:29033250].

**Reaction (RHEA:23720, EC 6.4.1.3):** propanoyl-CoA + hydrogencarbonate + ATP = (S)-methylmalonyl-CoA + ADP + phosphate + H+. Km(propanoyl-CoA)=0.29 mM; Km(bicarbonate)=3.0 mM (PMID:6765947).

**Enzyme purified from human liver; MF characterized biochemically:**
- [PMID:6765947 "The native enzyme has a molecular weight of approximately 540,000 and is composed of nonidentical subunits (alpha and beta)"; "The apparent Km values for ATP, propionyl-CoA, and bicarbonate are 0.08 mM, 0.29 mM, and 3.0 mM, respectively."] — IDA propionyl-CoA carboxylase activity + subunit composition.
- [PMID:15890657 "Propionyl-CoA carboxylase (PCC) is a biotin-dependent mitochondrial enzyme that catalyzes the conversion of propionyl-CoA to D-methylmalonyl-CoA."] — EXP MF; also characterizes PCCB pathogenic variants (R165W, E168K, R410W) and A497V polymorphism.

**Substrate promiscuity:** minor activity on butyryl-CoA (-> ethylmalonyl-CoA), acetyl-CoA (~1.5% rate), crotonoyl-CoA; greatest affinity for propionyl-CoA (PMID:6765947, PMID:29033250, UniProt CATALYTIC ACTIVITY RHEA:59520).

## Pathway / biological process

PCC catalyzes step 1 of propanoyl-CoA degradation to succinyl-CoA (UniPathway UPA00945/UER00908; "succinyl-CoA from propanoyl-CoA: step 1/3"). Propionyl-CoA is generated from catabolism of the branched-chain/other amino acids **isoleucine, valine, methionine, threonine**, odd-chain fatty acids, and cholesterol side chain ("c-VOMIT").
- [PMID:29033250 "Propionyl-CoA is produced by catabolism of cholesterol, valine, odd chain fatty acids, methionine, isoleucine and threonine (c-VOMIT)"].
- [PMID:29033250 "catalyzes the carboxylation of propionyl-CoA with bicarbonate producing methylmalonyl-CoA which is then converted to succinyl-CoA, an intermediate in the tricarboxylic acid cycle (TCA)"].
- disorders KB (Propionic_Acidemia.yaml): biological process = **GO:0019543 propionate catabolic process** (DECREASED in PA); MF = GO:0004658; location = GO:0005739.

Best-fit BP for the direct role: **propionate catabolic process (GO:0019543)**. The GOA "short-chain fatty acid catabolic process" (GO:0019626, IC) and "fatty acid catabolic process / metabolic process" IEA/NAS terms are broader parent-ish framings that capture the odd-chain-FA-derived and general FA-catabolism aspects. "branched-chain amino acid metabolic process" (GO:0009081, NAS) captures the Ile/Val degradation feed-in (upstream, not PCC's direct reaction).

## Localization

Mitochondrial **matrix**. PCC precursors carry cleavable N-terminal targeting presequences and are imported into the matrix; PCCB transit peptide = residues 1-28 (mature protein 29-539).
- [PMID:16023992 "the two subunits of the enzyme (MCCalpha; MCCbeta) are imported into the mitochondrial matrix by the classical pathway involving cleavable amino-terminal targeting presequences. We identified the cleavage sites ... and the amino-termini of the mature polypeptides of MCC and propionyl-CoA carboxylase, a mitochondrial paralog."] — establishes PCC N-terminus / matrix import (IDA source for GO:0005759).
- [PMID:29033250 "It is often described as a matrix enzyme because it can dissociate with sonication."]
- [PMID:8188292 "Propionyl-CoA carboxylase (PCC) is a mitochondrial, biotin-dependent enzyme"] — TAS mitochondrion.
- UniProt SUBCELLULAR LOCATION: Mitochondrion matrix (ECO:0000305|PubMed:16023992).

Reactome models a transient **cytosolic** stage before mitochondrial import ("Cytosolic carboxylases translocate to mitochondrial matrix", R-HSA-3323111; "HLCS biotinylates 6x(PCCA:PCCB)", R-HSA-2993447). These cytosol TAS annotations reflect the biosynthesis/import itinerary, not the functional compartment; keep as non-core.

## Protein interactions (IPI, bare "protein binding")

- PMID:20725044 with PCCA (P05165) — obligate partner subunit (holoenzyme). Meaningful but captured by MF/complex terms; bare "protein binding" is uninformative.
- PMID:33961781 (BioPlex) with PCCA (P05165).
- PMID:40205054 (multimodal cell maps) with PCCA (P05165).
- PMID:32296183 (HuRI binary interactome) with ACTN3 (Q08043) — likely high-throughput; not biologically corroborated for a matrix enzyme.
All four are bare GO:0005515 protein binding IPIs → per curation policy, MARK_AS_OVER_ANNOTATED (do not REMOVE; do not invent a specific MF). The complex membership is better captured by the ComplexPortal GO:1902494 catalytic complex (CPX-6169) annotation.

## Disease

Biallelic PCCB (or PCCA) pathogenic variants cause **propionic acidemia** (PA / propionic acidemia type II, MIM:606054; MONDO:0011628) — autosomal recessive organic acidemia with metabolic acidosis, hyperammonemia, ketosis, and multi-organ complications. Many PCCB variants act by impairing holoenzyme assembly/stability rather than directly abolishing catalysis (PMID:15890657).

## Annotation decisions summary
- MF GO:0004658 propionyl-CoA carboxylase activity (IBA, IEA, EXP, IDA) → ACCEPT (core). This is the defining function.
- GO:0016874 ligase activity (IEA, InterPro) → MODIFY to GO:0004658 (too general; the specific carboxylase/ligase activity is known).
- GO:0005759 mitochondrial matrix (IDA, IEA, NAS, TAS) → ACCEPT (core location).
- GO:0005739 mitochondrion (IBA is_active_in, HTP, TAS) → ACCEPT / KEEP (correct but less specific than matrix).
- GO:0005829 cytosol (TAS Reactome) → KEEP_AS_NON_CORE (transient import intermediate, not functional site).
- GO:1902494 catalytic complex (IPI, ComplexPortal) → ACCEPT (PCC holoenzyme).
- GO:0019543 not currently in GOA as such; add as NEW core BP (propionate catabolic process) — the direct pathway role.
- GO:0019626 short-chain fatty acid catabolic process (IC) → KEEP_AS_NON_CORE (reasonable but propionate catabolic process is the precise term).
- GO:0009062 fatty acid catabolic process (IEA ARBA) / GO:0006631 fatty acid metabolic process (NAS) → KEEP_AS_NON_CORE (odd-chain FA are one propionyl-CoA source; broad).
- GO:0009081 branched-chain amino acid metabolic process (NAS) → KEEP_AS_NON_CORE (Ile/Val degradation feeds propionyl-CoA; upstream context).
- 4x GO:0005515 protein binding (IPI) → MARK_AS_OVER_ANNOTATED.

## Deep research
falcon deep-research file was polled for ~8 min and not present at review time; review grounded in UniProt (P05166), seeded GOA, cached publications (all 10 present), and dismech Propionic_Acidemia.yaml.

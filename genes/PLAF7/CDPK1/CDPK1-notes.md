# CDPK1 (Plasmodium falciparum 3D7, P62344, PF3D7_0217500) - curation notes

**Note:** automated deep research was unavailable in this environment (Falcon auth
failure, invalid OpenAI key). These notes are a manual literature review based on the
UniProt record, the cached publications in `publications/`, and a targeted web search
(which identified and cached PMID:29311293).

## Identity and domain architecture

- Calcium-dependent protein kinase 1 (PfCDPK1; old names PfCPK, PFB0815w). CDPKs are
  a plant/alveolate kinase family that fuse a Ser/Thr kinase domain to a junction (J)
  domain and a calmodulin-like domain (CLD) with four EF hands; they do not need
  separate calmodulin.
- [PMID:8142371 "multidomain protein composed of an N-terminal kinase domain connected via a linker region to a C-terminal CaM-like calcium-binding domain"]
- [PMID:8142371 "The kinase can be activated by Ca2+ alone and associates with 45Ca2+"]
- EF-hand sites I and II are critical for activation:
  [PMID:8142371 "Sites I and II appear to be crucial for both Ca(2+)-induced conformational change and enzymatic activation"]
- The CLD binds the J-domain P3 region in a Ca2+-dependent manner:
  [PMID:23204525 "we provide direct evidence for the binding of the CamLD with the P3 region (Leu(356) to Thr(370)) of the JD in the presence of calcium (Ca(2+))"]
- Autophosphorylation and the N-terminal extension contribute to activation:
  [PMID:22539638 "Mass spectrometry revealed that PfCDPK1 was autophosphorylated at several sites; some of these were placed at strategic locations and therefore were found to be critical for kinase activation."]
- Truncation removing the J domain/CLD gives Ca2+-independent activity
  [PMID:19307175 "this PfCDPK1 truncation was also active both in the presence and the absence of calcium"].

## Localization

- N-myristoylation (Gly2), palmitoylation (Cys3) and a basic cluster anchor it to membranes:
  [PMID:15491359 "The supposed membrane attachment function of the basic cluster was experimentally verified and shown to participate together with N-myristoylation in membrane anchoring of the kinase."]
- PV and tubovesicular network in trophozoites:
  [PMID:15491359 "Using immunogold electron microscopy, the protein was detected in the parasitophorous vacuole and the tubovesicular system of the parasite."]
- Parasite plasma membrane of merozoites (most consistent result across labs):
  [PMID:18768477 "CDPK1 localizes to the periphery of P. falciparum merozoites and is therefore suitably located to act on MTIP and GAP45 at the inner membrane complex"];
  [PMID:23548171 "CDPK1 localizes to the parasite plasma membrane of replicating and invasive forms as well as very young intracellular parasites and does not appear to be exported into RBCs"];
  [PMID:32003970 "undergoes dynamic palmitoylation and localizes to the merozoite membrane"].
- Host erythrocyte membrane: reported by IFA in one study
  [PMID:23204525 "PfCDPK1 localized to the rim of the infected erythrocyte and appeared to be associated with the erythrocyte membrane in rings and trophozoites"]
  but not seen with endogenous GFP tagging (PMID:23548171, above). Treat as unresolved / minor.
- Peripheral localization also in gametocytes and gametes:
  [PMID:29311293 "As in the asexual stages, CDPK1 shows peripheral localization in the gametocytes and gametes"].

## Activity and substrates

- Motor complex substrates MTIP and GAP45:
  [PMID:18768477 "we demonstrate that both proteins can be efficiently phosphorylated by CDPK1 in vitro"];
  [PMID:22479457 "We show that GAP45 is phosphorylated by calcium dependent protein kinase 1 (CDPK1), and identify the modified serine residues."]
- RKIP (PfPE-PB1) as in vitro substrate/modulator:
  [PMID:17123645 "Phosphorylation of RKIP by PfCDPK1 in in vitro kinase assays suggests that RKIP may be an in vivo substrate of this kinase"].
- Phosphoproteomic substrate set incl. IMC proteins and PKA-R:
  [PMID:28680058 "We identify substrates of PfCDPK1, which includes proteins of Inner Membrane Complex and glideosome-actomyosin motor assembly."];
  [PMID:28680058 "PfCDPK1 phosphorylates PfPKA regulatory subunit (PfPKA-R) and regulates PfPKA activity in the parasite"].
- SERA5 (contested protease) phosphorylation:
  [PMID:29716996 "PfCDPK1 phosphorylated PfSERA5 in vitro in the presence of Ca2+ and enhanced its proteolytic activity"].
- RhopH3 S804:
  [PMID:33024030 "We also identified P. falciparum CDPK1 (PfCDPK1) as a possible candidate kinase for RhopH3-S804 phosphorylation and found that it regulates RhopH3 secretion from the parasite."]
- Upstream: phosphorylated by PKG at S64
  [PMID:26149123 "the calcium-dependent protein kinase, PfCDPK1, is phosphorylated by PfPKG"].
- 14-3-3I binds phospho-S64 motif; scaffolds a CDPK1/PKAr/14-3-3I complex:
  [PMID:32484216 "CDPK1 polypeptide sequence (61KLGpS64) behaves as canonical Mode I-type (RXXpS/pT) consensus 14-3-3 binding motif"];
  [PMID:32817103 "Pf14-3-3I binds phosphorylated PfPKAr and PfCDPK1 to mediate the assembly of a multiprotein complex in P. falciparum merozoites"].

## Biological role

- Microneme secretion / invasion:
  [PMID:23204525 "Purfalcamine, a previously identified specific inhibitor of PfCDPK1, also inhibits microneme discharge and erythrocyte invasion, confirming a role for PfCDPK1 in this process."];
  [PMID:28680058 "Using a conditional knockdown strategy, we here establish that this kinase is critical for the invasion of host erythrocytes."]
- Conflicting view: DD knockdown had no phenotype, J-domain expression arrests early schizogony
  [PMID:23548171 "parasites tolerated reduced expression without displaying a phenotype"].
- KO possible only in T145M background; slow asexual growth and loss of gametogenesis:
  [PMID:29311293 "The CDPK1 KO parasites show a slow growth rate compared with the WT and the CDPK1 T145M parasites. Additionally, the CDPK1 KO parasites show a defect in both male and female gametogenesis and could not establish an infection in mosquitoes."]
- Drug target; inhibitor series do not cleanly correlate with growth inhibition
  [PMID:25070106 "However, we were unable to correlate biochemical inhibition with parasite growth inhibition for this series overall."]

## Curation calls (summary)

- Core MF: GO:0009931 calcium-dependent protein serine/threonine kinase activity.
  Generic kinase rows (GO:0004672, GO:0004674) and the IBA GO:0004683
  (Ca2+/calmodulin-dependent) are modified to GO:0009931: CDPKs carry their own CLD and
  are activated by Ca2+ alone (PMID:8142371).
- GO:0005516 calmodulin binding (IBA) removed: no evidence; the PAINT node spans
  CaMK/CRK-like kinases that do bind CaM, but CDPKs are CaM-independent.
- GO:0009410 response to xenobiotic stimulus removed: inhibitor-sensitivity screening
  (PMID:25070106) is not a biological process of the gene product.
- Nucleus (IBA) flagged as over-annotation: myristoylated/palmitoylated membrane kinase,
  no nuclear localization reported.
- Location: plasma membrane accepted as core; PV/PVM/host PM/cytoplasm/motile cilium
  kept as non-core; generic "membrane" modified to plasma membrane + PVM.
- No microneme-secretion-specific GO term exists; GO:1903307 positive regulation of
  regulated secretory pathway accepted as best available.

# PLK3 manual review notes

PLK3 is an active polo-like serine/threonine kinase, but it is not just a
weaker PLK1. The reviewed human evidence repeatedly points to stress signaling,
G1/S entry, Golgi disassembly and centrosome/cytokinesis outputs rather than a
core kinetochore or mitotic-spindle organizer role.

Key evidence reviewed:

- PMID:17264206 directly supports nucleolar PLK3 and G1/S entry: the paper
  reports that PLK3 protein peaks in G1 and that PLK3 depletion blocks cyclin E
  expression and S-phase entry.
- PMID:14980500 and PMID:19103756 support the Golgi branch. PLK3 localizes to
  the Golgi during interphase, is activated by nocodazole, and phosphorylates
  VRK1 on Ser342 in a MEK1-dependent Golgi-fragmentation pathway.
- PMID:11447225, PMID:16481012, PMID:19490146 and PMID:21376736 support the
  DNA-damage and TP53-family checkpoint branch. PLK3 phosphorylates TP53 after
  oxidative stress, primes CHEK2 activation after ionizing radiation, inhibits
  TP73-mediated apoptosis, and contributes to CDC25A degradation after DNA
  damage.
- PMID:20889502 and PMID:21098032 support additional stress substrates HIF1A
  and ATF2.
- PMID:20951827 supports CIB1 regulation of PLK3 at centrosomes and shows that
  either CIB1 overexpression or PLK3 knockdown disrupts microtubule
  organization, centrosome segregation and cytokinesis.
- PMID:27344333 supports PLK3 overexpression promoting abnormal prion-protein
  degradation through LAMP2A/HSC70-dependent chaperone-mediated autophagy, but
  this is a secondary proteostasis branch rather than the central PLK3 role.

PAINT review:

- The root PTHR24345 active-kinase and cytoplasm rows are safe for PLK3.
- The PTHR24345:PTN002804399 node is the right PLK3 stress/Golgi branch for
  DNA-damage response, G1/S checkpoint signaling and Golgi disassembly.
- The root kinetochore, spindle-pole and mitotic-spindle-organization assertions
  on PTN000679870 are PLK1-like and over-propagate to PLK3. PLK3 has credible
  centrosome localization and cytokinesis evidence, but the human record does
  not establish an endogenous kinetochore or mitotic-spindle organization role.

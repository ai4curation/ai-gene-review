# Tbh (Q86B61) review notes

## Identity
- Tyramine beta-hydroxylase / tyramine beta-monooxygenase; copper type II ascorbate-dependent monooxygenase family (PANTHER PTHR10157:SF29), single-pass membrane protein; DBH ortholog-like.

## Literature
- Cloning and null mutants [PMID:8656284 "T beta h-null flies are octopamine-less but survive to adulthood."]
- Biochemistry [PMID:16376104 "Recombinant TbetaM requires copper for activity and has a typical type 2 copper EPR spectrum."]
  [PMID:16376104 "TbetaM efficiently hydroxylates the aliphatic carbon of phenolic amines such as tyramine (the physiological substrate) and dopamine"]
- Ovulation [PMID:14623230 "ovulation process is defective in the mutant females resulting in blockage of mature oocytes within the ovaries"]
- Larval locomotion [PMID:14978721 "Mutant larvae spent much more time in pausing episodes than wild-type larvae"]; motor pattern [PMID:16452672 "a role of the biogenic amines in the initiation and modulation of motor pattern generation"]
- Adult locomotion normal [PMID:17638385 "exhibit normal locomotor activity and cocaine responses in spite of showing female sterility"]
- Flight [PMID:17928454 "profound differences with respect to flight initiation and flight maintenance"]
- Aggression [PMID:19160504 "decreased aggression in both males and females"]
- Behavioral choice [PMID:17360588 "males with no OCT or with low OCT levels do not adapt to changing sensory cues and court both males and females"]
- Courtship conditioning [PMID:23055498 "OA plays an important role in courtship conditioning through its OAMB receptor"]
- Appetitive memory [PMID:14627633 "dopamine for aversive and octopamine for appetitive conditioning"]; reward learning [PMID:21206762 "partially impaired sugar-reward learning"]
- Ethanol tolerance [PMID:11086999 "Mutants unable to synthesize the catecholamine octopamine are also impaired in their ability to develop tolerance."]
- Nociceptive escape (ABLK neurons) [PMID:37309249 "suppression of Dh44 or Tbh reduced the rolling probability"]

## Decisions
- Core MF GO:0004836, BP GO:0006589, CC secretory granule membrane (IBA from DBH).
- Generic MF rows (catalytic, monooxygenase, GO:0016715, dopamine beta-monooxygenase) MODIFY to GO:0004836.
- membrane MODIFY to secretory granule membrane; locomotion MODIFY to larval locomotory behavior;
  regulation of behavior MODIFY to sex discrimination; learning MODIFY to olfactory/associative learning.
- aggressive behavior kept (both sexes affected), not narrowed to inter-male.

## Deep research (falcon) additions
- [file:DROME/Tbh/Tbh-deep-research-falcon.md "mutant has no detectable octopamine and approximately **10-fold elevated tyramine**"]
- Deep research notes fly Tbh vesicle localization is not experimentally resolved; the secretory granule membrane location rests on the DBH-family IBA (already stated in the review). No change to decisions.

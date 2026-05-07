# GO Monoamine Transport Restructuring

## Overview

Plan to obsolete a set of vague "monoamine transport" GO terms and reparent their
descendants under mechanistically specific transmembrane transport terms.

## Terms to Obsolete

| GO ID | Label |
|-------|-------|
| GO:0015844 | monoamine transport |
| GO:0051937 | catecholamine transport |
| GO:0006837 | serotonin transport |
| GO:7770032 | tyramine transport |
| GO:0015872 | dopamine transport |
| GO:0048241 | epinephrine transport |
| GO:0015874 | norepinephrine transport |

## Goal 2: Reparenting Descendants

### Category 1: Uptake terms → GO:0098739 `import across plasma membrane`

GO:0098739 is a confirmed child of GO:0055085 (transmembrane transport).
Covers plasma membrane reuptake by SERT, DAT, NET, PMAT, OCT3 etc.

| Term ID | Label | Current parent (being obsoleted) |
|---------|-------|----------------------------------|
| GO:0051610 | serotonin uptake | GO:0006837 |
| GO:0051620 | norepinephrine uptake | GO:0015874 |
| GO:0090494 | dopamine uptake | GO:0015872 |
| GO:0051583 | dopamine uptake involved in synaptic transmission | GO:0015872 |
| GO:0090493 | catecholamine uptake | GO:0051937 |

### Category 2: Vesicular loading → GO:0098700 `neurotransmitter loading into synaptic vesicle` *(already in place)*

These already have GO:0098700 as a parent. Obsoleting the monoamine transport
parent simply removes a redundant second parent.

| Term ID | Label |
|---------|-------|
| GO:0160310 | dopamine loading into synaptic vesicle |
| GO:0160311 | tyramine loading into synaptic vesicle |

### Category 3: Neurotransmitter-specific secretion → GO:0007269 `neurotransmitter secretion`

| Term ID | Label | Current parent (being obsoleted) |
|---------|-------|----------------------------------|
| GO:0001820 | serotonin secretion | GO:0006837 |
| GO:0060096 | serotonin secretion, neurotransmission | GO:0006837 |
| GO:0014046 | dopamine secretion | GO:0015872 |
| GO:0061527 | dopamine secretion, neurotransmission | GO:0015872 |
| GO:0099123 | somato-dendritic dopamine secretion | GO:0015872 |
| GO:0099124 | axonal dopamine secretion | GO:0015872 |
| GO:0048242 | epinephrine secretion | GO:0048241 |
| GO:0061529 | epinephrine secretion, neurotransmission | GO:0048241 |
| GO:0048243 | norepinephrine secretion | GO:0015874 |
| GO:0061533 | norepinephrine secretion, neurotransmission | GO:0015874 |
| GO:0061545 | tyramine secretion | GO:7770032 |
| GO:0061546 | tyramine secretion, neurotransmission | GO:7770032 |
| GO:0160043 | catecholamine secretion, neurotransmission | GO:0051937 |

Note: GO:0050432 (catecholamine secretion) is NOT placed under GO:0007269 because
catecholamines function as both neurotransmitters and hormones.

### Category 4: No change needed — existing parents are sufficient

| Term ID | Label | Existing parent retained |
|---------|-------|--------------------------|
| GO:0050432 | catecholamine secretion | GO:0032940 secretion by cell |
| GO:0002442 | serotonin secretion involved in inflammatory response | immune process parent |
| GO:0002554 | serotonin secretion by platelet | immune process parent |
| GO:0002556 | serotonin secretion by basophil | immune process parent |
| GO:0002552 | serotonin secretion by mast cell | immune process parent |

### Category 5: MF terms — remove `part_of` link only

These are Molecular Function terms whose `part_of` relationship to the obsoleted
BP terms should simply be dropped.

| Term ID | Label |
|---------|-------|
| GO:0008504 | monoamine transmembrane transporter activity |
| GO:0005330 | dopamine:sodium symporter activity |
| GO:0005334 | norepinephrine:sodium symporter activity |
| GO:0005335 | serotonin:sodium:chloride symporter activity |
| GO:0015311 | monoamine:proton antiporter activity |
| GO:0070908 | tyrosine:tyramine antiporter activity |

## Goal 3: Annotation Transfer

See: `annotations/Review annotations to GO_0015844 monoamine transport and children - Sheet1.tsv`

TODO: Transfer annotations to surviving descendant terms or other appropriate
transmembrane transport terms.

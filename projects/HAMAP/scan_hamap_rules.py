"""Scan HAMAP family rules for the MF_01093 failure pattern.

MF_01093 (MtrA) annotates a soluble paralog with a membrane location and a
transmembrane segment because three things coincide in one rule:

1. a ``Duplicate:`` clause, so the rule is allowed to annotate more than one
   protein per proteome (paralogs included);
2. a membrane SUBCELLULAR LOCATION stated outside any ``case`` block, so every
   member gets it;
3. a transmembrane feature triggered on every member
   (``DR   General; Transmembrane; ...; trigger=yes``).

This script reads the HAMAP rule flat file (``hamap_rules.dat`` from
https://ftp.expasy.org/databases/hamap/) and reports, for each rule, which of
those features it has, its size range, and its complex-subunit statement. It
does not decide that any rule is wrong: a duplicate clause with an
unconditional membrane location is correct when every paralog is a membrane
protein. The output lists the rules for which that has to be checked.

Usage:
    python projects/HAMAP/scan_hamap_rules.py PATH/TO/hamap_rules.dat > projects/HAMAP/hamap_rule_scan.yaml
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

MEMBRANE = re.compile(r"membrane", re.IGNORECASE)


@dataclass
class HamapRule:
    """Features of one HAMAP family rule relevant to the scan."""

    accession: str
    name: str = ""
    size: str | None = None
    duplicate: str | None = None
    unconditional_locations: list[str] = field(default_factory=list)
    conditional_locations: list[str] = field(default_factory=list)
    tm_trigger: bool = False
    tm_lines: list[str] = field(default_factory=list)
    unconditional_subunit: str | None = None

    @property
    def unconditional_membrane(self) -> bool:
        """Whether a membrane location is given to every member.

        >>> HamapRule("MF_1", unconditional_locations=["Cell membrane; Single-pass membrane protein."]).unconditional_membrane
        True
        >>> HamapRule("MF_2", conditional_locations=["Cell membrane."]).unconditional_membrane
        False
        """
        return any(MEMBRANE.search(loc) for loc in self.unconditional_locations)

    @property
    def size_range(self) -> tuple[int, int] | None:
        """Lower and upper bound of the ``Size:`` line, if it has one.

        >>> HamapRule("MF_1", size="183-262;").size_range
        (183, 262)
        >>> HamapRule("MF_2", size="unlimited;").size_range is None
        True
        """
        if not self.size:
            return None
        m = re.match(r"\s*(\d+)\s*-\s*(\d+)", self.size)
        return (int(m.group(1)), int(m.group(2))) if m else None


def _cc_blocks(lines: list[str]) -> list[tuple[str, str, bool]]:
    """Group ``CC   -!- TOPIC:`` blocks as (topic, text, inside_case).

    A block is conditional when it sits between a ``case`` line and its
    ``end case`` (``else`` branches count as conditional too).
    """
    blocks: list[tuple[str, str, bool]] = []
    depth = 0
    topic: str | None = None
    text: list[str] = []
    cond = False

    def flush() -> None:
        if topic is not None:
            blocks.append((topic, " ".join(text).strip(), cond))

    for line in lines:
        if line.startswith("case ") or line.startswith("case<"):
            flush()
            topic = None
            depth += 1
        elif line.startswith("end case"):
            flush()
            topic = None
            depth -= 1
        elif line.startswith("else"):
            flush()
            topic = None
        elif line.startswith("CC   -!- "):
            flush()
            head = line[9:]
            topic, _, rest = head.partition(":")
            text = [rest.strip()]
            cond = depth > 0
        elif line.startswith("CC       ") and topic is not None:
            text.append(line[9:].strip())
        else:
            flush()
            topic = None
    flush()
    return blocks


def parse_rule(block: list[str]) -> HamapRule:
    """Parse one rule block (lines from ``AC`` to ``//``)."""
    acc = next(line[5:].strip().rstrip(";") for line in block if line.startswith("AC   "))
    rule = HamapRule(acc)
    for line in block:
        if line.startswith("Names:") and not rule.name:
            rule.name = line.split(":", 1)[1].strip()
        elif line.startswith("Size:"):
            rule.size = line.split(":", 1)[1].strip()
        elif line.startswith("Duplicate:"):
            value = line.split(":", 1)[1].strip().rstrip(";")
            # HAMAP writes "Duplicate: None" when no paralog is allowed.
            rule.duplicate = None if value.lower() == "none" else value
        elif line.startswith("DR   General; Transmembrane"):
            rule.tm_lines.append(line[5:].strip())
            if "trigger=yes" in line:
                rule.tm_trigger = True
    for topic, text, cond in _cc_blocks(block):
        if topic == "SUBCELLULAR LOCATION":
            (rule.conditional_locations if cond else rule.unconditional_locations).append(text)
        elif topic == "SUBUNIT" and not cond and rule.unconditional_subunit is None:
            rule.unconditional_subunit = text
    return rule


def iter_rule_blocks(text: str):
    """Yield the lines of each ``AC   MF_`` rule block."""
    block: list[str] = []
    inside = False
    for line in text.splitlines():
        if line.startswith("AC   MF_"):
            inside, block = True, [line]
        elif inside:
            block.append(line)
            if line.startswith("//"):
                yield block
                inside = False


def scan(path: Path) -> dict:
    """Scan every rule and summarise the candidates."""
    rules = [parse_rule(b) for b in iter_rule_blocks(path.read_text(errors="replace"))]
    dup = [r for r in rules if r.duplicate]
    candidates = [r for r in dup if r.unconditional_membrane and r.tm_trigger]
    weaker = [r for r in dup if r.unconditional_membrane and not r.tm_trigger]

    def row(r: HamapRule) -> dict:
        lo_hi = r.size_range
        return {
            "rule": r.accession,
            "name": r.name,
            "size": r.size,
            "size_ratio": round(lo_hi[1] / lo_hi[0], 2) if lo_hi and lo_hi[0] else None,
            "duplicate": r.duplicate,
            "location": r.unconditional_locations,
            "transmembrane": r.tm_lines,
            "subunit": r.unconditional_subunit,
        }

    return {
        "source": str(path.name),
        "rules": len(rules),
        "with_duplicate_clause": len(dup),
        "with_unconditional_membrane_location": sum(r.unconditional_membrane for r in rules),
        "with_transmembrane_trigger": sum(r.tm_trigger for r in rules),
        "candidates": {
            "description": ("Duplicate clause AND unconditional membrane location AND "
                            "transmembrane feature triggered on every member (the MF_01093 shape)"),
            "count": len(candidates),
            "rules": [row(r) for r in sorted(candidates, key=lambda r: r.accession)],
        },
        "weaker_candidates": {
            "description": ("Duplicate clause AND unconditional membrane location, "
                            "no transmembrane trigger"),
            "count": len(weaker),
            "rules": [row(r) for r in sorted(weaker, key=lambda r: r.accession)],
        },
    }


if __name__ == "__main__":
    yaml.safe_dump(scan(Path(sys.argv[1])), sys.stdout, sort_keys=False, width=100, allow_unicode=True)

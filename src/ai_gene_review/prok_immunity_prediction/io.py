"""Input parsing helpers for prokaryotic immunity prediction."""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature

from ai_gene_review.prok_immunity_prediction.models import PreparedProteome, ProteinRecord

GFF_ATTRIBUTES = ("ID", "Name", "protein_id", "locus_tag", "gene")
PROTEIN_FASTA_SUFFIXES = {
    ".faa",
    ".faa.gz",
    ".fasta",
    ".fa",
    ".fas",
    ".pep",
    ".aa",
}
NUCLEOTIDE_FASTA_SUFFIXES = {".fna", ".ffn", ".fasta", ".fa", ".fsa"}
GENBANK_SUFFIXES = {".gb", ".gbk", ".gbff", ".genbank"}


def prepare_analysis_inputs(
    input_path: Path,
    output_dir: Path,
    gff_path: Path | None = None,
    prodigal_mode: str = "single",
) -> PreparedProteome:
    """Normalize supported inputs into a protein FASTA plus optional GFF."""
    input_path = input_path.resolve()
    output_dir = output_dir.resolve()
    derived_dir = output_dir / "derived"
    derived_dir.mkdir(parents=True, exist_ok=True)

    suffixes = suffix_set(input_path)
    if suffixes & GENBANK_SUFFIXES:
        proteins = parse_genbank_proteins(input_path)
        faa_path = derived_dir / f"{input_path.stem}.faa"
        gff_out = derived_dir / f"{input_path.stem}.gff"
        write_proteome_fasta(proteins, faa_path)
        write_gff(proteins, gff_out)
        return PreparedProteome(
            proteins=proteins,
            faa_path=faa_path,
            gff_path=gff_out,
            derived_from=input_path,
            notes=["Derived protein FASTA and GFF from GenBank annotations."],
        )

    if suffixes & NUCLEOTIDE_FASTA_SUFFIXES and not looks_like_protein_fasta(input_path):
        faa_path = derived_dir / f"{input_path.stem}.prodigal.faa"
        gff_out = derived_dir / f"{input_path.stem}.prodigal.gff"
        run_prodigal(input_path, faa_path, gff_out, mode=prodigal_mode)
        proteins = parse_fasta_proteins(faa_path, gff_out)
        return PreparedProteome(
            proteins=proteins,
            faa_path=faa_path,
            gff_path=gff_out,
            derived_from=input_path,
            notes=[f"Called CDS features with prodigal ({prodigal_mode} mode)."],
        )

    proteins = parse_fasta_proteins(input_path, gff_path)
    return PreparedProteome(
        proteins=proteins,
        faa_path=input_path,
        gff_path=gff_path.resolve() if gff_path else None,
        derived_from=input_path,
        notes=["Using supplied proteome FASTA directly."],
    )


def parse_fasta_proteins(faa_path: Path, gff_path: Path | None = None) -> list[ProteinRecord]:
    """Parse proteins from FASTA with optional coordinate metadata from GFF."""
    gff_index = parse_gff_annotations(gff_path) if gff_path else {}
    proteins: list[ProteinRecord] = []
    for idx, record in enumerate(SeqIO.parse(str(faa_path), "fasta")):
        header = gff_index.get(record.id, {})
        description = str(record.description).removeprefix(f"{record.id} ").strip()
        proteins.append(
            ProteinRecord(
                protein_id=record.id,
                sequence=str(record.seq),
                description=description,
                gene_symbol=header.get("gene"),
                locus_tag=header.get("locus_tag"),
                contig=header.get("seqid"),
                index=idx,
                start=parse_optional_int(header.get("start")),
                end=parse_optional_int(header.get("end")),
                strand=header.get("strand"),
                source_path=faa_path,
            )
        )
    return proteins


def parse_genbank_proteins(genbank_path: Path) -> list[ProteinRecord]:
    """Extract CDS translations from a GenBank file."""
    proteins: list[ProteinRecord] = []
    for seq_record in SeqIO.parse(str(genbank_path), "genbank"):
        cds_features = [feature for feature in seq_record.features if feature.type == "CDS"]
        for feature in cds_features:
            translation = get_translation(feature, seq_record.seq)
            if not translation:
                continue
            qualifiers = feature.qualifiers
            protein_id = first_qualifier(qualifiers, ("protein_id", "locus_tag", "gene")) or (
                f"{seq_record.id}_{len(proteins) + 1}"
            )
            proteins.append(
                ProteinRecord(
                    protein_id=protein_id,
                    sequence=translation,
                    description=first_qualifier(qualifiers, ("product",)) or "",
                    gene_symbol=first_qualifier(qualifiers, ("gene",)),
                    locus_tag=first_qualifier(qualifiers, ("locus_tag",)),
                    contig=seq_record.id,
                    index=len(proteins),
                    start=int(feature.location.start) + 1,
                    end=int(feature.location.end),
                    strand="-" if feature.location.strand == -1 else "+",
                    source_path=genbank_path,
                )
            )
    return proteins


def parse_gff_annotations(gff_path: Path | None) -> dict[str, dict[str, str]]:
    """Parse minimal per-protein metadata from GFF."""
    if gff_path is None:
        return {}
    metadata: dict[str, dict[str, str]] = {}
    with gff_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line or line.startswith("#"):
                continue
            parts = line.rstrip().split("\t")
            if len(parts) != 9:
                continue
            seqid, _, feature_type, start, end, _, strand, _, attributes = parts
            if feature_type.lower() not in {"cds", "gene"}:
                continue
            attrs = parse_gff_attributes(attributes)
            protein_keys = [attrs.get(name) for name in GFF_ATTRIBUTES if attrs.get(name)]
            for protein_key in protein_keys:
                metadata[protein_key] = {
                    "seqid": seqid,
                    "start": start,
                    "end": end,
                    "strand": strand,
                    "gene": attrs.get("gene", ""),
                    "locus_tag": attrs.get("locus_tag", ""),
                }
    return metadata


def parse_gff_attributes(raw_attributes: str) -> dict[str, str]:
    """Parse the 9th GFF column into a dictionary."""
    attributes: dict[str, str] = {}
    for item in raw_attributes.split(";"):
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        attributes[key] = value
    return attributes


def write_proteome_fasta(proteins: list[ProteinRecord], output_path: Path) -> None:
    """Write protein records to a FASTA file."""
    with output_path.open("w", encoding="utf-8") as handle:
        for protein in proteins:
            desc = protein.description if protein.description else protein.display_name
            handle.write(f">{protein.protein_id} {desc}\n")
            handle.write(wrap_sequence(protein.sequence))
            handle.write("\n")


def write_gff(proteins: list[ProteinRecord], output_path: Path) -> None:
    """Write a minimal GFF derived from protein metadata."""
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("##gff-version 3\n")
        for protein in proteins:
            seqid = protein.contig or "unknown_contig"
            start = protein.start or ((protein.index + 1) * 3)
            end = protein.end or start + max(len(protein.sequence) * 3 - 1, 0)
            strand = protein.strand or "+"
            attrs = [
                f"ID={protein.protein_id}",
                f"protein_id={protein.protein_id}",
            ]
            if protein.gene_symbol:
                attrs.append(f"gene={protein.gene_symbol}")
            if protein.locus_tag:
                attrs.append(f"locus_tag={protein.locus_tag}")
            handle.write(
                f"{seqid}\tprok_immunity\tCDS\t{start}\t{end}\t.\t{strand}\t0\t{';'.join(attrs)}\n"
            )


def run_prodigal(input_path: Path, faa_path: Path, gff_path: Path, mode: str = "single") -> None:
    """Call prodigal to derive a proteome from nucleotide FASTA."""
    if shutil.which("prodigal") is None:
        raise RuntimeError(
            "Input appears to be nucleotide FASTA, but 'prodigal' is not installed. "
            "Install prodigal or provide a proteome FASTA / GenBank file."
        )
    command = [
        "prodigal",
        "-i",
        str(input_path),
        "-a",
        str(faa_path),
        "-o",
        str(gff_path),
        "-f",
        "gff",
        "-p",
        mode,
    ]
    subprocess.run(command, check=True)


def get_translation(feature: SeqFeature, sequence: Seq) -> str:
    """Extract a CDS translation, falling back to local translation if needed."""
    qualifiers = feature.qualifiers
    translations = qualifiers.get("translation", [])
    if translations:
        return translations[0]
    cds_seq = feature.extract(sequence)
    return str(cds_seq.translate(to_stop=True))


def first_qualifier(qualifiers: dict[str, list[str]], keys: tuple[str, ...]) -> str | None:
    """Return the first present qualifier value for a list of keys."""
    for key in keys:
        values = qualifiers.get(key)
        if values:
            return values[0]
    return None


def wrap_sequence(sequence: str, width: int = 80) -> str:
    """Wrap FASTA sequence lines."""
    return "\n".join(sequence[i : i + width] for i in range(0, len(sequence), width))


def suffix_set(path: Path) -> set[str]:
    """Return all suffixes in lower case."""
    suffixes = {suffix.lower() for suffix in path.suffixes}
    if path.suffix:
        suffixes.add(path.suffix.lower())
    return suffixes


def parse_optional_int(value: str | None) -> int | None:
    """Convert a value to int when possible."""
    if value is None or value == "":
        return None
    return int(value)


def looks_like_protein_fasta(path: Path) -> bool:
    """Best-effort heuristic to distinguish protein FASTA from nucleotide FASTA."""
    with path.open("r", encoding="utf-8") as handle:
        letters = []
        for line in handle:
            if line.startswith(">"):
                continue
            letters.extend(re.findall(r"[A-Za-z]", line.upper()))
            if len(letters) >= 100:
                break
    if not letters:
        return False
    nucleotide_letters = {"A", "C", "G", "T", "U", "N"}
    non_nucleotide_fraction = sum(letter not in nucleotide_letters for letter in letters) / len(letters)
    return non_nucleotide_fraction > 0.1

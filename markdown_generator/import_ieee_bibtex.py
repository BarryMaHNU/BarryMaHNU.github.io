#!/usr/bin/env python3
"""Convert an IEEE Xplore BibTeX export into Academic Pages entries."""

import argparse
import html
import json
import re
from pathlib import Path


ENTRY_START = re.compile(r"@(ARTICLE|INPROCEEDINGS)\s*\{\s*([^,]+),", re.I)


def parse_entries(text):
    entries = []
    incomplete = []
    for match in ENTRY_START.finditer(text):
        depth = 1
        position = match.end()
        while position < len(text) and depth:
            if text[position] == "{":
                depth += 1
            elif text[position] == "}":
                depth -= 1
            position += 1
        key = match.group(2).strip()
        if depth:
            incomplete.append(key)
            continue
        body = text[match.end():position - 1]
        entries.append((match.group(1).upper(), key, parse_fields(body)))
    return entries, incomplete


def parse_fields(body):
    fields = {}
    position = 0
    while position < len(body):
        separator = re.match(r"[\s,]*([A-Za-z][\w-]*)\s*=\s*", body[position:])
        if not separator:
            break
        name = separator.group(1).lower()
        position += separator.end()
        if position >= len(body):
            break
        opener = body[position]
        if opener in "{\"":
            closer = "}" if opener == "{" else "\""
            depth = 1
            start = position + 1
            position = start
            while position < len(body) and depth:
                if opener == "{" and body[position] == opener:
                    depth += 1
                elif body[position] == closer and body[position - 1] != "\\":
                    depth -= 1
                position += 1
            value = body[start:position - 1]
        else:
            end = body.find(",", position)
            end = len(body) if end == -1 else end
            value = body[position:end]
            position = end
        fields[name] = re.sub(r"[{}]", "", value).strip()
    return fields


def author_name(name):
    parts = [part.strip() for part in name.split(",", 1)]
    return f"{parts[1]} {parts[0]}" if len(parts) == 2 else parts[0]


def yaml_string(value):
    return json.dumps(value, ensure_ascii=False)


def build_markdown(entry_type, key, fields):
    title = fields["title"].replace("\\&", "&")
    year = fields["year"]
    venue = fields.get("journal") or fields.get("booktitle", "")
    category = "manuscripts" if entry_type == "ARTICLE" else "conferences"
    authors = [author_name(name) for name in fields["author"].split(" and ")]
    doi = fields.get("doi", "")
    paper_url = f"https://doi.org/{doi}" if doi else f"https://ieeexplore.ieee.org/document/{key}"

    volume = fields.get("volume")
    number = fields.get("number")
    pages = fields.get("pages")
    details = ""
    if volume:
        details = volume
        if number:
            details += f"({number})"
        if pages:
            details += f", {pages}"
    elif pages:
        details = pages
    citation = f'{", ".join(authors)}. &quot;{html.escape(title)}.&quot; <i>{html.escape(venue)}</i>'
    if details:
        citation += f", {details}"
    citation += f" ({year})."

    return "\n".join([
        "---",
        f"title: {yaml_string(title)}",
        "collection: publications",
        f"category: {category}",
        f"permalink: /publication/{year}-01-01-{key}",
        f"date: {year}-01-01",
        f"venue: {yaml_string(venue)}",
        f"paperurl: {yaml_string(paper_url)}",
        f"citation: {yaml_string(citation)}",
        "---",
        f'[Access paper on IEEE Xplore]({paper_url}){{:target="_blank"}}',
        "",
    ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bibtex", type=Path)
    parser.add_argument("--output", type=Path, default=Path("_publications"))
    args = parser.parse_args()

    entries, incomplete = parse_entries(args.bibtex.read_text(encoding="utf-8-sig"))
    args.output.mkdir(parents=True, exist_ok=True)
    for entry_type, key, fields in entries:
        required = {"author", "title", "year"}
        missing = required.difference(fields)
        if missing:
            raise ValueError(f"Entry {key} is missing: {', '.join(sorted(missing))}")
        filename = f"{fields['year']}-01-01-{key}.md"
        (args.output / filename).write_text(
            build_markdown(entry_type, key, fields), encoding="utf-8", newline="\n"
        )

    print(f"Generated {len(entries)} publication files.")
    if incomplete:
        print(f"Skipped incomplete entries: {', '.join(incomplete)}")


if __name__ == "__main__":
    main()

"""Generate Ultra-long markdown documents."""

# ruff: noqa: S311

import argparse
import pathlib
import random

WORDS = [
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
    "lambda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "rho",
    "sigma",
    "tau",
    "upsilon",
    "phi",
    "chi",
    "psi",
    "omega",
    "quantum",
    "neutron",
    "proton",
    "electron",
    "photon",
    "boson",
    "entropy",
    "vector",
    "matrix",
    "tensor",
    "derivative",
    "integral",
    "limit",
    "equation",
    "formula",
    "function",
    "variable",
    "constant",
    "operator",
    "theorem",
    "axiom",
    "lemma",
    "proof",
    "algorithm",
    "syntax",
    "runtime",
    "compile",
    "execute",
    "thread",
    "process",
    "kernel",
    "package",
    "library",
    "module",
    "class",
    "object",
    "method",
    "function",
    "variable",
    "parameter",
    "argument",
    "decorator",
    "iterator",
    "generator",
    "context",
    "async",
    "await",
    "future",
    "promise",
    "callback",
    "exception",
    "error",
    "debug",
    "test",
    "mock",
    "mountain",
    "valley",
    "river",
    "ocean",
    "forest",
    "tree",
    "leaf",
    "stone",
    "cloud",
    "rain",
    "snow",
    "storm",
    "wind",
    "sand",
    "desert",
    "island",
    "volcano",
    "earthquake",
    "horizon",
    "sunrise",
    "sunset",
    "moon",
    "star",
    "planet",
    "galaxy",
    "cosmos",
    "truth",
    "beauty",
    "justice",
    "chaos",
    "order",
    "harmony",
    "balance",
    "conflict",
    "memory",
    "dream",
    "vision",
    "silence",
    "whisper",
    "echo",
    "shadow",
    "light",
    "darkness",
    "hope",
    "fear",
    "joy",
    "sorrow",
    "curiosity",
    "wisdom",
    "ignorance",
    "knowledge",
    "table",
    "chair",
    "book",
    "paper",
    "pen",
    "clock",
    "door",
    "window",
    "road",
    "bridge",
    "tower",
    "city",
    "village",
    "garden",
    "field",
    "machine",
    "engine",
    "wheel",
    "signal",
    "pattern",
    "random",
    "sequence",
    "order",
    "flow",
    "structure",
    "system",
    "network",
    "model",
    "design",
    "architecture",
]

FILLER_TOKENS = [
    # Connectors
    "however",
    "therefore",
    "moreover",
    "furthermore",
    "consequently",
    "nevertheless",
    "thus",
    "instead",
    "likewise",
    "similarly",
    "alternatively",
    "in contrast",
    "nonetheless",
    "otherwise",
    "meanwhile",
    "eventually",
    "suddenly",
    "at last",
    "afterwards",
    "beforehand",
    "subsequently",
    "immediately",
    "soon",
    "earlier",
    "later on",
    "by then",
    "at the same time",
    "prior to",
    "kind of",
    "sort of",
    "basically",
    "essentially",
    "actually",
    "virtually",
    "nearly",
    "almost",
    "roughly",
    "approximately",
    "somewhat",
    "partially",
    "largely",
    "mostly",
    "above all",
    "indeed",
    "truly",
    "certainly",
    "clearly",
    "definitely",
    "obviously",
    "undoubtedly",
    "without question",
    "beyond doubt",
    "first of all",
    "to begin with",
    "in the first place",
    "secondly",
    "then",
    "next",
    "after that",
    "finally",
    "last but not least",
    "in fact",
    "as a matter of fact",
    "for example",
    "for instance",
    "in particular",
    "notably",
    "specifically",
    "as such",
    "on the other hand",
    "in any case",
    "all the same",
    "still",
    "even so",
    "yet",
    "regardless",
    "notwithstanding",
    "well",
    "so",
    "you know",
    "like",
    "I mean",
    "basically",
    "honestly",
    "seriously",
    "frankly",
    "actually",
    "anyway",
    "right",
    "okay",
    "alright",
    "it seems",
    "it appears",
    "perhaps",
    "maybe",
    "probably",
    "possibly",
    "presumably",
    "conceivably",
    "potentially",
    "as it were",
    "so to speak",
    "in a way",
    "to some extent",
    "more or less",
    "give or take",
    "in general",
    "on the whole",
    "by and large",
    "all things considered",
    "in summary",
    "to put it simply",
    "in other words",
]

TEXT_PATTERNS = [
    "The {WORD} of {WORD} is {WORD}.",
    "{WORD} and {WORD} form the basis of {WORD}.",
    "Without {WORD}, there can be no {WORD}.",
    "Every {WORD} contains a hidden {WORD}.",
    "{WORD} is important, {FILLER}, when considering {WORD}.",
    "In fact, {WORD} often leads to {WORD}, {FILLER}.",
    "{WORD} may appear as {WORD}, but {FILLER}, it is really {WORD}.",
    "Sometimes {WORD} follows {WORD}; {FILLER}, the reverse is true.",
    "If {WORD} increases, then {WORD} decreases.",
    "Because of {WORD}, the {WORD} becomes {WORD}.",
    "{WORD} results in {WORD}, which then produces {WORD}.",
    "The presence of {WORD} often implies {WORD}.",
    "{WORD} is like {WORD}, except with more {WORD}.",
    "Unlike {WORD}, {WORD} remains {WORD}.",
    "{WORD} is greater than {WORD}, but less than {WORD}.",
    "The essence of {WORD} lies within {WORD}.",
    "One could argue that {WORD} is merely {WORD}.",
    "Ultimately, {WORD} depends on {WORD}, {FILLER}.",
    "{WORD} represents the struggle between {WORD} and {WORD}.",
    "{WORD}, {WORD}, and {WORD} together define {WORD}.",
    "We observe {WORD}, then {WORD}, and finally {WORD}.",
    "The cycle of {WORD}, {WORD}, and {WORD} repeats endlessly.",
    "What is {WORD} without {WORD}?",
    "Can {WORD} exist alongside {WORD}?",
    "Is {WORD} just another form of {WORD}?",
    "Why should {WORD} matter more than {WORD}?",
    "In summary, {WORD} stands at the core of {WORD}.",
    "On the whole, {WORD} shapes the meaning of {WORD}.",
    "Thus, {WORD} is inseparable from {WORD}.",
]

CODE_SNIPPETS = {
    "python": "def func(x):\n    return x * 42",
    "bash": 'for i in {1..5}; do echo "Item $i"; done',
    "json": '{ "foo": "bar", "numbers": [1,2,3] }',
    "javascript": "function foo(x) { return x + 1; }",
    "html": "<div><p>Hello world</p></div>",
}


def random_paragraph():
    """Generate a random Paragraph of 3 - 10 sentences."""
    sentences = []
    freq = 0.3
    for _ in range(random.randint(3, 10)):
        words = random.sample(WORDS, k=random.randint(6, 12))
        filler = random.choice(FILLER_TOKENS) if random.random() < freq else ""
        sentence = " ".join(words).capitalize()
        if filler:
            sentence += f", {filler},"
        sentence += "."
        sentences.append(sentence)
    return "\n".join(sentences) + "\n"


def random_list():
    """Generate a random list of various lengths."""
    if random.choice([True, False]):
        return "\n".join([f"- {w}" for w in random.sample(WORDS, k=6)]) + "\n"
    else:
        return (
            "\n".join([f"{i}. {w}" for i, w in enumerate(random.sample(WORDS, k=6), 1)])
            + "\n"
        )


def random_blockquote():
    """Generate a random quote."""
    lines = ["> " + random_paragraph()]
    if random.choice([True, False]):
        lines.append("> > Nested " + random.choice(WORDS))
    return "\n".join(lines) + "\n"


def random_codeblock():
    """Generate a random code block."""
    lang, code = random.choice(list(CODE_SNIPPETS.items()))
    return f"```{lang}\n{code}\n```\n"


def random_table():
    """Generate a random table."""
    header = "| " + " | ".join(random.sample(WORDS, k=4)) + " |"
    sep = "|---|---|---|---|"
    rows = ["|" + "|".join(random.sample(WORDS, k=4)) + " |" for _ in range(4)]
    return "\n".join([header, sep, *rows]) + "\n"


def random_image():
    """Generate a random image link."""
    size = random.randint(100, 600)
    return (
        "![Placeholder](https://picsum.photos/"
        f"{random.randint(1, 999)}/{size}x{size})\n"
    )


def random_link():
    """Generate a random link."""
    return (
        f"[Link to {random.choice(WORDS)}]"
        f"(https://example.com/{random.choice(WORDS).lower()})\n"
    )


def random_checklist():
    """Generate a random checklist."""
    return (
        "\n".join(
            [
                f"- [{'x' if random.choice([True, False]) else ' '}] {w}"
                for w in random.sample(WORDS, k=5)
            ]
        )
        + "\n"
    )


def random_heading(depth=2):
    """Generate a random heading."""
    hashes = "#" * depth
    return f"{hashes} Heading {random.choice(WORDS).capitalize()}\n"


def generate_file(path: pathlib.Path, lines: int = 3000, seed=None):
    """Generate a file."""
    if seed is not None:
        random.seed(seed, lines)

    out = []
    out.append(f"# {' '.join(random.sample(WORDS, k=3))}\n\n")
    out.append("This file is automatically generated.\n\n")

    generators = [
        random_paragraph,
        random_list,
        random_blockquote,
        random_codeblock,
        random_table,
        random_image,
        random_link,
        random_checklist,
        lambda: random_heading(random.randint(2, 6)),
    ]
    weights = [
        50,
        5,
        5,
        2,
        5,
        3,
        10,
        10,
        10,
    ]

    while len("".join(out).splitlines()) < lines:
        func = random.choices(generators, weights, k=1)[0]
        out.append(func() + "\n")

    text = "".join(out)
    path.write_text(text, encoding="utf-8")
    print(f"✅ Wrote {path} ({len(text.splitlines())} lines)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Generate markdown files.")
    parser.add_argument(
        "file_name", help="Name of the file", default="markdown-example"
    )
    parser.add_argument("--lines", "-l", help="Number of lines of markdown.")
    parser.add_argument("--seed", "-s", help="Random seed")
    args = parser.parse_args()
    base = pathlib.Path("tests/data/")
    base.mkdir(exist_ok=True)

    generate_file(
        path=base / f"{args.file_name}.md",
        lines=int(args.lines) if args.lines else random.randint(2000, 6000),
        seed=int(args.seed) if args.seed else 123,
    )

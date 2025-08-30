"""Template strings."""

# ruff: noqa: E501, D101

from dataclasses import dataclass


@dataclass
class Block1:
    md = """# Theoretical Fabrication of Quantum Slopes

It is widely accepted that **intermodal resonances**
frequently result in pseudo-laminar substrates.
When considering *non-permeable equatorial inversions*,
one must account for:

- Transitive modulation of the scalar phase
- Recursive instantiation of flow-nodes
- Autonomous realignment of inert clusters

> “The ambiguity of convergence lies not in the frequency,
> but in the suggestion of its shadow.” – Anon

For further clarification, refer to the following function:

```python
def frobnicate(phase):
    return (phase ** 2) % 7
```
"""
    sections = [
        "# Theoretical Fabrication of Quantum Slopes",
        "It is widely accepted that **intermodal resonances**\n"
        "frequently result in pseudo-laminar substrates.\n"
        "When considering *non-permeable equatorial inversions*,\n"
        "one must account for:",
        "- Transitive modulation of the scalar phase\n"
        "- Recursive instantiation of flow-nodes\n"
        "- Autonomous realignment of inert clusters",
        "> “The ambiguity of convergence lies not in the frequency,\n"
        "> but in the suggestion of its shadow.” – Anon",
        "For further clarification, refer to the following function:",
        "```python\ndef frobnicate(phase):\n    return (phase ** 2) % 7\n```",
    ]
    html = """<html lang='en_gb' dir='ltr'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Markdown Document</title>
    <meta name="description" content="Generated from Markdown">
    <meta name="author" content="md-html">
    <style> body { max-width: 120ch; margin: 2rem auto; padding: 0 1rem; font-family: system-ui, sans-serif; line-height: 1.6; color: #222; background: #fff; } h1, h2, h3, h4, h5, h6 { line-height: 1.2; margin-top: 1.5em; } pre, code { font-family: monospace; background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 3px; } pre { padding: 1em; overflow-x: auto; } blockquote { margin: 1em 0; padding-left: 1em; border-left: 0.25em solid #ccc; color: #555; } a { color: #0645ad; text-decoration: none; } a:hover { text-decoration: underline; } </style>
  </head>
  <body>
    <p># Theoretical Fabrication of Quantum Slopes</p>
    <p>It is widely accepted that **intermodal resonances**
frequently result in pseudo-laminar substrates.
When considering *non-permeable equatorial inversions*,
one must account for:</p>
    <p>- Transitive modulation of the scalar phase
- Recursive instantiation of flow-nodes
- Autonomous realignment of inert clusters</p>
    <p>&gt; “The ambiguity of convergence lies not in the frequency,
&gt; but in the suggestion of its shadow.” – Anon</p>
    <p>For further clarification, refer to the following function:</p>
    <p>```python
def frobnicate(phase):
    return (phase ** 2) % 7
```</p>
  </body>
</html>"""


@dataclass
class Block2:
    md = """### Block 2: Tables, Links, and Inline Elements

Below is a table comparing hypothetical structures across irrelevant metrics:

| Structure        | Flux Index | Vibrancy Quotient  | Link                                       |
|------------------|------------|--------------------|--------------------------------------------|
| Node             | 84.1       | 0.003              | [Node.io](https://example.com/node)        |
| Cluster          | 13.7       | 42.0               | [Cluster](https://example.com/cluster)     |
| Entangler        | ∞          | 7.8                | [Entangler](https://example.com/entangler) |

Inline code can be used to denote variables like `theta`, `λ`, or `Markdown`.

Be cautious when applying multi-spatial dampening to **sub-quadratic manifolds**."""
    sections = [
        "### Block 2: Tables, Links, and Inline Elements",
        "Below is a table comparing hypothetical structures across irrelevant metrics:",
        "| Structure        | Flux Index | Vibrancy Quotient  | Link                                       |\n"
        "|------------------|------------|--------------------|--------------------------------------------|\n"
        "| Node             | 84.1       | 0.003              | [Node.io](https://example.com/node)        |\n"
        "| Cluster          | 13.7       | 42.0               | [Cluster](https://example.com/cluster)     |\n"
        "| Entangler        | ∞          | 7.8                | [Entangler](https://example.com/entangler) |",
        "Inline code can be used to denote variables like `theta`, `λ`, or `Markdown`.",
        "Be cautious when applying multi-spatial dampening to **sub-quadratic manifolds**.",
    ]
    html = """<html lang='en_gb' dir='ltr'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Markdown Document</title>
    <meta name="description" content="Generated from Markdown">
    <meta name="author" content="md-html">
    <style> body { max-width: 120ch; margin: 2rem auto; padding: 0 1rem; font-family: system-ui, sans-serif; line-height: 1.6; color: #222; background: #fff; } h1, h2, h3, h4, h5, h6 { line-height: 1.2; margin-top: 1.5em; } pre, code { font-family: monospace; background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 3px; } pre { padding: 1em; overflow-x: auto; } blockquote { margin: 1em 0; padding-left: 1em; border-left: 0.25em solid #ccc; color: #555; } a { color: #0645ad; text-decoration: none; } a:hover { text-decoration: underline; } </style>
  </head>
  <body>
    <p>### Block 2: Tables, Links, and Inline Elements</p>
    <p>Below is a table comparing hypothetical structures across irrelevant metrics:</p>
    <p>| Structure        | Flux Index | Vibrancy Quotient  | Link                                       |
|------------------|------------|--------------------|--------------------------------------------|
| Node             | 84.1       | 0.003              | [Node.io](https://example.com/node)        |
| Cluster          | 13.7       | 42.0               | [Cluster](https://example.com/cluster)     |
| Entangler        | ∞          | 7.8                | [Entangler](https://example.com/entangler) |</p>
    <p>Inline code can be used to denote variables like `theta`, `λ`, or `Markdown`.</p>
    <p>Be cautious when applying multi-spatial dampening to **sub-quadratic manifolds**.</p>
  </body>
</html>"""


@dataclass
class Block3:
    md = """### Block 3: Lists and quotes

1. Initialize the **frob layer**:
    - Compute delta flux.
    - Adjust *pseudo-nodal bias* if necessary.
        - Note: do **not** conflate with semi-factual torsion fields.
2. Iterate through *orbital segments*:
    1. Deconstruct local loops.
    1. Re-synchronize dampened echoes.
3. Finalize with an ephemeral mutex.

> “Every mutex is a promise, and every promise is a ghost.” – Prof. Wibble

_Italics_ can suggest uncertainty, while **bold text** affirms conviction."""
    sections = [
        "### Block 3: Lists and quotes",
        "1. Initialize the **frob layer**:\n"
        "    - Compute delta flux.\n"
        "    - Adjust *pseudo-nodal bias* if necessary.\n"
        "        - Note: do **not** conflate with semi-factual torsion fields.\n"
        "2. Iterate through *orbital segments*:\n"
        "    1. Deconstruct local loops.\n"
        "    1. Re-synchronize dampened echoes.\n"
        "3. Finalize with an ephemeral mutex.",
        "> “Every mutex is a promise, and every promise is a ghost.” – Prof. Wibble",
        "_Italics_ can suggest uncertainty, while **bold text** affirms conviction.",
    ]
    html = """<html lang='en_gb' dir='ltr'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Markdown Document</title>
    <meta name="description" content="Generated from Markdown">
    <meta name="author" content="md-html">
    <style> body { max-width: 120ch; margin: 2rem auto; padding: 0 1rem; font-family: system-ui, sans-serif; line-height: 1.6; color: #222; background: #fff; } h1, h2, h3, h4, h5, h6 { line-height: 1.2; margin-top: 1.5em; } pre, code { font-family: monospace; background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 3px; } pre { padding: 1em; overflow-x: auto; } blockquote { margin: 1em 0; padding-left: 1em; border-left: 0.25em solid #ccc; color: #555; } a { color: #0645ad; text-decoration: none; } a:hover { text-decoration: underline; } </style>
  </head>
  <body>
    <p>### Block 3: Lists and quotes</p>
    <p>1. Initialize the **frob layer**:
    - Compute delta flux.
    - Adjust *pseudo-nodal bias* if necessary.
        - Note: do **not** conflate with semi-factual torsion fields.
2. Iterate through *orbital segments*:
    1. Deconstruct local loops.
    1. Re-synchronize dampened echoes.
3. Finalize with an ephemeral mutex.</p>
    <p>&gt; “Every mutex is a promise, and every promise is a ghost.” – Prof. Wibble</p>
    <p>_Italics_ can suggest uncertainty, while **bold text** affirms conviction.</p>
  </body>
</html>"""


@dataclass
class Block4:
    md = """## Block 4: Images and links

![Sample diagram of a parabolic null field](https://example.com/null-field.png)

[Read more information about null fields](https://example.com/null-field-analysis)

---

To simulate a field discontinuity:

```js
function simulateNullField(amplitude) {
  return amplitude < 0 ? null : Math.sqrt(amplitude) * 3.1415;
}
```"""
    sections = [
        "## Block 4: Images and links",
        "![Sample diagram of a parabolic null field](https://example.com/null-field.png)",
        "[Read more information about null fields](https://example.com/null-field-analysis)",
        "---",
        "To simulate a field discontinuity:",
        "```js\n"
        "function simulateNullField(amplitude) {\n"
        "  return amplitude < 0 ? null : Math.sqrt(amplitude) * 3.1415;\n"
        "}\n"
        "```",
    ]
    html = """<html lang='en_gb' dir='ltr'>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Markdown Document</title>
    <meta name="description" content="Generated from Markdown">
    <meta name="author" content="md-html">
    <style> body { max-width: 120ch; margin: 2rem auto; padding: 0 1rem; font-family: system-ui, sans-serif; line-height: 1.6; color: #222; background: #fff; } h1, h2, h3, h4, h5, h6 { line-height: 1.2; margin-top: 1.5em; } pre, code { font-family: monospace; background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 3px; } pre { padding: 1em; overflow-x: auto; } blockquote { margin: 1em 0; padding-left: 1em; border-left: 0.25em solid #ccc; color: #555; } a { color: #0645ad; text-decoration: none; } a:hover { text-decoration: underline; } </style>
  </head>
  <body>
    <p>## Block 4: Images and links</p>
    <p>![Sample diagram of a parabolic null field](https://example.com/null-field.png)</p>
    <p>[Read more information about null fields](https://example.com/null-field-analysis)</p>
    <p>---</p>
    <p>To simulate a field discontinuity:</p>
    <p>```js
function simulateNullField(amplitude) {
  return amplitude &lt; 0 ? null : Math.sqrt(amplitude) * 3.1415;
}
```</p>
  </body>
</html>"""

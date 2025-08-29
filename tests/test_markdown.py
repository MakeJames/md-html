"""Test the methods of the Markdown module."""

# ruff: noqa: S101, E501

import pytest

from md_html.markdown import Markdown


class TestMarkdown:
    """Test the methods of the Markdown class."""

    @pytest.mark.parametrize(
        "content,expected",
        [
            (
                """# Theoretical Fabrication of Quantum Slopes

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
""",
                [
                    "# Theoretical Fabrication of Quantum Slopes",
                    """It is widely accepted that **intermodal resonances**
frequently result in pseudo-laminar substrates.
When considering *non-permeable equatorial inversions*,
one must account for:""",
                    """- Transitive modulation of the scalar phase
- Recursive instantiation of flow-nodes
- Autonomous realignment of inert clusters""",
                    """> “The ambiguity of convergence lies not in the frequency,
> but in the suggestion of its shadow.” – Anon""",
                    "For further clarification, refer to the following function:",
                    """```python
def frobnicate(phase):
    return (phase ** 2) % 7
```""",
                ],
            ),
            (
                """### Block 2: Tables, Links, and Inline Elements

Below is a table comparing hypothetical structures across irrelevant metrics:

| Structure        | Flux Index | Vibrancy Quotient  | Link                                       |
|------------------|------------|--------------------|--------------------------------------------|
| Node             | 84.1       | 0.003              | [Node.io](https://example.com/node)        |
| Cluster          | 13.7       | 42.0               | [Cluster](https://example.com/cluster)     |
| Entangler        | ∞          | 7.8                | [Entangler](https://example.com/entangler) |

Inline code can be used to denote variables like `theta`, `λ`, or `Markdown`.

Be cautious when applying multi-spatial dampening to **sub-quadratic manifolds**.""",
                [
                    "### Block 2: Tables, Links, and Inline Elements",
                    "Below is a table comparing hypothetical structures across irrelevant metrics:",
                    """| Structure        | Flux Index | Vibrancy Quotient  | Link                                       |
|------------------|------------|--------------------|--------------------------------------------|
| Node             | 84.1       | 0.003              | [Node.io](https://example.com/node)        |
| Cluster          | 13.7       | 42.0               | [Cluster](https://example.com/cluster)     |
| Entangler        | ∞          | 7.8                | [Entangler](https://example.com/entangler) |""",
                    "Inline code can be used to denote variables like `theta`, `λ`, or `Markdown`.",
                    "Be cautious when applying multi-spatial dampening to **sub-quadratic manifolds**.",
                ],
            ),
            (
                """### Block 3: Lists and quotes

1. Initialize the **frob layer**:
    - Compute delta flux.
    - Adjust *pseudo-nodal bias* if necessary.
        - Note: do **not** conflate with semi-factual torsion fields.
2. Iterate through *orbital segments*:
    1. Deconstruct local loops.
    1. Re-synchronize dampened echoes.
3. Finalize with an ephemeral mutex.

> “Every mutex is a promise, and every promise is a ghost.” – Prof. Wibble

_Italics_ can suggest uncertainty, while **bold text** affirms conviction.""",
                [
                    "### Block 3: Lists and quotes",
                    """1. Initialize the **frob layer**:
    - Compute delta flux.
    - Adjust *pseudo-nodal bias* if necessary.
        - Note: do **not** conflate with semi-factual torsion fields.
2. Iterate through *orbital segments*:
    1. Deconstruct local loops.
    1. Re-synchronize dampened echoes.
3. Finalize with an ephemeral mutex.""",
                    "> “Every mutex is a promise, and every promise is a ghost.” – Prof. Wibble",
                    "_Italics_ can suggest uncertainty, while **bold text** affirms conviction.",
                ],
            ),
            (
                """## Block 4: Images and links

![Sample diagram of a parabolic null field](https://example.com/null-field.png)

[Read more information about null fields](https://example.com/null-field-analysis)

---

To simulate a field discontinuity:

```js
function simulateNullField(amplitude) {
  return amplitude < 0 ? null : Math.sqrt(amplitude) * 3.1415;
}
```""",
                [
                    "## Block 4: Images and links",
                    "![Sample diagram of a parabolic null field](https://example.com/null-field.png)",
                    "[Read more information about null fields](https://example.com/null-field-analysis)",
                    "---",
                    "To simulate a field discontinuity:",
                    """```js
function simulateNullField(amplitude) {
  return amplitude < 0 ? null : Math.sqrt(amplitude) * 3.1415;
}
```""",
                ],
            ),
        ],
    )
    def test_given_markdwon_sections_splits_on_empty_lines(
        self, content, expected
    ) -> None:
        """R-BICEP: Right."""
        test = Markdown(content)
        test_sections = list(test.sections)
        assert test_sections == expected

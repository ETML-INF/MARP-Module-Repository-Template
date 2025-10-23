from docutils import nodes
from docutils.parsers.rst import Directive, directives
import re

def slugify(s: str) -> str:
    # compact, safe pour attributs
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"[^a-zA-Z0-9._\-]", "-", s)
    return s

class AnswerBlockDirective(Directive):
    """
    Usage:
    ```{answer} E-182-ALL01-ids-q1
    :label: Décrivez les étapes d'un IDS
    :lang: shell
    ```
    - Argument (optionnel) = id stable (conseillé).
    - :label: (optionnel) libellé explicite (sinon pris au titre précédent côté JS).
    - :lang:  (optionnel) ex. shell | powershell | javascript | text/x-csharp ...
    """
    required_arguments = 0
    optional_arguments = 1
    has_content = False
    option_spec = {
        "label": directives.unchanged,
        "lang": directives.unchanged,
    }

    def run(self):
        env = getattr(self.state.document.settings, "env", None)
        docname = env.docname if env else "page"
        data_id = self.arguments[0] if self.arguments else ""
        if not data_id:
            # ID déterministe: docname + numéro de ligne de la directive
            data_id = slugify(f"{docname}-answer-L{self.lineno}")

        label = self.options.get("label", "")
        lang  = self.options.get("lang", "")

        attrs = [f'data-id="{data_id}"']
        if label:
            attrs.append(f'data-label="{label}"')
        if lang:
            attrs.append(f'data-lang="{lang}"')

        html = [
            f'<div class="answer-block" {" ".join(attrs)}>',
            '<textarea class="answer-area"></textarea>',
            '</div>',
        ]
        return [nodes.raw("", "\n".join(html), format="html")]

class ExportAnswersDirective(Directive):
    has_content = False
    option_spec = {}
    def run(self):
        return [nodes.raw(
            "",
            '<button id="export-answers" class="export-btn">📥 Exporter mes réponses</button>',
            format="html"
        )]

def setup(app):
    app.add_directive("answer", AnswerBlockDirective)
    app.add_directive("export-answers", ExportAnswersDirective)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

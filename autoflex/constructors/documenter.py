from autoflex.types.core import AutoflexBaseModel
from sphinx.ext.autodoc import Documenter

class AutoflexDocumenter(Documenter):
    objtype = 'flex'
    # Optionally set a priority to override standard documenters if necessary
    priority = 10  # higher priority wins if multiple documenters match

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        # Determine if this documenter should handle the given member
        return isinstance(member, AutoflexBaseModel)

    def add_directive_header(self, sig):
        # Customize the directive header if necessary
        self.add_line(f".. autoclass:: {self.name}", self.get_sourcename())
        super().add_directive_header(sig)

    def add_content(self, more_content, no_docstring=False):
        # Add content related to the custom member
        super().add_content(more_content, no_docstring)

    def generate(self, *args, **kwargs):
        # Customize generation logic if necessary
        super().generate(*args, **kwargs)


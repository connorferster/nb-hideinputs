"""
A simple exporter for nbconvert (>= 7.0.0) that hides all input cells
in the export. Adds export options to JupyterLab's "export as" menu.
"""

__version__ = "0.1.1"

from nbconvert import PDFExporter, HTMLExporter, LatexExporter
from copy import deepcopy


class HTMLHideInputExporter(HTMLExporter):
    """
    Exports HTML documents without input cells.
    """

    export_from_notebook = "HTML Hide Input"

    exclude_input = deepcopy(HTMLExporter.exclude_input)
    exclude_input.default_value = True


class PDFHideInputExporter(PDFExporter):
    """
    Exports PDF documents without input cells.
    """

    export_from_notebook = "PDF Hide Input"
    exclude_input = deepcopy(PDFExporter.exclude_input)
    exclude_input.default_value = True


class LatexHideInputExporter(LatexExporter):
    """
    Exports LaTeX documents without input cells.
    """

    export_from_notebook = "LaTeX Hide Input"
    exclude_input = deepcopy(LatexExporter.exclude_input)
    exclude_input.default_value = True

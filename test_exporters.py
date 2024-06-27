from nb_hideinputs import (
    LatexHideInputExporter,
    HTMLHideInputExporter,
    PDFHideInputExporter,
)

def test_latex_exporter():
    exporter = LatexHideInputExporter()
    assert exporter.exclude_input == True
    parent = exporter.__class__.__bases__[0]()
    assert parent.exclude_input == False


def test_pdf_exporter():
    exporter = PDFHideInputExporter()
    assert exporter.exclude_input == True
    parent = exporter.__class__.__bases__[0]()
    assert parent.exclude_input == False


def test_html_exporter():
    exporter = HTMLHideInputExporter()
    assert exporter.exclude_input == True
    parent = exporter.__class__.__bases__[0]()
    assert parent.exclude_input == False


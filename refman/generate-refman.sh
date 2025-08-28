#!/bin/bash

PROJECT_NAME="Viz3DVideo"
PACKAGE_NAME="viz3dvideo"
PACKAGE_PARENT_PATH="../src"
DOCS_PATH="./ref"

mkdir -p $DOCS_PATH

# --- 1. Cria docs com sphinx-quickstart não interativo ---
sphinx-quickstart $DOCS_PATH \
    -q \
    -p $PROJECT_NAME \
    -a "Fernando Pujaico Rivera" \
    --sep \
    --makefile \
    --batchfile

# --- 2. Ajusta conf.py ---
CONF_FILE="$DOCS_PATH/source/conf.py"
if [ -f "$CONF_FILE" ]; then
    # Define tema ReadTheDocs
    sed -i "s/html_theme = 'alabaster'/html_theme = 'sphinx_rtd_theme'/" $CONF_FILE

    # Ativa autodoc e napoleon
    sed -i "s/extensions = \[/extensions = \['sphinx.ext.autodoc', 'sphinx.ext.napoleon', /" $CONF_FILE


else
    echo "Erro: conf.py não encontrado em $CONF_FILE"
    exit 1
fi

echo "Sphinx configurado para autodoc, napoleon e tema ReadTheDocs."


# --- 2.1 Adiciona modules.rst ao toctree do index.rst ---
INDEX_FILE="$DOCS_PATH/source/index.rst"
if [ -f "index.rst" ]; then
    cp "index.rst" "$INDEX_FILE"
    echo "index.rst atualizado com o template."
fi

# --- 2.2 ---
echo ".. |version| replace:: $(PYTHONPATH=../src python3 -c 'from viz3dvideo.about import __version__; print(__version__)')" > $DOCS_PATH/source/version.rst


# --- 3. Gera arquivos .rst para todos os módulos do pacote ---
sphinx-apidoc -o $DOCS_PATH/source $PACKAGE_PARENT_PATH/$PACKAGE_NAME

# --- 4. Build HTML ---
cd $DOCS_PATH
make clean
PYTHONPATH=../../src make html

echo "Documentation created in $DOCS_PATH/build/html/index.html"


#!/bin/bash

set -e

echo "🔧 Configurando ambiente do Lab-01-Flask..."

if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
else
    echo "✅ Ambiente virtual já existe."
fi

echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate

echo "📥 Instalando dependências..."
pip install -r requirements.txt

echo "✅ Ambiente pronto! Use 'source venv/bin/activate' para ativar em novas sessões."

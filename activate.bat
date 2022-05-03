@echo off
chcp 65001
echo Iniciar configuração ...
python -V

if not exist "venv" (
    echo Criando ambiente virtual ...
    python -m venv venv
)

echo Instalando as bibliotecas necessárias ...
.\venv\Scripts\pip install -r requirements.txt

if not exist "refreship.bat" (
    echo Criando arquivo de execução refreship.bat ...
    echo %~dp0venv\Scripts\python %~dp0refreship.bat
    echo %~dp0venv\Scripts\python %~dp0refreship > refreship
)
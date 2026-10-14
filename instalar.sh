#!/bin/sh
# Instalador para Calculadora - theking-cs

echo "********************************************************"
echo "* Instalando Calculadora V1.2                        *"
echo "********************************************************"

PLUGIN_NAME="Calculadora"
PLUGIN_PATH="/usr/lib/enigma2/python/Plugins/Extensions/$PLUGIN_NAME"

# Limpiar carpetas temporales y previas
rm -rf $PLUGIN_PATH
rm -rf /tmp/Calculadora.zip
rm -rf /tmp/Calculadora-main
rm -rf /tmp/Calculadora-master

echo "> Descargando desde GitHub..."
wget --no-check-certificate https://github.com/theking-cs/Calculadora/archive/refs/heads/main.zip -O /tmp/Calculadora.zip

if [ ! -f /tmp/Calculadora.zip ]; then
    echo "Error: No se pudo descargar el archivo."
    exit 1
fi

echo "> Extrayendo archivos..."
python3 -c "import zipfile; zipfile.ZipFile('/tmp/Calculadora.zip', 'r').extractall('/tmp/')"

# Detectar automáticamente si la carpeta extraída es main o master
if [ -d /tmp/Calculadora-main ]; then
    mv /tmp/Calculadora-main $PLUGIN_PATH
elif [ -d /tmp/Calculadora-master ]; then
    mv /tmp/Calculadora-master $PLUGIN_PATH
else
    echo "Error: No se encontró la carpeta extraída."
    exit 1
fi

echo "> Configurando permisos..."
chmod -R 755 $PLUGIN_PATH

# Limpieza
rm -rf /tmp/Calculadora.zip

echo "********************************************************"
echo "* INSTALACIÓN COMPLETADA - REINICIANDO ENIGMA2       *"
echo "********************************************************"
killall -9 enigma2

exit 0

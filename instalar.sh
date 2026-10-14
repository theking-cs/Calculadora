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

echo "> Descargando desde GitHub..."
wget --no-check-certificate https://github.com/theking-cs/Calculadora/archive/refs/heads/main.zip -O /tmp/Calculadora.zip

echo "> Extrayendo archivos..."
unzip -q /tmp/Calculadora.zip -d /tmp/

echo "> Instalando en el sistema..."
mv /tmp/Calculadora-main $PLUGIN_PATH

# Dar permisos
echo "> Configurando permisos..."
chmod -R 755 $PLUGIN_PATH

# Limpieza
rm -rf /tmp/Calculadora.zip

echo "********************************************************"
echo "* INSTALACIÓN COMPLETADA - REINICIANDO ENIGMA2       *"
echo "********************************************************"
killall -9 enigma2

exit 0

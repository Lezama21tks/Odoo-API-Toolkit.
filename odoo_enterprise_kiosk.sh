#!/bin/bash
# Odoo Enterprise Kiosk Mode - v2026.1
# Solución de terminal ligero para acceso seguro a ERP vía Red Local.

echo "--- INICIANDO TERMINAL DE ACCESO SEGURO ---"

# Configuración de Red Genérica
SERVER_IP="192.168.1.100" 
PORT="8069"

echo "Verificando conexión con el servidor central de la empresa..."
if ping -c 1 $SERVER_IP &> /dev/null
then
    echo "Servidor detectado. Abriendo interfaz de usuario..."
    # Modo Kiosko: Pantalla completa, sin barras de navegación, directo al Login
    firefox --kiosk "http://$SERVER_IP:$PORT/web/login"
else
    echo "ERROR: Fallo de red. Por favor, verifique el cable de red o el router."
fi

import xmlrpc.client
import time

# Configuración de Odoo
url = 'https://tu-instancia.odoo.com'
db = 'mi_base_de_datos'
username = 'admin'
api_key = 'tu_llave_api'

def registrar_actividad_iot(user_id, estado):
    """
    Simula la conexión entre un sensor de movimiento/cámara 
    y el módulo de asistencia de Odoo.
    """
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    if estado == "movimiento_detectado":
        # Acción en Odoo: Registrar entrada o actividad
        print(f"Propagando señal a Odoo: Usuario {user_id} está ACTIVO.")
        # Aquí se llamaría al método de Odoo hr.attendance
    else:
        print(f"Alerta: No se detecta actividad para el Usuario {user_id}.")

# Simulación de Monitoreo en Tiempo Real (CFTV + Sensor PIR)
def monitorear_estacion_trabajo():
    usuarios = [21, 45, 12] # IDs de ejemplo de Odoo
    
    for user in usuarios:
        print(f"\n[SCANNING] Verificando cámara y sensor de Usuario ID: {user}")
        
        # Simulación de sensor (True = Hay alguien trabajando)
        sensor_movimiento = True 
        
        if sensor_movimiento:
            registrar_actividad_iot(user, "movimiento_detectado")
        else:
            registrar_actividad_iot(user, "ausente")
        time.sleep(1)

if __name__ == "__main__":
    monitorear_estacion_trabajo()

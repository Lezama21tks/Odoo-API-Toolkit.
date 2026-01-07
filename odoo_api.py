import xmlrpc.client

# Proyecto Odoo 17/18 por Lezama21tks
url = 'https://demo.odoo.com'
db = 'mi_base_de_datos'
username = 'admin'
api_key = 'tu_llave_api'

# Conexión XML-RPC
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, api_key, {})

if uid:
    print(f"¡Conexión exitosa! ID de Usuario: {uid}")
else:
    print("Error: No se pudo conectar a Odoo.")

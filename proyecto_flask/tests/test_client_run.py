from app import app, characters, weapons

client = app.test_client()

# Clear any existing
characters.clear()
weapons.clear()

# Post a personaje (with vision and nacion)
resp1 = client.post('/nuevo', data={'tipo':'personaje','nombre':'Nahida','rol':'Support','vision':'Dendro','nacion':'Sumeru'}, follow_redirects=True)
print('POST personaje status', resp1.status_code)

# Post a arma
resp2 = client.post('/nuevo', data={'tipo':'arma','nombre_arma':'Aquila Favonia','rarity':'5★'}, follow_redirects=True)
print('POST arma status', resp2.status_code)

# Get /ver
resp3 = client.get('/ver')
print('/ver status', resp3.status_code)
text = resp3.get_data(as_text=True)
print('Contains Nahida?', 'Nahida' in text)
print('Contains Aquila Favonia?', 'Aquila Favonia' in text)

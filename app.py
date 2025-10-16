from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'cambiame_por_una_clave_segura'

# Datos temporales: listas de diccionarios para personajes y armas
characters = []
weapons = []


@app.route('/')
def index():
    # Simple index render (hero illustration embedded in template)
    return render_template('index.html')


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        tipo = request.form.get('tipo')

        if tipo == 'personaje':
            nombre = request.form.get('nombre', '').strip()
            rol = request.form.get('rol', '').strip()
            vision = request.form.get('vision', '').strip()
            nacion = request.form.get('nacion', '').strip()

            if not nombre:
                flash('El nombre del personaje es obligatorio.', 'error')
                return redirect(url_for('nuevo'))

            personaje = {
                'id': len(characters) + 1,
                'nombre': nombre,
                'rol': rol,
                'vision': vision,
                'nacion': nacion
            }
            characters.append(personaje)
            flash('Personaje registrado correctamente.', 'success')
            return redirect(url_for('ver'))

        elif tipo == 'arma':
            nombre = request.form.get('nombre_arma', '').strip()
            rarity_raw = request.form.get('rarity', '').strip()

            # Validar que rarity sea un entero positivo
            try:
                rarity = int(rarity_raw) if rarity_raw != '' else None
            except ValueError:
                flash('La rareza debe ser un número entero.', 'error')
                return redirect(url_for('nuevo'))

            if not nombre:
                flash('El nombre del arma es obligatorio.', 'error')
                return redirect(url_for('nuevo'))

            arma = {
                'id': len(weapons) + 1,
                'nombre': nombre,
                'rarity': rarity
            }
            weapons.append(arma)
            flash('Arma registrada correctamente.', 'success')
            return redirect(url_for('ver'))

        else:
            flash('Tipo inválido.', 'error')
            return redirect(url_for('nuevo'))

    return render_template('nuevo.html')


@app.route('/ver')
def ver():
    return render_template('ver.html', characters=characters, weapons=weapons)


def _find_item(items, item_id):
    for item in items:
        if item['id'] == item_id:
            return item
    return None


@app.route('/personajes/<int:personaje_id>', methods=['PUT', 'DELETE'])
def gestionar_personaje(personaje_id):
    personaje = _find_item(characters, personaje_id)
    if not personaje:
        return jsonify({'error': 'Personaje no encontrado.'}), 404

    if request.method == 'DELETE':
        characters.remove(personaje)
        flash('Personaje eliminado correctamente.', 'success')
        return jsonify({'message': 'Personaje eliminado.'}), 200

    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre', '').strip()
    rol = data.get('rol', '').strip()
    vision = data.get('vision', '').strip()
    nacion = data.get('nacion', '').strip()

    if not nombre:
        return jsonify({'error': 'El nombre del personaje es obligatorio.'}), 400

    personaje.update({
        'nombre': nombre,
        'rol': rol,
        'vision': vision,
        'nacion': nacion
    })
    flash('Personaje actualizado correctamente.', 'success')
    return jsonify({'message': 'Personaje actualizado.', 'personaje': personaje}), 200


@app.route('/armas/<int:arma_id>', methods=['PUT', 'DELETE'])
def gestionar_arma(arma_id):
    arma = _find_item(weapons, arma_id)
    if not arma:
        return jsonify({'error': 'Arma no encontrada.'}), 404

    if request.method == 'DELETE':
        weapons.remove(arma)
        flash('Arma eliminada correctamente.', 'success')
        return jsonify({'message': 'Arma eliminada.'}), 200

    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre', '').strip()
    rarity_raw = data.get('rarity', '')

    # Allow numeric input or string that can be converted
    if isinstance(rarity_raw, (int, float)):
        rarity_val = int(rarity_raw)
    else:
        try:
            rarity_val = int(str(rarity_raw).strip()) if str(rarity_raw).strip() != '' else None
        except (ValueError, TypeError):
            return jsonify({'error': 'La rareza del arma debe ser un número entero.'}), 400

    rarity = rarity_val

    if not nombre:
        return jsonify({'error': 'El nombre del arma es obligatorio.'}), 400

    arma.update({
        'nombre': nombre,
        'rarity': rarity
    })
    flash('Arma actualizada correctamente.', 'success')
    return jsonify({'message': 'Arma actualizada.', 'arma': arma}), 200


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash

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
            rarity = request.form.get('rarity', '').strip()

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


if __name__ == '__main__':
    app.run(debug=True)

@places.route('/places', methods=['GET'])
def list_places():
    places = Place.query.all()
    return render_template('places.html', places=places)

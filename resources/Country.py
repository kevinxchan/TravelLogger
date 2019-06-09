from flask import request
from flask_restful import Resource
from model import db, Country, CountrySchema


countries_schema = CountrySchema(many=True)
country_schema = CountrySchema()


class CountryResource(Resource):
    def get(self):
        countries = Country.query.all()
        countries = countries_schema.dump(countries).data
        return {'status': 'success', 'data': countries}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if json_data is None:
            return {'message': 'No input data provided'}, 400
        data, errors = country_schema.load(json_data)
        if errors:
            return errors, 422
        country = Country.query.filter_by(name=data['name']).first()
        if country:
            return {'message': 'Country already exists'}, 400

        country = Country(name=json_data['name'])
        db.session.add(country)
        db.session.commit()
        result = country_schema.dump(country).data
        return {'status': 'success', 'data': result}, 200

    def delete(self):
        json_data = request.get_json(force=True)
        if json_data is None:
            return {'message': 'No input data provided'}, 400
        data, errors = country_schema.load(json_data)
        if errors:
            return errors, 422
        country = Country.query.filter_by(id=data['id'])
        result = country_schema.dump(country).data
        country.delete()
        db.session.commit()
        return {'status': 'success', 'data': result}, 200

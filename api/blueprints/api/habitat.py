from api.models import db, Reading, EnvironmentConfig
from api.blueprints import utils

from marshmallow import Schema, fields, post_load

from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort

bp = Blueprint("habitat", __name__)


class ReadingSchema(Schema):
    temperature = fields.Decimal(required=True, place=1)
    humidity = fields.Decimal(required=True, places=1)
    time = fields.DateTime(required=True)


class FilterReadingsSchema(Schema):
    unit = fields.Str(required=False, allow_none=True)
    period = fields.Int(required=False, allow_none=True)
    date_from = fields.Date(required=False, allow_none=True)
    date_to = fields.Date(required=False, allow_none=True)

    @post_load
    def validate_unit(self, data, **kwargs):
        if data.get("unit") is not None:
            if data.get("period") is None:
                abort(
                    404,
                    message="If filtering by period, a unit of time must be provided",
                )
        return data


class ListReadingsSchema(ReadingSchema):
    readings = fields.List(
        fields.Nested(ReadingSchema(only=("temperature", "humidity", "time")))
    )


class ConfigSchema(Schema):
    lights_on_time = fields.Time(required=True, allow_none=False)
    lights_off_time = fields.Time(required=True, allow_none=False)
    day_h_sp = fields.Decimal(required=True, allow_none=False, places=1)
    day_l_sp = fields.Decimal(required=True, allow_none=False, places=1)
    night_h_sp = fields.Decimal(required=True, allow_none=False, places=1)
    night_l_sp = fields.Decimal(required=True, allow_none=False, places=1)
    humidity_h_sp = fields.Decimal(required=True, allow_none=False, places=1)
    humidity_l_sp = fields.Decimal(required=True, allow_none=False, places=1)
    created = fields.DateTime(required=False)


@bp.route("/reading/")
class HabitatReading(MethodView):
    @bp.response(200, ReadingSchema(only=("temperature", "humidity")))
    def get(self, **kwargs):
        reading = Reading.query.order_by(Reading.time.desc()).first()
        if reading is None:
            abort(404, message="A reading has not yet been taken!")

        return reading

    @bp.arguments(ReadingSchema(only=("temperature", "humidity")))
    @bp.response(201)
    def post(self, data, **kwargs):
        reading = Reading(temperature=data["temperature"], humidity=data["humidity"])
        db.session.add(reading)
        db.session.commit()


@bp.route("/readings/")
class HabitatReadings(MethodView):
    @bp.arguments(FilterReadingsSchema(only=("period", "unit", "date_from", "date_to")))
    @bp.response(200, ListReadingsSchema(many=True))
    def get(self, data, **kwargs):
        readings = Reading.find()

        if data.get("period") is not None:
            readings = Reading.find(period=data["period"], unit=data["unit"])
        elif data.get("date_from") is not None:
            if data.get("date_to") is None:
                data["date_to"] = datetime.utcnow().date()
            readings = Reading.find(
                date_from=data["date_from"], date_to=data["date_to"]
            )
        else:
            abort(404, message="A method to filter by must be provided")

        reads = [utils.localise_tz("reading", r) for r in readings.all()]
        return reads


@bp.route("/config/")
class HabitatConfig(MethodView):
    @bp.response(200, ConfigSchema)
    def get(self, **kwargs):
        env = EnvironmentConfig.query.order_by(EnvironmentConfig.created.desc()).first()
        if env is None:
            abort(404, message="An environment configuration has not yet been saved!")
        return utils.localise_tz("environment", env)

    @bp.arguments(
        ConfigSchema(
            only=(
                "lights_on_time",
                "lights_off_time",
                "day_h_sp",
                "day_l_sp",
                "night_h_sp",
                "night_l_sp",
                "humidity_h_sp",
                "humidity_l_sp",
            )
        )
    )
    @bp.response(201, ConfigSchema)
    def post(self, data, **kwargs):
        env = EnvironmentConfig.factory(data)
        return utils.localise_tz("environment", env)


@bp.route("/config/new/")
class NewHabitatConfig(MethodView):
    @bp.response(200, ConfigSchema)
    def get(self, data, **kwargs):
        env = EnvironmentConfig.factory()
        return utils.localise_tz("environment", env)

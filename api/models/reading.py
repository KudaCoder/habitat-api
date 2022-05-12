from sqlalchemy import func

from datetime import datetime, timedelta, timezone

from . import db


class Reading(db.Model):  
    __tablename__ = "reading"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def find(*args, **kwargs):
        query = Reading.query
        
        if kwargs.get("unit"):
            days = 0
            hours = 0
            minutes = 0

            if kwargs["unit"] == "days":
                days = kwargs["period"]
            elif kwargs["unit"] == "hours":
                hours = kwargs["period"]
            elif kwargs["unit"] == "minutes":
                minutes = kwargs["period"]

            now = datetime.now(timezone.utc)
            delta = timedelta(days=days, hours=hours, minutes=minutes)
            query = query.filter(Reading.time <= now, Reading.time >= (now - delta))
        
        if kwargs.get("date_from"):
            query = query.filter(Reading.time >= kwargs["date_from"])
        
            if kwargs.get("dateTo"):
                query = query.filter(Reading.time < kwargs["dateTo"])
        
        query = query.order_by(Reading.time)
        return query

    @staticmethod
    def to_dict(reading, *args, **kwargs):
        return {
            "temperature": reading.temperature,
            "humidity": reading.humidity,
            "time": reading.time,
        }

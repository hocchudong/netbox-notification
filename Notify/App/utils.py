import datetime
import logging

def format_timestamp(ts):
    try:
        try:
            ts_float = float(ts)
            dt = datetime.datetime.fromtimestamp(ts_float)
        except ValueError:
            dt = datetime.datetime.fromisoformat(ts)
        return dt.strftime("%d-%m-%Y %H:%M:%S")
    except Exception as e:
        logging.error(f"Error while formating timestamp: {e}")
        return ts
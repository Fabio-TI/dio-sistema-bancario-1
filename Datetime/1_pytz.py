from datetime import datetime
import pytz

data = datetime.now(pytz.timezone('Europe/London'))

print("Data e hora em Londres:", data.strftime("%d/%m/%Y %H:%M"))

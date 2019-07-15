from datetime import datetime

now = datetime.now()#store full date and time right now

#get each form seperatley
mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

print(now)
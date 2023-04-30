from datetime import datetime, timedelta
from quickstart import get_calendar_service


def main():
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=2)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   print(start)



   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'testing iso date format',
           "location": '800 Howard St., San Francisco, CA 94103',
           "description": 'we are just making sure for sure this works',
           "start": {"dateTime": '2023-05-01T10:00:00', "timeZone": 'America/Los_Angeles'},
           "end": {"dateTime": '2023-05-01T11:00:00', "timeZone": 'America/Los_Angeles'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("location: ", event_result['location'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])
   print()

if __name__ == '__main__':
   main()
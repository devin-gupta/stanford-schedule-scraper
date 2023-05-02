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
           "summary": 'Physics Department Senior Thesis Presentation',
           "location": 'PAB 102',
           "description": 'seniors present their thesis work before they graduate',
           "start": {"dateTime": '2023-05-11T13:00:00', "timeZone": 'America/Los_Angeles'},
           "end": {"dateTime": '2023-05-11T16:00:00', "timeZone": 'America/Los_Angeles'},
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
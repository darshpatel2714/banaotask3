from icalendar import Calendar, Event
from datetime import datetime, timedelta
from django.core.mail import EmailMessage

def create_icalendar_event(appointment):
    cal = Calendar()
    event = Event()
    event.add('summary', f'Appointment with {appointment.doctor.get_full_name()}')
    start_datetime = datetime.combine(appointment.appointment_date, appointment.start_time)
    end_datetime = start_datetime + timedelta(minutes=45)
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)
    event.add('description', f'Speciality: {appointment.speciality}')
    event.add('attendee', appointment.patient.email)
    event.add('attendee', appointment.doctor.email)
    cal.add_component(event)
    
    return cal.to_ical()

def send_appointment_email(appointment):
    ical_event = create_icalendar_event(appointment)
    email = EmailMessage(
        subject=f'Appointment Confirmation with {appointment.doctor.get_full_name()}',
        body=f'You have an appointment with {appointment.doctor.get_full_name()} on {appointment.appointment_date} at {appointment.start_time}.',
        to=[appointment.patient.email],
    )
    email.attach('appointment.ics', ical_event, 'text/calendar')
    email.send()
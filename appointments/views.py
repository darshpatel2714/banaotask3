from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Appointment
from .forms import AppointmentForm
from users.models import CustomUser
from .icalendar_utils import send_appointment_email

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(CustomUser, id=doctor_id, user_type='doctor')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            send_appointment_email(appointment)
            return redirect('appointment_confirmation', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form, 'doctor': doctor})

@login_required
def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointments/appointment_confirmation.html', {'appointment': appointment})

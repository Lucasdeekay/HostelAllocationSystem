import datetime
import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from Dashboard.forms import LoginForm, ForgotPasswordForm, ChangePasswordForm, UpdatePasswordForm, RegisterForm, \
    UploadImageForm
from Dashboard.models import Hostel, Room, Student


random = random.Random()


# Create a login view
class LoginView(View):
    # Add template name
    template_name = 'dashboard/login.html'

    # Create get function
    def get(self, request):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('Dashboard:home'))
        # Otherwise
        else:
            #  Get login form
            form = LoginForm()
            # load the page with the form
            return render(request, self.template_name, {'form': form})

    # Create post function to process te form on submission
    def post(self, request):
        # Get the submitted form
        form = LoginForm(request.POST)
        #  Check if the form is valid
        if form.is_valid():
            # Process the input
            username = form.cleaned_data['username'].strip().upper()
            password = form.cleaned_data['password'].strip()
            # Authenticate the user login details
            user = authenticate(request, username=username, password=password)
            # Check if user exists
            if user is not None:
                # Log in the user
                login(request, user)
                # Redirect to dashboard page
                return HttpResponseRedirect(reverse('Dashboard:home'))
            # If user does not exist
            else:
                # Create an error message
                messages.error(request, "Invalid login details")
                # Redirect back to the login page
                return HttpResponseRedirect(reverse('Dashboard:login'))


# Create a forgot password view
class ForgotPasswordView(View):
    # Add template name
    template_name = 'dashboard/forgot_password.html'

    # Create get function
    def get(self, request):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('Dashboard:home'))
        # Otherwise
        else:
            form = ForgotPasswordForm()
            # load the page with the form
            return render(request, self.template_name, {'form': form})

    # Create post function to process the form on submission
    def post(self, request):
        # Get the submitted form
        form = ForgotPasswordForm(request.POST)
        #  Check if the form is valid
        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            email = form.cleaned_data['email'].strip()

            if User.objects.filter(**{'username': username, 'email': email}).exists():
                user = User.objects.get(username=username)
                # Redirect back to dashboard if true
                return HttpResponseRedirect(reverse('Dashboard:change_password', args=(user.id,)))
            else:
                messages.success(request, "User details does not match")
                # Redirect back to page
                return HttpResponseRedirect(reverse('Dashboard:forgot_password'))


# Create an update password view
class ChangePasswordView(View):
    template_name = 'dashboard/change_password.html'

    def get(self, request, user_id):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('Dashboard:home'))
        # Otherwise
        else:
            form = ChangePasswordForm()
            user = get_object_or_404(User, id=user_id)
            context = {'user': user, 'user_id': user_id, 'form': form}
            return render(request, self.template_name, context)

    def post(self, request, user_id):
        if request.method == 'POST':
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                password1 = form.cleaned_data['password'].strip()
                password2 = form.cleaned_data['confirm_password'].strip()

                if password1 == "password":
                    messages.error(request, "Password cannot be 'password'")
                    return HttpResponseRedirect(reverse('Dashboard:update_password', args=(user_id,)))

                else:
                    if password1 == password2:
                        user = User.objects.get(id=user_id)
                        user.set_password(password1)
                        user.save()

                        messages.success(request, 'Password successfully changed')
                        return HttpResponseRedirect(reverse('Dashboard:login'))
                    else:
                        messages.error(request, "Password does not match")
                        return HttpResponseRedirect(reverse('Dashboard:update_password', args=(user_id,)))


class RegisterView(View):
    template_name = "dashboard/register.html"

    def get(self, request):
        # Check if user is logged in
        if request.user.is_authenticated and not request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('Dashboard:home'))
        # Otherwise
        else:
            form = RegisterForm()
            # Go to the register page
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        for hostel in Hostel.objects.all():
            if not Room.objects.filter(hostel=hostel).exists():
                for i in range(hostel.total_rooms):
                    room = Room.objects.create(hostel=hostel, room_no=i + 1)
                    room.save()

        form = RegisterForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name'].strip().upper()
            first_name = form.cleaned_data['first_name'].strip().upper()
            matric_no = form.cleaned_data['matric_no'].strip().upper()
            email = form.cleaned_data['email'].strip()
            gender = form.cleaned_data['gender'].strip()
            password = form.cleaned_data['password'].strip()
            confirm_password = form.cleaned_data['confirm_password'].strip()

            if User.objects.filter(**{"username": matric_no, "email": email}).exists():
                messages.error(request, "User already exists")
                return HttpResponseRedirect(reverse("Dashboard:register"))
            else:
                if password == confirm_password:
                    rooms = Room.objects.filter(space_available__gt=0)
                    free_rooms = [
                        room for room in rooms if room.hostel.gender == gender
                    ]
                    room = random.choice(free_rooms)
                    room.space_available -= 1
                    room.save()
                    user = User.objects.create_user(username=matric_no, password=password, email=email)
                    user.save()
                    Student.objects.create(user=user, last_name=last_name, first_name=first_name, matric_no=matric_no, gender=gender, room=room)
                    messages.success(request, "Registration successful")
                    return HttpResponseRedirect(reverse("Dashboard:login"))
                else:
                    messages.error(request, "Passwords does not match")
                    return HttpResponseRedirect(reverse("Dashboard:register"))


class HomeView(View):
    # Add template name
    template_name = 'dashboard/home.html'

    # @method_decorator(login_required)
    # Create get function
    def get(self, request):
        # Check if user is not logged in
        if request.user.is_superuser:
            # Redirect back to dashboard if true
            return HttpResponseRedirect(reverse('Dashboard:login'))
        # Otherwise
        else:
            form = UpdatePasswordForm()
            image_form = UploadImageForm()
            student = Student.objects.get(user=request.user)
            # load the page with the form
            return render(request, self.template_name, {'form': form, 'image_form': image_form, "student": student, "date": datetime.datetime.now().date()})

    # Create post function to process the form on submission
    def post(self, request):
        # Check if request method is POST
        if request.method == "POST":
            # Get the submitted form
            form = UpdatePasswordForm(request.POST)
            # Check if form is valid
            if form.is_valid():
                # Get user input
                old_password = form.cleaned_data['old_password'].strip()
                password = form.cleaned_data['password'].strip()
                confirm_password = form.cleaned_data['confirm_password'].strip()
                # Check if old password match
                if request.user.check_password(old_password):
                    if password == old_password:
                        # Create message report
                        messages.error(request, "Previous password cannot be used")
                        # return data back to page
                        return HttpResponseRedirect(reverse('Dashboard:home'))
                    elif password == old_password:
                        # Create message report
                        messages.error(request, "You cannot use previous password")
                        # return data back to page
                        return HttpResponseRedirect(reverse('Dashboard:home'))
                    else:
                        # Check if both passwords match
                        if password == confirm_password:
                            # Update password
                            request.user.set_password(password)
                            # Save updated data
                            request.user.save()
                            # Create message report
                            messages.success(request, "Password successfully changed")
                            # return data back to page
                            return HttpResponseRedirect(reverse('Dashboard:login'))
                        # If passwords do not match
                        else:
                            # Create message report
                            messages.error(request, "New password does not match")
                            # return data back to page
                            return HttpResponseRedirect(reverse('Dashboard:home'))
                # Otherwise
                else:
                    messages.error(request, "Old password entered does not match")
                    # return data back to page
                    return HttpResponseRedirect(reverse('Dashboard:home'))


def upload_image(request):
    # Check if request method is POST
    if request.method == "POST":
        # Get the submitted form
        form = UploadImageForm(request.POST, request.FILES)
        # Check if form is valid
        if form.is_valid():
            # Get user input
            image = form.cleaned_data['image']
            student = get_object_or_404(Student, user=request.user)
            student.image = image
            student.save()
            # Create a dictionary of data to be returned to the page
            messages.success(request, "Profile picture successfully updated")
            # return data back to page
            return HttpResponseRedirect(reverse("Dashboard:home"))


# Create a logout view
class LogoutView(View):

    # Add a method decorator to make sure user is logged in
    @method_decorator(login_required())
    # Create get function
    def get(self, request):
        # logout user
        logout(request)
        # redirect to login page
        return HttpResponseRedirect(reverse('Dashboard:login'))
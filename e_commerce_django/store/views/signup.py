"""Signup view."""

from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from loguru import logger

from e_commerce_django.store.models.customer import Customer


class SignUp(View):
    def get(self, request):
        return render(request, "store/signup.html")

    def post(self, request: HttpRequest):
        post_data = request.POST
        first_name = post_data.get("firstname")
        last_name = post_data.get("lastname")
        phone = post_data.get("phone")
        email = post_data.get("email")
        password = post_data.get("password")

        # Validation
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
        }
        error_message = None

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )
        error_message = self.validate_customer(customer)

        if not error_message:
            logger.info(
                f"Subscriber: {first_name} {last_name}, phone: {phone}, email:\
 {email}, password: {password}"
            )

            customer.password = make_password(customer.password)
            customer.register()
            return redirect("homepage")

        else:
            data = {
                "error": error_message,
                "values": value,
            }
            return render(request, "store/signup.html", data)

    def validate_customer(self, customer: Customer):
        error_message = None
        if not customer.first_name:
            error_message = "Please enter your first name!"
        elif len(customer.first_name) < 3:
            error_message = "First name must be 3 characters long or more"
        elif not customer.last_name:
            error_message = "Please enter your last name"
        elif len(customer.last_name) < 3:
            error_message = "Last name must be 3 characters long or more"
        elif not customer.phone:
            error_message = "Enter your phone number"
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 characters long"
        elif len(customer.email) < 5:
            error_message = "Password must be 5 characters long"
        elif customer.exists():
            error_message = "Email address already registered..."

        return error_message

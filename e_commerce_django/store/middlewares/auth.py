from django.http import HttpRequest
from django.shortcuts import redirect
from loguru import logger


def auth_middleware(get_response):
    """One time configuration and initialization."""

    def middleware(request: HttpRequest):
        logger.info(request.session.get("customer"))
        return_url = request.META["PATH_INFO"]
        logger.info(request.META["PATH_INFO"])

        if not request.session.get("customer"):
            return redirect(f"login?return_url={return_url}")

        response = get_response(request)

        return response

    return middleware

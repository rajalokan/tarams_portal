from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger(__name__)


@login_required(login_url='/accounts/login/')
def test_page(request):
    logger.debug("test_page")
    return HttpResponse("success")

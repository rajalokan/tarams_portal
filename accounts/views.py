'''
Created on Oct 9, 2013

@author: alok
'''
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    pass

from django.conf import settings # import the settings file

def cur_app(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {'app': 'capi_area'}
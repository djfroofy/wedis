from klein import route


@route('/')
def home(request):
    return "<h1>Welcome to Wedis</h1>"

from klein import run, route


@route('/')
def home(request):
    return "Hello World!"


run("localhost", 8080)

from Taskify_main.models import SystemVariables


def system_variables(request):
    variables = dict()
    for i in SystemVariables.objects.only_active():
        variables[i.code] = i.value

    return variables

from django.shortcuts import render

def index(request):
    result = None
    error = None
    num1 = ''
    num2 = ''
    op = ''
    if request.method == 'POST':
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        op = request.POST.get('operation', '')

        try:
            num1_float = float(num1)
            num2_float = float(num2)
            if op == 'add':
                result = num1_float + num2_float
            elif op == 'subtract':
                result = num1_float - num2_float
            elif op == 'multiply':
                result = num1_float * num2_float
            elif op == 'divide':
                if num2_float == 0:
                    error = 'Cannot divide by zero'
                    result = None
                else:
                    result = num1_float / num2_float
            else:
                error = 'Invalid operation'
                result = None
        except ValueError:
            error = 'Invalid input: please enter valid numbers'
            result = None

    context = {
        'result': result,
        'error': error,
        'num1': num1,
        'num2': num2,
        'operation': op,
    }
    return render(request, 'calc/index.html', context)

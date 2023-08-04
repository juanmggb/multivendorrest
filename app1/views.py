from django.shortcuts import render, get_object_or_404
from app1.models import Employee


# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()

    print(employees)

    context = {
        "employees": employees,
    }
    return render(request, "employee-list.html", context=context)
    # return render(request, "app1/index.html")


def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    print(employee)

    return render(
        request,
        "employee-detail.html",
        context={
            "employee": employee,
        },
    )

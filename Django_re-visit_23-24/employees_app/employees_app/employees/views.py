from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from employees_app.employees.models import Employee


def validate_negative_age(age):
    if age < 0:
        raise ValidationError('Age must be positive! Try again!')


# Create your views here.
#
# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter your first name',
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Firs Name'}
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'})
#     )
#
#     age = forms.IntegerField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={'type': 'text',
#                    'class': 'form-control', 'placeholder': 'Age'},
#
#         ),
#         validators=(
#             validate_negative_age,
#         )
#     )


class EmployeeFormBase(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class CreateEmployeeFormBase(EmployeeFormBase):
    # age = forms.IntegerField(
    #     validators=[validate_negative_age, ]
    # )
    class Meta:
        model = Employee
        fields = '__all__'
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={'class': 'form-control', }   # to make the field longer
        #     )
        # }


class EditEmployeeFormBase(EmployeeFormBase):
    # def clean(self):     # validation of the forms from here
    #     pass
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'disabled': 'disabled'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
        ),
    )


def home(request):
    context = {
        'employee_form': CreateEmployeeFormBase()
    }

    return render(request, 'home.html', context)


def create_employee(request):
    if request.method == 'POST':
        employee_form = CreateEmployeeFormBase(request.POST)
        if employee_form.is_valid():
            employee_form.save()

            return redirect('home')
    else:
        employee_form = CreateEmployeeFormBase()

    context = {
        'employee_form': employee_form,
    }
    return render(request, 'create_employee.html', context)


def log_in(request):
    return render(request, 'log_in.html')


def employees_list(request):
    employees_order_form = EmployeeOrderForm(request.GET)
    employees_order_form.is_valid()
    order_by = employees_order_form.cleaned_data.get('order_by', 'first_name')
    context = {
        'employees': Employee.objects.order_by(order_by).all(),
        'employees_order_form': employees_order_form,

    }
    return render(request, 'employees_list.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee_form = EditEmployeeFormBase(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()

            return redirect('home')
    else:
        employee_form = EditEmployeeFormBase(instance=employee)
    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit_employee.html', context)

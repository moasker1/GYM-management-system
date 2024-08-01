from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime,timedelta
from django.db.models import F
import pytz
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation, DecimalException
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import RecentAction , Client , Payment, Product
from django.contrib.auth.models import User
from datetime import timedelta


#====================================================================================================================
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'هناك خطأ في اسم المستخدم او كلمة المرور')

    return render(request, 'login.html')
#====================================================================================================================
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')
#====================================================================================================================
@login_required(login_url="login")

def home(request) :
    return render(request, "home.html")
#====================================================================================================================
@login_required(login_url="login")
def products(request):
    products = Product.objects.all()

    paginator = Paginator(products ,20)
    page = request.GET.get('page')
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage :
        product_list = paginator.page(paginator.num_pages)

    if "addSale" in request.POST :
        name = request.POST.get('name')
        num = request.POST.get('num')  
        price = request.POST.get('price')

        price = Decimal(price)
        num = Decimal(num)

        if price == 0 :
            messages.warning(request, "السعر اقل من صفر")
            return redirect("products")
        if num == 0 :
            messages.warning(request, "السعر اقل من صفر")
            return redirect("products")
        

        new_product = Product.objects.create(name=name, price=price, num=num)
        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='اضافة منتج',
            action_sort = 'منتج',
            model_affected=f'تم اضافة منتج ({new_product.name})  و بسعر ({new_product.price} جنيه)',
        )

        messages.success(request, "تمت إضافة منتج بنجاح")
        return redirect("products")
        
    
    elif 'search' in request.POST :
        search_input = request.POST.get('searchInput')
        results = [result['id'] for result in Product.objects.all().filter(Q(name__icontains=search_input)).values()]
        product_list = [Product.objects.get(pk = id) for id in results]

    pro_number = Product.objects.count()
    pro_number = pro_number or 0

    context ={
        "products" : product_list,
        "pro_number" : pro_number,
    }
    return render(request, 'products.html', context)
#====================================================================================================================
def sale_update(request, id):
    old_product_data = Product.objects.values().get(id=id)

    if "saleUpdate" in request.POST:
        name = request.POST["name"]
        price = request.POST["price"]
        num = request.POST["num"]

        num = Decimal(num)
        price = Decimal(price)


        edit = Product.objects.get(id=id)

        old_name = old_product_data["name"]
        old_price = old_product_data["price"]
        old_num = old_product_data["num"]

        changes = []
        if name != old_name:
            changes.append(f'المنتج من {old_name} إلى {name}')
        if str(num) != str(old_num):
            changes.append(f'الكمية من {old_num} إلى {num}')
        if str(price) != str(old_price):
            changes.append(f'السعر من {old_price} إلى {price}')

        edit.name = name
        edit.price = price
        edit.num = num
        edit.save()

        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='تعديل منتج',
            action_sort = 'تعديل',
            model_affected=f'تم تعديل بيانات المنتج: {", ".join(changes)}',
        )
        messages.success(request, 'تم تعديل بيانات المنتج بنجاح', extra_tags='success')
        return redirect("products")
      
#====================================================================================================================
def sale_delete(request, id):
    sale_to_delete = get_object_or_404(Product, id =id )

    if "saleDelete" in request.POST :
        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='حذف منتج',
            action_sort = 'حذف',
            model_affected=f'تم حذف منتج ({sale_to_delete.name})',
        )
        sale_to_delete.delete()
        messages.success(request, "تم حذف المنتج بنجاح")
        return redirect("products")
    
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
#====================================================================================================================
@login_required(login_url="login")
def clients(request):
    client = Client.objects.all().order_by("-date")
    paginator = Paginator(client, 20)
    page = request.GET.get('page')
    try:
        client_list = paginator.page(page)
    except PageNotAnInteger:
        client_list = paginator.page(1)
    except EmptyPage:
        client_list = paginator.page(paginator.num_pages)

    if "addClient" in request.POST:
        name = request.POST.get('name')
        opening_balance = request.POST.get('opening_balance')  
        phone = request.POST.get('phone')
        notes = request.POST.get('notes')
        date = request.POST.get('date')

        name = name.strip()

        if not opening_balance:
            opening_balance = 0
        if not phone:
            phone = None
        if not notes:
            notes = "-"

        if Client.objects.filter(name=name).exists():
            messages.warning(request, f'اسم العميل ({name}) موجود بالفعل في قاعدة البيانات')
            return redirect('clients')
        
        new_client = Client.objects.create(name=name, opening_balance=opening_balance, date=date, phone=phone, notes=notes)

        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='اضافة عميل',
            action_sort='عميل',
            model_affected=f'تم اضافة عميل ({new_client.name}) بإجمالي مبلغ ({new_client.opening_balance} جنيه)',
        )
        messages.success(request, 'تم إضافة عميل جديد بنجاح', extra_tags='success')
        return redirect('clients')
    current_date = timezone.now().date()
    expiration_date = current_date + timedelta(days=30)  # Calculate date 30 days from now
    target = current_date - timedelta(days=30)  # Calculate date 30 days from now

    
    if 'active' in request.POST:
        results = Client.objects.filter(date__gt=target).values_list('id', flat=True)
        client_list = list(Client.objects.filter(pk__in=results))
    if 'noactive' in request.POST:
        results = Client.objects.filter(date__lt=target).values_list('id', flat=True)
        client_list = list(Client.objects.filter(pk__in=results))

    if 'search' in request.POST:
        search_input = request.POST.get('searchInput')
        results = [result['id'] for result in Client.objects.all().filter(Q(name__icontains=search_input)).values()]
        client_list = [Client.objects.get(pk=id) for id in results]

    context = {
        "clients": client_list,
        'timedelta': timedelta(days=30),
        'today': current_date  # Pass today's date to the template
    }

    return render(request, "clients.html", context)
#====================================================================================================================
def client_update(request, id):
    old_client_data = None

    if 'clientUpdate' in request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        notes = request.POST['notes']
        opening_balance = request.POST['opening_balance']
        date = request.POST['date']

        name = name.strip()

        old_client_data = Client.objects.filter(id=id).values().first()

        if Client.objects.filter(name=name).exclude(id=id).exists():
            messages.warning(request, f'اسم العميل ({name}) موجود بالفعل في قاعدة البيانات')
            return redirect("clientpage", id=id)
        
        edit = Client.objects.get(id=id)
        old_name = old_client_data["name"]
        old_opening_balance = old_client_data["opening_balance"]
        old_phone = old_client_data["phone"]

        changes = []
        if name != old_name:
            changes.append(f'اسم العميل من {old_name} إلى {name}')
        if str(opening_balance) != str(old_opening_balance):
            changes.append(f'المبلغ من {old_opening_balance} إلى {opening_balance}')
        if str(phone) != str(old_phone):
            changes.append(f'الهاتف من {old_phone} إلى {phone}')

        edit.name = name
        edit.phone = phone
        edit.opening_balance = opening_balance
        edit.notes = notes
        edit.date = date
        edit.save()

        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='تعديل عميل',
            action_sort = 'تعديل',
            model_affected=f'تم تعديل بيانات العميل: {", ".join(changes)}',
        )
        messages.success(request, 'تم تعديل بيانات العميل بنجاح', extra_tags='success')
        return redirect("clients")
    
#====================================================================================================================
def client_delete(request, id):
    client_to_delete = get_object_or_404(Client, id =id )

    if "clientDelete" in request.POST :
        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='حذف عميل',
            action_sort = 'حذف',
            model_affected=f'تم حذف العميل ({client_to_delete.name})',
        )
        client_to_delete.delete()
        messages.success(request, "تم حذف العميل بنجاح")
        return redirect("clients")
#====================================================================================================================
@login_required(login_url="login")
def client_page(request, id):
    client = get_object_or_404(Client, id=id)
    sales = Sale.objects.filter(client=client).order_by("-date")
    payments = Payment.objects.filter(client=client).order_by('-date')

    context = {"client": client, "sales": sales, "payments"  : payments}
    return render(request, "clientpage.html", context)
#====================================================================================================================
@login_required(login_url="login")
def profits(request):
    payments = Payment.objects.all().order_by("-date")
    paginator = Paginator(payments ,20)
    page = request.GET.get('page')
    try:
        payment_list = paginator.page(page)
    except PageNotAnInteger:
        payment_list = paginator.page(1)
    except EmptyPage :
        payment_list = paginator.page(paginator.num_pages)

    if "addpay" in request.POST :
        lose = request.POST.get('lose')
        paid_money = request.POST.get('paid_money') 
        date = request.POST.get('date') 

        paid_money = Decimal(paid_money)

        
        if lose is not None:
            new_payment = Payment.objects.create(lose=lose, paid_money=paid_money, date=date )
            RecentAction.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action_type='اضافة مصروف',
                action_sort = 'مصروف',
                model_affected=f'تم اضافة مصروف ({new_payment.lose}) بإجمالي ({new_payment.paid_money} جنيه)',
            )

            messages.success(request, "تمت إضافة مصروف بنجاح")
            return redirect("profits")
        
    elif 'search' in request.POST :
        search_input = request.POST.get('searchInput')
        results = [result['id'] for result in Payment.objects.all().filter(Q(lose__icontains=search_input)).values()]
        payment_list = [Payment.objects.get(pk = id) for id in results]

    loses_month = Payment.objects.filter(date__date=timezone.now().date()).aggregate(Sum('paid_money'))['paid_money__sum']
    loses_month = loses_month or 0

        
    clients = Client.objects.all()
    context ={
        "pays" : payment_list,
        "clients" : clients,
        "loses_month" : loses_month,
    }
    return render(request,"loses.html", context)
#====================================================================================================================
def pay_update(request, id):
    old_pay_data = Payment.objects.values().get(id=id)

    if "payupdate" in request.POST:
        lose = request.POST["lose"]
        paid_money = request.POST["paid_money"]

        paid_money = Decimal(paid_money)

        edit = Payment.objects.get(id=id)

        old_lose = old_pay_data["lose"]
        old_paid_money = old_pay_data["paid_money"]

        changes = []
        if str(lose) != str(old_lose):
            changes.append(f'المصروف من {old_lose} إلى {lose}')
        if str(paid_money) != str(old_paid_money):
            changes.append(f'السعر من {old_paid_money} إلى {paid_money}')

        edit.lose = lose
        edit.paid_money = paid_money
        edit.save()

        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='تعديل مصروف',
            action_sort = 'مصروف',
            model_affected=f'تم تعديل مصروف: {", ".join(changes)}',
        )
        messages.success(request, 'تم تعديل بيانات المصروف بنجاح', extra_tags='success')
        return redirect("profits")

#====================================================================================================================
def pay_delete(request, id):
    pay_to_delete = get_object_or_404(Payment, id =id )

    if "paydelete" in request.POST :
        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='حذف مصروف',
            action_sort = 'حذف',
            model_affected=f'تم حذف مصروف ({pay_to_delete.lose}) و كانت بقيمة ({pay_to_delete.paid_money})',
        )
        pay_to_delete.delete()
        messages.success(request, "تم حذف المصروف بنجاح")
        return redirect("profits")
#====================================================================================================================
@login_required(login_url="login")
def adminPage(request):
    clients_number = Client.objects.count()
    clients_number = clients_number or 0
    total_money = Client.objects.aggregate(Sum('opening_balance'))['opening_balance__sum']
    total_money = total_money or 0
    current_date = timezone.now()
    start_of_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end_of_month = (start_of_month + timedelta(days=32)).replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(seconds=1)

    total_money_per_month = Client.objects.filter(date__gte=start_of_month, date__lte=end_of_month).aggregate(Sum('opening_balance'))['opening_balance__sum']
    total_money_per_month = total_money_per_month or 0
    clients_per_month = Client.objects.filter(date__gte=start_of_month, date__lte=end_of_month).count()

    pro_number = Product.objects.count()
    pro_number = pro_number or 0
    total_prod_value = Product.objects.aggregate(Sum('price'))['price__sum']
    total_prod_value = total_prod_value or 0
    loses_month = Payment.objects.filter(date__gte=start_of_month, date__lte=end_of_month).aggregate(Sum('paid_money'))['paid_money__sum']
    loses_month = loses_month or 0


    if "addUser" in request.POST :
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')

        username = username.strip()

        if not firstname :
            messages.warning(request,"يرجى ادخال نوع الصلاحية")
            return redirect('adminPage')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم موجود بالفعل')
            return redirect('adminPage')

        User.objects.create_user(username=username, password=password, first_name=firstname)
        messages.success(request, 'تم تسجيل مستخدم جديد بنجاح')
        return redirect('adminPage')
    context = {
        'timedelta': timedelta(days=30),
        'total_money' : total_money,
        'clients_number' : clients_number,
        'total_money_per_month': total_money_per_month,
        'users': User.objects.all(),
        "pro_number" : pro_number,
        "loses_month" : loses_month,
        "total_prod_value" : total_prod_value,
        "clients_per_month" : clients_per_month,
    }

    if "search" in request.POST:
        selected_date = request.POST.get('date', None)
        if selected_date:
            # Parse the selected month from the form input
            try:
                selected_month = datetime.strptime(selected_date, '%Y-%m').date()
            except ValueError:
                messages.error(request, 'Invalid date format')
                return redirect('adminPage')
            
            # Calculate start and end of selected month
            start_of_month = selected_month.replace(day=1)
            end_of_month = (start_of_month.replace(month=start_of_month.month % 12 + 1, year=start_of_month.year + start_of_month.month // 12) - timedelta(days=1))
            
            # Calculate total expenses for the selected month
            total_expenses = Payment.objects.filter(date__gte=start_of_month, date__lte=end_of_month).aggregate(Sum('paid_money'))['paid_money__sum']
            total_expenses = total_expenses or 0
            
            context['total_expenses'] = total_expenses or 0
    return render(request,"admin.html",context)
#====================================================================================================================
def user_delete(request, id):
    user_to_delete = get_object_or_404(User, id=id)
    user_to_delete.delete()
    messages.success(request, "تم حذف المستخدم بنجاح")
    return redirect("adminPage")
    
#====================================================================================================================
@login_required(login_url="login")    
def reports(request):

    if "reportsShow" in request.POST:
        date_str = request.POST.get('date')
        try:
            selected_date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'تاريخ غير صالح')
            return redirect('reports')

        recent_actions = RecentAction.objects.filter(timestamp__date=selected_date)
        return render(request, 'reports.html', {
            'recent_actions': recent_actions,
            'selected_date' : selected_date,
        })

    return render(request, 'reports.html')

#====================================================================================================================
def renew(request, id):
    if 'renew' in request.POST:
        
        edit = Client.objects.get(id=id)
        edit.date = timezone.now()
        edit.save()

        RecentAction.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action_type='تجديد اشتراك',
            action_sort = 'تجديد',
            model_affected=f'تم تجديد اشتراك العميل {edit.name}',
        )
        messages.success(request, 'تم تجديد اشتراك العميل بنجاح', extra_tags='success')
        return redirect("clients")
    
        


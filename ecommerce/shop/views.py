from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product,Contact,Orders,OrderUpdate
import json
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        products=Product.objects.all()
        print(products)
        # n=len(products)
        # nslides=n//4 + ceil(n/4-n//4)
        #params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
        # allprods=[[products,range(1,nslides),nslides],
        #           [products,range(1,nslides),nslides]]
        allprods=[]
        catprods=Product.objects.values('category','id')
        print(catprods)
        cats={item['category'] for item in catprods}
        print(cats)
        for cat in cats:
            prod=Product.objects.filter(category=cat)
            print(prod)
            n=len(prod)
            nslides=n//4 + ceil(n/4-n//4)
            allprods.append([prod,range(1,nslides),nslides])
        
        params={'allprods':allprods}
        return render(request,'shop/index.html',params)
    else:
        return HttpResponse("404- No page found.")

def searchMatch(query,item):
    ''' return true only if query matches the item '''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    return False

def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('category','id')
    print(catprods)
    cats={item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        # print(prod)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prod)
        nslides=n//4 + ceil(n/4-n//4)
        if len(prod)!=0:
         allprods.append([prod,range(1,nslides),nslides])
    
    params={'allprods':allprods,'msg':""}
    if len(allprods)==0 or len(query)<4:
        params={'msg':"please make sure to enter relevant search query."}
    return render(request,'shop/search.html',params)


def about(request):
    if request.user.is_authenticated:
     return render(request,'shop/about.html')
    else:
        return HttpResponse("404 not found")


def contact(request):
    
    if request.user.is_authenticated:
        
     if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
        return render(request,'shop/contact.html',{'thank':thank})
     return render(request,'shop/contact.html')

    else:
        return HttpResponse("404 not found")
    
def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        # return HttpResponse(f"{orderId}and{email}")
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    print(updates)
                    #response=json.dumps([updates,order[0].items_json],default=str)
                    response=json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json},default=str)
                    print(response)
                return HttpResponse(response)
            else:
            #    return HttpResponse('else')
                return HttpResponse('{"status":"error"}')
        except Exception as e:
           return HttpResponse(f'{{"status":"error-{e}"}}')
    return render(request,'shop/tracker.html')

def prodview(request,myid):
    #fetch product using id.
    product=Product.objects.filter(id=myid)
    print(product)
    params={'product':product[0]}
    return render(request,'shop/prodview.html',params)

def checkout(request):
    
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        phone=request.POST.get('phone','')
        amount=request.POST.get('amount','')
        
        order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,phone=phone,zip_code=zip_code,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        
    return render(request,'shop/checkout.html')
    
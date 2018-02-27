from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

# PARTICULARS #  
def listParticulars(request):
    particulars = Particular.objects.all()
    
    return render(request, 'particulars/particulars-list.html', {'particulars':particulars})

def addParticulars(request):
    if request.method == 'POST':
        form = ParticularForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-particulars'))
    else:
        form = ParticularForms()
    context = {'form': form}
    
    return render(request, 'particulars/add-particulars.html', context)

# END PARTICULARS #
# ACCOUNTS #
def listAccounts(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/accounts-list.html', {'accounts':accounts})


def addAccounts(request):
    if request.method == 'POST':
        form = AccountForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-accounts'))
    else:
        form = AccountForms()
    context = {'form': form}
    
    return render(request, 'accounts/add-accounts.html', context)

def listAccountParticulars(request):
    accounts = Account_Particular.objects.all()
    return render(request, 'accounts/accounts-particulars-list.html', {'accounts':accounts})

def addAccountParticulars(request):
    if request.method == 'POST':
        form = Account_ParticularForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-accounts'))
    else:
        form = Account_ParticularForms()
    context = {'form': form}
    
    return render(request, 'accounts/add-account-particulars.html', context)
# END ACCOUNTS #
# TRANSACTIONS #
from django.db.models import Sum

#ItemPrice.objects.aggregate(Sum('price'))

def listTransact(request):
    transacts = Transaction.objects.all()
    return render(request, 'transactions/transactions-list.html', {'transacts':transacts})


def addTransact(request):
    if request.method == 'POST':
        form = TransactionForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-transactions'))
    else:
        form = TransactionForms()
    context = {'form': form}
    
    return render(request, 'transactions/add-transactions.html', context)

def listTransactDetails(request):
    transacts = Transaction_Detail.objects.all()
    return render(request, 'transactions/transaction-details-list.html', {'transacts':transacts})

def addTransactDetails(request):
    curr_account = Account.objects.get(account_ID = 1)
    if request.method == 'POST':
        print request.POST['OR_num']
        form = Transaction_DetailForms(request.POST)
        if form.is_valid():
            #link this certain transaction detail to a transaction
            try:
                transact = Transaction.objects.get(OR_num=request.POST['OR_num']) 
            except Transaction.DoesNotExist:
                transact = Transaction(OR_num=request.POST['OR_num'], account_ID = curr_account)
                transact.save()
            post = form.save(commit=False)
            post.transact_ID = transact
            form.save()
            return HttpResponseRedirect(reverse('list-transactions'))
    else:
        form = Transaction_DetailForms()
        #Filters the foreign key fields
        form.fields["account_particular_ID"].queryset = Account_Particular.objects.filter(account_ID=curr_account)
    context = {'form': form}
    
    return render(request, 'transactions/add-transaction-details.html', context)
# END TRANSACTIONS #
# DAILY CASH #
def listDCash(request):
    pass

def addDCash(request):
    pass

def listDCashDetails(request):
    pass

def addDCashDetails(request):
    pass
# END DAILY CASH #
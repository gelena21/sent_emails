from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from automatic_email.models import Client, Mailout, Message
from automatic_email.forms import ClientForm, MailoutForm, MessageForm


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'automatic_email/client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('automatic_email:client_list')
    else:
        form = ClientForm()
    return render(request, 'automatic_email/client_form.html', {'form': form})


def mailout_list(request):
    mailouts = Mailout.objects.all()
    return render(request, 'automatic_email/mailout_list.html', {'mailouts': mailouts})


def mailout_create(request):
    if request.method == 'POST':
        form = MailoutForm(request.POST)
        if form.is_valid():
            mailout = form.save(commit=False)
            mailout.message = Message.objects.get(id=request.POST['message'])
            mailout.save()
            return redirect('mailout_list')
    else:
        form = MailoutForm()
    messages = Message.objects.all()
    return render(request, 'automatic_email/mailout_form.html', {'form': form, 'messages': messages})


def message_list(request):
    messages = Message.objects.all()
    return render(request, 'automatic_email/message_list.html', {'messages': messages})


def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'automatic_email/message_form.html', {'form': form})


@login_required
def client_update(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'automatic_email/client_update.html', {'form': form})


@login_required
def client_delete(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('client_list')


@login_required
def mailout_update(request, mailout_id):
    mailout = Mailout.objects.get(id=mailout_id)
    if request.method == 'POST':
        form = MailoutForm(request.POST, instance=mailout)
        if form.is_valid():
            form.save()
            return redirect('mailout_list')
    else:
        form = MailoutForm(instance=mailout)
    return render(request, 'automatic_email/mailout_update.html', {'form': form})


@login_required
def mailout_delete(request, mailout_id):
    mailout = Mailout.objects.get(id=mailout_id)
    mailout.delete()
    return redirect('mailout_list')


@login_required
def message_update(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'automatic_email/message_update.html', {'form': form})


@login_required
def message_delete(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('message_list')

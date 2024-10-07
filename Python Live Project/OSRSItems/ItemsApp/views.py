import os
import requests
import json
from bs4 import BeautifulSoup
from .forms import ItemForm
from .models import Item, Favorites
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


# Create your views here.
def itemsApp_home(request):
    """Function to open the homepage."""
    url = 'https://api.github.com/repos/Vexelior/The-Tech-Academy-Python-Live-Project/commits'
    
    headers = {
        'User-Agent': '@UnknwnEntity#2059'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        commit_data = response.json()

        if os.path.exists('OSRSItems\ItemsApp\data\commit_data.json'):
            with open('OSRSItems\ItemsApp\data\commit_data.json', 'w') as f:
                print('Saving updated data to cache...')
                json.dump(commit_data, f, indent=4)

        else:
            # create a new file and save the data to it
            with open('OSRSItems\ItemsApp\data\commit_data.json', 'w') as f:
                print('Saving inital data to cache...')
                json.dump(commit_data, f, indent=4)

        data = {}
        for commit in commit_data:
            data[commit['sha']] = {
                'message': commit['commit']['message'],
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date'],
                'link': commit['html_url'],
            }

        for commit in data:
            data[commit]['date'] = data[commit]['date'].split('T')[0]
            data[commit]['date'] = data[commit]['date'].split('-')
            data[commit]['date'] = data[commit]['date'][1] + '/' + \
            data[commit]['date'][2] + '/' + data[commit]['date'][0]
            
        
        content = {'success': True, 'message': 'Items updated successfully.', 'commit_data': data}

    except requests.exceptions.HTTPError as e:
        content = {'success': False, 'message': f'An error occurred: {e}'}

    return render(request, 'ItemsApp/ItemsApp_home.html', content)


def new_item(request):
    """Creates the form used for user input"""
    form = ItemForm(
        data=request.POST or None)  # Creates the form from forms.py.
    # Make only the name and image required.
    for field in form.fields:
        form.fields[field].required = False
        form.fields['name'].required = True
        form.fields['image'].required = True

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('select_item')
    content = {'form': form}  # Dictionary for form data entry.
    return render(request, 'ItemsApp/ItemsApp_new_item.html', content)


def select_item(request):
    """Creates a list of items from the database with anchor tag to select."""
    try:
        items = Item.objects.all()
        items_per_page = 25
        paginator = Paginator(items, items_per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        item_list = {}
        for item in page_obj:
            item_list[item.id] = {
                'name': item.name
            }

        content = {'success': True, 'message': 'Items updated successfully.',
                   'item_list': item_list, 'page_obj': page_obj}

        return render(request, 'ItemsApp/ItemsApp_details.html', content)
    except Exception as e:
        print(e)
        content = {'success': False, 'message': 'Error updating items.'}
        return render(request, 'ItemsApp/ItemsApp_details.html', content)


def search_item(request, search):
    """Creates a list of items from the database with anchor tag to select."""
    search = str(search)
    try:
        items = Item.objects.filter(name__icontains=search)
        items_per_page = 25
        paginator = Paginator(items, items_per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        item_list = {}
        for item in page_obj:
            item_list[item.id] = {
                'name': item.name
            }

        content = {'success': True, 'message': 'Items updated successfully.',
                   'item_list': item_list, 'page_obj': page_obj}

        return render(request, 'ItemsApp/ItemsApp_item_search.html', content)
    except Exception as e:
        print(e)
        content = {'success': False, 'message': 'Error updating items.'}
        return render(request, 'ItemsApp/ItemsApp_details.html', content)


def item_details(request, pk):
    """Displays the chosen item from 'select_item' function based on the given primary key."""
    pk = int(pk)
    item_get = Item.objects.get(pk=pk)
    context = {'item_get': item_get}
    return render(request, "ItemsApp/ItemsApp_details_page.html", context)


def edit_page(request):
    """Page that displays a drop-down menu for editing items in the database."""
    items = Item.objects.all()
    return render(request, 'ItemsApp/ItemsApp_edit_page.html', {'items': items})


def edit_form(request, pk):
    """Renders a new page for input and edit form."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('select_item')
        else:
            print(form.errors)
    else:
        return render(request, 'ItemsApp/ItemsApp_edit_items.html', {'form': form})

@permission_required('ItemsApp.delete_item')
def delete_item(request, pk):
    """Grabs the information from the primary key of the item to delete."""
    pk = int(pk)
    item = get_object_or_404(Item, pk=pk)
    # If the item is not null, delete the item.
    if item is not None:
        item.delete()
        messages.success(request, 'Item deleted successfully.')
        return redirect('select_item')
    else:
        messages.error(request, 'Item could not be deleted.')
        return redirect('select_item')


def fetch_api_data(url, headers):
    if os.path.exists('OSRSItems/ItemsApp/data/api_data.json'):
        with open('OSRSItems/ItemsApp/data/api_data.json', 'r') as f:
            print('Loading data from cache...')
            api_data = json.load(f)
            return api_data
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    api_data = response.json()

    if os.path.exists('OSRSItems/ItemsApp/data/api_data.json'):
        with open('OSRSItems/ItemsApp/data/api_data.json', 'w') as f:
            print('Saving data to cache...')
            json.dump(api_data, f, indent=4)
    else:
        pass
    return api_data


def save_items_to_database(api_data):
    for item_data in api_data:
        if Item.objects.filter(id=item_data['id']).exists():
            continue
        item_id = item_data['id']
        name = item_data['name']
        Item.objects.get_or_create(id=item_id, defaults={'name': name})


def api(request):
    url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
    headers = {
        'User-Agent': '@UnknwnEntity#2059'
    }

    try:
        api_data = fetch_api_data(url, headers)
        save_items_to_database(api_data)
        items = Item.objects.all()
        items_per_page = 25
        paginator = Paginator(items, items_per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        data = {}
        for item in page_obj:
            data[item.id] = {
                'name': item.name
            }
        content = {'success': True, 'message': 'Items updated successfully.',
                   'data': data, 'page_obj': page_obj}

    except requests.exceptions.HTTPError as e:
        # handle exceptions caused by non-200 status codes
        content = {'success': False, 'message': f'An error occurred: {e}'}

    return render(request, 'ItemsApp/ItemsApp_details.html', content)


def scrape_search(request, name):
    # OSRS account stats lookup for scraping.
    url = "https://secure.runescape.com/m=hiscore_oldschool/hiscorepersonal?user1=" + name
    response = requests.get(url)
    html_content = response.content

    # Check the status code of the response
    if response.status_code != 200:
        content = {'success': False,
                   'message': 'An error occurred while scraping the website.'}
        messages.error(
            request, 'An error occurred while scraping the website.')
        return render(request, 'ItemsApp/ItemsApp_scrape_search.html', content)

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table that contains your stats and level
    table = soup.find_all('table')[0]
    table_rows = table.find_all('tr')

    # Extract and print your stats and level
    account_data = []
    for row in table_rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        # Add all cols to the account_data list except the first four elements
        account_data.append([ele for ele in cols if ele])

    # Remove the first four elements of the list
    account_data = account_data[4:]

    # If there are any elements that are empty, remove them
    account_data = [x for x in account_data if x]

    # Create a new node at the beginning of the list for the account name
    account_data.insert(0, [name])

    # if there is only the name in the list, the account does not exist
    # This does not validate that the account exists, only that the account name was passed in
    if len(account_data) == 1:
        account_data = []

    # Create a dictionary for the account data
    content = {'account_data': account_data}

    # Check for a folder named 'data' in the static folder
    if not os.path.exists('data'):
        os.makedirs('data')
    else:
        pass

    if not os.path.exists('OSRSItems/ItemsApp/data/account_data.json'):
        # Save the data to a JSON file
        with open('OSRSItems/ItemsApp/data/account_data.json', 'w') as f:
            json.dump(account_data, f)
    else:
        # Write the data to the JSON file
        with open('OSRSItems/ItemsApp/data/account_data.json', 'w') as f:
            json.dump(account_data, f)

    return render(request, 'ItemsApp/ItemsApp_scrape.html', content)


def scrape_page(request):
    # Look for the account data JSON file
    if os.path.exists('OSRSItems/ItemsApp/data/account_data.json'):
        # Open the JSON file
        with open('OSRSItems/ItemsApp/data/account_data.json', 'r') as f:
            account_data = json.load(f)
    else:
        # If the file doesn't exist, redirect to the scrape page
        messages.error(
            request, 'No account data found. Please enter a valid username.')
        return redirect('scrape')

    # Create a dictionary for the account data
    content = {'account_data': account_data}

    return render(request, 'ItemsApp/ItemsApp_scrape.html', content)


def login_modal(request):
    """Function to open the login modal."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('itemsApp_home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('itemsApp_home')

    return render(request, 'itemsApp_login_modal')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('itemsApp_home')
    else:
        form = UserCreationForm()

    return render(request, 'ItemsApp/ItemsApp_register.html', {'form': form})


def logout_account(request):
    logout(request)
    return redirect('itemsApp_home')


@login_required
def show_favorites(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        item = get_object_or_404(Item, id=item_id)

        # if there is already a favorite for this item, don't create a new one
        if Favorites.objects.filter(user=request.user, item=item).exists():
            messages.error(request, 'This item is already in your favorites.')
            return redirect('itemsApp_favorites')

        favorite = Favorites(user=request.user, item=item)
        favorite.save()

    favorites = Favorites.objects.filter(user=request.user)
    item_list = [favorite.item for favorite in favorites]
    return render(request, 'ItemsApp/ItemsApp_show_favorites.html', {'favorites': favorites, 'item_list': item_list})


@login_required
def delete_favorite(request, pk):
    pk = int(pk)
    # look through the database for the favorite in the item_id column with the given pk
    favorite = get_object_or_404(Favorites, item_id=pk)
    if favorite is not None:
        favorite.delete()
        messages.success(request, f'{favorite.item.name} has been removed.')
        return redirect('itemsApp_favorites')
    else:
        messages.error(request, 'The selected item is not in your favorites.')
        return redirect('itemsApp_favorites')

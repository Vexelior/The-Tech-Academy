from django.forms import ModelForm
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'Item Name',
            'type': 'Item Type',
            'atk_stab': 'Stab Attack',
            'atk_slash': 'Slash Attack',
            'atk_crush': 'Crush Attack',
            'atk_magic': 'Magic Attack',
            'atk_range': 'Ranged Attack',
            'def_stab': 'Stab Defence',
            'def_slash': 'Slash Defence',
            'def_crush': 'Crush Defence',
            'def_magic': 'Magic Defence',
            'def_range': 'Ranged Defence',
            'bns_strength': 'Strength Bonus',
            'bns_range': 'Range Bonus',
            'bns_magic': 'Magic Bonus',
            'bns_prayer': 'Prayer Bonus',
            'slot': 'Slot',
            'range': 'Attack Distance',
            'image': 'Image',
            'speed': 'Attack Speed'
        }

from django import forms
from .models import Stock,StockHistory

class StockCreateForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'quantity']

   def clean_category(self) :
      category = self.cleaned_data.get('category')
      if not category:
        raise forms.ValidationError('This field is required')

      # item = self.cleaned_data.get('item_name')

      # for instance in Stock.objects.all():
      #   if instance.item_name == item:
      #     raise forms.ValidationError(str(item) + ' is already created')
      return category

   def clean_item_name(self):
      item_name = self.cleaned_data.get('item_name')
      if not item_name:
        raise forms.ValidationError('This field is required')

      for instance in Stock.objects.all():
        if instance.item_name == item_name:
          raise forms.ValidationError(str(item_name) + ' is already created')

      return item_name

class StockHistorySearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = StockHistory
		fields = ['category', 'item_name', 'start_date', 'end_date']


#search 
class StockSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)
   class Meta:
     model = Stock
     fields = ['category', 'item_name']

#Update
class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']

#sub item
class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']

#add item
class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']

#再訂貨水平
class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']


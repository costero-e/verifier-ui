from django import forms

class BamForm(forms.Form):
    url_link = forms.CharField(max_length=100, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")

    
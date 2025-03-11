from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente, Treinador, plano

class ClienteForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
    plano = forms.ModelChoiceField(queryset=plano.objects.all())

    class Meta:
        model = User
        fields = ['username', 'nome_completo', 'email', 'telefone', 'plano', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nome_completo"]
        user.email = self.cleaned_data["email"]

        if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("As senhas não coincidem")

        if commit:
            user.set_password(self.cleaned_data["password1"])
            user.save()

        cliente = Cliente(user=user, telefone=self.cleaned_data["telefone"], plano=self.cleaned_data["plano"], email=self.cleaned_data["email"], nome_completo=self.cleaned_data["nome_completo"])
        if commit:
            cliente.save()
        return cliente


class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Treinador
        fields = ['nome', 'email', 'telefone', 'especialidade', 'foto']

class planoForm(forms.ModelForm):
    class Meta:
        model = plano
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']

    data_inicio = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    data_fim = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

from django import forms 

class LoginForms(forms.Form):
    email_login=forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    senha_login=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirmar senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
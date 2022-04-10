# ContaConmigo2022
Repositorio Creado para Entrega Final UTN

**Steps to run the the project:**
1. Install python
2. You need to install django within the virtual environment
python -m pip install django	
3. you can verify the django version installed typing the following command:
django-admin version
4. Move to ContaConmigo2022
cd ContaConmigo2022
5. run python server
python manage.py runserver
6. Install the postgre module
pip install psycopg2
8. django redux
pip install django-registration-redux
9. crispy: pip install django-crispy-forms
10. TemplateSyntaxError
Exception Value:	'crispy_forms_tag' is not a registered tag library: https://ordinarycoders.com/blog/article/errors-in-django
BROWSER WINDOW: TemplateSyntaxError at/ Invalid filter:'crispy'

This is one of the trickier errors given that it does not have much to do with the actual filter added to the form.

The error occurs when you have a space between the closing percentage sign and bracket of the crispy form tags like so: {% load crispy_forms_tags % }.

env > mysite > main > templates > main > home.html

{% load crispy_forms_tags %}
	
		<form method="post">
        {% csrf_token %}
            {{form|crispy}}
            <button type="submit">Submit</button>
        </form>
    

It's honestly one of the harder errors to resolve if you are new to using crispy-forms or Jinja.

You just need to make sure there are no spaces in the actual Jinja tag {% ... %}. But space between the tag and the variables within them is okay. 

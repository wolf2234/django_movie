from django.template import Library
from contact.forms import ContactForm

register = Library()


@register.inclusion_tag("contact/tags/form.html")
def contact_form():
    return {"contact_form": ContactForm()}

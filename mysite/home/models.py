from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import StreamField
from wagtail import blocks


class PortfolioProject(Orderable):
    
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='projecten')
    
    project_naam = models.CharField(max_length=255, help_text="Vul hier de naam van het project in")
    project_uitleg = RichTextField(blank=True, help_text="Vertel hier wat over dit project")
    github_link = models.URLField(blank=True, help_text="Link naar de GitHub-code")

    panels = [
        FieldPanel('project_naam'),
        FieldPanel('project_uitleg'),
        FieldPanel('github_link'),
    ]

class HomePage(Page):
    
    body = RichTextField(blank=True, help_text="Vertel hier wat over jezelf")

    profielfoto = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'     
    )

    vaardigheden = StreamField([
        ('tool_naam', blocks.CharBlock(max_length=50, help_text="Bijv: Python, HTML of Django")),
    ], blank=True, null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('profielfoto'), 
        FieldPanel('vaardigheden'), 
        InlinePanel('projecten', label="Projecten"),
    ]
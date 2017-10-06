from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core import serializers
from django_tables2 import RequestConfig
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from .forms2 import GenericRelationForm
from entities.forms import (PlaceHighlighterForm, PersonHighlighterForm)
from highlighter.models import Annotation
from .models import (PersonPlace, PersonPerson, PersonInstitution, InstitutionPlace,
                     InstitutionInstitution, PlacePlace, PersonEvent, InstitutionEvent, PlaceEvent, PersonWork,
                     InstitutionWork, PlaceWork, EventWork)
from .tables import PersonInstitutionTable
from relations.tables import (PersonInstitutionTable, PersonPersonTable, PersonPlaceTable,
                              EntityLabelTable, InstitutionPlaceTable, InstitutionInstitutionTable,
                              PersonEventTable, InstitutionEventTable, PlaceEventTable, PersonWorkTable,
                              InstitutionWorkTable, PlaceWorkTable, EventWorkTable, EntityUriTable, PlacePlaceTable)
from metainfo.models import Uri
from entities.models import Person, Institution, Place, Event, Work
from entities.forms import PersonResolveUriForm
from labels.models import Label
from helper_functions.highlighter import highlight_text

import json, re
from copy import deepcopy

############################################################################
############################################################################
#
#   Generic views for AjaxForms
#
############################################################################
############################################################################

######################################################
# test for class-ignoring _ajax_form-functions
######################################################

# Model-classes must be registered together with their ModelForm-classes
registered_forms = {'PersonPlaceForm': [PersonPlace, Person, Place],
                    'PersonPlaceHighlighterForm': [PersonPlace, Person, Place],
                    'PersonPersonForm': [PersonPerson, Person, Person],
                    'PersonPersonHighlighterForm': [PersonPerson, Person, Person],
                    'PersonInstitutionForm': [PersonInstitution, Person, Institution],
                    'PersonEventForm': [PersonEvent, Person, Event],
                    'PersonWorkForm': [PersonWork, Person, Work],
                    'PersonInstitutionHighlighterForm': [PersonInstitution, Person, Institution],
                    'PersonWorkHighlighterForm': [PersonWork, Person, Work],
                    'PlaceWorkHighlighterForm': [PlaceWork, Place, Work],
                    'InstitutionWorkHighlighterForm': [InstitutionWork, Institution, Work],
                    'InstitutionPlaceForm': [InstitutionPlace, Institution, Place],
                    'InstitutionInstitutionForm': [
                        InstitutionInstitution,
                        Institution,
                        Institution,
                        PersonInstitutionTable],
                    'InstitutionPersonForm': [PersonInstitution, Institution, Person],
                    'InstitutionEventForm': [InstitutionEvent, Institution, Event],
                    'InstitutionWorkForm': [InstitutionWork, Institution, Work],
                    'PlaceEventForm': [PlaceEvent, Place, Event],
                    'PlaceWorkForm': [PlaceWork, Place, Work],
                    'PlacePlaceForm': [PlacePlace, Place, Place],
                    'EventWorkForm': [EventWork, Event, Work],
                    'InstitutionLabelForm': [Label, Institution, Label],
                    'PersonLabelForm': [Label, Person, Label],
                    'EventLabelForm': [Label, Event, Label],
                    'PersonResolveUriForm': [Uri, Person, Uri],
                    'AddRelationHighlighterPersonForm': [],
                    'PlaceHighlighterForm': [Annotation, ],
                    'PersonHighlighterForm': [Annotation, ]
                    }


@login_required
def get_form_ajax(request):
    '''Returns forms rendered in html'''

    FormName = request.POST.get('FormName')
    SiteID = request.POST.get('SiteID')
    ButtonText = request.POST.get('ButtonText')
    ObjectID = request.POST.get('ObjectID')
    entity_type_str = request.POST.get('entity_type')
    if FormName:
        form_match = re.match(r'([A-Z][a-z]+)([A-Z][a-z]+)(Highlighter)?Form', FormName)
        entity_type_v1 = ContentType.objects.filter(model='{}{}'.format(form_match.group(1), form_match.group(2)).lower())
    else:
        entity_type_v1 = ContentType.objects.none()
    if FormName not in registered_forms.keys():
        raise Http404

    if ObjectID == 'false' or ObjectID is None or ObjectID == 'None':
        ObjectID = False
        form_dict = {'entity_type': entity_type_str}
    else:
        d = registered_forms[FormName][0].objects.get(pk=ObjectID)
        form_dict = {'instance': d, 'siteID': SiteID, 'entity_type': entity_type_str}
    if entity_type_v1.count() > 0:
        form_dict['relation_form'] = '{}{}'.format(form_match.group(1), form_match.group(2))
        if form_match.group(3) == 'Highlighter':
            form_dict['highlighter'] = True
        form = GenericRelationForm(**form_dict)
    else:
        form = globals()[FormName](**form_dict)
    tab = FormName[:-4]

    data = {'tab': tab, 'form': render_to_string("_ajax_form.html", {
                "entity_type": entity_type_str,
                "form": form,
                'type1': FormName,
                'url2': 'save_ajax_'+FormName,
                'button_text': ButtonText,
                'ObjectID': ObjectID,
                'SiteID': SiteID})}

    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def save_ajax_form(request, entity_type, kind_form, SiteID, ObjectID=False):
    '''Tests validity and saves AjaxForms, returns them when validity test fails'''
    if kind_form not in registered_forms.keys():
        raise Http404

    button_text = "create/modify"

    if not ObjectID:
        instance_id = ''
    else:
        instance_id = ObjectID
    entity_type_str = entity_type
    entity_type = ContentType.objects.get(model=entity_type.lower()).model_class()
    form_match = re.match(r'([A-Z][a-z]+)([A-Z][a-z]+)(Highlighter)?Form', kind_form)
    form_dict = {'data': request.POST,
                 'entity_type': entity_type,
                 'request': request}
    try:
        test_form_relations = ContentType.objects.filter(
            model='{}{}'.format(form_match.group(1).lower(), form_match.group(2)).lower(),
            app_label='relations')
        tab = re.match(r'(.*)Form', kind_form).group(1)
        call_function = 'EntityRelationForm_response'
        if test_form_relations.count() > 0:
            relation_form = test_form_relations[0].model_class()
            form_dict['relation_form'] = relation_form
            if form_match.group(3) == 'Highlighter':
                form_dict['highlighter'] = True
                tab = form_match.group(1)+form_match.group(2)
                call_function = 'HighlForm_response'
            form = GenericRelationForm(**form_dict)
        else:
            form = globals()[kind_form](**form_dict)
        if form.is_valid():
            site_instance = entity_type.objects.get(pk=SiteID)
            set_ann_proj = request.session.get('annotation_project', 1)
            entity_types_highlighter = request.session.get('entity_types_highlighter')
            users_show = request.session.get('users_show_highlighter', None)
            hl_text = None
            if ObjectID:
                instance = form.save(instance=ObjectID, site_instance=site_instance)
            else:
                instance = form.save(site_instance=site_instance)
            right_panel = True
            if test_form_relations.count() > 0:
                table_html = form.get_html_table(entity_type_str, request, site_instance, form_match)
            if 'Highlighter' in tab or form_match.group(3) == 'Highlighter':
                hl_text = {
                    'text': highlight_text(form.get_text_id(),
                                           users_show=users_show,
                                           set_ann_proj=set_ann_proj,
                                           types=entity_types_highlighter).strip(),
                    'id': form.get_text_id()}
            if tab == 'PersonLabel':
                table_html = EntityLabelTable(
                        site_instance.label_set.all(),
                        prefix='PL-')
            elif tab == 'InstitutionLabel':
                table_html = EntityLabelTable(
                        site_instance.label_set.all(),
                        prefix='IL-')
            elif tab == 'PersonResolveUri':
                table_html = EntityUriTable(
                    Uri.objects.filter(entity=site_instance),
                    prefix = 'PURI-'
                )

            elif tab == 'AddRelationHighlighterPerson' or tab == 'PlaceHighlighter' or tab == 'PersonHighlighter':
                table_html = None
                right_panel = False
                call_function = 'PAddRelation_response'
                instance = None
            if instance:
                instance2 = instance.get_web_object()
            else:
                instance2 = None
            if table_html:
                table_html2 = table_html.as_html(request)
            else:
                table_html2 = None
            data = {'test': True, 'tab': tab, 'call_function': call_function,
                    'instance': instance2,
                    'table_html': table_html2,
                    'text': hl_text,
                    'right_panel': right_panel}
        else:
            if 'Highlighter' in tab:
                call_function = 'HighlForm_response'
            data = {'test': False, 'call_function': call_function,
                    'DivID': 'div_'+kind_form+instance_id,
                    'form': render_to_string("_ajax_form.html", {
                        "entity_type": entity_type_str,
                        "form": form, 'type1': kind_form, 'url2': 'save_ajax_'+kind_form,
                        'button_text': button_text, 'ObjectID': ObjectID, 'SiteID': SiteID},
                        context_instance=RequestContext(request))}

    except Exception as e:
        print('Error in save method')
        print(e)
        data = {'test': False, 'error': json.dumps(e)}
    return HttpResponse(json.dumps(data), content_type='application/json')

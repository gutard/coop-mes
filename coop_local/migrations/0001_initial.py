# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LegalStatus'
        db.create_table('coop_local_legalstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coop_local', ['LegalStatus'])

        # Adding model 'OrganizationCategoryIAE'
        db.create_table('coop_local_organizationcategoryiae', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coop_local', ['OrganizationCategoryIAE'])

        # Adding model 'OrganizationDocument'
        db.create_table('coop_local_organizationdocument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=255)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.Organization'])),
        ))
        db.send_create_signal('coop_local', ['OrganizationDocument'])

        # Adding model 'OrganizationCategory'
        db.create_table('coop_local_organizationcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coop_local', ['OrganizationCategory'])

        # Adding model 'Organization'
        db.create_table('coop_local_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='WXDKvt6U23Yr8BfshvYmsk', max_length=50, unique=True, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pref_label', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=3000, null=True, blank=True)),
            ('logo', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('email_sha1', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('pref_email', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pref_email', null=True, to=orm['coop_local.Contact'])),
            ('pref_phone', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pref_phone', null=True, to=orm['coop_local.Contact'])),
            ('pref_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pref_adress', null=True, to=orm['coop_geo.Location'])),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('siret', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('legal_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.LegalStatus'], null=True, blank=True)),
            ('agreement_iae', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('brief_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('added_value', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('annual_revenue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('workforce', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('production_workforce', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('supervision_workforce', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('integration_workforce', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('annual_integration_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Organization'])

        # Adding M2M table for field category on 'Organization'
        db.create_table('coop_local_organization_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm['coop_local.organization'], null=False)),
            ('organizationcategory', models.ForeignKey(orm['coop_local.organizationcategory'], null=False))
        ))
        db.create_unique('coop_local_organization_category', ['organization_id', 'organizationcategory_id'])

        # Adding M2M table for field category_iae on 'Organization'
        db.create_table('coop_local_organization_category_iae', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm['coop_local.organization'], null=False)),
            ('organizationcategoryiae', models.ForeignKey(orm['coop_local.organizationcategoryiae'], null=False))
        ))
        db.create_unique('coop_local_organization_category_iae', ['organization_id', 'organizationcategoryiae_id'])

        # Adding model 'LinkProperty'
        db.create_table('coop_local_linkproperty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('coop_local', ['LinkProperty'])

        # Adding model 'Link'
        db.create_table('coop_local_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('predicate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.LinkProperty'])),
            ('object_uri', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Link'])

        # Adding model 'Article'
        db.create_table('coop_local_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='i7aFRn8Ys2jPWjwV4WLpWW', max_length=50, unique=True, null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=100, separator=u'-', blank=True, unique=True, populate_from='title', overwrite=True)),
            ('title', self.gf('django.db.models.fields.TextField')(default=u'Page title', blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default=u'Page content', blank=True)),
            ('publication', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('template', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('temp_logo', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='coop_local_article_rel', null=True, blank=True, to=orm['coop_cms.ArticleCategory'])),
            ('in_newsletter', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_homepage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('headline', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='articles', null=True, to=orm['coop_local.Organization'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='articles', null=True, to=orm['coop_local.Person'])),
            ('remote_person_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_person_label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('remote_organization_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_organization_label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('isSection', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('coop_local', ['Article'])

        # Adding model 'NavTree'
        db.create_table('coop_local_navtree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='USFLbdi45gNVrQRqyH3XJ9', max_length=50, unique=True, null=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='default', unique=True, max_length=100, db_index=True)),
        ))
        db.send_create_signal('coop_local', ['NavTree'])

        # Adding M2M table for field types on 'NavTree'
        db.create_table('coop_local_navtree_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('navtree', models.ForeignKey(orm['coop_local.navtree'], null=False)),
            ('navtype', models.ForeignKey(orm['coop_cms.navtype'], null=False))
        ))
        db.create_unique('coop_local_navtree_types', ['navtree_id', 'navtype_id'])

        # Adding model 'Tag'
        db.create_table('coop_local_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='WRFxbgXQdUsGzeHcURhYTY', max_length=50, unique=True, null=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='fr', max_length=10)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.Person'], null=True, blank=True)),
            ('person_uri', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('concept_uri', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Tag'])

        # Adding model 'TaggedItem'
        db.create_table('coop_local_taggeditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='coop_local_taggeditem_items', to=orm['coop_local.Tag'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='coop_local_taggeditem_taggeditem_items', to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal('coop_local', ['TaggedItem'])

        # Adding model 'PersonCategory'
        db.create_table('coop_local_personcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=True)),
        ))
        db.send_create_signal('coop_local', ['PersonCategory'])

        # Adding model 'Person'
        db.create_table('coop_local_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='ZRnBAV4rFiZx7EdbGJng3o', max_length=50, unique=True, null=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('email_sha1', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('structure', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('remote_organization_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_organization_label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_geo.Location'], null=True, blank=True)),
            ('location_display', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
        ))
        db.send_create_signal('coop_local', ['Person'])

        # Adding M2M table for field category on 'Person'
        db.create_table('coop_local_person_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm['coop_local.person'], null=False)),
            ('personcategory', models.ForeignKey(orm['coop_local.personcategory'], null=False))
        ))
        db.create_unique('coop_local_person_category', ['person_id', 'personcategory_id'])

        # Adding model 'Contact'
        db.create_table('coop_local_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='9GxZGkL46idJAQqR4mYb4e', max_length=50, unique=True, null=True)),
            ('category', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('display', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('coop_local', ['Contact'])

        # Adding model 'RoleCategory'
        db.create_table('coop_local_rolecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=True)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('coop_local', ['RoleCategory'])

        # Adding model 'Role'
        db.create_table('coop_local_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='PQtNM7DezXi22BxRecG3HA', max_length=50, unique=True, null=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='label', unique_with=())),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.RoleCategory'], null=True, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Role'])

        # Adding model 'Relation'
        db.create_table('coop_local_relation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source', to=orm['coop_local.Organization'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='target', to=orm['coop_local.Organization'])),
            ('reltype', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Relation'])

        # Adding model 'Engagement'
        db.create_table('coop_local_engagement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='Ge5XzaWEVnaAsahxZ8F8y3', max_length=50, unique=True, null=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='engagements', to=orm['coop_local.Person'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.Organization'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.Role'], null=True, blank=True)),
            ('role_detail', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('org_admin', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('engagement_display', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('remote_role_uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('remote_role_label', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Engagement'])

        # Adding model 'Exchange'
        db.create_table('coop_local_exchange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='5E5sW6JmeiHys5oSNXTS5L', max_length=50, unique=True, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='exchanges', null=True, to=orm['coop_local.Organization'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coop_local.Person'], null=True, blank=True)),
            ('eway', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('etype', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('permanent', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('expiration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=True)),
            ('remote_person_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_person_label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('remote_organization_uri', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_organization_label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='exchange_location', null=True, to=orm['coop_geo.Location'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='exchange_area', null=True, to=orm['coop_geo.Area'])),
        ))
        db.send_create_signal('coop_local', ['Exchange'])

        # Adding M2M table for field products on 'Exchange'
        db.create_table('coop_local_exchange_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exchange', models.ForeignKey(orm['coop_local.exchange'], null=False)),
            ('product', models.ForeignKey(orm['coop_local.product'], null=False))
        ))
        db.create_unique('coop_local_exchange_products', ['exchange_id', 'product_id'])

        # Adding M2M table for field methods on 'Exchange'
        db.create_table('coop_local_exchange_methods', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exchange', models.ForeignKey(orm['coop_local.exchange'], null=False)),
            ('exchangemethod', models.ForeignKey(orm['coop_local.exchangemethod'], null=False))
        ))
        db.create_unique('coop_local_exchange_methods', ['exchange_id', 'exchangemethod_id'])

        # Adding model 'ExchangeMethod'
        db.create_table('coop_local_exchangemethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('etypes', self.gf('coop.utils.fields.MultiSelectField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('coop_local', ['ExchangeMethod'])

        # Adding model 'Product'
        db.create_table('coop_local_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('uri_mode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='cnuySLPfcc6vk3xzTZuu7Z', max_length=50, unique=True, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='products', null=True, to=orm['coop_local.Organization'])),
            ('remote_organization_uri', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('remote_organization_label', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('coop_local', ['Product'])

        # Adding model 'SitePrefs'
        db.create_table('coop_local_siteprefs', (
            ('preferences_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['preferences.Preferences'], unique=True, primary_key=True)),
            ('main_organization', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='main_org', null=True, to=orm['coop_local.Organization'])),
        ))
        db.send_create_signal('coop_local', ['SitePrefs'])


    def backwards(self, orm):
        # Deleting model 'LegalStatus'
        db.delete_table('coop_local_legalstatus')

        # Deleting model 'OrganizationCategoryIAE'
        db.delete_table('coop_local_organizationcategoryiae')

        # Deleting model 'OrganizationDocument'
        db.delete_table('coop_local_organizationdocument')

        # Deleting model 'OrganizationCategory'
        db.delete_table('coop_local_organizationcategory')

        # Deleting model 'Organization'
        db.delete_table('coop_local_organization')

        # Removing M2M table for field category on 'Organization'
        db.delete_table('coop_local_organization_category')

        # Removing M2M table for field category_iae on 'Organization'
        db.delete_table('coop_local_organization_category_iae')

        # Deleting model 'LinkProperty'
        db.delete_table('coop_local_linkproperty')

        # Deleting model 'Link'
        db.delete_table('coop_local_link')

        # Deleting model 'Article'
        db.delete_table('coop_local_article')

        # Deleting model 'NavTree'
        db.delete_table('coop_local_navtree')

        # Removing M2M table for field types on 'NavTree'
        db.delete_table('coop_local_navtree_types')

        # Deleting model 'Tag'
        db.delete_table('coop_local_tag')

        # Deleting model 'TaggedItem'
        db.delete_table('coop_local_taggeditem')

        # Deleting model 'PersonCategory'
        db.delete_table('coop_local_personcategory')

        # Deleting model 'Person'
        db.delete_table('coop_local_person')

        # Removing M2M table for field category on 'Person'
        db.delete_table('coop_local_person_category')

        # Deleting model 'Contact'
        db.delete_table('coop_local_contact')

        # Deleting model 'RoleCategory'
        db.delete_table('coop_local_rolecategory')

        # Deleting model 'Role'
        db.delete_table('coop_local_role')

        # Deleting model 'Relation'
        db.delete_table('coop_local_relation')

        # Deleting model 'Engagement'
        db.delete_table('coop_local_engagement')

        # Deleting model 'Exchange'
        db.delete_table('coop_local_exchange')

        # Removing M2M table for field products on 'Exchange'
        db.delete_table('coop_local_exchange_products')

        # Removing M2M table for field methods on 'Exchange'
        db.delete_table('coop_local_exchange_methods')

        # Deleting model 'ExchangeMethod'
        db.delete_table('coop_local_exchangemethod')

        # Deleting model 'Product'
        db.delete_table('coop_local_product')

        # Deleting model 'SitePrefs'
        db.delete_table('coop_local_siteprefs')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coop_cms.articlecategory': {
            'Meta': {'object_name': 'ArticleCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        'coop_cms.navtype': {
            'Meta': {'object_name': 'NavType'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_rule': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'search_field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'coop_geo.area': {
            'Meta': {'object_name': 'Area'},
            'area_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.AreaType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'default_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'associated_area'", 'null': 'True', 'to': "orm['coop_geo.Location']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'polygon': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'related_areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_geo.Area']", 'through': "orm['coop_geo.AreaRelations']", 'symmetrical': 'False'}),
            'update_auto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'eX6gXs7kcStypByDfPAE4b'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_geo.arealink': {
            'Meta': {'object_name': 'AreaLink'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.Area']", 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'coop_geo.arearelations': {
            'Meta': {'object_name': 'AreaRelations'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_rels'", 'to': "orm['coop_geo.Area']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child_rels'", 'to': "orm['coop_geo.Area']"})
        },
        'coop_geo.areatype': {
            'Meta': {'object_name': 'AreaType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'txt_idx': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        },
        'coop_geo.located': {
            'Meta': {'object_name': 'Located'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.LocationCategory']", 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.Location']", 'null': 'True', 'blank': 'True'}),
            'main_location': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'coop_geo.location': {
            'Meta': {'object_name': 'Location'},
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.Area']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'geohash': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'7wSzjSG9Pt9BZyMvEwYgfE'", 'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'x_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'coop_geo.locationcategory': {
            'Meta': {'ordering': "['label']", 'object_name': 'LocationCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'False'})
        },
        'coop_local.article': {
            'Meta': {'object_name': 'Article'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'coop_local_article_rel'", 'null': 'True', 'blank': 'True', 'to': "orm['coop_cms.ArticleCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u'Page content'", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isSection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'to': "orm['coop_local.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'to': "orm['coop_local.Person']"}),
            'publication': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'remote_organization_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'remote_organization_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remote_person_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'remote_person_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'temp_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "u'Page title'", 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'aTZCq4N2wdYZFcTvtcH7zk'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.contact': {
            'Meta': {'ordering': "['category']", 'object_name': 'Contact'},
            'category': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'display': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'uiCMbVmsbX5gSt2EA9gJTf'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.engagement': {
            'Meta': {'object_name': 'Engagement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'engagement_display': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'org_admin': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'engagements'", 'to': "orm['coop_local.Person']"}),
            'remote_role_label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'remote_role_uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.Role']", 'null': 'True', 'blank': 'True'}),
            'role_detail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'R9wZLR7tBwJWc7ie7rkqQT'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.exchange': {
            'Meta': {'ordering': "('-modified',)", 'object_name': 'Exchange'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exchange_area'", 'null': 'True', 'to': "orm['coop_geo.Area']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'etype': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'eway': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'expiration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exchange_location'", 'null': 'True', 'to': "orm['coop_geo.Location']"}),
            'methods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_local.ExchangeMethod']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exchanges'", 'null': 'True', 'to': "orm['coop_local.Organization']"}),
            'permanent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.Person']", 'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_local.Product']", 'symmetrical': 'False'}),
            'remote_organization_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'remote_organization_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remote_person_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'remote_person_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'DDZEbNn29BKTs2fx5FNWVg'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.exchangemethod': {
            'Meta': {'object_name': 'ExchangeMethod'},
            'etypes': ('coop.utils.fields.MultiSelectField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'coop_local.legalstatus': {
            'Meta': {'object_name': 'LegalStatus'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'True'})
        },
        'coop_local.link': {
            'Meta': {'object_name': 'Link'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'object_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'predicate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.LinkProperty']"})
        },
        'coop_local.linkproperty': {
            'Meta': {'object_name': 'LinkProperty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'coop_local.navtree': {
            'Meta': {'object_name': 'NavTree'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'default'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_cms.NavType']", 'symmetrical': 'False', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'Ln7F4Fr2atuviAp6gxzo6L'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.organization': {
            'Meta': {'ordering': "['title']", 'object_name': 'Organization'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'added_value': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'agreement_iae': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'annual_integration_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'annual_revenue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'brief_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['coop_local.OrganizationCategory']", 'null': 'True', 'blank': 'True'}),
            'category_iae': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['coop_local.OrganizationCategoryIAE']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_sha1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integration_workforce': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legal_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.LegalStatus']", 'null': 'True', 'blank': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_local.Person']", 'through': "orm['coop_local.Engagement']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pref_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pref_adress'", 'null': 'True', 'to': "orm['coop_geo.Location']"}),
            'pref_email': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pref_email'", 'null': 'True', 'to': "orm['coop_local.Contact']"}),
            'pref_label': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'pref_phone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pref_phone'", 'null': 'True', 'to': "orm['coop_local.Contact']"}),
            'production_workforce': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coop_local.Organization']", 'through': "orm['coop_local.Relation']", 'symmetrical': 'False'}),
            'siret': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'supervision_workforce': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'KNtch3NegWG88ciufGztDj'", 'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'workforce': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'coop_local.organizationcategory': {
            'Meta': {'object_name': 'OrganizationCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'True'})
        },
        'coop_local.organizationcategoryiae': {
            'Meta': {'object_name': 'OrganizationCategoryIAE'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'True'})
        },
        'coop_local.organizationdocument': {
            'Meta': {'object_name': 'OrganizationDocument'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.Organization']"})
        },
        'coop_local.person': {
            'Meta': {'object_name': 'Person'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['coop_local.PersonCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_sha1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_geo.Location']", 'null': 'True', 'blank': 'True'}),
            'location_display': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'remote_organization_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'remote_organization_uri': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'8rdDxYzCeCuz6LE9vy4sTD'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.personcategory': {
            'Meta': {'object_name': 'PersonCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'True'})
        },
        'coop_local.product': {
            'Meta': {'ordering': "['-modified']", 'object_name': 'Product'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': "orm['coop_local.Organization']"}),
            'remote_organization_label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'remote_organization_uri': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'wCoh3HLMucpnsswSWjBaDU'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.relation': {
            'Meta': {'object_name': 'Relation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'reltype': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source'", 'to': "orm['coop_local.Organization']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'target'", 'to': "orm['coop_local.Organization']"})
        },
        'coop_local.role': {
            'Meta': {'object_name': 'Role'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.RoleCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'label'", 'unique_with': '()'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'iPYgE5u6YrXXTZwrhaG9Li'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.rolecategory': {
            'Meta': {'ordering': "['label']", 'object_name': 'RoleCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'True'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'coop_local.siteprefs': {
            'Meta': {'object_name': 'SitePrefs'},
            'main_organization': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'main_org'", 'null': 'True', 'to': "orm['coop_local.Organization']"}),
            'preferences_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['preferences.Preferences']", 'unique': 'True', 'primary_key': 'True'})
        },
        'coop_local.tag': {
            'Meta': {'object_name': 'Tag'},
            'concept_uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'fr'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coop_local.Person']", 'null': 'True', 'blank': 'True'}),
            'person_uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'uri_mode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'MbzzUzoFWkTbqMQ2yrwa4L'", 'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'coop_local.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'coop_local_taggeditem_taggeditem_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'coop_local_taggeditem_items'", 'to': "orm['coop_local.Tag']"})
        },
        'preferences.preferences': {
            'Meta': {'object_name': 'Preferences'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['coop_local']
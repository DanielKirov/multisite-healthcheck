# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URLStatusLog'
        db.create_table(u'multi_health_urlstatuslog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('site_is_up', self.gf('django.db.models.fields.BooleanField')()),
            ('latest_update', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'multi_health', ['URLStatusLog'])


    def backwards(self, orm):
        # Deleting model 'URLStatusLog'
        db.delete_table(u'multi_health_urlstatuslog')


    models = {
        u'multi_health.urlstatuslog': {
            'Meta': {'object_name': 'URLStatusLog'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_update': ('django.db.models.fields.DateTimeField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'site_is_up': ('django.db.models.fields.BooleanField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['multi_health']
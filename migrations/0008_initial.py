# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BlogsBlog'
        db.create_table('blogs_blogsblog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='active', max_length=15, db_index=True)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('post_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('comment_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('blogs', ['BlogsBlog'])

        # Adding model 'BlogsPost'
        db.create_table('blogs_blogspost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blogs_blogspost_related', to=orm['auth.User'])),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_edit', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='active', max_length=15, db_index=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogs.BlogsBlog'], blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogs.BlogsPostImage'], null=True, blank=True)),
        ))
        db.send_create_signal('blogs', ['BlogsPost'])

        # Adding model 'BlogsPostImage'
        db.create_table('blogs_blogspostimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogs.BlogsPost'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('blogs', ['BlogsPostImage'])

        # Adding model 'BlogsPostComment'
        db.create_table('blogs_blogspostcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(default=0, related_name='blogs_blogspostcomment_related', null=True, blank=True, to=orm['blogs.BlogsPostComment'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blogs_blogspostcomment_related', to=orm['auth.User'])),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogs.BlogsPost'])),
        ))
        db.send_create_signal('blogs', ['BlogsPostComment'])


    def backwards(self, orm):
        
        # Deleting model 'BlogsBlog'
        db.delete_table('blogs_blogsblog')

        # Deleting model 'BlogsPost'
        db.delete_table('blogs_blogspost')

        # Deleting model 'BlogsPostImage'
        db.delete_table('blogs_blogspostimage')

        # Deleting model 'BlogsPostComment'
        db.delete_table('blogs_blogspostcomment')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 12, 12, 15, 36, 6, 243737, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 12, 12, 15, 36, 6, 243499, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'blogs.blogsblog': {
            'Meta': {'object_name': 'BlogsBlog'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'comment_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '15', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'blogs.blogspost': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'BlogsPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogs_blogspost_related'", 'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.BlogsBlog']", 'blank': 'True'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edit': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.BlogsPostImage']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '15', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'blogs.blogspostcomment': {
            'Meta': {'object_name': 'BlogsPostComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blogs_blogspostcomment_related'", 'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'default': '0', 'related_name': "'blogs_blogspostcomment_related'", 'null': 'True', 'blank': 'True', 'to': "orm['blogs.BlogsPostComment']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.BlogsPost']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'blogs.blogspostimage': {
            'Meta': {'object_name': 'BlogsPostImage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.BlogsPost']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogs']

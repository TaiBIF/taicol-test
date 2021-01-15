/code/mysite/mysite
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class 00E(models.Model):
    auto = models.AutoField(primary_key=True)
    name_code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '00e'


class 20130816Yen(models.Model):
    serial = models.IntegerField(db_column='Serial', primary_key=True)  # Field name made lowercase.
    tsid = models.CharField(db_column='TSID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s3 = models.CharField(db_column='S3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=255, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    order_c = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    family_c = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    本地是否圈養 = models.CharField(max_length=255, blank=True, null=True)
    原產地 = models.CharField(max_length=255, blank=True, null=True)
    輸入頻度 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '20130816yen'


class AlienStatus(models.Model):
    alien_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alien_status'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Changeid(models.Model):
    name_code_old = models.CharField(max_length=50, blank=True, null=True)
    name_code_new = models.CharField(primary_key=True, max_length=50)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'changeid'


class Coaendemic214(models.Model):
    serial = models.IntegerField(primary_key=True)
    big_group = models.CharField(max_length=255, blank=True, null=True)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    sname = models.CharField(max_length=255, blank=True, null=True)
    protection_level = models.CharField(max_length=255, blank=True, null=True)
    taibnet_id = models.CharField(db_column='TaiBNET_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taibnet_n = models.CharField(db_column='TaiBNET_n', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taibnet_v = models.CharField(db_column='TaiBNET_v', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sname_dlike = models.CharField(max_length=255, blank=True, null=True)
    common_dlike = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coaendemic214'


class Combo(models.Model):
    item = models.CharField(max_length=150)
    hierarchy = models.CharField(max_length=20, blank=True, null=True)
    is_virus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'combo'


class CommonNames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(max_length=255, blank=True, null=True)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    provider_id = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'common_names'


class Details(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    redlist2017 = models.CharField(max_length=10, blank=True, null=True)
    redlist2017_note = models.CharField(max_length=100, blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'


class Details20161226Bk(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_20161226bk'


class Details20161227(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_20161227'


class Details20180104(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_20180104'


class DetailsOld(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_old'


class Detailstoadd(models.Model):
    auto_id = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=255)
    redlist_nsc = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_wang_ass = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    iucn_assessment = models.CharField(max_length=255, blank=True, null=True)
    iucn_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    iucn_id = models.CharField(max_length=255, blank=True, null=True)
    iucn_group = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    coa_dateassessed = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    diagnosis_c = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    habitat_c = models.TextField(blank=True, null=True)
    habitat = models.TextField(blank=True, null=True)
    distribution_c = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    utility_c = models.TextField(blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    datelastmodified = models.CharField(max_length=255, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailstoadd'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Experts(models.Model):
    auto_id = models.AutoField(primary_key=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_e = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    institute_e = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_e = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_1 = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    telephone_1 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_e = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_e = models.CharField(max_length=255, blank=True, null=True)
    bioobject = models.CharField(max_length=255, blank=True, null=True)
    bioobject_e = models.CharField(max_length=255, blank=True, null=True)
    bioobject_detail = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    specialty_e = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    keyin_date = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experts'


class ExpertsCopy(models.Model):
    auto_id = models.AutoField(primary_key=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_e = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    institute_e = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_e = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_1 = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    telephone_1 = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_e = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_e = models.CharField(max_length=255, blank=True, null=True)
    bioobject = models.CharField(max_length=255, blank=True, null=True)
    bioobject_e = models.CharField(max_length=255, blank=True, null=True)
    bioobject_detail = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    specialty_e = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    keyin_date = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experts_copy'


class Families(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    subfamily = models.CharField(db_column='Subfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superfamily = models.CharField(db_column='Superfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suborder = models.CharField(db_column='Suborder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superorder = models.CharField(db_column='Superorder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subphylum = models.CharField(db_column='Subphylum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'families'


class Families20180509(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    subfamily = models.CharField(db_column='Subfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superfamily = models.CharField(db_column='Superfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suborder = models.CharField(db_column='Suborder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superorder = models.CharField(db_column='Superorder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subphylum = models.CharField(db_column='Subphylum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'families_20180509'


class FamiliesApg4Pre20170531(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    subfamily = models.CharField(db_column='Subfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superfamily = models.CharField(db_column='Superfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suborder = models.CharField(db_column='Suborder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superorder = models.CharField(db_column='Superorder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subphylum = models.CharField(db_column='Subphylum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'families_apg4pre_20170531'


class FamiliesCopy20170804(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    subfamily = models.CharField(db_column='Subfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tribe = models.CharField(db_column='Tribe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superfamily = models.CharField(db_column='Superfamily', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suborder = models.CharField(db_column='Suborder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superorder = models.CharField(db_column='Superorder', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subclass = models.CharField(db_column='Subclass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subphylum = models.CharField(db_column='Subphylum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'families_copy_20170804'


class FamiliesDel(models.Model):
    deldate = models.DateField(blank=True, null=True)
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    subfamily = models.CharField(max_length=50, blank=True, null=True)
    tribe = models.CharField(max_length=50, blank=True, null=True)
    superfamily = models.CharField(max_length=50, blank=True, null=True)
    suborder = models.CharField(max_length=50, blank=True, null=True)
    superorder = models.CharField(max_length=50, blank=True, null=True)
    subclass = models.CharField(max_length=50, blank=True, null=True)
    subphylum = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'families_del'


class FamiliesDelOriginal(models.Model):
    deldate = models.DateField(blank=True, null=True)
    auto_id = models.IntegerField()
    family_id = models.CharField(max_length=5, blank=True, null=True)
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'families_del_original'


class Fishdelete(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=255, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fishdelete'


class Fixurls(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(max_length=25, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    linkurl_eng = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixurls'


class GenusChinese(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    genus = models.CharField(max_length=70, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genus_chinese'
        unique_together = (('family_id', 'genus'),)


class GenusChineseCopy(models.Model):
    auto_id = models.AutoField(primary_key=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    genus = models.CharField(max_length=70, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genus_chinese_copy'
        unique_together = (('family_id', 'genus'),)


class Guestboard(models.Model):
    id = models.IntegerField(primary_key=True)
    original_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    e_mail = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    original = models.TextField(blank=True, null=True)
    response_from_ip = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guestboard'


class GuestboardCopy(models.Model):
    id = models.IntegerField(primary_key=True)
    original_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    e_mail = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    original = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guestboard_copy'


class IucnAcceptMatch(models.Model):
    primarykey = models.IntegerField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(max_length=255, blank=True, null=True)
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    kingdom_name = models.CharField(max_length=255, blank=True, null=True)
    phylum_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    order_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255, blank=True, null=True)
    genus_name = models.CharField(max_length=255, blank=True, null=True)
    species_name = models.CharField(max_length=255, blank=True, null=True)
    authority = models.CharField(max_length=255, blank=True, null=True)
    population = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    criteria = models.CharField(max_length=255, blank=True, null=True)
    annotation = models.CharField(max_length=255, blank=True, null=True)
    name_code = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iucn_accept_match'


class IucnSynoMatch(models.Model):
    primarykey = models.CharField(db_column='PrimaryKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scientific_name = models.CharField(max_length=255, blank=True, null=True)
    genus_name = models.CharField(max_length=255, blank=True, null=True)
    species_name = models.CharField(max_length=255, blank=True, null=True)
    authority = models.CharField(max_length=255, blank=True, null=True)
    infra_name = models.CharField(max_length=255, blank=True, null=True)
    infra_authority = models.CharField(max_length=255, blank=True, null=True)
    stock_name = models.CharField(max_length=255, blank=True, null=True)
    infra_rank = models.CharField(max_length=255, blank=True, null=True)
    fk_synonyms = models.CharField(db_column='FK_synonyms', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fk_species = models.CharField(db_column='FK_species', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name_code = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iucn_syno_match'


class Modihistry(models.Model):
    auto_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    process = models.CharField(max_length=10, blank=True, null=True)
    name_code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    new_name = models.CharField(max_length=50, blank=True, null=True)
    modifields = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modihistry'


class ModihistryOld(models.Model):
    auto_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    process = models.CharField(max_length=10, blank=True, null=True)
    name_code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    new_name = models.CharField(max_length=50, blank=True, null=True)
    modifields = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modihistry_old'


class Nametype(models.Model):
    auto_id = models.AutoField(primary_key=True)
    type_id = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nametype'


class News(models.Model):
    auto_id = models.AutoField(primary_key=True)
    inshort = models.CharField(max_length=255, blank=True, null=True)
    indate = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class NewsCopy(models.Model):
    auto_id = models.AutoField(primary_key=True)
    serial = models.IntegerField()
    inshort = models.CharField(max_length=255, blank=True, null=True)
    indate = models.DateField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_copy'
        unique_together = (('auto_id', 'serial'),)


class Newspecies(models.Model):
    auto_id = models.AutoField(primary_key=True)
    valid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_chinese = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_chinese = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_chinese = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_chinese = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_chinese = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    chinese_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    collect_date = models.CharField(max_length=50, blank=True, null=True)
    collector = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    characteristic = models.TextField(blank=True, null=True)
    habitats = models.TextField(blank=True, null=True)
    specimen = models.CharField(max_length=255, blank=True, null=True)
    data_provider = models.CharField(max_length=255, blank=True, null=True)
    data_provided_date = models.CharField(max_length=50, blank=True, null=True)
    data_provider_mail = models.CharField(max_length=50, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    news_report = models.TextField(blank=True, null=True)
    picture = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newspecies'


class Pcounter(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    pcounter = models.FloatField(primary_key=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcounter'


class PcounterOld(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    pcounter = models.FloatField(primary_key=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcounter_old'


class Photos(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(max_length=50, blank=True, null=True)
    is_type = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    folder = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)
    chinese_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    photographer = models.CharField(max_length=255, blank=True, null=True)
    uploader = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lon = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photos'


class Providers(models.Model):
    auto_id = models.AutoField(primary_key=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=255, blank=True, null=True)
    bioobject = models.CharField(max_length=50, blank=True, null=True)
    bioobject_e = models.CharField(max_length=50, blank=True, null=True)
    manager = models.CharField(max_length=50, blank=True, null=True)
    manager_e = models.CharField(max_length=50, blank=True, null=True)
    taxon_e = models.CharField(max_length=255, blank=True, null=True)
    taxon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'providers'


class RedlistBooks(models.Model):
    redlist_id = models.IntegerField(primary_key=True)
    columname = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    subject_e = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    publish_year = models.IntegerField(blank=True, null=True)
    citation = models.CharField(max_length=50, blank=True, null=True)
    citation_e = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redlist_books'


class RedlistTaiwan(models.Model):
    auto_id = models.IntegerField(unique=True, blank=True, null=True)
    taxon_name = models.CharField(max_length=100)
    name_c = models.CharField(max_length=50, blank=True, null=True)
    name_e = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=10)
    criteria = models.CharField(max_length=100, blank=True, null=True)
    adjusting = models.CharField(max_length=50, blank=True, null=True)
    taxon_group = models.CharField(max_length=50)
    name_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redlist_taiwan'


class ScientificNames(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    is_marine = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names'


class ScientificNames2(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names2'


class ScientificNames3(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names3'


class ScientificNames20161221(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20161221'


class ScientificNames20161226(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20161226'


class ScientificNames20161227(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20161227'


class ScientificNames20170417(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20170417'


class ScientificNames20180514(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20180514'


class ScientificNames20191030(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_20191030'


class ScientificNamesDel(models.Model):
    deldate = models.DateField(blank=True, null=True)
    auto_id = models.IntegerField()
    name_code = models.CharField(max_length=50, blank=True, null=True)
    name_code_sp2k = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=20, blank=True, null=True)
    subgenus = models.CharField(db_column='Subgenus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scientific_names_del'


class Statistics(models.Model):
    auto_id = models.AutoField(primary_key=True)
    viruses = models.CharField(max_length=30, blank=True, null=True)
    bacteria = models.CharField(max_length=30, blank=True, null=True)
    archaea = models.CharField(max_length=30, blank=True, null=True)
    protozoa = models.CharField(max_length=30, blank=True, null=True)
    chromista = models.CharField(max_length=30, blank=True, null=True)
    fungi = models.CharField(max_length=30, blank=True, null=True)
    plantae = models.CharField(max_length=30, blank=True, null=True)
    animalia = models.CharField(max_length=30, blank=True, null=True)
    kingdom = models.CharField(max_length=30, blank=True, null=True)
    phylum = models.CharField(max_length=30, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=30, blank=True, null=True)
    family = models.CharField(max_length=30, blank=True, null=True)
    genus = models.CharField(max_length=30, blank=True, null=True)
    species = models.CharField(max_length=30, blank=True, null=True)
    provider = models.CharField(max_length=30, blank=True, null=True)
    expert = models.CharField(max_length=30, blank=True, null=True)
    viruses_a = models.CharField(max_length=30, blank=True, null=True)
    bacteria_a = models.CharField(max_length=30, blank=True, null=True)
    archaea_a = models.CharField(max_length=30, blank=True, null=True)
    protozoa_a = models.CharField(max_length=30, blank=True, null=True)
    chromista_a = models.CharField(max_length=30, blank=True, null=True)
    fungi_a = models.CharField(max_length=30, blank=True, null=True)
    plantae_a = models.CharField(max_length=30, blank=True, null=True)
    animalia_a = models.CharField(max_length=30, blank=True, null=True)
    alien = models.CharField(max_length=30, blank=True, null=True)
    invasive = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics'


class Statuses(models.Model):
    auto_id = models.AutoField(primary_key=True)
    status_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    status_c = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuses'


class Suggestedlinks(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    linkurl_eng = models.CharField(max_length=255, blank=True, null=True)
    suggested_link_name = models.CharField(max_length=255, blank=True, null=True)
    suggested_link_name_eng = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suggestedlinks'


class SuggestedlinksCopy(models.Model):
    auto_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50, blank=True, null=True)
    linkurl = models.CharField(max_length=255, blank=True, null=True)
    linkurl_eng = models.CharField(max_length=255, blank=True, null=True)
    suggested_link_name = models.CharField(max_length=255, blank=True, null=True)
    suggested_link_name_eng = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suggestedlinks_copy'


class TableSpecieslist(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    is_marine = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    common_name_c = models.TextField(blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_specieslist'


class TableSpecieslist02(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    common_name_c = models.TextField(blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_specieslist_02'


class TableSpecieslist20160722(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    common_name_c = models.CharField(max_length=255, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_specieslist_20160722'


class TableSpecieslist20161221(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    common_name_c = models.TextField(blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_specieslist_20161221'


class TableSpecieslist20161227(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    name_code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    family_id = models.CharField(max_length=5, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    provider_id = models.SmallIntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    suggested_link = models.CharField(max_length=50, blank=True, null=True)
    common_name_c = models.TextField(blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    is_photo = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_specieslist_20161227'


class Tree(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    text = models.TextField(blank=True, null=True)
    texte = models.TextField(db_column='textE', blank=True, null=True)  # Field name made lowercase.
    textt = models.CharField(db_column='textT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    haschildren = models.IntegerField(db_column='hasChildren', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree'


class TreeCopy(models.Model):
    id = models.FloatField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    texte = models.TextField(db_column='textE', blank=True, null=True)  # Field name made lowercase.
    textt = models.CharField(db_column='textT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.FloatField(blank=True, null=True)
    haschildren = models.IntegerField(db_column='hasChildren', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_copy'


class Treeclass(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    kingdom2 = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treeclass'


class TreeclassCopy(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_id = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    kingdom2 = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treeclass_copy'


class Treefamily(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treefamily'


class TreefamilyCopy(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treefamily_copy'


class Treegenus(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treegenus'


class TreegenusCopy(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treegenus_copy'


class Treekingdom(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treekingdom'


class TreekingdomCopy(models.Model):
    kingdom_id = models.IntegerField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treekingdom_copy'


class Treeorder(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treeorder'


class TreeorderCopy(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treeorder_copy'


class Treephylum(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treephylum'


class TreephylumCopy(models.Model):
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum_id = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=255, blank=True, null=True)
    genus = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treephylum_copy'


class TreetopTable(models.Model):
    kingdom = models.IntegerField(blank=True, null=True)
    phylum = models.IntegerField(blank=True, null=True)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.IntegerField(blank=True, null=True)
    family = models.IntegerField(blank=True, null=True)
    genus = models.BigIntegerField(blank=True, null=True)
    species = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treetop_table'


class TreetopTableCopy(models.Model):
    kingdom = models.IntegerField(blank=True, null=True)
    phylum = models.IntegerField(blank=True, null=True)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.IntegerField(blank=True, null=True)
    family = models.IntegerField(blank=True, null=True)
    genus = models.BigIntegerField(blank=True, null=True)
    species = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treetop_table_copy'


class User(models.Model):
    auto_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    chinesename = models.CharField(max_length=50, blank=True, null=True)
    englishname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    hierarchy = models.CharField(max_length=50, blank=True, null=True)
    taxon = models.CharField(max_length=255, blank=True, null=True)
    creatdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Userlogin(models.Model):
    user = models.CharField(max_length=50, blank=True, null=True)
    logindate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlogin'


class Userresponse(models.Model):
    auto_id = models.AutoField(primary_key=True)
    name_code = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=150, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    cc = models.CharField(max_length=50, blank=True, null=True)
    watchback = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userresponse'


class ViewAlternativeNameC(models.Model):
    name_code = models.CharField(max_length=255, blank=True, null=True)
    alternative_name_c = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_alternative_name_c'


class ViewApioutput(models.Model):
    name_code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    infraspecies_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies = models.CharField(max_length=50, blank=True, null=True)
    infraspecies2_marker = models.CharField(max_length=20, blank=True, null=True)
    infraspecies2 = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    author2 = models.CharField(max_length=150, blank=True, null=True)
    is_accepted_name = models.IntegerField(blank=True, null=True)
    accepted_name_code = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    is_endemic = models.IntegerField(blank=True, null=True)
    alien_status = models.IntegerField(blank=True, null=True)
    is_marine = models.IntegerField(blank=True, null=True)
    is_fossil = models.IntegerField(blank=True, null=True)
    ref_short = models.CharField(max_length=200, blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    datelastmodified = models.DateField(blank=True, null=True)
    kingdom = models.CharField(max_length=50, blank=True, null=True)
    kingdom_c = models.CharField(max_length=50, blank=True, null=True)
    phylum = models.CharField(max_length=50, blank=True, null=True)
    phylum_c = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    class_c = models.CharField(max_length=50, blank=True, null=True)
    order = models.CharField(max_length=50, blank=True, null=True)
    order_c = models.CharField(max_length=50, blank=True, null=True)
    family = models.CharField(max_length=50, blank=True, null=True)
    family_c = models.CharField(max_length=50, blank=True, null=True)
    genus_c = models.CharField(max_length=50, blank=True, null=True)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    alternative_name_c = models.TextField(blank=True, null=True)
    iucn_code = models.CharField(max_length=255, blank=True, null=True)
    cites_code = models.CharField(max_length=255, blank=True, null=True)
    coa_redlist_code = models.CharField(max_length=255, blank=True, null=True)
    redlist2017 = models.CharField(max_length=10, blank=True, null=True)
    redlist_wang = models.CharField(max_length=255, blank=True, null=True)
    redlist_chen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_apioutput'


class ViewGetchinesen(models.Model):
    name_code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_getchinesen'


class ViewGetchinesenCopy(models.Model):
    name_code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_getchinesen_copy'


class ViewGetenglishn(models.Model):
    name_code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_getenglishn'


class Windtable1(models.Model):
    id = models.IntegerField(primary_key=True)
    name_code = models.FloatField(blank=True, null=True)
    name_project = models.CharField(max_length=255, blank=True, null=True)
    name_species_socalled = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'windtable1'

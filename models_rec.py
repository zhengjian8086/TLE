# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssignmentStatus(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'assignment_status'


class AssignmentTypes(models.Model):
    fk_table = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'assignment_types'


class Attachments(models.Model):
    fk_id = models.PositiveIntegerField()
    fk_table = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    file_name = models.CharField(max_length=250)
    file_path = models.CharField(max_length=250, blank=True, null=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=250)
    date_added = models.DateTimeField()
    content = models.TextField(blank=True, null=True)
    compression_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attachments'


class Builds(models.Model):
    testplan_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    release_date = models.DateField(blank=True, null=True)
    closed_on_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'builds'
        unique_together = (('testplan_id', 'name'),)


class CfieldBuildDesignValues(models.Model):
    field_id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'cfield_build_design_values'
        unique_together = (('field_id', 'node_id'),)


class CfieldDesignValues(models.Model):
    field_id = models.IntegerField(primary_key=True)
    node_id = models.IntegerField()
    value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'cfield_design_values'
        unique_together = (('field_id', 'node_id'),)


class CfieldExecutionValues(models.Model):
    field_id = models.IntegerField(primary_key=True)
    execution_id = models.IntegerField()
    testplan_id = models.IntegerField()
    tcversion_id = models.IntegerField()
    value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'cfield_execution_values'
        unique_together = (('field_id', 'execution_id', 'testplan_id', 'tcversion_id'),)


class CfieldNodeTypes(models.Model):
    field_id = models.IntegerField(primary_key=True)
    node_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cfield_node_types'
        unique_together = (('field_id', 'node_type_id'),)


class CfieldTestplanDesignValues(models.Model):
    field_id = models.IntegerField(primary_key=True)
    link_id = models.IntegerField()
    value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'cfield_testplan_design_values'
        unique_together = (('field_id', 'link_id'),)


class CfieldTestprojects(models.Model):
    field_id = models.PositiveIntegerField(primary_key=True)
    testproject_id = models.PositiveIntegerField()
    display_order = models.PositiveSmallIntegerField()
    location = models.PositiveSmallIntegerField()
    active = models.IntegerField()
    required = models.IntegerField()
    required_on_design = models.IntegerField()
    required_on_execution = models.IntegerField()
    monitorable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cfield_testprojects'
        unique_together = (('field_id', 'testproject_id'),)


class Codetrackers(models.Model):
    name = models.CharField(unique=True, max_length=100)
    type = models.IntegerField(blank=True, null=True)
    cfg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codetrackers'


class CustomFields(models.Model):
    name = models.CharField(unique=True, max_length=64)
    label = models.CharField(max_length=64)
    type = models.SmallIntegerField()
    possible_values = models.CharField(max_length=4000)
    default_value = models.CharField(max_length=4000)
    valid_regexp = models.CharField(max_length=255)
    length_min = models.IntegerField()
    length_max = models.IntegerField()
    show_on_design = models.PositiveIntegerField()
    enable_on_design = models.PositiveIntegerField()
    show_on_execution = models.PositiveIntegerField()
    enable_on_execution = models.PositiveIntegerField()
    show_on_testplan_design = models.PositiveIntegerField()
    enable_on_testplan_design = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'custom_fields'


class DbVersion(models.Model):
    version = models.CharField(primary_key=True, max_length=50)
    upgrade_ts = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_version'


class Events(models.Model):
    transaction_id = models.PositiveIntegerField()
    log_level = models.PositiveSmallIntegerField()
    source = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField()
    fired_at = models.PositiveIntegerField()
    activity = models.CharField(max_length=45, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class ExecutionBugs(models.Model):
    execution_id = models.PositiveIntegerField(primary_key=True)
    bug_id = models.CharField(max_length=64)
    tcstep_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'execution_bugs'
        unique_together = (('execution_id', 'bug_id', 'tcstep_id'),)


class ExecutionTcsteps(models.Model):
    execution_id = models.PositiveIntegerField()
    tcstep_id = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'execution_tcsteps'
        unique_together = (('execution_id', 'tcstep_id'),)


class Executions(models.Model):
    build_id = models.IntegerField()
    tester_id = models.PositiveIntegerField(blank=True, null=True)
    execution_ts = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    testplan_id = models.PositiveIntegerField()
    tcversion_id = models.PositiveIntegerField()
    tcversion_number = models.PositiveSmallIntegerField()
    platform_id = models.PositiveIntegerField()
    execution_type = models.IntegerField()
    execution_duration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'executions'


class Inventory(models.Model):
    testproject_id = models.PositiveIntegerField()
    owner_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    ipaddress = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    modification_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Issuetrackers(models.Model):
    name = models.CharField(unique=True, max_length=100)
    type = models.IntegerField(blank=True, null=True)
    cfg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issuetrackers'


class Keywords(models.Model):
    keyword = models.CharField(max_length=100)
    testproject_id = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keywords'
        unique_together = (('keyword', 'testproject_id'),)


class Milestones(models.Model):
    testplan_id = models.PositiveIntegerField()
    target_date = models.DateField(blank=True, null=True)
    start_date = models.DateField()
    a = models.PositiveIntegerField()
    b = models.PositiveIntegerField()
    c = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'milestones'
        unique_together = (('name', 'testplan_id'),)


class NodeTypes(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'node_types'


class NodesHierarchy(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    node_type_id = models.PositiveIntegerField()
    node_order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes_hierarchy'


class ObjectKeywords(models.Model):
    fk_id = models.PositiveIntegerField()
    fk_table = models.CharField(max_length=30, blank=True, null=True)
    keyword_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'object_keywords'
        unique_together = (('fk_id', 'fk_table', 'keyword_id'),)


class Platforms(models.Model):
    name = models.CharField(max_length=100)
    testproject_id = models.PositiveIntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'platforms'
        unique_together = (('testproject_id', 'name'),)


class Plugins(models.Model):
    basename = models.CharField(max_length=100)
    enabled = models.IntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plugins'


class PluginsConfiguration(models.Model):
    testproject_id = models.IntegerField()
    config_key = models.CharField(max_length=255)
    config_type = models.IntegerField()
    config_value = models.CharField(max_length=255)
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plugins_configuration'


class ReqCoverage(models.Model):
    req_id = models.IntegerField()
    req_version_id = models.IntegerField()
    testcase_id = models.IntegerField()
    tcversion_id = models.IntegerField()
    link_status = models.IntegerField()
    is_active = models.IntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    review_requester_id = models.PositiveIntegerField(blank=True, null=True)
    review_request_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_coverage'
        unique_together = (('req_id', 'req_version_id', 'testcase_id', 'tcversion_id'),)


class ReqMonitor(models.Model):
    req_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    testproject_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_monitor'
        unique_together = (('req_id', 'user_id', 'testproject_id'),)


class ReqRelations(models.Model):
    source_id = models.PositiveIntegerField()
    destination_id = models.PositiveIntegerField()
    relation_type = models.PositiveSmallIntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'req_relations'


class ReqRevisions(models.Model):
    parent_id = models.PositiveIntegerField()
    id = models.PositiveIntegerField(primary_key=True)
    revision = models.PositiveSmallIntegerField()
    req_doc_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=1, blank=True, null=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    log_message = models.TextField(blank=True, null=True)
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.PositiveIntegerField(blank=True, null=True)
    modification_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'req_revisions'
        unique_together = (('parent_id', 'revision'),)


class ReqSpecs(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    testproject_id = models.PositiveIntegerField()
    doc_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'req_specs'
        unique_together = (('doc_id', 'testproject_id'),)


class ReqSpecsRevisions(models.Model):
    parent_id = models.PositiveIntegerField()
    id = models.PositiveIntegerField(primary_key=True)
    revision = models.PositiveSmallIntegerField()
    doc_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    total_req = models.IntegerField()
    status = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    log_message = models.TextField(blank=True, null=True)
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.PositiveIntegerField(blank=True, null=True)
    modification_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'req_specs_revisions'
        unique_together = (('parent_id', 'revision'),)


class ReqVersions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    version = models.PositiveSmallIntegerField()
    revision = models.PositiveSmallIntegerField()
    scope = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=1, blank=True, null=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    modifier_id = models.PositiveIntegerField(blank=True, null=True)
    modification_ts = models.DateTimeField()
    log_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_versions'


class Reqmgrsystems(models.Model):
    name = models.CharField(unique=True, max_length=100)
    type = models.IntegerField(blank=True, null=True)
    cfg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reqmgrsystems'


class Requirements(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    srs_id = models.PositiveIntegerField()
    req_doc_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'requirements'
        unique_together = (('srs_id', 'req_doc_id'),)


class Rights(models.Model):
    description = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'rights'


class RiskAssignments(models.Model):
    testplan_id = models.PositiveIntegerField()
    node_id = models.PositiveIntegerField()
    risk = models.CharField(max_length=1)
    importance = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'risk_assignments'
        unique_together = (('testplan_id', 'node_id'),)


class RoleRights(models.Model):
    role_id = models.IntegerField(primary_key=True)
    right_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role_rights'
        unique_together = (('role_id', 'right_id'),)


class Roles(models.Model):
    description = models.CharField(unique=True, max_length=100)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Tcsteps(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    step_number = models.IntegerField()
    actions = models.TextField(blank=True, null=True)
    expected_results = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    execution_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tcsteps'


class Tcversions(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    tc_external_id = models.PositiveIntegerField(blank=True, null=True)
    version = models.PositiveSmallIntegerField()
    layout = models.PositiveSmallIntegerField()
    status = models.PositiveSmallIntegerField()
    summary = models.TextField(blank=True, null=True)
    preconditions = models.TextField(blank=True, null=True)
    importance = models.PositiveSmallIntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    updater_id = models.PositiveIntegerField(blank=True, null=True)
    modification_ts = models.DateTimeField()
    active = models.IntegerField()
    is_open = models.IntegerField()
    execution_type = models.IntegerField()
    estimated_exec_duration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcversions'


class TestcaseKeywords(models.Model):
    testcase_id = models.PositiveIntegerField()
    tcversion_id = models.PositiveIntegerField()
    keyword_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'testcase_keywords'
        unique_together = (('testcase_id', 'tcversion_id', 'keyword_id'),)


class TestcaseRelations(models.Model):
    source_id = models.PositiveIntegerField()
    destination_id = models.PositiveIntegerField()
    link_status = models.IntegerField()
    relation_type = models.PositiveSmallIntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testcase_relations'


class TestcaseScriptLinks(models.Model):
    tcversion_id = models.PositiveIntegerField(primary_key=True)
    project_key = models.CharField(max_length=64)
    repository_name = models.CharField(max_length=64)
    code_path = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=64, blank=True, null=True)
    commit_id = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testcase_script_links'
        unique_together = (('tcversion_id', 'project_key', 'repository_name', 'code_path'),)


class TestplanPlatforms(models.Model):
    testplan_id = models.PositiveIntegerField()
    platform_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'testplan_platforms'
        unique_together = (('testplan_id', 'platform_id'),)


class TestplanTcversions(models.Model):
    testplan_id = models.PositiveIntegerField()
    tcversion_id = models.PositiveIntegerField()
    node_order = models.PositiveIntegerField()
    urgency = models.SmallIntegerField()
    platform_id = models.PositiveIntegerField()
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testplan_tcversions'
        unique_together = (('testplan_id', 'tcversion_id', 'platform_id'),)


class Testplans(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    testproject_id = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    is_public = models.IntegerField()
    api_key = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'testplans'


class TestprojectCodetracker(models.Model):
    testproject_id = models.PositiveIntegerField(primary_key=True)
    codetracker_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'testproject_codetracker'


class TestprojectIssuetracker(models.Model):
    testproject_id = models.PositiveIntegerField(primary_key=True)
    issuetracker_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'testproject_issuetracker'


class TestprojectReqmgrsystem(models.Model):
    testproject_id = models.PositiveIntegerField(primary_key=True)
    reqmgrsystem_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'testproject_reqmgrsystem'


class Testprojects(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    notes = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=12)
    active = models.IntegerField()
    option_reqs = models.IntegerField()
    option_priority = models.IntegerField()
    option_automation = models.IntegerField()
    options = models.TextField(blank=True, null=True)
    prefix = models.CharField(unique=True, max_length=16)
    tc_counter = models.PositiveIntegerField()
    is_public = models.IntegerField()
    issue_tracker_enabled = models.IntegerField()
    code_tracker_enabled = models.IntegerField()
    reqmgr_integration_enabled = models.IntegerField()
    api_key = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'testprojects'


class Testsuites(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testsuites'


class TextTemplates(models.Model):
    id = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    template_data = models.TextField(blank=True, null=True)
    author_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    is_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'text_templates'
        unique_together = (('type', 'title'),)


class Transactions(models.Model):
    entry_point = models.CharField(max_length=45)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    session_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserAssignments(models.Model):
    type = models.PositiveIntegerField()
    feature_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField(blank=True, null=True)
    build_id = models.PositiveIntegerField(blank=True, null=True)
    deadline_ts = models.DateTimeField(blank=True, null=True)
    assigner_id = models.PositiveIntegerField(blank=True, null=True)
    creation_ts = models.DateTimeField()
    status = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_assignments'


class UserGroup(models.Model):
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'


class UserGroupAssign(models.Model):
    usergroup_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'user_group_assign'
        unique_together = (('usergroup_id', 'user_id'),)


class UserTestplanRoles(models.Model):
    user_id = models.IntegerField(primary_key=True)
    testplan_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_testplan_roles'
        unique_together = (('user_id', 'testplan_id'),)


class UserTestprojectRoles(models.Model):
    user_id = models.IntegerField(primary_key=True)
    testproject_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_testproject_roles'
        unique_together = (('user_id', 'testproject_id'),)


class Users(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=32)
    role_id = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    locale = models.CharField(max_length=10)
    default_testproject_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    script_key = models.CharField(max_length=32, blank=True, null=True)
    cookie_string = models.CharField(unique=True, max_length=64)
    auth_method = models.CharField(max_length=10, blank=True, null=True)
    creation_ts = models.DateTimeField()
    expiration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

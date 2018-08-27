# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessTokens(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.TextField()
    device_id = models.TextField(blank=True, null=True)
    token = models.TextField(unique=True)
    last_used = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'access_tokens'


class AccountData(models.Model):
    user_id = models.TextField()
    account_data_type = models.TextField()
    stream_id = models.BigIntegerField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_data'
        unique_together = (('user_id', 'account_data_type'),)


class AccountDataMaxStreamId(models.Model):
    lock = models.CharField(unique=True, max_length=1)
    stream_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'account_data_max_stream_id'


class ApplicationServices(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.TextField(blank=True, null=True)
    token = models.TextField(unique=True, blank=True, null=True)
    hs_token = models.TextField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_services'


class ApplicationServicesRegex(models.Model):
    id = models.BigIntegerField(primary_key=True)
    as_field = models.ForeignKey(ApplicationServices, models.DO_NOTHING, db_column='as_id')  # Field renamed because it was a Python reserved word.
    namespace = models.IntegerField(blank=True, null=True)
    regex = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_services_regex'


class ApplicationServicesState(models.Model):
    as_id = models.TextField(primary_key=True)
    state = models.CharField(max_length=5, blank=True, null=True)
    last_txn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_services_state'


class ApplicationServicesTxns(models.Model):
    as_id = models.TextField()
    txn_id = models.IntegerField()
    event_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'application_services_txns'
        unique_together = (('as_id', 'txn_id'),)


class AppliedModuleSchemas(models.Model):
    module_name = models.TextField()
    file = models.TextField()

    class Meta:
        managed = False
        db_table = 'applied_module_schemas'
        unique_together = (('module_name', 'file'),)


class AppliedSchemaDeltas(models.Model):
    version = models.IntegerField()
    file = models.TextField()

    class Meta:
        managed = False
        db_table = 'applied_schema_deltas'
        unique_together = (('version', 'file'),)


class AppserviceRoomList(models.Model):
    appservice_id = models.TextField()
    network_id = models.TextField()
    room_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'appservice_room_list'
        unique_together = (('appservice_id', 'network_id', 'room_id'),)


class AppserviceStreamPosition(models.Model):
    lock = models.CharField(unique=True, max_length=1)
    stream_ordering = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appservice_stream_position'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class BackgroundUpdates(models.Model):
    update_name = models.TextField(unique=True)
    progress_json = models.TextField()
    depends_on = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'background_updates'


class BlockedRooms(models.Model):
    room_id = models.TextField(unique=True)
    user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'blocked_rooms'


class CacheInvalidationStream(models.Model):
    stream_id = models.BigIntegerField(blank=True, null=True)
    cache_func = models.TextField(blank=True, null=True)
    keys = models.TextField(blank=True, null=True)  # This field type is a guess.
    invalidation_ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cache_invalidation_stream'


class CurrentStateDeltaStream(models.Model):
    stream_id = models.BigIntegerField()
    room_id = models.TextField()
    type = models.TextField()
    state_key = models.TextField()
    event_id = models.TextField(blank=True, null=True)
    prev_event_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_state_delta_stream'


class CurrentStateEvents(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    type = models.TextField()
    state_key = models.TextField()

    class Meta:
        managed = False
        db_table = 'current_state_events'
        unique_together = (('room_id', 'type', 'state_key'),)


class CurrentStateResets(models.Model):
    event_stream_ordering = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'current_state_resets'


class DeletedPushers(models.Model):
    stream_id = models.BigIntegerField()
    app_id = models.TextField()
    pushkey = models.TextField()
    user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'deleted_pushers'


class Destinations(models.Model):
    destination = models.TextField(primary_key=True)
    retry_last_ts = models.BigIntegerField(blank=True, null=True)
    retry_interval = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinations'


class DeviceFederationInbox(models.Model):
    origin = models.TextField()
    message_id = models.TextField()
    received_ts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'device_federation_inbox'


class DeviceFederationOutbox(models.Model):
    destination = models.TextField()
    stream_id = models.BigIntegerField()
    queued_ts = models.BigIntegerField()
    messages_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_federation_outbox'


class DeviceInbox(models.Model):
    user_id = models.TextField()
    device_id = models.TextField()
    stream_id = models.BigIntegerField()
    message_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_inbox'


class DeviceListsOutboundLastSuccess(models.Model):
    destination = models.TextField()
    user_id = models.TextField()
    stream_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'device_lists_outbound_last_success'


class DeviceListsOutboundPokes(models.Model):
    destination = models.TextField()
    stream_id = models.BigIntegerField()
    user_id = models.TextField()
    device_id = models.TextField()
    sent = models.BooleanField()
    ts = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'device_lists_outbound_pokes'


class DeviceListsRemoteCache(models.Model):
    user_id = models.TextField()
    device_id = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_lists_remote_cache'


class DeviceListsRemoteExtremeties(models.Model):
    user_id = models.TextField()
    stream_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_lists_remote_extremeties'


class DeviceListsStream(models.Model):
    stream_id = models.BigIntegerField()
    user_id = models.TextField()
    device_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'device_lists_stream'


class DeviceMaxStreamId(models.Model):
    stream_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'device_max_stream_id'


class Devices(models.Model):
    user_id = models.TextField()
    device_id = models.TextField()
    display_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'
        unique_together = (('user_id', 'device_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class E2EDeviceKeysJson(models.Model):
    user_id = models.TextField()
    device_id = models.TextField()
    ts_added_ms = models.BigIntegerField()
    key_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'e2e_device_keys_json'
        unique_together = (('user_id', 'device_id'),)


class E2EOneTimeKeysJson(models.Model):
    user_id = models.TextField()
    device_id = models.TextField()
    algorithm = models.TextField()
    key_id = models.TextField()
    ts_added_ms = models.BigIntegerField()
    key_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'e2e_one_time_keys_json'
        unique_together = (('user_id', 'device_id', 'algorithm', 'key_id'),)


class ErasedUsers(models.Model):
    user_id = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'erased_users'


class EventAuth(models.Model):
    event_id = models.TextField()
    auth_id = models.TextField()
    room_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_auth'


class EventBackwardExtremities(models.Model):
    event_id = models.TextField()
    room_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_backward_extremities'
        unique_together = (('event_id', 'room_id'),)


class EventContentHashes(models.Model):
    event_id = models.TextField(blank=True, null=True)
    algorithm = models.TextField(blank=True, null=True)
    hash = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_content_hashes'
        unique_together = (('event_id', 'algorithm'),)


class EventDestinations(models.Model):
    event_id = models.TextField()
    destination = models.TextField()
    delivered_ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_destinations'
        unique_together = (('event_id', 'destination'),)


class EventEdgeHashes(models.Model):
    event_id = models.TextField(blank=True, null=True)
    prev_event_id = models.TextField(blank=True, null=True)
    algorithm = models.TextField(blank=True, null=True)
    hash = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_edge_hashes'
        unique_together = (('event_id', 'prev_event_id', 'algorithm'),)


class EventEdges(models.Model):
    event_id = models.TextField()
    prev_event_id = models.TextField()
    room_id = models.TextField()
    is_state = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'event_edges'
        unique_together = (('event_id', 'prev_event_id', 'room_id', 'is_state'),)


class EventForwardExtremities(models.Model):
    event_id = models.TextField()
    room_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_forward_extremities'
        unique_together = (('event_id', 'room_id'),)


class EventJson(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    internal_metadata = models.TextField()
    json = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_json'


class EventPushActions(models.Model):
    room_id = models.TextField()
    event_id = models.TextField()
    user_id = models.TextField()
    profile_tag = models.CharField(max_length=32, blank=True, null=True)
    actions = models.TextField()
    topological_ordering = models.BigIntegerField(blank=True, null=True)
    stream_ordering = models.BigIntegerField(blank=True, null=True)
    notif = models.SmallIntegerField(blank=True, null=True)
    highlight = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_push_actions'
        unique_together = (('room_id', 'event_id', 'user_id', 'profile_tag'),)


class EventPushActionsStaging(models.Model):
    event_id = models.TextField()
    user_id = models.TextField()
    actions = models.TextField()
    notif = models.SmallIntegerField()
    highlight = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'event_push_actions_staging'


class EventPushSummary(models.Model):
    user_id = models.TextField()
    room_id = models.TextField()
    notif_count = models.BigIntegerField()
    stream_ordering = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event_push_summary'


class EventPushSummaryStreamOrdering(models.Model):
    lock = models.CharField(unique=True, max_length=1)
    stream_ordering = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event_push_summary_stream_ordering'


class EventReferenceHashes(models.Model):
    event_id = models.TextField(blank=True, null=True)
    algorithm = models.TextField(blank=True, null=True)
    hash = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_reference_hashes'
        unique_together = (('event_id', 'algorithm'),)


class EventReports(models.Model):
    id = models.BigIntegerField(primary_key=True)
    received_ts = models.BigIntegerField()
    room_id = models.TextField()
    event_id = models.TextField()
    user_id = models.TextField()
    reason = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_reports'


class EventSearch(models.Model):
    event_id = models.TextField(unique=True, blank=True, null=True)
    room_id = models.TextField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    vector = models.TextField(blank=True, null=True)  # This field type is a guess.
    origin_server_ts = models.BigIntegerField(blank=True, null=True)
    stream_ordering = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_search'


class EventSignatures(models.Model):
    event_id = models.TextField(blank=True, null=True)
    signature_name = models.TextField(blank=True, null=True)
    key_id = models.TextField(blank=True, null=True)
    signature = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_signatures'
        unique_together = (('event_id', 'signature_name', 'key_id'),)


class EventToStateGroups(models.Model):
    event_id = models.TextField(unique=True)
    state_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event_to_state_groups'


class Events(models.Model):
    stream_ordering = models.IntegerField(primary_key=True)
    topological_ordering = models.BigIntegerField()
    event_id = models.TextField(unique=True)
    type = models.TextField()
    room_id = models.TextField()
    content = models.TextField(blank=True, null=True)
    unrecognized_keys = models.TextField(blank=True, null=True)
    processed = models.BooleanField()
    outlier = models.BooleanField()
    depth = models.BigIntegerField()
    origin_server_ts = models.BigIntegerField(blank=True, null=True)
    received_ts = models.BigIntegerField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)
    contains_url = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'events'


class ExOutlierStream(models.Model):
    event_stream_ordering = models.BigIntegerField(primary_key=True)
    event_id = models.TextField()
    state_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ex_outlier_stream'


class FederationStreamPosition(models.Model):
    type = models.TextField()
    stream_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'federation_stream_position'


class Feedback(models.Model):
    event_id = models.TextField(unique=True)
    feedback_type = models.TextField(blank=True, null=True)
    target_event_id = models.TextField(blank=True, null=True)
    sender = models.TextField(blank=True, null=True)
    room_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class GroupAttestationsRemote(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()
    valid_until_ms = models.BigIntegerField()
    attestation_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'group_attestations_remote'


class GroupAttestationsRenewals(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()
    valid_until_ms = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'group_attestations_renewals'


class GroupInvites(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'group_invites'
        unique_together = (('group_id', 'user_id'),)


class GroupRoles(models.Model):
    group_id = models.TextField()
    role_id = models.TextField()
    profile = models.TextField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_roles'
        unique_together = (('group_id', 'role_id'),)


class GroupRoomCategories(models.Model):
    group_id = models.TextField()
    category_id = models.TextField()
    profile = models.TextField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_room_categories'
        unique_together = (('group_id', 'category_id'),)


class GroupRooms(models.Model):
    group_id = models.TextField()
    room_id = models.TextField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_rooms'
        unique_together = (('group_id', 'room_id'),)


class GroupSummaryRoles(models.Model):
    group_id = models.TextField()
    role_id = models.TextField()
    role_order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'group_summary_roles'
        unique_together = (('group_id', 'role_id', 'role_order'),)


class GroupSummaryRoomCategories(models.Model):
    group_id = models.TextField()
    category_id = models.TextField()
    cat_order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'group_summary_room_categories'
        unique_together = (('group_id', 'category_id', 'cat_order'),)


class GroupSummaryRooms(models.Model):
    group_id = models.TextField()
    room_id = models.TextField()
    category_id = models.TextField()
    room_order = models.BigIntegerField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_summary_rooms'
        unique_together = (('group_id', 'category_id', 'room_id', 'room_order'), ('group_id', 'room_id', 'category_id'),)


class GroupSummaryUsers(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()
    role_id = models.TextField()
    user_order = models.BigIntegerField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_summary_users'


class GroupUsers(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()
    is_admin = models.BooleanField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_users'
        unique_together = (('group_id', 'user_id'),)


class Groups(models.Model):
    group_id = models.TextField(unique=True)
    name = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField()
    join_policy = models.TextField()

    class Meta:
        managed = False
        db_table = 'groups'


class GuestAccess(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    guest_access = models.TextField()

    class Meta:
        managed = False
        db_table = 'guest_access'


class HistoryVisibility(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    history_visibility = models.TextField()

    class Meta:
        managed = False
        db_table = 'history_visibility'


class LocalGroupMembership(models.Model):
    group_id = models.TextField()
    user_id = models.TextField()
    is_admin = models.BooleanField()
    membership = models.TextField()
    is_publicised = models.BooleanField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'local_group_membership'


class LocalGroupUpdates(models.Model):
    stream_id = models.BigIntegerField()
    group_id = models.TextField()
    user_id = models.TextField()
    type = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'local_group_updates'


class LocalInvites(models.Model):
    stream_id = models.BigIntegerField()
    inviter = models.TextField()
    invitee = models.TextField()
    event_id = models.TextField()
    room_id = models.TextField()
    locally_rejected = models.TextField(blank=True, null=True)
    replaced_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_invites'


class LocalMediaRepository(models.Model):
    media_id = models.TextField(unique=True, blank=True, null=True)
    media_type = models.TextField(blank=True, null=True)
    media_length = models.IntegerField(blank=True, null=True)
    created_ts = models.BigIntegerField(blank=True, null=True)
    upload_name = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    quarantined_by = models.TextField(blank=True, null=True)
    url_cache = models.TextField(blank=True, null=True)
    last_access_ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_media_repository'


class LocalMediaRepositoryThumbnails(models.Model):
    media_id = models.TextField(blank=True, null=True)
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    thumbnail_type = models.TextField(blank=True, null=True)
    thumbnail_method = models.TextField(blank=True, null=True)
    thumbnail_length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_media_repository_thumbnails'
        unique_together = (('media_id', 'thumbnail_width', 'thumbnail_height', 'thumbnail_type'),)


class LocalMediaRepositoryUrlCache(models.Model):
    url = models.TextField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    etag = models.TextField(blank=True, null=True)
    expires_ts = models.BigIntegerField(blank=True, null=True)
    og = models.TextField(blank=True, null=True)
    media_id = models.TextField(blank=True, null=True)
    download_ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_media_repository_url_cache'


class MonthlyActiveUsers(models.Model):
    user_id = models.TextField(unique=True)
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'monthly_active_users'


class OpenIdTokens(models.Model):
    token = models.TextField(primary_key=True)
    ts_valid_until_ms = models.BigIntegerField()
    user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'open_id_tokens'


class Presence(models.Model):
    user_id = models.TextField(unique=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    status_msg = models.TextField(blank=True, null=True)
    mtime = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presence'


class PresenceAllowInbound(models.Model):
    observed_user_id = models.TextField()
    observer_user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'presence_allow_inbound'
        unique_together = (('observed_user_id', 'observer_user_id'),)


class PresenceList(models.Model):
    user_id = models.TextField()
    observed_user_id = models.TextField()
    accepted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'presence_list'
        unique_together = (('user_id', 'observed_user_id'),)


class PresenceStream(models.Model):
    stream_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    last_active_ts = models.BigIntegerField(blank=True, null=True)
    last_federation_update_ts = models.BigIntegerField(blank=True, null=True)
    last_user_sync_ts = models.BigIntegerField(blank=True, null=True)
    status_msg = models.TextField(blank=True, null=True)
    currently_active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'presence_stream'


class Profiles(models.Model):
    user_id = models.TextField(unique=True)
    displayname = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class PublicRoomListStream(models.Model):
    stream_id = models.BigIntegerField()
    room_id = models.TextField()
    visibility = models.BooleanField()
    appservice_id = models.TextField(blank=True, null=True)
    network_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_room_list_stream'


class PushRules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_name = models.TextField()
    rule_id = models.TextField()
    priority_class = models.SmallIntegerField()
    priority = models.IntegerField()
    conditions = models.TextField()
    actions = models.TextField()

    class Meta:
        managed = False
        db_table = 'push_rules'
        unique_together = (('user_name', 'rule_id'),)


class PushRulesEnable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_name = models.TextField()
    rule_id = models.TextField()
    enabled = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_rules_enable'
        unique_together = (('user_name', 'rule_id'),)


class PushRulesStream(models.Model):
    stream_id = models.BigIntegerField()
    event_stream_ordering = models.BigIntegerField()
    user_id = models.TextField()
    rule_id = models.TextField()
    op = models.TextField()
    priority_class = models.SmallIntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    actions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_rules_stream'


class PusherThrottle(models.Model):
    pusher = models.BigIntegerField(primary_key=True)
    room_id = models.TextField()
    last_sent_ts = models.BigIntegerField(blank=True, null=True)
    throttle_ms = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pusher_throttle'
        unique_together = (('pusher', 'room_id'),)


class Pushers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_name = models.TextField()
    access_token = models.BigIntegerField(blank=True, null=True)
    profile_tag = models.TextField()
    kind = models.TextField()
    app_id = models.TextField()
    app_display_name = models.TextField()
    device_display_name = models.TextField()
    pushkey = models.TextField()
    ts = models.BigIntegerField()
    lang = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    last_stream_ordering = models.IntegerField(blank=True, null=True)
    last_success = models.BigIntegerField(blank=True, null=True)
    failing_since = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pushers'
        unique_together = (('app_id', 'pushkey', 'user_name'),)


class RatelimitOverride(models.Model):
    user_id = models.TextField(unique=True)
    messages_per_second = models.BigIntegerField(blank=True, null=True)
    burst_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratelimit_override'


class ReceiptsGraph(models.Model):
    room_id = models.TextField()
    receipt_type = models.TextField()
    user_id = models.TextField()
    event_ids = models.TextField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'receipts_graph'
        unique_together = (('room_id', 'receipt_type', 'user_id'),)


class ReceiptsLinearized(models.Model):
    stream_id = models.BigIntegerField()
    room_id = models.TextField()
    receipt_type = models.TextField()
    user_id = models.TextField()
    event_id = models.TextField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'receipts_linearized'
        unique_together = (('room_id', 'receipt_type', 'user_id'),)


class ReceivedTransactions(models.Model):
    transaction_id = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    ts = models.BigIntegerField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    response_json = models.BinaryField(blank=True, null=True)
    has_been_referenced = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'received_transactions'
        unique_together = (('transaction_id', 'origin'),)


class Redactions(models.Model):
    event_id = models.TextField(unique=True)
    redacts = models.TextField()

    class Meta:
        managed = False
        db_table = 'redactions'


class Rejections(models.Model):
    event_id = models.TextField(unique=True)
    reason = models.TextField()
    last_check = models.TextField()

    class Meta:
        managed = False
        db_table = 'rejections'


class RemoteMediaCache(models.Model):
    media_origin = models.TextField(blank=True, null=True)
    media_id = models.TextField(blank=True, null=True)
    media_type = models.TextField(blank=True, null=True)
    created_ts = models.BigIntegerField(blank=True, null=True)
    upload_name = models.TextField(blank=True, null=True)
    media_length = models.IntegerField(blank=True, null=True)
    filesystem_id = models.TextField(blank=True, null=True)
    last_access_ts = models.BigIntegerField(blank=True, null=True)
    quarantined_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remote_media_cache'
        unique_together = (('media_origin', 'media_id'),)


class RemoteMediaCacheThumbnails(models.Model):
    media_origin = models.TextField(blank=True, null=True)
    media_id = models.TextField(blank=True, null=True)
    thumbnail_width = models.IntegerField(blank=True, null=True)
    thumbnail_height = models.IntegerField(blank=True, null=True)
    thumbnail_method = models.TextField(blank=True, null=True)
    thumbnail_type = models.TextField(blank=True, null=True)
    thumbnail_length = models.IntegerField(blank=True, null=True)
    filesystem_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remote_media_cache_thumbnails'
        unique_together = (('media_origin', 'media_id', 'thumbnail_width', 'thumbnail_height', 'thumbnail_type'),)


class RemoteProfileCache(models.Model):
    user_id = models.TextField(unique=True)
    displayname = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)
    last_check = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'remote_profile_cache'


class RoomAccountData(models.Model):
    user_id = models.TextField()
    room_id = models.TextField()
    account_data_type = models.TextField()
    stream_id = models.BigIntegerField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_account_data'
        unique_together = (('user_id', 'room_id', 'account_data_type'),)


class RoomAliasServers(models.Model):
    room_alias = models.TextField()
    server = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_alias_servers'


class RoomAliases(models.Model):
    room_alias = models.TextField(unique=True)
    room_id = models.TextField()
    creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_aliases'


class RoomDepth(models.Model):
    room_id = models.TextField(unique=True)
    min_depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_depth'


class RoomHosts(models.Model):
    room_id = models.TextField()
    host = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_hosts'
        unique_together = (('room_id', 'host'),)


class RoomMemberships(models.Model):
    event_id = models.TextField(unique=True)
    user_id = models.TextField()
    sender = models.TextField()
    room_id = models.TextField()
    membership = models.TextField()
    forgotten = models.IntegerField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_memberships'


class RoomNames(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_names'


class RoomTags(models.Model):
    user_id = models.TextField()
    room_id = models.TextField()
    tag = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_tags'
        unique_together = (('user_id', 'room_id', 'tag'),)


class RoomTagsRevisions(models.Model):
    user_id = models.TextField()
    room_id = models.TextField()
    stream_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'room_tags_revisions'
        unique_together = (('user_id', 'room_id'),)


class Rooms(models.Model):
    room_id = models.TextField(primary_key=True)
    is_public = models.NullBooleanField()
    creator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class SchemaVersion(models.Model):
    lock = models.CharField(unique=True, max_length=1)
    version = models.IntegerField()
    upgraded = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_version'


class SentTransactions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    transaction_id = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    response_code = models.IntegerField(blank=True, null=True)
    response_json = models.TextField(blank=True, null=True)
    ts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sent_transactions'


class ServerKeysJson(models.Model):
    server_name = models.TextField()
    key_id = models.TextField()
    from_server = models.TextField()
    ts_added_ms = models.BigIntegerField()
    ts_valid_until_ms = models.BigIntegerField()
    key_json = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'server_keys_json'
        unique_together = (('server_name', 'key_id', 'from_server'),)


class ServerSignatureKeys(models.Model):
    server_name = models.TextField(blank=True, null=True)
    key_id = models.TextField(blank=True, null=True)
    from_server = models.TextField(blank=True, null=True)
    ts_added_ms = models.BigIntegerField(blank=True, null=True)
    verify_key = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_signature_keys'
        unique_together = (('server_name', 'key_id'),)


class ServerTlsCertificates(models.Model):
    server_name = models.TextField(blank=True, null=True)
    fingerprint = models.TextField(blank=True, null=True)
    from_server = models.TextField(blank=True, null=True)
    ts_added_ms = models.BigIntegerField(blank=True, null=True)
    tls_certificate = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_tls_certificates'
        unique_together = (('server_name', 'fingerprint'),)


class StateEvents(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    type = models.TextField()
    state_key = models.TextField()
    prev_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_events'


class StateForwardExtremities(models.Model):
    event_id = models.TextField()
    room_id = models.TextField()
    type = models.TextField()
    state_key = models.TextField()

    class Meta:
        managed = False
        db_table = 'state_forward_extremities'
        unique_together = (('event_id', 'room_id'),)


class StateGroupEdges(models.Model):
    state_group = models.BigIntegerField()
    prev_state_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'state_group_edges'


class StateGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    room_id = models.TextField()
    event_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'state_groups'


class StateGroupsState(models.Model):
    state_group = models.BigIntegerField()
    room_id = models.TextField()
    type = models.TextField()
    state_key = models.TextField()
    event_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'state_groups_state'


class StatsReporting(models.Model):
    reported_stream_token = models.IntegerField(blank=True, null=True)
    reported_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats_reporting'


class StreamOrderingToExterm(models.Model):
    stream_ordering = models.BigIntegerField()
    room_id = models.TextField()
    event_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'stream_ordering_to_exterm'


class ThreepidGuestAccessTokens(models.Model):
    medium = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    guest_access_token = models.TextField(blank=True, null=True)
    first_inviter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'threepid_guest_access_tokens'
        unique_together = (('medium', 'address'),)


class Topics(models.Model):
    event_id = models.TextField(unique=True)
    room_id = models.TextField()
    topic = models.TextField()

    class Meta:
        managed = False
        db_table = 'topics'


class TransactionIdToPdu(models.Model):
    transaction_id = models.IntegerField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    pdu_id = models.TextField(blank=True, null=True)
    pdu_origin = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_id_to_pdu'
        unique_together = (('transaction_id', 'destination'),)


class UserDailyVisits(models.Model):
    user_id = models.TextField()
    device_id = models.TextField(blank=True, null=True)
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_daily_visits'


class UserDirectory(models.Model):
    user_id = models.TextField(unique=True)
    room_id = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_directory'


class UserDirectorySearch(models.Model):
    user_id = models.TextField(unique=True)
    vector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user_directory_search'


class UserDirectoryStreamPos(models.Model):
    lock = models.CharField(unique=True, max_length=1)
    stream_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_directory_stream_pos'


class UserFilters(models.Model):
    user_id = models.TextField(blank=True, null=True)
    filter_id = models.BigIntegerField(blank=True, null=True)
    filter_json = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_filters'


class UserIps(models.Model):
    user_id = models.TextField()
    access_token = models.TextField()
    device_id = models.TextField(blank=True, null=True)
    ip = models.TextField()
    user_agent = models.TextField()
    last_seen = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_ips'


class UserThreepids(models.Model):
    user_id = models.TextField()
    medium = models.TextField()
    address = models.TextField()
    validated_at = models.BigIntegerField()
    added_at = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_threepids'
        unique_together = (('medium', 'address'),)


class Users(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    password_hash = models.TextField(blank=True, null=True)
    creation_ts = models.BigIntegerField(blank=True, null=True)
    admin = models.SmallIntegerField()
    upgrade_ts = models.BigIntegerField(blank=True, null=True)
    is_guest = models.SmallIntegerField()
    appservice_id = models.TextField(blank=True, null=True)
    consent_version = models.TextField(blank=True, null=True)
    consent_server_notice_sent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersInPublicRooms(models.Model):
    user_id = models.TextField(unique=True)
    room_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'users_in_public_rooms'


class UsersPendingDeactivation(models.Model):
    user_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'users_pending_deactivation'


class UsersWhoShareRooms(models.Model):
    user_id = models.TextField()
    other_user_id = models.TextField()
    room_id = models.TextField()
    share_private = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_who_share_rooms'
        unique_together = (('user_id', 'other_user_id'),)

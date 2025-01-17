from controllers.tests.common.test_settings import HOST_NAME
import controllers.common.settings as common_settings

SPEC_FIELD = 'spec'
METADATA_FIELD = 'metadata'
STATUS_FIELD = 'status'
STORAGE_CLASS_DRIVERS_FIELD = 'drivers'
CSI_NODE_NODE_ID_FIELD = 'nodeID'
CSI_PROVISIONER_NAME = 'block.csi.ibm.com'
FAKE_SECRET = 'fake_secret'
FAKE_SECRET_NAMESPACE = 'fake_secret_namespace'
FAKE_NODE_NAME = 'fake_node_name'
FAKE_DAEMON_SET_NAME = 'fake_daemon_set_name'
FAKE_NODE_PODS_NAME = '{}-jdf5g'.format(FAKE_DAEMON_SET_NAME)
FAKE_SECRET_ARRAY = 'management_address'
FAKE_SECRET_PASSWORD = 'fake_password'
FAKE_SECRET_USER_NAME = 'fake_user_name'
FAKE_STORAGE_CLASS = 'fake_storage_class'
IQN = 'iqn.1994-05.com.redhat:686358c930fe'
WWPN = '34859340583048'
NQN = 'nqn.2014-08.org.nvmexpress:uuid:b57708c7-5bb6-46a0-b2af-9d824bf539e1'
FAKE_NODE_ID = '{};;;{}'.format(HOST_NAME, IQN)
FAKE_CSI_PROVISIONER = 'fake_csi_provisioner'
TRUE_STRING = 'true'
NODE_LABELS_FIELD = 'labels'
FAKE_LABEL = 'FAKE_LABEL'
MANAGE_NODE_LABEL = 'hostdefiner.block.csi.ibm.com/manage-node'
FORBID_DELETION_LABEL = 'hostdefiner.block.csi.ibm.com/do-not-delete-definition'
WATCHER_HELPER_PATH = 'controllers.servers.host_definer.watcher.watcher_helper'
NODES_WATCHER_PATH = 'controllers.servers.host_definer.watcher.node_watcher'
SECRET_WATCHER_PATH = 'controllers.servers.host_definer.watcher.secret_watcher'
CSI_NODE_WATCHER_PATH = 'controllers.servers.host_definer.watcher.csi_node_watcher'
STORAGE_CLASS_WATCHER_PATH = 'controllers.servers.host_definer.watcher.storage_class_watcher'
SETTINGS_PATH = 'controllers.servers.host_definer.settings'
METADATA_RESOURCE_VERSION_FIELD = 'resource_version'
FAKE_RESOURCE_VERSION = '495873498573'
FAKE_UID = '50345093486093'
EVENT_TYPE_FIELD = 'type'
EVENT_OBJECT_FIELD = 'object'
KUBERNETES_MANAGER_INIT_FUNCTIONS_TO_PATCH = ['_load_cluster_configuration', '_get_dynamic_client']
UPDATED_PODS = 'updated_number_scheduled'
POD_NODE_NAME_FIELD = 'node_name'
DESIRED_UPDATED_PODS = 'desired_number_scheduled'
DELETED_EVENT_TYPE = 'DELETED'
MODIFIED_EVENT_TYPE = 'MODIFIED'
ADDED_EVENT = 'ADDED'
METADATA_UID_FIELD = 'uid'
STATUS_PHASE_FIELD = 'phase'
READY_PHASE = 'Ready'
HOST_DEFINITION_FIELD = 'hostDefinition'
SECRET_NAME_FIELD = 'secretName'
SECRET_NAMESPACE_FIELD = 'secretNamespace'
HOST_DEFINITION_NODE_NAME_FIELD = 'nodeName'
SECRET_DATA_FIELD = 'data'
FAIL_MESSAGE_FROM_STORAGE = 'fail_from_storage'
PENDING_CREATION_PHASE = 'PendingCreation'
PENDING_DELETION_PHASE = 'PendingDeletion'
SUCCESS_MESSAGE = 'Host defined successfully on the array'
HOST_DEFINITION_PENDING_VARS = {'HOST_DEFINITION_PENDING_RETRIES': 3,
                                'HOST_DEFINITION_PENDING_EXPONENTIAL_BACKOFF_IN_SECONDS': 0.2,
                                'HOST_DEFINITION_PENDING_DELAY_IN_SECONDS': 0.2}
STORAGE_CLASS_PROVISIONER_FIELD = 'provisioner'
STORAGE_CLASS_PARAMETERS_FIELD = 'parameters'
STORAGE_CLASS_SECRET_FIELD = 'csi.storage.k8s.io/secret-name'
STORAGE_CLASS_SECRET_NAMESPACE_FIELD = 'csi.storage.k8s.io/secret-namespace'
FAKE_PREFIX = 'fake-prefix'
IO_GROUP_ID_FIELD = 'id'
IO_GROUP_IDS = ['0', '2']
IO_GROUP_NAMES = ['io_grp0', 'io_grp2']
FAKE_STRING_IO_GROUP = common_settings.IO_GROUP_DELIMITER.join(IO_GROUP_IDS)

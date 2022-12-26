from controllers.common.settings import HOST_DEFINITION_PLURAL, CSI_IBM_GROUP
import controllers.array_action.settings as array_config

STORAGE_API_VERSION = 'storage.k8s.io/v1'
CSI_PARAMETER_PREFIX = "csi.storage.k8s.io/"
CSINODE_KIND = 'CSINode'
CSI_IBM_API_VERSION = 'csi.ibm.com/v1'
HOST_DEFINITION_KIND = 'HostDefinition'
SECRET_NAME_SUFFIX = 'secret-name'
CSI_PROVISIONER_NAME = 'block.csi.ibm.com'
ADDED_EVENT = 'ADDED'
DELETED_EVENT = 'DELETED'
MODIFIED_EVENT = 'MODIFIED'
PENDING_PREFIX = 'Pending'
PENDING_CREATION_PHASE = 'PendingCreation'
PENDING_DELETION_PHASE = 'PendingDeletion'
ERROR_PHASE = 'Error'
READY_PHASE = 'Ready'
DRIVER_PRODUCT_LABEL = 'product=ibm-block-csi-driver'
DEFAULT_NAMESPACE = 'default'
HOST_DEFINER = 'hostDefiner'
MANAGE_NODE_LABEL = 'hostdefiner.block.csi.ibm.com/manage-node'
FORBID_DELETION_LABEL = 'hostdefiner.block.csi.ibm.com/do-not-delete-definition'
CONNECTIVITY_TYPE_LABEL = 'block.csi.ibm.com/connectivity-type'
SUPPORTED_CONNECTIVITY_TYPES = [array_config.ISCSI_CONNECTIVITY_TYPE,
                                array_config.FC_CONNECTIVITY_TYPE, array_config.NVME_OVER_FC_CONNECTIVITY_TYPE]
NODE_NAME_FIELD = 'nodeName'
SECRET_NAME_FIELD = 'secretName'
SECRET_NAMESPACE_FIELD = 'secretNamespace'
CONNECTIVITY_TYPE_FIELD = 'connectivityType'
PORTS_FIELD = 'ports'
NODE_NAME_ON_STORAGE_FIELD = 'nodeNameOnStorage'
IO_GROUP_FIELD = 'ioGroups'
MANAGEMENT_ADDRESS_FIELD = 'managementAddress'
API_VERSION = 'apiVersion'
KIND = 'kind'
METADATA = 'metadata'
SPEC = 'spec'
HOST_DEFINITION_FIELD = 'hostDefinition'
PREFIX_ENV_VAR = 'PREFIX'
CONNECTIVITY_ENV_VAR = 'CONNECTIVITY_TYPE'
STATUS = 'status'
PHASE = 'phase'
LABELS = 'labels'
TRUE_STRING = 'true'
DYNAMIC_NODE_LABELING_ENV_VAR = 'DYNAMIC_NODE_LABELING'
ALLOW_DELETE_ENV_VAR = 'ALLOW_DELETE'
DEFINE_ACTION = 'Define'
UNDEFINE_ACTION = 'Undefine'
SUCCESS_MESSAGE = 'Host defined successfully on the array'
FAILED_MESSAGE_TYPE = 'Failed'
SUCCESSFUL_MESSAGE_TYPE = 'Successful'
NORMAL_EVENT_TYPE = 'Normal'
WARNING_EVENT_TYPE = 'Warning'
FINALIZERS = 'finalizers'
CSI_IBM_FINALIZER = HOST_DEFINITION_PLURAL + '.' + CSI_IBM_GROUP
HOST_DEFINITION_PENDING_RETRIES = 5
HOST_DEFINITION_PENDING_EXPONENTIAL_BACKOFF_IN_SECONDS = 3
HOST_DEFINITION_PENDING_DELAY_IN_SECONDS = 3
SECRET_CONFIG_FIELD = 'config'
TOPOLOGY_PREFIXES = ['topology.block.csi.ibm.com']
POSSIBLE_NUMBER_OF_IO_GROUP = 4

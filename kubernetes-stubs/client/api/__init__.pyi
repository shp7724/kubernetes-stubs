from kubernetes.client.api.admissionregistration_api import \
    AdmissionregistrationApi as AdmissionregistrationApi
from kubernetes.client.api.admissionregistration_v1_api import \
    AdmissionregistrationV1Api as AdmissionregistrationV1Api
from kubernetes.client.api.admissionregistration_v1beta1_api import \
    AdmissionregistrationV1beta1Api as AdmissionregistrationV1beta1Api
from kubernetes.client.api.apiextensions_api import \
    ApiextensionsApi as ApiextensionsApi
from kubernetes.client.api.apiextensions_v1_api import \
    ApiextensionsV1Api as ApiextensionsV1Api
from kubernetes.client.api.apiextensions_v1beta1_api import \
    ApiextensionsV1beta1Api as ApiextensionsV1beta1Api
from kubernetes.client.api.apiregistration_api import \
    ApiregistrationApi as ApiregistrationApi
from kubernetes.client.api.apiregistration_v1_api import \
    ApiregistrationV1Api as ApiregistrationV1Api
from kubernetes.client.api.apiregistration_v1beta1_api import \
    ApiregistrationV1beta1Api as ApiregistrationV1beta1Api
from kubernetes.client.api.apis_api import ApisApi as ApisApi
from kubernetes.client.api.apps_api import AppsApi as AppsApi
from kubernetes.client.api.apps_v1_api import AppsV1Api as AppsV1Api
from kubernetes.client.api.authentication_api import \
    AuthenticationApi as AuthenticationApi
from kubernetes.client.api.authentication_v1_api import \
    AuthenticationV1Api as AuthenticationV1Api
from kubernetes.client.api.authentication_v1beta1_api import \
    AuthenticationV1beta1Api as AuthenticationV1beta1Api
from kubernetes.client.api.authorization_api import \
    AuthorizationApi as AuthorizationApi
from kubernetes.client.api.authorization_v1_api import \
    AuthorizationV1Api as AuthorizationV1Api
from kubernetes.client.api.authorization_v1beta1_api import \
    AuthorizationV1beta1Api as AuthorizationV1beta1Api
from kubernetes.client.api.autoscaling_api import \
    AutoscalingApi as AutoscalingApi
from kubernetes.client.api.autoscaling_v1_api import \
    AutoscalingV1Api as AutoscalingV1Api
from kubernetes.client.api.autoscaling_v2beta1_api import \
    AutoscalingV2beta1Api as AutoscalingV2beta1Api
from kubernetes.client.api.autoscaling_v2beta2_api import \
    AutoscalingV2beta2Api as AutoscalingV2beta2Api
from kubernetes.client.api.batch_api import BatchApi as BatchApi
from kubernetes.client.api.batch_v1_api import BatchV1Api as BatchV1Api
from kubernetes.client.api.batch_v1beta1_api import \
    BatchV1beta1Api as BatchV1beta1Api
from kubernetes.client.api.certificates_api import \
    CertificatesApi as CertificatesApi
from kubernetes.client.api.certificates_v1_api import \
    CertificatesV1Api as CertificatesV1Api
from kubernetes.client.api.certificates_v1beta1_api import \
    CertificatesV1beta1Api as CertificatesV1beta1Api
from kubernetes.client.api.coordination_api import \
    CoordinationApi as CoordinationApi
from kubernetes.client.api.coordination_v1_api import \
    CoordinationV1Api as CoordinationV1Api
from kubernetes.client.api.coordination_v1beta1_api import \
    CoordinationV1beta1Api as CoordinationV1beta1Api
from kubernetes.client.api.core_api import CoreApi as CoreApi
from kubernetes.client.api.core_v1_api import CoreV1Api as CoreV1Api
from kubernetes.client.api.custom_objects_api import \
    CustomObjectsApi as CustomObjectsApi
from kubernetes.client.api.discovery_api import DiscoveryApi as DiscoveryApi
from kubernetes.client.api.discovery_v1_api import \
    DiscoveryV1Api as DiscoveryV1Api
from kubernetes.client.api.discovery_v1beta1_api import \
    DiscoveryV1beta1Api as DiscoveryV1beta1Api
from kubernetes.client.api.events_api import EventsApi as EventsApi
from kubernetes.client.api.events_v1_api import EventsV1Api as EventsV1Api
from kubernetes.client.api.events_v1beta1_api import \
    EventsV1beta1Api as EventsV1beta1Api
from kubernetes.client.api.extensions_api import ExtensionsApi as ExtensionsApi
from kubernetes.client.api.extensions_v1beta1_api import \
    ExtensionsV1beta1Api as ExtensionsV1beta1Api
from kubernetes.client.api.flowcontrolApiserver_api import \
    FlowcontrolApiserverApi as FlowcontrolApiserverApi
from kubernetes.client.api.flowcontrolApiserver_v1beta1_api import \
    FlowcontrolApiserverV1beta1Api as FlowcontrolApiserverV1beta1Api
from kubernetes.client.api.internalApiserver_api import \
    InternalApiserverApi as InternalApiserverApi
from kubernetes.client.api.internalApiserver_v1alpha1_api import \
    InternalApiserverV1alpha1Api as InternalApiserverV1alpha1Api
from kubernetes.client.api.logs_api import LogsApi as LogsApi
from kubernetes.client.api.networking_api import NetworkingApi as NetworkingApi
from kubernetes.client.api.networking_v1_api import \
    NetworkingV1Api as NetworkingV1Api
from kubernetes.client.api.networking_v1beta1_api import \
    NetworkingV1beta1Api as NetworkingV1beta1Api
from kubernetes.client.api.node_api import NodeApi as NodeApi
from kubernetes.client.api.node_v1_api import NodeV1Api as NodeV1Api
from kubernetes.client.api.node_v1alpha1_api import \
    NodeV1alpha1Api as NodeV1alpha1Api
from kubernetes.client.api.node_v1beta1_api import \
    NodeV1beta1Api as NodeV1beta1Api
from kubernetes.client.api.openid_api import OpenidApi as OpenidApi
from kubernetes.client.api.policy_api import PolicyApi as PolicyApi
from kubernetes.client.api.policy_v1_api import PolicyV1Api as PolicyV1Api
from kubernetes.client.api.policy_v1beta1_api import \
    PolicyV1beta1Api as PolicyV1beta1Api
from kubernetes.client.api.rbacAuthorization_api import \
    RbacAuthorizationApi as RbacAuthorizationApi
from kubernetes.client.api.rbacAuthorization_v1_api import \
    RbacAuthorizationV1Api as RbacAuthorizationV1Api
from kubernetes.client.api.rbacAuthorization_v1alpha1_api import \
    RbacAuthorizationV1alpha1Api as RbacAuthorizationV1alpha1Api
from kubernetes.client.api.rbacAuthorization_v1beta1_api import \
    RbacAuthorizationV1beta1Api as RbacAuthorizationV1beta1Api
from kubernetes.client.api.scheduling_api import SchedulingApi as SchedulingApi
from kubernetes.client.api.scheduling_v1_api import \
    SchedulingV1Api as SchedulingV1Api
from kubernetes.client.api.scheduling_v1alpha1_api import \
    SchedulingV1alpha1Api as SchedulingV1alpha1Api
from kubernetes.client.api.scheduling_v1beta1_api import \
    SchedulingV1beta1Api as SchedulingV1beta1Api
from kubernetes.client.api.storage_api import StorageApi as StorageApi
from kubernetes.client.api.storage_v1_api import StorageV1Api as StorageV1Api
from kubernetes.client.api.storage_v1alpha1_api import \
    StorageV1alpha1Api as StorageV1alpha1Api
from kubernetes.client.api.storage_v1beta1_api import \
    StorageV1beta1Api as StorageV1beta1Api
from kubernetes.client.api.version_api import VersionApi as VersionApi
from kubernetes.client.api.WellKnown_api import WellKnownApi as WellKnownApi

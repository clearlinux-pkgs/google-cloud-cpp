#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
Name     : google-cloud-cpp
Version  : 2.38.0
Release  : 13
URL      : https://github.com/googleapis/google-cloud-cpp/archive/v2.38.0/google-cloud-cpp-2.38.0.tar.gz
Source0  : https://github.com/googleapis/google-cloud-cpp/archive/v2.38.0/google-cloud-cpp-2.38.0.tar.gz
Source1  : https://github.com/googleapis/googleapis/archive/6a474b31c53cc1797710206824a17b364a835d2d.tar.gz
Summary  : @GOOGLE_CLOUD_CPP_PC_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0
Requires: google-cloud-cpp-lib = %{version}-%{release}
Requires: google-cloud-cpp-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : fmt-dev
BuildRequires : glibc-dev
BuildRequires : google-crc32c-dev
BuildRequires : googletest-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(benchmark)
BuildRequires : pkgconfig(grpc)
BuildRequires : pkgconfig(nlohmann_json)
BuildRequires : pkgconfig(systemd)
BuildRequires : protobuf-dev
BuildRequires : pugixml-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Google Cloud Platform C++ Client Libraries
<!-- This file is automatically generated by ci/test-markdown/generate-readme.sh -->

%package dev
Summary: dev components for the google-cloud-cpp package.
Group: Development
Requires: google-cloud-cpp-lib = %{version}-%{release}
Provides: google-cloud-cpp-devel = %{version}-%{release}
Requires: google-cloud-cpp = %{version}-%{release}

%description dev
dev components for the google-cloud-cpp package.


%package lib
Summary: lib components for the google-cloud-cpp package.
Group: Libraries
Requires: google-cloud-cpp-license = %{version}-%{release}

%description lib
lib components for the google-cloud-cpp package.


%package license
Summary: license components for the google-cloud-cpp package.
Group: Default

%description license
license components for the google-cloud-cpp package.


%prep
%setup -q -n google-cloud-cpp-2.38.0
cd %{_builddir}
tar xf %{_sourcedir}/6a474b31c53cc1797710206824a17b364a835d2d.tar.gz
cd %{_builddir}/google-cloud-cpp-2.38.0
mkdir -p external/googleapis
cp -r %{_builddir}/googleapis-6a474b31c53cc1797710206824a17b364a835d2d/. %{_builddir}/google-cloud-cpp-2.38.0/external/googleapis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749569164
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DBUILD_TESTING=OFF \
-DGOOGLE_CLOUD_CPP_ENABLE=storage \
-DGOOGLE_CLOUD_CPP_ENABLE_EXAMPLES=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749569164
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-cloud-cpp
cp %{_builddir}/google-cloud-cpp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/google-cloud-cpp/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/googleapis-6a474b31c53cc1797710206824a17b364a835d2d/LICENSE %{buildroot}/usr/share/package-licenses/google-cloud-cpp/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/google/cloud/access_token.h
/usr/include/google/cloud/backoff_policy.h
/usr/include/google/cloud/common_options.h
/usr/include/google/cloud/credentials.h
/usr/include/google/cloud/experimental_tag.h
/usr/include/google/cloud/future.h
/usr/include/google/cloud/future_generic.h
/usr/include/google/cloud/future_void.h
/usr/include/google/cloud/idempotency.h
/usr/include/google/cloud/internal/absl_str_cat_quiet.h
/usr/include/google/cloud/internal/absl_str_join_quiet.h
/usr/include/google/cloud/internal/absl_str_replace_quiet.h
/usr/include/google/cloud/internal/algorithm.h
/usr/include/google/cloud/internal/api_client_header.h
/usr/include/google/cloud/internal/attributes.h
/usr/include/google/cloud/internal/auth_header_error.h
/usr/include/google/cloud/internal/backoff_policy.h
/usr/include/google/cloud/internal/base64_transforms.h
/usr/include/google/cloud/internal/big_endian.h
/usr/include/google/cloud/internal/binary_data_as_debug_string.h
/usr/include/google/cloud/internal/build_info.h
/usr/include/google/cloud/internal/call_context.h
/usr/include/google/cloud/internal/clock.h
/usr/include/google/cloud/internal/compiler_info.h
/usr/include/google/cloud/internal/compute_engine_util.h
/usr/include/google/cloud/internal/credentials_impl.h
/usr/include/google/cloud/internal/curl_handle.h
/usr/include/google/cloud/internal/curl_handle_factory.h
/usr/include/google/cloud/internal/curl_http_payload.h
/usr/include/google/cloud/internal/curl_impl.h
/usr/include/google/cloud/internal/curl_options.h
/usr/include/google/cloud/internal/curl_rest_client.h
/usr/include/google/cloud/internal/curl_rest_response.h
/usr/include/google/cloud/internal/curl_wrappers.h
/usr/include/google/cloud/internal/curl_writev.h
/usr/include/google/cloud/internal/debug_future_status.h
/usr/include/google/cloud/internal/debug_string.h
/usr/include/google/cloud/internal/detect_gcp.h
/usr/include/google/cloud/internal/detect_gcp_impl.h
/usr/include/google/cloud/internal/diagnostics_pop.inc
/usr/include/google/cloud/internal/diagnostics_push.inc
/usr/include/google/cloud/internal/disable_deprecation_warnings.inc
/usr/include/google/cloud/internal/disable_msvc_crt_secure_warnings.inc
/usr/include/google/cloud/internal/error_context.h
/usr/include/google/cloud/internal/external_account_source_format.h
/usr/include/google/cloud/internal/external_account_token_source_aws.h
/usr/include/google/cloud/internal/external_account_token_source_file.h
/usr/include/google/cloud/internal/external_account_token_source_url.h
/usr/include/google/cloud/internal/filesystem.h
/usr/include/google/cloud/internal/format_time_point.h
/usr/include/google/cloud/internal/future_base.h
/usr/include/google/cloud/internal/future_coroutines.h
/usr/include/google/cloud/internal/future_fwd.h
/usr/include/google/cloud/internal/future_impl.h
/usr/include/google/cloud/internal/future_then_impl.h
/usr/include/google/cloud/internal/getenv.h
/usr/include/google/cloud/internal/group_options.h
/usr/include/google/cloud/internal/http_header.h
/usr/include/google/cloud/internal/http_payload.h
/usr/include/google/cloud/internal/invocation_id_generator.h
/usr/include/google/cloud/internal/invoke_result.h
/usr/include/google/cloud/internal/ios_flags_saver.h
/usr/include/google/cloud/internal/json_parsing.h
/usr/include/google/cloud/internal/log_impl.h
/usr/include/google/cloud/internal/make_jwt_assertion.h
/usr/include/google/cloud/internal/make_status.h
/usr/include/google/cloud/internal/noexcept_action.h
/usr/include/google/cloud/internal/non_constructible.h
/usr/include/google/cloud/internal/oauth2_access_token_credentials.h
/usr/include/google/cloud/internal/oauth2_anonymous_credentials.h
/usr/include/google/cloud/internal/oauth2_api_key_credentials.h
/usr/include/google/cloud/internal/oauth2_authorized_user_credentials.h
/usr/include/google/cloud/internal/oauth2_cached_credentials.h
/usr/include/google/cloud/internal/oauth2_compute_engine_credentials.h
/usr/include/google/cloud/internal/oauth2_credential_constants.h
/usr/include/google/cloud/internal/oauth2_credentials.h
/usr/include/google/cloud/internal/oauth2_decorate_credentials.h
/usr/include/google/cloud/internal/oauth2_error_credentials.h
/usr/include/google/cloud/internal/oauth2_external_account_credentials.h
/usr/include/google/cloud/internal/oauth2_external_account_token_source.h
/usr/include/google/cloud/internal/oauth2_google_application_default_credentials_file.h
/usr/include/google/cloud/internal/oauth2_google_credentials.h
/usr/include/google/cloud/internal/oauth2_http_client_factory.h
/usr/include/google/cloud/internal/oauth2_impersonate_service_account_credentials.h
/usr/include/google/cloud/internal/oauth2_logging_credentials.h
/usr/include/google/cloud/internal/oauth2_minimal_iam_credentials_rest.h
/usr/include/google/cloud/internal/oauth2_refreshing_credentials_wrapper.h
/usr/include/google/cloud/internal/oauth2_service_account_credentials.h
/usr/include/google/cloud/internal/oauth2_universe_domain.h
/usr/include/google/cloud/internal/opentelemetry.h
/usr/include/google/cloud/internal/opentelemetry_context.h
/usr/include/google/cloud/internal/pagination_range.h
/usr/include/google/cloud/internal/parse_rfc3339.h
/usr/include/google/cloud/internal/parse_service_account_p12_file.h
/usr/include/google/cloud/internal/populate_common_options.h
/usr/include/google/cloud/internal/populate_rest_options.h
/usr/include/google/cloud/internal/port_platform.h
/usr/include/google/cloud/internal/random.h
/usr/include/google/cloud/internal/rest_carrier.h
/usr/include/google/cloud/internal/rest_client.h
/usr/include/google/cloud/internal/rest_context.h
/usr/include/google/cloud/internal/rest_lro_helpers.h
/usr/include/google/cloud/internal/rest_opentelemetry.h
/usr/include/google/cloud/internal/rest_options.h
/usr/include/google/cloud/internal/rest_parse_json_error.h
/usr/include/google/cloud/internal/rest_request.h
/usr/include/google/cloud/internal/rest_response.h
/usr/include/google/cloud/internal/rest_retry_loop.h
/usr/include/google/cloud/internal/rest_set_metadata.h
/usr/include/google/cloud/internal/retry_info.h
/usr/include/google/cloud/internal/retry_loop_helpers.h
/usr/include/google/cloud/internal/retry_policy_impl.h
/usr/include/google/cloud/internal/service_endpoint.h
/usr/include/google/cloud/internal/sha256_hash.h
/usr/include/google/cloud/internal/sha256_hmac.h
/usr/include/google/cloud/internal/sha256_type.h
/usr/include/google/cloud/internal/sign_using_sha256.h
/usr/include/google/cloud/internal/status_payload_keys.h
/usr/include/google/cloud/internal/status_utils.h
/usr/include/google/cloud/internal/strerror.h
/usr/include/google/cloud/internal/subject_token.h
/usr/include/google/cloud/internal/throw_delegate.h
/usr/include/google/cloud/internal/timer_queue.h
/usr/include/google/cloud/internal/trace_propagator.h
/usr/include/google/cloud/internal/traced_stream_range.h
/usr/include/google/cloud/internal/tracing_http_payload.h
/usr/include/google/cloud/internal/tracing_rest_client.h
/usr/include/google/cloud/internal/tracing_rest_response.h
/usr/include/google/cloud/internal/tuple.h
/usr/include/google/cloud/internal/type_list.h
/usr/include/google/cloud/internal/type_traits.h
/usr/include/google/cloud/internal/unified_rest_credentials.h
/usr/include/google/cloud/internal/url_encode.h
/usr/include/google/cloud/internal/user_agent_prefix.h
/usr/include/google/cloud/internal/utility.h
/usr/include/google/cloud/internal/version_info.h
/usr/include/google/cloud/internal/win32/win32_helpers.h
/usr/include/google/cloud/kms_key_name.h
/usr/include/google/cloud/location.h
/usr/include/google/cloud/log.h
/usr/include/google/cloud/mocks/current_options.h
/usr/include/google/cloud/mocks/mock_async_streaming_read_write_rpc.h
/usr/include/google/cloud/mocks/mock_stream_range.h
/usr/include/google/cloud/no_await_tag.h
/usr/include/google/cloud/opentelemetry_options.h
/usr/include/google/cloud/optional.h
/usr/include/google/cloud/options.h
/usr/include/google/cloud/polling_policy.h
/usr/include/google/cloud/project.h
/usr/include/google/cloud/rest_options.h
/usr/include/google/cloud/retry_policy.h
/usr/include/google/cloud/rpc_metadata.h
/usr/include/google/cloud/ssl_certificate.h
/usr/include/google/cloud/status.h
/usr/include/google/cloud/status_or.h
/usr/include/google/cloud/storage/auto_finalize.h
/usr/include/google/cloud/storage/bucket_access_control.h
/usr/include/google/cloud/storage/bucket_autoclass.h
/usr/include/google/cloud/storage/bucket_billing.h
/usr/include/google/cloud/storage/bucket_cors_entry.h
/usr/include/google/cloud/storage/bucket_custom_placement_config.h
/usr/include/google/cloud/storage/bucket_encryption.h
/usr/include/google/cloud/storage/bucket_hierarchical_namespace.h
/usr/include/google/cloud/storage/bucket_iam_configuration.h
/usr/include/google/cloud/storage/bucket_lifecycle.h
/usr/include/google/cloud/storage/bucket_logging.h
/usr/include/google/cloud/storage/bucket_metadata.h
/usr/include/google/cloud/storage/bucket_object_retention.h
/usr/include/google/cloud/storage/bucket_retention_policy.h
/usr/include/google/cloud/storage/bucket_rpo.h
/usr/include/google/cloud/storage/bucket_soft_delete_policy.h
/usr/include/google/cloud/storage/bucket_versioning.h
/usr/include/google/cloud/storage/bucket_website.h
/usr/include/google/cloud/storage/client.h
/usr/include/google/cloud/storage/client_options.h
/usr/include/google/cloud/storage/download_options.h
/usr/include/google/cloud/storage/enable_object_retention.h
/usr/include/google/cloud/storage/hash_mismatch_error.h
/usr/include/google/cloud/storage/hashing_options.h
/usr/include/google/cloud/storage/headers_map.h
/usr/include/google/cloud/storage/hmac_key_metadata.h
/usr/include/google/cloud/storage/iam_policy.h
/usr/include/google/cloud/storage/idempotency_policy.h
/usr/include/google/cloud/storage/include_folders_as_prefixes.h
/usr/include/google/cloud/storage/internal/access_control_common.h
/usr/include/google/cloud/storage/internal/access_control_common_parser.h
/usr/include/google/cloud/storage/internal/access_token_credentials.h
/usr/include/google/cloud/storage/internal/base64.h
/usr/include/google/cloud/storage/internal/binary_data_as_debug_string.h
/usr/include/google/cloud/storage/internal/bucket_access_control_parser.h
/usr/include/google/cloud/storage/internal/bucket_acl_requests.h
/usr/include/google/cloud/storage/internal/bucket_metadata_parser.h
/usr/include/google/cloud/storage/internal/bucket_requests.h
/usr/include/google/cloud/storage/internal/common_metadata.h
/usr/include/google/cloud/storage/internal/common_metadata_parser.h
/usr/include/google/cloud/storage/internal/complex_option.h
/usr/include/google/cloud/storage/internal/compute_engine_util.h
/usr/include/google/cloud/storage/internal/connection_factory.h
/usr/include/google/cloud/storage/internal/connection_impl.h
/usr/include/google/cloud/storage/internal/const_buffer.h
/usr/include/google/cloud/storage/internal/crc32c.h
/usr/include/google/cloud/storage/internal/curl/request.h
/usr/include/google/cloud/storage/internal/curl/request_builder.h
/usr/include/google/cloud/storage/internal/default_object_acl_requests.h
/usr/include/google/cloud/storage/internal/empty_response.h
/usr/include/google/cloud/storage/internal/error_credentials.h
/usr/include/google/cloud/storage/internal/generate_message_boundary.h
/usr/include/google/cloud/storage/internal/generic_object_request.h
/usr/include/google/cloud/storage/internal/generic_request.h
/usr/include/google/cloud/storage/internal/generic_stub.h
/usr/include/google/cloud/storage/internal/generic_stub_adapter.h
/usr/include/google/cloud/storage/internal/generic_stub_factory.h
/usr/include/google/cloud/storage/internal/hash_function.h
/usr/include/google/cloud/storage/internal/hash_function_impl.h
/usr/include/google/cloud/storage/internal/hash_validator.h
/usr/include/google/cloud/storage/internal/hash_validator_impl.h
/usr/include/google/cloud/storage/internal/hash_values.h
/usr/include/google/cloud/storage/internal/hmac_key_metadata_parser.h
/usr/include/google/cloud/storage/internal/hmac_key_requests.h
/usr/include/google/cloud/storage/internal/http_response.h
/usr/include/google/cloud/storage/internal/impersonate_service_account_credentials.h
/usr/include/google/cloud/storage/internal/lifecycle_rule_parser.h
/usr/include/google/cloud/storage/internal/logging_stub.h
/usr/include/google/cloud/storage/internal/make_jwt_assertion.h
/usr/include/google/cloud/storage/internal/md5hash.h
/usr/include/google/cloud/storage/internal/metadata_parser.h
/usr/include/google/cloud/storage/internal/notification_metadata_parser.h
/usr/include/google/cloud/storage/internal/notification_requests.h
/usr/include/google/cloud/storage/internal/object_access_control_parser.h
/usr/include/google/cloud/storage/internal/object_acl_requests.h
/usr/include/google/cloud/storage/internal/object_metadata_parser.h
/usr/include/google/cloud/storage/internal/object_read_source.h
/usr/include/google/cloud/storage/internal/object_read_streambuf.h
/usr/include/google/cloud/storage/internal/object_requests.h
/usr/include/google/cloud/storage/internal/object_write_streambuf.h
/usr/include/google/cloud/storage/internal/patch_builder.h
/usr/include/google/cloud/storage/internal/patch_builder_details.h
/usr/include/google/cloud/storage/internal/policy_document_request.h
/usr/include/google/cloud/storage/internal/request_project_id.h
/usr/include/google/cloud/storage/internal/rest/object_read_source.h
/usr/include/google/cloud/storage/internal/rest/request_builder.h
/usr/include/google/cloud/storage/internal/rest/stub.h
/usr/include/google/cloud/storage/internal/retry_object_read_source.h
/usr/include/google/cloud/storage/internal/service_account_parser.h
/usr/include/google/cloud/storage/internal/service_account_requests.h
/usr/include/google/cloud/storage/internal/sign_blob_requests.h
/usr/include/google/cloud/storage/internal/signed_url_requests.h
/usr/include/google/cloud/storage/internal/storage_connection.h
/usr/include/google/cloud/storage/internal/tracing_connection.h
/usr/include/google/cloud/storage/internal/tracing_object_read_source.h
/usr/include/google/cloud/storage/internal/tuple_filter.h
/usr/include/google/cloud/storage/internal/unified_rest_credentials.h
/usr/include/google/cloud/storage/internal/well_known_parameters_impl.h
/usr/include/google/cloud/storage/lifecycle_rule.h
/usr/include/google/cloud/storage/list_buckets_reader.h
/usr/include/google/cloud/storage/list_hmac_keys_reader.h
/usr/include/google/cloud/storage/list_objects_and_prefixes_reader.h
/usr/include/google/cloud/storage/list_objects_reader.h
/usr/include/google/cloud/storage/notification_event_type.h
/usr/include/google/cloud/storage/notification_metadata.h
/usr/include/google/cloud/storage/notification_payload_format.h
/usr/include/google/cloud/storage/oauth2/anonymous_credentials.h
/usr/include/google/cloud/storage/oauth2/authorized_user_credentials.h
/usr/include/google/cloud/storage/oauth2/compute_engine_credentials.h
/usr/include/google/cloud/storage/oauth2/credential_constants.h
/usr/include/google/cloud/storage/oauth2/credentials.h
/usr/include/google/cloud/storage/oauth2/google_application_default_credentials_file.h
/usr/include/google/cloud/storage/oauth2/google_credentials.h
/usr/include/google/cloud/storage/oauth2/refreshing_credentials_wrapper.h
/usr/include/google/cloud/storage/oauth2/service_account_credentials.h
/usr/include/google/cloud/storage/object_access_control.h
/usr/include/google/cloud/storage/object_metadata.h
/usr/include/google/cloud/storage/object_read_stream.h
/usr/include/google/cloud/storage/object_retention.h
/usr/include/google/cloud/storage/object_rewriter.h
/usr/include/google/cloud/storage/object_stream.h
/usr/include/google/cloud/storage/object_write_stream.h
/usr/include/google/cloud/storage/options.h
/usr/include/google/cloud/storage/override_default_project.h
/usr/include/google/cloud/storage/override_unlocked_retention.h
/usr/include/google/cloud/storage/owner.h
/usr/include/google/cloud/storage/parallel_upload.h
/usr/include/google/cloud/storage/policy_document.h
/usr/include/google/cloud/storage/project_team.h
/usr/include/google/cloud/storage/retry_policy.h
/usr/include/google/cloud/storage/service_account.h
/usr/include/google/cloud/storage/signed_url_options.h
/usr/include/google/cloud/storage/soft_deleted.h
/usr/include/google/cloud/storage/storage_class.h
/usr/include/google/cloud/storage/testing/mock_client.h
/usr/include/google/cloud/storage/upload_options.h
/usr/include/google/cloud/storage/user_ip_option.h
/usr/include/google/cloud/storage/version.h
/usr/include/google/cloud/storage/version_info.h
/usr/include/google/cloud/storage/well_known_headers.h
/usr/include/google/cloud/storage/well_known_parameters.h
/usr/include/google/cloud/stream_range.h
/usr/include/google/cloud/terminate_handler.h
/usr/include/google/cloud/tracing_options.h
/usr/include/google/cloud/universe_domain_options.h
/usr/include/google/cloud/version.h
/usr/lib64/cmake/google_cloud_cpp_common/google_cloud_cpp_common-config-version.cmake
/usr/lib64/cmake/google_cloud_cpp_common/google_cloud_cpp_common-config.cmake
/usr/lib64/cmake/google_cloud_cpp_common/google_cloud_cpp_common-targets-relwithdebinfo.cmake
/usr/lib64/cmake/google_cloud_cpp_common/google_cloud_cpp_common-targets.cmake
/usr/lib64/cmake/google_cloud_cpp_mocks/google_cloud_cpp_mocks-config-version.cmake
/usr/lib64/cmake/google_cloud_cpp_mocks/google_cloud_cpp_mocks-config.cmake
/usr/lib64/cmake/google_cloud_cpp_mocks/google_cloud_cpp_mocks-targets.cmake
/usr/lib64/cmake/google_cloud_cpp_rest_internal/google_cloud_cpp_rest_internal-config-version.cmake
/usr/lib64/cmake/google_cloud_cpp_rest_internal/google_cloud_cpp_rest_internal-config.cmake
/usr/lib64/cmake/google_cloud_cpp_rest_internal/google_cloud_cpp_rest_internal-targets-relwithdebinfo.cmake
/usr/lib64/cmake/google_cloud_cpp_rest_internal/google_cloud_cpp_rest_internal-targets.cmake
/usr/lib64/cmake/google_cloud_cpp_storage/google_cloud_cpp_storage-config-version.cmake
/usr/lib64/cmake/google_cloud_cpp_storage/google_cloud_cpp_storage-config.cmake
/usr/lib64/cmake/google_cloud_cpp_storage/storage-targets-relwithdebinfo.cmake
/usr/lib64/cmake/google_cloud_cpp_storage/storage-targets.cmake
/usr/lib64/libgoogle_cloud_cpp_common.so
/usr/lib64/libgoogle_cloud_cpp_rest_internal.so
/usr/lib64/libgoogle_cloud_cpp_storage.so
/usr/lib64/pkgconfig/google_cloud_cpp_common.pc
/usr/lib64/pkgconfig/google_cloud_cpp_mocks.pc
/usr/lib64/pkgconfig/google_cloud_cpp_rest_internal.pc
/usr/lib64/pkgconfig/google_cloud_cpp_storage.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgoogle_cloud_cpp_common.so.2
/usr/lib64/libgoogle_cloud_cpp_common.so.2.38.0
/usr/lib64/libgoogle_cloud_cpp_rest_internal.so.2
/usr/lib64/libgoogle_cloud_cpp_rest_internal.so.2.38.0
/usr/lib64/libgoogle_cloud_cpp_storage.so.2
/usr/lib64/libgoogle_cloud_cpp_storage.so.2.38.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-cloud-cpp/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

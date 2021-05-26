# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class MediaJobState(str, Enum):

    canceled = "Canceled"  #: The job was canceled. This is a final state for the job.
    canceling = "Canceling"  #: The job is in the process of being canceled. This is a transient state for the job.
    error = "Error"  #: The job has encountered an error. This is a final state for the job.
    finished = "Finished"  #: The job is finished. This is a final state for the job.
    processing = "Processing"  #: The job is processing. This is a transient state for the job.
    queued = "Queued"  #: The job is in a queued state, waiting for resources to become available. This is a transient state.
    scheduled = "Scheduled"  #: The job is being scheduled to run on an available resource. This is a transient state, between queued and processing states.


class MediaJobErrorCode(str, Enum):

    service_error = "ServiceError"  #: Fatal service error, please contact support.
    service_transient_error = "ServiceTransientError"  #: Transient error, please retry, if retry is unsuccessful, please contact support.
    download_not_accessible = "DownloadNotAccessible"  #: While trying to download the input files, the files were not accessible, please check the availability of the source.
    download_transient_error = "DownloadTransientError"  #: While trying to download the input files, there was an issue during transfer (storage service, network errors), see details and check your source.
    upload_not_accessible = "UploadNotAccessible"  #: While trying to upload the output files, the destination was not reachable, please check the availability of the destination.
    upload_transient_error = "UploadTransientError"  #: While trying to upload the output files, there was an issue during transfer (storage service, network errors), see details and check your destination.
    configuration_unsupported = "ConfigurationUnsupported"  #: There was a problem with the combination of input files and the configuration settings applied, fix the configuration settings and retry with the same input, or change input to match the configuration.
    content_malformed = "ContentMalformed"  #: There was a problem with the input content (for example: zero byte files, or corrupt/non-decodable files), check the input files.
    content_unsupported = "ContentUnsupported"  #: There was a problem with the format of the input (not valid media file, or an unsupported file/codec), check the validity of the input files.


class MediaJobErrorCategory(str, Enum):

    service = "Service"  #: The error is service related.
    download = "Download"  #: The error is download related.
    upload = "Upload"  #: The error is upload related.
    configuration = "Configuration"  #: The error is configuration related.
    content = "Content"  #: The error is related to data in the input files.


class MediaJobRetry(str, Enum):

    do_not_retry = "DoNotRetry"  #: Issue needs to be investigated and then the job resubmitted with corrections or retried once the underlying issue has been corrected.
    may_retry = "MayRetry"  #: Issue may be resolved after waiting for a period of time and resubmitting the same Job.
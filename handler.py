import boto3


def update_threat_intel_sets_by_region(aws_region):
    client = boto3.client('guardduty', region_name=aws_region)
    detector_dict = client.list_detectors()
    detector_ids = []
    if detector_dict['DetectorIds']:
        detector_ids = detector_dict['DetectorIds']

    for detector_id in detector_ids:
        ti_list_dict = client.list_threat_intel_sets(
            DetectorId=detector_id
        )
        if ti_list_dict[u'ThreatIntelSetIds']:
            for ti_id in ti_list_dict[u'ThreatIntelSetIds']:
                ti_dict = client.get_threat_intel_set(
                    DetectorId=detector_id,
                    ThreatIntelSetId=ti_id
                )
                status = ti_dict[u'Status']
                # we only want to update ACTIVE lists
                if status != 'ACTIVE':
                    continue
                print('updating %s %s' % (detector_id, ti_id))
                # update the list
                client.update_threat_intel_set(
                    DetectorId=detector_id,
                    ThreatIntelSetId=ti_id
                )


def update_threat_intel_sets(event, context):
    boto3_session = boto3.session.Session()
    # iterate over all guard duty regions
    guardduty_regions = boto3_session.get_available_regions('guardduty')
    for aws_region in guardduty_regions:
        update_threat_intel_sets_by_region(aws_region)

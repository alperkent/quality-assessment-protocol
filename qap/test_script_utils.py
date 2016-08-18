
import pytest

# for - qap_aws_s3_dict_generator.py

# site_1
# 0026005 - 3 sessions, 1 anat and 2 func each
# 0026006 - 3 sessions, first two have 1 anat and 2 func each, third has
#                       1 anat and no func
# site_2
# 0033005 - 2 sessions, 1 anat and 2 func each
nonBIDS_s3_list = [
 'data/RawData/site_1/0026005/session_1/anat_1/anat.nii.gz',
 'data/RawData/site_1/0026005/session_1/dti_1/dti.bval',
 'data/RawData/site_1/0026005/session_1/dti_1/dti.bvec',
 'data/RawData/site_1/0026005/session_1/dti_1/dti.nii.gz',
 'data/RawData/site_1/0026005/session_1/rest_1/rest.nii.gz',
 'data/RawData/site_1/0026005/session_1/rest_2/rest.nii.gz',
 'data/RawData/site_1/0026005/session_2/anat_1/anat.nii.gz',
 'data/RawData/site_1/0026005/session_2/dti_1/dti.bval',
 'data/RawData/site_1/0026005/session_2/dti_1/dti.bvec',
 'data/RawData/site_1/0026005/session_2/dti_1/dti.nii.gz',
 'data/RawData/site_1/0026005/session_2/rest_1/rest.nii.gz',
 'data/RawData/site_1/0026005/session_2/rest_2/rest.nii.gz',
 'data/RawData/site_1/0026005/session_3/anat_1/anat.nii.gz',
 'data/RawData/site_1/0026005/session_3/dti_1/dti.bval',
 'data/RawData/site_1/0026005/session_3/dti_1/dti.bvec',
 'data/RawData/site_1/0026005/session_3/dti_1/dti.nii.gz',
 'data/RawData/site_1/0026005/session_3/rest_1/rest.nii.gz',
 'data/RawData/site_1/0026005/session_3/rest_2/rest.nii.gz',
 'data/RawData/site_1/0026006/session_1/anat_1/anat.nii.gz',
 'data/RawData/site_1/0026006/session_1/dti_1/dti.bval',
 'data/RawData/site_1/0026006/session_1/dti_1/dti.bvec',
 'data/RawData/site_1/0026006/session_1/dti_1/dti.nii.gz',
 'data/RawData/site_1/0026006/session_1/rest_1/rest.nii.gz',
 'data/RawData/site_1/0026006/session_1/rest_2/rest.nii.gz',
 'data/RawData/site_1/0026006/session_2/anat_1/anat.nii.gz',
 'data/RawData/site_1/0026006/session_2/dti_1/dti.bval',
 'data/RawData/site_1/0026006/session_2/dti_1/dti.bvec',
 'data/RawData/site_1/0026006/session_2/dti_1/dti.nii.gz',
 'data/RawData/site_1/0026006/session_2/rest_1/rest.nii.gz',
 'data/RawData/site_1/0026006/session_2/rest_2/rest.nii.gz',
 'data/RawData/site_1/0026006/session_3/anat_1/anat.nii.gz',
 'data/RawData/site_2/0033005/session_1/anat_1/anat.nii.gz',
 'data/RawData/site_2/0033005/session_1/dti_1/dti.bval',
 'data/RawData/site_2/0033005/session_1/dti_1/dti.bvec',
 'data/RawData/site_2/0033005/session_1/dti_1/dti.nii.gz',
 'data/RawData/site_2/0033005/session_1/rest_1/rest.nii.gz',
 'data/RawData/site_2/0033005/session_1/rest_2/rest.nii.gz',
 'data/RawData/site_2/0033005/session_2/anat_1/anat.nii.gz',
 'data/RawData/site_2/0033005/session_2/dti_1/dti.bval',
 'data/RawData/site_2/0033005/session_2/dti_1/dti.bvec',
 'data/RawData/site_2/0033005/session_2/dti_1/dti.nii.gz',
 'data/RawData/site_2/0033005/session_2/rest_1/rest.nii.gz',
 'data/RawData/site_2/0033005/session_2/rest_2/rest.nii.gz']

BIDS_s3_list = [
 'data/RawDataBIDS/sub-A0200/ses-A01/anat/sub-A0200_ses-A01_T1w.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/anat/sub-A0200_ses-A01_T1w_brainmask.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/anat/sub-A0200_ses-A01_T1w_skullstripped.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/fmap/sub-A0200_ses-A01_magnitude1.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/fmap/sub-A0200_ses-A01_phasediff.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY1_bold.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY1_events.tsv',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY1_physio.json',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY1_physio.tsv.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY2_bold.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY2_physio.json',
 'data/RawDataBIDS/sub-A0200/ses-A01/func/sub-A0200_ses-A01_task-STUDY2_physio.tsv.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/anat/sub-A0200_ses-A02_T1w.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/anat/sub-A0200_ses-A02_T1w_brainmask.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/anat/sub-A0200_ses-A02_T1w_skullstripped.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/fmap/sub-A0200_ses-A02_magnitude1.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/fmap/sub-A0200_ses-A02_phasediff.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY1_bold.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY1_events.tsv',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY1_physio.json',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY1_physio.tsv.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY2_bold.nii.gz',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY2_physio.json',
 'data/RawDataBIDS/sub-A0200/ses-A02/func/sub-A0200_ses-A02_task-STUDY2_physio.tsv.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/anat/sub-A0300_ses-A01_T1w.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/anat/sub-A0300_ses-A01_T1w_brainmask.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/anat/sub-A0300_ses-A01_T1w_skullstripped.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/fmap/sub-A0300_ses-A01_magnitude1.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/fmap/sub-A0300_ses-A01_phasediff.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY1_bold.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY1_events.tsv',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY1_physio.json',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY1_physio.tsv.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY2_bold.nii.gz',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY2_physio.json',
 'data/RawDataBIDS/sub-A0300/ses-A01/func/sub-A0300_ses-A01_task-STUDY2_physio.tsv.gz']


@pytest.mark.quick
def test_create_subdict_from_s3_list_anat_nonBIDS():

    from qap.script_utils import create_subdict_from_s3_list

    img_type = "anat"
    bucket_prefix = "data/RawData"

    ref_dict = {
        ('0026005', 'session_1', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026005/session_1/anat_1/anat.nii.gz'},
        ('0026005', 'session_2', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026005/session_2/anat_1/anat.nii.gz'},
        ('0026005', 'session_3', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026005/session_3/anat_1/anat.nii.gz'},
        ('0026006', 'session_1', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026006/session_1/anat_1/anat.nii.gz'},
        ('0026006', 'session_2', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026006/session_2/anat_1/anat.nii.gz'},
        ('0026006', 'session_3', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_1/0026006/session_3/anat_1/anat.nii.gz'},
        ('0033005', 'session_1', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_2/0033005/session_1/anat_1/anat.nii.gz'},
        ('0033005', 'session_2', 'anat_1'):
            {'anatomical_scan': 'data/RawData/site_2/0033005/session_2/anat_1/anat.nii.gz'}}

    s3_dict = create_subdict_from_s3_list(nonBIDS_s3_list, img_type,
    	bucket_prefix)

    assert s3_dict == ref_dict


@pytest.mark.quick
def test_create_subdict_from_s3_list_anat_nonBIDS_BIDSdata():
	# todo
	raise Exception


@pytest.mark.quick
def test_create_subdict_from_s3_list_func_nonBIDS():

    from qap.script_utils import create_subdict_from_s3_list

    img_type = "func"
    bucket_prefix = "data/RawData"

    ref_dict = {
        ('0026005', 'session_1', 'rest_1'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_1/rest_1/rest.nii.gz'},
        ('0026005', 'session_1', 'rest_2'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_1/rest_2/rest.nii.gz'},
        ('0026005', 'session_2', 'rest_1'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_2/rest_1/rest.nii.gz'},
        ('0026005', 'session_2', 'rest_2'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_2/rest_2/rest.nii.gz'},
        ('0026005', 'session_3', 'rest_1'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_3/rest_1/rest.nii.gz'},
        ('0026005', 'session_3', 'rest_2'):
            {'functional_scan': 'data/RawData/site_1/0026005/session_3/rest_2/rest.nii.gz'},
        ('0026006', 'session_1', 'rest_1'):
            {'functional_scan': 'data/RawData/site_1/0026006/session_1/rest_1/rest.nii.gz'},
        ('0026006', 'session_1', 'rest_2'):
            {'functional_scan': 'data/RawData/site_1/0026006/session_1/rest_2/rest.nii.gz'},
        ('0026006', 'session_2', 'rest_1'):
            {'functional_scan': 'data/RawData/site_1/0026006/session_2/rest_1/rest.nii.gz'},
        ('0026006', 'session_2', 'rest_2'):
            {'functional_scan': 'data/RawData/site_1/0026006/session_2/rest_2/rest.nii.gz'},
        ('0033005', 'session_1', 'rest_1'):
            {'functional_scan': 'data/RawData/site_2/0033005/session_1/rest_1/rest.nii.gz'},
        ('0033005', 'session_1', 'rest_2'):
            {'functional_scan': 'data/RawData/site_2/0033005/session_1/rest_2/rest.nii.gz'},
        ('0033005', 'session_2', 'rest_1'):
            {'functional_scan': 'data/RawData/site_2/0033005/session_2/rest_1/rest.nii.gz'},
        ('0033005', 'session_2', 'rest_2'):
            {'functional_scan': 'data/RawData/site_2/0033005/session_2/rest_2/rest.nii.gz'}}

    s3_dict = create_subdict_from_s3_list(nonBIDS_s3_list, img_type,
    	bucket_prefix)

    assert s3_dict == ref_dict


@pytest.mark.quick
def test_create_subdict_from_s3_list_anat_BIDS():

    from qap.script_utils import create_subdict_from_s3_list

    img_type = "anat"
    bucket_prefix = "data/RawDataBIDS"

    ref_dict = {
        ('sub-A0200', 'ses-A01', 'T1w'):
            {'anatomical_scan': 'data/RawDataBIDS/sub-A0200/ses-A01/anat/sub-A0200_ses-A01_T1w.nii.gz'},
        ('sub-A0200', 'ses-A02', 'T1w'):
            {'anatomical_scan': 'data/RawDataBIDS/sub-A0200/ses-A02/anat/sub-A0200_ses-A02_T1w.nii.gz'},
        ('sub-A0300', 'ses-A01', 'T1w'):
            {'anatomical_scan': 'data/RawDataBIDS/sub-A0300/ses-A01/anat/sub-A0300_ses-A01_T1w.nii.gz'}
    }

    s3_dict = create_subdict_from_s3_list(BIDS_s3_list, img_type, 
    	bucket_prefix, BIDS=True)

    assert s3_dict == ref_dict


@pytest.mark.quick
def test_create_subdict_from_s3_list_anat_BIDS_nonBIDS_data():

    import pytest
    from qap.script_utils import create_subdict_from_s3_list

    img_type = "anat"
    bucket_prefix = "data/RawData"

    with pytest.raises(Exception) as excinfo:
        s3_dict = create_subdict_from_s3_list(nonBIDS_s3_list, img_type, 
    	    bucket_prefix, BIDS=True)

    assert "dataset provided" in str(excinfo.value)


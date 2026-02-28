"""
utils.py

A utility module for working with DICOM files and networks using pydicom and pynetdicom.

Features:
- Reading DICOM files from disk or pydicom test data
- Displaying DICOM images using matplotlib
- Establishing DICOM associations (C-ECHO)
- Sending DICOM datasets to a remote SCP via C-STORE

Dependencies:
- pydicom
- pynetdicom
- matplotlib
- logging
"""

import logging
import matplotlib.pyplot as plt
#from typing import Optional

from pydicom import dcmread
from pydicom.data import get_testdata_file
from pydicom.dataset import FileDataset
from pynetdicom import AE

logger = logging.getLogger('utils')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


def read_dcm(path: str) -> FileDataset:
    """
    Read a DICOM file from a given path into a pydicom Dataset.

    Parameters
    ----------
    path : str
        The file path to the DICOM file to be read.

    Returns
    -------
    FileDataset
        The DICOM dataset read from the file.
    """
    logger.info("function 'read_dcm' start")
    
    with open(path, 'rb') as file:
        logger.info("dcm file open: " + path)
        ds = dcmread(file)
    
    logger.info("function 'read_dcm' end")
    return ds


def get_testdata(filename: str) -> FileDataset:
    """
    Retrieve a test DICOM file from pydicom's built-in test data and read it.

    Parameters
    ----------
    filename : str
        The filename of the test DICOM file.

    Returns
    -------
    FileDataset
        The DICOM dataset read from the test file.
    """
    logger.info("function 'get_testdata' start")
    
    file = get_testdata_file(filename)
    ds = dcmread(file)
    
    logger.info("function 'get_testdata' end")
    return ds


def plot_ds(ds: FileDataset) -> None:
    """
    Plot the pixel data of a DICOM dataset using matplotlib.

    Parameters
    ----------
    ds : FileDataset
        The DICOM dataset containing pixel data.

    Returns
    -------
    None
    """
    logger.info("function 'plot_ds' start")

    arr = ds.pixel_array
    logger.info("Array shape: " + str(arr.shape))
    logger.info("Array data type: " + str(arr.dtype))

    plt.imshow(arr, cmap="gray")
    plt.show()

    logger.info("function 'plot_ds' end")


# Instantiate the application entity as SCU
ae = AE()


def test_assoc(scp_ip: str, scp_udp_port: int) -> None:
    """
    Test DICOM association (C-ECHO) with a remote SCP server.

    Parameters
    ----------
    scp_ip : str
        IP address of the SCP server.
    scp_udp_port : int
        Port of the SCP server.

    Returns
    -------
    None
    """
    ae.add_requested_context("1.2.840.10008.1.1")

    assoc = ae.associate(scp_ip, scp_udp_port)
    if assoc.is_established:
        logger.info("Association established with SCP!")
        status = assoc.send_c_echo()
        logger.info('Echo request status: 0x{0:04x}'.format(status.Status))
        assoc.release()
    else:
        logger.error("Failed to associate")


def store_ds(scp_ip: str, scp_udp_port: int, ds: FileDataset) -> None:
    """
    Send a DICOM dataset to a remote SCP server using C-STORE.

    Parameters
    ----------
    scp_ip : str
        IP address of the SCP server.
    scp_udp_port : int
        Port of the SCP server.
    ds : FileDataset
        The DICOM dataset to be sent.

    Returns
    -------
    None
    """
    sop_class_uid = ds.SOPClassUID
    ae.add_requested_context(sop_class_uid)

    assoc = ae.associate(scp_ip, scp_udp_port)
    if assoc.is_established:
        status = assoc.send_c_store(ds)
        if status:
            logger.info('C-STORE request status: 0x{0:04x}'.format(status.Status))
        else:
            logger.warning('Connection timed out, was aborted or received invalid response')
        assoc.release()
    else:
        logger.error('Association rejected, aborted or never connected')
import logging
from pydicom import dcmread
import matplotlib.pyplot as plt
from pynetdicom import AE


logger = logging.getLogger('utils')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


def read_dcm(path):
    logger.info("function 'read_dcm' start")
    
    # Open the dcm file and read to dataset
    with open(path, 'rb') as file:
        logger.info("dcm file open: " + path)
        ds = dcmread(file)
    
    logger.info("function 'read_dcm' end")
    return ds


def plot_ds(ds):
    logger.info("function 'plot_ds' start")

    # elem = ds[0x7fe0, 0x0010]
    # logger.debug(elem)
    # raw_pixel_data = elem.value

    # Convert the pixel data to an ndarray
    arr = ds.pixel_array
    logger.debug("Array shape: " + str(arr.shape))
    logger.debug("Array data type: " + str(arr.dtype))

    # Display the ndarray using matplotlib
    plt.imshow(arr, cmap="gray")
    plt.show()

    logger.info("function 'plot_ds' end")


# Instantiate the application entity as SCU
ae = AE()


# TODO: Implement AE with association as a context manager


def test_assoc(scp_ip, scp_udp_port):
    ae.add_requested_context("1.2.840.10008.1.1")

    # Associate with the local Orthanc server as SCP
    assoc = ae.associate(scp_ip, scp_udp_port)
    if assoc.is_established:
        logger.info("Association established with SCP!")
        status = assoc.send_c_echo()
        logger.info('Echo request status: 0x{0:04x}'.format(status.Status))
        assoc.release()
    else:
        # Association rejected, aborted or never connected
        logger.error("Failed to associate")


def store_ds(scp_ip, scp_udp_port, sop_class, ds):
    ae.add_requested_context(sop_class)

    assoc = ae.associate(scp_ip, scp_udp_port)
    if assoc.is_established:
        # Use the C-STORE service to send the dataset
        # returns the response status as a pydicom Dataset
        status = assoc.send_c_store(ds)

        # Check the status of the storage request
        if status:
            # If the storage request succeeded this will be 0x0000
            logger.info('C-STORE request status: 0x{0:04x}'.format(status.Status))
        else:
            logger.warning('Connection timed out, was aborted or received invalid response')

        # Release the association
        assoc.release()
    else:
        logger.error('Association rejected, aborted or never connected')
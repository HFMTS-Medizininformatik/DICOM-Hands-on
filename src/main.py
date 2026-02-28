import logging

from utils import read_dcm, get_testdata, plot_ds, test_assoc, store_ds


# Set up logging configuration
logging.basicConfig(level=logging.INFO)

# Create a logger for the main module
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


def main():
    """
    Main function to demonstrate reading a DICOM file, plotting it, and sending it to a remote SCP server.
    """
    logger.info("function 'main' start")

    # Option 1) Read the dcm file from local folder and get the dataset
    # ==============================
    # dcm_path = './data/image-000001.dcm'
    # ds = read_dcm(dcm_path)
    # logger.info(ds)

    # Option 2) Get the dcm file from pydicom testdata and get the dataset
    # =============================
    dcm_name = 'CT_small.dcm'
    ds = get_testdata(dcm_name)
    logger.info(ds)

    # Check the transfer syntax of the dataset
    tsyntax = ds.file_meta.TransferSyntaxUID
    logger.info("Transfer Syntax UID: " + tsyntax.name)
    logger.info("Is compressed: " + str(tsyntax.is_compressed))

    # Plot the dataset, then the image should be displayed in a pop-up window
    plot_ds(ds)

    # The script will stop here until the plot window is closed.

    # Test the association with the remote SCP server and send the dataset using C-STORE
    scp_ip = "127.0.0.1"
    scp_udp_port = 4242
    test_assoc(scp_ip, scp_udp_port)
    store_ds(scp_ip, scp_udp_port, ds)

    logger.info("function 'main' end")


if __name__ == "__main__":
    """
    Run the main function when the script is executed.
    """
    main()
import logging
from pynetdicom.sop_class import DigitalXRayImageStorageForPresentation

from utils import read_dcm, plot_ds, test_assoc, store_ds


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


def main():
    logger.info("function 'main' start")

    dsm_path = './data/image-000001.dcm'
    ds = read_dcm(dsm_path)
    logger.info(ds)
    """
    Refer to Supported Service Classes:
    - https://pydicom.github.io/pynetdicom/dev/service_classes/index.html
    """

    tsyntax = ds.file_meta.TransferSyntaxUID
    logger.info("Transfer Syntax UID: " + tsyntax.name)
    logger.info("Is compressed: " + str(tsyntax.is_compressed))

    plot_ds(ds)

    scp_ip = "127.0.0.1"
    scp_udp_port = 4242
    test_assoc(scp_ip, scp_udp_port)
    store_ds(scp_ip, scp_udp_port, DigitalXRayImageStorageForPresentation, ds)

    logger.info("function 'main' end")


if __name__ == "__main__":
    main()

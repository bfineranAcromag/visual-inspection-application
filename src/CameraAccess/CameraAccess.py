import imageio, zxingcpp
import visvis as vv

class CameraAccess:
    def __init__(self, img_to_read, serial_number_length):
        self.img_to_read = img_to_read
        self.serial_number_length = serial_number_length
    
    """
    searches image, reads, and returns barcode only if:
        - the barcode read is equal to the length of the serial number requested
    
    returns serial number in type:
        - 'String'
    
    """
    def readBarcodeString(self):
        # note imageio takes a single period shortened dir instead of a double
        img = imageio.imread(self.img_to_read)
        results = zxingcpp.read_barcodes(img)
        
        for result in results:
            if len(result.text) == self.serial_number_length:
                return result.text

        return "No Serial Number Found"

    """

    takes image capture from live webcam (soon to be industrial camera)

    side_of_board: string
        - expected values: "top", "bottom"
    
    isUV: bool
        - true if caputure is taken under UV light for conformal coat inspection
    
    board_serial_num: string
        - board serial number to make the filenames more organized
    """
    def imageCamputure(self, side_of_board, isUV, board_serial_num):
        for frame_count, frame in enumerate(imageio.imiter("<video0>")): 
            
            # find file extension that the camera will save to 
            if isUV:
                imageio.imwrite(f"{board_serial_num}-{side_of_board}-UVLight.jpg", frame)
            else:
                imageio.imwrite(f"{board_serial_num}-{side_of_board}.jpg", frame)

            # this method seems very dependant on frame rate and computer speed, 
            # check at various speeds and see if it holds
            if frame_count > 1: 
                break

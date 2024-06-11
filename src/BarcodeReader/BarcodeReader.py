import imageio, zxingcpp

class BarcodeReader:
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

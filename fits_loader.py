import os
from astropy.io import fits
from astropy.wcs import WCS

class FitsLoader:
    @staticmethod
    def loading_FITS(string_filepath, extension=0):
        try:
            if not os.path.exists(string_filepath):
                raise FileNotFoundError("File does not exist")
            assert isinstance(string_filepath, str), 'Filepath must be a string'
            endings = ['.FIT', '.FITS', '.fit', '.fits']
            assert any(string_filepath.endswith(i) for i in endings), "Must be of type .FIT, .FITS, .fit, .fits"
            with fits.open(string_filepath) as hdu:
                extension_total = len(hdu)
                assert extension < extension_total, 'Extension not in range, the extension value must be less than {}'.format(extension_total)
                header = hdu[extension].header
                data = hdu[extension].data
                wcs = WCS(header)
            return header, data, wcs
        except (AssertionError, ValueError, FileNotFoundError) as msg:
            print(msg)
            return None, None, None

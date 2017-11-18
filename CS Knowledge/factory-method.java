public class ImageReaderFactory{
    public static ImageReader createImageReader(InputStream is){
        // until we read the input stream, we don't know what 
        // type of object to make
        int imageType = getImageType(is);
        switch(imageType){
            // since now we know the types, we can return appropreate object
            case ImageReaderFactory.GIF                
                return new GifReader(is);
            case ImageReaderFactory.JPEG
                return new JpegReader(is);
        }
    }
}